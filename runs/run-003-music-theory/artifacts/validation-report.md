---
artifact: validation-report
owner: validator
run_id: run-003-music-theory
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

# Validation Report — Music Theory for Score Reading and Analysis (attempt 2)

## Summary

**ALL GATES PASS.** No step needs to be re-run. `assessment-designer`'s attempt-2 fix
(adding the missing "Cumulative review — after Module 6" section, 25 min) is verified
present, and its Summary, "Cumulative reviews — summary" table, and Findings sections
now agree with each other — the exact self-contradiction that blocked G5 last time is
gone. I independently re-derived the course total from `resources.md` + `exercises.md`
+ `assessments.md` module-by-module rather than trusting that `schedule.md` and
`effort-budget.md` now agree, and got the same figure they report: **47.7667 h ≈
47.77 h** against the 48 h envelope, treating Module 10 as the single flat 5.0 h
envelope per my own attempt-1 ruling (both artifacts correctly applied that ruling this
attempt). No week exceeds the 4.4 h (+10%) G1 ceiling — the highest is exactly 4.40 h,
at the ceiling, not over it. The schedule now has essentially no margin (0.23 h, 0.48%,
concentrated in Week 12) and a ~2-minute sliver of Week 11's capstone proofread spills
into Week 12 — but that spillover stays inside the 12-week horizon (it does not create
a 13th week), so G2 holds at 12 ≤ 12. This is flagged prominently below as a real-world
risk, not papered over, but it is not a gate failure under G1/G2 as written.

## Findings

### G1 — Weekly hours ≤ 4.4h ceiling (schedule.md)

**PASS.** Re-derived every week's session-line sum against the Load-check table:

| Week | Sessions sum | Table figure | ≤ 4.4h? |
|---|---|---|---|
| 1 | 2.6+1.0+0.5 = 4.10 | 4.10 | yes |
| 2 | 2.7+0.5+1.1 = 4.30 | 4.30 | yes |
| 3 | 0.42+2.33+1.1+0.42 = 4.27 | 4.27 | yes |
| 4 | 0.57+0.42+3.3 = 4.29 (table: 4.28) | 4.28 | yes — 0.01h rounding gap, immaterial, unchanged from attempt 1 |
| 5 | 1.9+0.42+2.08 = 4.40 | 4.40 | yes (at ceiling) |
| 6 | 0.92+1.0+0.33+2.15 = 4.40 | 4.40 | yes (at ceiling) |
| 7 | 2.15+1.4+0.42+0.42 = 4.39 | 4.39 | yes — this is the fix: attempt 1's Week 7 gap (4.10 summed vs. 4.40 stated) is now closed |
| 8 | 1.5+0.75+0.33+1.82 = 4.40 | 4.40 | yes (at ceiling) |
| 9 | 1.18+1.1+0.33+1.79 = 4.40 | 4.40 | yes (at ceiling) |
| 10 | 1.51+1.4+0.42+1.07 = 4.40 | 4.40 | yes (at ceiling) |
| 11 | 1.43+2.5+0.47 = 4.40 | 4.40 | yes (at ceiling) |
| 12 | 0.03 | 0.03 | yes (near-empty buffer) |

Total: 4.10+4.30+4.27+4.28+4.40+4.40+4.39+4.40+4.40+4.40+4.40+0.03 = **47.77 h**,
matching both `schedule.md`'s and `effort-budget.md`'s stated totals. No week exceeds
4.4 h. **G1 PASSES.**

**Near-zero slack (reported prominently, not a gate failure).** Seven of eleven active
weeks (5, 6, 8, 9, 10, 11 at exactly 4.40 h, and 7 at 4.39 h) sit at or within one
minute of the ceiling with zero cushion of their own. Total slack across the whole
48-hour path is 48 − 47.77 = **0.23 h (≈0.49%; the artifacts round this to 0.48%, a
sub-0.01-point rounding difference — 0.2333/48 = 0.4861%, immaterial either way),
almost entirely concentrated in Week 12's 4.37 h of genuinely free time. This is
tighter than attempt 1's already-thin 0.65 h (1.35%). In practice, any session running
even slightly long has nowhere to absorb it except the single end-of-course buffer.
`curriculum.md` and `schedule.md` both independently name the same fix if this matters
more than covering all ten modules: **drop Module 8 (Seventh Chords, 4.43 real
hours)**, which would restore a real ≈9-hour (19%) buffer.

**Re-derivation of the 47.77h total from source artifacts (not trusting agreement).**
I re-summed `resources.md`'s per-module reading hours, `exercises.md`'s per-module core
practice hours, and `assessments.md`'s per-module check + cumulative-review minutes
independently, module by module:

- Reading, Modules 1–9 (`resources.md` Coverage-check table): 2.6+3.2+2.9+3.3+3.0+4.3+1.5+3.0+3.3 = **27.1 h**.
- Practice, Modules 1–9, core only (`exercises.md` Practice-load table): 1.0+1.1+1.1+1.9+1.0+1.4+0.75+1.1+1.4 = **10.75 h**.
- Module checks, Modules 1–9 (`assessments.md`): 30+25+25+25+20+25+20+20+25 = 215 min = **3.5833 h**.
- Three cumulative reviews (after Modules 3, 6, 9): 25+25+30 = 80 min = **1.3333 h**.
- Module 10: one flat **5.0 h** envelope — `resources.md`'s own Module 10 text names
  "score study, chord-by-chord labelling, and drafting the written analysis" as filling
  the module's 5 hours; `exercises.md`'s Module 10 exercises ("completing the chord
  labelling," "the written capstone document") and `assessments.md`'s Module 10 check
  ("already budgeted within its estimated hours in the curriculum") both name the
  identical activity rather than additional work. Both artifacts confirm this attempt
  that they applied my attempt-1 ruling rather than stacking three figures.
- **Total: 27.1 + 10.75 + 3.5833 + 1.3333 + 5.0 = 47.7667 h ≈ 47.77 h.**

This matches `schedule.md`'s and `effort-budget.md`'s reported totals exactly — not
because I trusted their agreement, but because I rebuilt the figure from the three
upstream artifacts myself and landed in the same place. 48 − 47.7667 = **0.2333 h
(≈14 minutes) of real slack.**

### G2 — Total path length ≤ horizon_weeks (schedule.md, curriculum.md)

**PASS**, at the boundary, and tighter than attempt 1. `schedule.md` schedules content
through Week 12 (11 active weeks + Week 12 as buffer). `requirements.md` states
`horizon_weeks = 12`. 12 ≤ 12 holds. The ~2-minute (0.03h) sliver of Week 11's capstone
proofread that now spills into Week 12 does **not** breach G2: it lands inside the
already-counted 12th week, not a 13th one — `schedule.md` reports Week 12's total as
0.03h, still fully inside the horizon, with 4.37h of that week genuinely unstructured.
G2 checks total weeks ≤ horizon_weeks, not whether the buffer week is empty, so this is
correctly a PASS, with the caveat that Week 12 is no longer pure slack.

### G3 — Total cost ≤ budget (effort-budget.md, resources.md)

**PASS.** Budget is £30 (not `unspecified`), so this gate applies. Unchanged from
attempt 1 — `resources.md` was not rewritten this attempt. Re-summed
`effort-budget.md`'s Money table: 13 resources × £0 each = £0. Cross-checked against
`resources.md`: every one of the 13 resources carries `free` as its cost field (9
Internet Archive borrowable loans, 3 free web pages, 1 public-domain IMSLP/Mutopia
score). £0 ≤ £30 — **£30 of headroom.**

### G4 — Prerequisite ordering; module 1 grounded in baseline (curriculum.md)

**PASS.** `curriculum.md` is unchanged this attempt. Traced every module's prerequisite
list against modules earlier in the sequence (1→baseline; 2→1; 3→1,2; 4→2; 5→3,4;
6→5; 7→6; 8→6,7; 9→6,7 [table typo "9" self-corrected in prose]; 10→1–9) — no module
lists a prerequisite only taught later. Module 1's prerequisite ("baseline": note
names, major scale) is confirmed "Known" in `baseline-assessment.md`'s Assessed
Baseline table. **G4 PASSES.**

### G5 — Outcome coverage + per-module resource/exercise/assessment (curriculum.md, resources.md, exercises.md, assessments.md)

**PASS.** This is the gate that failed last attempt; re-verified in full, not just spot-checked.

**The specific defect is fixed.** I checked all three places `assessments.md` makes a
claim about the cumulative reviews, not just that a new section appeared:

1. **Summary** (line 28): "Cumulative reviews land after Modules 3, 6 and 9" — names three.
2. **"Cumulative reviews — summary" table** (Findings, near the end): three rows —
   "After module 6" is present, covering "+ triads, primary triads, Roman numerals"
   with "3rd fluency timing" as its new element.
3. **Findings itself**: three fully worked sections exist —
   "Cumulative review — after Module 3" (25 min, retrieval sweep + 2nd fluency
   timing), "Cumulative review — after Module 6" (25 min, retrieval sweep over
   Modules 4–6 — 2 triads, 2 primary-triad spellings, a 4-chord Roman-numeral
   progression — plus the 3rd fluency timing), and "Cumulative review — after Module
   9" (30 min, retrieval sweep across Modules 1–9 plus the 4th fluency timing).

All three agree with each other on count (3), placement (after 3/6/9), and content.
The self-contradiction that blocked this gate last attempt — content promised in
Summary and the table but missing from Findings — no longer exists.

**Outcome coverage and per-module minimums (re-verified, unchanged from attempt 1
since `curriculum.md` and `resources.md`/`exercises.md` were not rewritten):** all 5
target outcomes in `requirements.md` map to ≥1 module in `curriculum.md`'s Outcome
coverage table (1→1,2–10; 2→1,3,7; 3→4,5,6,8; 4→9; 5→10). Every module has ≥1 resource
(module counts: 2,2,1,1,1,2,1,1,1,1 — all ≥1), ≥1 exercise (4 per module in
`exercises.md`), and ≥1 assessment (a Check section for every one of Modules 1–10 in
`assessments.md`, plus the three cumulative reviews as extras). **G5 PASSES.**

### G6 — No resource URL reused across modules (resources.md)

**PASS.** `resources.md` is unchanged this attempt. All 13 resource URLs across the 10
modules are distinct. Piston's *Harmony* appears under Module 5
(`https://openlibrary.org/works/OL5272107W`, 1941 DeVoto revision) and Module 7
(`https://openlibrary.org/works/OL10474110W`, 1948 edition) — two different Open
Library works with two different URLs and ISBNs, so the letter of the gate ("no
resource URL appears under more than one module") is met. Carried forward as a caveat
in `resources.md`'s own Open Questions, not a defect.

### G7 — Every resource verified this run with a reachable URL (resources.md)

**PASS.** `resources.md` is unchanged this attempt; all 13 lines still carry a
`verified: <method> <date>` marker (9× `mcp:openlibrary`, 3× `webfetch`, 1× `webfetch`
for the IMSLP score), dated `2026-08-18`. Per the run's date note (run began
2026-08-18, today is 2026-08-19), `2026-08-18` counts as "this run."

I independently re-sampled 5 of the 13 URLs this attempt (above the ≥3 minimum),
including the mandatory IMSLP capstone page:

| URL | Result |
|---|---|
| imslp.org/wiki/6_Piano_Sonatinas,_Op.36_(Clementi,_Muzio) | Live. Confirms 6 sonatinas (1797, Longman & Broderip); Sonatina No. 1 in C major; the Mutopia/Chris Sawer 2003 typeset edition plus multiple public-domain scans, all downloadable — matches the citation. |
| openlibrary.org/works/OL280670W (Kostka/Payne *Tonal Harmony*, Module 8) | Live. Confirms title, authors (Stefan Kostka, Dorothy Payne), 1989 original / 1995 3rd ed. — matches citation. |
| teoria.com/en/tutorials/intervals/ | Live. Confirmed as an intervals tutorial covering interval number and quality, matching the citation. |
| openmusictheory.github.io/harmonicAnalysis.html | Live. Confirmed as a Roman-numeral/functional harmonic-analysis guide with a worked Haydn example — matches citation. |
| openlibrary.org/works/OL5272107W (Piston/DeVoto *Harmony*, Module 5) | **Inconclusive** — WebFetch returned a tool-side read timeout on two attempts, not a confirmed-dead page. Not counted as a failure: this citation's original verification method is `mcp:openlibrary`, a different, structured-metadata channel than the WebFetch spot-check used here, and the same URL/work-ID (`OL5272107W`) was already independently confirmed live in attempt 1's validation. |

4 of 5 sampled URLs resolved and matched their citations on this attempt; the fifth
timed out at the tool level rather than returning a dead-link response. This meets and
exceeds the ≥3-URL sampling floor with URLs that did resolve. **G7 PASSES.** The
remaining 8 unsampled URLs carry the same `mcp:openlibrary`/`webfetch` verification
markers and were independently sampled (a different subset) and confirmed in attempt
1's validation.

### G8 — ≥70% of resources match preferred_modality (resources.md)

**PASS.** `preferred_modality = reading`. Unchanged this attempt: all 13 resources are
reading-format (9 borrowable/public-domain books, 3 web tutorials/lessons, 1
public-domain score). 13/13 = **100% reading**, well above the 70% floor.

### G9 — No module more than one level above assessed baseline (curriculum.md, baseline-assessment.md)

**PASS**, under the same progressive-tier reading applied in attempt 1 (see Open
Questions — this judgement call is unchanged since neither `curriculum.md` nor
`baseline-assessment.md` was rewritten). `baseline-assessment.md` places the learner at
the Rudiments/Grade 1 boundary on its five-tier ABRSM-aligned ladder; `curriculum.md`
advances exactly one tier per prerequisite step (Rudiments→Grade 1 for Modules 1–2,
Grade 1→Grade 2–3 for Modules 3–5, Grade 2–3→Grade 4–5 for Modules 6–8, Grade
4–5→Grade 5–6 for Modules 9–10) — no module is more than one tier ahead of where its
own prerequisite chain leaves the learner. **G9 PASSES** under this reading.

### Structural checks

| Artifact | Frontmatter ok | Sections ok | Citations ok |
|---|---|---|---|
| requirements.md | yes | yes | n/a (`None.` — see attempt-1 note on the skill's exception list) |
| baseline-assessment.md | yes | yes | yes (5 sources, `verified:` + dated) |
| curriculum.md | yes | yes | yes (9 sources, `verified:` + dated) |
| resources.md | yes | yes | yes (13 sources, `verified:` + dated; 5 sampled this attempt, 4 confirmed live, 1 tool-timeout) |
| exercises.md | yes | yes | n/a (`None.` — permitted) |
| assessments.md | yes | **yes (fixed)** — Summary, the reviews table, and Findings now agree on 3 cumulative reviews after Modules 3/6/9 | n/a (`None.` — permitted) |
| schedule.md | yes | yes | n/a (`None.` — permitted) |
| effort-budget.md | yes | yes | n/a (`None.` with explanatory sentence — permitted; still substantively "no external source") |

All eight artifacts have valid seven-key YAML frontmatter, correct `owner` values
matching `pipeline.json`'s step names, `attempt: 2` on the three revised artifacts
(`assessments.md`, `schedule.md`, `effort-budget.md`) and `attempt: 1` on the four
untouched ones, and `inputs` paths that all exist on disk. No `output/` artifacts exist
yet (this run has not reached `learning-path-builder` or `html-builder`), so the
"no workflow internals leak into output/" check is moot at this stage.

### Link sample

| URL | Verified via | Status |
|---|---|---|
| https://imslp.org/wiki/6_Piano_Sonatinas,_Op.36_(Clementi,_Muzio) | WebFetch | Live — confirms capstone score, Sonatina No.1 in C major, free scores incl. Mutopia edition |
| https://openlibrary.org/works/OL280670W | WebFetch | Live — matches citation (Kostka/Payne, *Tonal Harmony*, 1989/1995) |
| https://www.teoria.com/en/tutorials/intervals/ | WebFetch | Live — matches citation |
| https://openmusictheory.github.io/harmonicAnalysis.html | WebFetch | Live — matches citation |
| https://openlibrary.org/works/OL5272107W | WebFetch (2 attempts) | Tool-side read timeout — inconclusive, not counted as dead; verified live in attempt 1 |

## Sources

- [6 Piano Sonatinas, Op.36 (Clementi, Muzio)](https://imslp.org/wiki/6_Piano_Sonatinas,_Op.36_(Clementi,_Muzio)) — IMSLP/Mutopia · verified: webfetch 2026-08-19
- [Tonal Harmony (Kostka/Payne)](https://openlibrary.org/works/OL280670W) — Open Library · verified: webfetch 2026-08-19
- [Intervals: What is an Interval?](https://www.teoria.com/en/tutorials/intervals/) — teoria.com · verified: webfetch 2026-08-19
- [Performing a harmonic analysis](https://openmusictheory.github.io/harmonicAnalysis.html) — Open Music Theory · verified: webfetch 2026-08-19

## Open Questions

- **G9's "level" semantics.** Unchanged from attempt 1: I applied a progressive-tier
  reading (no module more than one ABRSM-ladder tier ahead of where its own
  prerequisite chain leaves the learner) rather than a literal static-baseline reading,
  because the literal reading would make G9 unsatisfiable by any multi-tier course
  design. `gates.md` should specify which reading is intended so future validator runs
  don't have to guess.
- **The 0.23h vs. 0.48%/0.49% rounding.** `schedule.md` and `effort-budget.md` both
  state the remaining slack as "0.48%"; my own division of 0.2333/48 gives 0.4861%,
  which rounds to 0.49% at two significant figures. This is a sub-0.01-percentage-point
  difference with no effect on any gate outcome and is noted only for completeness.
- **OL5272107W WebFetch timeout.** Two WebFetch attempts on this URL both returned a
  tool-side read timeout rather than page content. This is not treated as a G7 failure
  — the citation's original verification method is `mcp:openlibrary` (a different
  channel), and this exact URL was independently confirmed live via WebFetch in
  attempt 1's validation — but a future run should re-check it if the pattern recurs.
- **Real-world slack is now 0.48–0.49%, effectively zero.** Not a gate failure (G1 and
  G2 are both satisfied on the numbers as re-derived), but flagged as a genuine
  practical risk per the dispatch instructions: seven of eleven active weeks have no
  cushion of their own, and the only remaining margin is a 14-minute sliver of Week 12.
  If the coordinator or learner wants real breathing room rather than the bare minimum
  gate pass, `curriculum.md` and `schedule.md` both independently point to the same
  lever — dropping Module 8 (Seventh Chords) would restore a genuine ~9-hour (19%)
  buffer. This is a scope decision for the coordinator/learner, not something this
  validator can or should apply unilaterally.
- **Week 4's 0.01h rounding gap** (session lines sum to 4.29h against a stated 4.28h)
  persists unchanged from attempt 1 — cosmetic, does not affect any gate outcome, not
  reported as a failure.
