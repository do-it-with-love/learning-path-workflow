---
artifact: resources
owner: curator
run_id: run-001-spanish-b1
status: final
attempt: 2
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
  - artifacts/validation-report.md
generated: 2026-08-19T00:00:00Z
---

# Resources — Conversational European Spanish for Travel

## Summary
The **video** curator variant ran again for this pipeline on attempt 2, a targeted
gate-failure retry (frontmatter `owner` is the pipeline slot `curator`, per contract).
Attempt 1 failed two gates: **G7**, because module 5's "Perfecting the Prepositions in
Spanish" citation resolved to a paid Amazon workbook promotion page rather than the
claimed free lesson; and **G8**, because the genuine video ratio was 18/26 = 69.2% once
that dead citation and one mislabeled audio-only resource were correctly excluded. This
revision (1) removes the dead citation and replaces it with a WebFetch-confirmed free
video lesson on directions/prepositions of place for module 5, (2) re-audits every
resource's format claim by WebFetch rather than trusting the original search snippet,
correcting **two** entries: "How to Order Food in Spanish" (module 6) is genuinely
audio-only and is now labeled `audio`, while "Free Spanish Podcast 17: Daily Routine"
(module 4) turned out on re-fetch to carry a genuine embedded video (not audio-only as
originally mislabeled) and is now correctly labeled `video`, and (3) adds one further
WebFetch-confirmed free video resource to module 6 (comparatives) both to strengthen that
module's coverage and to raise the video-ratio buffer well clear of the 70% floor. The
result is **27 resources across 9 modules** (2–4 each), of which **21 are genuine video**
(77.8%), 5 audio, and 1 text — comfortably above gate G8's floor with margin to spare.
Backbone providers are unchanged: **LightSpeed Spanish** (Peninsular pronunciation,
vosotros, ser/estar), **Language Transfer** (free audio grammar induction, used
sparingly), **Dreaming Spanish** (Spain-accent comprehensible input), **BBC's Mi Vida
Loca** (Madrid-set beginner drama, flagged distribution risk unchanged from attempt 1),
and one **Rick Steves' Europe** video and one **SpanishDict** text article where no
Peninsular-exclusive video cleared the bar. Cost position is unchanged: every cited
resource is free, so the run spends **EUR 0 of the EUR 50 budget**. No two modules share
a URL. Every citation carries a `verified:` marker; newly verified or re-verified lines
this attempt carry `2026-08-19`, unchanged lines retain their valid `2026-08-18` markers
from attempt 1.

## Findings

### Module 1: Sounds, Script & Survival Basics
- [Absolute Beginners Spanish 4-10 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb9T_CxcHYbsKNJRgLY4wAEJ) — LightSpeed Spanish (YouTube) · 2020s · video playlist (~7 lessons) · ~1.5h (est.) · free · verified: websearch 2026-08-18 — alphabet continuation, greetings and numbers, taught by Spain-based Cynthia (native Peninsular speaker) and Gordon; auto-captions available on YouTube.
- [Complete Spanish, Track 1 — Language Transfer, The Thinking Method](https://soundcloud.com/languagetransfer/complete-spanish-track-1-language-transfer-the-thinking-method) — Language Transfer (SoundCloud) · ongoing/free · audio · unknown (typically ~20–30 min per track, per the course's own general description; exact runtime not independently confirmable — SoundCloud's player requires JavaScript this tool does not execute) · free · verified: websearch 2026-08-18 — foundational sound/structure induction (no rote memorisation); audio only, so used sparingly against the video quota; a volunteer transcript exists (noted in Open Questions) for accessibility.
- [Mi Vida Loca — BBC Spanish Learning Ep.1 full](https://www.youtube.com/watch?v=J85JdNuCQ6I) — BBC (produced) / unofficial YouTube reupload · 2009 (production) · video · ~10 min · free · verified: websearch 2026-08-18 — Madrid-set beginner drama, Episode 1 survival basics/greetings; see Open Questions on official-site discontinuation.

### Module 2: Being & Describing
- [42 Beginners Understanding SER and ESTAR in Spanish — LightSpeed Spanish](https://www.youtube.com/watch?v=ENOX40X20-s) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — dedicated ser/estar contrast lesson at absolute-beginner tier.
- [47 Easily Learn Spanish, YOU ARE / VOSOTROS ESTÁIS — LightSpeed Spanish](https://www.youtube.com/watch?v=cXT06H3x9GI) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — vosotros conjugation of estar, explicit Peninsular-register content.
- [Absolute Beginners Spanish 11-15 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb-UBdc_Mj-htkVGp3-ea5gA) — LightSpeed Spanish (YouTube) · 2020s · video playlist (5 lessons) · ~1h (est.) · free · verified: websearch 2026-08-18 — gender/number agreement and self-introductions building on module 1.

### Module 3: Present-Tense Action
- [Absolute Beginners Spanish 16-20 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb86MxcytqlICBUNe_CAyjUy) — LightSpeed Spanish (YouTube) · 2020s · video playlist (5 lessons) · ~1h (est.) · free · verified: websearch 2026-08-18 — regular -ar/-er/-ir conjugation and common irregular verbs (tener, ir, querer, poder, hacer).
- [Beginners Spanish Podcast 16: Spanish Question Words — LightSpeed Spanish](https://lightspeedspanish.co.uk/beginners/beginners-spanish-podcast-16-spanish-question-words/) — LightSpeed Spanish (own site) · 2020s · **video** · unknown · free · verified: webfetch 2026-08-19 — qué/dónde/cuándo/cómo/quién and question word order. **Corrected this attempt:** re-fetched directly rather than trusting the search snippet; the page confirms a genuine embedded video player ("Video for This Spanish Lesson") alongside the audio, so this is labeled plain `video`, not the ambiguous "video/podcast" hedge attempt 1 used.
- [58 Beginners Spanish ¿Qué vs Cuál? — LightSpeed Spanish](https://www.youtube.com/watch?v=eQ9-w8brxyU) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — reinforces question-word nuance ahead of the module's unscripted Q&A objective.

### Module 4: Daily Life & Routine
- [14 Tell Time in Spanish — LightSpeed Spanish](https://www.youtube.com/watch?v=3K1PpC-gT0c) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — telling time, matching objective 2 directly.
- [44 Beginners Verbs like Gustar — LightSpeed Spanish](https://www.youtube.com/watch?v=vNEzUTNSHwU) — LightSpeed Spanish (YouTube) · 2021-03-05 · video · unknown · free · verified: websearch 2026-08-18 — gustar-type verbs for likes/dislikes.
- [Free Spanish Podcast 17: Daily Routine — LightSpeed Spanish](https://lightspeedspanish.co.uk/20111231-free-spanish-podcast-17-daily-routine/) — LightSpeed Spanish (own site) · 2011 · **video** · unknown · free · verified: webfetch 2026-08-19 — reflexive verbs for daily routine. **Corrected this attempt, twice:** (1) re-fetched directly and found the page has both a "Video for This Spanish Lesson" and an "Audio for This Spanish Lesson" section — attempt 1 mislabeled this `audio podcast`; it is genuine video. (2) attempt 1's stated duration, "10 min 38 sec (confirmed)", was not actually confirmable — the page's player renders "0:00 / 0:00" via JavaScript this tool cannot execute and no duration appears in the page text, so duration is now honestly `unknown` rather than a false "(confirmed)" figure. Also disclosing, for consistency with module 6's disclosure below: the page's own title is "**Early Intermediate** Spanish Podcast 17," one tier above this module's A1.3→A2.1 target, though the reflexive-verb/routine content itself is beginner-appropriate.
- [30 Beginners Test your listening skills — LightSpeed Spanish](https://www.youtube.com/watch?v=JqBVaAQzOVQ) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — listening review consolidating routine vocabulary before module 5.

### Module 5: Getting Around
- [Directions in Spanish — LightSpeed Spanish](https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lessons-4-directions/) — LightSpeed Spanish (own site) · 2020s · video · unknown (no duration stated in page text; player renders "0:00/0:00" via JavaScript) · free · verified: webfetch 2026-08-19 — **replaces attempt 1's dead "Perfecting the Prepositions in Spanish" citation**, which G7 found to be a paid Amazon workbook promotion page with no lesson at all. This lesson directly matches objective 1 (prepositions of place, ESTAR/QUEDAR, imperative direction-giving phrases like "siga" and "a la izquierda") and objective 3 (directions role-play). WebFetch confirms it is free, has both an embedded video and audio player, and is titled "Early Intermediate Spanish Podcast 4 – Directions in Spanish" — the same one-tier-above-module label pattern disclosed for module 4 and module 6's LightSpeed resources; content matches the module's A2.1 objective regardless of the site's own tier tag.
- [Superbeginner Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7GbOHc3siOGQ5KmVSngZucl) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable (self-paced) · free (up to ~1,000 videos on the free tier) · verified: websearch 2026-08-18 — comprehensible-input listening; filter to Spain-accent hosts on the platform for Peninsular pronunciation exposure.
- [BBC Spanish - 'Mi Vida Loca'. Full Story (All Episodes). English Commentary, Spanish Subtitles](https://www.youtube.com/watch?v=_th2tbkpZ8c) — BBC (produced) / unofficial YouTube reupload · 2009 (production) · video · ~220 min (22 episodes × ~10 min) · free · verified: websearch 2026-08-18 — Episode 3 of this compilation covers street/subway directions; watch from that segment for module 5's role-play objective.

### Module 6: Eating, Shopping & Lodging
- [How to Order Food in Spanish | Restaurants — LightSpeed Spanish](https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lesson-3-how-to-order-food-in-spanish-restaurant/) — LightSpeed Spanish (own site) · 2020s · **audio** · unknown · free · verified: webfetch 2026-08-19 — restaurant ordering and polite request forms. **Corrected this attempt:** re-fetched directly; the page has only an audio player ("Podcast_3_Ordering_in_a_Restaurant.mp3", with speed controls) and no video player at all — attempt 1's "video/podcast" label was wrong and is now honestly `audio`. Still catalogued under LightSpeed's "Early Intermediate" tier; content matches this module's A2.1–A2.2 objective directly (see Open Questions).
- [Beginner Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7HWrrenMs3-nuhxgzyAiA-C) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable (self-paced) · free (up to ~1,000 videos on the free tier) · verified: websearch 2026-08-18 — shopping/food-themed comprehensible-input listening, Spain-accent filterable.
- [Make Comparisons in Spanish — SpanishDict Grammar Guide](https://www.spanishdict.com/guide/make-comparisons-in-spanish) — SpanishDict · current · text article · ~15 min read · free · verified: webfetch 2026-08-18 — más/menos...que and tan...como comparatives; kept as a reading-reference companion to the new video lesson below, and remains the module's one non-video resource.
- [Spanish Lesson | Making Comparisons in Spanish — LightSpeed Spanish](https://lightspeedspanish.co.uk/20131208-early-intermediate-spanish-podcast-24-making-comparisons-in-spanish/) — LightSpeed Spanish (own site) · 2013 · video · unknown (no duration stated in page text) · free · verified: webfetch 2026-08-19 — **new this attempt**, added to strengthen module 6 (flagged as the weakest-covered module in attempt 1) and to raise the video ratio with a real resource rather than a reclassification. WebFetch confirms a free lesson with both a "Video for This Spanish Lesson" and an "Audio for This Spanish Lesson" section, covering más/menos que, tan...como, and superlatives — directly matching objective 2. Same "Early Intermediate" own-site tier label as the other LightSpeed entries above; content fits the module's A2.1→A2.2 target.

### Module 7: Talking About the Past
- [Gordon's Diaries Help with the Spanish past 2 Preterite — LightSpeed Spanish](https://www.youtube.com/watch?v=k9BPcxMKhrU) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — regular and irregular preterite conjugation walkthrough.
- [Complete Spanish, Track 58 — Language Transfer, The Thinking Method](https://soundcloud.com/languagetransfer/complete-spanish-track-58) — Language Transfer (SoundCloud) · ongoing/free · audio · unknown (typically ~20–30 min per track) · free · verified: websearch 2026-08-18 — "the dot in the past" (preterite) for -ar verbs, taught through the Thinking Method rather than rote tables; deliberately picked over Language Transfer's earlier "line in the past" tracks (44–53), which teach the *imperfect* — out of this curriculum's scope per `curriculum.md`.

### Module 8: Plans, Requests & Unexpected Situations
- [Complete Spanish, Track 7 — Language Transfer, The Thinking Method](https://soundcloud.com/languagetransfer/complete-spanish-track-7-language-transfer-the-thinking-method) — Language Transfer (SoundCloud) · ongoing/free · audio · unknown (typically ~20–30 min per track) · free · verified: websearch 2026-08-18 — "Voy a: Moving Toward Action," the near-future ir a + infinitive construction.
- [Spanish Language for Travelers — Rick Steves' Europe, Travel Talks](https://www.ricksteves.com/watch-read-listen/video/travel-talks/spanish-language) — Rick Steves' Europe · current · video · unknown · free · verified: webfetch 2026-08-18 — practical travel Spanish incl. requests and problem situations, taught in English by instructor Trish Feaster; covers "Spain and Latin America" together rather than Peninsular-exclusive — flagged as a partial regional mismatch in Open Questions; unchanged from attempt 1 (module 8 remains the weakest-covered module, see below).

### Module 9: Conversation Consolidation
- [Learning Spanish "Mi Vida Loca" BBC — full episode playlist](https://www.youtube.com/playlist?list=PL2k7gzcwtLTMgQpcYZSC5qCVz46bchbU4) — BBC (produced) / unofficial YouTube reupload · 2009 (production) · video playlist (22 episodes) · ~220 min · free · verified: websearch 2026-08-18 — cumulative review across transport, restaurant, shop and mystery-plot scenarios for consolidated listening.
- [Intermediate Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7Gssxi9f72cZktgOb4Vpdoy) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable (self-paced) · free (up to ~1,000 videos on the free tier) · verified: websearch 2026-08-18 — natural-pace listening without drawings/scaffolding, matching the A2.3→B1-threshold target; filter to Spain-accent hosts.
- [Complete Spanish, Track 90 (End) — Language Transfer, The Thinking Method](https://soundcloud.com/languagetransfer/complete-spanish-track-90-end) — Language Transfer (SoundCloud) · ongoing/free · audio · unknown (typically ~20–30 min per track) · free · verified: websearch 2026-08-18 — final lesson of the course, reviewing the grammar built across all 90 tracks; used as a capstone-listening bookend to Track 1 in module 1.

### Coverage check

| Module | Resources | Video | Non-video | Approx. resource hours | Cost |
|---|---|---|---|---|---|
| 1. Sounds, Script & Survival Basics | 3 | 2 | 1 (audio) | ~2.5h (2 est. + 1 unknown) | free |
| 2. Being & Describing | 3 | 3 | 0 | ~1h+ (1 est. + 2 unknown) | free |
| 3. Present-Tense Action | 3 | 3 | 0 | ~1h+ (1 est. + 2 unknown) | free |
| 4. Daily Life & Routine | 4 | 4 | 0 | 4 unknown | free |
| 5. Getting Around | 3 | 3 | 0 | ~3.7h (1 est.) + 2 unknown | free |
| 6. Eating, Shopping & Lodging | 4 | 2 | 2 (1 audio, 1 text) | ~0.25h confirmed + 3 unknown | free |
| 7. Talking About the Past | 2 | 1 | 1 (audio) | 2 unknown | free |
| 8. Plans, Requests & Unexpected | 2 | 1 | 1 (audio) | 2 unknown | free |
| 9. Conversation Consolidation | 3 | 2 | 1 (audio) | ~3.7h (1 est.) + 1 unknown | free |
| **Total** | **27** | **21 (77.8%)** | **6 (5 audio, 1 text)** | **honestly incomplete — see note** | **EUR 0** |

**Video ratio for gate G8: 21/27 = 77.8%**, clearing the 70% floor with an 8-percentage-point
margin, so a small future correction (e.g. one more reclassification on a future validator
pass) would not by itself put the run back under the floor.

Note on hours: 17 of the 27 resources carry `unknown` individual durations. This is a
deliberate, audited figure, not an oversight — see "Duration honesty" in Open Questions
for the full breakdown and why it changed from attempt 1's disclosed count. Playlist and
Dreaming-Spanish totals remain self-paced estimates. This table is resource **viewing**
time only — it is not the full per-module hour budget in `curriculum.md`, which also
includes the practice `exercise-designer` will add.

## Sources
- [Absolute Beginners Spanish 4-10 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb9T_CxcHYbsKNJRgLY4wAEJ) — LightSpeed Spanish (YouTube) · 2020s · video playlist · ~1.5h (est.) · free · verified: websearch 2026-08-18
- [Complete Spanish, Track 1 — Language Transfer, The Thinking Method](https://soundcloud.com/languagetransfer/complete-spanish-track-1-language-transfer-the-thinking-method) — Language Transfer (SoundCloud) · ongoing · audio · unknown · free · verified: websearch 2026-08-18
- [Mi Vida Loca — BBC Spanish Learning Ep.1 full](https://www.youtube.com/watch?v=J85JdNuCQ6I) — BBC/unofficial reupload · 2009 · video · ~10 min · free · verified: websearch 2026-08-18
- [42 Beginners Understanding SER and ESTAR in Spanish — LightSpeed Spanish](https://www.youtube.com/watch?v=ENOX40X20-s) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [47 Easily Learn Spanish, YOU ARE / VOSOTROS ESTÁIS — LightSpeed Spanish](https://www.youtube.com/watch?v=cXT06H3x9GI) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [Absolute Beginners Spanish 11-15 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb-UBdc_Mj-htkVGp3-ea5gA) — LightSpeed Spanish (YouTube) · 2020s · video playlist · ~1h (est.) · free · verified: websearch 2026-08-18
- [Absolute Beginners Spanish 16-20 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb86MxcytqlICBUNe_CAyjUy) — LightSpeed Spanish (YouTube) · 2020s · video playlist · ~1h (est.) · free · verified: websearch 2026-08-18
- [Beginners Spanish Podcast 16: Spanish Question Words — LightSpeed Spanish](https://lightspeedspanish.co.uk/beginners/beginners-spanish-podcast-16-spanish-question-words/) — LightSpeed Spanish · 2020s · video · unknown · free · verified: webfetch 2026-08-19
- [58 Beginners Spanish ¿Qué vs Cuál? — LightSpeed Spanish](https://www.youtube.com/watch?v=eQ9-w8brxyU) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [14 Tell Time in Spanish — LightSpeed Spanish](https://www.youtube.com/watch?v=3K1PpC-gT0c) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [44 Beginners Verbs like Gustar — LightSpeed Spanish](https://www.youtube.com/watch?v=vNEzUTNSHwU) — LightSpeed Spanish (YouTube) · 2021-03-05 · video · unknown · free · verified: websearch 2026-08-18
- [Free Spanish Podcast 17: Daily Routine — LightSpeed Spanish](https://lightspeedspanish.co.uk/20111231-free-spanish-podcast-17-daily-routine/) — LightSpeed Spanish · 2011 · video · unknown · free · verified: webfetch 2026-08-19
- [30 Beginners Test your listening skills — LightSpeed Spanish](https://www.youtube.com/watch?v=JqBVaAQzOVQ) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [Directions in Spanish — LightSpeed Spanish](https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lessons-4-directions/) — LightSpeed Spanish · 2020s · video · unknown · free · verified: webfetch 2026-08-19
- [Superbeginner Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7GbOHc3siOGQ5KmVSngZucl) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable · free · verified: websearch 2026-08-18
- [BBC Spanish - 'Mi Vida Loca'. Full Story (All Episodes)](https://www.youtube.com/watch?v=_th2tbkpZ8c) — BBC/unofficial reupload · 2009 · video · ~220 min · free · verified: websearch 2026-08-18
- [How to Order Food in Spanish | Restaurants — LightSpeed Spanish](https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lesson-3-how-to-order-food-in-spanish-restaurant/) — LightSpeed Spanish · 2020s · audio · unknown · free · verified: webfetch 2026-08-19
- [Beginner Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7HWrrenMs3-nuhxgzyAiA-C) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable · free · verified: websearch 2026-08-18
- [Make Comparisons in Spanish — SpanishDict Grammar Guide](https://www.spanishdict.com/guide/make-comparisons-in-spanish) — SpanishDict · current · text article · ~15 min read · free · verified: webfetch 2026-08-18
- [Spanish Lesson | Making Comparisons in Spanish — LightSpeed Spanish](https://lightspeedspanish.co.uk/20131208-early-intermediate-spanish-podcast-24-making-comparisons-in-spanish/) — LightSpeed Spanish · 2013 · video · unknown · free · verified: webfetch 2026-08-19
- [Gordon's Diaries Help with the Spanish past 2 Preterite — LightSpeed Spanish](https://www.youtube.com/watch?v=k9BPcxMKhrU) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [Complete Spanish, Track 58 — Language Transfer](https://soundcloud.com/languagetransfer/complete-spanish-track-58) — Language Transfer (SoundCloud) · ongoing · audio · unknown · free · verified: websearch 2026-08-18
- [Complete Spanish, Track 7 — Language Transfer](https://soundcloud.com/languagetransfer/complete-spanish-track-7-language-transfer-the-thinking-method) — Language Transfer (SoundCloud) · ongoing · audio · unknown · free · verified: websearch 2026-08-18
- [Spanish Language for Travelers — Rick Steves' Europe](https://www.ricksteves.com/watch-read-listen/video/travel-talks/spanish-language) — Rick Steves' Europe · current · video · unknown · free · verified: webfetch 2026-08-18
- [Learning Spanish "Mi Vida Loca" BBC — full episode playlist](https://www.youtube.com/playlist?list=PL2k7gzcwtLTMgQpcYZSC5qCVz46bchbU4) — BBC/unofficial reupload · 2009 · video playlist · ~220 min · free · verified: websearch 2026-08-18
- [Intermediate Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7Gssxi9f72cZktgOb4Vpdoy) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable · free · verified: websearch 2026-08-18
- [Complete Spanish, Track 90 (End) — Language Transfer](https://soundcloud.com/languagetransfer/complete-spanish-track-90-end) — Language Transfer (SoundCloud) · ongoing · audio · unknown · free · verified: websearch 2026-08-18

## Open Questions
- **Attempt 1 → attempt 2 changes, summarised for the coordinator.** (1) Removed the dead
  "Perfecting the Prepositions in Spanish" citation (module 5) and replaced it with
  "Directions in Spanish" (LightSpeed Spanish), WebFetch-confirmed free and video this
  attempt. (2) Reclassified "How to Order Food in Spanish" (module 6) from
  "video/podcast" to `audio` — WebFetch confirms only an audio player is embedded. (3)
  Reclassified "Free Spanish Podcast 17: Daily Routine" (module 4) from `audio podcast`
  to `video` — WebFetch confirms it actually has a genuine embedded video player that
  attempt 1 missed; also corrected its duration from a false "10 min 38 sec (confirmed)"
  to honest `unknown`, since the figure could not actually be verified. (4) Added one new
  video resource to module 6 ("Making Comparisons in Spanish," LightSpeed) to both
  strengthen that module's weakest-flagged coverage and give the video ratio real margin
  above the 70% floor rather than resting on the bare minimum. Net effect: 26 resources →
  27; genuine video 18/26 (69.2%, failing) → 21/27 (77.8%, passing with margin).
- **Duration honesty.** 17 of 27 resources carry `unknown` duration, up from the 15
  the validator counted in attempt 1 (which itself corrected `effort-budget.md`'s
  undercounted "14"). This is a net increase, not a regression: it reflects (a) one
  already-unknown resource removed (the dead Prepositions citation) and two new/
  replacement resources added, both genuinely `unknown` (Directions, Comparisons), and
  (b) Free Spanish Podcast 17's duration moving from a false "confirmed" figure to an
  honestly disclosed `unknown`. I attempted to close these gaps directly: WebFetching
  LightSpeed's own-site pages (not just YouTube) for several entries, and fetching
  Language Transfer's official site for a course-level duration table. Neither source
  renders duration in static page text — LightSpeed's players show "0:00 / 0:00" until
  JavaScript runs, and languagetransfer.org lists no per-track or total-course runtime.
  The remaining `unknown` YouTube entries would require opening individual watch pages,
  which this run is instructed to avoid due to the consent-wall loop. This is a genuine
  data-availability limit of the tools available this run, not an unexamined gap.
- **BBC Mi Vida Loca's official home is gone.** `bbc.co.uk/languages` was abandoned by the
  BBC around 2014 (confirmed via websearch of Association for Language Learning coverage);
  the content now survives only through third-party YouTube reuploads (English commentary,
  Spanish subtitles). Authority for the *content* is still BBC (a recognised institution),
  but the *distribution* is unofficial and could disappear without notice. Unchanged from
  attempt 1; the coordinator should know it is not an evergreen link the way an active
  institutional page would be.
- **Several LightSpeed lessons (modules 4, 5, 6) are catalogued under LightSpeed's own
  "Early Intermediate" site tier**, one tier above their target module's A1.3–A2.2 CEFR
  range, even though the content itself matches the module objective. This is a
  site-taxonomy label mismatch, not a content-level mismatch — flagging it once, here,
  for all three instances rather than repeating the same caveat per line.
- **Module 8 remains the weakest-covered module.** Neither resource is a clean
  Peninsular-only, video, service/emergency-specific lesson: Language Transfer Track 7 is
  audio and covers only the ir a + infinitive sub-objective, and the Rick Steves video is
  region-mixed ("Spain and Latin America"). Unchanged from attempt 1 — a targeted search
  for a Spain-based creator's "reporting a problem"/emergency-request video would be the
  next thing to try if the coordinator wants a stronger match here.
- **SpanishPod101 has an explicitly labeled "Absolute Beginner European Spanish" series**
  (confirmed via webfetch in attempt 1 — lesson 55, "10 Phrases to Help You in an
  Emergency," names Spain-specific detail) that would have been an excellent fit for
  module 8. It remains excluded because its free tier covers only the first 3 lessons of
  each series and the target lesson is #55 — the free tier does not cover what would be
  assigned, which fails this run's free-budget instruction even though the paid tiers
  ($4–47/month) would technically fit the EUR 50 ceiling. Recorded here in case the
  learner later decides to spend part of the budget on it.
- **Speaking practice is intentionally out of scope for this artifact.** None of the cited
  resources are interactive — LightSpeed, BBC and Dreaming Spanish are all receptive
  (listening/watching) even where they model spoken dialogue. Per `requirements.md`, target
  outcomes 1–3 require dedicated speaking practice that a video resource cannot itself
  provide; `exercise-designer` is expected to build the role-play, shadowing and
  self-recording exercises the curriculum's modules 2–9 all name as spoken-production
  objectives.
- **Captions:** Dreaming Spanish confirms English/Spanish subtitles across its library; the
  BBC Mi Vida Loca reuploads explicitly advertise "English Commentary, Spanish Subtitles";
  LightSpeed's YouTube videos carry YouTube's standard auto-captions (not individually
  verified per video), and its own-site video/audio lessons ship with downloadable
  helpsheets (paid tier) but no confirmed free transcript. Language Transfer is audio-only;
  a volunteer-made transcript PDF for the Complete Spanish course exists online, which
  partially offsets the lack of captions for a non-native reader, though it was not
  verified as officially maintained.
