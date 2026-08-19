---
artifact: validation-report
owner: validator
run_id: run-002-machine-learning
status: final
attempt: 2
inputs:
  - artifacts/requirements.md
  - artifacts/baseline-assessment.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
  - artifacts/schedule.md
  - artifacts/effort-budget.md
generated: 2026-08-19T12:00:00Z
---

# Validation Report — Machine Learning (classical, project-based)

## Summary

**1 GATE(S) FAILED.** G1 is now genuinely fixed (re-derived from scratch, not
trusted from agreement between `resources.md`, `schedule.md`, and
`effort-budget.md`): every module subtotal in `resources.md` attempt 2 is now an
explicit sum of its own resource lines, the weekly totals in `schedule.md` inherit
those correctly, and the heaviest week (Week 3) lands at 191 min against the 198 min
ceiling. G2, G3, G4, G5, G6, G7, and G9 all pass on independently re-derived
numbers. **G8 still fails**, on a different resource than last time: `resources.md`
attempt 2 counts "Learn Pandas" (Module 1) as interactive/project-based, but the
artifact's own "what the learner does" text describes its cited portion as "guided —
... follow worked examples" and explicitly labels it a "guided read-along," not the
"independent auto-graded application" it pairs it with — the exact passive-following
pattern that disqualified the two resources removed in attempt 2. Recounting with
"Learn Pandas" moved to reference gives **11/17 = 64.7%** interactive/project-based,
5.3 points under the 70% floor, not the claimed 70.6%.

**Steps to re-run: `curator` only** (fixes G8's root cause; `schedule-planner` and
`effort-budget-aggregator` will need to re-run again via the automatic staleness
cascade once `resources.md` changes, purely to re-confirm their totals still tie out
— neither is expected to need a substantive rebalance since G8 is a classification
question, not a time-budget one, but the cascade will re-run them regardless).

## Findings

### G1 — Weekly hour ceiling (≤ 3.30h, +10% of 3h = 198 min)

**PASS**

Re-derived independently from `resources.md`'s own itemized resource lines (not
copied from any subtotal), `exercises.md`'s practice-load table, and
`assessments.md`'s per-checkpoint times:

| Module/week block | Resource (min) | Practice (min) | Checkpoint (min) | Week total (min) | ≤198? |
|---|---|---|---|---|---|
| 1 | 60+20+6=86 | 10+15=25 | 15 | **126** | Yes |
| 2 | 120+20=140 | 10+20=30 | 15 | **185** | Yes |
| 3 | 120+20+6=146 | 10+20=30 | 15 | **191** | Yes |
| 4 (+ Review 1) | 30+30=60 | 10+20=30 | 15+20=35 | **125** | Yes |
| 5 | 120+6=126 | 10+20=30 | 15 | **171** | Yes |
| 6 (+ Review 2) | 30+60=90 | 10+20=30 | 15+20=35 | **155** | Yes |
| 7 | 90+30=120 | 15+15+15=45 | 20 | **185** | Yes |
| 8 | 30+90=120 | 10+20=30 | 15 | **165** | Yes |
| 9 (wk 9, capstone pt.1) | — | — | — | **180** | Yes |
| 10 (wk 10, capstone pt.2) | — | — | — | **130** | Yes |

Module 9's two-week split (180 + 130 = 310 min) matches `resources.md`'s own
310-min (5.17h) capstone total exactly, even though `schedule.md` breaks that time
into "build / diagnose / write-up" labels rather than the "300 build + 10 setup"
labels `resources.md` uses — the totals reconcile.

Resource-hours grand total, checked by direct addition of every module's own line:
86+140+146+60+126+90+120+120+310 = **1,198 min = 19.97h** (matches `resources.md`'s
stated 19.97h). Exercises: 25+30+30+30+30+30+45+30 = **250 min** (Module 9's 10 min
excluded — both `exercises.md` and its consumers explicitly treat it as embedded in
the capstone's own 5h, not additive; confirmed, not merely trusted). Assessments:
15×7 + 20 + 20×2 = **165 min**. Grand total: 1,198+250+165 = **1,613 min = 26.88h**
against 1,800 min (30h) capacity — **187 min = 3.12h = 10.4% slack**, genuine
margin, thinner than the 15% guideline but not manufactured.

Heaviest week: **Week 3 at 191 min**, 7 min under the 198 min ceiling (96.5% of
ceiling, 106.1% of the 180-min per-week target) — the exact week that breached the
ceiling at 201 min in attempt 1. The fix traces correctly to `resources.md`: Module
3's true resource-line sum is 146 min (120+20+6), not attempt 1's undercounted 126
min or the validator's own attempt-1 correction of 156 min (which assumed the
Logistic Regression read stayed at its original, more generous estimate — `curator`
instead trimmed that read's own duration in this revision, a legitimate, disclosed
choice, not a second undercount).

### G2 — Deadline (≤ `horizon_weeks` = 10)

**PASS** — `schedule.md` uses exactly 10 weeks; all 9 modules from `curriculum.md`
appear (Module 9 spans Weeks 9–10 as one deliberate contiguous capstone block). 10 ≤
10, zero weeks of margin, as `schedule.md` itself states.

### G3 — Cost (≤ `requirements.budget` = 0, free-only, hard constraint — NOT skipped)

**PASS** — All 17 resources in `resources.md`/`effort-budget.md`'s money table are
$0, independently re-summed: 17 rows × $0 = $0 ≤ $0. The Kaggle phone-verification
question flagged unresolved in attempt 1 is now closed (websearch-verified this run:
phone verification gates progression points/medals/public Models, not "Getting
Started" competition submissions) — no hidden fee anywhere sampled. Titles for the
Titanic and House Prices competition pages resolved live via WebFetch this run and
match their citations (see Link sample); Kaggle's client-rendered pages did not
return fee/status detail beyond the title, so this is a liveness check, not an
independent fee re-derivation — noted in Open Questions.

### G4 — Prerequisite ordering

**PASS** — Unchanged from attempt 1 (`curriculum.md` was not re-run): all 9 modules'
`Prerequisites` reference only earlier module numbers (2→1, 3→2, 4→3, 5→2, 6→5,
7→{4,6}, 8→7, 9→{1–8}). Module 1's assumed baseline ("programming fundamentals only")
matches exactly what `baseline-assessment.md` marks **Known**; every gap it marks
**Absent** is taught, not assumed, starting in Module 1.

### G5 — Outcome coverage and per-module completeness

**PASS** (full clause applies — `assessment-designer` ran). All 6 target outcomes
map to ≥1 module. Every module 1–9 has ≥1 resource (`resources.md`: counts are
2,2,2,2,1,2,2,2,2 — Module 5 now has exactly 1 after the OLS/Ridge removal, still
≥1), ≥1 exercise (`exercises.md`: 2,2,2,2,2,2,3,2,1 — Module 9's capstone self-audit
checklist counts as 1), and ≥1 assessment (`assessments.md`: one checkpoint per
module 1–8, Module 9's assessment is explicitly the Final check).

### G6 — No duplicate resource URLs

**PASS** — All 17 URLs in `resources.md` attempt 2 are distinct, checked
individually. The Module 8 pair is a genuine G6 concern given last attempt's swap,
and it holds up: `.../code/alexisbcook/pipelines` (Pipelines lesson) and
`.../code/alexisbcook/exercise-categorical-variables` (the new Categorical Variables
exercise) are different URL paths; live WebFetch confirms different page titles
("Pipelines | Kaggle" vs. "Exercise: Categorical Variables | Kaggle" — see Link
sample), confirming two distinct lessons, not a relabeled duplicate. The
`#classification-metrics` / `#regression-metrics` anchor pair (Modules 4 and 6) is
the same sanctioned same-page/different-anchor exception noted in attempt 1.

### G7 — Citation verification

**PASS** — All 17 resource lines in `resources.md` carry a `verified:` method and a
this-run date (`2026-08-18` or `2026-08-19` — both within this run per the date
note). Sampled 10 of 17 resource URLs via live WebFetch this round (well above the
3-URL minimum): all 10 resolved with titles matching their citations (see Link
sample). One limitation: Kaggle's pages are client-rendered, so WebFetch returned
page titles but not full body content for the six Kaggle URLs sampled — sufficient
to confirm reachability and title match (the G7 bar), insufficient to independently
re-derive lesson-level structure claims from the fetched text alone (see Open
Questions and the G8 finding below, which relies on `resources.md`'s own written
description rather than fetched Kaggle page content for that reason).

### G8 — Modality match (≥70% match `preferred_modality` = project)

**FAIL**

`resources.md` claims 12/17 (70.6%) interactive/project-based, naming exactly 5
reference resources (Getting Started, Logistic Regression, both
`model_evaluation.html` metrics sections, the cross-validation strategy guide).
Applying the instructed standard — "interactive means the learner does work and gets
feedback on THEIR work" — to every one of the 17 lines' own "what the learner does"
text surfaces a sixth resource that the artifact's own words describe as passive:

| Resource | Module | `resources.md`'s own description | Honest classification |
|---|---|---|---|
| Learn Pandas | 1 | "the first two lessons are **guided** — load a CSV, inspect shape/dtypes/columns, **follow worked examples**." Ramp is explicitly stated as "**guided read-along** → independent auto-graded application" — the artifact's own words place this resource *before*, and distinct from, the independent/graded step. | **Reference/passive — misclassified** |

This is the identical disqualifying pattern already applied by `curator` itself to
justify removing the Module 5 OLS/Ridge example ("demonstrates... a second, simpler
dataset... no learner data, not modified") and the Module 7 underfitting example
("runs the... example to see..."): worked/guided material the learner follows but
does not independently apply or get graded on. By contrast, every resource this
recount left classified interactive has explicit graded or own-data language in its
own description (e.g. "Kaggle's exercise auto-grades," "with their own trained model
and data swapped in," "swapped to their own regressor," "linked graded exercise").
Learn Pandas has neither — its own graded, independent component was correctly
identified and cited *separately* as "Exercise: Summary Functions and Maps," which
remains correctly classified interactive.

Live WebFetch this round independently confirmed the *type* of two resources central
to this recount: the Confusion Matrix example (Module 4) is a self-contained runnable
notebook built around the iris dataset with a simple `.from_estimator(classifier,
X_test, y_test, ...)` call — trivially substitutable with the learner's own Module 3
classifier and data as `resources.md` describes, supporting that resource's
interactive classification (unlike Learn Pandas, no equivalent live check was needed
for the Learn Pandas finding since it rests on the artifact's own stated description,
not a claim about the live page).

Reclassifying Learn Pandas consistently with the standard applied to the two already
-removed resources: **reference = 6, interactive = 11, total = 17 → 11/17 = 64.7%** —
5.3 points under the 70% floor, not the claimed 70.6%.

**owner: curator**

**fix:** With reference at 6, gate G8's floor requires interactive ≥ 0.7(interactive
+ 6), i.e. interactive ≥ 14 — a net gain of at least 3 more genuinely interactive
resources is needed if Learn Pandas is correctly moved to reference and nothing else
changes. Two more targeted options: (a) replace the Learn Pandas *tutorial* citation
for Module 1 with citations to that course's own auto-graded exercise pages for
lessons 1 and 2 ("Exercise: Creating, Reading and Writing" and "Exercise: Indexing,
Selecting & Assigning" both exist on Kaggle Learn per the course's standard
tutorial-then-exercise structure) — this earns the interactive classification
honestly for the same minutes already budgeted, without adding a new reference line;
or (b) keep Learn Pandas as reference (an honest description of what it is) and
source 2–3 more genuinely graded/own-data resources across the modules currently
thinnest on interactive coverage (Module 2's "Getting Started" and Module 3's
"Logistic Regression" reference pages are candidates for the same tutorial-to
-exercise substitution as (a), since scikit-learn's own docs have no graded
component but Kaggle's parallel material might). Re-verify the arithmetic
(interactive ÷ total ≥ 0.70) explicitly against the final resource list before
resubmitting, the same way this report just did.

### G9 — Level fit (no module more than one level above the assessed baseline)

**PASS**, under the progressive (module-to-module) reading — see Open Questions for
why the literal one-baseline reading cannot be the intended check. `curriculum.md`'s
progression L0→L1→L1→L2→L2→L2→L3→L3→L3 (unchanged from attempt 1, `curriculum.md` was
not re-run) never increases by more than one level from the immediately preceding
module.

### Structural checks

| Artifact | Frontmatter ok (7 keys) | Sections ok (4, in order, non-empty) | Citations ok |
|---|---|---|---|
| requirements.md | Yes | Yes | Sources: "None." — no external data consumed; see Open Questions (skill-exemption-list gap, carried from attempt 1) |
| baseline-assessment.md | Yes | Yes | Yes — 6 Wikipedia citations, `verified: mcp:wikipedia 2026-08-18` |
| curriculum.md | Yes | Yes | Yes — 10 Wikipedia citations, `verified: mcp:wikipedia 2026-08-18` |
| resources.md (attempt 2) | Yes | Yes | Structurally yes — all 17 lines carry `verified:` + this-run date; see G8 for the data-accuracy (not structural) finding |
| exercises.md (attempt 1, unchanged) | Yes | Yes | Yes — Sources: "None.", exempted |
| assessments.md (attempt 1, unchanged) | Yes | Yes | Yes — Sources: "None.", exempted |
| schedule.md (attempt 2) | Yes | Yes | Yes — Sources: "None.", exempted |
| effort-budget.md (attempt 2) | Yes | Yes | Yes — Sources: "None." with an explanation, exempted |

`owner` fields all match `pipeline.json`. All `inputs` paths exist in this run
(`resources.md` and `schedule.md` list `artifacts/validation-report.md` among their
inputs — this file existed at the path when they read it, from attempt 1). No
`output/` files exist yet, so the internal-machinery-leak check does not yet apply.

### Link sample

| URL | Method | Result |
|---|---|---|
| https://www.kaggle.com/learn/pandas | WebFetch | Resolved — "Learn Pandas Tutorials \| Kaggle," matches citation; body content not retrievable (client-rendered), title only |
| https://www.kaggle.com/code/residentmario/exercise-summary-functions-and-maps | WebFetch | Resolved — "Exercise: Summary Functions and Maps \| Kaggle," title confirms "Exercise" (graded) type, matches citation |
| https://www.kaggle.com/learn/intro-to-machine-learning | WebFetch | Resolved — "Learn Intro to Machine Learning Tutorials \| Kaggle," matches citation |
| https://www.kaggle.com/code/alexisbcook/pipelines | WebFetch | Resolved — "Pipelines \| Kaggle," matches citation |
| https://www.kaggle.com/code/alexisbcook/exercise-categorical-variables | WebFetch | Resolved — "Exercise: Categorical Variables \| Kaggle," title confirms "Exercise" type and confirms this is a distinct page/title from "Pipelines" (G6) |
| https://www.kaggle.com/c/titanic | WebFetch | Resolved — "Titanic - Machine Learning from Disaster \| Kaggle," matches citation; live status/fee detail not retrievable beyond title (client-rendered) |
| https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques | WebFetch | Resolved — "House Prices - Advanced Regression Techniques \| Kaggle," matches citation |
| https://www.kaggle.com/code/alexisbcook/cross-validation | WebFetch | Resolved — "Cross-Validation \| Kaggle," matches citation |
| https://archive.ics.uci.edu/dataset/186/wine+quality | WebFetch | Resolved — UCI Wine Quality, 4,898 instances / 11 features, CC BY 4.0, free CSV — matches citation exactly |
| https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html | WebFetch | Resolved — confusion-matrix example built on the built-in iris dataset via `ConfusionMatrixDisplay.from_estimator(classifier, X_test, y_test, ...)`; confirms the page is a substitutable template, supporting (not contradicting) `resources.md`'s "adapted to the learner's own model" claim |

## Sources

- [Learn Pandas Tutorials](https://www.kaggle.com/learn/pandas) — Kaggle · verified: webfetch 2026-08-19
- [Exercise: Summary Functions and Maps](https://www.kaggle.com/code/residentmario/exercise-summary-functions-and-maps) — Kaggle · verified: webfetch 2026-08-19
- [Learn Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) — Kaggle · verified: webfetch 2026-08-19
- [Pipelines](https://www.kaggle.com/code/alexisbcook/pipelines) — Kaggle · verified: webfetch 2026-08-19
- [Exercise: Categorical Variables](https://www.kaggle.com/code/alexisbcook/exercise-categorical-variables) — Kaggle · verified: webfetch 2026-08-19
- [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic) — Kaggle · verified: webfetch 2026-08-19
- [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) — Kaggle · verified: webfetch 2026-08-19
- [Cross-Validation](https://www.kaggle.com/code/alexisbcook/cross-validation) — Kaggle · verified: webfetch 2026-08-19
- [Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality) — UCI Machine Learning Repository · verified: webfetch 2026-08-19
- [scikit-learn: Confusion Matrix example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html) — scikit-learn · verified: webfetch 2026-08-19

## Open Questions

- **G9's exact scope remains ambiguous as worded**, carried from attempt 1 ("no
  module more than one level above the assessed baseline" vs. "...above the
  preceding module"). Applied the progressive reading again since the literal
  one-baseline reading fails any multi-level curriculum by construction.
- **Kaggle's client-side rendering limited WebFetch to page titles for all 8 Kaggle
  URLs sampled this round.** This is sufficient to confirm reachability and
  title-match for G7, and sufficient to distinguish the Pipelines vs. Categorical
  Variables URLs for G6, but it means the G8 finding above rests on `resources.md`'s
  own written description of what the learner does, cross-checked for internal
  consistency (the "guided" language applied to Learn Pandas vs. the "graded"/"own
  data" language applied to the resources left classified interactive), not on
  independently fetched Kaggle lesson content. If the coordinator has a way to
  browser-render Kaggle pages, re-confirming the actual lesson 1/2 exercise
  structure directly would strengthen this finding further.
- **`requirements.md`'s "Sources: None." is still not covered by the
  artifact-validator skill's explicit exemption list**, carried from attempt 1 — not
  scored as a structural failure, flagged again for the skill's owner.
- **The possible double-count between Kaggle's own auto-graded exercises and
  `exercises.md`'s bespoke practice (Modules 1, 2, 3, 5, 7, 8, up to 165 min /
  2.75h if fully overlapping)** remains unresolved, now flagged by three artifacts
  independently (`resources.md`, `exercises.md` via inheritance, `effort-budget.md`).
  It does not change any gate verdict above — resolving it in the "overlap"
  direction only creates more slack, never a shortfall — but the coordinator may
  want `exercise-designer` to weigh in once `curator` re-runs for G8, since the
  G8 fix (adding or reclassifying Module 1/2/3 resources) will directly touch the
  modules this question is about.
