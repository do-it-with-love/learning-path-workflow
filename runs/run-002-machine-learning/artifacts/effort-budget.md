---
artifact: effort-budget
owner: effort-budget-aggregator
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

# Effort & Budget — Machine Learning (classical, project-based)

## Summary

Total cost is **$0** against a **$0 (free-only, hard-constraint) budget** — gate G3
passes exactly, verified line-by-line against all 17 resources in `resources.md` (none
are subscriptions; none carry a hidden paid tier). Total designed effort is **27h49m
(27.82h)** against **30h available** (3h/week × 10 weeks) — it fits, with **2h11m
(2.18h)** of margin — but it **exceeds `curriculum.md`'s own 25.5h content estimate by
2h19m (2.32h)**, because the 4.5h of slack the curriculum reserved for practice and
checkpoints was undersized against what `exercise-designer` and `assessment-designer`
actually designed (6.92h combined, additive). There is no monetary cost driver — every
resource is free — so the single biggest driver of the plan is *time*: Module 7
(Overfitting, Underfitting & Generalization) at 4h05m is the largest single-week load,
and the capstone (Module 9) at 5h12m is the largest module overall but is expected to
span more than one week. The free-only variant **is** this path; nothing paid was
dropped, and nothing essential would be bought by paying.

## Findings

### Money

All 17 resources in `resources.md` were checked individually — every one is listed as
`free` with no signup fee, no paywall, and no trial-only access. None are recurring
subscriptions (Kaggle Learn/Competitions and scikit-learn documentation carry no paid
tier; UCI datasets are one-time downloads), so there is no "€X/month × path length"
conversion to do here.

| Resource | Module | Type | Unit cost | Cost over path |
|---|---|---|---|---|
| Learn Pandas | 1 | one-off (free access) | $0 | $0 |
| Intro to Machine Learning | 2 | one-off (free access) | $0 | $0 |
| Getting Started (scikit-learn docs) | 2 | one-off (free access) | $0 | $0 |
| Titanic – Machine Learning from Disaster | 3 | one-off (free access) | $0 | $0 |
| Logistic Regression (scikit-learn user guide) | 3 | one-off (free access) | $0 | $0 |
| Metrics and scoring — classification metrics | 4 | one-off (free access) | $0 | $0 |
| Confusion matrix example | 4 | one-off (free access) | $0 | $0 |
| House Prices – Advanced Regression Techniques | 5 | one-off (free access) | $0 | $0 |
| Linear regression example (OLS / Ridge) | 5 | one-off (free access) | $0 | $0 |
| Metrics and scoring — regression metrics | 6 | one-off (free access) | $0 | $0 |
| Plotting Cross-Validated Predictions | 6 | one-off (free access) | $0 | $0 |
| Cross-Validation (Kaggle lesson) | 7 | one-off (free access) | $0 | $0 |
| Underfitting vs. Overfitting example | 7 | one-off (free access) | $0 | $0 |
| Cross-validation: evaluating estimator performance | 7 | one-off (free access) | $0 | $0 |
| Pipelines (Kaggle lesson) | 8 | one-off (free access) | $0 | $0 |
| Adult (UCI dataset) | 9 | one-off (free access) | $0 | $0 |
| Wine Quality (UCI dataset) | 9 | one-off (free access) | $0 | $0 |
| **Total (17 resources)** | | | | **$0** |

**Arithmetic:** 17 rows × $0 unit cost = $0. Sum of the "cost over path" column = $0.

**Budget comparison:** $0 total ≤ $0 budget (free-only, hard constraint). **Gate G3:
PASS**, exactly at the ceiling.

The only non-zero "price" anywhere in the plan is a free Kaggle account (email
signup, no card) — `resources.md` states this needs no phone verification because
nothing assigned requires internet-enabled or GPU notebooks. That claim covers
*notebook* access; it does not address whether *submitting* to the Titanic (Module 3)
or House Prices (Module 5) competition leaderboards separately requires phone
verification. This carries no monetary cost either way and is recorded under Hidden
costs and Open Questions below rather than in the money table, since it would still be
$0 if true.

### Time

Resource hours are taken verbatim from `resources.md`'s per-module coverage-check
table (including its module-9 total of 5.0h build time + 0.2h dataset download =
5.2h, which is how `resources.md`'s own stated grand total of "~20.9h" reconciles).
Practice hours are taken from `exercises.md`'s practice-load table. Assessment hours
are taken from `assessments.md`'s per-checkpoint times, with the two cumulative
reviews listed as their own rows since they don't belong to a single module. Module 9's
practice (10 min) and Final check are explicitly stated by their owning artifacts as
**embedded inside the module's existing 5.2h**, not additive — they are shown as
"embedded" and excluded from the additive sums so the total isn't inflated.

| Module | Resource hours | Practice hours | Assessment hours | Module total |
|---|---|---|---|---|
| 1. Tabular Data & Descriptive Statistics | 1.60h (96 min) | 0.42h (25 min) | 0.25h (15 min) | 2.27h |
| 2. Supervised Learning Workflow | 2.00h (120 min) | 0.50h (30 min) | 0.25h (15 min) | 2.75h |
| 3. Classification I | 2.10h (126 min) | 0.50h (30 min) | 0.25h (15 min) | 2.85h |
| Cumulative review 1 (after Module 3) | — | — | 0.33h (20 min) | 0.33h |
| 4. Evaluating Classifiers | 1.50h (90 min) | 0.50h (30 min) | 0.25h (15 min) | 2.25h |
| 5. Regression I | 2.50h (150 min) | 0.50h (30 min) | 0.25h (15 min) | 3.25h |
| 6. Evaluating Regressors | 1.50h (90 min) | 0.50h (30 min) | 0.25h (15 min) | 2.25h |
| Cumulative review 2 (after Module 6) | — | — | 0.33h (20 min) | 0.33h |
| 7. Overfitting, Underfitting & Generalization | 3.00h (180 min) | 0.75h (45 min) | 0.33h (20 min) | 4.08h |
| 8. Feature Engineering & Preparing Real Data | 1.50h (90 min) | 0.50h (30 min) | 0.25h (15 min) | 2.25h |
| 9. Capstone | 5.20h (5.0h build + 0.2h dataset download) | embedded (10 min, not additive) | embedded (Final check, not additive) | 5.20h |
| **Total** | **20.90h (1,254 min)** | **4.17h (250 min additive)** | **2.75h (165 min additive)** | **27.82h (1,669 min = 27h49m)** |

**Arithmetic:**
- Resource hours: 96+120+126+90+150+90+180+90+312 = 1,254 min = 20.90h.
- Practice hours (additive only, excludes Module 9's embedded 10 min):
  25+30+30+30+30+30+45+30 = 250 min = 4.17h. (`exercises.md`'s own stated total of
  260 min includes that embedded 10 min; 250 min is the portion that adds to the
  grand total.)
- Assessment hours (additive only, excludes Module 9's embedded Final check):
  15+15+15+20+15+15+15+20+20+15 = 165 min = 2.75h, matching `assessments.md`'s
  own stated "2 hours 45 minutes."
- Grand total: 1,254 + 250 + 165 = 1,669 min = 27.82h = 27h49m.

**Comparison against 30h available (3h/week × 10 weeks):** 27.82h ≤ 30h. **Fits**,
with 2h11m (2.18h, ~7.3%) of margin.

**Comparison against curriculum's 25.5h content allocation:** 27.82h > 25.5h, an
**overrun of 2h19m (2.32h, ~9.1%)**. This is not a contradiction of the first
comparison — it is a mismatch between how `curriculum.md` framed its own budget and
what was actually produced downstream:
- `curriculum.md` allocated 25.5h to module content and explicitly reserved 4.5h
  (30h − 25.5h) as slack "as instructed."
- Actual resource hours came in at 20.9h — 4.6h *under* the 25.5h estimate.
- But `exercise-designer` and `assessment-designer`, working independently and in
  parallel, together added 6.92h of additive practice + assessment time — 2.42h
  *over* the 4.5h slack curriculum reserved for exactly this.
- The resource-hour underrun (4.6h) almost, but not quite, absorbs the practice/
  assessment overrun (6.92h), leaving the net 2.32h overrun against the 25.5h figure
  — while still fitting under the hard 30h ceiling because of the underrun.

**Per-module overrun check** (against a nominal 3h/week single-module allowance,
since 9 modules over 10 weeks means most modules occupy roughly one week each):
- Module 5 (Regression I): 3.25h — **0.25h over** a 3h week.
- Module 7 (Overfitting/Underfitting/Generalization): 4.08h — **1.08h over** a 3h
  week; this is also the module carrying the hard-gate checkpoint
  (`assessments.md`'s non-negotiable "not yet" rule), so it is the single tightest
  and highest-stakes week in the path.
- Module 9 (Capstone): 5.20h — over a single week, but expected to span roughly two
  weeks (5.2h ÷ 3h/week ≈ 1.7 weeks); this is a scheduling matter, not a budget
  failure, but it is not confirmed here since `schedule.md` was not an input to this
  artifact (see Open Questions).
- All other modules (1–4, 6, 8) fit inside a 3h week individually.

**Possible double-count, checked explicitly.** `resources.md`'s Open Questions flag
that Kaggle's own auto-graded exercises already supply practice for Modules 2, 3, 5,
7, and 8, and ask whether `exercises.md` separately budgets time for the same work.
Checking both artifacts side by side:
- `exercises.md`'s own Open Questions show the exercise-designer read that flag and
  responded by design: bespoke exercises for those five modules were deliberately
  aimed at *synthesis across skills* (e.g. Module 4's imbalance exercise, Module 7's
  cross-validation-on-your-own-models exercise) rather than *re-deriving* the exact
  task Kaggle already grades (e.g. re-doing a plain train/test split).
- This means the hours are **not a literal duplicate** of the same task counted
  twice — no single exercise appears both as a Kaggle lesson step and as a bespoke
  exercise with the same deliverable.
- However, the boundary is not fully clean. Module 2's bespoke drill ("split
  instability," 10 min) and application ("first end-to-end model," 20 min) both
  re-exercise the same split→fit→score motion that Module 2's Kaggle course
  resource (`Intro to Machine Learning`) already has the learner perform as part of
  its own 2.0h. The two are not identical tasks, but they are the same skill
  practiced twice within the same module, and the combined 30 minutes is being
  counted as pure incremental time here.
- **Net effect on this budget:** if a learner judges the Kaggle-graded practice in
  Modules 2, 3, 5, 7, and 8 (30+30+30+45+30 = 165 min = 2.75h of bespoke practice
  across those five modules) sufficiently overlapping to skip some of it, the real
  time need is *lower* than 27.82h, not higher — this is a slack opportunity, not a
  budget risk, given the direction of the possible error. It is reported here rather
  than resolved because only the accountant sees both artifacts' hour figures
  together; `exercise-designer` and `curator` each estimated their own slice
  correctly on its own terms.

### Hidden costs

Nothing here is monetary (the whole plan is $0), but several items were not
budgeted as line items and are exactly the kind of thing a learner would resent
discovering mid-path:

- **Kaggle competition phone verification (Modules 3, 5) — unresolved.**
  `resources.md` states no phone verification is needed because nothing here uses
  GPU or internet-enabled notebooks, but that claim does not address whether
  *submitting a prediction file* to the Titanic or House Prices leaderboard requires
  phone verification (a real, separate Kaggle account-security gate independent of
  compute type). If it does, it is still $0 but requires a phone number the learner
  may not want to give up — a friction cost, not a money cost.
- **Kaggle notebook session limits.** Kaggle's browser notebooks have a maximum
  session runtime and an idle timeout. The capstone (Module 9, 5.2h of build time)
  is very likely to span more than one sitting; a learner who doesn't save/commit
  their notebook mid-session risks losing unsaved work. Not costed, since it doesn't
  add hours if the learner saves regularly, but worth a one-line warning.
- **Binder / JupyterLite cold starts.** Five of the scikit-learn `auto_examples`
  resources (Modules 4, 5, 6, 7) launch via Binder or JupyterLite rather than
  running locally. Binder in particular is known for multi-minute cold starts and
  occasional build failures under load; none of the ~0.5–1h estimates for those
  examples include this startup time.
- **Capstone dataset scale asymmetry.** The Adult dataset (48,842 rows) is ~10× the
  size of Wine Quality (4,898 rows). Both train in seconds on any modern machine or
  in a Kaggle/Colab session, so this is not a training-time problem, but a learner
  working in a constrained or throttled free-tier browser session (slow connection,
  low-powered device) may notice Adult is noticeably slower to load, explore, and
  plot than Wine Quality — an asymmetry in effort across the two "equal" capstone
  halves that isn't visible from the hour estimate alone.
- **Colab free-tier throttling — checked, not applicable.** Nothing in this plan
  routes through Google Colab; all notebook work is Kaggle-hosted or Binder/
  JupyterLite-hosted per `resources.md`. Flagged as checked and cleared, not as a
  live risk.
- **No textbook, workbook, tuner, exam fee, or equipment cost applies to this
  subject** — unlike a language or instrument path, this is entirely
  browser/code-based, so there is no analogous "required workbook" trap here.

### Free-only variant

This path **already is** the free-only variant — there is no paid version to strip
out and no coverage to lose. All 17 resources are free by construction (the curator
ran under the same $0 hard constraint verified above), so there is nothing to
recompute.

**What a paid alternative would buy: nothing essential.** Paid platforms in this
space (e.g. a structured MOOC with a certificate, a paid book with worked datasets,
an instructor-graded course) would typically add smoother pacing, human feedback on
open-ended judgment calls, or a certificate — none of which are required by any of
the six target outcomes in `requirements.md`, all of which are met here through
Kaggle's auto-graded exercises/leaderboards, scikit-learn's own documentation and
runnable examples, and two free UCI datasets. Stated plainly, as instructed: paying
here would buy convenience and credentialing, not additional capability the learner
needs.

## Sources

None. No currency conversion was performed — every resource in `resources.md` was
already denominated in the learner's target of $0, so no exchange rate or price
source was consulted.

## Open Questions

- **Whether Kaggle requires phone verification to *submit* to a competition
  leaderboard (Modules 3 and 5) is unresolved.** `resources.md` verifies only that
  GPU/internet-enabled notebooks aren't needed. Assumption used: treated as $0 cost
  either way in the money table, since Kaggle's phone verification carries no fee;
  flagged under Hidden costs as a possible friction point rather than assumed
  resolved.
- **`resources.md`'s own per-module coverage-check subtotals for Modules 2 and 3
  appear to undercount by ~0.5h each relative to summing that module's individual
  resource-line times** (Module 2: Kaggle "~2h" + scikit-learn "~0.5h" = 2.5h vs.
  the table's stated "~2.0h"; Module 3: Titanic "~2h" + Logistic Regression doc
  "~0.5h" = 2.5h vs. the table's stated "~2.1h"). This artifact used `resources.md`'s
  own stated per-module and grand-total figures (20.9h) throughout, per the
  instruction to use producing agents' numbers rather than re-estimate — but the
  inconsistency is real and, if resolved upward, would add up to ~1h more to the
  resource-hours total (pushing the grand total from 27.82h toward ~28.8h, still
  under the 30h ceiling but with less margin). Flagged for `resources.md`'s owner
  to reconcile on any retry.
- **Module-to-week mapping for Modules 5, 7, and 9 (each over the nominal 3h/week
  single-module allowance) was not confirmed against an actual weekly schedule**,
  because `schedule.md` was not among this artifact's inputs. Assumption used:
  treated Module 9 as spanning roughly two weeks based on its hour count alone.
  `schedule-planner`'s artifact should be checked to confirm the 2h11m of overall
  slack is actually distributed to cover these three heavier modules, not
  uniformly spread across all ten weeks in a way that leaves Module 7's single week
  short.
- **Possible practice/resource skill overlap in Modules 2, 3, 5, 7, and 8** (see
  Findings → Time → "Possible double-count, checked explicitly") could not be
  resolved to a specific number of overlapping minutes from the text alone — the
  assumption used is that all designed practice time is genuinely additive, which
  is the conservative (safer) direction for a budget check, since any overlap would
  only create slack, not a shortfall.
