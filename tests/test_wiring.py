#!/usr/bin/env python3
"""Wiring tests: python3 tests/test_wiring.py

Checks that the declarative pieces actually refer to things that exist. The
pipeline graph, the agent files, the skills, the hook registration and the gate
table are separate files that must agree; nothing at runtime notices when they
stop agreeing, which is exactly why this runs in CI-style checks instead.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PASSED: list[str] = []
FAILED: list[str] = []
SKIPPED: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    (PASSED if condition else FAILED).append(name)
    print(f"  {'PASS' if condition else 'FAIL'}  {name}{'  ' + detail if detail and not condition else ''}")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "-", "\t")):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def main() -> int:
    pipeline = json.loads((ROOT / ".claude/workflow/pipeline.json").read_text())
    steps = pipeline["steps"]

    print("\npipeline graph")
    all_steps = set(steps)
    dangling = {d for spec in steps.values() for d in spec.get("depends_on", []) if d not in all_steps}
    check("no dependency on an unknown step", not dangling, str(dangling))

    artifacts = [spec["artifact"] for spec in steps.values() if "artifact" in spec]
    check("every step owns an artifact", len(artifacts) == len(steps))
    check("no two steps own the same artifact", len(artifacts) == len(set(artifacts)))

    # A step must never share a group with something it depends on.
    bad_groups = [
        f"{name} (g{spec['group']}) depends on {dep} (g{steps[dep]['group']})"
        for name, spec in steps.items()
        for dep in spec.get("depends_on", [])
        if steps[dep]["group"] >= spec["group"]
    ]
    check("group numbers respect dependencies", not bad_groups, "; ".join(bad_groups))

    parallel = {g: [n for n, s in steps.items() if s["group"] == g]
                for g in {s["group"] for s in steps.values()}}
    check("at least two parallel groups exist",
          sum(1 for names in parallel.values() if len(names) > 1) >= 2,
          str({g: n for g, n in parallel.items() if len(n) > 1}))

    print("\nagents")
    agent_dir = ROOT / ".claude/agents"
    agent_files = {p.stem: p for p in agent_dir.glob("*.md")}
    check("at least 5 subagents exist", len(agent_files) >= 5, f"found {len(agent_files)}")

    referenced: set[str] = set()
    for spec in steps.values():
        if spec.get("agent"):
            referenced.add(spec["agent"])
        referenced.update(spec.get("agent_choices", []))

    missing = sorted(referenced - set(agent_files))
    check("every agent in the pipeline has a file", not missing, str(missing))
    orphans = sorted(set(agent_files) - referenced)
    check("no orphaned agent files", not orphans, str(orphans))

    for name, path in sorted(agent_files.items()):
        fields = frontmatter(path)
        check(f"{name}: frontmatter name matches filename",
              fields.get("name") == name, f"got {fields.get('name')!r}")
        check(f"{name}: has a description", bool(fields.get("description")))

    print("\nskills")
    skill_dir = ROOT / ".claude/skills"
    skills = {p.name for p in skill_dir.iterdir() if (p / "SKILL.md").is_file()}
    check("at least 2 reusable skills exist", len(skills) >= 2, str(skills))
    for skill in sorted(skills):
        fields = frontmatter(skill_dir / skill / "SKILL.md")
        check(f"{skill}: frontmatter name matches directory",
              fields.get("name") == skill, f"got {fields.get('name')!r}")

    agent_text = "\n".join(p.read_text(encoding="utf-8") for p in agent_files.values())
    for skill in sorted(skills):
        check(f"{skill}: referenced by at least one agent", skill in agent_text)

    print("\nhooks")
    settings = json.loads((ROOT / ".claude/settings.json").read_text())
    hooks = settings.get("hooks", {})
    check("PreToolUse hooks registered", bool(hooks.get("PreToolUse")))
    check("PostToolUse hooks registered", bool(hooks.get("PostToolUse")))

    registered = re.findall(r"hooks/(\w+\.py)", json.dumps(hooks))
    for script in registered:
        check(f"{script}: file exists", (ROOT / ".claude/hooks" / script).is_file())
    on_disk = {p.name for p in (ROOT / ".claude/hooks").glob("*.py")} - {"wfstate.py"}
    check("every hook script is registered", on_disk <= set(registered),
          str(sorted(on_disk - set(registered))))

    print("\ncommands and MCP")
    commands = {p.stem for p in (ROOT / ".claude/commands").glob("*.md")}
    for expected in ("build-learning-path", "resume-learning-path", "approve-learning-path"):
        check(f"/{expected} exists", expected in commands)

    mcp = json.loads((ROOT / ".mcp.json").read_text())["mcpServers"]
    check("at least one MCP server configured", len(mcp) >= 1, str(list(mcp)))
    check("no secrets in .mcp.json",
          not re.search(r"(api[_-]?key|token|secret|password)", json.dumps(mcp), re.I))
    # The venv is a setup step, not a repository artifact, so on a fresh clone its
    # absence is expected rather than broken. Report it as pending setup — a clean
    # checkout should not greet you with failures you are about to fix anyway.
    venv_present = (ROOT / ".venv").is_dir()
    for name, spec in mcp.items():
        if spec["command"].startswith(".") and not venv_present:
            SKIPPED.append(f"mcp {name}: command path")
            print(f"  SETUP mcp {name}: needs the venv — "
                  "python3 -m venv .venv && .venv/bin/pip install -r requirements.txt")
        elif spec["command"].startswith("."):
            check(f"mcp {name}: command path exists", (ROOT / spec["command"]).exists())
        for arg in spec.get("args", []):
            if arg.endswith(".py"):
                check(f"mcp {name}: server script exists", (ROOT / arg).is_file())

    mcp_tools = set(re.findall(r"mcp__(\w+?)__\w+", agent_text))
    check("agents only reference configured MCP servers",
          mcp_tools <= set(mcp), str(sorted(mcp_tools - set(mcp))))

    print("\ngates")
    gates_text = (ROOT / ".claude/workflow/gates.md").read_text()
    gate_ids = set(re.findall(r"\bG(\d)\b", gates_text))
    check("at least 5 gates defined", len(gate_ids) >= 5, str(sorted(gate_ids)))
    owners = set(re.findall(r"`([a-z-]+)`", gates_text)) & all_steps
    check("gate owners are real steps", bool(owners), str(sorted(owners)))

    tail = f", {len(SKIPPED)} pending setup" if SKIPPED else ""
    print(f"\n{len(PASSED)} passed, {len(FAILED)} failed{tail}")
    for name in FAILED:
        print(f"  failed: {name}")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
