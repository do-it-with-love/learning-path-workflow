---
artifact: assessments
owner: assessment-designer
run_id: run-002-machine-learning
status: final
attempt: 1
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
generated: 2026-08-18T00:00:00Z
---

# Assessments — Machine Learning (classical, project-based)

## Summary

Nine module checkpoints, each a production task graded against a concrete self-check
(compare against a library function, hand-computed arithmetic, or a fixed worked
example with a known answer) rather than a conceptual quiz — the domain allows this
almost everywhere. All checkpoints hold to 15 minutes except Module 7, held at 20
minutes as a deliberate, small exception: that module's checkpoint is the one
purpose-built to catch a learner who reads a high training score as "the model is
good," which is named in the brief as the failure this curriculum exists to prevent,
and it is the one checkpoint whose go/no-go rule is a hard block rather than a
recommendation. Two cumulative reviews (20 minutes each) fall after Module 3 and
Module 6, retrieving arithmetic and workflow steps from memory against fixed worked
examples with known answers. The third cumulative pass, due after Module 9, is
absorbed into the Final check below rather than run separately, since Module 9 *is*
the capstone and re-testing everything a second time on top of building it would
break the 15-minute-per-checkpoint budget for no benefit. Total dedicated checkpoint
time across the run is roughly 2 hours 45 minutes (checkpoints 1–6 and 8 at 15 min,
checkpoint 7 at 20 min, two cumulative reviews at 20 min each); the capstone's own
assessment activity is costed inside its existing 5-hour budget, not added on top.
All checks assume only free, browser-based or locally-installed tooling (a notebook
environment and scikit-learn) — no specific platform is named, since resource
selection is out of scope for this artifact.

## Findings

### Module 1: Working with Tabular Data & Descriptive Statistics

**Check (15 min).** Load any small CSV dataset into a DataFrame. Print its shape,
column names, and dtypes. For every numeric column, compute mean, variance, and
standard deviation by hand (with `.mean()`, `.var()`, `.std()`, not `.describe()`).
For every categorical column, produce a one-line summary (unique values and counts).
Then run `.describe()` and confirm your numbers match. Write one sentence per
numeric column interpreting its spread in its own units (e.g. "a std of 12,000 on a
mean of 50,000 is a wide spread," not "this shows variation").

**Rubric.**
- *Not yet* — shape/dtype commands error, or a categorical column is treated as
  numeric (or vice versa), or the hand-computed mean/variance/std don't match
  `.describe()` once rounding is accounted for.
- *Good enough to continue* — data loads cleanly, categorical vs. numeric columns
  are correctly identified, hand-computed statistics match `.describe()`, but the
  interpretation sentences are generic ("this shows some variation") rather than
  anchored to the column's actual units and scale.
- *Solid* — all of the above, plus each interpretation names the actual units and
  compares std to mean to judge relative spread, and at least one column is
  correctly flagged as numeric-looking-but-actually-categorical (e.g. an ID or
  code column) if the dataset has one.

**Go/no-go.** *Not yet* → re-read the descriptive-statistics section, redo the
exercise on a second small dataset, and don't proceed to Module 2 until hand-computed
values match `.describe()` — a mismatch here means a mechanical error, not a
judgment call, and it will resurface as confusing evaluation numbers later.

**Time:** 15 minutes.

### Module 2: The Supervised Learning Workflow — Your First Model

**Check (15 min).** On a clean dataset, perform `train_test_split`, fit a model
end-to-end (`fit`/`predict`/`score`), and report the score on *both* the train set
and the test set. Then, without looking at notes, say or write two to three
sentences explaining why the model isn't scored on the data it was trained on.

**Rubric.**
- *Not yet* — the split/fit/predict/score pipeline errors out, or the explanation
  amounts to "because you're supposed to" with no mention of measuring performance
  on unseen data.
- *Good enough to continue* — the pipeline runs cleanly and produces a plausible
  score; the explanation correctly identifies that testing on training data would
  overstate performance, even if the phrasing is rough.
- *Solid* — all of the above, plus the learner notices the size of the train-vs-test
  score gap and states, tentatively, what a much bigger gap would suggest (this is
  the seed of the Module 7 diagnosis, not a full explanation yet).

**Go/no-go.** *Not yet* → redo the workflow using the module's own worked example
line by line, then repeat on a fresh dataset. This is foundational plumbing every
later module depends on — don't carry forward a pipeline that still errors.

**Time:** 15 minutes.

### Module 3: Classification I — Predicting Categories

**Check (15 min).** Train a classifier on a tabular dataset. For five test-set rows,
print `predict()` and `predict_proba()` side by side. For each row, confirm the
predicted class is the one with the higher probability (this must always be true —
if it isn't, something is broken, not just imperfect). Pick one row where the
probabilities are close to 50/50 and write a sentence on what that means about the
model's confidence there.

**Rubric.**
- *Not yet* — `predict()` and `predict_proba()` disagree on any row and the
  discrepancy is unresolved, or the learner cannot distinguish a confident
  prediction (e.g. 0.95/0.05) from a coin-flip one (e.g. 0.52/0.48).
- *Good enough to continue* — predict/predict_proba are cross-checked and
  consistent across all five rows; confident vs. borderline predictions are
  correctly told apart.
- *Solid* — all of the above, plus for a row where the prediction turned out wrong,
  the learner explains why the probability value was still informative (e.g. "it
  called it right at 51% — barely better than a guess").

**Go/no-go.** *Not yet* → reread the predict-vs-predict_proba section, rerun the
module's worked example verbatim, then retry on your own data. Don't move to
Module 4's metrics work with an unresolved predict/predict_proba mismatch — that
almost always signals a code error that will silently corrupt the metrics next.

**Time:** 15 minutes.

### Cumulative review 1 (after Module 3)

See **Cumulative reviews** below.

### Module 4: Evaluating Classifiers

**Check (15 min).** Compute accuracy, precision, recall, and a confusion matrix for
the Module 3 classifier on the test set; verify the confusion matrix entries sum to
the test-set size. Then create an imbalanced version of the same problem (e.g.
subsample one class down to ~10%), retrain, and recompute the same metrics. Write
two to three sentences on which metric moved the most and why accuracy alone would
have been misleading on the imbalanced version.

**Rubric.**
- *Not yet* — confusion matrix entries don't sum correctly (arithmetic never
  checked), or the learner defaults to "accuracy is the best metric" without
  qualification, or cannot say which metric would have been misleading on the
  imbalanced data.
- *Good enough to continue* — all four metrics and the confusion matrix are
  computed correctly and self-verified; the learner correctly identifies that
  accuracy overstated performance on the imbalanced version and names precision or
  recall as more informative there.
- *Solid* — all of the above, plus the learner connects the metric choice to the
  real-world cost of false positives vs. false negatives for a stated scenario
  (e.g. "missing a positive case here is worse than a false alarm, so recall
  matters more").

**Go/no-go.** *Not yet* → redo the confusion-matrix-by-hand exercise from the
module, recheck the arithmetic, and repeat the imbalance comparison using the
module's worked dataset before trying your own. This module's metrics are load-
bearing for Module 7's overfitting diagnosis — don't carry an unresolved
accuracy-paradox misunderstanding forward.

**Time:** 15 minutes.

### Module 5: Regression I — Predicting Numbers

**Check (15 min).** Train a regression model on a tabular dataset. For five test-set
rows, print actual value, predicted value, and residual (actual − predicted),
consistently signed. Then, given three short scenarios (e.g. "predict a house's
sale price," "predict whether an email is spam," "predict tomorrow's high
temperature"), label each as regression or classification and name the matching
type of scikit-learn estimator.

**Rubric.**
- *Not yet* — the residual sign is inconsistent across rows (mixing
  actual−predicted and predicted−actual), or more than one of the three scenarios
  is mislabeled.
- *Good enough to continue* — residuals are computed correctly and consistently
  signed; all three scenarios are correctly classified with a matching estimator
  type named.
- *Solid* — all of the above, plus the learner spots a pattern across the five
  residuals (e.g. "the model consistently under-predicts the higher values") and
  says why that's worth flagging rather than dismissing as noise.

**Go/no-go.** *Not yet* → re-derive the residual formula from the module text,
redo the worked example, then retry on your own dataset before Module 6 — a sign
error here will make every MAE/RMSE comparison in Module 6 nonsensical.

**Time:** 15 minutes.

### Module 6: Evaluating Regressors

**Check (15 min).** Compute MAE and RMSE for the Module 5 regressor on the test
set, cross-checked against scikit-learn's own metric functions, and state both in
the target's actual units (e.g. "$3,200," not "3200"). Train a second, different
regression model on the same split and compare MAE between the two. Finally, look
at the five-plus residuals: do they cluster roughly symmetrically around zero, or
is there an obvious skew or one large outlier?

**Rubric.**
- *Not yet* — MAE/RMSE are reported as bare numbers with no units, or the
  hand/manual computation doesn't match scikit-learn's own metric function when
  checked, or the learner can't say which of the two models has lower error.
- *Good enough to continue* — MAE/RMSE are correctly computed, cross-checked, and
  stated in units; the better of the two models is correctly identified; the
  residual symmetry check is attempted even if the description is rough ("looks
  pretty centered").
- *Solid* — all of the above, plus an unusual residual pattern (skew, one big
  outlier) is connected to something specific in the data itself, not just written
  off as "the model got it wrong."

**Go/no-go.** *Not yet* → redo the MAE/RMSE worked example from the module,
verifying against scikit-learn's metric functions line by line, before retrying on
your own data.

**Time:** 15 minutes.

### Cumulative review 2 (after Module 6)

See **Cumulative reviews** below.

### Module 7: Overfitting, Underfitting & Generalization

**Check (20 minutes — the one checkpoint held slightly over budget; see Summary).**
Take a model type from Module 3 or 5. Deliberately produce two versions on the same
train/test split: one tuned to overfit (e.g. an unconstrained decision tree, or
k-NN with k=1, or a high-degree polynomial regression) and one reasonably fit.
Report **train score and test score side by side for both**. Before doing anything
else, answer in writing: *which model would you ship, and why?* Then run k-fold
cross-validation on both and compare how much the scores vary across folds. Finally,
apply one mitigation to the overfit model (simplify it, regularize it, or add more
training data) and show whether the train/test gap shrinks.

This check exists specifically to catch a learner who looks at a higher training
score and calls the model "better." The rubric below fails that answer outright,
regardless of how well the rest of the module was executed.

**Rubric.**
- *Not yet* — the learner picks the overfit model as "better" because of its
  higher (or perfect) training score without checking the test score, or checks
  the test score but still prefers the overfit model, or cannot say why a large
  train/test gap is a problem beyond "it seems off." This is the exact failure
  mode the checkpoint is built to catch.
- *Good enough to continue* — the overfit model is correctly identified by its
  large train/test gap (or by a wide spread across cross-validation folds) and
  explicitly rejected despite its higher training score, with a one-sentence
  reason such as "it memorized noise in the training set and won't generalize."
  A mitigation is applied and the gap is observed to shrink, even if not
  optimally tuned.
- *Solid* — all of the above, plus the specific choice driving overfitting (e.g.
  k=1 vs. a larger k, unregularized vs. regularized) is named using bias-variance
  language, and the learner correctly predicts — before running it — which
  direction a proposed change will move the train/test gap.

**Go/no-go.** This is a hard gate, not a recommendation: *not yet* means **do not
proceed to Module 8.** Re-read the bias-variance section, redo the paired
train/test comparison using the module's own worked example (not your own dataset)
until "higher training score plus a big gap = worse model, not better" is
unambiguous, then retry with a fresh dataset before moving on. Every other
checkpoint in this run can tolerate a rough pass forward; this one cannot, because
it is the specific misunderstanding the whole curriculum was built to prevent.

**Time:** 20 minutes.

### Module 8: Feature Engineering & Preparing Real Data

**Check (15 min).** Take a messier dataset (missing values, at least one
categorical column). Build a single scikit-learn `Pipeline` that imputes missing
values, encodes categoricals, scales numeric features, and fits a model, then call
`.fit()` once. Confirm `.predict()` runs directly on new, raw, unprocessed rows —
if you find yourself manually preprocessing before calling `.predict()`, the
pipeline isn't actually doing its job. Then answer: for which model types used so
far does scaling matter, and why?

**Rubric.**
- *Not yet* — `.predict()` on new raw data throws an error or requires manual
  preprocessing outside the pipeline, or the learner can't say which model types
  need scaling and which don't.
- *Good enough to continue* — the pipeline runs end-to-end on new raw data with no
  manual preprocessing step outside it; distance-based and regularized models are
  correctly identified as needing scaling, tree-based models as generally not.
- *Solid* — all of the above, plus the learner can explain in one sentence why
  chaining preprocessing inside the pipeline (rather than doing it once on the
  whole dataset before splitting) avoids leaking test-set information into
  training.

**Go/no-go.** *Not yet* → redo the module's worked Pipeline example step by step,
verify each preprocessing stage in isolation, then reassemble and retry before
starting the capstone — a leaking or broken pipeline will quietly invalidate the
capstone's evaluation.

**Time:** 15 minutes.

### Module 9: Capstone — Build and Evaluate a Classifier and a Regressor

This module's assessment **is** the Final check below — building the two
deliverables and assessing them are the same activity, so there is no separate
15-minute add-on. Budget the checklist-and-comparison work in **Final check** as
part of the module's existing 5-hour estimate, concentrated in its last 30–45
minutes once both models are trained.

### Cumulative reviews

Two reviews, each a short retrieval pass done from memory before checking a
supplied worked answer — this is where forgetting from earlier modules gets caught
before it compounds.

**Cumulative review 1 — after Module 3 (20 min).** Covers Modules 1–3.
1. From memory, list the four steps of the supervised workflow in order (load and
   inspect → split into train/test → fit → predict/score). Self-check: compare
   against the Module 2 summary — if "split before fit" is missing or out of order,
   that's the gap to revisit.
2. By hand, compute the mean and variance of `[2, 4, 4, 4, 5, 5, 7, 9]`.
   Answer key: mean = 5, population variance = 4, std = 2.
3. Given a `predict_proba` output of `[0.12, 0.88]` for classes `[0, 1]`, state the
   predicted class and whether it's confident or borderline. Answer: class 1,
   confident (far from 0.5).

*Rubric:* **not yet** if two or more of the three are wrong or the workflow order
is scrambled → revisit Module 2's summary and Module 1's statistics section before
continuing to Module 4. **Good enough to continue** if one slip occurs and is
self-corrected on sight of the answer key. **Solid** if all three are right
unaided.

**Cumulative review 2 — after Module 6 (20 min).** Covers Modules 4–6, retrieves 1–3.
1. Given a confusion matrix TP=40, FP=10, FN=5, TN=45, compute accuracy, precision,
   and recall by hand. Answer key: accuracy = 85/100 = 0.85, precision = 40/50 =
   0.80, recall = 40/45 ≈ 0.89.
2. Given actual = `[3, 5, 2, 8]` and predicted = `[2, 5, 4, 7]`, compute MAE and
   RMSE by hand. Answer key: errors = −1, 0, 2, −1; MAE = 1.0; squared errors =
   1, 0, 4, 1; RMSE = √1.5 ≈ 1.22.
3. From memory, state the difference between `predict()` and `predict_proba()` in
   one sentence.

*Rubric:* same three-band structure as review 1, scaled to five items — **not
yet** on two or more misses (revisit Module 4's confusion-matrix section and
Module 6's MAE/RMSE worked example), **good enough to continue** on one
self-corrected slip, **solid** on a clean unaided pass. A realistic bar at this
point in a first ML exposure is *good enough to continue*, not *solid* — expect
and accept the occasional slip on hand arithmetic.

A third cumulative pass would normally fall after Module 9; it is folded into the
**Final check** instead, since Module 9 already requires touching every skill from
Modules 1–8 to complete the capstone.

### Final check

Ties directly to the six target outcomes in `requirements.md`. Assesses the two
capstone deliverables — a working classifier and a working regressor — using a
checklist the learner marks against their own capstone notebook/write-up. No item
requires anyone but the learner to judge it.

**"Properly evaluated" — what that means observably, for both deliverables:**
1. **Held-out data.** The reported metrics come from a test set that was never
   touched by `.fit()` — not training accuracy, not training error.
2. **Appropriate metric for the task.** The classifier's headline metrics are
   accuracy, precision, and recall (not MAE/RMSE); the regressor's are MAE or RMSE
   (not accuracy). If the classification data is imbalanced, precision or recall —
   not raw accuracy — is the number treated as most informative.
3. **A stated baseline to beat.** A naive baseline is explicitly computed — a
   majority-class predictor for the classifier, a mean-prediction for the
   regressor — and the trained model's metric is compared against it in writing,
   with an explicit conclusion ("beats baseline by X" or "doesn't beat it, because
   Y").

**Checklist — classifier (outcomes 1, 2, 4):**
- [ ] Train/test split performed before any fitting.
- [ ] Classifier trained with scikit-learn.
- [ ] Accuracy, precision, and recall reported on the held-out test set.
- [ ] A baseline (e.g. majority-class predictor) is computed and the model is
      explicitly compared against it.
- [ ] Train-vs-test gap checked; if it indicates overfitting or underfitting, at
      least one mitigation is applied and its effect shown.

**Checklist — regressor (outcomes 1, 3, 4):**
- [ ] Train/test split performed before any fitting.
- [ ] Regressor trained with scikit-learn.
- [ ] MAE or RMSE reported on the held-out test set, in the target's units.
- [ ] A baseline (e.g. predicting the mean) is computed and the model is explicitly
      compared against it.
- [ ] Train-vs-test gap checked; if it indicates overfitting or underfitting, at
      least one mitigation is applied and its effect shown.

**Statistics-in-context check (outcome 5):** point to at least one specific place
in the capstone write-up where mean/variance, basic probability, or the idea of a
normal-ish spread was used to interpret data or a model's output — e.g. describing
class balance in probability terms, describing residual spread using variance/std,
or judging a residual as typical vs. unusual.

**Rubric.**
- *Not yet* — either deliverable is missing, or its headline metric was computed on
  training data, or the metric doesn't match the task (e.g. only accuracy reported
  on an imbalanced classifier, or no MAE/RMSE for the regressor), or no baseline
  was stated, or the train/test gap was never checked.
- *Good enough to continue* — both classifier and regressor are trained and
  evaluated on a genuine held-out test set with the correct metrics; a baseline is
  stated and explicitly compared against, even if the model only just beats it (or
  doesn't, and that's said honestly); the train/test gap was checked for both. This
  is the realistic bar for someone ten weeks into their first exposure to ML — most
  learners finishing this run should land here, not below.
- *Solid* — all of the above, plus the model meaningfully beats its baseline on
  both tasks, at least one mitigation was applied with its before/after effect on
  the train/test gap shown quantitatively, and the statistics-in-context item is
  specific and correctly reasoned rather than a passing mention.

**Go/no-go.** There is no next module to gate, so *not yet* means: identify which
specific checklist item is unmet and redo only that piece, pointing back to its
owning module — classifier metrics → Module 4's worked example; regressor metrics →
Module 6's; the baseline concept → this checklist's own definition above; the
overfitting check → Module 7's worked comparison (non-negotiable given that
module's go/no-go rule). The capstone is complete when every checklist box is
checked, not on a calendar date — this is the one checkpoint in the run explicitly
not time-boxed to 15 minutes, because it is the deliverable the entire 10-week plan
was built to produce.

## Sources

None.

## Open Questions

- **"Recognize when cross-validation is warranted" (target outcome 1) is only
  partly self-assessable.** The checkpoints verify that the learner can *run*
  cross-validation and interpret its output (Module 7), but judging whether CV is
  warranted on a genuinely novel problem, outside the fixed scenarios this artifact
  can pre-answer, is a judgment call a self-check can't fully validate. A second
  opinion — a study partner, an online ML forum, or an instructor — would be needed
  to pressure-test that judgment on cases with no supplied answer key.
- **Verbal/written conceptual explanations (e.g. "explain why data is split,"
  "explain the bias-variance tradeoff") are graded by the learner against their own
  rubric description, which is weaker than an external check.** A learner with a
  subtly wrong mental model can produce a plausible-sounding sentence that passes
  their own self-review. Periodic spot-checks against a knowledgeable third party
  (a forum post, a study partner, a teacher) would catch what self-assessment
  structurally cannot.
- **The capstone's "baseline to beat" is only as good as the baseline the learner
  chooses**, and for a genuinely novel self-chosen dataset there's no answer key to
  confirm the chosen baseline is reasonable (as opposed to trivially easy to beat).
  A brief sanity check from someone else familiar with the dataset's domain would
  close this gap; absent that, the checklist item ("baseline is computed and
  compared against") is the most this artifact can verify unaided.
