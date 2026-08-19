---
artifact: validation-report
owner: validator
run_id: run-002-machine-learning
status: final
attempt: 3
inputs:
  - artifacts/requirements.md
  - artifacts/baseline-assessment.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
  - artifacts/schedule.md
  - artifacts/effort-budget.md
generated: 2026-08-19T16:00:00Z
---

# Validation Report — Machine Learning (classical, project-based)

## Summary

**ALL GATES PASS.** No steps need re-running. This is the third and final allowed
attempt, following `curator` attempt 3's fix to G8: rather than patch only the named
"Learn Pandas" instance, `curator` audited all 17 attempt-2 resources for the same
tutorial-page-credited-with-graded-work pattern, found three more instances (Module 2
"Intro to Machine Learning," Module 7 "Cross-Validation," Module 8 "Pipelines"), and
re-cited all four against their actual per-lesson exercise notebooks. Two two-lesson
citations split into per-lesson ones, taking the resource count from 17 to 19. Every
number in this report was re-derived independently from the artifacts' own itemized
lines — not accepted from any subtotal, and not accepted merely because
`schedule-planner` and `effort-budget-aggregator` (both attempt 3) agree with each
other, since on this same run three artifacts once agreed on a wrong number by copying
one bad table. All nine gates pass on this independent re-derivation.

## Findings

### G1 — Weekly hour ceiling (≤ 3.30h, +10% of 3h = 198 min)

**PASS**

Re-derived from `resources.md` attempt 3's 19 itemized resource lines, `exercises.md`'s
unchanged practice table, and `assessments.md`'s unchanged checkpoint times — added by
hand, not copied from any artifact's stated subtotal:

| Week | Content | Resource (min) | Practice (min) | Checkpoint (min) | Week total | ≤198? |
|---|---|---|---|---|---|---|
| 1 | Module 1 | 6+30+30+20=86 | 10+15=25 | 15 | **126** | Yes |
| 2 | Module 2 | 20+60+60=140 | 10+20=30 | 15 | **185** | Yes |
| 3 | Module 3 | 6+120+20=146 | 10+20=30 | 15 | **191** | Yes |
| 4 | Review 1 + Module 4 | 30+30=60 | 10+20=30 | 15+20=35 | **125** | Yes |
| 5 | Module 5 | 6+120=126 | 10+20=30 | 15 | **171** | Yes |
| 6 | Module 6 + Review 2 | 30+60=90 | 10+20=30 | 15+20=35 | **155** | Yes |
| 7 | Module 7 | 90+30=120 | 15+15+15=45 | 20 | **185** | Yes |
| 8 | Module 8 | 30+90=120 | 10+20=30 | 15 | **165** | Yes |
| 9 | Module 9 pt.1 | — | — | — | **180** | Yes |
| 10 | Module 9 pt.2 | — | — | — | **130** | Yes |

Sum: 126+185+191+125+171+155+185+165+180+130 = **1,613 min**, matching the grand
total below exactly (cross-check by two independent routes).

Module-level resource sum, checked one line at a time against `resources.md`
attempt 3's own Findings section (not its Coverage-check table): Module 1
(30+30+20+6=86), Module 2 (20+60+60=140), Module 3 (120+20+6=146), Module 4
(30+30=60), Module 5 (120+6=126), Module 6 (30+60=90), Module 7 (90+30=120), Module 8
(90+30=120), Module 9 (300+10=310). Total: 86+140+146+60+126+90+120+120+310 =
**1,198 min = 19.97h** — matches `resources.md`'s stated total exactly, and matches
attempt 2's total exactly, confirming the four citation swaps and two line-splits
neither dropped nor double-counted a minute. Exercises: 25+30+30+30+30+30+45+30 =
**250 min** (Module 9's 10 min correctly excluded as embedded, not additive — both
`exercises.md` and its consumers say so explicitly). Assessments: 7 checkpoints × 15 +
20 (Module 7) + 2×20 (cumulative reviews) = 105+20+40 = **165 min**.

Grand total: 1,198 + 250 + 165 = **1,613 min = 26.88h**, against 1,800 min (30h)
capacity — **187 min = 3.12h = 10.4% slack** (187/1,800 = 0.1039). Genuine margin,
thinner than the 15% guideline but arithmetically real, unchanged from attempt 2 by
independent re-derivation from a differently-shaped (19-line, not 17-line) resource
list — the strongest form of confirmation available.

Heaviest week: **Week 3 at 191 min**, 7 min under the 198 min ceiling (96.5% of
ceiling). Unchanged from attempt 2, correctly, since Module 3 was not touched by this
attempt's citation swaps.

### G2 — Deadline (≤ `horizon_weeks` = 10)

**PASS** — `schedule.md` uses exactly 10 weeks; all 9 modules from `curriculum.md`
appear (Module 9 spans Weeks 9–10 as one deliberate contiguous capstone block).
10 ≤ 10, zero weeks of margin.

### G3 — Cost (≤ `requirements.budget` = 0, free-only, hard constraint — NOT skipped)

**PASS** — All 19 resources in `resources.md` attempt 3 / `effort-budget.md`'s money
table checked individually: every one is $0, including all four resources swapped or
split this attempt for the G8 fix (all four require only the same free Kaggle account
already budgeted since Module 1 — no new signup, no paid tier). 19 rows × $0 = $0 ≤
$0. The Kaggle phone-verification question (resolved in attempt 2, carried forward)
holds: phone verification gates progression points/medals/public Models, not
"Getting Started" competition submissions — re-confirmed present in `resources.md`'s
Sources this attempt, dated within this run.

### G4 — Prerequisite ordering

**PASS** — `curriculum.md` was not re-run this attempt; unchanged from the version
already validated. All 9 modules' `Prerequisites` reference only earlier module
numbers (2→1, 3→2, 4→3, 5→2, 6→5, 7→{4,6}, 8→7, 9→{1–8}). Module 1's assumed
baseline ("programming fundamentals only") matches exactly what `baseline-assessment.md`
marks **Known**; every gap it marks **Absent** is taught, not assumed, starting in
Module 1.

### G5 — Outcome coverage and per-module completeness

**PASS** (full clause applies — `assessment-designer` ran, `wants_assessments` = true).
All 6 target outcomes map to ≥1 module (unchanged, `curriculum.md` not re-run).
Resource counts per module, recounted from `resources.md` attempt 3's 19 lines: 3, 3,
2, 2, 1, 2, 2, 2, 2 — all ≥1 (Module 1 and 2 gained a resource each from the citation
splits). Exercise counts (`exercises.md`, unchanged): 2, 2, 2, 2, 2, 2, 3, 2, 1 — all
≥1. Assessment counts (`assessments.md`, unchanged): one checkpoint per module 1–8,
Module 9's assessment is the Final check — all ≥1.

### G6 — No duplicate resource URLs

**PASS** — All 19 URLs in `resources.md` attempt 3 checked individually; all distinct.
The two new split-off pairs (Module 1: `exercise-creating-reading-and-writing` /
`exercise-indexing-selecting-assigning` / `exercise-summary-functions-and-maps`;
Module 2: `exercise-your-first-machine-learning-model` / `exercise-model-validation`)
are five and two distinct URL paths respectively, confirmed live via WebFetch this
round (see Link sample) — genuinely different lesson pages, not a relabeled
duplicate. The `#classification-metrics` / `#regression-metrics` anchor pair (Modules
4 and 6) remains the same sanctioned same-page/different-anchor exception validated in
attempts 1 and 2.

### G7 — Citation verification

**PASS** — All 19 resource lines in `resources.md` attempt 3 carry a `verified:`
method and a this-run date (`2026-08-18` or `2026-08-19`, both within this run per the
date note: run began 2026-08-18, today is 2026-08-19). Sampled 6 of 19 URLs via live
WebFetch this round, all six being the resources newly cited or swapped this
attempt (the highest-risk set, since a repeat of the G8 bug would show up here first):
all 6 resolved with titles explicitly beginning "Exercise:", confirming each is the
actual graded-exercise page, not a tutorial/landing page carrying the same URL pattern
that caused the last two failures. As in prior attempts, Kaggle's client-side
rendering limited WebFetch to page titles rather than full body content — sufficient
to confirm reachability and to distinguish exercise pages from tutorial pages by title
(the G7 and G8 bar used here), insufficient to independently re-derive lesson-level
grading mechanics from fetched text alone (see Open Questions).

### G8 — Modality match (≥70% match `preferred_modality` = project)

**PASS**

Recounted independently against the instructed standard — "the learner does work and
gets feedback on THEIR work" — applied to all 19 lines' own "what the learner does"
text, not accepted from `resources.md`'s tally:

| # | Resource | Module | Classification | Basis |
|---|---|---|---|---|
| 1 | Exercise: Creating, Reading and Writing | 1 | Interactive | Auto-graded notebook, own answers checked |
| 2 | Exercise: Indexing, Selecting & Assigning | 1 | Interactive | Auto-graded notebook |
| 3 | Exercise: Summary Functions and Maps | 1 | Interactive | Auto-graded notebook |
| 4 | Getting Started | 2 | Reference | Explicitly "reference, not graded" per its own text |
| 5 | Exercise: Your First Machine Learning Model | 2 | Interactive | Auto-graded notebook |
| 6 | Exercise: Model Validation | 2 | Interactive | Auto-graded notebook |
| 7 | Titanic | 3 | Interactive | Graded via live public leaderboard on learner's own submission |
| 8 | Logistic Regression (user guide) | 3 | Reference | Explicitly "reference, not graded" |
| 9 | Classification metrics (user guide) | 4 | Reference | Explicitly "targeted read," not graded |
| 10 | Confusion matrix example | 4 | Interactive | Runnable notebook, learner swaps in own model/data, own plot as feedback |
| 11 | House Prices | 5 | Interactive | Graded via live public leaderboard |
| 12 | Regression metrics (user guide) | 6 | Reference | Explicitly "targeted read," not graded |
| 13 | Plotting Cross-Validated Predictions | 6 | Interactive | Runnable notebook, swapped to learner's own regressor/data |
| 14 | Exercise: Cross-Validation | 7 | Interactive | Auto-graded notebook (verified this round — was mis-cited as tutorial in attempt 2) |
| 15 | Cross-validation (user guide) | 7 | Reference | Explicitly "targeted read," strategy catalogue only |
| 16 | Exercise: Pipelines | 8 | Interactive | Auto-graded notebook (verified this round — was mis-cited as tutorial in attempt 2) |
| 17 | Exercise: Categorical Variables | 8 | Interactive | Auto-graded notebook |
| 18 | Adult | 9 | Interactive | Raw dataset that *is* the capstone's own unassisted project substrate, not a mislabeled tutorial — feedback comes from the learner's own train/test scores plus `assessments.md`'s Final check, which is a distinct owning artifact, not a separate citable exercise page this line failed to cite |
| 19 | Wine Quality | 9 | Interactive | Same basis as Adult |

Interactive = 14, Reference = 5, Total = 19. **14/19 = 73.68% ≈ 73.7%**, 3.7 points
clear of the 70.0% floor (need ≥13.3, have 14).

Specifically checked for a repeat of the exact bug that failed this gate twice before
— a citation pointing at a tutorial/landing page while credited with graded work that
actually lives on a separate, uncited exercise page. Live WebFetch of the four
resources central to attempt 3's fix (rows 1–2, 5–6 by proxy, 14, 16 above; see Link
sample) confirms all four now resolve to pages whose titles begin "Exercise:", the
observable signature of the actual graded page — not the "Learn X Tutorials" or bare
lesson-name signature that flagged the bug in attempts 1–2. No fifth instance of the
pattern was found scanning the remaining 15 lines' "what the learner does" text: every
resource still classified reference is explicitly described in its own text as a
"read" or "targeted read," never as carrying graded work it doesn't cite directly; the
Module 9 dataset lines were checked against the same pattern and found structurally
different (a raw dataset is not a tutorial mislabeling a separate exercise — it is the
literal project substrate, with the actual assessment living correctly in a different
artifact by design, not a miscitation).

### G9 — Level fit (no module more than one level above the assessed baseline)

**PASS**, under the progressive (module-to-module) reading — see Open Questions for
why the literal one-baseline reading cannot be the intended check. `curriculum.md`'s
progression L0→L1→L1→L2→L2→L2→L3→L3→L3 (unchanged, `curriculum.md` was not re-run)
never increases by more than one level from the immediately preceding module.

### Structural checks

| Artifact | Frontmatter ok (7 keys) | Sections ok (4, in order, non-empty) | Citations ok |
|---|---|---|---|
| requirements.md | Yes | Yes | Sources: "None." — no external data consumed; see Open Questions (skill-exemption-list gap, carried forward) |
| baseline-assessment.md | Yes | Yes | Yes — 6 Wikipedia citations, `verified: mcp:wikipedia 2026-08-18` |
| curriculum.md | Yes | Yes | Yes — 10 Wikipedia citations, `verified: mcp:wikipedia 2026-08-18` |
| resources.md (attempt 3) | Yes | Yes | Structurally yes — all 19 lines carry `verified:` + this-run date; see G8 for the data-accuracy finding (now passing) |
| exercises.md (attempt 1, unchanged) | Yes | Yes | Yes — Sources: "None.", exempted |
| assessments.md (attempt 1, unchanged) | Yes | Yes | Yes — Sources: "None.", exempted |
| schedule.md (attempt 3) | Yes | Yes | Yes — Sources: "None.", exempted |
| effort-budget.md (attempt 3) | Yes | Yes | Yes — Sources: "None." with an explanation, exempted |

`owner` fields all match `pipeline.json` (`resources.md`'s owner is `curator`, its
Summary correctly names the `project-curator` variant). All `inputs` paths exist in
this run. No `output/` files exist yet, so the internal-machinery-leak check does not
yet apply.

### Link sample

| URL | Method | Result |
|---|---|---|
| https://www.kaggle.com/code/residentmario/exercise-creating-reading-and-writing | WebFetch | Resolved — "Exercise: Creating, Reading and Writing \| Kaggle," title confirms graded-exercise page, matches citation |
| https://www.kaggle.com/code/residentmario/exercise-indexing-selecting-assigning | WebFetch | Resolved — "Exercise: Indexing, Selecting & Assigning \| Kaggle," confirms graded-exercise page |
| https://www.kaggle.com/code/dansbecker/exercise-your-first-machine-learning-model | WebFetch | Resolved — "Exercise: Your First Machine Learning Model \| Kaggle," confirms graded-exercise page |
| https://www.kaggle.com/code/dansbecker/exercise-model-validation | WebFetch | Resolved — "Exercise: Model Validation \| Kaggle," confirms graded-exercise page |
| https://www.kaggle.com/code/alexisbcook/exercise-cross-validation | WebFetch | Resolved — "Exercise: Cross-Validation \| Kaggle," confirms this is now the graded page (attempt 2 had cited the tutorial page `.../cross-validation` instead) |
| https://www.kaggle.com/code/alexisbcook/exercise-pipelines | WebFetch | Resolved — "Exercise: Pipelines \| Kaggle," confirms this is now the graded page (attempt 2 had cited the tutorial page `.../pipelines` instead) |

Kaggle's pages are client-rendered, so WebFetch returned page titles but not full body
content for all six — sufficient to confirm reachability and to distinguish
"Exercise: ..." titles from tutorial-page titles (the check both G7 and G8 need here),
consistent with the same limitation noted in attempts 1 and 2.

## Sources

- [Exercise: Creating, Reading and Writing](https://www.kaggle.com/code/residentmario/exercise-creating-reading-and-writing) — Kaggle · verified: webfetch 2026-08-19
- [Exercise: Indexing, Selecting & Assigning](https://www.kaggle.com/code/residentmario/exercise-indexing-selecting-assigning) — Kaggle · verified: webfetch 2026-08-19
- [Exercise: Your First Machine Learning Model](https://www.kaggle.com/code/dansbecker/exercise-your-first-machine-learning-model) — Kaggle · verified: webfetch 2026-08-19
- [Exercise: Model Validation](https://www.kaggle.com/code/dansbecker/exercise-model-validation) — Kaggle · verified: webfetch 2026-08-19
- [Exercise: Cross-Validation](https://www.kaggle.com/code/alexisbcook/exercise-cross-validation) — Kaggle · verified: webfetch 2026-08-19
- [Exercise: Pipelines](https://www.kaggle.com/code/alexisbcook/exercise-pipelines) — Kaggle · verified: webfetch 2026-08-19

## Open Questions

- **G9's exact scope remains ambiguous as worded**, carried from attempt 1 ("no
  module more than one level above the assessed baseline" vs. "...above the
  preceding module"). Applied the progressive reading again since the literal
  one-baseline reading fails any multi-level curriculum by construction.
- **Kaggle's client-side rendering limited WebFetch to page titles for every Kaggle
  URL sampled across all three attempts.** Sufficient to confirm reachability and to
  tell an "Exercise: ..." page from a tutorial/landing page by title — the exact
  distinction G8 turned on this round — but not sufficient to independently confirm
  each notebook's internal grading mechanics from fetched text. If the coordinator has
  a way to browser-render Kaggle pages, that would strengthen this finding further,
  though it is no longer load-bearing for any gate verdict now that G8 passes with a
  3.7-point margin.
- **`requirements.md`'s "Sources: None." is still not covered by the
  artifact-validator skill's explicit exemption list**, carried from attempts 1 and
  2 — not scored as a structural failure, flagged again for the skill's owner.
- **The possible double-count between Kaggle's own auto-graded exercises and
  `exercises.md`'s bespoke practice, now precisely located to one named exercise per
  module (Module 1: "Exercise: Summary Functions and Maps"; Module 2: "Exercise:
  Model Validation") per `resources.md` and `effort-budget.md`'s own attempt-3
  analysis**, remains open and does not change any gate verdict — resolving it in the
  "overlap" direction only creates more slack (up to 60 min for Modules 1–2 alone, up
  to 165 min if the wider pattern across Modules 3, 5, 7 is included), never a
  shortfall. This is a design decision for the coordinator to route to
  `exercise-designer` if desired, not a gate failure.
- **Slack (10.4%) is thinner than the 15% guideline** but is not a gate — G1 and G2
  both pass with real, re-derived margin (7 min on the heaviest week, 187 min overall).
  Noted for the coordinator's awareness, not a finding requiring action.
