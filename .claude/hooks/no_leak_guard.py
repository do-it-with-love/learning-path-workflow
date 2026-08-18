#!/usr/bin/env python3
"""PreToolUse — artifact ownership, artifact structure, and output hygiene.

Three checks on every Write/Edit aimed at a run directory:

1. **Ownership.** A file may only appear under ``artifacts/`` if pipeline.json
   declares a step that owns it, and its frontmatter must name that owner. This is
   what makes "each subagent has explicit artifact ownership" a property of the
   system rather than a promise in a prompt.

2. **Structure.** A full Write of an artifact must satisfy the contract from the
   artifact-validator skill. Enforcing it here is what makes repeated runs on the
   same input structurally identical — the guarantee cannot drift with the prompt.

3. **No leaks.** Learner-facing output must not mention internal artifacts, state
   files, or agent names. The learner asked for a study plan, not a tour of the
   machinery.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wfstate import (  # noqa: E402
    allow,
    artifact_owners,
    deny,
    load_pipeline,
    read_hook_input,
    repo_root,
    split_run_path,
    target_path,
    written_content,
)

REQUIRED_KEYS = ("artifact", "owner", "run_id", "status", "attempt", "inputs", "generated")
REQUIRED_SECTIONS = ("## Summary", "## Findings", "## Sources", "## Open Questions")

# Literals that must never reach a learner-facing document.
LEAK_LITERALS = ("artifacts/", "workflow-state.json", "approval.json", "pipeline.json", ".claude/")

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def frontmatter(text: str) -> dict[str, str] | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if line.startswith((" ", "-", "\t")) or ":" not in line:
            continue  # nested list entries such as inputs:
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def internal_names(pipeline: dict) -> list[str]:
    names: list[str] = []
    for step, spec in pipeline["steps"].items():
        names.append(step)
        names.extend(spec.get("agent_choices", []))
        if spec.get("agent"):
            names.append(spec["agent"])
    # Only multi-word hyphenated names — single words like "validator" or
    # "curator" are ordinary English and would produce constant false positives.
    return sorted({name for name in names if "-" in name})


def main() -> None:
    payload = read_hook_input()
    raw_target = target_path(payload)
    if not raw_target:
        allow()

    split = split_run_path(raw_target)
    if split is None:
        allow()
    _run_dir, rel = split

    try:
        pipeline = load_pipeline(repo_root())
    except (OSError, ValueError):
        allow()  # structural policing is best-effort; the approval gate fails closed

    content = written_content(payload)
    is_full_write = (payload.get("tool_name") == "Write")

    # ---------------------------------------------------------------- ownership
    if rel.startswith("artifacts/"):
        owners = artifact_owners(pipeline)
        if rel not in owners:
            known = "\n  ".join(sorted(owners))
            deny(
                f"'{rel}' is not a registered workflow artifact, so nothing owns it. "
                f"Write one of the declared artifacts instead:\n  {known}\n"
                "If this run genuinely needs a new artifact, add it to "
                ".claude/workflow/pipeline.json first so the dependency graph stays honest."
            )

        if is_full_write and rel.endswith(".md"):
            expected_owner = owners[rel]
            fields = frontmatter(content)
            if fields is None:
                deny(
                    f"'{rel}' must open with the YAML frontmatter block defined in the "
                    "artifact-validator skill. Load that skill and rewrite the file."
                )

            missing = [key for key in REQUIRED_KEYS if key not in fields]
            if missing:
                deny(
                    f"'{rel}' frontmatter is missing: {', '.join(missing)}. "
                    "See the artifact-validator skill for the required shape."
                )

            if fields.get("owner") != expected_owner:
                deny(
                    f"'{rel}' is owned by step '{expected_owner}' but its frontmatter "
                    f"says owner: {fields.get('owner')}. Either you are writing another "
                    "step's artifact — which is not allowed — or the frontmatter is wrong."
                )

            stem = Path(rel).stem
            if fields.get("artifact") != stem:
                deny(f"'{rel}' frontmatter says artifact: {fields.get('artifact')}, "
                     f"but the filename stem is '{stem}'. They must match.")

            positions = [content.find(section) for section in REQUIRED_SECTIONS]
            if any(pos == -1 for pos in positions):
                absent = [s for s, p in zip(REQUIRED_SECTIONS, positions) if p == -1]
                deny(
                    f"'{rel}' is missing required section(s): {', '.join(absent)}. "
                    "All four are mandatory and in order; use 'None.' as the body of a "
                    "section that has nothing to report."
                )
            if positions != sorted(positions):
                deny(
                    f"'{rel}' has its sections out of order. Required order: "
                    f"{' → '.join(REQUIRED_SECTIONS)}."
                )

    # -------------------------------------------------------------------- leaks
    if rel.startswith("output/") and content:
        hits = [literal for literal in LEAK_LITERALS if literal in content]
        hits += [name for name in internal_names(pipeline) if name in content]
        if hits:
            deny(
                f"'{rel}' is read by the learner and must not expose workflow internals. "
                f"Found: {', '.join(sorted(set(hits)))}. Describe the learning path in the "
                "learner's terms — no artifact paths, state files, or agent names."
            )

    allow()


if __name__ == "__main__":
    main()
