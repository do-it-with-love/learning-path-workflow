---
artifact: effort-budget
owner: effort-budget-aggregator
run_id: run-002-machine-learning
status: final
attempt: 2
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
generated: 2026-08-19T00:00:00Z
---

# Effort & Budget — Machine Learning (classical, project-based)

## Summary

Total cost is **$0** against a **$0 (free-only, hard-constraint) budget** — gate G3
passes exactly, re-verified line-by-line against all 17 resources in `resources.md`
attempt 2. Total designed effort is **1,613 min = 26.88h** against **1,800 min (30h)
available** (3h/week × 10 weeks) — it fits, with **187 min (3.12h, 10.4%)** of margin,
re-derived independently from every module's own resource/practice/assessment lines
rather than trusted from the curator's stated total (which matches, digit for digit).
This closes both gate failures from attempt 1: the Module 2/3 resource-hour undercount
this artifact originally flagged is gone (both modules' subtotals are now explicit sums
in `resources.md` and check out), and the resulting slack (10.4%) is comfortably above
the thin 3.9% margin the validator computed on the broken numbers. There is no monetary
cost driver — every resource remains free — so the single biggest driver of the plan is
still *time*: the capstone (Module 9) at 5.17h is the largest single module, and Module 3
(3.18h) is now the largest non-capstone module, edging out Module 7 (3.08h) now that
Module 7 lost its removed scikit-learn example. The free-only variant **is** this path;
nothing paid was dropped, and nothing essential would be bought by paying.

## Findings

### Money

All 17 resources in `resources.md` attempt 2 were checked individually against its own
Findings-section entries — every one is `free`, including the two new Kaggle exercise
notebooks (Summary Functions and Maps, Module 1; Categorical Variables, Module 8), which
require only the same free Kaggle account already needed for other modules — no separate
payment or paid tier. None are recurring subscriptions (Kaggle Learn/Competitions and
scikit-learn documentation carry no paid tier; UCI datasets are one-time downloads), so
there is no "€X/month × path length" conversion to do here, and none of attempt 1's
resources that were removed (the Module 5 OLS/Ridge example, the Module 7
underfitting/overfitting example) were paid either — their removal is a G8 modality fix,
not a cost change.

| Resource | Module | Type | Unit cost | Cost over path |
|---|---|---|---|---|
| Learn Pandas | 1 | one-off (free access) | $0 | $0 |
| Exercise: Summary Functions and Maps | 1 | one-off (free access, new this attempt) | $0 | $0 |
| Intro to Machine Learning | 2 | one-off (free access) | $0 | $0 |
| Getting Started (scikit-learn docs) | 2 | one-off (free access) | $0 | $0 |
| Titanic – Machine Learning from Disaster | 3 | one-off (free access) | $0 | $0 |
| Logistic Regression (scikit-learn user guide) | 3 | one-off (free access) | $0 | $0 |
| Metrics and scoring — classification metrics | 4 | one-off (free access) | $0 | $0 |
| Confusion matrix example | 4 | one-off (free access) | $0 | $0 |
| House Prices – Advanced Regression Techniques | 5 | one-off (free access) | $0 | $0 |
| Metrics and scoring — regression metrics | 6 | one-off (free access) | $0 | $0 |
| Plotting Cross-Validated Predictions | 6 | one-off (free access) | $0 | $0 |
| Cross-Validation (Kaggle lesson) | 7 | one-off (free access) | $0 | $0 |
| Cross-validation: evaluating estimator performance | 7 | one-off (free access) | $0 | $0 |
| Pipelines (Kaggle lesson) | 8 | one-off (free access) | $0 | $0 |
| Exercise: Categorical Variables | 8 | one-off (free access, new this attempt) | $0 | $0 |
| Adult (UCI dataset) | 9 | one-off (free access) | $0 | $0 |
| Wine Quality (UCI dataset) | 9 | one-off (free access) | $0 | $0 |
| **Total (17 resources)** | | | | **$0** |

**Arithmetic:** 17 rows × $0 unit cost = $0. Sum of the "cost over path" column = $0.

**Budget comparison:** $0 total ≤ $0 budget (free-only, hard constraint). **Gate G3:
PASS**, exactly at the ceiling — unchanged from attempt 1; this gate never failed and
the retry did not touch it.

The only non-monetary "account cost" anywhere in the plan is a free Kaggle account
(email signup, no card), now first required in **Module 1** (for the new Summary
Functions exercise) rather than Module 3 as in attempt 1 — see Hidden costs for the
phone-verification question, which `resources.md` reports as resolved this run.

### Time

Resource hours are taken verbatim from `resources.md` attempt 2's Coverage-check table,
then independently re-summed from that table's own module-level arithmetic (each module
now shows its minutes as an explicit sum of its resource lines plus setup, so this is a
direct check, not a trust exercise). Practice hours are taken from `exercises.md`'s
practice-load table (unchanged from attempt 1 — `exercises.md` was not revised this
attempt). Assessment hours are taken from `assessments.md`'s per-checkpoint times
(likewise unchanged). Module 9's practice (10 min) and Final check are, as both owning
artifacts state explicitly, embedded inside the module's own 5.17h and excluded from the
additive sums below.

| Module | Resource hours | Practice hours | Assessment hours | Module total |
|---|---|---|---|---|
| 1. Tabular Data & Descriptive Statistics | 86 min = 1.43h | 25 min = 0.42h | 15 min = 0.25h | 126 min = 2.10h |
| 2. Supervised Learning Workflow | 140 min = 2.33h | 30 min = 0.50h | 15 min = 0.25h | 185 min = 3.08h |
| 3. Classification I | 146 min = 2.43h | 30 min = 0.50h | 15 min = 0.25h | 191 min = 3.18h |
| Cumulative review 1 (after Module 3) | — | — | 20 min = 0.33h | 20 min = 0.33h |
| 4. Evaluating Classifiers | 60 min = 1.00h | 30 min = 0.50h | 15 min = 0.25h | 105 min = 1.75h |
| 5. Regression I | 126 min = 2.10h | 30 min = 0.50h | 15 min = 0.25h | 171 min = 2.85h |
| 6. Evaluating Regressors | 90 min = 1.50h | 30 min = 0.50h | 15 min = 0.25h | 135 min = 2.25h |
| Cumulative review 2 (after Module 6) | — | — | 20 min = 0.33h | 20 min = 0.33h |
| 7. Overfitting, Underfitting & Generalization | 120 min = 2.00h | 45 min = 0.75h | 20 min = 0.33h | 185 min = 3.08h |
| 8. Feature Engineering & Preparing Real Data | 120 min = 2.00h | 30 min = 0.50h | 15 min = 0.25h | 165 min = 2.75h |
| 9. Capstone | 310 min = 5.17h | embedded (10 min, not additive) | embedded (Final check, not additive) | 310 min = 5.17h |
| **Total** | **1,198 min = 19.97h** | **250 min = 4.17h** | **165 min = 2.75h** | **1,613 min = 26.88h** |

**Arithmetic, shown module-by-module (matches `resources.md`'s own per-module sums):**
- Module 1: 86 (60+20+6 setup) + 25 + 15 = 126 min.
- Module 2: 140 (120+20) + 30 + 15 = 185 min.
- Module 3: 146 (120+20+6 setup) + 30 + 15 = 191 min.
- Module 4: 60 (30+30) + 30 + 15 = 105 min.
- Module 5: 126 (120+6 setup) + 30 + 15 = 171 min.
- Module 6: 90 (30+60) + 30 + 15 = 135 min.
- Module 7: 120 (90+30) + 45 + 20 = 185 min.
- Module 8: 120 (90+30) + 30 + 15 = 165 min.
- Module 9: 310 (300 build + 10 setup) + 0 (embedded) + 0 (embedded) = 310 min.
- Cumulative reviews: 20 + 20 = 40 min (not tied to a single module).

**Column totals, independently re-summed:**
- Resource hours: 86+140+146+60+126+90+120+120+310 = **1,198 min = 19.97h** (matches
  `resources.md`'s own stated total exactly).
- Practice hours (additive only, excludes Module 9's embedded 10 min):
  25+30+30+30+30+30+45+30 = **250 min = 4.17h** (matches `exercises.md`'s own additive
  figure).
- Assessment hours (additive only, excludes Module 9's embedded Final check):
  15+15+15+20+15+15+15+20+20+15 = **165 min = 2.75h** (matches `assessments.md`'s own
  stated "2 hours 45 minutes").
- **Grand total: 1,198 + 250 + 165 = 1,613 min = 26.88h.**

**Comparison against 1,800 min (30h) available (3h/week × 10 weeks):** 1,613 ≤ 1,800.
**Fits**, with **187 min = 3.12h (10.4%)** of margin — 187/1,800 = 0.1039.

**What changed from attempt 1, and why the gate now passes:**
- Attempt 1's stated resource-hours total (1,254 min / 20.90h) silently dropped 30 min
  each from Modules 2 and 3 relative to their own cited resource-line durations — that
  was this artifact's own finding, confirmed by the validator as the G1 root cause.
- Attempt 2 does not merely restore those 30+30 = 60 min. It also **trims three
  over-estimated reference reads** elsewhere (per `resources.md`'s Summary) and
  **removes two resource lines outright** (Module 5's OLS/Ridge example, 6 min per its
  own module total was folded into the removed line rather than a standalone entry so
  no separate subtraction is needed here; Module 7's underfitting/overfitting example),
  replacing lost interactive weight with two new graded Kaggle exercises rather than
  padding hours. Net effect: resource hours actually *fell* slightly, from the
  validator's corrected 1,314 min (21.9h) to this attempt's 1,198 min (19.97h) — a
  116-minute reduction — even though the specific Module 2/3 undercount that caused the
  G1 failure is now fixed.
- Grand total moved from the validator's corrected 1,729 min (28.82h, 3.9% slack) down
  to 1,613 min (26.88h, 10.4% slack) — genuine margin, not a rounding artifact.

**Per-module check against a nominal 3h (180 min) single week**, since 9 modules over
10 weeks means most modules occupy roughly one week each (informative only —
`schedule.md` was not an input to this artifact, same as attempt 1; see Open Questions):
- Module 2: 185 min — 5 min over a nominal 3h week, but 13 min under gate G1's own
  110%-tolerance ceiling of 198 min.
- Module 3: 191 min — 11 min over a nominal 3h week, and still 7 min under the 198-min
  ceiling. This is the module the validator's Week 3 breach (201 min) traced to; with
  the corrected resource line (146 min, not the old undercounted or over-corrected
  figure), Module 3 alone no longer breaches 198 min even before any rebalancing.
- Module 7: 185 min — 5 min over a nominal 3h week, 13 min under 198 min; lighter than
  attempt 1's 245 min (4.08h) now that its misclassified example is gone.
- Module 9: 310 min — expected to span roughly 1.7 weeks (310 ÷ 180), not a single week;
  this is a scheduling matter, not a budget failure.
- All other modules (1, 4, 5, 6, 8) fit inside a 3h week individually with room to
  spare.
- None of the per-module totals above exceed 198 min on their own, so — on this
  artifact's numbers alone — there is no module that mechanically forces a Week
  reshuffle the way attempt 1's Module 3 did. Confirming this against the actual week
  packing is `schedule-planner`'s job on its own cascade re-run.

**Possible double-count with Kaggle's own graded exercises — re-checked, now covers
Module 1 as well as Module 2.** `resources.md`'s own Open Questions this attempt state
plainly: "Modules 1, 2, 3, 5, 7, and 8 now each carry at least one Kaggle resource with
its own auto-graded exercise or live leaderboard (**Module 1 gained one this
revision**)." Checking that claim directly against `exercises.md`'s Module 1 entries:
- Kaggle's new **Exercise: Summary Functions and Maps** has the learner independently
  compute `.describe()`, `.mean()`, `.std()`, and related summary functions on an
  unfamiliar dataset, auto-graded.
- `exercises.md`'s Module 1 **drill** ("hand vs. pandas") has the learner hand-compute
  mean/variance/std on 10 rows and verify against `.mean()`/`.var()`/`.std()`; its
  **application** ("profile a whole dataset") has the learner produce mean/std/min/max
  for every numeric column and a categorical summary for every categorical column.
- These are the same underlying skill — computing and reading summary statistics —
  exercised three times in one module (once bespoke-drill, once bespoke-application,
  once Kaggle-graded) where attempt 1 had it exercised only twice (both bespoke, no
  Kaggle counterpart existed yet). This is the identical pattern already flagged for
  Module 2 in attempt 1 (its bespoke split/fit/score drill and application overlapping
  with the Kaggle `Intro to Machine Learning` course's own split-and-score exercise),
  now also present in Module 1.
- **Net effect on this budget: unchanged in direction.** As with the Module 2 instance,
  this is not a literal duplicate task (different datasets, different framing — hand
  arithmetic vs. an unfamiliar-dataset submission), so no minutes are removed from the
  additive total above. If a learner judges the overlap close enough to skip some
  bespoke practice, the real time need in Modules 1 and 2 is *lower* than 26.88h, not
  higher — a slack opportunity, consistent with the conservative (safe) direction used
  throughout. This is reported rather than resolved because only this artifact sees
  `exercises.md`'s bespoke minutes and `resources.md`'s Kaggle-graded minutes side by
  side; `exercise-designer` and `curator` each estimated their own slice correctly on
  its own terms.

### Hidden costs

Nothing here is monetary (the whole plan is $0), but several items are not budgeted as
line items and are exactly the kind of thing a learner would resent discovering
mid-path. Carried forward from attempt 1 except where noted as changed:

- **Kaggle competition-submission phone verification — resolved this attempt (was
  unresolved in attempt 1).** `resources.md` cites a live-verified Kaggle product
  announcement confirming phone verification applies to accounts earning progression
  points, medals, or prizes, and to publishing public Models — not to submitting
  predictions to a "Getting Started" competition like Titanic (Module 3) or House
  Prices (Module 5), which award neither. No phone number is required anywhere in this
  plan. Still $0 either way, but the friction risk this artifact flagged last attempt
  is now closed rather than open.
- **Free Kaggle account now required starting in Module 1**, not Module 3 as in
  attempt 1 (the new Summary Functions exercise needs one). The 6-minute signup cost is
  already counted inside Module 1's resource-hours arithmetic above, so this is a
  *timing* change, not an uncounted cost.
- **Kaggle notebook session limits.** Kaggle's browser notebooks have a maximum session
  runtime and an idle timeout. The capstone (Module 9, 5.17h of build time) is very
  likely to span more than one sitting; a learner who doesn't save/commit their
  notebook mid-session risks losing unsaved work. Not costed, since it doesn't add hours
  if the learner saves regularly, but worth a one-line warning.
- **Binder / JupyterLite cold starts — smaller footprint than attempt 1.** Only **two**
  of the 17 resources now launch via Binder/JupyterLite rather than running locally
  (Module 4's confusion-matrix example, Module 6's cross-validated-predictions example),
  down from five in attempt 1 — both removed examples (Modules 5 and 7) were also
  Binder/JupyterLite-hosted, so their removal shrinks this risk as a side effect, not
  just a G8 fix. Binder in particular is known for multi-minute cold starts and
  occasional build failures under load; the ~0.5–1h estimates for those two examples
  don't include this startup time.
- **Capstone dataset scale asymmetry — unchanged.** Adult (48,842 rows) is ~10× the size
  of Wine Quality (4,898 rows). Both train in seconds on any modern machine or in a
  Kaggle/Colab session, so this is not a training-time problem, but a learner in a
  constrained or throttled free-tier browser session may notice Adult is noticeably
  slower to load, explore, and plot — an asymmetry in effort across the two "equal"
  capstone halves that isn't visible from the hour estimate alone.
- **Colab free-tier throttling — checked, not applicable, unchanged.** Nothing in this
  plan routes through Google Colab; all notebook work is Kaggle-hosted or
  Binder/JupyterLite-hosted per `resources.md`.
- **No textbook, workbook, tuner, exam fee, or equipment cost applies to this
  subject — unchanged.** Entirely browser/code-based; no analogous "required workbook"
  trap here.

### Free-only variant

This path **already is** the free-only variant — there is no paid version to strip out
and no coverage to lose, unchanged from attempt 1. All 17 resources (including both new
Kaggle exercises) are free by construction, verified individually above, so there is
nothing to recompute.

**What a paid alternative would buy: nothing essential.** Paid platforms in this space
(a structured MOOC with a certificate, a paid book with worked datasets, an
instructor-graded course) would typically add smoother pacing, human feedback on
open-ended judgment calls, or a certificate — none of which are required by any of the
six target outcomes in `requirements.md`, all of which are met here through Kaggle's
auto-graded exercises/leaderboards, scikit-learn's own documentation and runnable
examples, and two free UCI datasets. Paying here would buy convenience and
credentialing, not additional capability the learner needs.

## Sources

None. No currency conversion was performed — every resource in `resources.md` was
already denominated in the learner's target of $0, so no exchange rate or price source
was consulted.

## Open Questions

- **Module-to-week mapping for Modules 2, 3, 7, and 9 was not confirmed against an
  actual weekly schedule**, because `schedule.md` was not among this artifact's inputs
  (same scope as attempt 1). None of these modules' totals exceed the 198-min (3.30h)
  per-week ceiling individually, so on this artifact's numbers alone no reshuffle is
  mechanically forced — but `schedule-planner`'s own cascade re-run is what confirms
  the 187-min (3.12h) overall margin is actually reachable week by week, not
  concentrated in a way that leaves any single week short once cumulative reviews are
  folded in.
- **Possible practice/resource skill overlap, now present in Modules 1, 2, 3, 5, 7, and
  8** (see Findings → Time → "Possible double-count," updated this attempt to include
  Module 1's new overlap alongside Module 2's previously-flagged one) could not be
  resolved to a specific number of overlapping minutes from the text alone. The
  assumption used is that all designed practice time is genuinely additive — the
  conservative direction for a budget check, since any overlap would only create slack,
  not a shortfall. `resources.md`'s own Open Questions this attempt suggest
  `exercise-designer` redirect these modules' bespoke exercises toward synthesis rather
  than re-deriving what Kaggle already grades; that is a design decision for the
  coordinator to route, not something this artifact can resolve on its own.
- **Capstone dataset "messiness" is unpredictable**, carried forward from attempt 1 and
  from `curriculum.md`'s own Open Questions: if the learner's self-chosen or provided
  capstone dataset requires nonstandard cleanup, the 5.17h allocated to Module 9 may run
  short. Not something additional budget can absorb given the 10.4% slack is a
  plan-wide margin, not a per-module reserve.
