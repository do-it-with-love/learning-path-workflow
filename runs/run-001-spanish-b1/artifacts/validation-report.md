---
artifact: validation-report
owner: validator
run_id: run-001-spanish-b1
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

# Validation Report — Conversational European Spanish for Travel

## Summary
2 GATE(S) FAILED — G7 and G8, both owned by `curator` (video-curator variant). Re-run
`curator` to (a) replace or fix the module 5 "Perfecting the Prepositions in Spanish"
citation, which resolves to a paid workbook promotion page rather than the claimed free
video/podcast lesson, and (b) restore the video-modality ratio to ≥70% after correctly
reclassifying two resources that were counted as video but are not. Because
`schedule-planner` and `effort-budget-aggregator` both depend on `curator`'s artifact,
they will need to re-run after the curator fix even though neither is independently at
fault. G1–G6 and G9 pass; G9 required a judgement call on gate wording, recorded below.
All artifacts pass structural checks. No artifact is `BLOCKED`.

## Findings

### G1 — Weekly hours ≤ 5h (+10% = 5.5h ceiling)
**PASS**, independently re-derived. Summed `schedule.md`'s 26 weekly totals myself:
1.33+1.83+1.83+0.83+1.33+1.50+0.83+1.33+2.17+0.57+0.90+1.73+1.73+2.48+2.65+0.58+1.08+2.01
+0.50+0.92+1.75+0.92+1.42+2.68+3.02+3.17 = **41.09h** (schedule.md reports 41.09–41.10,
consistent). The heaviest week is week 26 at 3.17h, 2.33h under the 5.5h ceiling; no week
comes close. G1 passes with large margin.

**Data-quality caveat, investigated per the task's instruction 1.** `effort-budget.md`
states "14 of 26 resources ... have `unknown` individual durations." I counted the
literal `unknown` duration fields in `resources.md` myself: Track 1 (M1); SER/ESTAR #42,
VOSOTROS ESTÁIS #47 (M2); Podcast 16, ¿Qué vs Cuál? #58 (M3); Tell Time #14, Gustar #44,
Listening Test #30 (M4); **Perfecting the Prepositions (M5)**; How to Order Food (M6);
Gordon's Diaries Preterite, Track 58 (M7); Track 7, Rick Steves (M8); Track 90 (M9) — **15
resources**, not 14. `effort-budget.md`'s own itemised breakdown ("modules 1, 2×2, 3×2,
4×3, 6×1, 7×2, 8×2, 9×1" = 14) omits module 5's "Perfecting the Prepositions," which
`resources.md` itself marks `unknown`. This is an arithmetic/count error — attributable
to `effort-budget-aggregator` — but it does **not** change the module-hour floor totals
(12.35h resource / 41.10h grand total), because those totals already treated all unknowns,
including module 5's, as contributing 0. **Judgement: G1 can be honestly evaluated and
should remain PASS, not BLOCKED.** The margins are large enough (smallest weekly margin
against the 5.5h ceiling is 2.33h, week 26; most weeks have 3.5–4.9h of margin) that even
`effort-budget.md`'s own generous illustrative estimate for the unknowns (+5–7h spread
across the whole 26-week path, i.e. well under 0.3h/week on average) could not push any
single week over budget. `gates.md`'s BLOCKED condition is for a missing input artifact,
not incomplete data within one that exists — this is a real data-quality gap worth fixing,
but not one that prevents an honest PASS verdict here.
fix: `effort-budget-aggregator` should correct "14 of 26" to "15 of 26" (and its module
breakdown) on next revision; not gate-blocking on its own.

### G2 — Total path length ≤ 26 weeks
**PASS.** `schedule.md`'s module→week table sums to 9+9+9+9+9+9+9+6+9 = 78 sessions ÷ 3
sessions/week = 26 weeks exactly. 26 ≤ 26 (`horizon_weeks`). No slack, but not exceeded.

### G3 — Total cost ≤ EUR 50
**PASS.** Recounted `resources.md`: all 26 resource lines are marked `free`. 26 × EUR 0 =
**EUR 0** vs EUR 50 budget. Budget is specified (EUR 50, not `unspecified`), so this gate
is not skipped, and it clears with the full EUR 50 unspent.

### G4 — No forward-referenced prerequisites; module 1 grounded in baseline-assessment.md
**PASS.** Checked every module's `prerequisites` column in `curriculum.md`: module 2 →
{1}, module 3 → {1,2}, module 4 → {1,2,3}, module 5 → {1,2,3,4}, module 6 → {1,2,3,4,5},
module 7 → {1,2,3,4}, module 8 → {1,2,3,4,5,6}, module 9 → {1–8}. Every prerequisite
number is strictly less than its module number — no forward references. Module 1's
prerequisite is `baseline`, and `baseline-assessment.md` asserts exactly that starting
point (pre-A1, zero grammar) as its placement, so module 1's prerequisite is present in
the baseline assessment as required.

### G5 — Outcome coverage; every module has ≥1 resource/exercise/assessment
**PASS.** `assessment-designer` ran (`skipped_steps` is empty in `workflow-state.json`,
`wants_assessments: true`), so the assessment clause is **not** relaxed. Re-checked
`curriculum.md`'s outcome-coverage table: all 5 target outcomes from `requirements.md`
map to at least one module. Re-checked each of the 9 modules against `resources.md`,
`exercises.md`, `assessments.md`: every module has 2–4 resources, 3–4 exercises, and one
checkpoint (plus cumulative reviews after modules 3, 6, 9, and a final check). Module 8
has exactly 2 resources — satisfies the "≥1" numeric requirement.

Quality caveat (not a gate failure, since G5 tests existence not fit): module 8's two
resources only partially serve its "service/emergency-adjacent exchange" objective —
Language Transfer Track 7 covers only the ir a + infinitive plans sub-objective; the Rick
Steves video covers requests/problems but is region-mixed ("Spain and Latin America,"
confirmed by WebFetch below) rather than Peninsular-exclusive. `resources.md` discloses
this itself as its weakest-covered module. G5's literal criterion (≥1 resource) is met;
the fit gap is a curator quality note, not a G5 failure.

### G6 — No resource URL repeated across modules
**PASS.** Scanned all 26 URLs in `resources.md` for exact duplicates. The BBC "Mi Vida
Loca" content appears in modules 1, 5, and 9, but under three distinct URLs (Episode 1
single video, the full-story compilation, and a full-episode playlist respectively) — no
literal duplicate. Dreaming Spanish appears in modules 5, 6, 9 under three distinct
playlist URLs (Superbeginner/Beginner/Intermediate tiers). Language Transfer appears in
modules 1, 7, 8, 9 under four distinct track URLs. No two resource lines share a URL.

### G7 — Every resource verified this run, and reachable
**FAIL** — owner: `curator`.

Every one of the 26 lines in `resources.md` carries a `verified:` marker dated
2026-08-18, which is this run (the run began 2026-08-18; see the run's DATE NOTE — this
alone is not a failure). I sampled 7 non-YouTube URLs by WebFetch (YouTube watch/playlist
pages were excluded per this run's instruction to avoid the consent-wall loop; see the
BBC Mi Vida Loca note below for how that citation was instead assessed):

**GATE G7 FAIL** — the module 5 resource "[Perfecting the Prepositions in
Spanish](https://lightspeedspanish.co.uk/20201003-perfecting-the-prepositions-in-spanish/)"
is cited as `video/podcast · unknown · free`, "prepositions of place needed for
giving/following directions." WebFetch of that exact URL shows the page is **a book/
workbook announcement and Amazon promotion page** for a paid "Perfecting the Prepositions
in Spanish" workbook — there is no embedded lesson (video or audio) on the page at all,
and the underlying product is not free. The `verified: websearch 2026-08-18` marker
confirms the URL and title exist and match the topic by search, but does not confirm the
actual page content matches the citation's claimed format and cost — which is exactly
what G7 requires. — owner: `curator`
fix: Replace this citation with an actual free video or podcast lesson on Spanish
prepositions of place (or an amended citation that accurately labels this as a paid
workbook, with cost updated from `free` to its real price, and format from `video/podcast`
to `text/book`), and re-verify the replacement by WebFetch before citing it.

Everything else sampled held up:
- `Beginners Spanish Podcast 16: Spanish Question Words` (M3) — confirmed live, matches
  topic, and genuinely presents both an embedded video and an audio player (see G8 below).
- `How to Order Food in Spanish | Restaurants` (M6) — confirmed live, matches topic, but
  is audio-only, not video/podcast (see G8 below — a G8 issue, not a G7 one; the resource
  itself is real and free).
- `Free Spanish Podcast 17: Daily Routine` (M4) — confirmed live, matches topic. Its
  claimed "10 min 38 sec (confirmed)" duration could not be independently verified (the
  audio player renders via JavaScript that WebFetch does not execute; it shows "0:00 /
  0:00" in the fetched HTML). Also worth noting: the page's own title is "**Early
  Intermediate** Spanish Podcast 17," the same tier-mismatch the curator explicitly
  flagged for module 6's "How to Order Food" resource but did not flag here for module 4
  — an inconsistent disclosure, not a hard failure, since the content itself (reflexive
  verbs, routine vocabulary) is beginner-appropriate regardless of the site's tier label.
- `Make Comparisons in Spanish` (SpanishDict, M6) — confirmed live, matches topic, text
  article as claimed.
- `Spanish Language for Travelers` (Rick Steves, M8) — confirmed live video, matches
  topic; confirms the curator's own disclosed caveat that it covers "Spain and Latin
  America" together, not Peninsular-exclusive.
- Language Transfer Track 1 (SoundCloud, M1) — the track page exists (title and track
  name match), but WebFetch could not confirm the audio actually streams (SoundCloud's
  player requires a browser SoundCloud does not support in this tool; the fetched HTML
  shows only a compatibility warning). This is a tooling limitation, not evidence of a
  dead link — treated as inconclusive, not a failure.

**BBC "Mi Vida Loca" (modules 1, 5, 9), per this run's instruction, was judged on the
curator's stated evidence rather than fetched.** `resources.md` discloses that the
official `bbc.co.uk/languages` home was abandoned around 2014 and the content survives
only via unofficial YouTube reuploads — content-authority (BBC) is real, but
distribution is not evergreen. This is an accurate, honestly-flagged continuity risk, not
a G7 failure: the citation says what it is and names the risk rather than hiding it.

### G8 — ≥70% of resources match preferred modality (video)
**FAIL** — owner: `curator`.

`resources.md` claims 20 of 26 (76.9%) resources are video. I reclassified all 26 lines
by their stated `format` field, then corrected two of the three ambiguous "video/podcast"
entries using the WebFetch results above:

| Classification | Count | Items |
|---|---|---|
| Confirmed video (clear `video`/`video playlist`, plus 1 confirmed video/podcast) | **18** | All clearly-labeled `video`/`video playlist` lines (17), plus "Question Words Podcast 16" (M3), confirmed via WebFetch to genuinely embed a video section |
| Confirmed non-video (audio/text) | **7** | Language Transfer Tracks 1, 7, 58, 90 (audio, M1/7/8/9); SpanishDict comparatives (text, M6); Free Spanish Podcast 17 (audio, M4); **"How to Order Food in Spanish" (M6) — reclassified from the curator's "video/podcast" to audio-only**, confirmed by WebFetch: the page's lesson is delivered by an embedded audio player ("Podcast_3_Ordering_in_a_Restaurant"), with no video component |
| Not a valid lesson resource at all | **1** | "Perfecting the Prepositions in Spanish" (M5) — the G7 failure above; not video, not audio, not a free lesson of any kind |

18 / 26 = **69.2%**, below the 70% floor. The curator's 76.9% figure over-counted by
including both the M6 "How to Order Food" resource (actually audio-only) and the M5
"Perfecting the Prepositions" resource (not a lesson at all) as video.
— owner: `curator`
fix: Reclassify "How to Order Food in Spanish" as audio in `resources.md`'s format field
(the resource itself can stay, since G8 only requires the *ratio*, not removing it), and
replace the broken "Perfecting the Prepositions" citation (G7 fix above) with a genuine
free video resource. Replacing that one line with an actual video would raise the count
to 19/26 = 73.1%, clearing the 70% floor; alternatively add one more video resource to
any module without exceeding the 4-resources-per-module cap in the `resource-vetting`
skill.

### G9 — No module more than one level above the assessed baseline
**PASS, under a recorded interpretation.**

`baseline-assessment.md` places the learner at a single fixed baseline: pre-A1.
`curriculum.md` explicitly flags the ambiguity in G9's wording and asks the validator to
rule on it: read completely literally against that one fixed baseline, "no module more
than one level above baseline" would cap **every** module at A1 (one level above pre-A1),
since modules 4–9 progress into A2 and B1-threshold territory. Under that literal
reading, module 4 onward (A1.3 → A2.1) would already fail, and the confirmed
A2/B1-threshold target from `requirements.md` — a retargeting the learner explicitly
made and confirmed — would be structurally unreachable by any curriculum, since it is
two full CEFR levels above the assessed starting point.

I judge the literal, whole-curriculum reading to be untenable as the gate's intended
meaning, for a structural reason rather than a preference: a gate that makes it
impossible for **any** pre-A1 learner's curriculum to ever progress past A1, regardless
of module count or duration, directly contradicts G2 (the path must fit inside the
confirmed horizon) and G5 (every confirmed target outcome must be covered by some
module) for every subject where the learner starts at the lowest level and the goal is
realistically above "one level up." That would make G9 unsatisfiable by design for the
learner type it most needs to serve, which is not a plausible design intent for a pacing
gate. I instead read G9 as a step-wise pacing check — no module assumes more than one
increment of progress beyond what the immediately preceding module established — which
is exactly the fine-grained CEFR sub-level scheme (A1.1 → A1.2 → A1.3 → A2.1 → A2.2 →
A2.3 → B1-threshold) `curriculum.md` used. Checked module-by-module: every module's
level column advances by exactly one sub-step from the prior module's end-state (e.g.
module 3 ends A1.3, module 4 spans A1.3 → A2.1 — one sub-step forward, not a leap). No
module skips a sub-level. Under this reading, G9 passes.

This is a judgement call, recorded per the coordinator's instruction, not a relaxation of
the gate — the literal alternative reading was tested against the actual module
progression and found to make G9 unsatisfiable for this (and any similar) learner
profile. Flagging for the user/coordinator: if `gates.md`'s intent is genuinely the
literal single-baseline reading, that is a conflict between G9 and the retargeted goal
in `requirements.md` that only a human can resolve (loosen G9's wording, or re-scope the
goal back toward what a literal one-level cap could reach) — not something a further
validator retry could fix.

### Structural checks

| Artifact | Frontmatter (7 keys) ok | Owner matches pipeline.json | Sections ok (4, in order, non-empty) | Inputs exist | Citations ok |
|---|---|---|---|---|---|
| requirements.md | yes | yes (`requirements-formalizer`) | yes | n/a (none) | n/a (`Sources: None.` — no external data consumed, consistent with a Q&A-derived artifact) |
| baseline-assessment.md | yes | yes (`knowledge-assessor`) | yes | yes | yes (4 Wikipedia citations, all `verified: mcp:wikipedia 2026-08-18`) |
| curriculum.md | yes | yes (`curriculum-architect`) | yes | yes | yes (5 Wikipedia citations, all `verified: mcp:wikipedia 2026-08-18`) |
| resources.md | yes | yes (`curator`, video-curator variant named in Summary) | yes | yes | format ok on all 26 lines; **1 of 26 fails content-verification (G7 above)** |
| exercises.md | yes | yes (`exercise-designer`) | yes | yes | `Sources: None.` — exempt (exercises consumes no external data) |
| assessments.md | yes | yes (`assessment-designer`) | yes | yes | `Sources: None.` — exempt |
| schedule.md | yes | yes (`schedule-planner`) | yes | yes | `Sources: None.` — exempt |
| effort-budget.md | yes | yes (`effort-budget-aggregator`) | yes | yes | `Sources: None.` — exempt; explanation given |

No artifact is `BLOCKED`. No structural failures. All content failures are confined to
`resources.md` (G7, G8).

### Link sample

| URL | Method | Result |
|---|---|---|
| https://lightspeedspanish.co.uk/beginners/beginners-spanish-podcast-16-spanish-question-words/ | webfetch | Live, matches topic, genuinely has both video and audio sections |
| https://lightspeedspanish.co.uk/20201003-perfecting-the-prepositions-in-spanish/ | webfetch | Live, but is a paid workbook/Amazon promotion page, **not** the claimed free video/podcast lesson — G7 FAIL |
| https://www.spanishdict.com/guide/make-comparisons-in-spanish | webfetch | Live, matches topic, text article as claimed |
| https://www.ricksteves.com/watch-read-listen/video/travel-talks/spanish-language | webfetch | Live video, matches topic, confirms curator's own "Spain and Latin America" region-mix disclosure |
| https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lesson-3-how-to-order-food-in-spanish-restaurant/ | webfetch | Live, matches topic, but audio-only — reclassified for G8 |
| https://lightspeedspanish.co.uk/20111231-free-spanish-podcast-17-daily-routine/ | webfetch | Live, matches topic; "10 min 38 sec" duration not independently confirmable (JS player); page is titled "Early Intermediate," undisclosed here |
| https://soundcloud.com/languagetransfer/complete-spanish-track-1-language-transfer-the-thinking-method | webfetch | Track page exists and title matches; streaming content not verifiable via this tool (SoundCloud requires JS the fetch does not run) — inconclusive, not a failure |
| youtube.com/watch and /playlist URLs (BBC Mi Vida Loca, all LightSpeed and Dreaming Spanish YouTube items) | not fetched, per run instruction | Assessed on curator's stated evidence only; BBC continuity risk is honestly disclosed in `resources.md` |

## Sources
- [Beginners Spanish Podcast 16: Spanish Question Words](https://lightspeedspanish.co.uk/beginners/beginners-spanish-podcast-16-spanish-question-words/) — LightSpeed Spanish · verified: webfetch 2026-08-19
- [Perfecting the Prepositions in Spanish](https://lightspeedspanish.co.uk/20201003-perfecting-the-prepositions-in-spanish/) — LightSpeed Spanish · verified: webfetch 2026-08-19 (confirmed to be a workbook promotion page, not a lesson)
- [Make Comparisons in Spanish](https://www.spanishdict.com/guide/make-comparisons-in-spanish) — SpanishDict · verified: webfetch 2026-08-19
- [Spanish Language for Travelers](https://www.ricksteves.com/watch-read-listen/video/travel-talks/spanish-language) — Rick Steves' Europe · verified: webfetch 2026-08-19
- [How to Order Food in Spanish | Restaurants](https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lesson-3-how-to-order-food-in-spanish-restaurant/) — LightSpeed Spanish · verified: webfetch 2026-08-19
- [Free Spanish Podcast 17: Daily Routine](https://lightspeedspanish.co.uk/20111231-free-spanish-podcast-17-daily-routine/) — LightSpeed Spanish · verified: webfetch 2026-08-19
- [Complete Spanish, Track 1](https://soundcloud.com/languagetransfer/complete-spanish-track-1-language-transfer-the-thinking-method) — Language Transfer (SoundCloud) · verified: webfetch 2026-08-19 (existence only; streaming content unconfirmed)
- `.claude/workflow/gates.md`, `.claude/workflow/pipeline.json`, `runs/run-001-spanish-b1/state/workflow-state.json` — read directly for gate definitions, ownership, and skipped-step status.

## Open Questions
- **G9's wording is genuinely ambiguous and worth fixing at the source.** I resolved it
  in favour of the fine-grained sub-level reading with reasoning above, but this required
  judgement `validator` should not have to exercise on every run targeting a beginner
  learner. Recommend the coordinator/user consider clarifying `gates.md`'s G9 text (e.g.
  "no module more than one level above the level established by the immediately
  preceding module" instead of "the assessed baseline") so future runs don't depend on a
  re-derived interpretation.
- **`effort-budget.md`'s "14 of 26 unknown durations" undercounts by one** (module 5's
  "Perfecting the Prepositions" resource is also `unknown` in `resources.md` but is
  missing from the aggregator's breakdown). Does not change any totals or gate verdicts,
  since that resource already contributed 0 to the floor either way — flagged for
  correction on `effort-budget-aggregator`'s next revision, not blocking.
- **`assessments.md`'s Summary states "~325 minutes" total assessment time; its own
  itemised checkpoints sum to 330 minutes (5.50h).** `schedule.md` and `effort-budget.md`
  both independently and correctly used 330/5.50, so this is a self-contained ~1.5%
  rounding slip in `assessments.md`'s prose only — does not affect any gate, flagged for
  `assessment-designer`'s awareness.
- **SoundCloud citations (4 Language Transfer tracks) could not be fully verified by
  WebFetch** because SoundCloud's player requires JavaScript this tool does not execute;
  page/title existence was confirmed but actual audio streaming was not. This is a
  tooling limitation of this validation pass, not a finding against the resources — noted
  so a future validator run with browser-based fetching could close the gap.
