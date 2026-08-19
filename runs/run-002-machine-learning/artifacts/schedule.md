---
artifact: schedule
owner: schedule-planner
run_id: run-002-machine-learning
status: final
attempt: 3
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
  - artifacts/validation-report.md
generated: 2026-08-19T15:30:00Z
---

# Schedule — Machine Learning (classical, project-based)

## Summary

Light revision of attempt 2, triggered by `resources.md` attempt 3, which fixed gate
G8 (modality match) by swapping four citations — Modules 1, 2, 7, and 8 — from
tutorial/landing pages to the corresponding per-lesson Kaggle exercise notebooks, and
splitting two two-lesson citations into per-lesson ones (resource count 17→19,
interactive ratio 64.7%→73.7%). The coordinator's brief was explicit that `curator`
held every module's total minutes fixed, but that claim is re-derived here from
scratch rather than trusted: every module's resource subtotal below is re-summed from
`resources.md` attempt 3's own itemized lines, one line at a time, because the list
just changed shape (19 lines, not 17) and the same "trust the producer's stated
subtotal" shortcut is exactly what caused attempt 1's G1 failure. **The re-derivation
confirms the claim**: every module subtotal is identical to attempt 2's (Module 1:
30+30+20+6=86; Module 2: 20+60+60=140; Module 7: 90+30=120; Module 8: 30+90=120 — see
the Load check table for all nine). Real demand is unchanged at **1,613 minutes =
26.88h** (resources 1,198 + exercises 250 + assessments 165) against **1,800 minutes
= 30.00h** of capacity — **187 min = 3.12h = 10.4% slack**. Ten weeks are used,
exactly at `horizon_weeks` = 10 (**G2 passes with zero margin**). Every week stays at
or under the 198 min (3.30h) ceiling — Week 3 remains the heaviest at 191 min = 106.1%
of the 180 min target (**G1 passes**). Because the arithmetic did not move, **the
week-by-week layout is unchanged from attempt 2**; the only edits below are to the
session contents of Weeks 1, 2, 7, and 8, so a learner following this schedule opens
the actual exercise notebook `resources.md` now cites, not the tutorial/landing page
it cited before. Module 9 (the capstone) still occupies Weeks 9–10 as a contiguous
block. Slack remains 10.4%, thinner than the 15% guideline, for the same reason as
before: upstream content already uses 89.6% of the 30h cap, and I did not compress
any week's real hours to manufacture slack that doesn't exist. See Open Questions for
what I would cut first if more margin is needed.

## Findings

### Week 1 — Module 1: Working with Tabular Data & Descriptive Statistics

- **Session A (main, weekend, 96 min):** Kaggle account signup (6 min) + Exercise:
  Creating, Reading and Writing, auto-graded (30 min) + Exercise: Indexing, Selecting
  & Assigning, auto-graded (30 min) + Exercise: Summary Functions and Maps,
  auto-graded (20 min) + drill — hand-vs-pandas mean/variance/std on 10 rows
  (10 min). *(Updated from attempt 2: the two lessons formerly bundled as a single
  "Learn Pandas" tutorial read are now their own graded exercise notebooks, per
  `resources.md` attempt 3's G8 fix — durations unchanged, 30+30 in place of 60.)*
- **Session B (short, weekday, 30 min):** Application — profile a whole dataset
  (15 min) + **Module 1 checkpoint** (15 min).
- **Week total: 126 min = 2.10 h.** (unchanged)
- **Checkpoint:** Module 1 check (descriptive statistics match `.describe()`).

### Week 2 — Module 2: The Supervised Learning Workflow — Your First Model

- **Session A (main, weekend, 140 min):** scikit-learn "Getting Started" walkthrough
  (20 min) + Exercise: Your First Machine Learning Model, auto-graded (60 min) +
  Exercise: Model Validation, auto-graded (60 min). *(Updated from attempt 2: "Intro
  to Machine Learning" is no longer cited by its course-landing page; the two lessons
  it credited are now the exercise notebooks that actually carry the graded work, per
  `resources.md` attempt 3's G8 fix — durations unchanged, 60+60 in place of 120.)*
- **Session B (short, weekday, 45 min):** Drill — split instability across three
  `random_state` values (10 min) + application — first end-to-end model, honestly
  reported (20 min) + **Module 2 checkpoint** (15 min).
- **Week total: 185 min = 3.08 h.** (unchanged)
- **Checkpoint:** Module 2 check (train/test score reported honestly, split
  explained).

### Week 3 — Module 3: Classification I — Predicting Categories

- **Session A (main, weekend, 146 min):** Titanic competition-join (6 min) + Titanic
  — train a classifier, submit to the leaderboard (120 min) + Logistic Regression
  user-guide read (20 min). (no citation change this round)
- **Session B (short, weekday, 45 min):** Drill — probability by hand vs.
  `predict_proba` (10 min) + application — `predict` vs. `predict_proba` on a second
  dataset (20 min) + **Module 3 checkpoint** (15 min).
- **Week total: 191 min = 3.18 h** — the heaviest week in the plan (106.1% of the
  180 min target, within the 198 min gate ceiling).
- **Checkpoint:** Module 3 check (predict/predict_proba consistency).

### Week 4 — Cumulative Review 1 + Module 4: Evaluating Classifiers

- **Session A (main, weekend, 70 min):** Classification-metrics user guide (30 min)
  + confusion-matrix example, applied to the Module 3 classifier (30 min) + drill —
  precision/recall by hand (10 min). (no citation change this round)
- **Session B (short, weekday, 55 min):** Synthesis — choosing a metric under
  imbalance (20 min) + **Module 4 checkpoint** (15 min) + **Cumulative review 1** —
  Modules 1–3, retrieval from memory against a worked answer key (20 min).
- **Week total: 125 min = 2.08 h** — a deliberately light recovery week after two
  weeks near the ceiling.
- **Checkpoints:** Module 4 check; Cumulative review 1.

### Week 5 — Module 5: Regression I — Predicting Numbers

- **Session A (main, weekend, 126 min):** Competition-join (6 min) + House Prices —
  train a regressor, submit to the leaderboard (120 min). (no citation change this
  round)
- **Session B (short, weekday, 45 min):** Drill — residuals by hand (10 min) +
  application — a second regression dataset (20 min) + **Module 5 checkpoint**
  (15 min).
- **Week total: 171 min = 2.85 h.**
- **Checkpoint:** Module 5 check (residual sign, regression-vs-classification
  scenarios).

### Week 6 — Module 6: Evaluating Regressors + Cumulative Review 2

- **Session A (main, weekend, 90 min):** Regression-metrics user guide (30 min) +
  Plotting Cross-Validated Predictions example, applied to the Module 5 regressor
  (60 min). (no citation change this round)
- **Session B (short, weekday, 65 min):** Drill — MAE/RMSE by hand (10 min) +
  synthesis — compare two models and eyeball the residual spread (20 min) +
  **Module 6 checkpoint** (15 min) + **Cumulative review 2** — Modules 4–6,
  retrieval against a worked answer key (20 min).
- **Week total: 155 min = 2.58 h.**
- **Checkpoints:** Module 6 check; Cumulative review 2.

### Week 7 — Module 7: Overfitting, Underfitting & Generalization

- **Session A (main, weekend, 135 min):** Exercise: Cross-Validation, auto-graded
  (90 min) + scikit-learn cross-validation user guide (30 min) + drill — watch
  overfitting happen, train vs. test accuracy on a flexible vs. a simple model
  (15 min). *(Updated from attempt 2: the "Kaggle Cross-Validation lesson + linked
  graded exercise" is now cited directly as the exercise notebook itself, per
  `resources.md` attempt 3's G8 fix — duration unchanged at 90 min.)*
- **Session B (short, weekday, 50 min):** Application — cross-validation on your own
  Module 3/5 models (15 min) + synthesis — fix the overfit model (15 min) +
  **Module 7 checkpoint, hard gate** (20 min).
- **Week total: 185 min = 3.08 h.** (unchanged)
- **Checkpoint:** Module 7 check — hard go/no-go; a learner who prefers the
  higher-training-score model does not proceed to Module 8.

### Week 8 — Module 8: Feature Engineering & Preparing Real Data

- **Session A (main, weekend, 120 min):** Exercise: Categorical Variables,
  auto-graded — drop/ordinal/one-hot compared (30 min) + Exercise: Pipelines,
  auto-graded — `SimpleImputer`/`OneHotEncoder`/`StandardScaler` chained in one
  `Pipeline` (90 min). *(Updated from attempt 2: the "Pipelines lesson and its linked
  auto-graded exercise" is now cited directly as the exercise notebook itself, per
  `resources.md` attempt 3's G8 fix — duration unchanged at 90 min.)*
- **Session B (short, weekday, 45 min):** Drill — impute by hand, mean vs. median
  (10 min) + application — a full preprocessing `Pipeline` on messy data (20 min) +
  **Module 8 checkpoint** (15 min).
- **Week total: 165 min = 2.75 h.** (unchanged)
- **Checkpoint:** Module 8 check (pipeline runs end-to-end on raw data, no leakage).

### Week 9 — Module 9: Capstone, part 1 — Classifier (Adult dataset)

Contiguous capstone block begins; no other module content mixed in. The Adult
dataset (48,842 rows) is the larger of the two capstone datasets and gets the larger
share of build time. (no citation change this round)

- **Session A (main, weekend, 130 min):** Download the Adult dataset (5 min) + build
  the classification pipeline end-to-end — split, train, evaluate (accuracy,
  precision, recall) — reusing the workflow, evaluation, and pipeline patterns from
  Modules 1–8 (125 min).
- **Session B (short, weekday, 50 min):** Diagnose over/underfitting on the
  classifier (train/test gap or cross-validation), apply one mitigation, and begin
  the capstone self-audit checklist for the classifier half (50 min).
- **Week total: 180 min = 3.00 h** — exactly at target, no slack this week.
- **Checkpoint:** none separate this week — the capstone's assessment is the Final
  check, completed at the end of Week 10.

### Week 10 — Module 9: Capstone, part 2 — Regressor (Wine Quality dataset) + write-up

- **Session A (main, weekend, 90 min):** Download the Wine Quality dataset (5 min) +
  build the regression pipeline end-to-end — split, train, evaluate (MAE, RMSE),
  diagnose over/underfitting, apply one mitigation (85 min).
- **Session B (short, weekday, 40 min):** Complete the capstone self-audit checklist
  for both halves, write up the pipeline/results/mitigations for both models, and
  work through the **Final check** against the six target outcomes in
  `requirements.md` (40 min).
- **Week total: 130 min = 2.17 h** — 50 min of slack, the largest single-week margin
  in the plan, placed as the closest thing this budget affords to a buffer
  immediately before the deadline.
- **Checkpoint:** Final check (capstone classifier + regressor checklists).

### Load check

Real hours = resource time (`resources.md` attempt 3's Coverage-check table,
re-itemized line by line) + practice time (`exercises.md` Practice-load table,
unchanged) + checkpoint time (`assessments.md`, unchanged), summed per module exactly
as those artifacts state them — no re-estimation.

**Module-level arithmetic** (resource line-items re-summed from `resources.md`
attempt 3's own 19 itemized lines — verified by addition, not copied as a subtotal;
modules with a citation swap this round are marked):

| Module | Resource (min, itemized) | Practice (min) | Checkpoint (min) | Total (min) | Changed this round? |
|---|---|---|---|---|---|
| 1 | 30+30+20+6 = 86 | 10+15 = 25 | 15 | **126** | Lines re-split (30+30+20 vs. 60+20), sum identical |
| 2 | 20+60+60 = 140 | 10+20 = 30 | 15 | **185** | Lines re-split (20+60+60 vs. 120+20), sum identical |
| 3 | 120+20+6 = 146 | 10+20 = 30 | 15 | **191** | No |
| Review 1 | — | — | 20 | **20** | No |
| 4 | 30+30 = 60 | 10+20 = 30 | 15 | **105** | No |
| 5 | 120+6 = 126 | 10+20 = 30 | 15 | **171** | No |
| 6 | 30+60 = 90 | 10+20 = 30 | 15 | **135** | No |
| Review 2 | — | — | 20 | **20** | No |
| 7 | 90+30 = 120 | 15+15+15 = 45 | 20 | **185** | URL swapped (tutorial→exercise), sum identical |
| 8 | 30+90 = 120 | 10+20 = 30 | 15 | **165** | URL swapped (tutorial→exercise), sum identical |
| 9 (capstone) | 300+10 = 310 | 0 (folded into build time, per `exercises.md`) | 0 (folded into Final check, per `assessments.md`) | **310** | No |
| **Total** | **1,198** | **250** | **165** | **1,613** | Grand total unchanged |

Check: 86+140+146+60+126+90+120+120+310 = **1,198 min** (matches `resources.md`
attempt 3's own 19.97h total, computed from 19 lines instead of attempt 2's 17 —
the two citation splits in Modules 1 and 2 added a line each without changing the
sum). 25+30+30+30+30+30+45+30 = **250 min** (matches `exercises.md`'s own table,
unchanged, Module 9's 10 min excluded — it directs the capstone's own time, not
additive). 7×15 + 20 + 2×20 = **165 min** (matches `assessments.md`'s own total,
unchanged). 1,198 + 250 + 165 = **1,613 min = 26.88 h** — identical to attempt 2.

**Week-level arithmetic:**

| Week | Content | Planned | Budget (target) | Margin vs. target | ≤ G1 ceiling (198 min / 3.30 h)? |
|---|---|---|---|---|---|
| 1 | Module 1 | 126 min = 2.10 h | 180 min = 3.00 h | +54 min (+0.90 h) | Yes (126 ≤ 198, 70.0%) |
| 2 | Module 2 | 185 min = 3.08 h | 180 min = 3.00 h | −5 min (−0.08 h) | Yes (185 ≤ 198, 102.8%) |
| 3 | Module 3 | 191 min = 3.18 h | 180 min = 3.00 h | −11 min (−0.18 h) | Yes (191 ≤ 198, 106.1%) |
| 4 | Review 1 + Module 4 | 125 min = 2.08 h | 180 min = 3.00 h | +55 min (+0.92 h) | Yes (125 ≤ 198, 69.4%) |
| 5 | Module 5 | 171 min = 2.85 h | 180 min = 3.00 h | +9 min (+0.15 h) | Yes (171 ≤ 198, 95.0%) |
| 6 | Module 6 + Review 2 | 155 min = 2.58 h | 180 min = 3.00 h | +25 min (+0.42 h) | Yes (155 ≤ 198, 86.1%) |
| 7 | Module 7 | 185 min = 3.08 h | 180 min = 3.00 h | −5 min (−0.08 h) | Yes (185 ≤ 198, 102.8%) |
| 8 | Module 8 | 165 min = 2.75 h | 180 min = 3.00 h | +15 min (+0.25 h) | Yes (165 ≤ 198, 91.7%) |
| 9 | Module 9 — capstone pt. 1 | 180 min = 3.00 h | 180 min = 3.00 h | 0 min (0.00 h) | Yes (180 ≤ 198, 100.0%) |
| 10 | Module 9 — capstone pt. 2 | 130 min = 2.17 h | 180 min = 3.00 h | +50 min (+0.83 h) | Yes (130 ≤ 198, 72.2%) |
| **Total** | **9 modules + 2 reviews** | **1,613 min = 26.88 h** | **1,800 min = 30.00 h** | **+187 min (+3.12 h, 10.4% slack)** | **Yes — max week 191/198 = 96.5% of ceiling, 106.1% of target, under the 110% cap** |

Check: 126+185+191+125+171+155+185+165+180+130 = **1,613 min**, matching the
module-level total exactly — identical to attempt 2, confirming that this round's
citation swaps in `resources.md` (17→19 lines) genuinely held every module's minutes
fixed rather than merely claiming to.

### Deadline check

- Weeks used: **10**.
- `horizon_weeks`: **10**.
- 10 ≤ 10 — **fits, with zero weeks of margin.** Every module in `curriculum.md`
  (1 through 9) appears in the schedule above, and no module was split across a week
  boundary within a single session (Module 9 spans two weeks as a deliberate,
  contiguous two-week capstone block, per the coordinator's instruction, not a
  session split mid-week).

## Sources

None.

## Open Questions

- **What changed this round (attempt 3) and why no week moved.** `resources.md`
  attempt 3 fixed gate G8 by swapping four citations (Modules 1, 2, 7, 8) from
  tutorial/landing pages to the corresponding exercise notebooks, and splitting two
  two-lesson citations into per-lesson ones (17→19 resource lines). I re-summed every
  module's resource lines independently rather than trusting the "totals held fixed"
  claim in the coordinator's brief, because a reshaped resource list is exactly the
  kind of change that hid the attempt-1 G1 failure. The re-derivation confirms the
  claim exactly: all nine module totals match attempt 2's, so the only edits in this
  revision are to the session-content wording in Weeks 1, 2, 7, and 8, so a learner
  opens the exercise notebook `resources.md` now cites rather than the tutorial page
  it cited before.
- **What changed from attempt 1 to attempt 2, and why it's fixed (carried forward).**
  Attempt 1 copied `resources.md` attempt 1's Module 2 (120 min) and Module 3
  (126 min) subtotals without checking they summed their own resource lines; the true
  sums were 150 and 156 min respectively, pushing Week 3 to 201 min — over the
  198 min ceiling. `resources.md` attempt 2 fixed this with explicit per-line sums,
  which I independently verified then and have now re-verified against attempt 3's
  reshaped line list.
- **Slack is 10.4%, not the ~15% the method calls for, and there is no single empty
  buffer week.** Real demand (26.88 h) leaves 3.12 h of headroom across 10 weeks at
  3 h/week; a dedicated empty buffer week would need close to 3 h of slack
  concentrated in one place, which this plan cannot afford without exceeding G1
  elsewhere or exceeding G2's 10-week ceiling. Per the brief, I protected G1 (no week
  over 198 min) and G2 (≤10 weeks) exactly, rather than manufacture slack the
  arithmetic doesn't support. The closest approximation to a buffer is Week 10's
  50-minute margin, placed immediately before the plan ends. If more margin is
  needed, the first things I would cut, in order: (1) the Module 1, 2, 5, and 8
  drills that `exercises.md` itself names as lowest-stakes (mechanical verification,
  not the overfitting or metric-choice exercises that carry a module's real
  insight) — cutting all four reclaims 40 minutes; (2) resolving the possible
  double-count below, which could reclaim up to 165 minutes if confirmed redundant.
- **Possible double-count between Kaggle's own auto-graded exercises and
  `exercises.md`'s bespoke practice, flagged but not resolved here, now sharper.**
  `resources.md` attempt 3's Open Questions restates this flag and notes it is now
  more visible: Module 1 carries three graded Kaggle notebooks and Module 2 carries
  two, on top of `exercises.md`'s own separately budgeted practice for those modules
  (30+30 = 60 min across Modules 1–2 alone). Per this artifact's brief, I used both
  numbers as given rather than silently netting them out. If genuinely redundant
  across Modules 2, 3, 5, 7, and 8 (30+30+30+45+30 = 165 min = 2.75 h, per the
  original flag), real demand could be as low as 22.30 h (26.88 h − 2.75 h) against
  the 30 h budget, which would restore slack close to the intended 15% without
  cutting anything. This needs a decision from `curriculum-architect` or
  `exercise-designer`, not something this schedule can determine alone.
- **Weeks 2, 3, and 7 run slightly above the 180-minute target (102.8%, 106.1%, and
  102.8% respectively) though all remain well inside the 198-minute ceiling.** These
  three weeks have the least built-in catch-up room; a learner who misses part of a
  session here is more likely to feel the squeeze than in Weeks 1, 4, or 10.
- **Capstone time is split 180 min (Week 9, Adult/classifier) vs. 130 min (Week 10,
  Wine Quality/regressor), favoring the larger dataset**, matching `resources.md`'s
  note on the two datasets' size asymmetry (48,842 vs. 4,898 rows). `resources.md`
  itself notes this is not a runtime bottleneck (both train in seconds) — the extra
  time in Week 9 reflects the larger dataset's greater conceptual/exploratory
  surface, a judgement call rather than an arithmetic necessity. A learner who wants
  strictly symmetric effort across the two capstone halves could instead subsample
  Adult, per `resources.md`'s own suggestion, and rebalance the two weeks closer to
  155/155.
- **No scope was cut and no gate was broken to hit the deadline.** Both G1 and G2 are
  met as computed above; this section exists because the fit is tight (10.4% slack,
  not 15%), not because it fails.
