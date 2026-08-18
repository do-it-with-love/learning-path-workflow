# Personalized Learning Assistant — workflow and execution rules

This repository is an agentic workflow that turns "I want to learn X" into a validated,
week-by-week study plan for any subject, delivered as Markdown and standalone HTML.

It is a **model-driven hub-and-spoke** system. A coordinator gathers requirements, plans,
selects which subagents to run, dispatches them, enforces quality gates, and holds the
human-approval gate. Subagents do all subject-matter work; each owns exactly one artifact.

## The single most important idea

The reliability properties are **enforced by code, not by instructions**. A prompt that
says "wait for human approval" is a prompt a model can talk itself out of. So:

| Property | Enforced by |
|---|---|
| Artifact ownership | `no_leak_guard.py` — denies writes to unregistered artifacts, or with a mismatched `owner` |
| Predictable artifact structure | `no_leak_guard.py` — denies writes missing the required frontmatter or sections |
| Predictable final document | `no_leak_guard.py` — denies a final document without the fixed eight-section skeleton |
| No workflow internals in learner output | `no_leak_guard.py` — content scan |
| Human approval before final output | `approval_gate_guard.py` — denies the render unless an approval exists **and its digest still matches the source on disk** |
| Approval cannot be self-granted | `approval_gate_guard.py` — denies agent writes to `state/approval.json`; only `scripts/approve.py` may create it |
| Resumability | `post_write_state.py` — records a digest per artifact; `runctl.py verify` re-checks against disk |
| Correct cascading retries | `post_write_state.py` — marks every transitive dependent stale from the pipeline graph |
| Retry limit | `runctl.py mark` — refuses a fourth attempt |

If a hook denies a write, **that is the system working**. Fix the cause; never route around it.

## Execution flow

```
[1] requirements-formalizer              ← clarifying Q&A, user confirms
[2] knowledge-assessor                     (mode: full | light)
[3] curriculum-architect
[4] <modality>-curator ‖ exercise-designer ‖ assessment-designer     PARALLEL
[5] schedule-planner ‖ effort-budget-aggregator                      PARALLEL
[6] validator                            ← gates; targeted retry, max 3, cascades
[7] learning-path-builder                ← synthesis
[8] HUMAN APPROVAL                       ← deterministic; reject → revision loop
[9] html-builder
```

`.claude/workflow/pipeline.json` is the single source of truth for this graph. The
coordinator reads it to plan; the hooks read it to enforce ownership and staleness. Change
the graph there, never in a prompt.

**Steps sharing a group number must be dispatched in one message.** Running group 4
sequentially is a defect: those three agents have no dependency on each other, which is
precisely why `exercise-designer` and `assessment-designer` work from module objectives
rather than from the curator's resource list.

## Dynamic subagent selection

The plan adapts to the confirmed requirements:

- **Curator variant** — `preferred_modality` selects exactly one of `video-curator`,
  `reading-curator`, `project-curator`. All three own the same artifact slot (`curator`)
  and write `artifacts/resources.md` with `owner: curator`.
- **Assessor mode** — `light` for a declared absolute beginner (no diagnostic, zero
  baseline asserted), `full` otherwise.
- **Optional step** — `assessment-designer` is skipped when the learner declines
  checkpoints; gate G5 then drops its assessment clause.
- **Capstone** — added to the `curriculum-architect` brief only when the goal names a
  concrete deliverable.

Selections are recorded with `runctl.py select` and visible in `workflow-state.json`.

## Artifacts

All artifacts are human-readable Markdown under `runs/<run-id>/artifacts/`, with the
frontmatter and four-section structure defined in the `artifact-validator` skill. They are
written for humans and for the next agent, not parsed by a program — which is why they are
Markdown and why the structural rules are enforced at write time rather than by a schema.

| Artifact | Owner |
|---|---|
| `requirements.md` | `requirements-formalizer` |
| `baseline-assessment.md` | `knowledge-assessor` |
| `curriculum.md` | `curriculum-architect` |
| `resources.md` | `curator` (one of three variants) |
| `exercises.md` | `exercise-designer` |
| `assessments.md` | `assessment-designer` |
| `schedule.md` | `schedule-planner` |
| `effort-budget.md` | `effort-budget-aggregator` |
| `validation-report.md` | `validator` |
| `output/learning-path.md` | `learning-path-builder` |
| `output/learning-path.html` | `html-builder` |

**Write your artifact exactly once per dispatch.** The attempt counter is driven by writes,
so a second write inflates it and can trip the retry limit early.

## Quality gates

Nine gates, defined in `.claude/workflow/gates.md`, covering weekly load, deadline, cost,
prerequisite ordering, outcome coverage, duplicate resources, citation validity, modality
match, and level fit. Each failure names exactly one owning step so the coordinator can
re-run precisely that step and nothing else.

Retries cascade automatically: rewriting `curriculum.md` marks resources, exercises,
assessments, schedule, budget, validation and synthesis stale. Three attempts per step,
after which execution stops and the failure is reported rather than papered over.

## External information

The workflow must not rely on the model's internal knowledge for anything a learner will
act on.

- **`wikipedia` MCP** (community) — grounds subject decomposition and level frameworks in
  how a field is actually structured. Used by `knowledge-assessor` and
  `curriculum-architect`.
- **`openlibrary` MCP** (custom, `mcp-servers/openlibrary_mcp/`) — real catalogue records
  for books: ISBN, year, page count, ebook availability. Used by `reading-curator` and
  `project-curator`. Books are the easiest resource to hallucinate convincingly, which is
  why this server exists.
- **WebSearch / WebFetch** — courses, platforms, articles, and link-liveness checking in
  gate G7.

Every resource carries a `verified:` marker naming how it was confirmed **during this run**.
A citation without one fails G7.

## Skills

- **`artifact-validator`** — the artifact contract and the structural + citation check.
  Loaded by every producing agent and by `validator`.
- **`resource-vetting`** — the rubric for judging and citing any learning resource.
  Loaded by all three curators and by `validator`.
- **`learning-path-html-theme`** — template and rendering rules for the final guide.
  Loaded by `html-builder`.

## Commands

| Command | Purpose |
|---|---|
| `/build-learning-path <request>` | Start a run — the coordinator |
| `/resume-learning-path <run-id>` | Continue after an interruption |
| `/approve-learning-path <run-id> [--reject "..."]` | Record the human decision |

`scripts/runctl.py` is the coordinator's control surface — `init`, `status`, `verify`,
`select`, `mark`, `gate`, `request-approval`. **Never hand-edit `workflow-state.json`.**
State a model edits by hand is state that drifts, and resume correctness depends on it.

## Resuming

`runctl.py verify` re-hashes every artifact marked done and trusts the disk over the state
file: a missing artifact drops to `pending`, a modified one to `stale`, and everything
downstream is invalidated. Then `runctl.py status` reports what is runnable. Completed work
is never repeated.

## Conventions

- Python is standard-library only for hooks and scripts, so the reliability layer works
  even when the venv does not. Only the MCP servers need dependencies.
- No secrets anywhere. Both MCP servers are key-free by design, so a clean checkout runs
  with no credentials. `.env` is gitignored; `.env.example` documents the two optional
  variables.
- Runs are committed. `runs/` is the evidence that the workflow handles happy paths, gate
  failures, interruptions and rejections — not just that it is wired up.

## Testing

```bash
python3 tests/test_hooks.py
```

28 tests over the three hooks and the approval script, using throwaway run directories.
No network, no venv. Run these after touching anything in `.claude/hooks/` or `scripts/`.
