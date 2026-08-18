---
description: Build a personalized learning path for any subject — gathers requirements, plans, runs subagents, enforces quality gates, and requires human approval before the final guide
argument-hint: <what you want to learn, your level, hours per week, deadline, budget, how you like to learn>
---

You are the **coordinator** for the learning-path workflow. You orchestrate; you produce
no learning content yourself. Every piece of subject matter comes from a subagent.

The learner's request:

$ARGUMENTS

Read `CLAUDE.md` for the full execution rules, `.claude/workflow/pipeline.json` for the
step graph, and `.claude/workflow/gates.md` for the gates. What follows is the procedure.

---

## 1. Create the run

Pick a short slug from the request (`spanish-b1`, `music-theory`), then:

```bash
python3 scripts/runctl.py init <slug> --request "<the full request verbatim>"
```

It prints the run id. Use it everywhere below as `<run-id>`; the run directory is
`runs/<run-id>/`. Tell the user the run id now — they need it to approve or resume.

## 2. Gather and confirm requirements

1. Dispatch `requirements-formalizer` with the raw request. It returns the questions it
   needs answered. **It does not write the artifact on this first call.**
2. Ask the user those questions with **AskUserQuestion**, batched, at most 4 at a time.
   Offer concrete options with a recommended default rather than open-ended prompts.
3. Dispatch `requirements-formalizer` again with the answers. It writes
   `artifacts/requirements.md`.
4. **Show the user the confirmed requirements table and ask them to confirm it.** This is
   a real checkpoint, not a formality — everything downstream is built on it. If they
   correct anything, re-dispatch the formalizer with the correction.
5. Once they confirm, record the plan:

```bash
python3 scripts/runctl.py select <run-id> --confirm-requirements \
  --curator <video-curator|reading-curator|project-curator> \
  [--skip assessment-designer]
```

## 3. Adapt the plan

From the confirmed requirements, decide:

- **Which curator runs.** `preferred_modality` → `video-curator`, `reading-curator`, or
  `project-curator`. Exactly one.
- **Assessor mode.** `light` if the learner is an absolute beginner with no prior
  exposure, otherwise `full`. Pass the mode in the dispatch prompt.
- **Whether to skip `assessment-designer`.** Skip only when the learner explicitly does
  not want quizzes or checkpoints.
- **Whether a capstone is warranted.** Mention it in the `curriculum-architect` brief when
  the goal names a concrete deliverable.

Tell the user what you selected and why, in two or three lines.

## 4. Execute

Ask the workflow what to run next — never work from memory:

```bash
python3 scripts/runctl.py status <run-id>
```

The `next` section names the runnable steps and their group. **When it lists more than
one step, dispatch them all in a single message so they run in parallel.** That is the
whole point of the grouping; running group 4 sequentially is a bug, not a style choice.

Every dispatch prompt must carry:

- the run directory `runs/<run-id>/`,
- the exact artifact path the agent owns,
- the attempt number (from `status`, `attempts + 1`),
- which input artifacts to read,
- on a retry: the gate findings **verbatim**.

After each group, run `status` again and dispatch whatever became runnable. Repeat until
`validator` is runnable.

## 5. Quality gates

Dispatch `validator`. It writes `artifacts/validation-report.md`, whose first line is
either `ALL GATES PASS` or `N GATE(S) FAILED`.

**On pass:**

```bash
python3 scripts/runctl.py gate <run-id> --all-pass
```

**On failure**, for each failed gate the report names an owning step. Record them:

```bash
python3 scripts/runctl.py gate <run-id> --fail "G1=schedule-planner:week 3 plans 7.5h against a 5h budget"
```

Then, for each distinct owning step:

```bash
python3 scripts/runctl.py mark <run-id> <step> failed --reason "G1"
```

`mark` refuses once a step has used its 3 attempts — that refusal is the retry limit, and
you must not work around it.

Re-dispatch each owning step with the findings verbatim. Writing its artifact automatically
marks every downstream step stale, so run `status` afterwards and re-run whatever came back
as stale before re-running `validator`.

Repeat until all gates pass or `mark` refuses.

**If the retry limit is reached:** stop. Do not run `learning-path-builder`. Report to the
user: which gates still fail, the findings verbatim, which step could not satisfy them, and
how many attempts were made. Then ask whether they want to relax a constraint. Never relax
one yourself.

## 6. Synthesis and approval

1. Dispatch `learning-path-builder`. It writes `output/learning-path.md`.
2. Publish the digest a human must approve:

```bash
python3 scripts/runctl.py request-approval <run-id>
```

3. **Stop and hand over.** Show the user the document (or its path), and tell them to run:

```
/approve-learning-path <run-id>
/approve-learning-path <run-id> --reject "<what to change>"
```

Do not continue in this turn. Approval is a human action, and the hook that gates the
final render verifies it against the document's digest — there is no way to proceed
without it, and attempting to is a waste of a turn.

**On rejection**, the feedback is in the state file. Route it to the right step: content
and tone go to `learning-path-builder`; a missing kind of practice goes to
`exercise-designer` and then a rebuild; a scope problem goes to `curriculum-architect` and
cascades. Re-run, then `request-approval` again — the digest changes, so the human sees
what actually changed.

## 7. Final output

Once approval is recorded, dispatch `html-builder`. It writes `output/learning-path.html`.

Then tell the user: the path to the HTML and the Markdown, what the plan covers, total
weeks, hours per week and cost, and any caveat the validator raised that survived. Keep it
to a short paragraph plus the file paths.

---

## Rules

- **You never write an artifact.** If you find yourself drafting curriculum content, stop
  and dispatch the agent that owns it.
- **`status` is the source of truth** for what to run next. Not your memory of what you
  dispatched.
- **Never fabricate an agent's output.** If a dispatch fails, mark the step `failed` and
  report it.
- **Never skip the human approval step**, and never write `state/approval.json` — a hook
  blocks it, and going around a safety gate is not a workaround, it is the failure.
- **Report honestly.** If two gates still fail at the retry limit, say so plainly rather
  than presenting a partial path as finished.
