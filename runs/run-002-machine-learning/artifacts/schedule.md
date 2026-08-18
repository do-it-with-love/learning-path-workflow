---
artifact: schedule
owner: schedule-planner
run_id: run-002-machine-learning
status: final
attempt: 1
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
generated: 2026-08-18T00:00:00Z
---

# Schedule — Machine Learning (classical, project-based)

## Summary

Ten weeks at 3 h/week (30 h capacity) carrying real demand of **27.82 h (1,669
minutes)** — resource time from `resources.md` + practice time from `exercises.md` +
checkpoint time from `assessments.md`, added module by module, not re-estimated. That
leaves **2.18 h (131 min, ≈7.3%) of slack**, thinner than the 15% guideline the method
calls for; see Open Questions for why, and what to flag rather than quietly compress.
The plan fits both gates: **G1** — every week stays at or under 3.30 h (the hardest
weeks, 5 and 7, run 3.25 h, 8.3% over the 3 h target and within the 10% ceiling); **G2**
— the plan uses exactly 10 of the 10 available weeks. Sessions follow the brief's
"one main + one short" pattern rather than three sessions, since 3 h/week is barely
more than one sitting: a longer weekend block for new material/projects, a short
weekday block for drills, review, and checkpoints. Module 9 (the capstone) occupies
weeks 9–10 as a contiguous, uninterrupted block with no other module content mixed in,
weighted 180 min → 132 min in favor of the larger capstone dataset (Adult, 48,842
rows) over the smaller one (Wine Quality, 4,898 rows), per `resources.md`'s note on
the size asymmetry. One judgement call worth flagging up front: `resources.md`'s Open
Questions names a likely double-count between Kaggle's built-in auto-graded exercises
(Modules 2, 3, 5, 7, 8) and `exercises.md`'s separately budgeted practice for the same
modules — both numbers are used below as instructed, and the risk is documented, not
silently resolved.

## Findings

### Week 1 — Module 1: Working with Tabular Data & Descriptive Statistics

- **Session A (main, weekend, 106 min):** Kaggle account setup (6 min) + "Learn
  Pandas" lessons — Creating/Reading/Writing, Indexing, Summary Functions (90 min) +
  hand-vs-pandas drill: compute mean/variance/std on 10 rows by hand, verify against
  pandas (10 min).
- **Session B (short, weekday, 30 min):** Profile-a-whole-dataset application
  exercise (15 min) + **Module 1 checkpoint** (15 min).
- **Week total: 136 min = 2.27 h.**
- **Checkpoint:** Module 1 check (descriptive statistics match `.describe()`).

### Week 2 — Module 2: The Supervised Learning Workflow — Your First Model

- **Session A (main, weekend, 120 min):** Kaggle "Intro to Machine Learning" —
  Model Validation and first model fit + scikit-learn "Getting Started" walkthrough.
- **Session B (short, weekday, 45 min):** Split-instability drill (10 min) +
  first-end-to-end-model application exercise (20 min) + **Module 2 checkpoint**
  (15 min).
- **Week total: 165 min = 2.75 h.**
- **Checkpoint:** Module 2 check (train/test score reported honestly, split
  explained).

### Week 3 — Module 3: Classification I — Predicting Categories

- **Session A (main, weekend, 126 min):** Titanic competition — train a classifier,
  submit to the leaderboard + Logistic Regression user-guide read.
- **Session B (short, weekday, 45 min):** Probability-by-hand drill (10 min) +
  predict-vs-predict_proba application exercise (20 min) + **Module 3 checkpoint**
  (15 min).
- **Week total: 171 min = 2.85 h.**
- **Checkpoint:** Module 3 check (predict/predict_proba consistency).

### Week 4 — Cumulative review 1 + Module 4: Evaluating Classifiers

- **Session A (main, weekend, 100 min):** Classification-metrics user guide +
  confusion-matrix example, applied to the Module 3 classifier (90 min) +
  precision/recall-by-hand drill (10 min).
- **Session B (short, weekday, 55 min):** Imbalance synthesis exercise (20 min) +
  **Module 4 checkpoint** (15 min) + **Cumulative review 1** — Modules 1–3, retrieval
  from memory against a worked answer key (20 min).
- **Week total: 155 min = 2.58 h.**
- **Checkpoints:** Module 4 check; Cumulative review 1.

### Week 5 — Module 5: Regression I — Predicting Numbers

- **Session A (main, weekend, 150 min):** House Prices competition — fit a
  regressor, submit to the leaderboard + linear regression (OLS/Ridge) example.
- **Session B (short, weekday, 45 min):** Residuals-by-hand drill (10 min) +
  second-regression-dataset application exercise (20 min) + **Module 5 checkpoint**
  (15 min).
- **Week total: 195 min = 3.25 h** — the heaviest week in the plan (8.3% over the
  3 h target, within the 3.30 h gate ceiling; see Open Questions).
- **Checkpoint:** Module 5 check (residual sign, regression-vs-classification
  scenarios).

### Week 6 — Module 6: Evaluating Regressors + Cumulative review 2

- **Session A (main, weekend, 90 min):** Regression-metrics user guide +
  cross-validated-predictions example, applied to the Module 5 regressor.
- **Session B (short, weekday, 65 min):** MAE/RMSE-by-hand drill (10 min) +
  compare-two-models synthesis exercise (20 min) + **Module 6 checkpoint** (15 min) +
  **Cumulative review 2** — Modules 4–6, retrieval against a worked answer key
  (20 min).
- **Week total: 155 min = 2.58 h.**
- **Checkpoints:** Module 6 check; Cumulative review 2.

### Week 7 — Module 7: Overfitting, Underfitting & Generalization (part 1)

- **Session A (main, weekend, 180 min):** Kaggle Cross-Validation lesson + linked
  graded exercise, Underfitting-vs-Overfitting example, and the scikit-learn
  cross-validation user guide — the module's full resource load, taken as one
  extended project block since the three pieces build on each other directly.
- **Session B (short, weekday, 15 min):** "Watch overfitting happen" drill —
  deliberately overfit and underfit a model, compare train/test accuracy.
- **Week total: 195 min = 3.25 h** — tied with Week 5 as the heaviest week (8.3%
  over target, within the 3.30 h ceiling).
- **Checkpoint:** none this week — Module 7's checkpoint is the hard go/no-go gate
  and is deliberately placed in Week 8 once the module's practice is complete (see
  below), not split across the boundary.

### Week 8 — Module 7 (part 2, closes) + Module 8: Feature Engineering & Preparing Real Data

- **Session A (main, weekend, 140 min):** Finish Module 7 — cross-validation-on-
  your-own-models exercise (15 min), fix-the-overfit-model exercise (15 min), and
  the **Module 7 checkpoint** (20 min, the one hard go/no-go gate in this run: a
  learner who prefers the higher-training-score model does not proceed) — then
  begin Module 8 with the Kaggle Pipelines lesson and its linked graded exercise
  (90 min).
- **Session B (short, weekday, 45 min):** Impute-by-hand drill (10 min) +
  full-preprocessing-pipeline application exercise (20 min) + **Module 8 checkpoint**
  (15 min).
- **Week total: 185 min = 3.08 h** (2.8% over target, within ceiling).
- **Checkpoints:** Module 7 check (hard gate); Module 8 check.

### Week 9 — Module 9: Capstone, part 1 — Classifier (Adult dataset)

Contiguous capstone block, no other module content mixed in. The Adult dataset
(48,842 rows) is the larger of the two capstone datasets, so it gets the larger and
earlier share of capstone time.

- **Session A (main, weekend, 130 min):** Download the Adult dataset; build the
  classification pipeline end-to-end — split, train, evaluate (accuracy, precision,
  recall) — reusing the workflow, evaluation, and pipeline patterns from Modules
  1–8.
- **Session B (short, weekday, 50 min):** Diagnose over/underfitting on the
  classifier (train/test gap or cross-validation), apply one mitigation, and begin
  the capstone self-audit checklist for the classifier half.
- **Week total: 180 min = 3.00 h** — exactly at target, no slack this week.
- **Checkpoint:** none separate — the capstone's assessment is the Final check,
  completed at the end of Week 10.

### Week 10 — Module 9: Capstone, part 2 — Regressor (Wine Quality dataset) + write-up

- **Session A (main, weekend, 90 min):** Download the Wine Quality dataset (4,898
  rows, the smaller of the two); build the regression pipeline end-to-end — split,
  train, evaluate (MAE, RMSE), diagnose over/underfitting, apply one mitigation.
- **Session B (short, weekday, 42 min):** Complete the capstone self-audit checklist
  for both halves; write up the pipeline, results, and mitigations for both models;
  work through the **Final check** against the six target outcomes in
  `requirements.md`.
- **Week total: 132 min = 2.20 h** — 48 min of slack, the largest single-week margin
  in the plan, deliberately placed here as the closest thing this budget can afford
  to a buffer before the deadline (see Open Questions on why a full buffer week
  was not otherwise possible).
- **Checkpoint:** Final check (capstone classifier + regressor checklists).

### Load check

Real hours = resource time (`resources.md` coverage-check table) + practice time
(`exercises.md` practice-load table) + checkpoint time (`assessments.md`), summed per
module/week exactly as those artifacts state them — no re-estimation.

| Week | Content | Planned | Budget (target) | Margin vs. target | ≤ G1 ceiling (3.30 h)? |
|---|---|---|---|---|---|
| 1 | Module 1 | 136 min = 2.27 h | 180 min = 3.00 h | +44 min (+0.73 h) | Yes |
| 2 | Module 2 | 165 min = 2.75 h | 180 min = 3.00 h | +15 min (+0.25 h) | Yes |
| 3 | Module 3 | 171 min = 2.85 h | 180 min = 3.00 h | +9 min (+0.15 h) | Yes |
| 4 | Review 1 + Module 4 | 155 min = 2.58 h | 180 min = 3.00 h | +25 min (+0.42 h) | Yes |
| 5 | Module 5 | 195 min = 3.25 h | 180 min = 3.00 h | −15 min (−0.25 h) | Yes (195 ≤ 198) |
| 6 | Module 6 + Review 2 | 155 min = 2.58 h | 180 min = 3.00 h | +25 min (+0.42 h) | Yes |
| 7 | Module 7 (part 1) | 195 min = 3.25 h | 180 min = 3.00 h | −15 min (−0.25 h) | Yes (195 ≤ 198) |
| 8 | Module 7 (part 2) + Module 8 | 185 min = 3.08 h | 180 min = 3.00 h | −5 min (−0.08 h) | Yes |
| 9 | Module 9 — capstone pt.1 | 180 min = 3.00 h | 180 min = 3.00 h | 0 min (0.00 h) | Yes |
| 10 | Module 9 — capstone pt.2 | 132 min = 2.20 h | 180 min = 3.00 h | +48 min (+0.80 h) | Yes |
| **Total** | **9 modules + 2 reviews** | **1,669 min = 27.82 h** | **1,800 min = 30.00 h** | **+131 min (+2.18 h, 7.3% slack)** | **Yes — max week 195/180 = 108.3%, under the 110% ceiling** |

Arithmetic behind the module totals (resource + practice + checkpoint, in minutes):

| Module | Resource (resources.md) | Practice (exercises.md) | Checkpoint (assessments.md) | Total |
|---|---|---|---|---|
| 1 | 96 | 25 | 15 | 136 |
| 2 | 120 | 30 | 15 | 165 |
| 3 | 126 | 30 | 15 | 171 |
| Review 1 | — | — | 20 | 20 |
| 4 | 90 | 30 | 15 | 135 |
| 5 | 150 | 30 | 15 | 195 |
| 6 | 90 | 30 | 15 | 135 |
| Review 2 | — | — | 20 | 20 |
| 7 | 180 | 45 | 20 | 245 |
| 8 | 90 | 30 | 15 | 135 |
| 9 (capstone) | 312 (300 build + 12 dataset dl) | 0 (folded into build time per `exercises.md`) | 0 (folded into build time per `assessments.md`) | 312 |
| **Total** | **1,254** | **250** | **165** | **1,669** |

1,254 + 250 + 165 = 1,669 minutes = 27.82 h. Against 1,800 minutes (30 h) of capacity,
this leaves 131 minutes (2.18 h, 7.3%) of slack — see Open Questions for why this is
below the 15% guideline and what to do about it.

### Deadline check

- Weeks used: **10**.
- `horizon_weeks`: **10**.
- 10 ≤ 10 — **fits, with zero weeks of margin.** Every module in `curriculum.md`
  (1 through 9) appears in the schedule above.

## Sources

None.

## Open Questions

- **Slack is 7.3%, not the ~15% the method calls for, and there is no genuine empty
  buffer week.** Real demand (27.82 h) leaves only 2.18 h of headroom across 10 weeks
  at 3 h/week; a dedicated empty buffer week would need ~3 h of slack concentrated in
  one place, which this plan cannot afford without breaking gate G1 elsewhere. I chose
  to protect G1 (no week over 3.30 h) and G2 (≤10 weeks) exactly as instructed, rather
  than manufacture slack that the arithmetic doesn't support. The closest approximation
  to a buffer is Week 10's 48-minute margin, placed immediately before the plan ends.
  If a true buffer week is wanted, the first things I would cut are the lower-stakes
  drills `exercises.md` itself names as the least load-bearing: the Module 1, 2, 5, and
  8 drills (mechanical verification, not the overfitting or metric-choice exercises
  that carry the module's real insight) — cutting all four would reclaim 40 minutes,
  not enough alone; the double-count below would need resolving too.
- **Possible double-count, flagged but not resolved here.** `resources.md`'s Open
  Questions states that Kaggle's own auto-graded exercises already cover the practice
  for Modules 2, 3, 5, 7, and 8, and that if `exercises.md` separately budgets time for
  the same work, that is a double-count. `exercises.md` did add separate bespoke
  drills/applications for exactly those five modules (30 + 30 + 30 + 45 + 30 = 165 min
  = 2.75 h). Per this artifact's brief, I used both numbers as given rather than
  silently netting them out — but if that practice time genuinely overlaps with what
  the Kaggle courses' own exercises already require, real demand could be as low as
  25.07 h (27.82 h − 2.75 h) against the 30 h budget, which would restore slack close
  to the intended 15%. This needs a decision from `curriculum-architect` or
  `exercise-designer` about whether those bespoke exercises are additive practice or
  redundant with the resource's own graded work — it is not something this schedule can
  determine on its own.
- **Weeks 5 and 7 are the tightest in the plan (3.25 h each, 8.3% over the 3 h
  target, within the 3.30 h gate ceiling).** Module 5's competition-based resource
  (150 min) and Module 7's three-resource load (180 min) don't subdivide cleanly
  without breaking a module's contiguity or separating the Module 7 checkpoint from
  the practice that precedes it. A learner who has a bad week should expect these two
  weeks to be the ones that slip first.
- **Capstone time was split 180 min (Week 9, Adult/classifier) vs. 132 min (Week 10,
  Wine Quality/regressor), favoring the larger dataset**, per the brief's instruction
  to account for the two datasets' size difference (48,842 vs. 4,898 rows). Worth
  noting: `resources.md` itself says this is not actually a runtime bottleneck (both
  train in seconds), so the extra time given to Week 9 is really about the larger
  dataset's greater conceptual/exploratory surface, not compute time — a judgement
  call, not an arithmetic necessity.
- **No scope was cut and no gate was broken to hit the deadline.** Both G1 and G2 are
  met as computed above; this section exists because the fit is tight, not because it
  fails.
