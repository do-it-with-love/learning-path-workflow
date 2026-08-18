---
artifact: resources
owner: curator
run_id: run-002-machine-learning
status: final
attempt: 1
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
generated: 2026-08-18T00:00:00Z
---

# Resources — Machine Learning (classical, project-based)

## Summary

The `project-curator` variant ran (the learner's confirmed `preferred_modality` is
`project`). Resources are drawn from two providers that between them cover the whole
budget for free: **Kaggle** (Kaggle Learn micro-courses, competitions, and individual
lesson notebooks — browser-based, zero-install, auto-graded exercises and leaderboard
feedback) and the **official scikit-learn documentation** (user guide chapters and
`auto_examples` pages, several of which are runnable in-browser via Binder/JupyterLite
with no local install). The capstone draws two real tabular datasets directly from the
**UCI Machine Learning Repository**. All 17 resources are free with no signup cost
beyond a free Kaggle account (email only, no card, no phone verification needed for
CPU-only notebooks) — the zero budget (gate G3) is met exactly, at $0 total. 12 of 17
resources (70.6%) are interactive or project-based — auto-graded Kaggle exercises,
competitions with leaderboard feedback, or runnable scikit-learn example notebooks —
meeting gate G8's 70% floor; the remaining 5 are official reference documentation cited
because the module's core deliverable is a specific API (metrics functions, pipeline
composition) that the docs define authoritatively. Setup cost is near-zero throughout:
Kaggle notebooks and scikit-learn's Binder/JupyterLite links both run in the browser,
and the two capstone datasets are plain CSV downloads.

## Findings

### Module 1: Working with Tabular Data & Descriptive Statistics

- [Learn Pandas](https://www.kaggle.com/learn/pandas) — Kaggle Learn · 2026 · interactive notebook course · ~4h full course / ~1.5h for the lessons this module needs (Creating/Reading/Writing, Indexing, Summary Functions) · free · verified: websearch 2026-08-18

  What the learner does: works through short tutorial pages interleaved with
  auto-graded coding exercises on real datasets (loading a CSV, inspecting shape and
  dtypes, computing `.describe()`, mean, and standard deviation on numeric columns).
  Feedback: exercises are checked in-notebook against the correct answer immediately,
  with hints and a solution reveal. Definition of done: the learner has loaded at
  least one real CSV into a DataFrame, produced a summary table of numeric and
  categorical columns, and correctly stated the mean and standard deviation of one
  numeric column in their own words.

### Module 2: The Supervised Learning Workflow — Your First Model

- [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) — Kaggle Learn · 2026 · interactive notebook course · ~3h full course / ~2h for the lessons this module needs (Model Validation, first model fit) · free · verified: websearch 2026-08-18
- [Getting Started](https://scikit-learn.org/stable/getting_started.html) — scikit-learn · 2026 (v1.9) · documentation walkthrough with runnable code · ~0.5h read-and-type-along · free · verified: webfetch 2026-08-18

  What the learner does: fits their first scikit-learn estimator end-to-end
  (`fit`/`predict`/`score`), then in the Kaggle course performs a `train_test_split`
  and computes mean absolute error on held-out data. The scikit-learn page is the
  reference for the exact `fit`/`predict`/`score` and `train_test_split` API surface.
  Feedback: Kaggle's exercise auto-grades the split and score against a known-correct
  answer; the scikit-learn page is reference material with no grading of its own.
  Definition of done: the learner can split a dataset, fit any scikit-learn estimator
  on the training portion, and report its `.score()` or an error metric on the test
  portion, from memory of the API shape, not by copying a snippet.

### Module 3: Classification I — Predicting Categories

- [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic) — Kaggle Competitions · 2026 (rolling, no end date) · competition with leaderboard · ~2h for a first working submission · free · verified: websearch 2026-08-18
- [Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression) — scikit-learn · 2026 (v1.9) · user guide · ~0.5h read · free · verified: webfetch 2026-08-18

  What the learner does: trains a classifier (logistic regression or k-NN) on the
  Titanic tabular dataset, generates both class predictions and `predict_proba`
  output, and submits predictions for a leaderboard score. The guide page is the
  reference for what the logistic regression probability output actually means.
  Feedback: the Kaggle leaderboard score is real, comparative, and immediate on
  submission — the strongest feedback loop sourced for this module. Definition of
  done: a submitted Titanic prediction file that scores on the public leaderboard,
  plus a one-paragraph explanation of how the model's predicted probability for one
  passenger differs from its class prediction.

### Module 4: Evaluating Classifiers

- [Metrics and scoring — classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) — scikit-learn · 2026 (v1.9) · user guide · ~1h read-and-apply · free · verified: webfetch 2026-08-18
- [Confusion matrix example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html) — scikit-learn · 2026 (v1.9) · runnable example (Jupyter notebook, Binder, JupyterLite) · ~0.5h · free · verified: webfetch 2026-08-18

  What the learner does: computes accuracy, precision, and recall with
  `sklearn.metrics` on their Module 3 classifier, then runs the confusion-matrix
  example (swapping in their own model and data) to visualize true/false positives
  and negatives. Feedback: the example notebook's output is a concrete, checkable
  plot — a correctly-specified confusion matrix looks structurally right or wrong on
  sight, and running it against their own Titanic model gives a real check. Definition
  of done: the learner reports accuracy, precision, and recall for their Module 3
  model, states in one sentence why accuracy alone would mislead on the Titanic
  dataset's class balance, and can read a confusion matrix they generated.

### Module 5: Regression I — Predicting Numbers

- [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) — Kaggle Competitions · 2026 (rolling, no end date) · competition with leaderboard, RMSE-scored · ~2h for a first working submission · free · verified: websearch 2026-08-18
- [Linear regression example (OLS / Ridge)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html) — scikit-learn · 2026 (v1.9) · runnable example (Jupyter notebook, Binder, JupyterLite) · ~0.5h · free · verified: webfetch 2026-08-18

  What the learner does: fits a linear regression model to predict a numeric target
  (Ames house sale price), generates predictions and residuals, and submits to the
  leaderboard; the scikit-learn example demonstrates the same estimator on a second,
  simpler dataset (diabetes) so the pattern is seen twice, once realistic and once
  minimal. Feedback: the House Prices leaderboard reports RMSE on unseen data
  immediately on submission. Definition of done: a submitted House Prices prediction
  file with a leaderboard RMSE, plus a table of five example predictions vs. actual
  values with residuals computed by hand from the model's output.

### Module 6: Evaluating Regressors

- [Metrics and scoring — regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics) — scikit-learn · 2026 (v1.9) · user guide · ~0.5h read-and-apply · free · verified: webfetch 2026-08-18
- [Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html) — scikit-learn · 2026 (v1.9) · runnable example (Jupyter notebook, Binder, JupyterLite) · ~1h · free · verified: webfetch 2026-08-18

  What the learner does: computes MAE and RMSE for their Module 5 regressor with
  `sklearn.metrics`, then runs the cross-validated-predictions example (swapped to
  their own regressor) to plot actual-vs-predicted and residual-vs-predicted values.
  Feedback: the example's two plots are a direct visual check — a model that fits
  well clusters tightly along the diagonal; one that doesn't is visibly obvious.
  Definition of done: the learner reports MAE and RMSE for two different regression
  models on the same dataset (their Module 5 model plus one variant) and states which
  is better and why, in the target's own units.

### Module 7: Overfitting, Underfitting & Generalization

- [Cross-Validation](https://www.kaggle.com/code/alexisbcook/cross-validation) — Kaggle Learn (Intermediate Machine Learning, lesson notebook) · 2026 · interactive tutorial + linked graded exercise · ~1.5h · free · verified: webfetch 2026-08-18
- [Underfitting vs. Overfitting example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html) — scikit-learn · 2026 (v1.9) · runnable example (Jupyter notebook, Binder, JupyterLite) · ~0.5h · free · verified: webfetch 2026-08-18
- [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html) — scikit-learn · 2026 (v1.9) · user guide · ~1h read · free · verified: webfetch 2026-08-18

  What the learner does: runs the polynomial-degree example to see underfitting
  (degree 1), a good fit (degree 4), and overfitting (degree 15) quantified by MSE
  side by side, applies `cross_val_score`/k-fold CV to one of their own Module 3 or 5
  models via the Kaggle lesson and exercise, and reads the user guide for the CV
  strategy catalogue (`KFold`, `StratifiedKFold`, etc.). Feedback: the Kaggle exercise
  is auto-graded against a known-correct CV score; the scikit-learn example's MSE
  values make over/underfitting numerically undeniable rather than a matter of
  opinion. Definition of done: the learner has a documented train/test performance
  gap (or learning curve) for one of their own models, a cross-validated score for the
  same model, and has applied and re-measured after one concrete mitigation
  (simplify, regularize, or more data).

### Module 8: Feature Engineering & Preparing Real Data

- [Pipelines](https://www.kaggle.com/code/alexisbcook/pipelines) — Kaggle Learn (Intermediate Machine Learning, lesson notebook) · 2026 · interactive tutorial + linked graded exercise · ~1.5h · free · verified: webfetch 2026-08-18

  What the learner does: builds a scikit-learn `Pipeline` that chains a
  `SimpleImputer`/`OneHotEncoder`/`StandardScaler` preprocessing step to a model,
  on a dataset with real missing values and categorical columns, then completes the
  linked auto-graded exercise. Feedback: the exercise's score is checked against a
  reference solution's validation score; a correctly-built pipeline reproduces it
  within a small tolerance. Definition of done: a single scikit-learn `Pipeline`
  object that takes raw (uncleaned) tabular data in and produces predictions out,
  with missing values handled, categoricals encoded, and scaling applied where the
  model needs it.

### Module 9: Capstone — Build and Evaluate a Classifier and a Regressor

- [Adult](https://archive.ics.uci.edu/dataset/2/adult) — UCI Machine Learning Repository · 1996 data, page current 2026 · dataset (CSV, CC BY 4.0) · 48,842 instances / 14 features, classification target (income >$50K) · free · verified: webfetch 2026-08-18
- [Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality) — UCI Machine Learning Repository · 2009 data, page current 2026 · dataset (CSV, CC BY 4.0) · 4,898 instances / 11 features, regression target (quality score 0–10) · free · verified: webfetch 2026-08-18

  What the learner does: runs the full workflow from Modules 1–8 twice, unassisted —
  split, train, evaluate (accuracy/precision/recall), diagnose over/underfitting on
  Adult for classification; split, train, evaluate (MAE/RMSE), diagnose
  over/underfitting on Wine Quality for regression — and writes up the pipeline,
  results, and the one mitigation applied to each. Feedback: no leaderboard here (both
  are static UCI datasets, not live competitions), so the feedback loop is the
  learner's own train/test and cross-validated scores plus, if desired, informal
  comparison against published benchmark accuracies/errors for these two well-known
  datasets. Definition of done: two working, documented pipelines (one classifier,
  one regressor), each reporting the required metrics, each with a diagnosed
  over/underfitting verdict and one applied mitigation, using only free tools.

### Coverage check

| Module | Resources | Hands-on hours (incl. setup) | Cost |
|---|---|---|---|
| 1 | 1 | ~1.6h (1.5h course lessons + ~0.1h Kaggle account setup) | free |
| 2 | 2 | ~2.0h (Kaggle lessons + doc read; setup ~0h, account already exists) | free |
| 3 | 2 | ~2.1h (2.0h competition + read; ~0.1h competition join) | free |
| 4 | 2 | ~1.5h (metrics read + example run) | free |
| 5 | 2 | ~2.5h (2.0h competition + 0.5h example) | free |
| 6 | 2 | ~1.5h (metrics read + example run) | free |
| 7 | 3 | ~3.0h (1.5h Kaggle lesson/exercise + 0.5h example + 1.0h guide read) | free |
| 8 | 1 | ~1.5h (Kaggle lesson + exercise) | free |
| 9 | 2 | ~5.0h build time + ~0.2h dataset download (no other setup) | free |
| **Total** | **17** | **~20.9h** against 25.5h of module-estimated content (curriculum reserves the remainder for the exercises `exercise-designer` will add on top) | **$0** |

Total cost is $0, meeting the hard zero-budget constraint (gate G3). Setup cost across
the whole plan is under 30 minutes total: a free Kaggle account (email only, no card, no
phone step needed since nothing here requires internet-enabled or GPU notebooks) and two
CSV downloads from UCI. Nothing here requires a local Python install — every Kaggle
resource runs in-browser, and every scikit-learn `auto_examples` page cited offers a
zero-install Binder or JupyterLite launch link, so a lost or broken local environment
never blocks a session.

## Sources

- [Learn Pandas](https://www.kaggle.com/learn/pandas) — Kaggle Learn · 2026 · interactive notebook course · ~4h full course · free · verified: websearch 2026-08-18
- [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) — Kaggle Learn · 2026 · interactive notebook course · ~3h full course · free · verified: websearch 2026-08-18
- [Getting Started](https://scikit-learn.org/stable/getting_started.html) — scikit-learn · 2026 (v1.9) · documentation walkthrough · ~0.5h · free · verified: webfetch 2026-08-18
- [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic) — Kaggle Competitions · 2026 (rolling) · competition · ~2h for first submission · free · verified: websearch 2026-08-18
- [Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression) — scikit-learn · 2026 (v1.9) · user guide · ~0.5h · free · verified: webfetch 2026-08-18
- [Metrics and scoring — classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) — scikit-learn · 2026 (v1.9) · user guide · ~1h · free · verified: webfetch 2026-08-18
- [Confusion matrix example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html) — scikit-learn · 2026 (v1.9) · runnable example · ~0.5h · free · verified: webfetch 2026-08-18
- [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) — Kaggle Competitions · 2026 (rolling) · competition · ~2h for first submission · free · verified: websearch 2026-08-18
- [Linear regression example (OLS / Ridge)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html) — scikit-learn · 2026 (v1.9) · runnable example · ~0.5h · free · verified: webfetch 2026-08-18
- [Metrics and scoring — regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics) — scikit-learn · 2026 (v1.9) · user guide · ~0.5h · free · verified: webfetch 2026-08-18
- [Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html) — scikit-learn · 2026 (v1.9) · runnable example · ~1h · free · verified: webfetch 2026-08-18
- [Cross-Validation](https://www.kaggle.com/code/alexisbcook/cross-validation) — Kaggle Learn (Intermediate Machine Learning) · 2026 · interactive tutorial + exercise · ~1.5h · free · verified: webfetch 2026-08-18
- [Underfitting vs. Overfitting example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html) — scikit-learn · 2026 (v1.9) · runnable example · ~0.5h · free · verified: webfetch 2026-08-18
- [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html) — scikit-learn · 2026 (v1.9) · user guide · ~1h · free · verified: webfetch 2026-08-18
- [Pipelines](https://www.kaggle.com/code/alexisbcook/pipelines) — Kaggle Learn (Intermediate Machine Learning) · 2026 · interactive tutorial + exercise · ~1.5h · free · verified: webfetch 2026-08-18
- [Adult](https://archive.ics.uci.edu/dataset/2/adult) — UCI Machine Learning Repository · 1996 data · dataset · free · verified: webfetch 2026-08-18
- [Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality) — UCI Machine Learning Repository · 2009 data · dataset · free · verified: webfetch 2026-08-18

## Open Questions

- **Modules already well covered — bespoke exercises risk redundancy.** Modules 2, 3,
  5, 7, and 8 each already carry a Kaggle resource with its own auto-graded exercise or
  live leaderboard. `exercise-designer` should treat these as the primary practice for
  their core skill and focus bespoke exercises on synthesis across skills (e.g.
  applying Module 4's evaluation metrics to the Module 5 regressor's classification
  cousin, or a mixed diagnostic exercise spanning Modules 3–7) rather than re-deriving
  a train/test-split or pipeline exercise that Kaggle already grades.
- **Modules 1, 4, 6, and 9 have thinner interactive coverage.** Module 1's descriptive
  statistics work and Module 9's capstone have no auto-graded checkpoint at all (Kaggle
  Learn has no dedicated descriptive-statistics course, and UCI datasets carry no
  grading harness) — `exercise-designer` and `assessment-designer` are the actual
  feedback loop for these two modules; the resources here supply the material to
  practice on, not the check that the learner got it right. Flagging so those two
  agents weight accordingly.
- **Two resource pairs were cut from Modules 1 and 8 to hold gate G8's 70% interactive
  floor.** Module 1 would ideally also cite scikit-learn's `datasets` loading-utilities
  guide (toy datasets to inspect) and Module 8 would ideally also cite the
  `Pipelines and composite estimators` user guide (formal `ColumnTransformer` API) —
  both were verified to exist (webfetch, 2026-08-18) but adding them back would drop
  the interactive ratio to 63–65%, under gate G8's floor. Either can be added back on
  request if a learner wants the formal API reference alongside the hands-on lesson;
  omitting them costs nothing functional since the Kaggle lesson notebooks in both
  modules already demonstrate the equivalent code.
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
