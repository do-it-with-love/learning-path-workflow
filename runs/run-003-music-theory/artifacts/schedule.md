---
artifact: schedule
owner: schedule-planner
run_id: run-003-music-theory
status: final
attempt: 2
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
generated: 2026-08-19T11:00:00Z
---

# Schedule — Music Theory for Score Reading and Analysis

## Summary

**Revision (attempt 2).** `assessments.md` attempt 2 added the previously-missing
Module 6 cumulative review (25 min), raising checkpoint/review time across the course
from ~5.0 h to **245 min of module checks + 80 min of cumulative reviews (25+25+30) =
5 h 25 min (~5.42 h)**. The validator ruled schedule.md's Module‑10 reading (one flat
5.0 h envelope, not three stacked figures) correct, and `effort-budget.md` now agrees
at **~47.77 h** total real work — up 0.42 h from the previous 47.35 h. Against the
48 h budget (4 h/week × 12 weeks) that leaves **0.23 h (0.48%) of real slack — tighter
than the already-thin 0.65 h (1.35%) in attempt 1**, and it does not fit anywhere for
free: the new 25 minutes had to be threaded through the back half of the course. I
placed the Module 6 cumulative review immediately after Module 6 finishes (Week 7,
now entirely Module‑6 content), which pushed every already-at-ceiling week from
Weeks 7–11 forward by the same amount; because Weeks 5–11 have no room of their own
(all sit at or within 0.01 h of the 4.4 h G1 ceiling), that pressure cascades to the
very end of the course, where **a ~2‑minute (0.03 h) sliver of the capstone's final
fluency check now falls just past the Week 11 boundary into Week 12**. No week
exceeds 4.4 h anywhere (G1 holds), and the total stays at 12 scheduled weeks (G2
holds, 12 ≤ 12), but Week 12 is no longer a perfectly empty buffer — it is now a
buffer with 0.03 h (about two minutes) of unavoidable spillover and 4.37 h still
completely free. This rebuild also resolves the arithmetic gap the validator flagged
in attempt 1's Week 7 (session lines summing to 4.10 h against a stated 4.40 h): the
Module 6 reading total (4.30 h) now correctly splits as 2.15 h + 2.15 h across Weeks
6–7 rather than 2.15 h + 1.85 h. Weeks 1–5 are unchanged from attempt 1 — the revision
only touches Weeks 6–12, exactly where the new content and its consequences land.
**The honest caveat, now sharper than before: real slack is 0.48%, not the ~15% this
method targets, and seven of eleven active weeks (5, 6, 8, 9, 10, 11, and Week 7 at
4.39 h) sit at or within a minute of the ceiling with zero cushion of their own.** If
genuine weekly breathing room matters more than covering all ten modules, **Module 8
(Seventh Chords, 4.43 real hours) remains the cut `curriculum.md` itself names as most
cuttable** — dropping it would restore a real ~9-hour (19%) buffer distributed across
the course, comfortably resolving both this run's tightness and any future revision.

## Findings

### Real hours per module (arithmetic)

| Module | Resource + practice | Checkpoint (assessments.md) | **Real total** | Curriculum's own estimate |
|---|---|---|---|---|
| 1. Key signatures & fluency | 3.60 h | 0.50 h (30 min) | **4.10 h** | 4 h |
| 2. Intervals | 4.30 h | 0.42 h (25 min) | **4.72 h** | 4 h |
| 3. Minor scales & relative keys | 4.00 h | 0.42 h (25 min) | **4.42 h** | 4 h |
| — Cumulative review after M3 | — | 0.42 h (25 min) | **0.42 h** | (not in curriculum) |
| 4. Triad construction | 5.20 h | 0.42 h (25 min) | **5.62 h** | 5 h |
| 5. Primary triads | 4.00 h | 0.33 h (20 min) | **4.33 h** | 3 h |
| 6. Roman-numeral & lead-sheet | 5.70 h | 0.42 h (25 min) | **6.12 h** | 5 h |
| — **Cumulative review after M6 (NEW this attempt)** | — | 0.42 h (25 min) | **0.42 h** | (not in curriculum) |
| 7. Cadences | 2.25 h | 0.33 h (20 min) | **2.58 h** | 2 h |
| 8. Seventh chords | 4.10 h | 0.33 h (20 min) | **4.43 h** | 4 h |
| 9. Phrase structure & form | 4.70 h | 0.42 h (25 min) | **5.12 h** | 4 h |
| — Cumulative review after M9 | — | 0.50 h (30 min) | **0.50 h** | (not in curriculum) |
| 10. Capstone | 5.00 h* | — * | **5.00 h** | 5 h |
| **Total** | — | — | **47.77 h** | 40 h |

\* Module 10: `resources.md`'s full 5-hour envelope already covers score study,
chord-by-chord labelling and drafting — the same activities `exercises.md` (1.9 h)
and `assessments.md` (0.5 h) separately itemize, and `assessments.md` states its
Module 10 check is "already budgeted" within the curriculum's 5-hour allocation.
Treated as one 5.0 h envelope, per the validator's ruling in `validation-report.md`
attempt 1 (schedule.md's reading was found correct; `effort-budget.md`'s 49.75 h
was found to double-count ≈2.4 h here and has since been corrected to ~47.77 h).

**Arithmetic check (precise, computed in minutes to avoid compounding rounding):**
R+E sum across Modules 1–9 = 37.85 h. Checkpoints across Modules 1–9, computed at
exact fractions of an hour (30, 25, 25, 25, 20, 25, 20, 20, 25 min) = 3.58333 h.
Three cumulative reviews (25, 25, 30 min) = 1.33333 h. Module 10 flat envelope =
5.00 h. **Total = 37.85 + 3.58333 + 1.33333 + 5.00 = 47.76667 h ≈ 47.77 h** — matches
`effort-budget.md`'s independently re-derived total exactly. (Summing the table's
individually-rounded 2-decimal figures instead gives 47.78 h; the 0.01 h gap is
compounding rounding across seven 25-minute items each rounded to 0.42 h rather than
0.41667 h, and is immaterial — the 47.77 h figure is the one both this artifact and
`effort-budget.md` report.) Against the 48-hour budget (4 h × 12 weeks): real slack =
48 − 47.77 = **0.23 h (0.48%)**.

### Week 1: Module 1 — Key Signatures, Circle of Fifths & Reading Fluency

*Unchanged from attempt 1.*

- **Weekend session (2.6 h, new material):** Read Wharram, *Elementary Rudiments of
  Music*, pp. 20–55 (2.3 h) + musictheory.net "Key Signatures" lesson (0.3 h).
- **Weekday session (1.0 h, drills):** Key-signature flashcards, bass-clef fluency
  baseline timing, naming keys from unfamiliar signatures, capstone key preview.
- **Weekday session (0.5 h, review):** Module 1 checkpoint — key-signature quiz and
  fluency baseline logged (first of five fluency data points).

**Week total: 4.10 h.**

### Week 2: Module 2 — Intervals (part 1)

*Unchanged from attempt 1.*

- **Weekend session (2.7 h, new material):** Read Ottman & Mainous, *Rudiments of
  Music*, pp. 60–100.
- **Weekday session (0.5 h, drills):** teoria.com interval tutorial and exercises.
- **Weekday session (1.1 h, drills):** Interval flashcards (played, not just
  named), bass-clef fluency with interval-spotting, real-music leap application,
  capstone interval synthesis.

**Week total: 4.30 h.** Module 2 checkpoint (0.42 h) carried to Week 3.

### Week 3: Module 2 checkpoint → Module 3 — Minor Scales & Relative/Parallel Keys (part 1)

*Unchanged from attempt 1.*

- **Weekday session (0.42 h, review):** Module 2 checkpoint — interval quiz plus
  the unfamiliar-tonic major-scale check.
- **Weekend session (2.33 h, new material):** Read Benward, Saker & White, *Music
  in Theory and Practice*, pp. 40–75 — first ~4/5 of the assigned reading.
- **Weekday session (1.1 h, drills):** Three-forms-of-minor drill, raised-leading-
  tone fluency, major-or-relative-minor application, Module 1 excerpt revisit.
- **Weekday session (0.42 h, review):** Module 3 checkpoint — minor-scale and
  relative-minor quiz.

**Week total: 4.27 h.**

### Week 4: Module 3 finish, cumulative review → Module 4 — Triad Construction (part 1)

*Unchanged from attempt 1.*

- **Weekday session (0.57 h, new material):** Finish the Benward/Saker/White
  reading, pp. 40–75 (remaining portion).
- **Weekday session (0.42 h, review):** Cumulative review after Module 3 —
  retrieval sweep over key signatures, intervals, and minor scales, plus the
  2nd fluency timing.
- **Weekend session (3.3 h, new material):** Read Benward & Saker, *Music in
  Theory and Practice, Vol. 1*, pp. 90–130 (triad construction, quality,
  inversion).

**Week total: 4.28 h.**

### Week 5: Module 4 finish → Module 5 — Primary Triads (part 1)

*Unchanged from attempt 1.*

- **Weekday sessions (1.9 h total, drills, split ~1.0 h + ~0.9 h across two
  evenings):** Triad-building-and-playing drills (all four qualities), fluency
  naming triad quality while reading, root/quality/inversion-by-ear application,
  capstone triad synthesis.
- **Weekday session (0.42 h, review):** Module 4 checkpoint — triad build,
  sight-quality ID, and inversion quiz.
- **Weekend session (2.08 h, new material):** Read Piston & DeVoto, *Harmony*,
  pp. 15–45 — first portion (primary triads).

**Week total: 4.40 h** — at the G1 ceiling.

### Week 6: Module 5 finish → Module 6 — Roman-Numeral & Lead-Sheet Analysis (part 1)

*Unchanged from attempt 1.*

- **Weekday session (0.92 h, new material):** Finish the Piston & DeVoto reading,
  pp. 15–45 (remaining portion).
- **Weekday session (1.0 h, drills):** Spelling I/IV/V/vi from memory, fluency
  naming I/IV/V while reading, locating primary triads by feel, matching Module
  4's triads to the primary-triad set.
- **Weekday session (0.33 h, review):** Module 5 checkpoint — primary-triad
  spelling, degree-pattern recall, and score-location check.
- **Weekend session (2.15 h, new material):** Read Piston, *Principles of
  Harmonic Analysis*, pp. 1–40 — first portion (~half the assigned reading).

**Week total: 4.40 h** — at the G1 ceiling.

### Week 7: Module 6 completion (reading, exercises, checkpoint) + NEW cumulative review

**Revised.** Week 7 is now entirely Module 6 content — no Module 7 material starts
here — which both fits the new cumulative review and fixes the 0.30 h arithmetic gap
the validator flagged in attempt 1 (the Piston *Principles* reading now correctly
splits 2.15 h + 2.15 h = 4.30 h across Weeks 6–7, matching `resources.md` exactly,
instead of 2.15 h + 1.85 h = 4.00 h).

- **Weekend session (2.15 h, new material):** Finish the Piston *Principles of
  Harmonic Analysis* reading, pp. 1–40 (remaining portion, now correctly sized),
  plus the Open Music Theory "Performing a harmonic analysis" web chapter.
- **Weekday session (1.4 h, drills):** Full diatonic triad set drill, Roman-
  numeral fluency while reading, two-labelling-systems application, first
  Roman-numeral pass on the capstone's opening phrase.
- **Weekday session (0.42 h, review):** Module 6 checkpoint — progression
  labelling plus the Clementi first pass.
- **Weekday session (0.42 h, review — NEW):** Cumulative review after Module 6 —
  closed-book retrieval sweep over Modules 4–6 (2 triads built from root+quality,
  2 primary-triad spellings, a 4-chord Roman-numeral progression), plus the
  **3rd fluency timing exercise**.

**Week total: 4.39 h** — 0.01 h under the G1 ceiling. Module 7 now starts fresh
in Week 8 with no material carried in from here.

### Week 8: Module 7 (complete) → Module 8 — Seventh Chords (part 1)

**Revised.** Because Module 7 no longer has a head start from Week 7, all of it
(2.58 h) now fits inside Week 8 alongside the start of Module 8's reading.

- **Weekday session (1.5 h, new material):** Read Piston, *Harmony* (1948),
  pp. 40–55 (cadences) — the full assigned reading, now done in one week.
- **Weekday session (0.75 h, drills):** Naming cadences by ear, cadence-spotting
  fluency, cadence-as-key-evidence application, confirming the capstone's key.
- **Weekday session (0.33 h, review):** Module 7 checkpoint — cadence naming and
  key confirmation.
- **Weekend session (1.82 h, new material):** Read Kostka & Payne, *Tonal
  Harmony*, pp. 200–230 — first portion (the dominant seventh chord).

**Week total: 4.40 h** — at the G1 ceiling.

### Week 9: Module 8 finish → Module 9 — Phrase Structure & Musical Form (part 1)

**Revised** (split points shifted to absorb the forward pressure from Week 7).

- **Weekday session (1.18 h, new material):** Finish the Kostka & Payne reading,
  pp. 200–230 (remaining portion).
- **Weekday session (1.1 h, drills):** Spell-and-resolve-V7 drill, fluency
  spotting V7 while reading, V7-in-context application, upgrading V to V7 in
  the capstone.
- **Weekday session (0.33 h, review):** Module 8 checkpoint — V7 spelling and
  passage-scan check.
- **Weekend session (1.79 h, new material):** Read Green, *Form in Tonal Music*,
  pp. 1–40 — first portion.

**Week total: 4.40 h** — at the G1 ceiling.

### Week 10: Module 9 finish, cumulative review → Capstone begins

**Revised** (capstone's first session now starts smaller — 0.57 h instead of
1.0 h — to keep the week at the ceiling rather than over it).

- **Weekday session (1.51 h, new material):** Finish the Green reading, pp. 1–40
  (remaining portion).
- **Weekday session (1.4 h, drills):** Marking phrase boundaries by ear, full-
  piece fluency reading-speed check, binary-or-ternary application, mapping the
  capstone's opening section.
- **Weekday session (0.42 h, review):** Module 9 checkpoint — phrase/form quiz
  on a fresh short piece.
- **Weekend session (1.07 h):** Cumulative review after Module 9 (0.50 h —
  retrieval sweep across Modules 1–9 plus the 4th fluency timing) directly
  followed by the **first capstone session** (0.57 h — begin extending the
  Roman-numeral/lead-sheet labelling to the whole movement).

**Week total: 4.40 h** — at the G1 ceiling.

### Week 11: Module 10 — Capstone, almost to completion

**Revised** (absorbs the remainder of the labelling session carried from Week 10;
the final session is trimmed by 0.03 h, which completes in Week 12).

- **Weekend session (1.43 h):** Complete extending the chord labelling to the
  entire movement — the 0.43 h remainder of the session begun in Week 10 (0.57 h
  there), plus a full continuation session (1.0 h).
- **Weekend session (2.5 h, one long contiguous sitting):** Complete the
  phrase/form map for the whole piece and draft the connected written analysis
  — key with evidence, the chord progression in prose, and how the sections
  relate.
- **Weekday session (0.47 h):** Final (5th) fluency check — repeat the timed
  sight-reading exercise and compare against the four earlier data points —
  plus most of a proofread of the capstone document, verifying claims against
  the score. The last couple of minutes of this proofread pass finish in
  Week 12 (see below).

**Week total: 4.40 h** — at the G1 ceiling.

### Week 12: Buffer week (with a ~2-minute tail item)

**Revised.** Nearly unchanged in spirit — this remains the schedule's deliberate
slack week — but it is no longer perfectly empty. A genuinely tiny (0.03 h, about
two minutes) sliver of Week 11's final proofread pass falls just past the Week 11
boundary once the new cumulative review's 25 minutes are threaded through the
already-full Weeks 5–11.

- **(0.03 h):** Finish the last line or two of the capstone proofread / fluency
  trend write-up carried over from Week 11.
- **The remaining 4.37 h is unstructured, as before:** catch up on any module that
  ran long, get extra sight-reading fluency practice, revisit a *not yet* rubric
  result from any checkpoint, or simply stop early if the course went to plan.

**Week total: 0.03 h.** In every practical sense this is still a full buffer week.

### Load check

| Week | Module(s) | Planned hours | Budget | Margin |
|---|---|---|---|---|
| 1 | 1 | 4.10 | 4.0 | +0.10 (+2.5%) |
| 2 | 2 | 4.30 | 4.0 | +0.30 (+7.5%) |
| 3 | 2 → 3 | 4.27 | 4.0 | +0.27 (+6.7%) |
| 4 | 3 → 4 | 4.28 | 4.0 | +0.28 (+7.0%) |
| 5 | 4 → 5 | 4.40 | 4.0 | +0.40 (+10.0%) |
| 6 | 5 → 6 | 4.40 | 4.0 | +0.40 (+10.0%) |
| 7 | 6 (complete) + cumulative review | 4.39 | 4.0 | +0.39 (+9.75%) |
| 8 | 7 (complete) → 8 | 4.40 | 4.0 | +0.40 (+10.0%) |
| 9 | 8 → 9 | 4.40 | 4.0 | +0.40 (+10.0%) |
| 10 | 9 → 10 | 4.40 | 4.0 | +0.40 (+10.0%) |
| 11 | 10 | 4.40 | 4.0 | +0.40 (+10.0%) |
| 12 | buffer (+0.03 h tail) | 0.03 | 4.0 | −3.97 (−99.25%) |
| **Total** | — | **47.77** | **48.0** | **−0.23 (−0.48%)** |

No week exceeds 4.4 h (the 10%-over ceiling for G1). Seven weeks (5, 6, 8, 9, 10, 11
at exactly +10.0%, and 7 at +9.75%) sit at or within 0.01 h of that ceiling with zero
cushion of their own — one more week at the ceiling than attempt 1's six. Total
planned hours (47.77) is 0.23 h under the 48-hour budget — that 0.23 h, concentrated
almost entirely in Week 12's 4.37 h of genuinely free time, is the entirety of the
schedule's real slack.

**Arithmetic reproduction:** 4.10+4.30+4.27+4.28+4.40+4.40+4.39+4.40+4.40+4.40+4.40+0.03
= 47.77 h. 48.0 − 47.77 = 0.23 h (0.23/48 = 0.48%).

### Deadline check

Active-content weeks: 11 (Weeks 1–11 all carry scheduled study; Week 11 is now fully
packed at the ceiling rather than the 4.00 h it held in attempt 1). Total scheduled
weeks including the buffer: **12**. `horizon_weeks` = 12. **12 ≤ 12 — G2 is met**,
with Week 12's now-thinner-than-before buffer as the only margin against the deadline.

## Sources

None.

## Open Questions

- **Real slack has fallen to 0.48%, from an already-thin 1.35% in attempt 1.**
  Bottom-up hours (resources + exercises + assessments, summed exactly as instructed,
  not re-estimated) now come to 47.77 h against a 48 h budget. I did not compress any
  module's or checkpoint's hours to manufacture room — every minute of the new
  Module 6 cumulative review is accounted for by nudging split points across Weeks
  7–11, all of which were already at the G1 ceiling with nothing to give. The result
  is genuinely tight: seven of eleven active weeks are now at or within one minute of
  4.4 h. **If real weekly breathing room matters more than covering all ten modules,
  the fix is scope, not arithmetic:** `curriculum.md`'s own Open Questions already
  names **Module 8 (Seventh Chords, 4.43 real hours)** as the most cuttable — outcome
  3 only requires "simple" sevenths and could be reduced to recognition-only inside
  Module 6. Cutting it would restore a real ~9-hour (19%) buffer distributed across
  the course, comfortably absorbing this and any future revision.
- **Week 12 is no longer perfectly empty.** A 0.03 h (≈2-minute) tail item — the last
  moment of the Week 11 proofread/fluency write-up — now falls into Week 12 because
  Weeks 5–11 have no room of their own to absorb the new review's 25 minutes. This is
  reported plainly rather than rounded away, per the instruction to show arithmetic
  the validator can reproduce; in every practical sense (4.37 h of the week still
  fully free) Week 12 still functions as the course's buffer week.
- **Attempt 1's Week 7 arithmetic gap is resolved by this revision.** The validator
  found Week 7's session lines summed to 4.10 h against a stated 4.40 h, because the
  Piston *Principles of Harmonic Analysis* reading (4.30 h total per `resources.md`)
  was split 2.15 h (Week 6) + 1.85 h (Week 7) = 4.00 h, short by 0.30 h. Restructuring
  Week 7 to hold all remaining Module 6 content (reading remainder, exercises,
  checkpoint, and the new cumulative review) forced the split back to the correct
  2.15 h + 2.15 h = 4.30 h. No separate fix was needed — placing the new review
  correctly required re-deriving this boundary anyway.
- **Module-level overruns versus `curriculum.md`'s per-module budget remain
  systemic, not isolated**, unchanged from attempt 1: Module 6 costs 6.12 h against a
  5 h curriculum allocation (+22%), Module 9 costs 5.12 h against 4 h (+28%), Module 2
  costs 4.72 h against 4 h (+18%). This is worth `curriculum-architect` knowing for
  any future revision.
- **Module 10's hours remain a single 5.0 h envelope**, per the validator's explicit
  ruling in attempt 1 (`validation-report.md`): `resources.md`'s capstone description
  already covers the chord-labelling and drafting activities `exercises.md` and
  `assessments.md` separately itemize, so adding all three literally would
  double-count ≈2.4 h of the same work. `effort-budget.md` now agrees at ~47.77 h.
- **Reading-block splits across weeks use approximate proportions, not confirmed page
  breakpoints**, as in attempt 1 — `resources.md` gives page ranges, not a
  chapter-level table of contents, so a precise split point isn't available. The
  learner should divide each assigned page range roughly in the stated proportion.
