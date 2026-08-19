---
artifact: effort-budget
owner: effort-budget-aggregator
run_id: run-002-machine-learning
status: final
attempt: 3
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
generated: 2026-08-19T15:00:00Z
---

# Effort & Budget — Machine Learning (classical, project-based)

## Summary

Total cost is **$0** against a **$0 (free-only, hard-constraint) budget** — gate G3
passes exactly, re-verified line-by-line against all **19** resources in
`resources.md` attempt 3 (up from 17). Total designed effort is **1,613 min = 26.88h**
against **1,800 min (30h) available** (3h/week × 10 weeks) — it fits, with **187 min
(3.12h, 10.4%)** of margin. Both totals are **re-derived from the 19 resource lines
directly, not trusted from the curator's claim that they are unchanged** — the resource
list changed shape (two two-lesson citations each split into two per-lesson exercise
citations, in Modules 1 and 2), so every module subtotal was re-summed from its own
lines from scratch; the re-derivation confirms the curator's claim exactly, to the
minute, in every one of the 9 modules and in both grand totals. There is no monetary
cost driver — every one of the 19 resources is free, including all four resources the
curator swapped this attempt to fix gate G8 (they require only the same free Kaggle
account already budgeted since Module 1) — so the single biggest driver of the plan
remains *time*: the capstone (Module 9) at 5.17h is the largest single module. The
free-only variant **is** this path; nothing paid was dropped. One finding sharpens this
attempt rather than changing any number: the practice/resource skill-overlap risk
previously flagged for Module 2 (and, since attempt 2, Module 1) is now traceable to a
*specific* graded exercise in each module — "Exercise: Summary Functions and Maps"
(Module 1) and "Exercise: Model Validation" (Module 2) — rather than to a whole-course
citation, because the G8 fix that split those citations named the exact lesson doing
the overlapping work. It is not resolved, and it does not change any total (see Time).

## Findings

### Money

All 19 resources in `resources.md` attempt 3 were checked individually against its own
Findings-section entries — every one is `free`, including the two new per-lesson
exercise notebooks that replaced tutorial/landing-page citations in Modules 1, 2, 7,
and 8 as the G8 fix. All four swapped resources require only the same free Kaggle
account already needed elsewhere in the plan (first required in Module 1) — no new
signup, no separate payment, no paid tier. None are recurring subscriptions (Kaggle
Learn/Competitions and scikit-learn documentation carry no paid tier; UCI datasets are
one-time downloads), so there is still no "€X/month × path length" conversion to do.

| Resource | Module | Type | Unit cost | Cost over path |
|---|---|---|---|---|
| Exercise: Creating, Reading and Writing | 1 | one-off (free access, new this attempt — split from "Learn Pandas") | $0 | $0 |
| Exercise: Indexing, Selecting & Assigning | 1 | one-off (free access, new this attempt — split from "Learn Pandas") | $0 | $0 |
| Exercise: Summary Functions and Maps | 1 | one-off (free access, unchanged since attempt 2) | $0 | $0 |
| Getting Started (scikit-learn docs) | 2 | one-off (free access) | $0 | $0 |
| Exercise: Your First Machine Learning Model | 2 | one-off (free access, new this attempt — split from "Intro to Machine Learning") | $0 | $0 |
| Exercise: Model Validation | 2 | one-off (free access, new this attempt — split from "Intro to Machine Learning") | $0 | $0 |
| Titanic – Machine Learning from Disaster | 3 | one-off (free access) | $0 | $0 |
| Logistic Regression (scikit-learn user guide) | 3 | one-off (free access) | $0 | $0 |
| Metrics and scoring — classification metrics | 4 | one-off (free access) | $0 | $0 |
| Confusion matrix example | 4 | one-off (free access) | $0 | $0 |
| House Prices – Advanced Regression Techniques | 5 | one-off (free access) | $0 | $0 |
| Metrics and scoring — regression metrics | 6 | one-off (free access) | $0 | $0 |
| Plotting Cross-Validated Predictions | 6 | one-off (free access) | $0 | $0 |
| Exercise: Cross-Validation | 7 | one-off (free access, URL swapped this attempt — same lesson, now cites the graded page) | $0 | $0 |
| Cross-validation: evaluating estimator performance | 7 | one-off (free access) | $0 | $0 |
| Exercise: Pipelines | 8 | one-off (free access, URL swapped this attempt — same lesson, now cites the graded page) | $0 | $0 |
| Exercise: Categorical Variables | 8 | one-off (free access, unchanged since attempt 2) | $0 | $0 |
| Adult (UCI dataset) | 9 | one-off (free access) | $0 | $0 |
| Wine Quality (UCI dataset) | 9 | one-off (free access) | $0 | $0 |
| **Total (19 resources)** | | | | **$0** |

**Arithmetic:** 19 rows × $0 unit cost = $0. Sum of the "cost over path" column = $0.

**Budget comparison:** $0 total ≤ $0 budget (free-only, hard constraint). **Gate G3:
PASS**, exactly at the ceiling — unchanged from attempts 1 and 2. This gate has never
failed and this attempt's resource-count change (17→19) does not touch it: every new or
swapped line is $0, same as every line it replaced or split from.

The only non-monetary "account cost" anywhere in the plan is a free Kaggle account
(email signup, no card), required from **Module 1** — unchanged from attempt 2. The
phone-verification question (whether submitting to the Titanic/House Prices
competitions in Modules 3 and 5 requires a phone number) remains resolved per
`resources.md`'s Open Questions: it does not, since neither competition awards
progression points, medals, or prizes. See Hidden costs.

### Time

Resource hours are taken from `resources.md` attempt 3's Coverage-check table, then
**independently re-summed from each module's own resource lines**, not trusted from the
curator's claim that the total is unchanged — the instruction for this attempt was
explicit that a 17→19 line-count change is exactly the kind of edit that can silently
drop or double-count minutes even when a total is stated to hold. It does not, here:
every module's re-sum matches its own stated subtotal and matches attempt 2's subtotal
for that module, to the minute. Practice hours are taken from `exercises.md`'s
practice-load table (unchanged — `exercises.md` was not revised this attempt).
Assessment hours are taken from `assessments.md`'s per-checkpoint times (likewise
unchanged). Module 9's practice (10 min) and Final check are, as both owning artifacts
state explicitly, embedded inside the module's own 5.17h and excluded from the additive
sums below.

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

**Arithmetic, re-derived line-by-line from `resources.md` attempt 3's 19 resource
lines (not from its module subtotals):**
- Module 1 (3 lines, was 2): 30 (Exercise: Creating, Reading and Writing) + 30
  (Exercise: Indexing, Selecting & Assigning) + 20 (Exercise: Summary Functions and
  Maps) = 80 min resource lines, + 6 min Kaggle-account setup = **86 min** — matches
  attempt 2's 86 min (60 tutorial + 20 exercise + 6 setup) exactly; only the 60-min
  tutorial line became two 30-min exercise lines.
- Module 2 (3 lines, was 2): 20 (Getting Started) + 60 (Exercise: Your First Machine
  Learning Model) + 60 (Exercise: Model Validation) = **140 min**, no setup — matches
  attempt 2's 140 min (120 + 20) exactly; only the 120-min "Intro to Machine Learning"
  line became two 60-min exercise lines.
- Module 3 (2 lines, unchanged): 120 + 20 + 6 setup = **146 min** — unchanged.
- Module 4 (2 lines, unchanged): 30 + 30 = **60 min** — unchanged.
- Module 5 (1 line, unchanged): 120 + 6 setup = **126 min** — unchanged.
- Module 6 (2 lines, unchanged): 30 + 60 = **90 min** — unchanged.
- Module 7 (2 lines, unchanged count — pure URL swap): 90 (Exercise: Cross-Validation,
  same 90 min as attempt 2's tutorial citation) + 30 = **120 min** — unchanged.
- Module 8 (2 lines, unchanged count — pure URL swap): 90 (Exercise: Pipelines, same
  90 min as attempt 2's tutorial citation) + 30 = **120 min** — unchanged.
- Module 9 (2 lines, unchanged): 300 build + 10 setup = **310 min** — unchanged.
- Cumulative reviews (assessment-only, not resource lines): 20 + 20 = 40 min.

**Column totals, independently re-summed from the module figures above:**
- Resource hours: 86+140+146+60+126+90+120+120+310 = **1,198 min = 19.97h** — matches
  `resources.md`'s own stated total exactly, and matches attempt 2's total exactly.
  Checked twice: once as 19 individual resource-line numbers grouped by module (above),
  once as 9 module subtotals summed directly — both routes land on 1,198.
- Practice hours (additive only, excludes Module 9's embedded 10 min):
  25+30+30+30+30+30+45+30 = **250 min = 4.17h** (matches `exercises.md`'s own additive
  figure; `exercises.md` was not revised this attempt, so this could not have moved).
- Assessment hours (additive only, excludes Module 9's embedded Final check):
  15+15+15+20+15+15+15+20+20+15 = **165 min = 2.75h** (matches `assessments.md`'s own
  stated "2 hours 45 minutes"; `assessments.md` was not revised this attempt either).
- **Grand total: 1,198 + 250 + 165 = 1,613 min = 26.88h.**

**Comparison against 1,800 min (30h) available (3h/week × 10 weeks):** 1,613 ≤ 1,800.
**Fits**, with **187 min = 3.12h (10.4%)** of margin — 187/1,800 = 0.1039. Identical to
attempt 2's figure, which the validator independently re-derived and passed for G1 last
round — this attempt's re-derivation, done from a differently-shaped resource list,
reaches the same number by a different arithmetic path, which is the strongest form of
confirmation available without re-running the validator.

**Did the split introduce a double-count or a dropped minute anywhere? No — checked
explicitly per the instruction to be sceptical of an unchanged-total claim on a
changed-shape list.** The two splits (Module 1's "Learn Pandas" → two exercises;
Module 2's "Intro to Machine Learning" → two exercises) each preserve their combined
parent line's minutes exactly (60→30+30; 120→60+60), and `resources.md`'s own
arithmetic notes for both modules state this explicitly and correctly. The two pure
swaps (Module 7, Module 8) hold their single line's minutes exactly (90→90 in each
case) because the exercise notebook is described as self-contained, not requiring
separate tutorial time on top — a claim this artifact cannot independently verify
against Kaggle's live page content (Kaggle is client-rendered; see
`validation-report.md`'s own Open Questions on this same limitation), but which is at
least internally consistent with how every other Kaggle exercise notebook in this plan
is already budgeted (as a single self-contained duration, not tutorial-plus-exercise).

**Per-module check against a nominal 3h (180 min) single week** (informative only —
`schedule.md` was not an input to this artifact; see Open Questions), unchanged from
attempt 2 since no module total moved:
- Module 2: 185 min — 5 min over a nominal 3h week, 13 min under gate G1's own
  110%-tolerance ceiling of 198 min.
- Module 3: 191 min — 11 min over a nominal 3h week, 7 min under the 198-min ceiling.
- Module 7: 185 min — 5 min over a nominal 3h week, 13 min under 198 min.
- Module 9: 310 min — expected to span roughly 1.7 weeks (310 ÷ 180), a scheduling
  matter, not a budget failure.
- All other modules (1, 4, 5, 6, 8) fit inside a 3h week individually with room to
  spare.
- None of the per-module totals exceed 198 min, so on this artifact's numbers alone no
  module mechanically forces a Week reshuffle. Confirming this against the actual week
  packing remains `schedule-planner`'s job on its own cascade re-run.

**Practice/resource skill-overlap — re-checked as instructed, now sharpened for both
Module 1 and Module 2, not resolved and not newly created.** The underlying overlap is
not new: attempt 1 already flagged Module 2's bespoke split/fit/score exercises against
Kaggle's course-level credit for the same skill, and attempt 2 flagged the same pattern
newly appearing in Module 1. What changed this attempt is that the G8 fix replaced each
whole-course citation with per-lesson exercise citations, which means the overlap can
now be pinned to one specific exercise per module instead of a whole course:
- **Module 1.** `exercises.md`'s drill ("hand vs. pandas": hand-compute mean/variance/
  std on 10 rows, verify with `.mean()`/`.var()`/`.std()`) and application ("profile a
  whole dataset": mean/std/min/max for every numeric column) now overlap specifically
  with **Exercise: Summary Functions and Maps** (lesson 3: "independently compute
  `.describe()`, `.mean()`, `.std()`, and related summary functions"). The other two
  new Module 1 resources — Exercise: Creating, Reading and Writing (building/loading
  DataFrames) and Exercise: Indexing, Selecting & Assigning (`loc`/`iloc`/boolean
  masks) — teach and grade a *different* skill (constructing and selecting data, not
  summarizing it) and do not overlap with either bespoke Module 1 exercise. Net new
  overlap from this attempt's split: **none** — the overlap is exactly as wide as it
  was in attempt 2, just now attributable to a named exercise rather than a vaguely-
  described tutorial page.
- **Module 2.** `exercises.md`'s drill ("split instability": `train_test_split` three
  times with different `random_state`, record scores) and application ("first
  end-to-end model, honestly reported": split, fit, report test score, split
  proportions, random state, trust judgment) now overlap specifically with **Exercise:
  Model Validation** (lesson 4: "performs a `train_test_split` and computes mean
  absolute error on held-out data"), not with Exercise: Your First Machine Learning
  Model (lesson 3, which only fits and predicts — no split, no held-out evaluation).
  Same conclusion: the overlap is exactly as wide as attempt 2's (where it was
  attributed to "Intro to Machine Learning" generically), now precisely located.
- **Net effect on this budget: still unchanged in direction, and unchanged in
  magnitude.** No minutes move. As before, this is not a literal duplicate task
  (different datasets — the learner's own choice vs. Kaggle's paired dataset — and
  different framing), so nothing is subtracted from the additive total above. If a
  learner judges the overlap close enough to skip some bespoke practice once they see
  it named this precisely, the real time need in Modules 1 and 2 is *lower* than
  26.88h, not higher — the same conservative (safe) direction used throughout.
  `resources.md`'s own Open Questions this attempt make the same recommendation
  (redirect `exercise-designer`'s Module 1/2/8 exercises toward synthesis), now with
  the specific exercise named rather than the whole course.

### Hidden costs

Nothing here is monetary (the whole plan is $0). Carried forward from attempt 2
unchanged except where the resource-count denominator changed:

- **Kaggle competition-submission phone verification — resolved, unchanged.**
  `resources.md` cites a live-verified Kaggle product announcement confirming phone
  verification applies to accounts earning progression points, medals, or prizes, and
  to publishing public Models — not to submitting predictions to a "Getting Started"
  competition like Titanic (Module 3) or House Prices (Module 5). No phone number is
  required anywhere in this plan.
- **Free Kaggle account required starting in Module 1 — unchanged.** The 6-minute
  signup cost is already counted inside Module 1's resource-hours arithmetic above.
  Now first exercised across three lessons instead of one tutorial-plus-one-exercise,
  which does not change the signup cost, only how many graded checkpoints sit behind it.
- **Kaggle notebook session limits — unchanged.** Kaggle's browser notebooks have a
  maximum session runtime and an idle timeout. The capstone (Module 9, 5.17h of build
  time) is very likely to span more than one sitting; a learner who doesn't save/commit
  their notebook mid-session risks losing unsaved work. Not costed, since it doesn't add
  hours if the learner saves regularly, but worth a one-line warning. This attempt adds
  a second reason to flag it: the capstone is now the module with the *most* Kaggle-
  session dependency in the plan relative to modules with fewer, shorter Kaggle
  exercise notebooks, since Modules 1, 2, 7, and 8 each now run their graded work as
  several short, separately-committed notebook sessions rather than one longer one —
  a lower per-session risk profile than the capstone's single unbroken 5-hour block.
- **Binder / JupyterLite cold starts — same two resources, now two of 19 rather than
  two of 17.** Module 4's confusion-matrix example and Module 6's cross-validated-
  predictions example still launch via Binder/JupyterLite; no other resource in the
  plan does, including all four resources swapped or split this attempt (all four are
  Kaggle-hosted, not Binder-hosted). Binder is known for multi-minute cold starts and
  occasional build failures under load; the ~0.5–1h estimates for those two examples
  don't include this startup time.
- **Capstone dataset scale asymmetry — unchanged.** Adult (48,842 rows) is ~10× the
  size of Wine Quality (4,898 rows). Both train in seconds on any modern machine or in
  a Kaggle/Colab session, so this is not a training-time problem, but a learner in a
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
and no coverage to lose, unchanged from attempts 1 and 2. All 19 resources (including
all four resources swapped or split this attempt for the G8 fix) are free by
construction, verified individually above, so there is nothing to recompute.

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
  (same scope as attempts 1 and 2). None of these modules' totals exceed the 198-min
  (3.30h) per-week ceiling individually, so on this artifact's numbers alone no
  reshuffle is mechanically forced — but `schedule-planner`'s own cascade re-run is
  what confirms the 187-min (3.12h) overall margin is actually reachable week by week.
- **Practice/resource skill overlap in Modules 1 and 2 is now precisely located (see
  Findings → Time) but still not resolved to a specific number of overlapping
  minutes.** The assumption used is that all designed practice time is genuinely
  additive — the conservative direction for a budget check, since any overlap would
  only create slack, not a shortfall. `resources.md`'s own Open Questions this attempt
  suggest `exercise-designer` redirect Module 1, 2, and 8's bespoke exercises toward
  synthesis rather than re-deriving what Kaggle already grades; that is a design
  decision for the coordinator to route, not something this artifact can resolve on its
  own. The equivalent overlap flagged for Modules 3, 5, and 7 (a graded Kaggle
  leaderboard or exercise alongside bespoke practice on the same model) was already
  judged in attempt 2 to be a different-enough pairing (leaderboard score vs. hand-
  computed diagnostic) not to warrant the same "same skill, same checkpoint" framing
  applied to Modules 1 and 2 here, and nothing this attempt changes that judgment.
- **Capstone dataset "messiness" is unpredictable**, carried forward from attempts 1
  and 2 and from `curriculum.md`'s own Open Questions: if the learner's self-chosen or
  provided capstone dataset requires nonstandard cleanup, the 5.17h allocated to
  Module 9 may run short. Not something additional budget can absorb given the 10.4%
  slack is a plan-wide margin, not a per-module reserve.
- **Whether a Kaggle exercise notebook genuinely requires zero separate tutorial time
  on top of its own duration** (the assumption `resources.md` uses to hold Module 7 and
  8's minutes unchanged after their URL swaps) could not be independently confirmed
  from this artifact's own inputs — `resources.md` and `validation-report.md` both note
  Kaggle's pages are client-rendered, limiting live verification to titles, not full
  lesson content. Assumed true here because it is consistent with how every other
  Kaggle exercise notebook in this plan is already budgeted, and because the two
  Modules affected (7, 8) still land comfortably under the 198-min weekly ceiling even
  if that assumption is optimistic by a few minutes.
