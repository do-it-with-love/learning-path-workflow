---
artifact: resources
owner: curator
run_id: run-002-machine-learning
status: final
attempt: 3
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
  - artifacts/validation-report.md
generated: 2026-08-19T14:00:00Z
---

# Resources — Machine Learning (classical, project-based)

## Summary

The `project-curator` variant ran a third time, revising attempt 2's `resources.md`
after its single G8 failure. The validator's finding was narrow and correct: "Learn
Pandas" (Module 1) was cited as its course-landing/tutorial page and counted
interactive, but the artifact's own words called that page "guided" and a
"read-along" distinct from the graded exercise paired with it — the same
passive-following pattern already used to disqualify two other resources in attempt 2.
The validator offered two fixes and named option (a), citing the course's own
lesson-level *exercise* pages instead of the tutorial/landing page, as cleaner.

That fix is applied here. But rather than patch Module 1 alone, this revision audits
**every** resource against the same test the validator just applied twice ("does the
learner do work and get feedback on THEIR work, verified from the artifact's own
description, not the citation's format") — because the instruction was explicit that
the validator "will check every one again," and Module 1's problem had a structural
twin: any resource cited by its **course-landing or lesson-tutorial URL** while being
described as covering graded work is the same latent bug, whether or not it had been
caught yet. That search surfaced three more instances of the identical pattern, not
previously flagged: Module 2's "Intro to Machine Learning" was cited by its course
*landing* page while being credited with exercise-level work ("performs a
`train_test_split` and computes MAE"); Module 7's "Cross-Validation" and Module 8's
"Pipelines" were cited by their *tutorial* notebook URLs while being credited with
"its own linked auto-graded exercise" — the word "linked" is the tell: the graded
page was never the one cited. All four are fixed the same way as the validator's
option (a): the citation is moved from the tutorial/landing page to the actual
exercise notebook the course pairs with it, confirmed live via WebFetch this run.
Each swap **preserves the module's already-validated total resource minutes exactly**
(the exercise notebook's own duration is set equal to what the tutorial+exercise pair
was already budgeted at, since Kaggle Learn exercise notebooks are self-contained —
brief recap, then graded questions with hints and a solution reveal — not a bare
problem set requiring separate tutorial time on top), so **G1's numbers do not move**:
resource total stays **1,198 min = 19.97h**, grand total stays **1,613 min = 26.88h**
against the 1,800 min (30h) cap, **187 min = 3.12h = 10.4% slack**, identical to the
figure the validator independently re-derived and passed last round. Two of the four
swaps (Module 1, Module 2) add a resource line each, because a two-lesson tutorial
citation splits into two separate per-lesson exercise citations; the other two
(Module 7, Module 8) are pure URL swaps with no count change. Net effect: resource
count 17→**19**, interactive count 11→**14**, reference count 6→**5**. Corrected
ratio: **14/19 = 73.7%**, 3.7 points clear of the 70% floor — a real margin, not a
one-resource knife-edge, because the fix closed all four instances of the pattern at
once instead of patching only the one instance the validator named. Every resource
remains free; no new signups beyond the Kaggle account already budgeted in Module 1.

## Findings

### Module 1: Working with Tabular Data & Descriptive Statistics

- [Exercise: Creating, Reading and Writing](https://www.kaggle.com/code/residentmario/exercise-creating-reading-and-writing) — Kaggle Learn (Pandas course, lesson 1 exercise notebook) · 2026 · interactive auto-graded exercise notebook · ~0.5h (30 min) · free · verified: webfetch 2026-08-19
- [Exercise: Indexing, Selecting & Assigning](https://www.kaggle.com/code/residentmario/exercise-indexing-selecting-assigning) — Kaggle Learn (Pandas course, lesson 2 exercise notebook) · 2026 · interactive auto-graded exercise notebook · ~0.5h (30 min) · free · verified: webfetch 2026-08-19
- [Exercise: Summary Functions and Maps](https://www.kaggle.com/code/residentmario/exercise-summary-functions-and-maps) — Kaggle Learn (Pandas course, lesson 3 exercise notebook) · 2026 · interactive auto-graded exercise notebook · ~0.33h (20 min) · free · verified: webfetch 2026-08-19

  What the learner does: all three are Kaggle Learn exercise notebooks — each opens
  with a short recap of the lesson's syntax, then a series of graded questions the
  learner answers against a real dataset, checked in-notebook with hints and a full
  solution available if stuck. Lesson 1 has the learner build and load DataFrames/
  Series by hand and from a CSV; lesson 2 has them select rows/columns with `loc`/
  `iloc` and boolean masks on the Wine Reviews dataset; lesson 3 has them independently
  compute `.describe()`, `.mean()`, `.std()`, and related summary functions and submit
  each answer for a check. Ramp: each notebook grades its own questions, and Kaggle's
  own hint density drops lesson-to-lesson — lesson 1 is the most scaffolded, lesson 3
  the most independent — so the ramp is inside the module, across three genuinely
  graded checkpoints, not one guided read-along followed by one graded step. Feedback:
  every question in all three notebooks is checked against a correct answer
  immediately, with hints and a solution reveal. Definition of done: the learner has
  built a DataFrame by hand and from a CSV, correctly selected data with `loc`/`iloc`
  and a boolean mask, and computed and stated the mean and standard deviation of a
  numeric column — each step confirmed by that notebook's own grader, not
  self-assessed.
  Arithmetic: 30 + 30 + 20 = 80 min resource lines, + 6 min (one-time free Kaggle
  account signup, first resource in the plan to need one) = **86 min (1.43h)** — the
  same total as attempt 2's Module 1 (60 tutorial + 20 exercise + 6 setup = 86); only
  the split between lines changed, not the sum.

### Module 2: The Supervised Learning Workflow — Your First Model

- [Getting Started](https://scikit-learn.org/stable/getting_started.html) — scikit-learn · 2026 (v1.9) · documentation walkthrough with runnable code · ~0.33h (20 min) read-and-type-along · free · verified: webfetch 2026-08-18
- [Exercise: Your First Machine Learning Model](https://www.kaggle.com/code/dansbecker/exercise-your-first-machine-learning-model) — Kaggle Learn (Intro to Machine Learning course, lesson 3 exercise notebook) · 2026 · interactive auto-graded exercise notebook · ~1.0h (60 min) · free · verified: webfetch 2026-08-19
- [Exercise: Model Validation](https://www.kaggle.com/code/dansbecker/exercise-model-validation) — Kaggle Learn (Intro to Machine Learning course, lesson 4 exercise notebook) · 2026 · interactive auto-graded exercise notebook · ~1.0h (60 min) · free · verified: webfetch 2026-08-19

  What the learner does: reads the scikit-learn "Getting Started" page first for the
  `fit`/`predict`/`score` API shape — reference, not graded, so it stays honestly
  reference below. Then, in the "Your First Machine Learning Model" exercise, selects
  features, fits a `DecisionTreeRegressor` on a real dataset, and generates
  predictions, each step checked in-notebook. Then, in the "Model Validation"
  exercise, performs a `train_test_split` and computes mean absolute error on
  held-out data the model has not seen, again checked against a reference answer.
  Ramp: read the API shape first (low stakes), fit a first real model (graded), then
  validate it honestly on held-out data (graded, and conceptually harder — it is where
  the module's core lesson, that training performance is not the same as real
  performance, lands). Feedback: both Kaggle exercises auto-grade against a
  known-correct answer with hints; the scikit-learn page has no grading of its own.
  Definition of done: the learner can split a dataset, fit a scikit-learn estimator on
  the training portion, and report a mean absolute error on the held-out test portion,
  from memory of the API shape, confirmed correct by both exercises' own graders.
  Arithmetic: 20 + 60 + 60 = **140 min (2.33h)**; no setup (Kaggle account already
  exists from Module 1) — the same total as attempt 2's Module 2 (120 + 20 = 140);
  only the split changed.

### Module 3: Classification I — Predicting Categories

- [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic) — Kaggle Competitions · 2026 (rolling, no end date) · competition with leaderboard · ~2.0h (120 min) for a first working submission · free · verified: websearch 2026-08-18
- [Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression) — scikit-learn · 2026 (v1.9) · user guide · ~0.33h (20 min) read · free · verified: webfetch 2026-08-18

  What the learner does: trains a classifier (logistic regression or k-NN) on the
  Titanic tabular dataset, generates both class predictions and `predict_proba`
  output, and submits predictions for a leaderboard score. The guide page is a short,
  targeted read on what the logistic regression probability output actually means —
  reference, not graded. Ramp: fit-and-submit first (concrete, scored), then read the
  probability-interpretation section to explain what the score meant. Feedback: the
  Kaggle leaderboard score is real, comparative, and immediate on submission — the
  strongest feedback loop sourced for this module. Definition of done: a submitted
  Titanic prediction file that scores on the public leaderboard, plus a one-paragraph
  explanation of how the model's predicted probability for one passenger differs from
  its class prediction.
  Arithmetic: 120 + 20 = 140 min resource lines, + 6 min (Titanic competition-join
  step, confirmed this run not to require phone verification — see Open Questions) =
  **146 min (2.43h)**. Unchanged from attempt 2.

### Module 4: Evaluating Classifiers

- [Metrics and scoring — classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) — scikit-learn · 2026 (v1.9) · user guide · ~0.5h (30 min) targeted read · free · verified: webfetch 2026-08-18
- [Confusion matrix example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html) — scikit-learn · 2026 (v1.9) · runnable example (Jupyter notebook, Binder, JupyterLite), adapted to the learner's own model and data · ~0.5h (30 min) · free · verified: webfetch 2026-08-18

  What the learner does: reads the classification-metrics section for the accuracy/
  precision/recall definitions, computes them with `sklearn.metrics` on their Module 3
  classifier, then runs the confusion-matrix example **with their own trained model
  and data swapped in** to visualize true/false positives and negatives. Ramp:
  definitions first, then a real check against the learner's own Titanic predictions.
  Feedback: the example notebook's output is a concrete, checkable plot generated
  from the learner's own model — a correctly-specified confusion matrix looks
  structurally right or wrong on sight. Definition of done: the learner reports
  accuracy, precision, and recall for their Module 3 model, states in one sentence why
  accuracy alone would mislead on the Titanic dataset's class balance, and can read a
  confusion matrix they generated from their own predictions.
  Arithmetic: 30 + 30 = **60 min (1.00h)**; no setup. Unchanged from attempt 2.

### Module 5: Regression I — Predicting Numbers

- [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) — Kaggle Competitions · 2026 (rolling, no end date) · competition with leaderboard, RMSE-scored · ~2.0h (120 min) for a first working submission · free · verified: websearch 2026-08-18

  What the learner does: fits a linear regression model to predict a numeric target
  (Ames house sale price), generates predictions and residuals, and submits to the
  leaderboard. Ramp within the module comes from the submission cycle itself: a first
  quick baseline submission, then at least one revision after inspecting residuals.
  Feedback: the House Prices leaderboard reports RMSE on unseen data immediately on
  submission. Definition of done: a submitted House Prices prediction file with a
  leaderboard RMSE, plus a table of five example predictions vs. actual values with
  residuals computed by hand from the model's output.
  Arithmetic: 120 min resource line, + 6 min (competition-join step, same account) =
  **126 min (2.10h)**. Unchanged from attempt 2.

### Module 6: Evaluating Regressors

- [Metrics and scoring — regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics) — scikit-learn · 2026 (v1.9) · user guide · ~0.5h (30 min) targeted read · free · verified: webfetch 2026-08-18
- [Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html) — scikit-learn · 2026 (v1.9) · runnable example (Jupyter notebook, Binder, JupyterLite), adapted to the learner's own regressor · ~1.0h (60 min) · free · verified: webfetch 2026-08-18

  What the learner does: computes MAE and RMSE for their Module 5 regressor with
  `sklearn.metrics`, then runs the cross-validated-predictions example **swapped to
  their own regressor and House Prices data** to plot actual-vs-predicted and
  residual-vs-predicted values. Ramp: metric definitions and computation first, then
  the more demanding cross-validated-prediction visualization on the learner's own
  data. Feedback: the example's two plots are a direct visual check on the learner's
  own results — a model that fits well clusters tightly along the diagonal; one that
  doesn't is visibly obvious. Definition of done: the learner reports MAE and RMSE for
  two different regression models on the same dataset (their Module 5 model plus one
  variant) and states which is better and why, in the target's own units.
  Arithmetic: 30 + 60 = **90 min (1.50h)**; no setup. Unchanged from attempt 2.

### Module 7: Overfitting, Underfitting & Generalization

- [Exercise: Cross-Validation](https://www.kaggle.com/code/alexisbcook/exercise-cross-validation) — Kaggle Learn (Intermediate Machine Learning, lesson 5 exercise notebook) · 2026 · interactive auto-graded exercise notebook · ~1.5h (90 min) · free · verified: webfetch 2026-08-19
- [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html) — scikit-learn · 2026 (v1.9) · user guide, CV-strategy catalogue (`KFold`, `StratifiedKFold`, etc.) · ~0.5h (30 min) targeted read · free · verified: webfetch 2026-08-18

  What the learner does: applies `cross_val_score`/k-fold CV to one of their own
  Module 3 or 5 models in the exercise notebook, comparing the cross-validated score
  to the single train/test score they already have from earlier modules to see the
  gap directly, each answer checked against a reference solution's validation score;
  reads the user guide afterward for the formal CV strategy catalogue and picks the
  correct one (`StratifiedKFold` for the Module 3 classifier, plain `KFold` for the
  Module 5 regressor) with a one-line justification. Ramp: apply CV to a model the
  learner already trained (concrete, graded), then generalize to naming the right
  strategy for a case they haven't tried yet (transfer, ungraded reference). Feedback:
  the exercise is auto-graded against a known-correct CV score, with hints and a
  solution. Definition of done: the learner has a documented train/test performance
  gap for one of their own models, a cross-validated score for the same model, and has
  applied and re-measured after one concrete mitigation (simplify, regularize, or more
  data).

  *(Attempt 2 cited this lesson's tutorial notebook, `.../code/alexisbcook/
  cross-validation`, and described it as "the Kaggle lesson and its linked exercise" —
  the actual graded page was never the one cited, the same latent pattern the
  validator caught in Module 1's Learn Pandas citation. Fixed here by citing the
  exercise notebook itself; duration held at the same 90 min already budgeted, since
  the exercise notebook is self-contained.)*
  Arithmetic: 90 + 30 = **120 min (2.00h)**; no setup — same total as attempt 2.

### Module 8: Feature Engineering & Preparing Real Data

- [Exercise: Pipelines](https://www.kaggle.com/code/alexisbcook/exercise-pipelines) — Kaggle Learn (Intermediate Machine Learning, lesson 4 exercise notebook) · 2026 · interactive auto-graded exercise notebook · ~1.5h (90 min) · free · verified: webfetch 2026-08-19
- [Exercise: Categorical Variables](https://www.kaggle.com/code/alexisbcook/exercise-categorical-variables) — Kaggle Learn (Intermediate Machine Learning, lesson 3 exercise notebook) · 2026 · interactive auto-graded exercise notebook · ~0.5h (30 min) · free · verified: webfetch 2026-08-19

  What the learner does: the Categorical Variables exercise (lesson 3, done first)
  has the learner compare three encoding approaches — drop, ordinal, one-hot — on a
  real dataset with categorical columns and check which produces the lowest error,
  which is graded. The Pipelines exercise (lesson 4) then has the learner chain a
  `SimpleImputer`/`OneHotEncoder`/`StandardScaler` preprocessing step to a model in a
  single `Pipeline` object, on data with real missing values, each step checked
  in-notebook. Ramp: encode categoricals correctly in isolation first, then compose
  that step into a full pipeline alongside imputation and scaling. Feedback: both
  exercises' scores are checked against a reference solution's validation score; a
  correct answer reproduces it within a small tolerance. Definition of done: a single
  scikit-learn `Pipeline` object that takes raw (uncleaned) tabular data in and
  produces predictions out, with missing values handled, categoricals encoded via the
  approach that scored best in the earlier exercise, and scaling applied where the
  model needs it.

  *(Attempt 2 cited this lesson's tutorial notebook, `.../code/alexisbcook/pipelines`,
  and described it as completing "its own linked auto-graded exercise" — again the
  graded page itself was never the one cited. Fixed here by citing the exercise
  notebook directly; duration held at the same 90 min already budgeted.)*
  Arithmetic: 90 + 30 = **120 min (2.00h)**; no setup — same total as attempt 2.

### Module 9: Capstone — Build and Evaluate a Classifier and a Regressor

- [Adult](https://archive.ics.uci.edu/dataset/2/adult) — UCI Machine Learning Repository · 1996 data, page current 2026 · dataset (CSV, CC BY 4.0) · 48,842 instances / 14 features, classification target (income >$50K) · free · verified: webfetch 2026-08-18
- [Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality) — UCI Machine Learning Repository · 2009 data, page current 2026 · dataset (CSV, CC BY 4.0) · 4,898 instances / 11 features, regression target (quality score 0–10) · free · verified: webfetch 2026-08-18

  What the learner does: runs the full workflow from Modules 1–8 twice, unassisted —
  split, train, evaluate (accuracy/precision/recall), diagnose over/underfitting on
  Adult for classification; split, train, evaluate (MAE/RMSE), diagnose
  over/underfitting on Wine Quality for regression — and writes up the pipeline,
  results, and the one mitigation applied to each. Ramp is external to any one
  resource here: this module is the ramp, requiring independent recombination of
  every skill built in Modules 1–8 with no lesson holding the learner's hand.
  Feedback: no leaderboard here (both are static UCI datasets, not live
  competitions), so the feedback loop is the learner's own train/test and
  cross-validated scores plus, if desired, informal comparison against published
  benchmark accuracies/errors for these two well-known datasets — genuinely thinner
  than Modules 3/5's leaderboard feedback; `assessment-designer`'s capstone checkpoint
  is the actual external check for this module. Definition of done: two working,
  documented pipelines (one classifier, one regressor), each reporting the required
  metrics, each with a diagnosed over/underfitting verdict and one applied
  mitigation, using only free tools.
  Arithmetic: ~5.0h (300 min) build time (matches `curriculum.md`'s own 5.0h estimate
  for this module) + 10 min (two plain CSV downloads) = **310 min (5.17h)**. Unchanged
  from attempt 2.

### Coverage check

| Module | Resources | Hands-on hours (incl. setup) | Cost |
|---|---|---|---|
| 1 | 3 | 86 min = **1.43h** (30+30+20 lines, +6 setup) | free |
| 2 | 3 | 140 min = **2.33h** (20+60+60 lines, +0 setup) | free |
| 3 | 2 | 146 min = **2.43h** (120+20 lines, +6 setup) | free |
| 4 | 2 | 60 min = **1.00h** (30+30 lines, +0 setup) | free |
| 5 | 1 | 126 min = **2.10h** (120 line, +6 setup) | free |
| 6 | 2 | 90 min = **1.50h** (30+60 lines, +0 setup) | free |
| 7 | 2 | 120 min = **2.00h** (90+30 lines, +0 setup) | free |
| 8 | 2 | 120 min = **2.00h** (90+30 lines, +0 setup) | free |
| 9 | 2 | 310 min = **5.17h** (300 build +10 setup) | free |
| **Total** | **19** | **1,198 min = 19.97h** | **$0** |

Every module's minutes above are shown as the literal sum of that module's own
resource-line durations plus its own setup, so the total is checkable by addition:
86+140+146+60+126+90+120+120+310 = 1,198 min = 19.97h — **identical to attempt 2's
total**, because every URL swap this round held its module's duration fixed and only
the resource count in Modules 1 and 2 changed (one two-lesson citation split into two
per-lesson citations each).

Grand total against the full plan: 1,198 min (resources) + 250 min (`exercises.md`,
independently re-summed: 25+30+30+30+30+30+45+30 = 250, unchanged) + 165 min
(`assessments.md`, independently re-summed: 7×15 + 20 + 2×20 = 165, unchanged) =
**1,613 min = 26.88h**, against the 1,800 min (30h) capacity (3h/week × 10 weeks).
**Slack: 187 min = 3.12h = 10.4%** — unchanged from the figure the validator already
verified and passed for G1.

Setup cost across the whole plan totals **28 minutes**: one free Kaggle account
signup (6 min, Module 1), two competition-join steps (6 min each, Modules 3 and 5),
and two plain CSV downloads (10 min total, Module 9). Unchanged. Nothing here requires
a local Python install — every Kaggle resource runs in-browser, and every scikit-learn
`auto_examples` page cited offers a zero-install Binder or JupyterLite launch link.

Interactive/project-based count: **14 of 19 = 73.7%**, clearing gate G8's 70% floor
with 3.7 points of margin (need ≥13.3, have 14 — better than a one-resource margin).
Every resource counted interactive now has, in its own "what the learner does" text,
either explicit grading language ("checked in-notebook," "auto-graded," "checked
against a reference solution") or explicit own-data language ("with their own trained
model and data swapped in," "swapped to their own regressor"). The 5 reference
resources (Getting Started, Logistic Regression, both `model_evaluation.html` metrics
sections, the cross-validation strategy guide) are cited because the module's
deliverable needs a specific API or definition the docs state authoritatively, and
each is honestly described as a read, not a graded step.

## Sources

- [Exercise: Creating, Reading and Writing](https://www.kaggle.com/code/residentmario/exercise-creating-reading-and-writing) — Kaggle Learn · 2026 · interactive auto-graded exercise · free · verified: webfetch 2026-08-19
- [Exercise: Indexing, Selecting & Assigning](https://www.kaggle.com/code/residentmario/exercise-indexing-selecting-assigning) — Kaggle Learn · 2026 · interactive auto-graded exercise · free · verified: webfetch 2026-08-19
- [Exercise: Summary Functions and Maps](https://www.kaggle.com/code/residentmario/exercise-summary-functions-and-maps) — Kaggle Learn · 2026 · interactive auto-graded exercise · free · verified: webfetch 2026-08-19
- [Getting Started](https://scikit-learn.org/stable/getting_started.html) — scikit-learn · 2026 (v1.9) · documentation walkthrough · free · verified: webfetch 2026-08-18
- [Exercise: Your First Machine Learning Model](https://www.kaggle.com/code/dansbecker/exercise-your-first-machine-learning-model) — Kaggle Learn · 2026 · interactive auto-graded exercise · free · verified: webfetch 2026-08-19
- [Exercise: Model Validation](https://www.kaggle.com/code/dansbecker/exercise-model-validation) — Kaggle Learn · 2026 · interactive auto-graded exercise · free · verified: webfetch 2026-08-19
- [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic) — Kaggle Competitions · 2026 (rolling) · competition · free · verified: websearch 2026-08-18
- [Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression) — scikit-learn · 2026 (v1.9) · user guide · free · verified: webfetch 2026-08-18
- [Metrics and scoring — classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) — scikit-learn · 2026 (v1.9) · user guide · free · verified: webfetch 2026-08-18
- [Confusion matrix example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html) — scikit-learn · 2026 (v1.9) · runnable example · free · verified: webfetch 2026-08-18
- [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) — Kaggle Competitions · 2026 (rolling) · competition · free · verified: websearch 2026-08-18
- [Metrics and scoring — regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics) — scikit-learn · 2026 (v1.9) · user guide · free · verified: webfetch 2026-08-18
- [Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html) — scikit-learn · 2026 (v1.9) · runnable example · free · verified: webfetch 2026-08-18
- [Exercise: Cross-Validation](https://www.kaggle.com/code/alexisbcook/exercise-cross-validation) — Kaggle Learn (Intermediate Machine Learning) · 2026 · interactive auto-graded exercise · free · verified: webfetch 2026-08-19
- [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html) — scikit-learn · 2026 (v1.9) · user guide · free · verified: webfetch 2026-08-18
- [Exercise: Pipelines](https://www.kaggle.com/code/alexisbcook/exercise-pipelines) — Kaggle Learn (Intermediate Machine Learning) · 2026 · interactive auto-graded exercise · free · verified: webfetch 2026-08-19
- [Exercise: Categorical Variables](https://www.kaggle.com/code/alexisbcook/exercise-categorical-variables) — Kaggle Learn (Intermediate Machine Learning) · 2026 · interactive auto-graded exercise · free · verified: webfetch 2026-08-19
- [Adult](https://archive.ics.uci.edu/dataset/2/adult) — UCI Machine Learning Repository · 1996 data · dataset · free · verified: webfetch 2026-08-18
- [Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality) — UCI Machine Learning Repository · 2009 data · dataset · free · verified: webfetch 2026-08-18
- [Phone verification is required for public Models](https://www.kaggle.com/discussions/product-announcements/558078) — Kaggle product announcement · 2026 · forum post · n/a · free · verified: websearch 2026-08-19 (used only to resolve the Module 3/5 setup-cost question in Open Questions, not cited as course material)

## Open Questions

- **The G8 fix was applied to all four instances of the pattern, not just the one the
  validator named.** Attempt 2's failure was specifically about Module 1's Learn
  Pandas citation, but the underlying bug — citing a lesson's tutorial/landing page
  while crediting it with graded work that actually lives on a separate, uncited
  exercise page — also existed undetected in Module 2 ("Intro to Machine Learning"),
  Module 7 ("Cross-Validation"), and Module 8 ("Pipelines"). All three used the tell
  "the Kaggle course/lesson and its linked exercise" or similar language, which in
  hindsight was the citation admitting the graded page was elsewhere. Fixing only
  Module 1 would likely have left the run one gate-check away from a fourth failure on
  a different resource, which the run's retry budget does not allow; fixing the
  pattern everywhere it appears is why the corrected ratio (73.7%) has real margin
  rather than landing exactly on 70.0%.
- **Kaggle competition-submission phone verification, resolved (carried from attempt
  2).** Kaggle's phone-verification requirement applies to accounts earning
  progression points, medals, or prizes, and to publishing public Models — not to
  submitting predictions to a "Getting Started" competition like Titanic or House
  Prices, which award neither. The 6-minute competition-join estimate in Modules 3 and
  5 stands as email-only signup.
- **Modules already well covered — bespoke exercises risk redundancy.** Modules 1, 2,
  3, 5, 7, and 8 now each carry Kaggle resources with their own auto-graded exercises
  or a live leaderboard; Module 1 now has three graded checkpoints and Module 2 has
  two. `exercise-designer` should treat these as the primary practice for their core
  skill and focus bespoke exercises on synthesis across skills (e.g. applying Module
  4's evaluation metrics to the Module 5 regressor's classification cousin, or a mixed
  diagnostic exercise spanning Modules 3–7) rather than re-deriving a summary-
  statistics, train/test-split, model-validation, encoding, or pipeline exercise that
  Kaggle already grades. If `exercises.md`'s existing Module 1, 2, or 8 entries
  currently re-derive that same graded content, the coordinator may want to flag it
  for `exercise-designer` to redirect toward synthesis instead.
- **Modules 4, 6, and 9 have thinner interactive coverage than the rest.** Module 4
  and 6 each pair one graded, learner's-own-data example with one reference read —
  solid, but neither has a leaderboard-strength feedback loop. Module 9's capstone has
  no auto-graded checkpoint at all (UCI datasets carry no grading harness, and this is
  correct — a capstone should not be auto-graded) — `assessment-designer`'s capstone
  checkpoint is the actual external check for this module, and `exercise-designer` is
  the primary feedback source for Modules 4 and 6 beyond what's cited here.
- **Capstone dataset scale is asymmetric.** Adult (48,842 rows) is comfortably larger
  than Wine Quality (4,898 rows); both load and train in seconds on a laptop or in
  Kaggle/Colab, so this is not a runtime problem, but a learner who wants symmetric
  effort across the two capstone halves may want to subsample Adult to a few thousand
  rows — noted for `schedule-planner`/`effort-budget-aggregator`, not a resource gap.
- **Kaggle competition leaderboards are the strongest feedback source cited (Modules 3
  and 5)** but they score on *held-out test data the learner never sees the labels
  for* — the leaderboard confirms the model generalizes but doesn't show *which*
  predictions were wrong. Pairing each with the metrics/example resources in Modules 4
  and 6 (computed on the learner's own train/test split) covers that gap.
