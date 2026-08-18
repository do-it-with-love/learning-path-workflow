#!/usr/bin/env python3
"""Record a human approval or rejection for a workflow run.

This is the only thing permitted to write ``state/approval.json``; the
``approval_gate_guard`` PreToolUse hook denies agent writes to that path.

The check that matters is the digest. The coordinator publishes
``state/approval-request.json`` containing a SHA-256 of the document it wants
approved. This script recomputes that digest from disk and refuses to record an
approval if the document has changed in the meantime — so an approval always
refers to specific bytes a person actually read, never to a filename whose
contents can drift afterwards.

Usage:
    python3 scripts/approve.py <run-id>
    python3 scripts/approve.py <run-id> --reject "too dense, add weekly practice"
    python3 scripts/approve.py <run-id> --status
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".claude" / "hooks"))

from wfstate import (  # noqa: E402
    load_state,
    repo_root,
    save_state,
    sha256_file,
    state_lock,
    utcnow,
)


def approver_identity() -> str:
    try:
        email = subprocess.run(
            ["git", "config", "user.email"],
            capture_output=True, text=True, timeout=5,
        ).stdout.strip()
        if email:
            return email
    except (OSError, subprocess.SubprocessError):
        pass
    return os.environ.get("USER") or "unknown"


def fail(message: str) -> None:
    print(f"REFUSED: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Approve or reject a workflow run's output.")
    parser.add_argument("run_id")
    parser.add_argument("--reject", metavar="FEEDBACK",
                        help="reject with feedback instead of approving")
    parser.add_argument("--status", action="store_true",
                        help="print the current approval state and exit")
    args = parser.parse_args()

    root = repo_root(Path(__file__).resolve())
    run_dir = root / "runs" / args.run_id
    if not run_dir.is_dir():
        fail(f"no such run: runs/{args.run_id}")

    approval_path = run_dir / "state" / "approval.json"
    request_path = run_dir / "state" / "approval-request.json"

    if args.status:
        for label, path in (("request", request_path), ("approval", approval_path)):
            if path.is_file():
                print(f"--- {label} ---")
                print(path.read_text(encoding="utf-8").rstrip())
            else:
                print(f"--- {label}: none ---")
        return 0

    if not request_path.is_file():
        fail(
            f"run {args.run_id} has not requested approval yet. The workflow writes "
            "state/approval-request.json once the draft is ready for review."
        )

    try:
        request = json.loads(request_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"approval-request.json is not valid JSON ({exc})")

    source_rel = request.get("source") or "output/learning-path.md"
    source_path = run_dir / source_rel
    if not source_path.is_file():
        fail(f"the document awaiting approval is missing: {source_rel}")

    current = sha256_file(source_path)
    requested = request.get("digest")

    if current != requested:
        fail(
            f"{source_rel} has changed since approval was requested.\n"
            f"  requested: {requested}\n"
            f"  on disk:   {current}\n"
            "Nothing was recorded. Ask the workflow to re-request approval so you are "
            "reviewing the document that would actually be published."
        )

    decision = {
        "run_id": args.run_id,
        "status": "changes_requested" if args.reject else "approved",
        "source": source_rel,
        "digest": current,
        "decided_at": utcnow(),
        "approver": approver_identity(),
        "feedback": args.reject or None,
    }

    approval_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = approval_path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(decision, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, approval_path)

    # Mirror into the run state so the coordinator sees the decision on resume.
    with state_lock(run_dir):
        state = load_state(run_dir)
        if state:
            approval = state.setdefault("approval", {})
            approval["status"] = decision["status"]
            approval["digest"] = decision["digest"]
            approval["decided_at"] = decision["decided_at"]
            approval["approver"] = decision["approver"]
            if args.reject:
                approval.setdefault("feedback", []).append(
                    {"at": decision["decided_at"], "text": args.reject}
                )
                state["status"] = "revising"
            else:
                state["status"] = "approved"
            state.setdefault("history", []).append({
                "at": decision["decided_at"],
                "event": f"human_{decision['status']}",
                "digest": decision["digest"],
                "approver": decision["approver"],
            })
            save_state(run_dir, state)

    if args.reject:
        print(f"Rejection recorded for {args.run_id}.")
        print(f"Feedback: {args.reject}")
        print("The workflow will revise the document and request approval again.")
    else:
        print(f"Approved: {args.run_id}")
        print(f"  document: {source_rel}")
        print(f"  digest:   {current}")
        print(f"  approver: {decision['approver']}")
        print("The final output may now be generated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
