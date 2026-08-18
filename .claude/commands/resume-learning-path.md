---
description: Resume an interrupted learning-path run from its persisted state, repeating no completed work
argument-hint: <run-id>   (omit to list runs)
---

Resume the workflow run: **$ARGUMENTS**

You are the coordinator picking up a run that was interrupted — a crash, a closed
terminal, a restarted process, or a session that simply ended mid-flight. Completed work
is on disk and must not be redone.

## 1. Find the run

If no run id was given, list what exists and ask which one:

```bash
ls runs/
```

## 2. Trust the disk, not the state file

```bash
python3 scripts/runctl.py verify <run-id>
```

This re-hashes every artifact marked `done` and corrects the record: a missing artifact
drops to `pending`, one that was edited outside the workflow drops to `stale`, and
everything downstream of a demoted step is invalidated too. An interruption can leave a
half-written file that the state file believes is finished, and this is what catches it.

## 3. See where things stand

```bash
python3 scripts/runctl.py status <run-id>
```

Read off: which steps are done, which are runnable now, whether any gate is failing,
whether any step has hit the retry limit, and the approval status.

Tell the user in a few lines what was already completed and what remains. They have
probably lost the thread since the interruption.

## 4. Continue

Pick up the procedure in `.claude/commands/build-learning-path.md` at whatever phase the
state indicates:

| State | Where to resume |
|---|---|
| `requirements_confirmed: false` | Phase 2 — gather and confirm requirements |
| Steps runnable, no gate failures | Phase 4 — dispatch the next group |
| Gates failing, attempts remaining | Phase 5 — re-run the owning steps with the findings |
| A step at the retry limit | Phase 5's failure branch — stop and report |
| `awaiting_approval` | Phase 6 — remind the user to approve; do not re-run the builder |
| `approved` | Phase 7 — dispatch `html-builder` |
| `revising` | Phase 6's rejection branch — route the feedback, then re-request approval |

**Re-run only what `status` lists as runnable.** A step marked `done` with a matching
digest is finished; re-running it wastes the work and, for the synthesis step,
invalidates an approval the human already gave.

If the run is `awaiting_approval` and the document is unchanged, do **not** call
`request-approval` again — the existing request is still valid and re-issuing it only
confuses the user about which version they are approving.
