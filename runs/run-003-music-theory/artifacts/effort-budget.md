---
artifact: effort-budget
owner: effort-budget-aggregator
run_id: run-003-music-theory
status: final
attempt: 1
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
generated: 2026-08-18T18:00:00Z
---

# Effort & Budget — Music Theory for Score Reading and Analysis

## Summary

Total money cost is **£0** against a £30 budget (gate G3 passes with £30 of headroom) —
verified against `resources.md`, where all 13 resources are either lent free via
Internet Archive ("borrowable") or public-domain downloads, with no purchase, paywall,
or subscription anywhere in the list. Total time demand, summing `resources.md`'s
reading hours, `exercises.md`'s core practice hours and `assessments.md`'s checkpoint
hours exactly as those three artifacts state them, is **≈49.75 hours** against the
48-hour envelope (4 h/week × 12 weeks) — **over by ≈1.75 hours (~3.6%)**, concentrated
in Modules 5, 6, 9 and, especially, Module 10, where `resources.md` and `exercises.md`
appear to double-book the same "label the chords / draft the analysis" work inside a
single 5-hour curriculum slot. The single biggest cost driver on this path is not money
at all — it is the **Internet Archive lending model** itself: nine of the thirteen
resources are "borrowable," which is genuinely free but comes with an account
requirement, one-copy-at-a-time queues, and time-limited loans, any of which can stall
a module in a way a cash price never would.

## Findings

### Money

All figures verified against the `verified:` lines and cost fields in `resources.md`
(no resource there carries a non-`free` cost). Currency is already GBP, matching the
learner's stated £30 budget — no conversion was needed.

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

**On "borrowable."** `resources.md`'s own summary states every book carries
`ebook_access: borrowable` or is public domain, "lent free through the Internet Archive
via Open Library — genuine £0 cost, not a paywalled sample," and each per-module entry
confirms this individually (9 of 9 books say "book (borrowable...)"; the capstone score
says "public-domain score," not borrowable). That claim checks out against the artifact
as written. But "borrowable" is a real constraint, not a synonym for "owned": it means
free-to-read subject to Internet Archive's one-user-at-a-time lending queue and a
time-limited loan window, not free-to-keep. See Hidden costs below — this is the actual
risk on this path, not the £0 price tag.

### Time

Reading hours are taken verbatim from `resources.md`'s per-module coverage table
(15/12/10 pages-per-hour rates already applied there). Practice hours are taken
verbatim from `exercises.md`'s practice-load table (core figures, excluding the one
optional Module 10 stretch exercise). Assessment hours are computed by summing the
stated minutes of every check, cumulative review, and the final check in
`assessments.md` (not re-estimated).

| Module | Resource (reading) hrs | Practice hrs (core) | Assessment hrs | Module total | Curriculum budget (hrs) | Over/(under) |
|---|---|---|---|---|---|---|
| 1. Key Signatures, Circle of Fifths & Fluency | 2.6 | 1.0 | 0.50 (30 min) | 4.10 | 4 | +0.10 |
| 2. Intervals | 3.2 | 1.1 | 0.42 (25 min) | 4.72 | 4 | +0.72 |
| 3. Minor Scales & Relative/Parallel Keys | 2.9 | 1.1 | 0.42 (25 min) | 4.42 | 4 | +0.42 |
| — Cumulative review after Module 3 | — | — | 0.42 (25 min) | 0.42 | (not a module) | n/a |
| 4. Triad Construction & Quality | 3.3 | 1.9 | 0.42 (25 min) | 5.62 | 5 | +0.62 |
| 5. Primary Triads in a Key | 3.0 | 1.0 | 0.33 (20 min) | 4.33 | 3 | +1.33 |
| 6. Roman-Numeral & Lead-Sheet Analysis | 4.3 | 1.4 | 0.42 (25 min) | 6.12 | 5 | +1.12 |
| 7. Cadences | 1.5 | 0.75 | 0.33 (20 min) | 2.58 | 2 | +0.58 |
| 8. Seventh Chords & Extended Analysis | 3.0 | 1.1 | 0.33 (20 min) | 4.43 | 4 | +0.43 |
| 9. Phrase Structure & Musical Form | 3.3 | 1.4 | 0.42 (25 min) | 5.12 | 4 | +1.12 |
| — Cumulative review after Module 9 | — | — | 0.50 (30 min) | 0.50 | (not a module) | n/a |
| 10. Capstone: Full Analysis | 5.0 | 1.9 | 0.33 (20 min) | 7.23 | 5 | +2.23 |
| — Final check (4th fluency timing) | — | — | 0.17 (10 min) | 0.17 | (not a module) | n/a |
| **Total** | **32.1** | **12.65** (~12.7) | **5.00** (300 min) | **≈49.75** | **40** (module content) + **8** slack = **48** | **+1.75 (~3.6%)** |

**Arithmetic:**
- Reading: 2.6+3.2+2.9+3.3+3.0+4.3+1.5+3.0+3.3+5.0 = 32.1 hrs (matches `resources.md`'s
  own stated total).
- Practice (core): 1.0+1.1+1.1+1.9+1.0+1.4+0.75+1.1+1.4+1.9 = 12.65 hrs (`exercises.md`
  rounds this to "~12.7").
- Assessment: (30+25+25+25+20+25+20+20+25) module checks = 215 min, + (25+30) cumulative
  reviews = 55 min, + 20 min Module 10 check, + 10 min final fluency check = 300 min =
  5.00 hrs.
- Grand total: 32.1 + 12.65 + 5.00 = **49.75 hrs**.
- Available: 4 h/week × 12 weeks = **48 hrs** (`requirements.md`, `curriculum.md`).
- 49.75 − 48 = **+1.75 hrs over**, ≈3.6% above the available envelope.

**Where the overage lives.** Curriculum's own module-by-module hour budget sums to 40
hrs, leaving a stated 8-hour slack for the assessments' ~5-hour overhead. But summing
`resources.md` + `exercises.md` hours **per module** and comparing to the curriculum's
per-module caps shows 8 of the 10 modules already run over their own individual budget
before any assessment time is added (only Module 1 and Module 3 land at or under cap).
The worst three: **Module 10 (+2.23 hrs)**, **Module 5 (+1.33 hrs)**, **Modules 6 and 9
(+1.12 hrs each)**. Module 5's overage was flagged by the curator itself
("a tight fit... if it runs long, stop at the spelling drills"). Module 10's is the
largest and looks structural, not marginal: `resources.md` allocates the module's
**entire** 5-hour curriculum budget to "score study, chord-by-chord labelling, and
drafting the written analysis," while `exercises.md` separately budgets 1.9 core hours
of exercises that do the same thing (completing the chord labelling, writing the
capstone document) — the two artifacts appear to be costing the same work twice inside
one 5-hour slot. This artifact does not own either file and cannot resolve the
conflict; it is reported here as a finding for `validator`/the coordinator to route to
whichever step should reconcile it.

### Hidden costs

None of these appear as a cost line in `resources.md` because none of them are priced
resources — but a learner would resent hitting any of them unwarned, especially in a
later module when a loan queue or a printer bill shows up mid-path:

- **Internet Archive account required.** All 9 borrowed books need a free Internet
  Archive/Open Library account to borrow. Free to create, but it is a real setup step
  the learner has not been told about anywhere else in this run.
- **Lending queues.** Internet Archive's "borrowable" model is controlled digital
  lending — one copy checked out at a time per scanned edition. A popular, widely-used
  text like Kostka & Payne's *Tonal Harmony* (Module 8) or Piston's *Harmony* (used
  twice, Modules 5 and 7) is exactly the kind of book that can have a hold queue. A
  queued book stalls that module until a copy frees up — this is the real content of
  "borrowable is not free-to-keep."
- **Time-limited loans.** Internet Archive loans typically run on a 14-day checkout
  window (renewable if no one else is waiting). If a module runs long — and the Time
  table above shows most of them already do — the loan can expire mid-module, forcing a
  re-borrow (and possibly a new queue wait) to finish the assigned pages.
- **In-browser-only reading.** Many Internet Archive lending books can only be read in
  the browser reader while the loan is active, not downloaded as a file — the learner
  needs a working internet connection each time they read, not just at borrow time. Not
  verified live this run against current Internet Archive terms (see Open Questions);
  flagged as a general characteristic of the lending model, not a run-confirmed fact.
- **Printing.** Several exercises ask the learner to notate on staff paper (flashcards,
  triad drills, the capstone score annotations). No printer, ink, or paper cost appears
  anywhere in `resources.md`. Cost: unknown, not sourced this run.
- **Manuscript paper.** Free blank-staff PDFs exist online, but using them still means
  printing (cost above) or working in a notation app not currently in the resource
  list. Cost: unknown, not sourced this run.
- **A metronome.** `exercises.md` references metronome use directly (e.g. Module 1's
  fluency drill: "halve the tempo with a metronome, then raise it 5 bpm per successful
  pass"). No metronome is listed as a resource. Free smartphone/web metronome apps
  exist and would keep this at £0, but a learner who buys a physical metronome would be
  paying for something this path assumed they'd source themselves. Cost: unknown, not
  sourced this run.
- **Ongoing piano access.** The whole path assumes continuous access to a piano or
  keyboard — every exercise and check leans on "play it to check." `requirements.md`
  states the learner is already a beginner-intermediate pianist, so an instrument is
  reasonably assumed already owned; flagged here only because it is the largest
  hidden cost class if that assumption is wrong, and nothing in this run prices one.

### Free-only variant

There is no separate free-only variant to compute — **the path as designed already
costs £0**, since every one of the 13 resources in `resources.md` is either an
Internet-Archive loan or a public-domain download. Dropping "paid" resources loses
nothing, because there are none to drop.

What a **paid** alternative would buy, instead, is resilience against the hidden costs
above: purchasing the Kostka, Piston, or Benward texts outright (used copies of any of
these standard theory texts are commonly available secondhand) would remove the
lending-queue and 14-day-loan risk entirely, allow offline reading, and let the learner
annotate the book directly rather than working from a time-limited library scan. No
purchase price is given here because none was found in `resources.md` — inventing one
would violate this artifact's own rule against pricing anything not sourced this run;
see Open Questions.

## Sources

None. No currency conversion was required — the learner's budget is already stated in
GBP (`requirements.md`) and every cost in `resources.md` is `free`, so there was no rate
to apply or date to record.

## Open Questions

- **Assessment-hour total vs. `assessments.md`'s own rounded figure.** Summing every
  stated check/review/final-check duration in `assessments.md` gives exactly 300 minutes
  (5.00 hrs), but that artifact's own Summary rounds this to "approximately 5.5–6
  hours." This artifact used the line-item sum (5.00 hrs) because it is the figure
  reproducible from the rows shown above; the discrepancy with `assessments.md`'s
  rounded claim is noted here rather than silently resolved in either direction.
- **Module 10 double-booking.** As described under Time, `resources.md`'s Module 10 row
  and `exercises.md`'s Module 10 practice rows both appear to cost the same
  labelling/drafting work inside the curriculum's single 5-hour Module 10 slot. This
  artifact reports the conflict rather than resolving it, since it owns neither file.
- **Internet Archive lending terms (queue length, loan duration, in-browser-only
  restrictions).** Described from general knowledge of how Open Library/Internet
  Archive lending works, not from a source verified live during this run. If exact,
  current terms matter to the learner, they should be checked directly at
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
