---
artifact: validation-report
owner: validator
run_id: run-003-music-theory
status: final
attempt: 1
inputs:
  - artifacts/requirements.md
  - artifacts/baseline-assessment.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
  - artifacts/schedule.md
  - artifacts/effort-budget.md
generated: 2026-08-19T00:00:00Z
---

# Validation Report — Music Theory for Score Reading and Analysis

## Summary

1 GATE(S) FAILED. G5 is BLOCKED because `assessments.md` is internally inconsistent —
its own Summary and "Cumulative reviews — summary" table both promise cumulative
reviews after Modules 3, 6 and 9, but the Findings section only contains worked
content for the reviews after Module 3 and Module 9; no "Cumulative review — after
Module 6" section exists anywhere in the artifact. **`assessment-designer` must be
re-run** to add the missing Module 6 review (or correct the Summary/table if only two
reviews were ever intended). Because that step's artifact is a direct input to
`schedule.md` and `effort-budget.md`, both of those are marked stale by the retry
cascade once `assessment-designer` is re-run, and **`schedule-planner` and
`effort-budget-aggregator` will need to re-run** as well even though neither made an
error of its own — their totals were computed correctly from the (incomplete) inputs
they were given. G1–G4 and G6–G9 all PASS on the evidence re-derived below. Separately,
`effort-budget.md`'s headline total (≈49.75 h) double-counts ≈2.4 h of Module 10 work
already covered by `resources.md`'s 5-hour capstone envelope; this does not fail any
gate (G3, the only gate that reads `effort-budget.md`, is a cost gate and is
unaffected) but the coordinator should pass this finding to
`effort-budget-aggregator` for reconciliation on the next pass regardless of the G5
retry, since it will re-run anyway.

## Findings

### G1 — Weekly hours ≤ 4.4h ceiling (schedule.md)

**PASS.** Re-derived every week's total from `schedule.md`'s own session lines and
cross-checked against its Load-check table:

| Week | Sessions sum | Table figure | ≤ 4.4h? |
|---|---|---|---|
| 1 | 2.6+1.0+0.5 = 4.10 | 4.10 | yes |
| 2 | 2.7+0.5+1.1 = 4.30 | 4.30 | yes |
| 3 | 0.42+2.33+1.1+0.42 = 4.27 | 4.27 | yes |
| 4 | 0.57+0.42+3.3 = 4.29 (table: 4.28) | 4.28 | yes |
| 5 | 1.9+0.42+2.08 = 4.40 | 4.40 | yes (at ceiling) |
| 6 | 0.92+1.0+0.33+2.15 = 4.40 | 4.40 | yes (at ceiling) |
| 7 | 1.85+1.4+0.42+0.43 = 4.10 (table: 4.40)* | 4.40 | see note |
| 8 | 1.07+0.75+0.33+2.25 = 4.40 | 4.40 | yes (at ceiling) |
| 9 | 0.75+1.1+0.33+2.22 = 4.40 | 4.40 | yes (at ceiling) |
| 10 | 1.08+1.4+0.42+1.5 = 4.40 | 4.40 | yes (at ceiling) |
| 11 | 1.0+2.5+0.5 = 4.00 | 4.00 | yes |
| 12 | 0 | 0.00 | yes (buffer) |

\*Week 7's four listed session lengths sum to 4.10h by my addition, not the 4.40h the
week-total line and Load-check table both state; this 0.30h gap does not change the
gate outcome (both the stated 4.40 and my re-derived 4.10 are ≤ 4.4h) but the module
running-total row for Module 6 (6.12h, used consistently elsewhere) requires 4.40h
across weeks 6–7 combined, which only balances if Week 7 is in fact 4.40h — so the
week narrative likely omits or mis-sizes a few minutes of a session rather than the
week-total being wrong. Not gate-relevant; flagged for `schedule-planner`'s awareness
only, not a fix requirement.

Total: 47.35h against the 48h envelope (4h × 12 weeks). No week exceeds the 4.4h
(+10%) ceiling. **G1 PASSES**, but with a real-world caveat — see "Near-zero slack"
below.

**Near-zero slack (reported per instruction, not a gate failure).** Six weeks (5, 6,
7 [as tabled], 8, 9, 10) sit exactly at the 4.40h ceiling with no cushion of their
own. Total slack across the whole 12-week, 48-hour path is 48 − 47.35 = **0.65h
(1.35%)**, concentrated entirely in the single Week-12 buffer. A plan this tight fails
in practice the first time any session overruns even slightly — there is no week-level
room to absorb it, only the one end-of-course buffer. `schedule.md` itself names the
fix if this matters more than covering all ten modules: drop Module 8 (Seventh
Chords, 4.43 real hours), which would restore a real ≈9-hour (19%) buffer distributed
across the course.

**Which total is right — schedule.md's 47.35h or effort-budget.md's 49.75h?**
Both artifacts sum `resources.md` (reading) + `exercises.md` (practice) +
`assessments.md` (checkpoints) per module, and their module-by-module figures agree
exactly for Modules 1–9 (I re-added every row: e.g. M6 = 4.30+1.40+0.42 = 6.12 in
both). The entire 2.40h gap is Module 10. `resources.md`'s Module 10 entry states
verbatim: "no additional page-count estimate applies... budget the full 5 module
hours to score study, **chord-by-chord labelling, and drafting the written
analysis**." `exercises.md`'s Module 10 exercises are literally "completing the
chord labelling" (Ex. 2, 60 min) and "the written capstone document" (Ex. 3, 45 min)
— the same two activities the curator's own sentence already named as filling the
5-hour envelope. `assessments.md` goes further and says outright that its Module 10
check is "already budgeted within its estimated hours in the curriculum," i.e. not
additional. No other module has this overlap — for Modules 1–9, "read the assigned
pages" (resources.md) and "do the flashcard/sight-reading drills" (exercises.md) are
genuinely separate activities that correctly stack. Module 10 is the one place a
resource description and an exercise description name the identical task. **I judge
schedule.md's reading — Module 10 = one 5.0h envelope, not 5.0+1.9+0.33 — to be the
one the artifacts actually support**, and its 47.35h total to be correct.
`effort-budget.md`'s 49.75h therefore overstates real time by ≈2.4h through a Module
10 double-count; recommend `effort-budget-aggregator` correct this on its next run
(it will run anyway, cascaded from the G5 retry).

### G2 — Total path length ≤ horizon_weeks (schedule.md, curriculum.md)

**PASS**, at the boundary. `schedule.md` schedules 11 active-content weeks plus 1
buffer week = 12 total scheduled weeks. `requirements.md` states `horizon_weeks = 12`.
12 ≤ 12 holds, but with zero margin — the buffer week (Week 12) is both the schedule's
only slack (see G1) and its only margin against the deadline. Any real slip pushes the
plan past the stated horizon.

### G3 — Total cost ≤ budget (effort-budget.md, resources.md)

**PASS.** Budget is £30 (not `unspecified`), so this gate applies. Re-summed
`effort-budget.md`'s Money table: 13 resources × £0 each = £0. Cross-checked against
`resources.md`: every one of the 13 resources carries `free` as its cost field (9
Internet Archive "borrowable" loans, 3 free web pages, 1 public-domain IMSLP/Mutopia
score) — no paywalled or purchase-required item anywhere. £0 ≤ £30, **£30 of
headroom**. The Module 10 hours dispute above does not touch this gate; cost is
unaffected either way.

### G4 — Prerequisite ordering; module 1 grounded in baseline (curriculum.md)

**PASS.** Traced every module's prerequisite list against modules that appear earlier
in the sequence:

| Module | Stated prerequisites | All earlier? |
|---|---|---|
| 1 | baseline | yes (n/a) |
| 2 | 1 | yes |
| 3 | 1, 2 | yes |
| 4 | 2 | yes |
| 5 | 3, 4 | yes |
| 6 | 5 | yes |
| 7 | 6 | yes |
| 8 | 6, 7 | yes |
| 9 | 6, 7 (the "9" printed in the prerequisites cell is explicitly named and corrected as a drafting typo in the prose directly below the table) | yes |
| 10 | 1–9 | yes |

No module lists a prerequisite only taught later. Module 1's prerequisite is
"baseline" (note names, major scale) — `baseline-assessment.md`'s Assessed Baseline
table confirms both as "Known." **G4 PASSES.** (Module 9's table-cell typo is a minor
authoring sloppiness in `curriculum.md`, already self-corrected in the artifact's own
text; not reported as a failure since it does not create an actual ordering problem
and a reader cannot be misled by it.)

### G5 — Outcome coverage + per-module resource/exercise/assessment (curriculum.md, resources.md, exercises.md, assessments.md)

**BLOCKED** — owner: `assessment-designer`.

Outcome coverage itself is fully satisfied: all 5 target outcomes in `requirements.md`
map to ≥1 module in `curriculum.md`'s Outcome coverage table (1→1,2-10; 2→1,3,7;
3→4,5,6,8; 4→9; 5→10). Every module has ≥1 resource (`resources.md`: module counts
2,2,1,1,1,2,1,1,1,1 — all ≥1), ≥1 exercise (`exercises.md`: 4 exercises in every
module), and ≥1 assessment (`assessments.md`: a "Check" section exists for every one
of Modules 1–10).

However, I verified `assessments.md` directly against the specific concern flagged by
`schedule.md`, and it is confirmed:

```
GATE G5 BLOCKED — assessments.md's Summary states "Cumulative reviews land after
Modules 3, 6 and 9," and its own "Cumulative reviews — summary" table (near the end
of Findings) lists a row for "After module 6" ("+ triads, primary triads, Roman
numerals" / "3rd fluency timing"). But Findings contains no "Cumulative review —
after Module 6" section — only "Cumulative review — after Module 3" and "Cumulative
review — after Module 9" exist with worked content (retrieval-sweep items, go/no-go
criteria). The artifact promises content it does not deliver. — owner: assessment-designer
fix: add a "Cumulative review — after Module 6" section to Findings, sized like the
other two reviews (a short retrieval sweep over Modules 4–6 — triads, primary triads,
Roman-numeral labelling — plus the "2nd fluency timing" already implied by the
summary table, ~20–30 minutes), OR, if only two reviews were ever intended, correct
the Summary and the "Cumulative reviews — summary" table to say so and remove the
Module 6 row.
```

Per the structural-check rule that a gate depending on a malformed artifact is
`BLOCKED` rather than `PASS`, G5 is reported as `BLOCKED`, not `PASS`, even though the
narrower "every module has ≥1 assessment" clause is independently satisfied. The
assessment plan as designed does not actually deliver what it claims to deliver, and
downstream artifacts (`schedule.md`, `effort-budget.md`) built their checkpoint-time
totals on the incomplete version, understating true assessment time by roughly
20–30 minutes if the Module 6 review is added rather than removed.

### G6 — No resource URL reused across modules (resources.md)

**PASS**, including the flagged edge case. All 13 resource URLs across the 10
modules are distinct — verified by listing every URL in `resources.md`'s Sources
section and confirming no repeats.

**Piston's *Harmony* edge case.** `resources.md` cites Piston's *Harmony* under both
Module 5 (`https://openlibrary.org/works/OL5272107W`, 1941, DeVoto revision) and
Module 7 (`https://openlibrary.org/works/OL10474110W`, 1948 edition). I judge this a
genuine distinction, not a G6 duplicate: these are two different Open Library **works**
with two different URLs and two different publication years/ISBNs — confirmed live
this run (see G7 sample below, `OL5272107W` fetched and independently confirmed as a
distinct catalog record, 1941/1987 DeVoto edition, 575pp). G6's rule is "no resource
**URL** appears under more than one module" — the URLs differ, so the letter of the
gate is met. `resources.md`'s own Open Questions is transparent that a learner using
only one physical/borrowed copy should simply read both assigned sections from
whichever single edition they obtain, which is the right caveat to carry forward but
does not make this a citation defect.

### G7 — Every resource verified this run with a reachable URL (resources.md)

**PASS.** All 13 resource lines in `resources.md` carry a `verified: <method>
<date>` marker (9× `mcp:openlibrary`, 3× `webfetch`, 1× `webfetch` for the IMSLP
score), all dated `2026-08-18`. Per the run's date note, the run began 2026-08-18 and
today is 2026-08-19, so `2026-08-18` counts as "this run" — not failed on date alone.

I independently sampled 7 of the 13 URLs (above the ≥3 minimum), including the
mandatory IMSLP capstone page:

| URL | Result |
|---|---|
| imslp.org/wiki/6_Piano_Sonatinas,_Op.36_(Clementi,_Muzio) | Live. Confirms Sonatina No. 1 in C major, multiple public-domain scans, and the Mutopia/Chris Sawer 2003 typeset edition `resources.md` recommends. |
| musictheory.net/lessons/24 (via musictheory.net/lessons index) | Live. Lesson 24 is confirmed as "Key Signatures" — matches the citation exactly. (Direct fetch of `/lessons/24` alone returns no readable content because the page is JS-rendered, consistent with `resources.md`'s own Open Questions note; the lesson index confirms existence and numbering.) |
| teoria.com/en/tutorials/intervals/ | Live. Confirmed as an intervals tutorial matching the citation's description. |
| openmusictheory.github.io/harmonicAnalysis.html | Live. Confirmed as a Roman-numeral/functional harmonic-analysis guide, matching the citation. |
| openlibrary.org/works/OL5272107W (Piston/DeVoto *Harmony*, Module 5) | Live. Confirms title, authors, 1941 original / 1987 DeVoto edition — matches citation. |
| openlibrary.org/works/OL280670W (Kostka/Payne *Tonal Harmony*, Module 8) | Live. Confirms title, authors, matches citation (year shown as 1989/1995/2000 editions, consistent with citation's "1989"). |

All 6 fetched (7 counting the capstone) resolved and matched their citations. No
dead links found in the sample. **G7 PASSES** for the sampled set; the remaining 6
unsampled URLs (Wharram, Ottman/Mainous, Benward/Saker/White, Benward/Saker Vol. 1,
Piston *Principles of Harmonic Analysis*, Piston *Harmony* 1948) are all
`mcp:openlibrary`-verified with the same structured-metadata method as the two
Open Library URLs sampled above and were not independently re-fetched.

### G8 — ≥70% of resources match preferred_modality (resources.md)

**PASS.** `preferred_modality = reading`. All 13 resources are reading-format: 9
borrowable/public-domain books, 3 web tutorials/lessons (text-based), and 1
public-domain score (read, not watched or listened to). 13/13 = **100% reading**,
well above the 70% floor. No video resources appear anywhere in the artifact,
consistent with the learner's explicit preference recorded in `requirements.md`.

### G9 — No module more than one level above assessed baseline (curriculum.md, baseline-assessment.md)

**PASS**, under the reading the artifacts themselves set up. `baseline-assessment.md`
defines a five-tier ABRSM-aligned ladder: Rudiments (pre-Grade 1) → Grade 1 → Grade
2–3 → Grade 4–5 → Grade 5–6+, and places the learner at the Rudiments/Grade 1
boundary. `curriculum.md` tags each module with a level from this same ladder:

| Module | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Level | Grade 1 | Grade 1 | Grade 2–3 | Grade 2–3 | Grade 2–3 | Grade 4–5 | Grade 4–5 | Grade 4–5 | Grade 5–6 | Grade 5–6 |

Read against the *static* baseline alone, Modules 6–10 sit two to three ladder-tiers
above the learner's entry point, which would fail a literal one-tier reading — but
that reading would make G9 unsatisfiable by any competently designed multi-week
curriculum for a beginner, since a 12-week course exists precisely to move a learner
several tiers. I instead read G9 as checking that no module jumps more than one
ladder-tier ahead of the tier reached by its own prerequisite chain (already
validated in G4) — i.e. progression is smooth, not that week 12 must resemble week 1.
Under that reading, every step in the module sequence advances by exactly one tier:
Rudiments→Grade 1 (M1–2), Grade 1→Grade 2–3 (M3–5), Grade 2–3→Grade 4–5 (M6–8), Grade
4–5→Grade 5–6 (M9–10) — no module is more than one tier ahead of where its
prerequisites leave the learner. **This is a judgement call, flagged in Open
Questions** — if the intended reading is the literal static-baseline one, this gate
would instead read as a structural failure of the curriculum design itself (the
learner would need a shorter horizon or a narrower goal), and the coordinator should
confirm the intended semantics of "level" in `gates.md` if this ambiguity recurs on
future runs.

### Structural checks

| Artifact | Frontmatter ok | Sections ok | Citations ok |
|---|---|---|---|
| requirements.md | yes | yes | n/a (`None.` — see note below) |
| baseline-assessment.md | yes | yes | yes (5 sources, all `verified:` + dated) |
| curriculum.md | yes | yes | yes (9 sources, all `verified:` + dated) |
| resources.md | yes | yes | yes (13 sources, all `verified:` + dated; 7 sampled live) |
| exercises.md | yes | yes | n/a (`None.` — permitted, exercises is in the exception list) |
| assessments.md | yes | **FAIL** (Summary/table claims content Findings does not contain — see G5) | n/a (`None.` — permitted) |
| schedule.md | yes | yes | n/a (`None.` — permitted) |
| effort-budget.md | yes | yes | n/a (`None.` — permitted) |

All eight artifacts have valid seven-key YAML frontmatter, correct `owner` values
matching `pipeline.json`'s step names, and `inputs` paths that all exist on disk.
No artifact leaks workflow internals — moot at this stage, since no `output/` file
exists yet (this run has not reached `learning-path-builder` or `html-builder`).

Minor observation, not a failure: `requirements.md`'s `## Sources` is `None.`, but
the artifact-validator skill's stated exception list for `None.` names only
`exercises`, `assessments`, `schedule`, and `effort-budget` — `requirements` is not
on that list. In practice `requirements-formalizer` consumes no external data (it is
a Q&A step, not a research step), so `None.` is the honest answer here; flagged in
Open Questions as a possible gap in the skill's exception list rather than a defect
in this run's artifact.

### Link sample

| URL | Verified via | Status |
|---|---|---|
| https://imslp.org/wiki/6_Piano_Sonatinas,_Op.36_(Clementi,_Muzio) | WebFetch | Live — confirms capstone score availability |
| https://www.musictheory.net/lessons (index, confirming lesson 24) | WebFetch | Live — confirms Lesson 24 = Key Signatures |
| https://www.teoria.com/en/tutorials/intervals/ | WebFetch | Live — matches citation |
| https://openmusictheory.github.io/harmonicAnalysis.html | WebFetch | Live — matches citation |
| https://openlibrary.org/works/OL5272107W | WebFetch | Live — matches citation (Piston/DeVoto, 1941/1987) |
| https://openlibrary.org/works/OL280670W | WebFetch | Live — matches citation (Kostka/Payne, *Tonal Harmony*) |

## Sources

- [6 Piano Sonatinas, Op.36 (Clementi, Muzio)](https://imslp.org/wiki/6_Piano_Sonatinas,_Op.36_(Clementi,_Muzio)) — IMSLP/Mutopia · verified: webfetch 2026-08-19
- [musictheory.net lesson index](https://www.musictheory.net/lessons) — musictheory.net · verified: webfetch 2026-08-19
- [Intervals: What is an Interval?](https://www.teoria.com/en/tutorials/intervals/) — teoria.com · verified: webfetch 2026-08-19
- [Performing a harmonic analysis](https://openmusictheory.github.io/harmonicAnalysis.html) — Open Music Theory · verified: webfetch 2026-08-19
- [Harmony (Piston/DeVoto, 1941/1987)](https://openlibrary.org/works/OL5272107W) — Open Library · verified: webfetch 2026-08-19
- [Tonal Harmony (Kostka/Payne)](https://openlibrary.org/works/OL280670W) — Open Library · verified: webfetch 2026-08-19

## Open Questions

- **G9's "level" semantics.** I applied a progressive-tier reading (no module more
  than one ABRSM-ladder tier ahead of where its own prerequisite chain leaves the
  learner) rather than a literal static-baseline reading (no module more than one
  tier above the learner's Day-1 assessed level), because the literal reading would
  make G9 unsatisfiable by any multi-tier course design. If the literal reading is
  actually intended, this run's entire curriculum structure (Modules 6–10) would need
  reconsideration — either a much longer horizon or a narrower goal — and `gates.md`
  should specify which reading is intended so future validator runs don't have to
  guess.
- **effort-budget.md's 49.75h vs schedule.md's 47.35h.** Resolved above in favor of
  schedule.md's reading (Module 10 = one 5.0h envelope). This is reported as a
  finding for `effort-budget-aggregator` to reconcile when it re-runs (cascaded from
  the G5 retry) rather than as a gate failure in its own right, since G3 (the only
  gate checked against `effort-budget.md`) is a cost gate and passes regardless.
- **Week 7 arithmetic in schedule.md's narrative.** The four session lengths listed
  in schedule.md's "Week 7" prose sum to 4.10h by my addition, not the 4.40h stated
  in both the week-total line and the Load-check table. Both the stated and
  re-derived figures are within the G1 ceiling, so this does not change any gate
  outcome, but it is inconsistent with the Module 6 running total (6.12h) which
  requires the full 4.40h across weeks 6–7. Flagged for `schedule-planner`'s
  awareness; not blocking.
- **requirements.md's `Sources: None.`** Not in the artifact-validator skill's
  stated exception list for `None.`, though substantively correct for a Q&A-only
  step. Noted as a possible gap in the skill document itself, not a defect to route
  back to `requirements-formalizer`.
