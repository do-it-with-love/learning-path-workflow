---
artifact: validation-report
owner: validator
run_id: run-001-spanish-b1
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
generated: 2026-08-19T18:00:00Z
---

# Validation Report — Conversational European Spanish for Travel (attempt 3)

## Summary
**ALL GATES PASS.** No step needs re-running. `curator`'s third and final attempt fixed
gate G8 correctly this time: the element-level check that failed attempt 2 (four
LightSpeed own-site pages labeled `video` with an empty "Video for This Spanish Lesson"
heading over an audio-only player) has not been repeated — attempt 3 cites **zero**
LightSpeed own-site pages as `video`; the two remaining own-site citations are honestly
labeled `audio`, and I independently re-fetched both and confirmed the label is still
correct. The three resources swapped in to replace the mislabeled ones are genuine
YouTube-hosted videos; I judged them on credibility and correct classification (per this
run's tooling constraint that YouTube watch pages cannot be WebFetched) rather than
penalizing them for being unfetchable, and found nothing suspicious about any of the
three. Re-deriving G8 myself from the resource table module-by-module gives **20/27 =
74.07%** genuine video, a real 5-resource margin above the 70% floor (19/27 minimum). The
module-1 hours correction (~2.5h → ~1.667h) that the validator flagged at attempt 2 has
propagated correctly into `schedule.md` (weeks 1–3 now total 4.17h, not 4.99h) and was
already correct in `effort-budget.md`. The 40.07h (`schedule.md`) vs 40.00h
(`effort-budget.md`) gap is genuine display rounding (modules 5 and 9's ~220-min Mi Vida
Loca blocks shown as 3.70h vs. the unrounded 3.6667h), not a scope divergence, and at
89.93–90.00h of margin against the 130h horizon it has no bearing on any gate. All nine
gates re-derived independently below; no artifact is `BLOCKED`; all pass structural
checks.

## Findings

### G1 — Weekly hours ≤ 5h (+10% = 5.5h ceiling)
**PASS.** Re-summed all 26 of `schedule.md`'s weekly totals independently:
1.00+1.50+1.67+0.83+1.33+1.50+0.83+1.33+2.17+0.57+0.70+1.73+1.73+2.48+2.65+0.58+1.08+2.01
+0.50+0.92+1.75+0.92+1.42+2.68+3.02+3.17 = **40.07h**, matching `schedule.md`'s own
claimed grand total exactly. The heaviest week is week 26 at **3.17h**, a **2.33h
margin** under the 5.5h ceiling — the smallest margin anywhere in the path, unchanged
from attempts 1–2 (week 26 was not touched by this revision). Every other week has
≥2.35h of margin. Weeks 1–3 are the only rows that changed this attempt, dropping from
1.33/1.83/1.83h (attempt 2) to **1.00/1.50/1.67h**, confirming the module-1 hours
correction propagated correctly.

**Ruling on the 40.07h vs 40.00h discrepancy between `schedule.md` and
`effort-budget.md`.** Recomputed both independently. `schedule.md` displays modules 5
and 9's Mi Vida Loca compilation (~220 min) as **3.70h** each; the unrounded conversion
is 220÷60 = **3.6667h**, a 0.0333h/module difference, 0.0667h combined — plus a residual
~0.003h from module 1's 1.667h shown as 1.67h. That accounts for the full ~0.07h gap
(40.07 − 40.00 = 0.07). This is genuine display rounding, not a methodological or scope
divergence: both artifacts use the identical underlying resource-hour, practice-hour,
and assessment-hour figures, and neither is silently dropping or double-counting a
component. **Ruling: it does not matter.** With 89.93h (`schedule.md`) to 90.00h
(`effort-budget.md`) of margin against the 130h horizon (a ~69% slack either way), a
0.07h rounding artifact cannot flip any gate; I confirm this explicitly rather than
leaving it as an open question, since restating "does not matter" without checking the
arithmetic behind it would be exactly the kind of unverified total this role exists to
catch.

**Ruling on 17 of 27 `unknown`-duration resources contributing zero hours — reconfirmed.**
Recounted directly against the attempt-3 `resources.md` Coverage-check table:
M1×1, M2×2, M3×2, M4×4, M5×1, M6×2, M7×2, M8×2, M9×1 = **17 of 27**, agreeing exactly
across `resources.md`, `schedule.md`, and `effort-budget.md` (unchanged from attempt 2's
already-reconciled count; the three attempt-3 resource swaps each replaced one
`unknown`-duration citation with another `unknown`-duration citation, so this count could
not move). **G1 remains honestly evaluable on this basis**: the smallest margin in the
path (2.33h, week 26) comfortably absorbs `effort-budget.md`'s own generous illustrative
estimate for the unknowns (+6–8.5h spread over 26 weeks, well under 0.3h/week on
average). The 40.07h/40.00h totals are **floors**, not real totals — the gate passes on
margin, not on precision, exactly as at attempt 2.

### G2 — Total path length ≤ 26 weeks
**PASS.** `schedule.md`'s module→week table: 9+9+9+9+9+9+9+6+9 = 78 sessions ÷ 3
sessions/week = **26 weeks exactly**. 26 ≤ 26 (`horizon_weeks`). Unchanged from
attempts 1–2; `exercises.md`'s session counts were not revised this attempt.

### G3 — Total cost ≤ EUR 50
**PASS.** Recounted `resources.md`'s attempt-3 Findings and Sources sections: all
27 resource lines are marked `free`, including the three new attempt-3 citations
(the two LightSpeed YouTube swaps and the Señor Jordan swap) and the one relabeled
citation ("Podcast 16," `video`→`audio`, still `free`). 27 × EUR 0 = **EUR 0** vs
EUR 50 budget. `effort-budget.md` independently reproduces the same EUR 0 total,
line by line. Budget is specified, so the gate is not skipped; it clears with the
full EUR 50 unspent.

### G4 — No forward-referenced prerequisites; module 1 grounded in baseline-assessment.md
**PASS.** `curriculum.md` was not revised this attempt (still attempt 1). Re-checked
every module's `prerequisites` column: 2→{1}, 3→{1,2}, 4→{1,2,3}, 5→{1,2,3,4},
6→{1,2,3,4,5}, 7→{1,2,3,4}, 8→{1,2,3,4,5,6}, 9→{1–8} — every prerequisite number is
strictly less than its module number. Module 1's prerequisite is `baseline`, and
`baseline-assessment.md` asserts exactly that starting point (pre-A1).

### G5 — Outcome coverage; every module has ≥1 resource/exercise/assessment
**PASS.** `assessment-designer` ran (not in `skipped_steps`; `wants_assessments: true`
in `requirements.md`), so the assessment clause applies in full — no relaxation needed.
`curriculum.md`'s outcome-coverage table maps all 5 target outcomes from
`requirements.md` (checked against the retargeted strong-A2/B1-threshold goal, not the
original "B1" label, per the run's DATE NOTE/context) to ≥1 module. Re-checked all 9
modules against the attempt-3 `resources.md`: resource counts per module are
3,3,3,4,3,4,2,2,3 (all ≥1). `exercises.md` (unrevised): 3,3,3,3,4,3,3,3,4 exercises per
module (all ≥1). `assessments.md` (unrevised): one checkpoint per module plus cumulative
reviews after modules 3/6/9 and a final check (all ≥1). Every module clears all three
minimums.

### G6 — No resource URL repeated across modules
**PASS.** Scanned all 27 URLs in `resources.md`'s attempt-3 `## Sources` list for exact
duplicates. Mi Vida Loca (modules 1, 5, 9) uses three distinct URLs (Ep.1 watch page,
full-story compilation watch page, full-episode playlist). Dreaming Spanish (modules 5,
6, 9) uses three distinct playlist URLs (Superbeginner/Beginner/Intermediate).
Language Transfer (modules 1, 7, 8, 9) uses four distinct track URLs. The three
attempt-3 replacement citations (LightSpeed "Reflexive Verbs," LightSpeed "Prepositions,"
Señor Jordan "Unequal Comparisons") are each new, distinct URLs not used elsewhere. No
two resource lines share a URL.

### G7 — Every resource verified this run, and reachable
**PASS.** Every one of the 27 lines in `resources.md`'s `## Sources` list carries a
`verified:` marker dated 2026-08-18 or 2026-08-19 — both from this run (run began
2026-08-18, per the run's DATE NOTE). Method breakdown: `webfetch` for the four
non-YouTube citations reachable by fetch (two LightSpeed own-site audio pages,
SpanishDict, Rick Steves), `websearch` for all 23 YouTube-hosted citations (per this
run's explicit tooling guidance: YouTube watch/playlist pages cannot be WebFetched
without tripping a consent-wall loop, so WebSearch confirming title and URL is the
sanctioned verification method).

I independently re-fetched a 4-URL sample this attempt (all fetchable, per the run's
sampling instruction to avoid youtube.com watch pages): both remaining LightSpeed
own-site citations (module 3's "Podcast 16," module 6's "How to Order Food"), the
SpanishDict comparatives article (module 6), and Señor Jordan's own site (companion
context for module 6's new YouTube citation). All four are live, free, and on-topic —
see Link sample below. I could not independently WebSearch-verify the 23 YouTube
citations (no WebSearch tool available to me in this session), so I instead judged them
on credibility: video IDs and titles follow the same naming conventions as citations
already WebFetch-confirmed in earlier attempts (LightSpeed's own numbered-lesson scheme,
e.g. "58 Beginners Spanish ¿Qué vs Cuál?," "47 Easily Learn Spanish... VOSOTROS
ESTÁIS"), the three new swaps are attributed to identifiable existing channels
(LightSpeed Spanish, Señor Jordan — the latter's own site independently confirmed real
and active by my WebFetch above), and no citation in this artifact was written without a
`verified:` marker naming a method and this run's date. This is a real limitation
recorded under Open Questions, not a basis for failing the gate, per this dispatch's
explicit instruction not to fail YouTube citations for being unfetchable in this
environment.

### G8 — ≥70% of resources match preferred modality (video)
**PASS.** Re-derived the video/non-video split module by module directly from
`resources.md`'s Findings section (not accepted from its own Coverage-check table),
cross-checked against the attempt-2 failure's four specific mislabeled pages:

| Module | Resources | Video | Audio | Text | Notes |
|---|---|---|---|---|---|
| 1 | 3 | 2 | 1 | 0 | LT Track 1 = audio |
| 2 | 3 | 3 | 0 | 0 | all YouTube |
| 3 | 3 | 2 | 1 | 0 | "Podcast 16" honestly relabeled `audio`, kept — no own-site video claimed |
| 4 | 4 | 4 | 0 | 0 | "Reflexive Verbs" (YouTube) replaces the audio-only "Podcast 17" |
| 5 | 3 | 3 | 0 | 0 | "Prepositions" (YouTube) replaces the audio-only "Directions in Spanish" |
| 6 | 4 | 2 | 1 | 1 | "Unequal Comparisons" (Señor Jordan, YouTube) replaces the audio-only "Making Comparisons"; "How to Order Food" stays `audio` (correct since attempt 2); SpanishDict stays `text` |
| 7 | 2 | 1 | 1 | 0 | LT Track 58 = audio |
| 8 | 2 | 1 | 1 | 0 | LT Track 7 = audio |
| 9 | 3 | 2 | 1 | 0 | LT Track 90 = audio |
| **Total** | **27** | **20** | **6** | **1** | |

**20/27 = 74.07%**, clearing the 70% floor (19/27 minimum) by a genuine one-resource
margin, matching `resources.md`'s own claim exactly (unlike attempt 2, whose 77.8%
claim did not survive re-derivation).

**Re-audit of LightSpeed own-site pages, confirmed via independent WebFetch this
attempt (see Link sample):** the two own-site citations remaining in this artifact
(module 3's "Podcast 16," module 6's "How to Order Food") are both labeled `audio` in
`resources.md`, and both are still, independently, audio-only on re-fetch — no
"Video for This Spanish Lesson" heading at all on the order-food page, and an empty one
on the podcast-16 page, exactly as `resources.md` describes. **No LightSpeed own-site
page in this artifact is labeled `video`.** The domain-wide failure mode that caused
attempts 1–2 to fail G8 cannot recur in this artifact as currently written, because the
artifact no longer makes the claim that caused it.

**Judgment on the three new YouTube citations, per this dispatch's explicit
instruction:** a YouTube-hosted video is video by construction (YouTube does not host
audio-only content as its primary format), so the open question is credibility and
topical correctness, not modality. All three (module 4's "Spanish Lesson Early Inter 6
Reflexive Verbs," module 5's "Spanish Lesson 35 Abs Beginner Spanish Prepositions,"
module 6's Señor Jordan "Unequal Comparisons (part 1)") carry specific, plausible
titles matching their module's objective, attributed to identifiable, previously-verified
channels, each cross-referenced against a companion page (two LightSpeed own-site pages,
one Señor Jordan's own site) that I or the curator independently WebFetched. Nothing in
this sample contradicts the classification. I did not find grounds to reclassify any of
the three.

### G9 — No module more than one level above the assessed baseline
**PASS, under the same recorded interpretation as attempts 1–2.** `curriculum.md` was
not revised this attempt, so the reasoning is unchanged: read literally against the
single fixed pre-A1 baseline, "one level above baseline" would cap every module at A1,
making the confirmed A2/B1-threshold target (itself a deliberate, user-confirmed
retargeting from certified B1, per `requirements.md`) structurally unreachable and
putting G9 in direct conflict with G2 and G5. I again read G9 as a step-wise pacing
check against fine-grained CEFR sub-levels (A1.1→A1.2→A1.3→A2.1→A2.2→A2.3→
B1-threshold), under which every module advances exactly one sub-step from its
predecessor. No module skips a sub-level under this reading. Flagging again, as in
attempts 1–2, that `gates.md`'s G9 wording is worth tightening at the source so future
runs don't need a re-derived interpretation — this is now a three-time-repeated
observation, not a new one.

### Structural checks

| Artifact | Frontmatter (7 keys) ok | Owner matches pipeline.json | Sections ok (4, in order, non-empty) | Inputs exist | Citations ok |
|---|---|---|---|---|---|
| requirements.md | yes | yes (`requirements-formalizer`) | yes | n/a | n/a (`Sources: None.`) |
| baseline-assessment.md | yes | yes (`knowledge-assessor`) | yes | yes | yes (4 Wikipedia citations, `verified: mcp:wikipedia 2026-08-18`) |
| curriculum.md | yes | yes (`curriculum-architect`) | yes | yes | yes (5 Wikipedia citations, `verified: mcp:wikipedia 2026-08-18`) |
| resources.md (attempt 3) | yes | yes (`curator`, video-curator variant) | yes | yes | yes — all 27 lines carry a `verified:` method + this-run date; no line labeled `video` fails on re-audit |
| exercises.md | yes | yes (`exercise-designer`) | yes | yes | `Sources: None.` — exempt |
| assessments.md | yes | yes (`assessment-designer`) | yes | yes | `Sources: None.` — exempt |
| schedule.md (attempt 3) | yes | yes (`schedule-planner`) | yes | yes | `Sources: None.` — exempt |
| effort-budget.md (attempt 3) | yes | yes (`effort-budget-aggregator`) | yes | yes | `Sources: None.` — exempt |

No artifact is `BLOCKED`. No structural failures. No content failures remain anywhere.

### Link sample

| URL | Method | Result |
|---|---|---|
| https://lightspeedspanish.co.uk/beginners/beginners-spanish-podcast-16-spanish-question-words/ | webfetch | Live, free, on-topic (question words); "Video of This Spanish Lesson" heading present but empty — no player/iframe; only an MP3 audio player under "Audio for This Spanish Lesson." Confirms `resources.md`'s `audio` label is correct. |
| https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lesson-3-how-to-order-food-in-spanish-restaurant/ | webfetch | Live, free, on-topic (ordering food in a restaurant); no video heading at all, only an MP3 audio player. Confirms `resources.md`'s `audio` label is correct. |
| https://www.spanishdict.com/guide/make-comparisons-in-spanish | webfetch | Live, free, on-topic (más/menos...que and tan...como comparatives). Confirms `resources.md`'s `text` label. |
| https://senorjordan.com | webfetch | Live, free, genuine independent Spanish-teaching site by an identifiable instructor (teaching since 2006, Truman State University); confirms the channel behind module 6's new YouTube citation is a real, active creator, though the homepage excerpt fetched did not itself show the specific "Unequal Comparisons" lesson (expected — that content is catalogued under `/los-videos/`, not the homepage, and the cited resource is the YouTube video, not this page). |

## Sources
- [Beginners Spanish Podcast 16: Spanish Question Words](https://lightspeedspanish.co.uk/beginners/beginners-spanish-podcast-16-spanish-question-words/) — LightSpeed Spanish · verified: webfetch 2026-08-19 (free, on-topic, reachable; audio-only, confirming `resources.md`'s label)
- [How to Order Food in Spanish | Restaurants](https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lesson-3-how-to-order-food-in-spanish-restaurant/) — LightSpeed Spanish · verified: webfetch 2026-08-19 (free, on-topic, reachable; audio-only, confirming `resources.md`'s label)
- [Make Comparisons in Spanish — SpanishDict Grammar Guide](https://www.spanishdict.com/guide/make-comparisons-in-spanish) — SpanishDict · verified: webfetch 2026-08-19 (free, on-topic, reachable, text)
- [Señor Jordan](https://senorjordan.com) — Señor Jordan · verified: webfetch 2026-08-19 (free, live, genuine instructor site; companion context for module 6's YouTube citation, not itself a cited resource)
- `.claude/workflow/gates.md`, `runs/run-001-spanish-b1/artifacts/validation-report.md` (attempts 1–2) — read directly for gate definitions and prior findings.

## Open Questions
- **YouTube citations could not be independently re-verified by WebSearch this
  attempt** — no WebSearch tool was available in this session, only WebFetch (which
  cannot reach youtube.com watch/playlist pages per this run's known tooling
  constraint) and Read/Write/Skill. I judged the 23 YouTube-hosted citations (including
  the three newly added this attempt) on credibility — naming conventions, channel
  attribution, and companion-page cross-references — rather than independently
  reproducing the curator's WebSearch confirmation. This is a genuine limit on how far
  this validation could go, consistent with the run's explicit instruction not to fail
  a YouTube citation for being unfetchable in this environment. If a future attempt has
  WebSearch available, re-confirming the three newest citations (module 4's "Reflexive
  Verbs," module 5's "Prepositions," module 6's "Unequal Comparisons") directly would
  close this gap.
- **Module 5's ~3.7h resource-hour figure still looks like it over-counts the Mi Vida
  Loca compilation** — unchanged from attempts 1–2, and not a gate failure. `resources.md`
  directs the learner to watch only Episode 3 (~10 min) of the 22-episode/~220-min
  compilation for module 5's directions/transport objective, but the Coverage-check
  table counts the full compilation length toward module 5's hours. Correcting this
  would only *increase* every week's margin in weeks 13–15, so it cannot be the basis
  of a gate failure; flagged again for `curator`'s awareness since the run is otherwise
  passing.
- **G9's wording remains genuinely ambiguous**, as flagged in attempts 1 and 2; not
  re-litigated in full here since `curriculum.md` did not change. Recommend the
  coordinator/user consider tightening `gates.md`'s G9 text at the source now that the
  run is complete, so a future run does not need a re-derived interpretation.
- **`assessments.md`'s "~325 minutes" vs. its own itemised 330-minute total** — unchanged
  across all three attempts, a self-contained ~1.5% rounding slip in prose only, does not
  affect any gate.
- **Module 8 remains the weakest-covered module** by `resources.md`'s own disclosure (one
  audio Language Transfer track plus one region-mixed Rick Steves video) — not a gate
  failure (module 8 has 2 resources, 1 video, clearing every per-module minimum and not
  the constraint on the path's 70% G8 floor), but worth the user's awareness if they
  revisit this path later.
