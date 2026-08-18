---
artifact: curriculum
owner: curriculum-architect
run_id: run-002-machine-learning
status: final
attempt: 1
inputs:
  - artifacts/requirements.md
  - artifacts/baseline-assessment.md
generated: 2026-08-18T00:00:00Z
---

# Curriculum — Machine Learning (classical, project-based)

## Summary

Nine modules, the last a capstone, taking the learner from the assessed L0 (pre-ML)
baseline to L3 (independent practitioner) on the four-level scale defined in
`baseline-assessment.md`. Progression moves one level at a time — L0 → L1 → L1 → L2 →
L2 → L2 → L3 → L3 → L3 — never skipping a level within the linear module sequence.
Statistics is not a standalone module: mean/variance/standard deviation lands in
Module 1 (needed the moment any dataset is summarized), basic probability lands in
Module 3 (needed to read `predict_proba` output), and the normal distribution lands
in Module 6 (needed to judge whether regression residuals look typical). Module 1
starts from data handling and descriptive statistics rather than "ML" proper, because
none of the six baseline gaps — pandas/CSV handling, mean/variance, probability,
distributions, the train/test paradigm, and scikit-learn itself — can be assumed, and
Module 2 gets a working fitted model on the board in week 2 so the path doesn't open
with three weeks of theory. Total estimated content is 25.5 hours against a
30-hour budget (3h × 10 weeks), leaving 4.5 hours (15%) of slack as instructed.
Deliberately left out: everything not classical/tabular (deep learning, images, text),
unsupervised learning, and most tuning/deployment/interpretability tooling — the
budget has no room for it and the goal doesn't require it.

## Findings

### Modules

| # | Title | Objectives | Prerequisites | Level | Estimated hours |
|---|---|---|---|---|---|
| 1 | Working with Tabular Data & Descriptive Statistics | Load a CSV into a pandas DataFrame and inspect its shape, columns, and dtypes. · Compute and interpret mean, variance, and standard deviation for numeric columns. · Identify categorical vs. numeric columns and produce a simple summary table for a dataset. | baseline | L0 | 2.5 |
| 2 | The Supervised Learning Workflow — Your First Model | Explain the difference between training and testing a model and why data is split into two sets. · Perform a train/test split with scikit-learn's `train_test_split`. · Fit a scikit-learn model end-to-end (`fit`/`predict`/`score`) on a clean dataset and report its default score. | 1 | L1 | 2.5 |
| 3 | Classification I — Predicting Categories | Train a classification model (e.g. logistic regression or k-NN) with scikit-learn on a tabular dataset. · Explain basic probability (relative frequency, complement) well enough to read `predict_proba` output. · Generate class predictions and predicted probabilities for the same inputs and explain how they differ. | 2 | L1 | 3.0 |
| 4 | Evaluating Classifiers | Compute accuracy, precision, and recall for a trained classifier with scikit-learn's `metrics` module. · Construct and read a confusion matrix. · Explain why accuracy alone can mislead on an imbalanced dataset and pick a more appropriate metric. | 3 | L2 | 2.5 |
| 5 | Regression I — Predicting Numbers | Train a regression model (e.g. linear regression) with scikit-learn on a tabular dataset. · Distinguish a regression target from a classification target and pick the matching scikit-learn estimator. · Generate predictions from a fitted regressor and compute residuals (prediction − actual). | 2 | L2 | 2.5 |
| 6 | Evaluating Regressors | Compute MAE and RMSE for a trained regressor and interpret them in the units of the target. · Explain, at an introductory level, what a normal distribution is and use it to judge whether a set of residuals looks typical or unusual. · Compare two regression models on the same dataset using a consistent error metric. | 5 | L2 | 2.0 |
| 7 | Overfitting, Underfitting & Generalization | Explain the bias–variance tradeoff and connect it to overfitting (high variance) and underfitting (high bias). · Diagnose overfitting vs. underfitting on a model from Module 3 or 5 using the train/test performance gap or a learning curve. · Apply k-fold cross-validation with scikit-learn and explain why it is a more reliable estimate than a single split. · Apply at least one concrete mitigation (simplify the model, regularize, get more data) to a model that is overfitting. | 4, 6 | L3 | 3.5 |
| 8 | Feature Engineering & Preparing Real Data | Handle missing values and encode categorical variables with scikit-learn preprocessing tools. · Apply feature scaling and explain when it matters (distance-based or regularized models). · Build a scikit-learn `Pipeline` that chains preprocessing and a model together. | 7 | L3 | 2.0 |
| 9 | Capstone — Build and Evaluate a Classifier and a Regressor | Complete an end-to-end classification workflow on a chosen or provided tabular dataset: split, train, evaluate (accuracy/precision/recall), diagnose over/underfitting. · Complete an end-to-end regression workflow on a second (or the same) dataset: split, train, evaluate (MAE/RMSE), diagnose over/underfitting. · Document the pipeline, results, and at least one mitigation applied, using only free tools and resources. | 1–8 | L3 | 5.0 |

**Total: 25.5 hours** against a 30-hour budget (3h/week × 10 weeks) — 4.5 hours (15%)
held back as slack, per the brief.

### Outcome coverage

| Target outcome (`requirements.md`) | Delivered by module(s) |
|---|---|
| 1. Apply train/test split; recognize when cross-validation is warranted | 2, 7 |
| 2. Train a classifier and evaluate with accuracy/precision/recall | 3, 4 |
| 3. Train a regressor and evaluate with an appropriate error metric (MAE/RMSE) | 5, 6 |
| 4. Diagnose overfitting vs. underfitting and describe a mitigation | 7 |
| 5. Apply just-enough statistics (mean/variance, probability, distributions) in context | 1 (mean/variance), 3 (probability), 6 (distributions) |
| 6. Capstone: build and evaluate a classifier and a regressor end-to-end, free tools only | 9 (built on the workflow and evaluation skills from 1–8) |

### Deliberately excluded

A fuller classical-ML treatment would also include, none of which fit the 25.5-hour
budget or the stated scope:

- **Unsupervised learning** — clustering (k-means, DBSCAN) and dimensionality
  reduction (PCA), both present in scikit-learn but outside the supervised-learning
  goal the learner stated.
- **Deep learning, neural networks, and non-tabular data** (images, text, audio,
  time series) — explicitly out of scope per `requirements.md`, including as stretch
  content.
- **Ensemble methods beyond a passing mention** — random forests, gradient boosting,
  stacking; each warrants its own module-worth of time this budget doesn't have.
- **Systematic hyperparameter tuning** — `GridSearchCV`/`RandomizedSearchCV` as a
  dedicated topic; Module 7 touches manual mitigation only.
- **Formal statistical inference** — hypothesis testing, p-values, confidence
  intervals; the brief calls for "just-enough" statistics woven in, not inferential
  statistics as a skill.
- **Class-imbalance remediation** (SMOTE, class weighting) — Module 4 names the
  problem via the accuracy-paradox example but does not teach a fix.
- **Model interpretability tooling** (SHAP, LIME, permutation importance).
- **Deployment, APIs, MLOps, model versioning.**
- **Fairness/ethics in ML as a dedicated topic.**

## Sources

- [Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning) — Wikipedia · 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Cross-validation (statistics)](https://en.wikipedia.org/wiki/Cross-validation_(statistics)) — Wikipedia · 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Bias-variance tradeoff](https://en.wikipedia.org/wiki/Bias-variance_tradeoff) — Wikipedia · 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Feature engineering](https://en.wikipedia.org/wiki/Feature_engineering) — Wikipedia · 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Statistical classification](https://en.wikipedia.org/wiki/Statistical_classification) — Wikipedia · 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Regression analysis](https://en.wikipedia.org/wiki/Regression_analysis) — Wikipedia · 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Overfitting](https://en.wikipedia.org/wiki/Overfitting) — Wikipedia · 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Feature scaling](https://en.wikipedia.org/wiki/Feature_scaling) — Wikipedia · 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall) — Wikipedia · 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn) — Wikipedia · 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18

## Open Questions

- **Feature engineering placed late (Module 8), not right after Module 1.** The
  method rule favors rewarding material early, so messy real-world data prep
  (missing values, encoding, scaling, pipelines) was deferred until after the
  learner already has a working classifier, regressor, and a diagnosed
  overfitting problem — at that point the *reason* for preprocessing is visible.
  The tradeoff: Modules 1–7 lean on clean, ready-to-model datasets (e.g.
  scikit-learn's bundled toy datasets), so Module 8 is the first time messiness
  is handled explicitly. If a reviewer would rather build that skill earlier,
  swapping Modules 7 and 8 doesn't break any prerequisite chain.
- **Regression (Module 5) is prerequisite-gated on Module 2, not Module 4.**
  Classification (3–4) and regression (5–6) run as two tracks that both depend
  only on the shared workflow from Module 2, converging at Module 7
  (generalization) rather than one being taught as a special case of the other.
  This keeps regression from silently assuming classification-specific content
  (precision/recall) it doesn't need — but it also means a learner doing the
  modules in numeric order sees classification metrics before regression
  training, which is a sequencing choice rather than a dependency requirement.
- **Cross-validation waits until Module 7**, after both a classifier and a
  regressor have been trained and evaluated with a single split, so the learner
  feels the problem (train/test gap) cross-validation solves before meeting the
  technique. An earlier introduction (right after Module 2) was considered and
  rejected only because the 25.5-hour budget doesn't support revisiting it twice.
- **Capstone sizing (5.0h) assumes reuse, not novelty.** It assumes the learner
  applies patterns already practiced in Modules 1–8 to one or two new tabular
  datasets, rather than a dataset requiring nonstandard cleanup. If the learner
  picks a genuinely messy self-chosen dataset, 5 hours may be tight — this is a
  known risk to flag for `schedule-planner` and `effort-budget-aggregator`, not
  something this budget can absorb given the 15% slack is already fully accounted
  for elsewhere.
