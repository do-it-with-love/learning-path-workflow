#!/usr/bin/env python3
"""PreToolUse — the human-approval gate.

Two jobs, both of which must be code rather than instructions, because an
instruction to "wait for approval" is exactly the kind of thing a model can
convince itself it has already satisfied:

1. The approval record itself is off-limits to the model. Only
   ``scripts/approve.py``, invoked by the user's /approve-learning-path command,
   may write ``state/approval.json``.

2. The final rendered output cannot be written unless an approval exists AND the
   digest in it still matches the source Markdown on disk right now. Editing the
   Markdown after approval invalidates the approval automatically — the human
   approved specific bytes, not a filename.

Fails closed: anything unexpected denies the write.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wfstate import (  # noqa: E402
    allow,
    deny,
    load_pipeline,
    read_hook_input,
    repo_root,
    sha256_file,
    split_run_path,
    target_path,
)


def approval_protected_step(pipeline: dict) -> tuple[str, str, str] | None:
    """(step, gated artifact, source artifact it must match)."""
    for step, spec in pipeline["steps"].items():
        if not spec.get("requires_approval"):
            continue
        parents = spec.get("depends_on") or []
        if not parents:
            return None
        source = pipeline["steps"].get(parents[0], {}).get("artifact")
        if spec.get("artifact") and source:
            return step, spec["artifact"], source
    return None


def main() -> None:
    payload = read_hook_input()
    raw_target = target_path(payload)
    if not raw_target:
        allow()

    split = split_run_path(raw_target)
    if split is None:
        allow()  # not a workflow file, none of our business
    run_dir, rel = split

    # 1. The approval record is written by scripts/approve.py alone.
    if rel in ("state/approval.json", "state/approval-request.json"):
        if rel == "state/approval.json":
            deny(
                "state/approval.json records a human decision and cannot be written by "
                "an agent. Ask the user to run:  /approve-learning-path "
                f"{run_dir.name}   (or /approve-learning-path {run_dir.name} --reject "
                '"<feedback>"). That command runs scripts/approve.py, which is the only '
                "thing permitted to create this file."
            )
        allow()

    # 2. The gated final output.
    try:
        pipeline = load_pipeline(repo_root())
    except (OSError, ValueError) as exc:
        deny(f"approval_gate_guard could not read pipeline.json ({exc}); refusing to "
             "let a gated write through while the gate definition is unreadable.")

    protected = approval_protected_step(pipeline)
    if protected is None:
        allow()
    step, gated_artifact, source_artifact = protected

    if rel != gated_artifact:
        allow()

    approval_path = run_dir / "state" / "approval.json"
    if not approval_path.is_file():
        deny(
            f"'{gated_artifact}' requires explicit human approval and none has been "
            f"recorded for run {run_dir.name}. Write {source_artifact}, then ask the "
            f"user to review it and run:  /approve-learning-path {run_dir.name}"
        )

    import json

    try:
        approval = json.loads(approval_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        deny(f"state/approval.json is unreadable ({exc}). Re-request approval.")

    status = approval.get("status")
    if status != "approved":
        feedback = approval.get("feedback") or "(no feedback recorded)"
        deny(
            f"Approval status for run {run_dir.name} is '{status}', not 'approved'. "
            f"Feedback: {feedback}. Revise {source_artifact} per that feedback, then "
            f"request approval again."
        )

    source_path = run_dir / source_artifact
    current = sha256_file(source_path)
    if current is None:
        deny(f"{source_artifact} is missing, so the approval cannot be verified.")

    if approval.get("digest") != current:
        deny(
            f"{source_artifact} has changed since it was approved "
            f"(approved {str(approval.get('digest'))[:19]}…, "
            f"on disk {current[:19]}…). The human approved specific content, not a "
            f"filename. Ask the user to re-approve:  /approve-learning-path {run_dir.name}"
        )

    allow()


if __name__ == "__main__":
    main()
