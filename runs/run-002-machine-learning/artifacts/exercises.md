---
artifact: exercises
owner: exercise-designer
run_id: run-002-machine-learning
status: final
attempt: 1
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
generated: 2026-08-18T00:00:00Z
---

# Exercises — Machine Learning (classical, project-based)

## Summary

This is the tightest budget of the three paths: 30 hours total, 25.5 already committed
to content, leaving roughly 4.5 hours for practice across 10 weeks. Every exercise below
is deliberately short (10–20 minutes) and every one either directly builds a piece of the
capstone or produces a fact the learner can check with their own eyes — a number that
should match, a gap that should appear, a score that should move. Two design choices
follow from the brief: first, wherever a module first introduces a statistical idea
(mean/variance in Module 1, probability in Module 3, the normal distribution in Module 6)
the drill is "compute it by hand on ~10 rows, then verify with pandas/scikit-learn" —
retrieval plus a built-in answer key, not an abstract explanation. Second, Module 7
(overfitting) gets the largest allocation of the nine because the brief is explicit that
*seeing* a train/test gap open and close teaches more than reading about bias-variance —
that module's drill deliberately overfits a model on purpose. Total designed practice is
about 4h20m (260 minutes) against the ~4.5h of slack the curriculum left, spread as one
or two short sessions per module rather than bulk weekend work. Because the modality is
project-based, almost every "application" exercise reuses the dataset and model from the
previous module rather than starting fresh, so synthesis is built into the accumulation
rather than bolted on as a separate step — by Module 9 the learner is assembling pieces
they already built, not starting cold.

## Findings

### Module 1: Working with Tabular Data & Descriptive Statistics

**1. Drill — hand vs. pandas**
- **Task:** Take any 10 rows of a numeric column from a dataset you've loaded into a
  DataFrame. On paper (or a text file), compute the mean by hand, then the variance
  (average squared deviation from the mean, dividing by n−1), then the standard
  deviation. Now run `.mean()`, `.var()`, `.std()` on the same 10 rows in pandas.
- **Success criteria:** Your hand-computed mean matches pandas exactly (to rounding).
  Your hand-computed variance matches pandas' `.var()` — if it doesn't, you almost
  certainly divided by n instead of n−1.
- **Time:** 10 minutes.
- **When:** Right after you first load a dataset and look at its columns — before
  moving on to anything else that module.
- **If stuck:** If variance won't match, recompute dividing by (n−1) instead of n —
  pandas uses the "sample" definition by default. If mean doesn't match, check you
  selected the same 10 rows pandas is using (watch for 0-indexing).

**2. Application — profile a whole dataset**
- **Task:** Load a full tabular dataset (not just 10 rows). Produce a one-page summary:
  for every numeric column, mean/std/min/max; for every categorical column, the count
  of unique values and the most common one. Decide, and write one sentence justifying,
  which columns look like they'd be useful for prediction and which look like noise or
  identifiers.
- **Success criteria:** Every column in the dataset appears in your summary exactly
  once, correctly classified as numeric or categorical. Your "useful vs. noise"
  judgment is defensible in one sentence per column you flag (there's no single right
  answer here — the test is whether you can justify it, not whether you match a key).
- **Time:** 15 minutes.
- **When:** Same session as the drill, once you're comfortable with `.mean()`/`.var()`
  — this is the exercise that carries into every later module, since you'll reuse this
  dataset-profiling habit before training any model.
- **If stuck:** If a column's dtype looks wrong (e.g., a numeric-looking column read as
  text), re-read how the module explains dtypes and check for stray characters or
  missing-value markers in that column.

### Module 2: The Supervised Learning Workflow — Your First Model

**1. Drill — split instability**
- **Task:** Take a clean dataset and run `train_test_split` three times with three
  different `random_state` values (keep test size fixed, e.g. 0.2). Fit the same simple
  model each time and record the three test scores.
- **Success criteria:** You can state, in one sentence, how much the score moved across
  the three splits (e.g., "score ranged from 0.81 to 0.89"). If the three scores are
  identical, you forgot to change `random_state`.
- **Time:** 10 minutes.
- **When:** Immediately after your first successful `fit`/`predict`/`score`, same
  session.
- **If stuck:** If `train_test_split` errors, check that features (X) and target (y)
  have the same number of rows — a stale variable from an earlier step is the usual
  cause.

**2. Application — first end-to-end model, honestly reported**
- **Task:** Pick a dataset, split it, fit a default model with no tuning, and report
  the test score alongside: the split proportions used, the random state, and one
  sentence on whether you'd trust this score to generalize to new data and why.
- **Success criteria:** You can reproduce the exact same score by re-running the cell
  with the same `random_state`. Your one-sentence trust judgment mentions the split
  size (a 90/10 split on a small dataset deserves less trust than 70/30 on a large one).
- **Time:** 20 minutes.
- **When:** End of the Module 2 session — this model and split become the baseline you
  compare against in Module 4 and again in Module 7.
- **If stuck:** If `.score()` is unfamiliar, print what it returns and check the
  module's explanation of what metric it defaults to for your model type.

### Module 3: Classification I — Predicting Categories

**1. Drill — probability by hand**
- **Task:** From a small labeled sample (10 rows) of a categorical outcome, hand-count
  the relative frequency of each class (count ÷ 10). Then train a simple classifier on
  a larger version of the same data and call `predict_proba` on those same 10 rows.
  Compare your naive frequency-based guess to the model's actual output per row.
- **Success criteria:** You can explain, for at least 2 of the 10 rows, why the model's
  probability differs from the plain class frequency (it's using the row's features,
  not just the overall base rate).
- **Time:** 10 minutes.
- **When:** Right after the module introduces `predict_proba`, before the application
  exercise.
- **If stuck:** If `predict_proba` errors, confirm your model supports it (k-NN and
  logistic regression both do) and that you're calling it on the same feature columns
  used to fit.

**2. Application — predict vs. predict_proba on a second dataset**
- **Task:** Train a classifier on a different tabular dataset from the one you used in
  Module 2 (a second built-in or public dataset works well). For 5 individual rows,
  print both the hard prediction (`predict`) and the class probabilities
  (`predict_proba`). Find one row where the model is confident and one where it's
  nearly 50/50, and write one sentence on what's different about those two rows.
- **Success criteria:** You've correctly identified one high-confidence and one
  low-confidence row (probability close to the decision boundary) and your explanation
  refers to actual feature values, not just "the model said so."
- **Time:** 20 minutes.
- **When:** Later the same week as the drill, once you're fitting comfortably —
  this classifier is what Module 4 evaluates and what Module 7 will deliberately
  overfit.
- **If stuck:** If every row looks equally confident, try a dataset with more feature
  overlap between classes, or re-check you didn't accidentally scale/filter the data
  to make classes trivially separable.

### Module 4: Evaluating Classifiers

**1. Drill — precision/recall by hand**
- **Task:** Write out a small 2×2 confusion matrix by hand from 10 predictions you
  choose yourself (mix of correct and wrong, both classes represented). Compute
  accuracy, precision, and recall from your matrix by hand. Then verify with
  scikit-learn's `confusion_matrix` and `classification_report` on the same 10 labels.
- **Success criteria:** All three of your hand-computed numbers match scikit-learn's
  output exactly.
- **Time:** 10 minutes.
- **When:** Before touching your Module 2/3 classifier — do this on invented numbers
  first so a mismatch is easy to debug.
- **If stuck:** If precision and recall are swapped, re-check which one divides by
  predicted-positive count (precision) and which divides by actual-positive count
  (recall) — this is the single most common mix-up.

**2. Synthesis — choosing a metric under imbalance**
- **Task:** Take your Module 2 or 3 classifier's dataset and deliberately make it
  imbalanced (e.g., drop most rows of one class so it's ~90/10). Retrain, then compute
  accuracy, precision, and recall. Decide which metric best represents whether the
  model is actually useful, and write two sentences defending your choice.
- **Success criteria:** Your reported accuracy is high (often >85%) while precision or
  recall for the minority class is visibly worse — if both look equally good, your
  imbalance isn't severe enough; drop more rows of the majority class. Your written
  defense correctly identifies accuracy as misleading here.
- **Time:** 20 minutes.
- **When:** Same week, after the drill — this reuses the exact classifier and dataset
  from Module 2/3, so no new setup is needed.
- **If stuck:** If accuracy doesn't stay high after imbalancing, check you didn't
  accidentally balance the test set too — only the training portion needs adjusting
  for this exercise to demonstrate the paradox.

### Module 5: Regression I — Predicting Numbers

**1. Drill — residuals by hand**
- **Task:** Fit a simple linear regression on a small dataset. Pick 10 rows, compute
  the model's predicted value and the residual (prediction − actual) by hand from the
  printed predictions, then verify against `y_pred - y_test` computed in code.
- **Success criteria:** All 10 hand-computed residuals match the code's output exactly,
  including sign (a negative residual means the model overpredicted).
- **Time:** 10 minutes.
- **When:** Right after your first regressor fits successfully.
- **If stuck:** If signs are flipped throughout, check the residual convention you're
  using (prediction − actual vs. actual − prediction) is consistent between your hand
  calculation and the code.

**2. Application — a second regression dataset**
- **Task:** Train a regressor on a different tabular dataset than the one used in the
  drill. Predict on the test set and produce a simple table of actual vs. predicted vs.
  residual for 10 test rows. Identify the single worst prediction and write one
  sentence speculating why the model missed it.
- **Success criteria:** Your table has all three columns correctly computed for 10
  rows, and your "worst prediction" is genuinely the largest absolute residual in your
  table, not just eyeballed.
- **Time:** 20 minutes.
- **When:** Later in the same week — this regressor is what Module 6 evaluates and
  what Module 7 will run cross-validation against.
- **If stuck:** If residuals look enormous across the board, check the target column
  wasn't accidentally left in your feature set (a model that can see the answer
  produces near-zero training error and then fails badly at test time — a preview of
  Module 7).

### Module 6: Evaluating Regressors

**1. Drill — MAE/RMSE by hand**
- **Task:** Using the 10 residuals from Module 5's application exercise, hand-compute
  MAE (mean of absolute residuals) and RMSE (square root of the mean of squared
  residuals). Verify with `mean_absolute_error` and `mean_squared_error`
  (`squared=False`, or take the square root yourself) from scikit-learn.
- **Success criteria:** Both hand-computed values match the library output. You can
  state, in the target's actual units (e.g., "off by $12,000 on average"), what MAE
  means for this dataset.
- **Time:** 10 minutes.
- **When:** Start of the Module 6 session, using last week's saved residuals table.
- **If stuck:** If RMSE is smaller than MAE, you've made an arithmetic error — RMSE is
  mathematically always ≥ MAE because squaring punishes large errors more.

**2. Synthesis — compare two models and eyeball the residual spread**
- **Task:** Train a second regressor (different algorithm or different features) on
  the same dataset from Module 5. Compute MAE and RMSE for both models side by side.
  Then plot (or just sort and skim) the residuals of the better model — check whether
  most residuals cluster near zero with a few larger ones on both sides, which is what
  a roughly normal, "typical" spread of errors looks like.
- **Success criteria:** You can state which model wins on both metrics (or explain why
  they disagree). You can point to whether the residual spread looks roughly
  symmetric around zero or is skewed/has one huge outlier — either answer is fine as
  long as it's backed by looking at the actual numbers, not assumed.
- **Time:** 20 minutes.
- **When:** Same week, after the drill.
- **If stuck:** If the two models score identically, make sure they're actually
  different (different algorithm, or drop/add a feature) — comparing a model to
  itself isn't a comparison.

### Module 7: Overfitting, Underfitting & Generalization

**1. Drill — watch overfitting happen**
- **Task:** Take your Module 3 classifier's dataset. Train two versions: one
  deliberately too flexible (e.g., a decision tree with no depth limit, or k-NN with
  `n_neighbors=1`) and one much simpler (a shallow tree, or k-NN with a larger k).
  Print train accuracy and test accuracy for both, side by side.
- **Success criteria:** The flexible model's train accuracy is much higher than its
  test accuracy (a visible gap — often train near 1.0, test noticeably lower). The
  simple model's train and test accuracy are much closer together. If you don't see a
  gap on the flexible model, make it more flexible still (deeper tree, k=1) until you
  do — the point is to reliably reproduce the gap, not just theorize about it.
- **Time:** 15 minutes.
- **When:** First thing in the Module 7 session, before any explanation of
  bias-variance is re-read — try to produce the gap, then explain what you saw.
- **If stuck:** If the flexible model doesn't overfit, your dataset may be too easy or
  too small to overfit on; add irrelevant/noisy columns or reduce the training set size
  to make overfitting easier to trigger.

**2. Application — cross-validation on your own models**
- **Task:** Run 5-fold cross-validation (`cross_val_score`) on your Module 3
  classifier and separately on your Module 5 regressor. Compare each model's
  cross-validated mean score to the single-split score you recorded back in those
  modules.
- **Success criteria:** You report five fold scores and their mean for each model, and
  state whether the single-split score you got weeks ago was optimistic, pessimistic,
  or about right compared to the more reliable cross-validated estimate.
- **Time:** 15 minutes.
- **When:** Same session as the drill, once the overfitting gap is fresh.
- **If stuck:** If `cross_val_score` errors on the regressor, check you're not passing
  a classification scoring metric (e.g., `accuracy`) to a regression estimator — the
  default scorer differs by estimator type.

**3. Synthesis — fix the overfit model**
- **Task:** Go back to the deliberately overfit model from the drill. Apply exactly one
  mitigation (limit tree depth, increase k, or add `L2` regularization if using a
  linear model), retrain, and recompute train/test accuracy.
- **Success criteria:** The train/test gap from the drill has visibly shrunk after your
  one change. If it hasn't, your change wasn't strong enough — push it further (a
  smaller max depth, a larger k) until the gap closes noticeably, then note how far you
  had to push it.
- **Time:** 15 minutes.
- **When:** End of the Module 7 session — this closes the loop the drill opened.
- **If stuck:** If test accuracy also drops after mitigating, you've likely
  over-corrected into underfitting; back off the change slightly until train and test
  scores converge without both collapsing.

### Module 8: Feature Engineering & Preparing Real Data

**1. Drill — impute by hand**
- **Task:** Build a tiny 10-row table with 2–3 missing numeric values. Fill them in
  by hand two ways: with the column mean, and with the column median. Then verify both
  using scikit-learn's `SimpleImputer` with the matching strategy.
- **Success criteria:** Your hand-filled values match `SimpleImputer`'s output exactly
  for both strategies. You can state one sentence on when median would beat mean (a
  column with outliers or skew).
- **Time:** 10 minutes.
- **When:** Before working with a real messy dataset, same session.
- **If stuck:** If values don't match, check whether your mean/median was computed
  before or after removing the missing rows — it must be computed only from the
  non-missing values, same as `SimpleImputer` does by default.

**2. Application — a full preprocessing Pipeline**
- **Task:** Take a dataset with a genuine mix of missing values and categorical
  columns. Build a single scikit-learn `Pipeline` that imputes, encodes, scales where
  appropriate, and fits a model — all in one `.fit()` call. Confirm it also handles
  the test set correctly with one `.predict()` call, no manual preprocessing steps
  repeated by hand.
- **Success criteria:** The pipeline fits and predicts without a `NotFittedError` or a
  dtype error on the test set, and you did not preprocess the test set separately
  outside the pipeline (which would leak information from train to test).
- **Time:** 20 minutes.
- **When:** Later the same week, once the drill's imputation logic makes sense.
- **If stuck:** If the pipeline errors on categorical columns, check you're routing
  numeric and categorical columns to different preprocessing steps with a
  `ColumnTransformer` rather than applying scaling to text columns.

### Module 9: Capstone — Build and Evaluate a Classifier and a Regressor

**1. Synthesis — capstone self-audit checklist**
- **Task:** Before you start building, write out (or copy and fill in) this checklist
  for each of your two capstone models: dataset chosen · split performed and
  reproducible · model fit · evaluation metrics computed (accuracy/precision/recall for
  the classifier, MAE/RMSE for the regressor) · train/test gap checked · at least one
  mitigation applied if a gap was found · one paragraph written up per model. Use it to
  self-grade your own capstone work as you go rather than only at the end.
- **Success criteria:** Every checklist item is checked for both models, and where an
  item can't be checked honestly (e.g., you found overfitting but haven't mitigated
  it), you can name specifically what's missing rather than skipping the item silently.
- **Time:** 10 minutes to fill in, used continuously across the capstone's own build
  time.
- **When:** Written at the very start of the capstone, then revisited as each capstone
  step is finished — the actual building time is the 5 hours the curriculum already
  allocated to this module; this checklist doesn't add new build time, it directs it.
- **If stuck:** If you can't check the "gap checked" item, reuse the exact train/test
  comparison code you wrote in Module 7 on your capstone's models — it generalizes
  directly.

### Practice load

| Module | Exercises | Practice time |
|---|---|---|
| 1. Tabular Data & Descriptive Statistics | 2 | 25 min |
| 2. The Supervised Learning Workflow | 2 | 30 min |
| 3. Classification I | 2 | 30 min |
| 4. Evaluating Classifiers | 2 | 30 min |
| 5. Regression I | 2 | 30 min |
| 6. Evaluating Regressors | 2 | 30 min |
| 7. Overfitting, Underfitting & Generalization | 3 | 45 min |
| 8. Feature Engineering & Preparing Real Data | 2 | 30 min |
| 9. Capstone | 1 | 10 min (directs, doesn't add to, the module's own 5h) |
| **Total** | **18** | **~260 min (≈4h20m)** |

## Sources

None.

## Open Questions

- **Total practice time (≈4h20m) is close to but under the ≈4.5h of curriculum slack**
  (30h budget − 25.5h content). This leaves almost no additional headroom — if
  `effort-budget-aggregator` finds any module's content estimate needs to grow, the
  first exercises to cut should be the Module 1, 2, 5, and 8 drills (they're the
  lowest-stakes: mechanical verification, not the overfitting or metric-choice
  exercises that carry the module's actual learning-bearing insight).
- **"Explain the bias-variance tradeoff" (Module 7) and "explain when scaling matters"
  (Module 8) are partly conceptual objectives** that a hands-on drill can only
  partially self-check. The Module 7 drill lets the learner *see* the symptom (the
  train/test gap) and the synthesis exercise lets them *fix* it, which is strong
  evidence of understanding — but neither confirms the learner can articulate *why*
  in general terms, independent of the specific dataset used. A tutor or study
  partner would ask the learner to explain the tradeoff cold, in their own words, on a
  dataset they haven't already worked with, and probe whether the explanation still
  holds up. The same gap applies to Module 8's "explain when scaling matters" —
  the pipeline exercise proves the learner can build one, not that they can predict in
  advance which future situations need it.
- **Capstone dataset "messiness" is unpredictable.** If the learner's self-chosen
  capstone dataset is unusually messy, the checklist-based self-audit still applies,
  but the 5 hours the curriculum allocated may run short — this was already flagged in
  `curriculum.md`'s Open Questions and is not something additional exercise time can
  absorb given the budget already used elsewhere.
