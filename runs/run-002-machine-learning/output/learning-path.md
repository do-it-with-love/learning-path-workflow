# Build and Evaluate Your Own Machine Learning Models — Your Learning Path

## Overview

By the end of this path you will be able to take a tabular dataset, split it properly,
train both a classification model and a regression model with scikit-learn, evaluate
each with the right metrics, and diagnose whether a model is overfitting or
underfitting before you trust its results. You'll prove all of this on a capstone
project where you build and evaluate a working classifier and a working regressor,
end to end, on your own.

The scope is deliberately classical and tabular: scikit-learn on rows-and-columns
data. Deep learning, neural networks, and non-tabular data (images, text, audio) are
out of scope — there's no room for them in this budget, and your stated goal doesn't
need them. Statistics is not taught as its own subject; the specific statistical
ideas you need (mean and variance, basic probability, the normal distribution) are
introduced exactly when a module first needs them, not gathered into a separate
chapter up front.

You originally asked to be done in 4 weeks. At 3 hours a week that's 12 hours total,
against a realistic 25–30 hour minimum for this scope done properly — so this plan
runs 10 weeks instead, at the same 3 hours a week, with nothing cut from the original
goal. That trade (more weeks, same weekly effort, full scope) is the decision this
plan is built around.

| | |
|---|---|
| **Starting point** | Comfortable with basic Python; no statistics or machine learning background assumed |
| **End point** | Can build, evaluate, and diagnose a classifier and a regressor on tabular data, independently |
| **Duration** | 10 weeks |
| **Weekly commitment** | 3 hours/week |
| **Total effort** | 26.88 hours (≈ 26h 53m), against 30 hours of available time — about 10% slack |
| **Cost** | $0 — every resource is free |
| **Format** | Project-led: you learn by building and submitting real models, not by watching lectures |
| **Capstone** | A classifier and a regressor, built and evaluated end to end on two real datasets |

If you only read this section: this plan is for a Python-literate beginner who wants
working, evaluated ML models in hand at the end of ten 3-hour weeks, spending nothing,
almost entirely in a web browser.

## Before You Start

**Prerequisites.** You need working Python fundamentals — variables, control flow,
functions, lists and dictionaries. You do **not** need any prior statistics or machine
learning exposure; this plan assumes zero on both and builds them in as you go. You
also don't need prior experience loading or manipulating tabular data (no pandas/numpy
assumed) — that's covered from the first session.

**What to install.** Nothing, in practice. Every resource in this plan runs in a
browser: Kaggle's notebook environment, and scikit-learn's own documentation pages,
which offer zero-install "run this" links (Binder or JupyterLite) for every runnable
example. The one thing to set up is a **free Kaggle account** (email signup, about 6
minutes) — you'll need it starting in Week 1 and will use it throughout. Two modules
(Weeks 3 and 5) also have you join a Kaggle competition to submit predictions; despite
Kaggle's phone-verification requirement for some account features (medals, prizes,
publishing public models), it does **not** apply to submitting predictions on the
"Getting Started" competitions used here, so an email-only account is enough.

**Confirm your starting point.** This placement check exists to confirm — or correct —
the assumption that you're starting from true zero on statistics and ML before the
plan builds on it. It's self-scored and takes under 15 minutes; there's no wrong
outcome, only a more or less accurate starting point.

1. Write a function that takes a list of numbers and returns their average.
2. Given `rows = [{"age": 25, "income": 50000}, {"age": 40, "income": 80000}, {"age":
   31, "income": 62000}]`, write code to compute the average `"age"` across all rows.
3. What is the difference between the *mean* and the *median* of a dataset? Give an
   example of a dataset where they'd differ substantially.
4. If you flip a fair coin 3 times, what is the probability of getting exactly 2 heads?
5. In your own words: what is the difference between *training* a model and *testing*
   it, and why do we split data into two sets instead of using all of it for both?
6. What does it mean for a model to "overfit" its training data?
7. Have you ever used scikit-learn, pandas, or numpy? Describe what you did — or answer
   "never used any of these."
8. A classifier predicts "not spam" for every email in a test set that's 95% not-spam
   and 5% spam. What's its accuracy? Why might accuracy alone be misleading here?

**Answer key** — 1) `sum(nums) / len(nums)`. 2) `sum(r["age"] for r in rows) /
len(rows)` → 32.0. 3) Mean is the arithmetic average; median is the middle sorted
value; they diverge with outliers or skew (e.g., three salaries near $45k and one CEO
at $2M: the mean is pulled far above what's typical). 4) 3/8 = 0.375. 5) Training fits
the model's parameters on known data; testing checks it on data it hasn't seen, to
estimate real-world performance rather than memorization. 6) The model has fit the
training data's noise too closely, so it performs well on training data but poorly on
new data. 7) Any concrete description counts as partial credit; "never used any of
these" is the expected answer. 8) 95% accuracy — misleading because the classifier
catches zero actual spam; precision and recall on the spam class would reveal the true
(poor) performance accuracy alone hides.

**Score yourself:** 0–2 correct confirms the assumed zero baseline — start Week 1
exactly as written. 3–5 correct means some prior exposure has likely happened since you
described your background — start Week 1 anyway, but expect some of it to move faster
than expected. 6–8 correct suggests you're already a level above where this plan
starts (closer to understanding the supervised-learning paradigm conceptually) — the
early weeks' statistics and tooling on-ramp may feel redundant; you can move through
Weeks 1–2 faster than the schedule below assumes.

## Your Path Week by Week

| Week | Focus | Sessions | Hours |
|---|---|---|---|
| 1 | Module 1 — Tabular data & descriptive statistics | Weekend (96 min) + weekday (30 min) | 2.10h |
| 2 | Module 2 — The supervised learning workflow, your first model | Weekend (140 min) + weekday (45 min) | 3.08h |
| 3 | Module 3 — Classification I: predicting categories | Weekend (146 min) + weekday (45 min) | 3.18h (heaviest week) |
| 4 | Cumulative review 1 (Modules 1–3) + Module 4 — Evaluating classifiers | Weekend (70 min) + weekday (55 min) | 2.08h (light recovery week) |
| 5 | Module 5 — Regression I: predicting numbers | Weekend (126 min) + weekday (45 min) | 2.85h |
| 6 | Module 6 — Evaluating regressors + Cumulative review 2 (Modules 4–6) | Weekend (90 min) + weekday (65 min) | 2.58h |
| 7 | Module 7 — Overfitting, underfitting & generalization | Weekend (135 min) + weekday (50 min) | 3.08h |
| 8 | Module 8 — Feature engineering & preparing real data | Weekend (120 min) + weekday (45 min) | 2.75h |
| 9 | Capstone, part 1 — classifier (Adult dataset) | Weekend (130 min) + weekday (50 min) | 3.00h |
| 10 | Capstone, part 2 — regressor (Wine Quality dataset) + write-up | Weekend (90 min) + weekday (40 min) | 2.17h (largest single-week margin) |
| **Total** | | | **26.88h of 30h available (10.4% slack)** |

A few things worth knowing about this shape: Week 3 is the heaviest week in the plan
(3.18h, driven by the Titanic competition submission) but still comes in under the
built-in tolerance for a busy week. Week 4 is deliberately light, giving you a recovery
week right after two weeks that ran close to the ceiling. The capstone spans two full
weeks (9–10) as one uninterrupted block rather than being squeezed alongside anything
else.

## Modules

### Module 1 — Working with Tabular Data & Descriptive Statistics (Week 1, 2.10h)

**What it covers.** This is where you go from "knows Python" to "can work with a real
dataset." You'll load a CSV into a pandas DataFrame, inspect its shape, columns, and
data types, and compute — and actually understand — the mean, variance, and standard
deviation of a numeric column. This is also where the statistics on-ramp begins: mean
and variance land here because you can't describe or summarize any dataset without
them, and nothing later in the plan can wait for a separate statistics unit.

**Objectives.** Load a CSV into a DataFrame and inspect its shape, columns, and
dtypes. Compute and interpret mean, variance, and standard deviation for numeric
columns. Identify categorical vs. numeric columns and produce a simple summary table.

**What to work through.** Three short Kaggle Learn exercise notebooks, each graded as
you go, each building directly on the last: *Creating, Reading and Writing* (build and
load DataFrames by hand and from a CSV, 30 min), *Indexing, Selecting & Assigning*
(select rows and columns with `loc`/`iloc` and boolean masks on a real dataset, 30
min), and *Summary Functions and Maps* (independently compute `.describe()`, `.mean()`,
`.std()`, and related summary functions, 20 min). Each notebook opens with a short
recap and then a series of graded questions checked immediately, with hints and a full
solution if you get stuck — the difficulty ramps across the three notebooks rather than
within any one of them.

**What to practise.** Two short exercises: a 10-minute drill where you hand-compute the
mean, variance, and standard deviation of 10 rows from a numeric column and check your
work against pandas' own `.mean()`/`.var()`/`.std()` (if variance doesn't match, you
likely divided by n instead of n−1 — pandas uses the sample definition by default); and
a 15-minute application where you profile an entire dataset — mean/std/min/max for
every numeric column, unique-value counts for every categorical column — and write one
sentence per column on whether it looks useful for prediction or looks like noise.
This dataset-profiling habit carries forward into every later module.

**How you'll know it landed.** A 15-minute check: load a dataset, compute descriptive
statistics by hand and cross-check them against `.describe()`, and write a genuinely
specific interpretation sentence per numeric column (not "this shows some variation,"
but something anchored to actual units, like "a spread of $12,000 around a mean of
$50,000 is wide"). If your hand-computed numbers don't match `.describe()`, that's a
mechanical error worth fixing before you move on — it will otherwise resurface as
confusing evaluation numbers much later.

### Module 2 — The Supervised Learning Workflow: Your First Model (Week 2, 3.08h)

**What it covers.** Your first fitted model. You'll learn why data gets split into a
training set and a test set, and you'll run the complete `fit`/`predict`/`score`
workflow that every later module builds on.

**Objectives.** Explain the difference between training and testing a model, and why
data is split into two sets. Perform a train/test split with `train_test_split`. Fit a
scikit-learn model end to end and report its score.

**What to work through.** Start with scikit-learn's own *Getting Started* walkthrough
(20 min) — a quick, non-graded read that shows you the shape of the `fit`/`predict`/
`score` API before you touch it yourself. Then two graded Kaggle exercises: *Your First
Machine Learning Model* (select features, fit a decision tree model, generate
predictions, 60 min) and *Model Validation* (perform a `train_test_split` and compute
mean absolute error on data the model never saw, 60 min) — the second of these is where
the module's core lesson actually lands: training performance is not the same as real
performance.

**What to practise.** A 10-minute drill where you run `train_test_split` three times
with three different random seeds on the same data and see how much the score moves
(if all three scores are identical, you forgot to change the seed) — a concrete look at
why a single split is a noisy estimate. Then a 20-minute application: fit a model with
no tuning, report the test score alongside the split proportions and a one-sentence
judgment on whether you'd trust that score to generalize. This exact model and split
becomes what you compare against in Modules 4 and 7.

**How you'll know it landed.** A 15-minute check: split, fit, and report scores on
*both* the train and test sets, then explain in two or three sentences why the model
isn't scored on the data it was trained on. If you also notice how big the train/test
gap is and venture a guess about what a much bigger gap would mean, you're already
planting the seed for Module 7's diagnosis.

### Module 3 — Classification I: Predicting Categories (Week 3, 3.18h)

**What it covers.** Your first real classification model, with the strongest feedback
loop in the whole plan: a live public leaderboard. This is also where basic probability
enters — you need just enough of it to read what `predict_proba` is actually telling
you.

**Objectives.** Train a classification model with scikit-learn. Understand enough basic
probability to read `predict_proba` output. Generate both class predictions and
predicted probabilities and explain how they differ.

**What to work through.** The *Titanic – Machine Learning from Disaster* competition
(120 min plus a 6-minute join step): train a classifier, generate both predictions and
predicted probabilities, and submit for a leaderboard score — real, comparative,
immediate feedback the moment you submit. Pair it with a short, targeted read on
scikit-learn's logistic regression documentation (20 min) on what a predicted
probability actually represents.

**What to practise.** A 10-minute drill: hand-count the relative frequency of each
class in a small 10-row sample, then compare that naive guess to what a trained
model's `predict_proba` actually outputs on those same rows — and explain, for at
least two rows, why the model's answer differs from the plain base rate. Then a
20-minute application on a second dataset: print `predict` and `predict_proba`
side by side for five rows, and find one confident prediction and one near-50/50
prediction.

**How you'll know it landed.** A 15-minute check: confirm that `predict()` and
`predict_proba()` agree on all five rows you inspect (the predicted class must always
be the one with the higher probability — if it isn't, something's broken, not just
imperfect), correctly tell a confident prediction from a coin-flip one, and write a
sentence on what a near-50/50 probability means about the model's confidence.

### Cumulative Review 1 (Week 4, 20 min)

Before diving into evaluation, a short retrieval pass covering Modules 1–3, done from
memory and checked against a worked answer key: recall the four steps of the
supervised workflow in order, hand-compute a mean and variance, and correctly read a
`predict_proba` output. A slip or two that you catch yourself is fine; two or more
misses is worth revisiting Module 1's statistics section and Module 2's workflow
summary before continuing.

### Module 4 — Evaluating Classifiers (Week 4, part of a light 2.08h week)

**What it covers.** Moving beyond "did it work" to "how well, and is that the right
question." This is where accuracy, precision, and recall enter, and where you meet the
accuracy paradox directly.

**Objectives.** Compute accuracy, precision, and recall with scikit-learn's `metrics`
module. Construct and read a confusion matrix. Explain why accuracy alone can mislead
on an imbalanced dataset.

**What to work through.** A targeted read on scikit-learn's classification-metrics
documentation for the definitions (30 min), then the confusion-matrix example notebook
— run **with your own Module 3 model and data swapped in** (30 min) — so the matrix
you read is your own, not a stock example.

**What to practise.** A 10-minute drill: write out a small confusion matrix by hand
from 10 predictions you invent yourself, compute accuracy/precision/recall by hand,
then verify against scikit-learn's own functions (if precision and recall come out
swapped, remember: precision divides by predicted-positive count, recall by
actual-positive count — the single most common mix-up). Then a 20-minute synthesis
exercise: deliberately make your Module 3 dataset imbalanced, retrain, recompute the
same three metrics, and defend in writing which metric actually represents whether the
model is useful.

**How you'll know it landed.** A 15-minute check: compute all four numbers (accuracy,
precision, recall, confusion matrix) on a genuinely imbalanced version of your data,
and state which metric moved the most and why accuracy alone would have misled you.
This module's metrics are load-bearing for Module 7's overfitting diagnosis, so don't
carry an unresolved misunderstanding of the accuracy paradox forward.

### Module 5 — Regression I: Predicting Numbers (Week 5, 2.85h)

**What it covers.** Your first regression model, with the same leaderboard-driven
feedback loop as Module 3, on a numeric target instead of a category.

**Objectives.** Train a regression model with scikit-learn. Distinguish a regression
target from a classification target and pick the matching estimator. Generate
predictions and compute residuals.

**What to work through.** The *House Prices – Advanced Regression Techniques*
competition (120 min plus a 6-minute join step): fit a linear regression model to
predict a house's sale price, generate predictions and residuals, and submit to a
leaderboard that reports RMSE on unseen data immediately.

**What to practise.** A 10-minute drill: hand-compute predicted values and residuals
(prediction minus actual) for 10 rows and verify against code — watch the sign
convention carefully, since a flipped sign here will confuse every later residual
discussion. Then a 20-minute application on a second regression dataset: build a table
of actual vs. predicted vs. residual for 10 rows and identify the single worst
prediction.

**How you'll know it landed.** A 15-minute check: report five residuals with
consistent signing, then correctly classify three short scenarios ("predict a house's
price," "predict whether an email is spam," "predict tomorrow's high temperature") as
regression or classification with the matching estimator type named. A sign error here
will make every MAE/RMSE comparison in Module 6 nonsensical, so it's worth getting
right before moving on.

### Module 6 — Evaluating Regressors (Week 6, 2.58h)

**What it covers.** The regression counterpart to Module 4: turning residuals into
proper error metrics, and the point where the normal distribution enters — just enough
of it to judge whether a set of residuals looks typical or unusual.

**Objectives.** Compute MAE and RMSE and interpret them in the target's own units.
Understand, at an introductory level, what a normal distribution is and use it to judge
residual spread. Compare two regression models with a consistent error metric.

**What to work through.** A targeted read on scikit-learn's regression-metrics
documentation (30 min), then the cross-validated-predictions example notebook — run
**with your own Module 5 regressor and data swapped in** (60 min) — producing an
actual-vs-predicted plot and a residual plot on your own results.

**What to practise.** A 10-minute drill: using the 10 residuals you saved from Module
5, hand-compute MAE and RMSE and verify against scikit-learn's own metric functions
(if RMSE comes out smaller than MAE, that's an arithmetic error — RMSE is always ≥ MAE,
since squaring punishes large errors more). Then a 20-minute synthesis exercise: train
a second, different regressor on the same data, compare MAE/RMSE for both, and check
whether the better model's residuals look roughly symmetric around zero or show a skew
or outlier.

**How you'll know it landed.** A 15-minute check: report MAE and RMSE for two models in
the target's actual units (not bare numbers), identify which model wins, and assess
whether the residual spread looks centered.

### Cumulative Review 2 (Week 6, 20 min)

A second retrieval pass, covering Modules 4–6: compute accuracy/precision/recall from a
given confusion matrix, compute MAE/RMSE from given actual and predicted values, and
state the difference between `predict()` and `predict_proba()` — all from memory,
checked against a worked answer key. A realistic bar at this point in your first
exposure to ML is "one self-corrected slip," not a clean unaided pass — expect and
accept the occasional arithmetic wobble.

### Module 7 — Overfitting, Underfitting & Generalization (Week 7, 3.08h)

**What it covers.** This is the single most valuable experience in the whole plan.
You'll deliberately train a model that's too flexible for its own good and watch its
training and test scores pull apart — and only then read about *why*. Seeing the gap
open, before anyone explains bias-variance to you, is what stops a beginner from
shipping a model that scores 99% on training data and predicts nothing useful in the
real world.

**Objectives.** Explain the bias–variance tradeoff and connect it to overfitting and
underfitting. Diagnose over/underfitting using the train/test gap or cross-validation.
Apply k-fold cross-validation and explain why it's more reliable than a single split.
Apply at least one concrete mitigation to an overfitting model.

**What to work through.** The *Cross-Validation* exercise notebook (90 min, graded):
apply cross-validation to one of your own earlier models and compare the
cross-validated score to the single-split score you already recorded, so the gap is
visible on your own results, not an abstract example. Then a targeted read on
scikit-learn's cross-validation strategy catalogue (30 min) to pick the right strategy
(`StratifiedKFold` for a classifier, plain `KFold` for a regressor).

**What to practise.** First, a 15-minute drill — and do this *before* re-reading any
explanation: train two versions of the same model type, one deliberately too flexible
(an unconstrained decision tree, or k-NN with a single neighbor) and one much simpler.
Print train and test accuracy for both side by side. You should see the flexible
model's train accuracy sit far above its test accuracy — a real, visible gap — while
the simple model's two numbers stay close together. If you don't see a gap, push the
flexible model further (deeper tree, fewer neighbors) until you do; the point is to
reliably produce the symptom, not just read about it. Then a 15-minute application
running cross-validation on your own Module 3 and Module 5 models, and a 15-minute
synthesis exercise where you apply exactly one mitigation (limit depth, increase k, or
add regularization) to the overfit model from the drill and confirm the gap visibly
shrinks.

**How you'll know it landed — and why this one matters more than the others.** A
20-minute check, and the one checkpoint in this plan that's a hard stop rather than a
recommendation: produce a deliberately overfit model and a reasonably fit one, report
train and test scores for both, and — before doing anything else — answer in writing
*which model you'd ship, and why*. If your answer is "the one with the higher training
score," that's the exact failure this checkpoint exists to catch, and the honest
instruction is: don't move on to Module 8 yet. Re-read the bias-variance material,
redo the paired comparison using a worked example until "higher training score plus a
big gap means worse, not better" feels unambiguous, then retry with your own data. Every
other checkpoint in this plan can tolerate a rough pass forward — this one can't.

### Module 8 — Feature Engineering & Preparing Real Data (Week 8, 2.75h)

**What it covers.** Real datasets are messy — missing values, categorical columns,
features on wildly different scales — and this module is where you learn to handle
that properly, chained into a single reusable pipeline, right before you need that
skill for the capstone.

**Objectives.** Handle missing values and encode categorical variables with
scikit-learn's preprocessing tools. Apply feature scaling and know when it matters.
Build a scikit-learn `Pipeline` that chains preprocessing and a model together.

**What to work through.** Two graded exercises, done in this order: *Exercise:
Categorical Variables* (compare drop/ordinal/one-hot encoding and see which produces
the lowest error, 30 min), then *Exercise: Pipelines* (chain imputation, encoding, and
scaling into a single `Pipeline` object on data with real missing values, 90 min).

**What to practise.** A 10-minute drill: fill 2–3 missing values in a tiny table by
hand two ways — column mean and column median — and verify against scikit-learn's
`SimpleImputer`. Then a 20-minute application: build a full `Pipeline` on a genuinely
messy dataset (missing values and categorical columns together) and confirm it handles
new, raw test rows with a single `.predict()` call and no manual preprocessing step
snuck in outside the pipeline — which would otherwise leak information from your test
set into training.

**How you'll know it landed.** A 15-minute check: confirm your `Pipeline` runs
end-to-end on new raw data, correctly identify which model types actually need scaling
(distance-based and regularized models, generally not tree-based ones), and be able to
explain in one sentence why keeping preprocessing inside the pipeline — rather than
doing it once on the whole dataset before splitting — avoids leaking test-set
information into training. A leaking or broken pipeline here would quietly invalidate
the capstone's evaluation, so it's worth getting solid before Week 9.

### Module 9 — Capstone: Build and Evaluate a Classifier and a Regressor (Weeks 9–10, 5.17h)

**What it covers.** Everything from Modules 1–8, recombined without a lesson holding
your hand. You'll run the full workflow twice, unassisted, on two real datasets: split,
train, evaluate, and diagnose over/underfitting for a classifier, then do the same for
a regressor.

**Objectives.** Complete an end-to-end classification workflow — split, train,
evaluate with accuracy/precision/recall, diagnose over/underfitting — on the Adult
dataset. Complete an end-to-end regression workflow — split, train, evaluate with
MAE/RMSE, diagnose over/underfitting — on the Wine Quality dataset. Document the
pipeline, results, and at least one applied mitigation for each.

**What to work through.** Two UCI datasets, both free CSV downloads: **Adult**
(48,842 rows, 14 features, classification target: income above or below $50K) in Week
9, and **Wine Quality** (4,898 rows, 11 features, regression target: a 0–10 quality
score) in Week 10. One thing worth knowing going in: Adult is roughly ten times larger
than Wine Quality. Both train in seconds on any modern machine, so this isn't a
runtime problem — but if you're working in a constrained browser session, Adult will
feel noticeably slower to load, explore, and plot than Wine Quality. That's why Week 9
carries more time than Week 10. If you'd rather have symmetric effort across both
halves, you can subsample Adult down to a few thousand rows without losing anything the
capstone needs.

**What to practise.** A short self-audit checklist, filled in at the start and revisited
as you go rather than only at the end: dataset chosen, split performed and reproducible,
model fit, evaluation metrics computed, train/test gap checked, at least one mitigation
applied if a gap was found, one paragraph written up per model. This doesn't add build
time — it directs the 5-hour build you're already doing.

**How you'll know it landed.** There's no leaderboard here (both datasets are static,
not live competitions), so the check is a checklist you mark against your own capstone
work — see **Checkpoints and Progress** below for the full final check, which is the
actual assessment for this module and ties directly back to your original goal.

## Checkpoints and Progress

Every module above ends with a short, self-scored check, graded against one of three
bands: **not yet** (something's mechanically wrong or a key idea hasn't landed —
revisit the specific material named in that module before continuing), **good enough
to continue** (the realistic bar for most people working through this for the first
time — move on), or **solid** (you've gone a step beyond the minimum). Checkpoints are
short by design — 15 minutes each, with one deliberate exception below — and every one
is checked against something concrete: a library function's own output, a hand
computation, or a fixed worked example with a known answer, not an open-ended
self-assessment.

**One hard gate.** Module 7's checkpoint (20 minutes, not 15) is the one exception to
"move on with a rough pass": if you catch yourself preferring the model with the higher
training score without checking the test score, don't proceed to Module 8. That
specific mistake — mistaking memorization for skill — is the one this whole plan is
built to prevent, so it's worth the extra five minutes and the willingness to redo it.

**Two cumulative reviews.** After Module 3 and after Module 6, a 20-minute retrieval
pass checks whether earlier material is sticking, not just the material you just
finished. A third pass would normally fall after Module 9, but it's folded into the
final check instead, since the capstone already touches every skill from Modules 1–8.

**The final check.** This is where the plan closes the loop with your original goal:
"build and evaluate my own machine learning models." It isn't time-boxed to 15 minutes,
because it's the deliverable the entire plan was built to produce. For each of your two
capstone models, confirm:

1. **Held-out data.** The reported metrics come from a test set that was never touched
   during fitting — not training accuracy, not training error.
2. **The right metric for the task.** Accuracy/precision/recall for the classifier
   (not MAE/RMSE); MAE or RMSE for the regressor (not accuracy). If your classification
   data is imbalanced, precision or recall — not raw accuracy — is the number that
   actually matters.
3. **A stated baseline.** Compute a naive baseline — a majority-class predictor for the
   classifier, a mean-prediction for the regressor — and explicitly compare your
   trained model against it in writing, even if the honest answer is "doesn't beat it,
   because Y."
4. **A checked train/test gap**, with at least one mitigation applied and shown if a
   gap was found.
5. **At least one specific place in your write-up** where mean/variance, basic
   probability, or the idea of a "typical" residual spread was used to interpret your
   data or your model's output — the statistics you picked up along the way, actually
   applied.

For most people finishing this plan for the first time, landing on "good enough to
continue" across the board — both models trained and properly evaluated, a baseline
stated and honestly compared against, the gap checked — is the realistic and expected
outcome, not a shortfall. If any item is missing, the fix points back to the module
that owns it: classifier metrics to Module 4's worked example, regressor metrics to
Module 6's, the overfitting check to Module 7's (non-negotiable, given that module's
hard gate).

**Two honest limits of self-assessment**, worth knowing rather than being surprised by:
judging whether cross-validation is warranted on a genuinely new problem — beyond the
fixed scenarios these checks can pre-answer — is a judgment call self-checking can't
fully validate; and a written explanation (like "explain the bias-variance tradeoff in
your own words") can sound plausible while resting on a subtly wrong mental model, in a
way a self-review won't always catch. If you want a second opinion on either, a study
partner, an ML forum, or anyone with more experience is worth the conversation —
nothing in this plan requires it, but nothing in it replaces it either.

## Resources

Every resource below is free and runs in a browser — no local installation is
required anywhere in this plan.

**Module 1 — Working with Tabular Data & Descriptive Statistics**
- [Exercise: Creating, Reading and Writing](https://www.kaggle.com/code/residentmario/exercise-creating-reading-and-writing) — Kaggle Learn (Pandas course) · 2026 · interactive auto-graded exercise notebook · ~30 min · free · verified: webfetch 2026-08-19
- [Exercise: Indexing, Selecting & Assigning](https://www.kaggle.com/code/residentmario/exercise-indexing-selecting-assigning) — Kaggle Learn (Pandas course) · 2026 · interactive auto-graded exercise notebook · ~30 min · free · verified: webfetch 2026-08-19
- [Exercise: Summary Functions and Maps](https://www.kaggle.com/code/residentmario/exercise-summary-functions-and-maps) — Kaggle Learn (Pandas course) · 2026 · interactive auto-graded exercise notebook · ~20 min · free · verified: webfetch 2026-08-19

**Module 2 — The Supervised Learning Workflow: Your First Model**
- [Getting Started](https://scikit-learn.org/stable/getting_started.html) — scikit-learn · 2026 (v1.9) · documentation walkthrough with runnable code · ~20 min · free · verified: webfetch 2026-08-18
- [Exercise: Your First Machine Learning Model](https://www.kaggle.com/code/dansbecker/exercise-your-first-machine-learning-model) — Kaggle Learn (Intro to Machine Learning) · 2026 · interactive auto-graded exercise notebook · ~60 min · free · verified: webfetch 2026-08-19
- [Exercise: Model Validation](https://www.kaggle.com/code/dansbecker/exercise-model-validation) — Kaggle Learn (Intro to Machine Learning) · 2026 · interactive auto-graded exercise notebook · ~60 min · free · verified: webfetch 2026-08-19

**Module 3 — Classification I: Predicting Categories**
- [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic) — Kaggle Competitions · 2026 (rolling, no end date) · competition with leaderboard · ~120 min for a first working submission · free · verified: websearch 2026-08-18
- [Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression) — scikit-learn · 2026 (v1.9) · user guide · ~20 min · free · verified: webfetch 2026-08-18

**Module 4 — Evaluating Classifiers**
- [Metrics and scoring — classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) — scikit-learn · 2026 (v1.9) · user guide · ~30 min · free · verified: webfetch 2026-08-18
- [Confusion matrix example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html) — scikit-learn · 2026 (v1.9) · runnable example (Binder / JupyterLite), adapted to your own model and data · ~30 min · free · verified: webfetch 2026-08-18

**Module 5 — Regression I: Predicting Numbers**
- [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) — Kaggle Competitions · 2026 (rolling, no end date) · competition with leaderboard, RMSE-scored · ~120 min for a first working submission · free · verified: websearch 2026-08-18

**Module 6 — Evaluating Regressors**
- [Metrics and scoring — regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics) — scikit-learn · 2026 (v1.9) · user guide · ~30 min · free · verified: webfetch 2026-08-18
- [Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html) — scikit-learn · 2026 (v1.9) · runnable example (Binder / JupyterLite), adapted to your own regressor · ~60 min · free · verified: webfetch 2026-08-18

**Module 7 — Overfitting, Underfitting & Generalization**
- [Exercise: Cross-Validation](https://www.kaggle.com/code/alexisbcook/exercise-cross-validation) — Kaggle Learn (Intermediate Machine Learning) · 2026 · interactive auto-graded exercise notebook · ~90 min · free · verified: webfetch 2026-08-19
- [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html) — scikit-learn · 2026 (v1.9) · user guide, cross-validation strategy catalogue · ~30 min · free · verified: webfetch 2026-08-18

**Module 8 — Feature Engineering & Preparing Real Data**
- [Exercise: Categorical Variables](https://www.kaggle.com/code/alexisbcook/exercise-categorical-variables) — Kaggle Learn (Intermediate Machine Learning) · 2026 · interactive auto-graded exercise notebook · ~30 min · free · verified: webfetch 2026-08-19
- [Exercise: Pipelines](https://www.kaggle.com/code/alexisbcook/exercise-pipelines) — Kaggle Learn (Intermediate Machine Learning) · 2026 · interactive auto-graded exercise notebook · ~90 min · free · verified: webfetch 2026-08-19

**Module 9 — Capstone: Build and Evaluate a Classifier and a Regressor**
- [Adult](https://archive.ics.uci.edu/dataset/2/adult) — UCI Machine Learning Repository · 1996 data, page current 2026 · dataset (CSV, CC BY 4.0) · 48,842 instances / 14 features, classification target (income above/below $50K) · free · verified: webfetch 2026-08-18
- [Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality) — UCI Machine Learning Repository · 2009 data, page current 2026 · dataset (CSV, CC BY 4.0) · 4,898 instances / 11 features, regression target (quality score 0–10) · free · verified: webfetch 2026-08-18

## Time and Cost

**Totals.** 26.88 hours of real work (19.97h of resources, 4.17h of hands-on practice,
2.75h of checkpoints) against 30 hours of available time over 10 weeks at 3 hours/week
— **187 minutes (3.12 hours, about 10.4%) of slack**. That's comfortable, not
generous: closer to a 10% cushion than the roughly 15% you'd want for real breathing
room. If a week runs long, the built-in cushion is thin, so treat the schedule above as
close to the real ceiling rather than as padded.

**Cost: $0, entirely.** Every single resource in this plan is free — no paid courses,
no paywalled books, no trial-only platforms. This plan *is* the free-only version;
there's no paid tier to strip out and nothing you'd be missing by not paying. What a
paid alternative would typically add — smoother pacing, human feedback on judgment
calls, a certificate — isn't required by any of your original goals, all of which are
met here through Kaggle's auto-graded exercises and leaderboards, scikit-learn's own
documentation and runnable examples, and two free public datasets.

**Setup cost, in total: about 28 minutes.** One free Kaggle account (6 minutes, first
needed in Week 1), two competition-join steps (6 minutes each, Weeks 3 and 5), and two
plain CSV downloads (10 minutes total, Weeks 9–10). Nothing requires a local Python
install.

**Worth knowing about, honestly:**

- **Kaggle needs an account, but not a phone number for this plan.** Phone
  verification is a real Kaggle requirement, but only for earning progression points,
  medals, or prizes, or for publishing public models — none of which this plan asks you
  to do. Joining and submitting to the "Getting Started" competitions in Weeks 3 and 5
  needs only an email-based account.
- **Kaggle notebooks have session limits.** The capstone's 5-hour build is very likely
  to span more than one sitting. Save or commit your notebook regularly — losing
  unsaved capstone work is the one real risk in an otherwise low-friction setup.
- **The two capstone datasets differ a lot in size** — Adult (48,842 rows) is roughly
  ten times larger than Wine Quality (4,898 rows). Both train in seconds on any modern
  machine, so this isn't a speed problem in absolute terms, but in a constrained
  browser session Adult will feel noticeably slower to load and explore than Wine
  Quality, which is why Week 9 carries more time than Week 10.
- **Two runnable examples (Modules 4 and 6) launch via Binder or JupyterLite**, which
  are known for occasional multi-minute cold starts. The time estimates for those two
  resources don't include that startup wait, so budget a few extra minutes around them
  if it happens.
- **A few Kaggle exercises overlap in skill with the bespoke practice in Modules 1 and
  2** — both ask you to compute summary statistics or run a train/test split, once
  inside a graded Kaggle notebook and once in the practice exercises above. This is
  intentional reinforcement of a first-exposure skill, not a mistake or wasted time; if
  it starts to feel repetitive once you're comfortable, it's safe to move through the
  bespoke practice for those two modules a little faster.

## What Comes Next

This plan deliberately stops at a specific, real boundary: classical, tabular machine
learning with scikit-learn, evaluated properly, with one worked capstone. A few things
were left out on purpose, not by oversight, because none of them fit a 30-hour budget
and none of them were part of your original goal:

- **Unsupervised learning** — clustering and dimensionality reduction (both present in
  scikit-learn) are a natural next step once you're comfortable with the supervised
  workflow this plan builds.
- **Deep learning, neural networks, and non-tabular data** — images, text, audio, and
  time series are a substantial separate path, not an extension of this one.
- **Ensemble methods beyond a passing mention** — random forests, gradient boosting,
  and stacking each deserve their own dedicated study once the fundamentals here are
  solid.
- **Systematic hyperparameter tuning** — `GridSearchCV`/`RandomizedSearchCV` as a
  dedicated skill; Module 7 only covers manual mitigation.
- **Formal statistical inference** — hypothesis testing, p-values, confidence
  intervals. This plan teaches "just enough" statistics to use in context, not
  statistics as its own subject.
- **Class-imbalance remediation** (SMOTE, class weighting) — Module 4 names the problem
  through the accuracy paradox but doesn't teach a fix.
- **Model interpretability tooling** (SHAP, LIME, permutation importance), deployment
  and MLOps, and fairness/ethics in ML as dedicated topics.

If any of these become the next thing you want, the workflow you'll have practiced by
the end of this plan — split, fit, evaluate honestly, check for overfitting — is the
same one you'll reuse to explore them; you won't be starting over.

One more thing worth carrying forward: your goal now includes a working, evaluated
classifier and regressor built end to end. If you revisit them later with a genuinely
messier, self-chosen dataset, expect the cleanup work to take longer than either
capstone half did here — both capstone datasets are well-behaved by design, and a real
messy dataset is where feature engineering (Module 8's skill) gets used the hardest.
