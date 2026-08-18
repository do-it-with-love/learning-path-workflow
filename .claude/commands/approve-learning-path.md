---
description: Record your approval or rejection of a finished learning path, then generate the final HTML guide
argument-hint: <run-id> [--reject "what needs to change"]
allowed-tools: Bash(python3 scripts/approve.py:*), Bash(python3 scripts/runctl.py:*), Read, Task
---

Record the human decision for: **$ARGUMENTS**

## 1. Record the decision

Run the approval script exactly as the user invoked it:

```bash
python3 scripts/approve.py $ARGUMENTS
```

This script is the only thing permitted to write `state/approval.json` — a PreToolUse
hook blocks every other route. It recomputes the document's SHA-256 and refuses if the
document changed since approval was requested, so an approval always refers to the exact
bytes the user read.

**If it refuses**, relay the reason and stop. The usual cause is that the document was
regenerated after approval was requested; the fix is to re-request approval so the user
reviews the current version, never to bypass the check.

## 2a. On approval

Dispatch `html-builder` to render `output/learning-path.html`.

Then report to the user: where both files are, what the plan covers, its duration, weekly
hours and total cost, plus any caveat that survived validation.

## 2b. On rejection

The feedback is now recorded in the run state. Route it to whichever step actually owns
the problem:

| Feedback is about | Re-run |
|---|---|
| Wording, tone, ordering, emphasis | `learning-path-builder` |
| Not enough practice, wrong kind of practice | `exercise-designer`, then `learning-path-builder` |
| Wrong or missing resources, cost | the selected curator, then the downstream steps `status` reports as stale |
| Scope, module order, too much or too little | `curriculum-architect`, then everything it invalidates |
| Pacing, weekly load | `schedule-planner`, then `learning-path-builder` |

Use `python3 scripts/runctl.py mark <run-id> <step> failed --reason "user feedback"`
before re-dispatching, so the attempt is counted, then follow the retry procedure in
`.claude/commands/build-learning-path.md`.

When the revision is done, request approval again:

```bash
python3 scripts/runctl.py request-approval <run-id>
```

The digest changes, so the user is approving the revised document rather than a stale one.
Show them what changed in response to their feedback — that is what makes the second
review quick.
