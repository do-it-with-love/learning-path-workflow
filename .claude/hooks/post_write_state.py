#!/usr/bin/env python3
"""PostToolUse — persist workflow state after every artifact write.

This hook is what makes the workflow resumable and what makes targeted retries
correct. Two things happen whenever an artifact lands on disk:

1. The owning step is marked done, with a SHA-256 of exactly what was written and
   an incremented attempt count. Because the count lives here rather than in the
   model's head, the retry limit cannot be talked around.

2. Every step that transitively depends on this artifact is marked **stale**. That
   is the cascade the assignment requires: regenerating an upstream artifact
   invalidates the downstream ones automatically, so a gate-driven retry can never
   leave a stale schedule sitting next to a fresh curriculum.

Never blocks the tool call — a state-tracking failure must not destroy work. Any
error is reported on stderr for the transcript and the hook exits 0.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wfstate import (  # noqa: E402
    artifact_owners,
    load_pipeline,
    load_state,
    read_hook_input,
    repo_root,
    save_state,
    sha256_file,
    split_run_path,
    state_lock,
    target_path,
    transitive_dependents,
    utcnow,
)

TRACKED_PREFIXES = ("artifacts/", "output/")


def main() -> None:
    payload = read_hook_input()
    raw_target = target_path(payload)
    if not raw_target:
        return

    split = split_run_path(raw_target)
    if split is None:
        return
    run_dir, rel = split

    if not rel.startswith(TRACKED_PREFIXES):
        return

    pipeline = load_pipeline(repo_root())
    owners = artifact_owners(pipeline)
    step = owners.get(rel)
    if step is None:
        return  # unregistered file; no_leak_guard already refuses these

    digest = sha256_file(run_dir / rel)
    if digest is None:
        return  # the write did not actually land

    with state_lock(run_dir):
        state = load_state(run_dir)
        if not state:
            return  # run not initialised yet; the coordinator owns creation

        steps = state.setdefault("steps", {})
        entry = steps.setdefault(step, {"status": "pending", "attempts": 0})

        # An attempt is a *production* of the artifact, not a write of it. Only
        # count when the step was not already done: a step that rewrites its own
        # artifact twice inside one dispatch is still one attempt.
        #
        # The earlier version counted every write and relied on a prompt telling
        # agents to write exactly once. That is exactly the kind of instruction
        # this layer exists to not depend on — an agent that revised its own file
        # burned a retry it had not used, and could be blocked while attempts
        # genuinely remained.
        if entry.get("status") != "done":
            entry["attempts"] = int(entry.get("attempts", 0)) + 1
        entry["status"] = "done"
        entry["artifact"] = rel
        entry["digest"] = digest
        entry["updated_at"] = utcnow()

        stale: list[str] = []
        for dependent in sorted(transitive_dependents(pipeline, step)):
            target = steps.setdefault(dependent, {"status": "pending", "attempts": 0})
            if target.get("status") == "done":
                target["status"] = "stale"
                target["stale_since"] = utcnow()
                target["stale_cause"] = step
                stale.append(dependent)

        history = state.setdefault("history", [])
        history.append({
            "at": utcnow(),
            "event": "artifact_written",
            "step": step,
            "artifact": rel,
            "attempt": entry["attempts"],
            "invalidated": stale,
        })
        del history[:-200]  # keep the tail bounded

        save_state(run_dir, state)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # never break the tool call over bookkeeping
        print(f"post_write_state: {type(exc).__name__}: {exc}", file=sys.stderr)
    sys.exit(0)
