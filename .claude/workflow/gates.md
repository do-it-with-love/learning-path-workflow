# Quality gates

The `validator` subagent checks every gate below against the artifacts of the current
run and writes `artifacts/validation-report.md`. The coordinator reads that report and
re-runs **only the owning step** of each failed gate.

Gates are checked in order. A gate that cannot be evaluated because its input artifact
is missing is reported as `BLOCKED`, not `PASS`.

| ID | Gate | Checked against | Owner on failure |
|----|------|-----------------|------------------|
| G1 | Planned hours in every week ≤ `requirements.weekly_hours`, tolerance +10% | `schedule.md` | `schedule-planner` |
| G2 | Total path length ≤ `requirements.horizon_weeks` | `schedule.md`, `curriculum.md` | `schedule-planner`, escalates to `curriculum-architect` |
| G3 | Total cost ≤ `requirements.budget` (0 means free-only) | `effort-budget.md`, `resources.md` | `curator` |
| G4 | No module lists a prerequisite that is only taught in a later module; module 1's prerequisites are all present in `baseline-assessment.md` | `curriculum.md` | `curriculum-architect` |
| G5 | Every target outcome in `requirements.md` maps to ≥1 module, **and** every module has ≥1 resource, ≥1 exercise, and ≥1 assessment | `curriculum.md`, `resources.md`, `exercises.md`, `assessments.md` | `curriculum-architect` |
| G6 | No resource URL appears under more than one module | `resources.md` | `curator` |
| G7 | Every resource cites a reachable URL, verified this run by MCP or WebFetch — never from model memory | `resources.md` | `curator` |
| G8 | ≥70% of resources match `requirements.preferred_modality` | `resources.md` | `curator` |
| G9 | No module is more than one level above the assessed baseline | `curriculum.md`, `baseline-assessment.md` | `curriculum-architect` |

## Conditional relaxations

- **G5** drops its `≥1 assessment` clause when `assessment-designer` is in
  `state.skipped_steps` (learner declined assessments).
- **G3** is skipped when `requirements.budget` is `unspecified`; the report must then
  state the computed total so the learner can judge it.

## Retry protocol

1. `validator` reports each failure as `GATE <id> FAIL — <finding> — owner: <step>`.
2. The coordinator re-runs each distinct owning step, passing the findings verbatim as
   corrective instructions.
3. Re-running a step rewrites its artifact, which fires `post_write_state.py`; that hook
   marks every transitive dependent **stale** from `pipeline.json`.
4. The coordinator re-runs stale steps, then re-runs `validator`.
5. Repeat until all gates pass or a step reaches `retry_limit` (3) attempts.

## On exhaustion

Set `state.status = "blocked"`, do **not** run `learning-path-builder`, and report to the
user: the failing gate IDs, the findings verbatim, the step that could not satisfy them,
and the number of attempts made. Never paper over an unresolved gate by relaxing it.
