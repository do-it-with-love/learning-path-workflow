---
artifact: effort-budget
owner: effort-budget-aggregator
run_id: run-003-music-theory
status: final
attempt: 2
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
  - artifacts/validation-report.md
generated: 2026-08-19T10:00:00Z
---

# Effort & Budget — Music Theory for Score Reading and Analysis

## Summary

Total money cost is **£0** against a £30 budget (gate G3 passes with £30 of headroom) —
all 13 resources in `resources.md` are Internet Archive loans, free web pages, or a
public-domain score; nothing is purchased. Total time demand is **≈47.77 hours (47h 46m)**
against the 48-hour envelope (4 h/week × 12 weeks) — **fits, with only ≈0.23 hours
(~14 minutes, ~0.5%) of margin left**, once Module 10 is costed correctly (see
correction below). This is a revision of attempt 1, which put the time total at 49.75h
and failed to fit the envelope; that number was wrong, not the envelope. **Correction
applied this attempt:** attempt 1 correctly *flagged* that `resources.md`'s Module 10
capstone envelope ("chord-by-chord labelling, and drafting the written analysis") and
`exercises.md`'s Module 10 exercises (labelling the chords, writing the capstone
document) describe the same work — but then wrongly *added* both instead of picking one.
The validator re-derived both totals, agreed with `schedule.md`'s reading, and ruled
Module 10 must be counted once, as a single flat 5.0-hour envelope, not as
reading + practice + assessment stacked on top of each other. That fix, plus the
`assessment-designer` revision adding the missing Module 6 cumulative review (+25 min),
are the two changes behind this attempt's total. The single biggest cost driver on this
path remains non-monetary: the **Internet Archive lending model** — 9 of 13 resources
are library loans (account required, one-copy queues, time-limited checkouts), not
owned copies, which is a real risk to the schedule that a £0 price tag hides.

## Findings

### Money

All figures verified against the `verified:` lines and cost fields in `resources.md`
(no resource there carries a non-`free` cost). Currency is already GBP, matching the
learner's stated £30 budget — no conversion was needed. Unchanged from attempt 1; the
validator confirmed this section clean (G3 PASS) and nothing upstream of it changed.

| Resource | Module | Type | Unit cost | Cost over path |
|---|---|---|---|---|
| Elementary Rudiments of Music (Wharram, 1969) | 1 | borrowable (Internet Archive loan) | £0 | £0 |
| Key Signatures — musictheory.net | 1 | free web page | £0 | £0 |
| Rudiments of Music (Ottman/Mainous, 1970) | 2 | borrowable (Internet Archive loan) | £0 | £0 |
| Intervals — teoria.com | 2 | free web page | £0 | £0 |
| Music in Theory and Practice (Benward/Saker/White, 1977) | 3 | borrowable (Internet Archive loan) | £0 | £0 |
| Music in Theory and Practice Vol. 1 (Benward/Saker, 2014) | 4 | borrowable (Internet Archive loan) | £0 | £0 |
| Harmony (Piston/DeVoto, 1941) | 5 | borrowable (Internet Archive loan) | £0 | £0 |
| Principles of Harmonic Analysis (Piston, 1933) | 6 | borrowable (Internet Archive loan) | £0 | £0 |
| Performing a harmonic analysis — Open Music Theory | 6 | free web page | £0 | £0 |
| Harmony (Piston, 1948 ed.) | 7 | borrowable (Internet Archive loan) | £0 | £0 |
| Tonal Harmony (Kostka/Payne, 1989) | 8 | borrowable (Internet Archive loan) | £0 | £0 |
| Form in Tonal Music (Green, 1965) | 9 | borrowable (Internet Archive loan) | £0 | £0 |
| 6 Piano Sonatinas, Op. 36 (Clementi) — IMSLP/Mutopia | 10 (capstone) | public domain (free download, no loan) | £0 | £0 |
| **Total (13 resources)** | — | 9 borrowable + 3 web + 1 public-domain | — | **£0** |

**Arithmetic:** 13 resources × £0 each = £0. £0 total ≤ £30 budget → **£30 of headroom,
gate G3 passes.**

**On "borrowable."** Every "borrowable" claim checks out against `resources.md` as
written — genuinely £0, not a paywalled sample. But it is a real constraint, not a
synonym for "owned": free-to-read subject to a one-user-at-a-time lending queue and a
time-limited loan window. See Hidden costs below.

### Time

**Method and the correction, shown explicitly.** Reading hours are taken verbatim from
`resources.md`'s per-module coverage table. Practice hours are taken verbatim from
`exercises.md`'s practice-load table (core figures, excluding the one optional Module 10
stretch exercise). Assessment hours are the stated minutes of every check and cumulative
review in `assessments.md` (not re-estimated). For **Modules 1–9**, these three sources
describe genuinely separate activities (read the assigned pages; do the flashcard/
sight-reading drills; take the checkpoint) and correctly stack. **Module 10 is
different**, and this is the fix from attempt 1: `resources.md` states its Module 10
entry covers "score study, chord-by-chord labelling, and drafting the written analysis"
inside the module's full 5-hour budget; `exercises.md`'s Module 10 exercises are
literally "completing the chord labelling" (60 min) and "the written capstone document"
(45 min) — the same two activities, not additional ones; and `assessments.md` says its
Module 10 check is "already budgeted within its estimated hours in the curriculum,"
i.e. not additional either. The Module 10 "final check" (a fifth, 10-minute fluency
timing) is likewise treated as occurring inside that same 5-hour session, matching how
`schedule.md` and the validator's re-derivation both handled it — not stacked on top.
So Module 10 is counted **once**, as a flat 5.0-hour envelope, not as
reading (5.0) + practice (1.9) + assessment (0.33) = 7.23h, which is what attempt 1 did.
Attempt 1 was right to flag the overlap as suspicious and wrong to then add both sides
anyway; this attempt corrects that.

| Module | Resource hrs | Practice hrs (core) | Assessment hrs | Module total | Curriculum budget (hrs) | Over/(under) |
|---|---|---|---|---|---|---|
| 1. Key Signatures, Circle of Fifths & Fluency | 2.6 | 1.0 | 0.50 (30 min) | 4.10 | 4 | +0.10 |
| 2. Intervals | 3.2 | 1.1 | 0.42 (25 min) | 4.72 | 4 | +0.72 |
| 3. Minor Scales & Relative/Parallel Keys | 2.9 | 1.1 | 0.42 (25 min) | 4.42 | 4 | +0.42 |
| — Cumulative review after Module 3 | — | — | 0.42 (25 min) | 0.42 | (slack) | n/a |
| 4. Triad Construction & Quality | 3.3 | 1.9 | 0.42 (25 min) | 5.62 | 5 | +0.62 |
| 5. Primary Triads in a Key | 3.0 | 1.0 | 0.33 (20 min) | 4.33 | 3 | +1.33 |
| 6. Roman-Numeral & Lead-Sheet Analysis | 4.3 | 1.4 | 0.42 (25 min) | 6.12 | 5 | +1.12 |
| — Cumulative review after Module 6 (**new this attempt**) | — | — | 0.42 (25 min) | 0.42 | (slack) | n/a |
| 7. Cadences | 1.5 | 0.75 | 0.33 (20 min) | 2.58 | 2 | +0.58 |
| 8. Seventh Chords & Extended Analysis | 3.0 | 1.1 | 0.33 (20 min) | 4.43 | 4 | +0.43 |
| 9. Phrase Structure & Musical Form | 3.3 | 1.4 | 0.42 (25 min) | 5.12 | 4 | +1.12 |
| — Cumulative review after Module 9 | — | — | 0.50 (30 min) | 0.50 | (slack) | n/a |
| 10. Capstone: Full Analysis (flat envelope — see method note) | — | — | — | **5.00** | 5 | **0.00** |
| **Total** | **27.1** (M1–9) + 5.0 folded into M10 = **32.1** | **10.75** (M1–9) + 1.9 folded into M10 | **3.58h/215 min** (M1–9 checks) + **1.33h/80 min** (3 reviews) + 0.33 + 0.17 folded into M10 | **≈47.77** | **40** (module content) + **8** slack = **48** | **+0.00 (fits, ~14 min/0.5% margin)** |

**Arithmetic (module totals, the reproducible path):**
- Modules 1–9, reading: 2.6+3.2+2.9+3.3+3.0+4.3+1.5+3.0+3.3 = **27.1 hrs**.
- Modules 1–9, practice (core): 1.0+1.1+1.1+1.9+1.0+1.4+0.75+1.1+1.4 = **10.75 hrs**.
- Modules 1–9, assessment (module checks): 30+25+25+25+20+25+20+20+25 = 215 min =
  **3.5833 hrs**.
- Modules 1–9 subtotal: 27.1 + 10.75 + 3.5833 = **41.4333 hrs** (matches the sum of the
  nine module-total cells above: 4.10+4.72+4.42+5.62+4.33+6.12+2.58+4.43+5.12 = 41.4333).
- Cumulative reviews (now three, after Module 3, 6, 9): 25+25+30 = 80 min = **1.3333 hrs**.
- Module 10: flat **5.0 hrs** (envelope; not decomposed, per the method note above).
- **Grand total:** 41.4333 + 1.3333 + 5.0 = **47.7667 hrs ≈ 47.77 hrs (47h 46m)**.
- Available: 4 h/week × 12 weeks = **48 hrs**.
- 48 − 47.7667 = **0.2333 hrs (≈14 min, ≈0.5%) of margin remaining. Fits, but only just.**

**Cross-checks.** The reading total (27.1h for Modules 1–9, +5.0h folded for Module 10 =
32.1h) matches `resources.md`'s own stated grand total of "~32.1" hrs exactly — a good
sign the reading figures were transcribed correctly. The curriculum's own module-hour
budget sums to 40h with an 8h slack reserve; the 6.4333h of module-level overage shown in
the "Over/(under)" column above (0.10+0.72+0.42+0.62+1.33+1.12+0.58+0.43+1.12, Module 10
now at exactly 0.00) consumes 6.4333h of that 8h slack, leaving 1.5667h; the three
cumulative reviews (1.3333h) consume nearly all of what remains, leaving the 0.2333h
final margin computed above. Every number in this paragraph is reproducible from the
table's own cells.

**Where the load still concentrates.** Even with Module 10 fixed, eight of the ten
modules still individually run over their own curriculum-budgeted hours before slack is
applied — the worst are **Module 5 (+1.33h)**, **Module 6 (+1.12h)**, and **Module 9
(+1.12h)**. Module 5's overage was flagged by the curator itself ("a tight fit... if it
runs long, stop at the spelling drills"). These are real per-module risks even though
the path fits in aggregate: a learner who runs long on Module 5 or 6 has no
module-level cushion of their own and is drawing down the shared 8-hour slack that the
whole rest of the course also depends on. With only ≈14 minutes of total margin left
after all nine module overages and three cumulative reviews are absorbed, **there is
effectively no room left for anything to run long** — this path is schedule-tight, not
schedule-comfortable, even though it technically fits under 48 hours.

### Hidden costs

Unchanged from attempt 1 — the validator did not dispute any of these, and nothing
upstream that would affect them changed this attempt. None of these appear as a cost
line in `resources.md` because none are priced resources, but a learner would resent
hitting any of them unwarned:

- **Internet Archive account required.** All 9 borrowed books need a free Internet
  Archive/Open Library account to borrow — a real setup step not mentioned anywhere else
  in this run.
- **Lending queues.** Internet Archive's "borrowable" model is controlled digital
  lending — one copy checked out at a time per scanned edition. A widely-used text like
  Kostka & Payne's *Tonal Harmony* (Module 8) or Piston's *Harmony* (used twice, Modules
  5 and 7) is exactly the kind of book that can have a hold queue, stalling that module
  until a copy frees up.
- **Time-limited loans.** Internet Archive loans typically run a 14-day checkout window
  (renewable if uncontested). Given the near-zero time margin computed above, a module
  running even slightly long risks the loan expiring mid-module, forcing a re-borrow
  (and possibly a new queue wait).
- **In-browser-only reading.** Many Internet Archive lending books can only be read in
  the browser reader while the loan is active, not downloaded — a working connection is
  needed each time, not just at borrow time. Not verified live this run against current
  terms; flagged as a general characteristic of the lending model (see Open Questions).
- **Printing.** Several exercises ask the learner to notate on staff paper. No printer,
  ink, or paper cost appears anywhere in `resources.md`. Cost: unknown, not sourced.
- **Manuscript paper.** Free blank-staff PDFs exist, but using them still means printing
  (above) or a notation app not currently in the resource list. Cost: unknown.
- **A metronome.** `exercises.md` references metronome use directly (e.g. Module 1's
  fluency drill). No metronome is listed as a resource. Free phone/web metronome apps
  exist and would keep this at £0, but a physical metronome would be an unbudgeted spend.
  Cost: unknown.
- **Ongoing piano access.** Every exercise and check leans on "play it to check."
  `requirements.md` states the learner is an existing beginner-intermediate pianist, so
  an instrument is reasonably assumed already owned; flagged only because it is the
  largest hidden-cost class if that assumption is wrong, and nothing in this run prices
  one.

### Free-only variant

No separate free-only variant is needed — **the path as designed already costs £0**,
since every one of the 13 resources in `resources.md` is either an Internet Archive loan
or a public-domain download. Dropping "paid" resources loses nothing, because there are
none to drop.

What a **paid** alternative would buy instead is resilience against the hidden costs
above and the near-zero time margin: purchasing the Kostka, Piston, or Benward texts
outright (used copies of these standard theory texts are commonly available secondhand)
would remove the lending-queue and 14-day-loan risk entirely, allow offline reading, and
let the learner annotate the book directly rather than working from a time-limited
library scan — directly protecting the ≈14-minute schedule margin computed above from a
stalled loan. No purchase price is given here because none was found in `resources.md`;
inventing one would violate this artifact's own rule against pricing anything not
sourced this run.

## Sources

None. No currency conversion was required — the learner's budget is already stated in
GBP (`requirements.md`) and every cost in `resources.md` is `free`, so there was no rate
to apply or date to record.

## Open Questions

- **Module 10 double-count — resolved this attempt.** Attempt 1 summed
  `resources.md`'s 5.0h capstone envelope, `exercises.md`'s 1.9h Module 10 practice, and
  `assessments.md`'s 0.33h Module 10 check as three additive figures (7.23h). All three
  describe the same underlying work (score study, chord labelling, drafting the written
  analysis), and `assessments.md` itself says its Module 10 check is "already budgeted."
  The validator's re-derivation agreed with `schedule.md`'s reading (Module 10 = one
  flat 5.0h envelope) and this attempt adopts it. No longer open.
- **Assessment-hour total vs. `assessments.md`'s own rounded figure — resolved this
  attempt.** In attempt 1, the line-item sum (5.00h) didn't match `assessments.md`'s own
  rounded claim ("5.5–6 hours"). The revised `assessments.md` now states "approximately
  5 hours 25 minutes (~5.4 hours)," which matches the line-item sum used here
  (245 + 80 = 325 min = 5.4167h) exactly. No longer open.
- **Whether the Module 10 "final check" (10-min fluency) truly belongs inside the
  5.0h envelope, or is a genuinely separate activity.** This attempt follows
  `schedule.md`'s convention (endorsed by the validator's re-derivation, which reproduced
  schedule.md's 47.35h total only when the final check was folded in, not added) and
  treats it as occurring inside the same capstone session. This is a modelling choice
  carried over from `schedule.md`, not a fact independently verified here — if a future
  revision of `schedule.md` unbundles it, this artifact's Module 10 row and grand total
  would need a matching one-line update (+0.17h).
- **Internet Archive lending terms (queue length, loan duration, in-browser-only
  restrictions).** Described from general knowledge of how Open Library/Internet
  Archive lending works, not from a source verified live during this run. Given the
  near-zero time margin computed above, this is worth the learner checking directly at
  archive.org/openlibrary.org before the path starts, particularly for the two
  higher-traffic texts (Kostka & Payne; Piston).
- **Printing, manuscript paper, and metronome costs.** No prices for any of these were
  found in `resources.md`, so each is recorded as `unknown` rather than estimated. The
  assumption used instead: the learner likely already owns a printer or working
  substitute, has access to free blank-staff PDFs, and can use a free phone metronome
  app, keeping these at £0 in practice — but this is an assumption, not a sourced fact.
- **Piano/keyboard ownership.** Assumed already met, based on `requirements.md`
  describing the learner as an existing beginner-intermediate pianist; not verified or
  priced here.
