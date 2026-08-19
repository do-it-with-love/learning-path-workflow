---
artifact: validation-report
owner: validator
run_id: run-001-spanish-b1
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
generated: 2026-08-19T00:00:00Z
---

# Validation Report — Conversational European Spanish for Travel (attempt 2)

## Summary
**1 GATE(S) FAILED — G8, owner: `curator`.** Re-run `curator` (video-curator variant) a
third time. Attempt 2 correctly fixed G7 (the dead "Perfecting the Prepositions" citation
is now a real, reachable, free resource) but its G8 fix was built on an insufficiently
rigorous check: four LightSpeed own-site lessons labeled `video` this attempt — including
both of the two new citations added specifically to raise the video ratio — have a "Video
for This Spanish Lesson" heading with **no video element under it at all**, only an audio
player. Re-deriving the ratio with these four corrected to `audio` gives **17/27 = 62.96%**
genuine video, below the 70% floor and *worse* than attempt 1's already-failing 69.2%.
Because `curator` is already at attempt 2 of 3, this is its final retry; the finding is
reported exactly as derived, not softened. `schedule.md` and `effort-budget.md` (both
attempt 2, correctly re-run because they depend on `resources.md`) do not themselves need
further correction from anything found here beyond what a `curator` re-run will again
cascade to them. G1–G7 and G9 pass, with two judgement calls recorded in G1 and G9 below.
No artifact is `BLOCKED`; all pass structural checks.

## Findings

### G1 — Weekly hours ≤ 5h (+10% = 5.5h ceiling)
**PASS**, independently re-derived from `schedule.md`'s 26 weekly totals: 1.33+1.83+1.83
+0.83+1.33+1.50+0.83+1.33+2.17+0.57+0.70+1.73+1.73+2.48+2.65+0.58+1.08+2.01+0.50+0.92+1.75
+0.92+1.42+2.68+3.02+3.17 = **40.89h**, matching `schedule.md`'s own claimed "~40.89
(component sum 40.90)." The heaviest week is week 26 at 3.17h — a **2.33h margin** under
the 5.5h ceiling, the smallest margin anywhere in the path; every other week has ≥2.48h of
margin. G1 passes with large margin.

**Ruling on the coordinator's first flagged item — the resources.md module-1 subtotal.**
Verified: `resources.md`'s Coverage-check table states module 1's resource hours as
"~2.5h," but module 1's three citation lines sum to 1.5h (playlist, "est.") + 10 min Mi
Vida Loca Ep.1 (0.167h) = **1.667h**, not 2.5h — a genuine arithmetic error (most likely a
units slip treating "10 min" as "1.0h"), unchanged from attempt 1 and still uncaught by
`curator`. `effort-budget.md` correctly recomputed bottom-up and used 1.667h; `schedule.md`
did not — it explicitly says it takes "resources.md's own 'Approx. resource hours' figures
per module" and its week 1–3 total for module 1 (1.33+1.83+1.83 = 4.99 ≈ 5.00h) reflects
the wrong 2.50h, not the correct 1.667h. This makes `schedule.md`'s 40.90h and
`effort-budget.md`'s 40.00h **two different totals for the same run, 0.90h apart, from the
same root cause**. **Ruling: this is a reporting defect, not a G1 gate failure.** Correcting
it can only *lower* weeks 1–3 by roughly 0.83h spread across three weeks (~0.28h/week);
those weeks currently run at 1.33–1.83h against a 5.5h ceiling, so the correction moves them
further from breach, never closer. A bug that can only widen an already-large margin cannot
be the basis of a gate failure. It is, however, a real data-quality defect that should be
fixed at its source: `resources.md`'s Coverage-check table (owner `curator`), so that
`schedule.md` (which trusted that table) and `effort-budget.md` (which had to work around
it) stop disagreeing on the path's total hours.
fix: `curator` corrects module 1's Coverage-check row from "~2.5h" to "~1.667h" (or states
the two components separately) on its next revision; `schedule-planner` should then take
its module totals from the same bottom-up arithmetic `effort-budget-aggregator` already
uses, not the summary row, to stop the two aggregator artifacts diverging.

**Ruling on the coordinator's second flagged item — 17 of 27 `unknown`-duration resources
contributing zero hours.** Recounted directly against `resources.md`: M1×1, M2×2, M3×2,
M4×4, M5×1, M6×2, M7×2, M8×2, M9×1 = **17 of 27**, which now agrees exactly across
`resources.md`, `schedule.md`, and `effort-budget.md` (a genuine improvement — attempt 1
had three different counts across three artifacts). **G1 can be honestly evaluated on this
basis**, for the same reason as attempt 1: the smallest margin in the path (2.33h, week 26)
comfortably absorbs `effort-budget.md`'s own generous illustrative estimate for the
unknowns (+6–8.5h spread over 26 weeks, well under 0.3h/week on average), and the two
resources with real quantified bulk (~3.67h Mi Vida Loca blocks in modules 5 and 9) are
already counted, not hidden in the unknown pool. The caveat is worth restating precisely
because it is large in count (63% of all resources): `schedule.md`'s 40.90h /
`effort-budget.md`'s 40.00h totals are **floors**, not real totals, and the gate passes on
margin, not on precision.

### G2 — Total path length ≤ 26 weeks
**PASS.** `schedule.md`'s module→week table: 9+9+9+9+9+9+9+6+9 = 78 sessions ÷ 3
sessions/week = 26 weeks exactly. 26 ≤ 26 (`horizon_weeks`). Unchanged from attempt 1;
`exercises.md`'s session counts were not revised this attempt.

### G3 — Total cost ≤ EUR 50
**PASS.** Recounted `resources.md`: all 27 resource lines (26 unchanged + 1 net new) are
marked `free`. 27 × EUR 0 = **EUR 0** vs EUR 50 budget. Budget is specified, so the gate is
not skipped; it clears with the full EUR 50 unspent.

### G4 — No forward-referenced prerequisites; module 1 grounded in baseline-assessment.md
**PASS.** `curriculum.md` was not revised this attempt. Re-checked every module's
`prerequisites` column: 2→{1}, 3→{1,2}, 4→{1,2,3}, 5→{1,2,3,4}, 6→{1,2,3,4,5},
7→{1,2,3,4}, 8→{1,2,3,4,5,6}, 9→{1–8} — every prerequisite number is strictly less than
its module number. Module 1's prerequisite is `baseline`, and `baseline-assessment.md`
asserts exactly that starting point (pre-A1).

### G5 — Outcome coverage; every module has ≥1 resource/exercise/assessment
**PASS.** `assessment-designer` ran (not in `skipped_steps`; `wants_assessments: true`), so
the assessment clause applies in full. `curriculum.md`'s outcome-coverage table maps all 5
target outcomes from `requirements.md` to ≥1 module (unchanged). Re-checked all 9 modules
against the revised `resources.md`: resource counts per module are now 3,3,3,4,3,4,2,2,3
(all ≥1, module 8 still the floor at 2). `exercises.md` (unrevised): 3,3,3,3,4,3,3,3,4
exercises per module. `assessments.md` (unrevised): one checkpoint per module plus
cumulative reviews after 3/6/9 and a final check. All ≥1 in every category, every module.

### G6 — No resource URL repeated across modules
**PASS.** Scanned all 27 URLs in `resources.md`'s `## Sources` list for exact duplicates.
BBC Mi Vida Loca (modules 1, 5, 9) uses three distinct URLs (Ep.1 watch page, full-story
compilation watch page, full-episode playlist). Dreaming Spanish (modules 5, 6, 9) uses
three distinct playlist URLs (Superbeginner/Beginner/Intermediate). Language Transfer
(modules 1, 7, 8, 9) uses four distinct track URLs. The two attempt-2 additions
("Directions in Spanish," "Making Comparisons in Spanish") are both new, distinct URLs not
used elsewhere. No two resource lines share a URL.

### G7 — Every resource verified this run, and reachable
**PASS** — the attempt-1 failure is fixed. Every one of the 27 lines in `resources.md`
carries a `verified:` marker dated 2026-08-18 or 2026-08-19, both from this run (run began
2026-08-18; see the run's DATE NOTE). The dead "Perfecting the Prepositions in Spanish"
citation (module 5) that failed G7 last time has been removed; its replacement, "Directions
in Spanish," was WebFetched this pass and confirmed **live, free, and on-topic** (prepositions
of place / direction-giving) — see the Link sample below. I re-verified reachability on all
sampled URLs (module 5's new citation, module 6's new citation, module 4's reclassified
citation, and module 3's citation) and all resolve to real, free, on-topic LightSpeed
Spanish lesson pages. No dead or paywalled link was found anywhere in the sample.

**Important cross-reference to G8, not a G7 failure in itself:** the same detailed WebFetch
inspection that confirmed reachability also found that four of these pages' `video` format
label is wrong (no video element exists on the page — see G8). G7 tests *existence and
reachability, verified this run*, which these four resources satisfy: they are real, free,
on-topic pages. The *format* claim inside the citation is inaccurate, which is a modality
(G8), not existence (G7), problem, consistent with how this run's attempt-1 report treated
an equivalent finding for "How to Order Food in Spanish."

### G8 — ≥70% of resources match preferred modality (video)
**FAIL** — owner: `curator`. Worse than attempt 1.

`resources.md` claims **21/27 (77.8%)** video. I independently re-verified every resource
labeled `video` that sits on LightSpeed Spanish's own site (as opposed to YouTube, where the
video element is unambiguous) by WebFetching each page and explicitly listing every
`<video>`/`<iframe>`/embed element present, not just reading the page's own section
headings. Four resources fail this check — each has a "Video for This Spanish Lesson"
heading with **nothing beneath it**: no iframe, no video tag, no paywall notice, just an
empty section, while a fully-populated MP3 audio player sits under the adjacent "Audio for
This Spanish Lesson" heading on the same page. This pattern was confirmed **independently
and consistently across all four pages**, including a second, more detailed re-fetch of
each:

| Module | Resource | Curator's label | What the page actually contains |
|---|---|---|---|
| 3 | Beginners Spanish Podcast 16: Spanish Question Words | `video` (bold, unhedged) | "Video for This Spanish Lesson" heading, empty; only an MP3 audio player (`Podcast_16_Questioning_words.mp3`) |
| 4 | Free Spanish Podcast 17: Daily Routine | `video` (bold, unhedged; reclassified *to* video this attempt) | Same empty video heading; only an MP3 audio player (`Podcast_17_Daily_Routine`) |
| 5 | Directions in Spanish | `video` (new citation this attempt, replacing the dead G7 resource) | Same empty video heading; only an MP3 audio player (`Podcast_4_Directions.mp3`) |
| 6 | Making Comparisons in Spanish | `video` (new citation this attempt, added specifically to raise the G8 ratio) | Same empty video heading; only an MP3 audio player (`Podcast_24_comparatives.mp3`) |

All four are reclassified `video → audio` for gate purposes (they remain valid, free,
on-topic resources — this is a modality miscount, not a reachability problem). Recomputing:

| Classification | Count |
|---|---|
| Genuine video (YouTube videos/playlists + ricksteves.com, independently confirmed as real video previously and again where re-sampled) | **17** |
| Audio (4 SoundCloud Language Transfer tracks + "How to Order Food" [already correctly labeled] + the 4 reclassified LightSpeed pages above) | **9** |
| Text | **1** (SpanishDict) |
| **Total** | **27** |

**17/27 = 62.96%**, below the 70% floor, and below attempt 1's already-failing 69.2%. The
two citations added *specifically* to fix G8 this attempt (Directions, Making Comparisons)
are both actually audio, and one of the two reclassifications the curator made in the
opposite direction (Podcast 17: audio → video) was also wrong — it is audio, as it was
originally, just with the "confirmed" duration correctly walked back to `unknown`. Only one
of the curator's four format changes this attempt (How to Order Food: video/podcast →
audio) was correct.
— owner: `curator`
fix: Before labeling any LightSpeed own-site lesson `video`, WebFetch the page and check for
an actual video/iframe/embed element under the "Video for This Spanish Lesson" heading, not
just the heading's presence — this heading appears to be a standing template element on
LightSpeed's site that is frequently unpopulated. Relabel modules 3, 4, 5, and 6's four
affected lines to `audio`. To clear the 70% floor, the path needs **≥19 of 27** genuine
video resources (currently 17); source at least 2 net additional genuine video resources —
YouTube-hosted LightSpeed content has been reliable in this audit (every YouTube-hosted
citation checked, this attempt and last, had a real video) — prioritising modules 3, 4, 5,
and 6, which each lost their only or a key video credit in this correction.

### G9 — No module more than one level above the assessed baseline
**PASS, under the same recorded interpretation as attempt 1.** `curriculum.md` was not
revised this attempt, so the reasoning is unchanged: read literally against the single
fixed pre-A1 baseline, "one level above baseline" would cap every module at A1, making the
confirmed A2/B1-threshold target structurally unreachable and putting G9 in direct conflict
with G2 and G5 for any similarly-staged learner. I again read G9 as a step-wise pacing
check against fine-grained CEFR sub-levels (A1.1→A1.2→A1.3→A2.1→A2.2→A2.3→B1-threshold),
under which every module advances exactly one sub-step from its predecessor (e.g. module 3
ends A1.3, module 4 spans A1.3→A2.1). No module skips a sub-level. This remains a
judgement call, not a relaxation — flagging again, as last time, that `gates.md`'s G9
wording is worth tightening at the source so future runs don't need a re-derived
interpretation.

### Structural checks

| Artifact | Frontmatter (7 keys) ok | Owner matches pipeline.json | Sections ok (4, in order, non-empty) | Inputs exist | Citations ok |
|---|---|---|---|---|---|
| requirements.md | yes | yes (`requirements-formalizer`) | yes | n/a | n/a (`Sources: None.`) |
| baseline-assessment.md | yes | yes (`knowledge-assessor`) | yes | yes | yes (4 Wikipedia citations, `verified: mcp:wikipedia 2026-08-18`) |
| curriculum.md | yes | yes (`curriculum-architect`) | yes | yes | yes (5 Wikipedia citations, `verified: mcp:wikipedia 2026-08-18`) |
| resources.md (attempt 2) | yes | yes (`curator`, video-curator variant) | yes | yes | format ok on all 27 lines' structure; **4 of 27 fail content-verification on format (G8 above)** |
| exercises.md | yes | yes (`exercise-designer`) | yes | yes | `Sources: None.` — exempt |
| assessments.md | yes | yes (`assessment-designer`) | yes | yes | `Sources: None.` — exempt |
| schedule.md (attempt 2) | yes | yes (`schedule-planner`) | yes | yes | `Sources: None.` — exempt |
| effort-budget.md (attempt 2) | yes | yes (`effort-budget-aggregator`) | yes | yes | `Sources: None.` — exempt |

No artifact is `BLOCKED`. No structural failures. All content failures are confined to
`resources.md` (G8 only — G7 now passes).

### Link sample

| URL | Method | Result |
|---|---|---|
| https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lessons-4-directions/ | webfetch (×2, incl. element-level re-check) | Live, free, on-topic (directions/prepositions) — **but "Video for This Spanish Lesson" heading is empty; only an MP3 audio player present** — G8 reclassification |
| https://lightspeedspanish.co.uk/20131208-early-intermediate-spanish-podcast-24-making-comparisons-in-spanish/ | webfetch (×2, incl. element-level re-check) | Live, free, on-topic (comparatives) — **same empty video heading; audio only** — G8 reclassification |
| https://lightspeedspanish.co.uk/20111231-free-spanish-podcast-17-daily-routine/ | webfetch (×2, incl. element-level re-check) | Live, free, on-topic (daily routine) — **same empty video heading; audio only** — G8 reclassification |
| https://lightspeedspanish.co.uk/beginners/beginners-spanish-podcast-16-spanish-question-words/ | webfetch (×3, incl. element-level and paywall re-checks) | Live, free, on-topic (question words) — **same empty video heading; audio only, no paywall found either** — G8 reclassification |

### Attempt-1 → attempt-2 delta, for the coordinator
- G7: **FAIL → PASS.** Dead "Perfecting the Prepositions" citation removed and replaced
  with a real, free, reachable resource ("Directions in Spanish").
- G8: **FAIL → still FAIL**, and the underlying number got worse (claimed fix: 69.2% →
  claimed 77.8%; re-derived actual: 69.2% → **62.96%**). The two resources added
  specifically to fix G8 are both misclassified, and one of two reclassifications made in
  the curator's own audit went the wrong way.
- G1, G2, G3, G4, G5, G6, G9: unchanged verdicts (all PASS), re-derived independently this
  attempt rather than assumed.

## Sources
- [Directions in Spanish](https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lessons-4-directions/) — LightSpeed Spanish · verified: webfetch 2026-08-19 (free, on-topic, reachable; video heading empty, audio-only)
- [Making Comparisons in Spanish](https://lightspeedspanish.co.uk/20131208-early-intermediate-spanish-podcast-24-making-comparisons-in-spanish/) — LightSpeed Spanish · verified: webfetch 2026-08-19 (free, on-topic, reachable; video heading empty, audio-only)
- [Free Spanish Podcast 17: Daily Routine](https://lightspeedspanish.co.uk/20111231-free-spanish-podcast-17-daily-routine/) — LightSpeed Spanish · verified: webfetch 2026-08-19 (free, on-topic, reachable; video heading empty, audio-only)
- [Beginners Spanish Podcast 16: Spanish Question Words](https://lightspeedspanish.co.uk/beginners/beginners-spanish-podcast-16-spanish-question-words/) — LightSpeed Spanish · verified: webfetch 2026-08-19 (free, on-topic, reachable; video heading empty, audio-only)
- `.claude/workflow/gates.md`, `runs/run-001-spanish-b1/artifacts/validation-report.md` (attempt 1) — read directly for gate definitions and prior findings.

## Open Questions
- **Is LightSpeed's "Video for This Spanish Lesson" heading ever populated?** All four
  pages sampled this attempt had it empty. If LightSpeed does ship real video on some
  lessons (e.g. behind a login this tool cannot exercise, or via a JS-lazy-loaded embed
  this tool's fetch does not execute — the same limitation already noted for duration
  data), that would change the correct classification back toward `video` for some of
  these four. I could not distinguish "genuinely no video" from "video hidden behind JS
  this tool can't run" with certainty, though the consistent, total absence of any
  iframe/embed reference in the raw fetched markup (as opposed to a player shell with
  "0:00/0:00," as seen for audio) is stronger evidence of true absence than of a rendering
  gap. Recommend `curator` cross-check by any means that can execute the page's JS (a real
  browser fetch) before its next revision, in case the reclassification should be reversed.
- **G9's wording remains genuinely ambiguous**, as flagged in the attempt-1 report; not
  re-litigated in full here since `curriculum.md` did not change. Recommend the
  coordinator/user consider tightening `gates.md`'s G9 text at the source.
- **`assessments.md`'s "~325 minutes" vs. its own itemised 330-minute total** — unchanged,
  self-contained ~1.5% rounding slip in prose only, noted in attempt 1, does not affect any
  gate.
- **`resources.md`'s module-1 Coverage-check subtotal (~2.5h vs. the reproducible 1.667h)**
  — ruled a reporting defect, not a G1 failure, with full reasoning under G1 above; still
  worth `curator` fixing on the next pass since it is the source of a 0.90h disagreement
  between `schedule.md`'s and `effort-budget.md`'s grand totals.
- **SoundCloud citations (4 Language Transfer tracks) still could not be fully verified by
  WebFetch** — page/title existence confirmed, actual audio streaming not, a tooling
  limitation carried over from attempt 1, not a finding against the resources.
