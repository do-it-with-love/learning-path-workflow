#!/usr/bin/env python3
"""Hook tests. Standard library only: python3 tests/test_hooks.py

These exercise the three hooks the way Claude Code does — a JSON payload on
stdin, a decision on stdout — against throwaway run directories. They are the
evidence that the reliability guarantees hold, so they run without the venv and
without the network.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOOKS = ROOT / ".claude" / "hooks"

PASSED: list[str] = []
FAILED: list[str] = []


def run_hook(script: str, payload: dict) -> tuple[str, str]:
    proc = subprocess.run(
        [sys.executable, str(HOOKS / script)],
        input=json.dumps(payload), capture_output=True, text=True, timeout=30,
    )
    return proc.stdout.strip(), proc.stderr.strip()


def decision(stdout: str) -> str | None:
    if not stdout:
        return None
    try:
        return json.loads(stdout)["hookSpecificOutput"]["permissionDecision"]
    except (json.JSONDecodeError, KeyError):
        return None


def check(name: str, condition: bool, detail: str = "") -> None:
    if condition:
        PASSED.append(name)
        print(f"  PASS  {name}")
    else:
        FAILED.append(name)
        print(f"  FAIL  {name}  {detail}")


def write_payload(path: Path, content: str, tool: str = "Write") -> dict:
    return {
        "hook_event_name": "PreToolUse",
        "tool_name": tool,
        "tool_input": {"file_path": str(path), "content": content},
    }


def make_run(tmp: Path, run_id: str = "run-test") -> Path:
    run_dir = tmp / "runs" / run_id
    (run_dir / "artifacts").mkdir(parents=True)
    (run_dir / "output").mkdir(parents=True)
    (run_dir / "state").mkdir(parents=True)
    pipeline = json.loads((ROOT / ".claude/workflow/pipeline.json").read_text())
    state = {
        "run_id": run_id,
        "status": "running",
        "steps": {
            name: {"status": "pending", "attempts": 0, "artifact": spec.get("artifact")}
            for name, spec in pipeline["steps"].items()
        },
        "approval": {"status": "pending"},
    }
    (run_dir / "state" / "workflow-state.json").write_text(json.dumps(state, indent=2))
    return run_dir


VALID_ARTIFACT = """---
artifact: curriculum
owner: curriculum-architect
run_id: run-test
status: draft
attempt: 1
inputs:
  - artifacts/requirements.md
generated: 2026-08-18T12:00:00Z
---

# Curriculum

## Summary
Six modules.

## Findings
Module 1 ...

## Sources
None.

## Open Questions
None.
"""


VALID_DOCUMENT = """# Spanish to B1 — Your Learning Path

## Overview
Six months.

## Before You Start
Nothing to buy.

## Your Path Week by Week
Week 1: greetings.

## Modules
Module 1.

## Checkpoints and Progress
Rubrics.

## Resources
Links.

## Time and Cost
Totals.

## What Comes Next
B2.
"""


def test_ownership(tmp: Path) -> None:
    print("\nno_leak_guard — artifact ownership & structure")
    run = make_run(tmp, "run-own")

    out, _ = run_hook("no_leak_guard.py", write_payload(
        run / "artifacts" / "curriculum.md", VALID_ARTIFACT))
    check("valid artifact is allowed", decision(out) is None, f"got {out!r}")

    out, _ = run_hook("no_leak_guard.py", write_payload(
        run / "artifacts" / "my-notes.md", VALID_ARTIFACT))
    check("unregistered artifact is denied", decision(out) == "deny")

    wrong_owner = VALID_ARTIFACT.replace("owner: curriculum-architect", "owner: validator")
    out, _ = run_hook("no_leak_guard.py", write_payload(
        run / "artifacts" / "curriculum.md", wrong_owner))
    check("wrong owner is denied", decision(out) == "deny")

    no_fm = VALID_ARTIFACT.split("---\n\n", 1)[-1]
    out, _ = run_hook("no_leak_guard.py", write_payload(
        run / "artifacts" / "curriculum.md", no_fm))
    check("missing frontmatter is denied", decision(out) == "deny")

    missing_section = VALID_ARTIFACT.replace("## Sources\nNone.\n\n", "")
    out, _ = run_hook("no_leak_guard.py", write_payload(
        run / "artifacts" / "curriculum.md", missing_section))
    check("missing required section is denied", decision(out) == "deny")

    reordered = VALID_ARTIFACT.replace(
        "## Findings\nModule 1 ...\n\n## Sources\nNone.\n",
        "## Sources\nNone.\n\n## Findings\nModule 1 ...\n")
    out, _ = run_hook("no_leak_guard.py", write_payload(
        run / "artifacts" / "curriculum.md", reordered))
    check("out-of-order sections denied", decision(out) == "deny")

    print("\nno_leak_guard — final document structure")
    doc = run / "output" / "learning-path.md"

    out, _ = run_hook("no_leak_guard.py", write_payload(doc, VALID_DOCUMENT))
    check("well-formed document allowed", decision(out) is None, f"got {out!r}")

    out, _ = run_hook("no_leak_guard.py", write_payload(
        doc, VALID_DOCUMENT.replace("## Time and Cost\nTotals.\n\n", "")))
    check("document missing a section denied", decision(out) == "deny")

    swapped = VALID_DOCUMENT.replace(
        "## Modules\nModule 1.\n\n## Checkpoints and Progress\nRubrics.\n",
        "## Checkpoints and Progress\nRubrics.\n\n## Modules\nModule 1.\n")
    out, _ = run_hook("no_leak_guard.py", write_payload(doc, swapped))
    check("document sections out of order denied", decision(out) == "deny")

    print("\nno_leak_guard — output hygiene")
    out, _ = run_hook("no_leak_guard.py", write_payload(
        doc, VALID_DOCUMENT.replace("Module 1.", "See artifacts/curriculum.md.")))
    check("leaked artifact path denied", decision(out) == "deny")

    out, _ = run_hook("no_leak_guard.py", write_payload(
        doc, VALID_DOCUMENT.replace("Module 1.", "Built by the curriculum-architect.")))
    check("leaked agent name denied", decision(out) == "deny")

    out, _ = run_hook("no_leak_guard.py", write_payload(
        doc, VALID_DOCUMENT.replace("Module 1.", "Module 2 covers the curriculum for scales.")))
    check("ordinary word 'curriculum' not a false positive", decision(out) is None,
          f"got {out!r}")


def test_approval(tmp: Path) -> None:
    print("\napproval_gate_guard")
    run = make_run(tmp, "run-approve")
    md = run / "output" / "learning-path.md"
    html = run / "output" / "learning-path.html"
    md.write_text("# Plan\n\nWeek 1.\n")

    out, _ = run_hook("approval_gate_guard.py", write_payload(html, "<h1>Plan</h1>"))
    check("html denied with no approval", decision(out) == "deny")

    out, _ = run_hook("approval_gate_guard.py", write_payload(md, "# Plan\n"))
    check("markdown itself is not gated", decision(out) is None, f"got {out!r}")

    out, _ = run_hook("approval_gate_guard.py", write_payload(
        run / "state" / "approval.json", '{"status":"approved"}'))
    check("agent cannot write approval.json", decision(out) == "deny")

    # Approve properly, via the script.
    request = {
        "source": "output/learning-path.md",
        "digest": "sha256:" + __import__("hashlib").sha256(md.read_bytes()).hexdigest(),
        "requested_at": "2026-08-18T12:00:00Z",
    }
    (run / "state" / "approval-request.json").write_text(json.dumps(request))
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "approve.py"), "run-approve"],
        capture_output=True, text=True, cwd=tmp,
    )
    # approve.py resolves runs/ from the repo root, so point it at the temp tree.
    if proc.returncode != 0:
        shutil.copytree(run, ROOT / "runs" / "run-approve", dirs_exist_ok=True)
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "approve.py"), "run-approve"],
            capture_output=True, text=True,
        )
        run = ROOT / "runs" / "run-approve"
        md = run / "output" / "learning-path.md"
        html = run / "output" / "learning-path.html"
    check("approve.py records approval", proc.returncode == 0, proc.stderr.strip())

    out, _ = run_hook("approval_gate_guard.py", write_payload(html, "<h1>Plan</h1>"))
    check("html allowed after approval", decision(out) is None, f"got {out!r}")

    md.write_text("# Plan\n\nWeek 1. And a sneaky edit.\n")
    out, _ = run_hook("approval_gate_guard.py", write_payload(html, "<h1>Plan</h1>"))
    check("html denied after post-approval edit", decision(out) == "deny")

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "approve.py"), "run-approve"],
        capture_output=True, text=True,
    )
    check("approve.py refuses a stale request digest", proc.returncode != 0,
          proc.stdout.strip())

    shutil.rmtree(ROOT / "runs" / "run-approve", ignore_errors=True)


def test_rejection(tmp: Path) -> None:
    """The revision loop: reject with feedback, revise, re-request, approve.

    approve.py resolves runs/ from the repo root, so this builds its run there
    and removes it afterwards.
    """
    print("\napprove.py — rejection and revision loop")
    run = ROOT / "runs" / "run-reject-test"
    shutil.rmtree(run, ignore_errors=True)
    for sub in ("artifacts", "output", "state"):
        (run / sub).mkdir(parents=True)
    (run / "state" / "workflow-state.json").write_text(
        json.dumps({"run_id": "run-reject-test", "status": "running",
                    "steps": {}, "approval": {"status": "pending"}}, indent=2))

    md = run / "output" / "learning-path.md"
    html = run / "output" / "learning-path.html"

    def request() -> None:
        digest = "sha256:" + __import__("hashlib").sha256(md.read_bytes()).hexdigest()
        (run / "state" / "approval-request.json").write_text(json.dumps(
            {"source": "output/learning-path.md", "digest": digest,
             "requested_at": "2026-08-20T00:00:00Z"}))

    def approve(*args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "approve.py"), "run-reject-test", *args],
            capture_output=True, text=True)

    try:
        md.write_text("# Plan v1\n\nToo much theory.\n")
        request()

        proc = approve("--reject", "too theory-heavy, add weekly practice")
        check("approve.py records a rejection", proc.returncode == 0, proc.stderr.strip())

        record = json.loads((run / "state" / "approval.json").read_text())
        check("rejection status is changes_requested",
              record["status"] == "changes_requested", str(record.get("status")))
        check("rejection feedback is preserved",
              record["feedback"] == "too theory-heavy, add weekly practice")

        state = json.loads((run / "state" / "workflow-state.json").read_text())
        check("run state flips to revising", state.get("status") == "revising",
              str(state.get("status")))
        check("feedback appended to state history",
              bool(state["approval"].get("feedback")))

        out, _ = run_hook("approval_gate_guard.py", write_payload(html, "<h1>Plan</h1>"))
        check("render blocked while changes are requested", decision(out) == "deny")

        # Revise, then re-request — the digest changes, so the human reviews the new text.
        md.write_text("# Plan v2\n\nWeekly practice added.\n")
        out, _ = run_hook("approval_gate_guard.py", write_payload(html, "<h1>Plan</h1>"))
        check("revising alone does not unblock the render", decision(out) == "deny")

        proc = approve()
        check("approving a stale request is refused after revision", proc.returncode != 0)

        request()
        proc = approve()
        check("approval succeeds after re-request", proc.returncode == 0, proc.stderr.strip())

        out, _ = run_hook("approval_gate_guard.py", write_payload(html, "<h1>Plan</h1>"))
        check("render unblocked after re-approval", decision(out) is None, f"got {out!r}")
    finally:
        shutil.rmtree(run, ignore_errors=True)


def test_state(tmp: Path) -> None:
    print("\npost_write_state — attempts & cascade")
    run = make_run(tmp, "run-state")
    curriculum = run / "artifacts" / "curriculum.md"
    curriculum.write_text(VALID_ARTIFACT)

    payload = {
        "hook_event_name": "PostToolUse",
        "tool_name": "Write",
        "tool_input": {"file_path": str(curriculum), "content": VALID_ARTIFACT},
        "tool_response": {"success": True},
    }
    _, err = run_hook("post_write_state.py", payload)
    check("hook runs without error", err == "", err)

    state = json.loads((run / "state" / "workflow-state.json").read_text())
    step = state["steps"]["curriculum-architect"]
    check("owning step marked done", step["status"] == "done", str(step))
    check("attempt counted", step["attempts"] == 1, str(step))
    check("digest recorded", str(step.get("digest", "")).startswith("sha256:"))

    # Mark a downstream step done, rewrite upstream, expect a cascade.
    state["steps"]["schedule-planner"]["status"] = "done"
    state["steps"]["html-builder"]["status"] = "done"
    (run / "state" / "workflow-state.json").write_text(json.dumps(state, indent=2))

    curriculum.write_text(VALID_ARTIFACT.replace("Six modules.", "Five modules."))
    run_hook("post_write_state.py", payload)
    state = json.loads((run / "state" / "workflow-state.json").read_text())
    check("rewriting a done artifact does not inflate attempts",
          state["steps"]["curriculum-architect"]["attempts"] == 1,
          f"got {state['steps']['curriculum-architect']['attempts']}")
    check("direct dependent marked stale",
          state["steps"]["schedule-planner"]["status"] == "stale")
    check("transitive dependent marked stale",
          state["steps"]["html-builder"]["status"] == "stale")
    check("stale cause recorded",
          state["steps"]["schedule-planner"].get("stale_cause") == "curriculum-architect")

    _, err = run_hook("post_write_state.py", {
        "hook_event_name": "PostToolUse", "tool_name": "Write",
        "tool_input": {"file_path": "/etc/passwd", "content": "x"},
    })
    check("non-run paths ignored", err == "", err)

    # Regression: an agent that revises its own artifact inside one dispatch must
    # not burn a retry. Counting raw writes once blocked a run that still had an
    # attempt left, which is why attempts now track productions, not writes.
    print("\npost_write_state — one dispatch is one attempt")
    run = make_run(tmp, "run-double")
    art = run / "artifacts" / "curriculum.md"
    payload = {
        "hook_event_name": "PostToolUse", "tool_name": "Write",
        "tool_input": {"file_path": str(art), "content": VALID_ARTIFACT},
    }
    art.write_text(VALID_ARTIFACT)
    run_hook("post_write_state.py", payload)
    art.write_text(VALID_ARTIFACT.replace("Six modules.", "Six modules, revised."))
    run_hook("post_write_state.py", payload)
    art.write_text(VALID_ARTIFACT.replace("Six modules.", "Six modules, again."))
    run_hook("post_write_state.py", payload)

    state = json.loads((run / "state" / "workflow-state.json").read_text())
    entry = state["steps"]["curriculum-architect"]
    check("three writes in one dispatch count as one attempt",
          entry["attempts"] == 1, f"got {entry['attempts']}")

    # A genuine retry — the coordinator marks the step failed first — does count.
    entry["status"] = "failed"
    (run / "state" / "workflow-state.json").write_text(json.dumps(state, indent=2))
    art.write_text(VALID_ARTIFACT.replace("Six modules.", "Five modules."))
    run_hook("post_write_state.py", payload)
    state = json.loads((run / "state" / "workflow-state.json").read_text())
    check("a marked retry does count as a new attempt",
          state["steps"]["curriculum-architect"]["attempts"] == 2,
          f"got {state['steps']['curriculum-architect']['attempts']}")


def main() -> int:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        test_ownership(tmp)
        test_approval(tmp)
        test_rejection(tmp)
        test_state(tmp)

    print(f"\n{len(PASSED)} passed, {len(FAILED)} failed")
    for name in FAILED:
        print(f"  failed: {name}")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
