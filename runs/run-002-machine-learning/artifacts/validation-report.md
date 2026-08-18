---
artifact: validation-report
owner: validator
run_id: run-002-machine-learning
status: final
attempt: 1
inputs:
  - artifacts/requirements.md
  - artifacts/baseline-assessment.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
  - artifacts/schedule.md
  - artifacts/effort-budget.md
generated: 2026-08-19T00:00:00Z
---

# Validation Report — Machine Learning (classical, project-based)

## Summary

**2 GATE(S) FAILED.** G1 (weekly hour ceiling) and G8 (modality match) fail. Both
failures trace to `resources.md`, so the coordinator needs to re-run only
**`curator`**: correcting resources.md's Module 2/3 time subtotals and its
interactive-resource classification will cascade automatically to
`schedule-planner` and `effort-budget-aggregator` per the pipeline graph, and
`schedule-planner` will need to confirm Week 3 stays under the ceiling once it
re-runs on the corrected numbers (it may need to move content out of Week 3). All
other gates (G2–G7, G9) pass on independently re-derived numbers. G7's citations
were spot-checked live: all 4 sampled URLs resolved and matched their claimed
content.

**Steps to re-run: `curator` (fixes both G1's root cause and G8), then let the
cascade re-run `schedule-planner` and `effort-budget-aggregator`, then re-run
`validator`.**

## Findings

### G1 — Weekly hour ceiling (≤ 3.30h, +10% of 3h)

**FAIL**

`resources.md`'s own Coverage-check table undercounts Modules 2 and 3 against the
sum of its own cited resource lines, and `schedule.md` copies those subtotals
verbatim ("no re-estimation," per its own Summary), so the undercount reaches the
schedule unnoticed:

- **Module 2:** resource lines are Intro to Machine Learning (~2h / 120 min for
  the lessons needed) + Getting Started (~0.5h / 30 min) = **150 min (2.5h)** true.
  The Coverage-check table states **"~2.0h" (120 min)** — a 30-minute (0.5h)
  undercount; the 0.5h "Getting Started" read is simply dropped from the sum.
- **Module 3:** resource lines are Titanic (~2h / 120 min for a first submission,
  + the table's own ~0.1h/6min competition-join buffer) + Logistic Regression
  user guide (~0.5h / 30 min) = **156 min (2.6h)** true. The table states
  **"~2.1h" (126 min)** — the same 30-minute (0.5h) undercount; the Logistic
  Regression read is likewise dropped.

`schedule.md`'s Week 2 and Week 3 totals inherit these numbers directly. Correcting
only the resource component:

| Week | Stated total | Corrected total | 3.30h (198 min) ceiling |
|---|---|---|---|
| 2 | 165 min (2.75h) | 150+30+15 = **195 min (3.25h)** | Pass (195 ≤ 198) |
| 3 | 171 min (2.85h) | 156+30+15 = **201 min (3.35h)** | **FAIL — 201 > 198 (111.7% of the 180-min target, over the 110% ceiling)** |

The "agreed" 27.82h grand total in `schedule.md` and `effort-budget.md` is not
independent confirmation of anything — both simply copy `resources.md`'s same
(undercounted) 20.9h resource figure, plus `exercises.md`'s 250 min (which I
re-summed by hand: 25+30+30+30+30+30+45+30 = 250, correct) and `assessments.md`'s
165 min (7×15 + 20 + 2×20 = 105+20+40 = 165, correct). Correcting only the
resource-hours component: true resource hours = 1,254 + 60 = 1,314 min (21.9h);
true grand total = 1,314 + 250 + 165 = **1,729 min = 28.82h** against 1,800 min
(30h) capacity — still under the aggregate cap, but true slack is **71 min
(1.18h, 3.9%)**, thinner even than the 7.3% `schedule.md` itself already flags as
below the 15% target.

**owner: curator** — the undercount originates in `resources.md`'s Coverage-check
table, which `schedule-planner` and `effort-budget-aggregator` both consume
verbatim by design (they do not re-derive resource hours from resource lines).
Re-running `schedule-planner` alone, without a corrected `resources.md`, would
reproduce the identical Week 3 breach and waste a retry. Once `curator` corrects
`resources.md`, the pipeline's staleness cascade will mark `schedule.md` and
`effort-budget.md` stale automatically.

**fix:** In `resources.md`'s Coverage-check table, correct Module 2's subtotal
from "~2.0h (120 min)" to "~2.5h (150 min)" and Module 3's from "~2.1h (126 min)"
to "~2.6h (156 min)"; update the grand total from "~20.9h" to "~21.9h". Then
`schedule-planner` (re-run automatically via cascade) must rebalance Week 3 to
stay ≤198 min — e.g. moving the Logistic Regression read to Week 4, which
currently has +25 min of headroom even before this correction.

### G2 — Deadline (≤ `horizon_weeks` = 10)

**PASS** — `schedule.md` uses exactly 10 weeks (Weeks 1–10, one per module plus two
cumulative reviews folded into Weeks 4 and 6); all 9 modules from `curriculum.md`
appear. 10 ≤ 10, zero weeks of margin, as `schedule.md` itself states.

### G3 — Cost (≤ `requirements.budget` = 0, free-only, hard constraint — NOT skipped)

**PASS** — All 17 resources in `resources.md`/`effort-budget.md`'s money table are
listed at $0 with no paid tier. Independently re-summed: 17 rows × $0 = $0 ≤ $0.
Sampled resources live via WebFetch (Kaggle Learn Pandas course, scikit-learn
Getting Started, UCI Adult dataset) confirmed as free, non-paywalled content — no
evidence of a hidden paid tier anywhere sampled. Budget met exactly at the
ceiling, as `effort-budget.md` states.

### G4 — Prerequisite ordering

**PASS** — No module's `Prerequisites` column in `curriculum.md` references a
later module number (checked all 9 rows: 2→1, 3→2, 4→3, 5→2, 6→5, 7→{4,6}, 8→7,
9→{1–8}; all strictly backward-referencing). Module 1's prerequisites are listed
as "baseline," and what it assumes (tabular-data handling, mean/variance) matches
exactly the items `baseline-assessment.md`'s "Prerequisite gaps" section marks
**Absent** — Module 1 teaches to those gaps rather than assuming they're already
closed.

### G5 — Outcome coverage and per-module completeness

**PASS** (`assessment-designer` ran — `wants_assessments = true` — so the full
clause applies, not the relaxed one). All 6 target outcomes in `requirements.md`
map to ≥1 module in `curriculum.md`'s Outcome-coverage table. Checked every
module (1–9) has ≥1 resource (`resources.md`), ≥1 exercise (`exercises.md`), and
≥1 assessment (`assessments.md`): minimum is Module 1 and Module 8 with exactly 1
resource each, and Module 9 with exactly 1 exercise (the capstone self-audit
checklist) — all still ≥1.

### G6 — No duplicate resource URLs

**PASS** — All 17 URLs in `resources.md` are distinct. The one apparent near-match
(`scikit-learn.org/.../model_evaluation.html#classification-metrics` for Module 4
and `#regression-metrics` for Module 6) uses distinct anchors on the same page for
two different modules — the sanctioned exception in the `resource-vetting` skill
("cite a specific chapter or lesson anchor when the same work legitimately serves
two modules"), not a duplicate.

### G7 — Citation verification

**PASS** — All 17 resource lines in `resources.md` (and all 6 in
`baseline-assessment.md`, all 10 in `curriculum.md`) carry a `verified: <method>
2026-08-18` marker; per the run's date note, `2026-08-18` is this run's date, not a
stale one. Sampled 4 of 17 resource URLs via live WebFetch (more than the 3-URL
minimum): all four resolved and matched their claimed content (see Link sample).
No resource was cited from model memory as far as sampling can detect.

### G8 — Modality match (≥70% match `preferred_modality` = project)

**FAIL**

`resources.md` claims 12/17 (70.6%) of resources are "interactive or
project-based," clearing the 70% floor by 0.6 points. Recounting against
`resources.md`'s own Findings-section descriptions of *how each resource is
used* (not just its format label) surfaces two misclassifications among the four
scikit-learn "runnable example" resources counted as interactive:

| Resource | Module | `resources.md`'s own description | Honest classification |
|---|---|---|---|
| Confusion matrix example | 4 | "swapping in **their own** model and data" | Interactive/project — correct |
| Linear regression example | 5 | "the scikit-learn example demonstrates the same estimator on **a second, simpler dataset** (diabetes) so the pattern is seen twice" — no learner data, not modified | **Reference/passive — misclassified** |
| Plotting Cross-Validated Predictions | 6 | "swapped to **their own** regressor" | Interactive/project — correct |
| Underfitting vs. Overfitting example | 7 | "runs the polynomial-degree example to see underfitting... quantified by MSE side by side" — the built-in synthetic-cosine demo, confirmed via live WebFetch (30 noisy samples of a cosine function, not learner data) | **Reference/passive — misclassified** |

Reclassifying those two consistently with the other 5 reference/user-guide pages
gives a corrected count of **10/17 = 58.8%** interactive/project-based — 11.2
points under the 70% floor.

This also means the two resources `curator` explicitly dropped from Modules 1 and
8 "to hold gate G8's 70% floor" (per `resources.md`'s own Open Questions — the
scikit-learn `datasets` loading-utilities guide, and the `Pipelines and composite
estimators` user guide) were cut to protect a ratio that was never genuinely at
70% to begin with. The cut left both modules thinner: Module 1 now has exactly
one resource total, with — by `resources.md`'s own Open Questions — "no
auto-graded checkpoint at all"; Module 8 now has exactly one resource, with no
formal `ColumnTransformer` API citation, which is the exact API
`exercises.md`'s own Module 8 troubleshooting note assumes the learner needs
("check you're routing numeric and categorical columns to different
preprocessing steps with a `ColumnTransformer`").

**owner: curator**

**fix:** Either (a) genuinely convert the Linear regression example and
Underfitting/Overfitting example into hands-on tasks — learner applies each to
their own Module 5/7 model and data, exactly as already done for the Module 4 and
6 examples — so the interactive classification is earned honestly and the ratio
stays at a true 12/17 (70.6%); or (b) reclassify both as reference and add enough
genuinely interactive resources to clear 70% honestly. Separately, reconsider
restoring the Module 1 and Module 8 resources dropped solely to protect this
ratio — note that restoring them without also adding interactive resources
elsewhere will push the ratio back down (12 interactive / 19 total = 63.2%), so
this cannot be done in isolation from the classification fix above.

### G9 — Level fit (no module more than one level above the assessed baseline)

**PASS**, under the progressive (module-to-module) reading of this gate — the
literal reading ("no module more than one level above the initial L0 baseline")
would fail any multi-level curriculum by construction and cannot be the intended
check; see Open Questions. `curriculum.md`'s own stated progression — L0 → L1 →
L1 → L2 → L2 → L2 → L3 → L3 → L3 — never increases by more than one level from
the immediately preceding module. Verified directly against the Level column in
`curriculum.md`'s module table: each step is +1 or +0 from the prior module.

### Structural checks

| Artifact | Frontmatter ok (7 keys) | Sections ok (4, in order, non-empty) | Citations ok |
|---|---|---|---|
| requirements.md | Yes | Yes | Sources: "None." — no external data consumed; not one of the four artifacts the skill explicitly exempts (exercises/assessments/schedule/effort-budget), but no citable claim exists in this Q&A-derived artifact. See Open Questions. |
| baseline-assessment.md | Yes | Yes | Yes — 6 Wikipedia citations, all `verified: mcp:wikipedia 2026-08-18` |
| curriculum.md | Yes | Yes | Yes — 10 Wikipedia citations, all `verified: mcp:wikipedia 2026-08-18` |
| resources.md | Yes | Yes | Structurally yes — all 17 lines carry `verified:` + this-run date; see G1/G8 for data-accuracy (not structural) findings |
| exercises.md | Yes | Yes | Yes — Sources: "None.", exempted for this artifact type |
| assessments.md | Yes | Yes | Yes — Sources: "None.", exempted for this artifact type |
| schedule.md | Yes | Yes | Yes — Sources: "None.", exempted for this artifact type |
| effort-budget.md | Yes | Yes | Yes — Sources: "None.", exempted for this artifact type |

`owner` fields all match `pipeline.json` step names exactly (`resources.md`'s
`owner: curator` is correct per the artifact-validator skill's rule that the
curator slot's owner is always `curator` regardless of which variant — here
`project-curator` — actually ran, named correctly in its Summary). All `inputs`
paths listed in every artifact's frontmatter exist in this run. No `output/`
files exist yet (pre-synthesis stage), so the internal-machinery-leak check does
not yet apply.

### Link sample

| URL | Method | Result |
|---|---|---|
| https://www.kaggle.com/learn/pandas | WebFetch | Resolved — "Learn Pandas Tutorials \| Kaggle," matches citation |
| https://scikit-learn.org/stable/getting_started.html | WebFetch | Resolved — scikit-learn Getting Started guide, matches citation |
| https://archive.ics.uci.edu/dataset/2/adult | WebFetch | Resolved — UCI Adult dataset, 48,842 instances / 14 features, matches citation exactly |
| https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html | WebFetch | Resolved — underfitting/overfitting polynomial-degree example on a synthetic cosine function; confirms the G8 finding that this example uses built-in demo data, not the learner's own |

## Sources

- [Learn Pandas Tutorials](https://www.kaggle.com/learn/pandas) — Kaggle · verified: webfetch 2026-08-19
- [scikit-learn: Getting Started](https://scikit-learn.org/stable/getting_started.html) — scikit-learn · verified: webfetch 2026-08-19
- [UCI Machine Learning Repository: Adult](https://archive.ics.uci.edu/dataset/2/adult) — UCI · verified: webfetch 2026-08-19
- [scikit-learn: Underfitting vs. Overfitting](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html) — scikit-learn · verified: webfetch 2026-08-19

## Open Questions

- **G9's exact scope is ambiguous as worded** ("no module more than one level
  above the assessed baseline" vs. "no module more than one level above the
  preceding module"). I applied the progressive reading, since the literal
  one-baseline reading would fail every curriculum spanning more than 2 levels of
  a 4-level scale, which cannot be the design intent. Worth clarifying in
  `gates.md` itself so future validator runs don't have to infer this.
- **`requirements.md`'s "Sources: None." is not covered by the artifact-validator
  skill's explicit exemption list** (only exercises/assessments/schedule/
  effort-budget are named as allowed to have no external sources). In practice
  `requirements-formalizer` genuinely consumes no external data — it is Q&A-only
  — so this is very likely a gap in the skill's exemption list rather than a
  defect in this artifact. Not scored as a structural failure; flagged for the
  skill's owner to consider adding `requirements` to the exemption list.
- **The possible double-count between Kaggle's own auto-graded exercises and
  `exercises.md`'s bespoke practice for Modules 2, 3, 5, 7, and 8** (raised in
  `resources.md`, `exercises.md`, and `effort-budget.md`'s own Open Questions, up
  to 165 min / 2.75h) could not be resolved from the text alone. It does not
  change the G1 verdict above (which fails independently of this question, from
  the resources.md undercount), and if resolved in the "overlap" direction it
  would only recover slack, not create a new shortfall — but the coordinator may
  want `exercise-designer` to weigh in when `curator` and `schedule-planner`
  re-run, since all three artifacts flagged it independently and it remains
  unresolved.
- **Kaggle competition-submission phone verification (Modules 3, 5)** is flagged
  as unresolved in `effort-budget.md`'s own Open Questions (does *submitting* to
  a leaderboard require phone verification, separate from notebook access). Not
  a G3 (money) issue either way since it carries no fee, but worth `curator`
  resolving directly with a live check if it re-runs anyway for G1/G8.
