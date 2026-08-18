---
artifact: baseline-assessment
owner: knowledge-assessor
run_id: run-002-machine-learning
status: final
attempt: 1
inputs:
  - artifacts/requirements.md
generated: 2026-08-18T00:00:00Z
---

# Baseline Assessment — Machine Learning (classical, project-based)

## Summary

The learner places at **L0 (Pre-ML) on the Classical ML Practitioner Progression**, a
custom four-level scale defined below since no CEFR-equivalent standard exists for this
subject: solid general Python fundamentals but a true zero baseline in statistics, ML
concepts, and scikit-learn tooling. Mode is **full**, so a short self-administered
placement check is included to confirm this before module 1 is built. Nothing here is
assessed above what the learner stated — "Python basics" is scored as programming
fundamentals only, not as data-handling (pandas/numpy) or ML competence, since neither
was claimed.

## Findings

### Level scale

**Classical ML Practitioner Progression** (custom scale — see Open Questions for why no
named external standard was used). Grounded in how Wikipedia's "Machine learning" and
"Supervised learning" articles decompose the field: a statistical-algorithm foundation,
a train/fit-and-evaluate workflow, and generalization to unseen data as the central
concern (bias–variance tradeoff, cross-validation).

| Level | Description |
|---|---|
| **L0 — Pre-ML** | Can program (variables, control flow, functions, data structures) but has no statistics, no ML concepts, and no exposure to an ML library. |
| **L1 — ML-aware** | Understands the supervised-learning paradigm (train/test split, fitting vs. predicting) and basic statistics (mean, variance, probability) conceptually, but has not implemented a model. |
| **L2 — Guided practitioner** | Can run a classification or regression workflow in scikit-learn (load data, fit, predict, score) with reference material at hand, and can name evaluation metrics, but cannot yet diagnose model behavior independently. |
| **L3 — Independent practitioner** | Can build, evaluate, and diagnose (overfitting/underfitting) a classifier and a regressor on tabular data end-to-end without guidance. This is the target end-state of the 10-week plan (target outcomes 1–6 in `requirements.md`). |

### Assessed baseline

Scope is bounded to classical/tabular ML in the scikit-learn ecosystem per
`requirements.md`; deep learning, neural networks, and non-tabular data are out of
scope and not assessed against.

| Core area | Status | Basis |
|---|---|---|
| Programming fundamentals (loops, functions, lists/dicts) | **Known** | Stated directly in requirements |
| Tabular data handling (loading/manipulating data, e.g. pandas/numpy) | **Absent** | Not claimed; "Python basics" does not imply a data library |
| Statistical foundations (mean/variance, basic probability, distributions) | **Absent** | Stated directly: "no statistics background" |
| Core ML concepts (supervised learning, train/test split, generalization) | **Absent** | Stated directly: "no prior ML exposure" |
| Classification workflow & evaluation (accuracy, precision, recall) | **Absent** | Follows from no prior ML exposure |
| Regression workflow & evaluation (MAE, RMSE) | **Absent** | Follows from no prior ML exposure |
| Model diagnosis (overfitting/underfitting, bias–variance) | **Absent** | Follows from no prior ML exposure |
| scikit-learn tooling (fit/predict/score API conventions) | **Absent** | Follows from no prior ML exposure |

### Prerequisite gaps

Statistics is woven into the modeling modules rather than taught as a standalone
module, so module 1 will assume some of it is already in place. These are the specific
absences gate G4 must check module 1 against:

- **No familiarity with mean and variance/standard deviation** — needed the moment any
  dataset is described or summarized, which will happen before the first model is
  trained.
- **No familiarity with basic probability** — needed to interpret classifier outputs
  (e.g., predicted class probabilities) once classification is introduced.
- **No familiarity with distributions (e.g., the normal distribution)** — needed for
  later interpretation of errors/residuals in the regression module.
- **No experience loading or manipulating tabular data programmatically** (CSV loading,
  pandas/numpy-style structures) — needed for the very first hands-on step of any
  project-based module, independent of ML content itself.
- **No exposure to the supervised-learning paradigm** (train vs. test, fitting vs.
  predicting, why splitting is done at all) — this is the conceptual scaffolding target
  outcome 1 depends on and cannot be assumed.
- **No prior use of scikit-learn or any ML library** — the fit/predict/score convention
  needs an explicit on-ramp; it cannot be assumed as "obvious" the way it might be for a
  learner with prior R or MATLAB modeling experience.

### Placement check

Self-administer this in one sitting (should take under 15 minutes). It is not scored by
the assessor — score yourself using the rule at the end. It exists to confirm or correct
the L0 placement above before module 1 is built, not to gate access to the course.

1. **(Python)** Write a function that takes a list of numbers and returns their average.
2. **(Python/data)** Given `rows = [{"age": 25, "income": 50000}, {"age": 40, "income":
   80000}, {"age": 31, "income": 62000}]`, write code to compute the average `"age"`
   across all rows.
3. **(Statistics)** What is the difference between the *mean* and the *median* of a
   dataset? Give an example of a dataset where they would differ substantially.
4. **(Probability)** If you flip a fair coin 3 times, what is the probability of getting
   exactly 2 heads?
5. **(ML concept)** In your own words: what is the difference between *training* a model
   and *testing* it, and why do we split data into two sets instead of using it all for
   both?
6. **(ML concept)** What does it mean for a model to "overfit" its training data?
7. **(Tooling)** Have you ever used scikit-learn, pandas, or numpy? Describe what you did
   — or answer "never used any of these."
8. **(Applied evaluation)** A classifier predicts "not spam" for every single email in a
   test set that is 95% not-spam and 5% spam. What is its accuracy? Why might accuracy
   alone be a misleading way to judge this classifier?

**Answer key**

1. Any correct implementation, e.g. `sum(nums) / len(nums)` (guard for empty list is a
   bonus, not required).
2. `sum(r["age"] for r in rows) / len(rows)` → 32.0, or an equivalent loop.
3. Mean = arithmetic average of all values; median = the middle value when sorted. They
   diverge when the data has outliers or skew — e.g., salaries of $40k, $45k, $50k, and
   one CEO at $2M: the mean is pulled far above what the median shows as typical.
4. 3/8 = 0.375 (three ways to get 2 heads out of 8 equally likely 3-flip outcomes).
5. Training = fitting the model's parameters on known data; testing = evaluating it on
   data it did not see during training, to estimate how it will perform on genuinely new
   data. Splitting prevents mistaking memorization of the training set for real
   predictive ability.
6. Overfitting means the model has fit the training data too closely — including its
   noise and quirks — so it performs well on training data but poorly on new, unseen
   data.
7. Any concrete description of prior use counts as partial credit; "never used any of
   these" is the expected answer given the stated baseline and is not a bad outcome.
8. Accuracy = 95% (matching the majority class every time); this is misleading because
   the classifier catches zero actual spam — precision and recall on the spam class
   would reveal the real (poor) performance that accuracy alone hides.

**Scoring rule**

Count answers that are correct or substantially correct (partial credit counts as a
half point) out of 8:

- **0–2 correct** — confirms the assessed L0 baseline exactly as scoped above. Start
  module 1 with no adjustment; the woven-in statistics and tooling on-ramps are exactly
  as needed.
- **3–5 correct** — some self-study has likely happened since requirements were
  gathered (commonly Q1–Q2 plus one of Q3/Q4). Still start at module 1, but flag to the
  curriculum which specific items (by question number) already land, so those moments
  can move faster.
- **6–8 correct** — placement is likely higher than L0 (closer to L1). Re-confirm with
  whoever runs `curriculum-architect` before finalizing module 1's pacing; the woven-in
  statistics primer may be redundant for this learner.

Q1–Q2 failing would be the one result that *contradicts* stated requirements (they
claimed working Python fundamentals); everything else scoring low is the expected,
already-assumed outcome.

## Sources

- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning) — Wikipedia · accessed 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning) — Wikipedia · accessed 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Bias-variance tradeoff](https://en.wikipedia.org/wiki/Bias-variance_tradeoff) — Wikipedia · accessed 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Cross-validation (statistics)](https://en.wikipedia.org/wiki/Cross-validation_(statistics)) — Wikipedia · accessed 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn) — Wikipedia · accessed 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18
- [Outline of machine learning](https://en.wikipedia.org/wiki/Outline_of_machine_learning) — Wikipedia · accessed 2026 · article · n/a · free · verified: mcp:wikipedia 2026-08-18

## Open Questions

- **No standard external proficiency framework exists for classical ML**, unlike CEFR
  for languages or ABRSM grades for music. Wikipedia's ML/supervised-learning/outline
  articles describe the field's conceptual decomposition (statistical foundations →
  train/fit workflow → generalization) but not a named beginner-to-practitioner scale.
  The four-level "Classical ML Practitioner Progression" above is therefore explicitly
  defined by this assessment, not an established external standard — it should not be
  cited elsewhere as one.
- **Assumed "Python basics: loops, functions, lists/dicts" does not extend to
  pandas/numpy or tabular-data handling**, since neither was mentioned in requirements.
  Placement check Q2 (list-of-dicts averaging) is designed to resolve this either way
  without a data library.
- **Assumed "no statistics background" means a true zero**, not "learned it once and
  forgot it," since requirements state it as flatly as "no prior ML exposure."
  Placement check Q3–Q4 would surface any residual, non-zero prior exposure.
