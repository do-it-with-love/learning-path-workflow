---
artifact: resources
owner: curator
run_id: run-001-spanish-b1
status: final
attempt: 3
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
  - artifacts/validation-report.md
generated: 2026-08-19T00:00:00Z
---

# Resources — Conversational European Spanish for Travel

## Summary
The **video** curator variant ran a third time on this pipeline, this run's final
allowed attempt. Attempt 2 fixed G7 but got G8 *worse* (62.96% genuine video, re-derived
by the validator, against 69.2% at attempt 1) because it trusted LightSpeed Spanish's own
"Video for This Spanish Lesson" section heading without checking whether a video element
actually sat under it. The validator's element-level check found four LightSpeed own-site
pages — "Beginners Spanish Podcast 16" (module 3), "Free Spanish Podcast 17: Daily
Routine" (module 4), "Directions in Spanish" (module 5), and "Making Comparisons in
Spanish" (module 6) — all have that heading empty, with only an MP3 player underneath. The
root cause, stated plainly: **lightspeedspanish.co.uk is a podcast site; LightSpeed's real
video lives on YouTube, not on their own domain.** I independently reproduced this with a
targeted element-level WebFetch on two more own-site pages before relying on them further
("Lesson 6 Reflexive Verbs," "35 Beginners Spanish Prepositions") and found the identical
pattern both times — an empty video heading, audio only — which confirms this is systemic
to the domain, not a one-off page defect.

This revision does not repeat that mistake. Of the four wrongly-labeled resources: three
(modules 4, 5, 6) are **replaced** with genuine YouTube-hosted LightSpeed videos on the
same topic, each cross-checked against LightSpeed's own-site companion page (confirming
the lesson is real, free, and on-topic — even though that companion page's own embed is
audio-only, consistent with the domain-wide pattern above) and verified via WebSearch per
this run's explicit tooling guidance (YouTube watch pages cannot be WebFetched without
tripping a consent-wall loop; a YouTube-hosted video is still genuine video, and WebSearch
confirming the title and URL is the sanctioned verification method for it). One (module 3,
"Podcast 16") is simply **relabeled honestly to `audio`** and kept, rather than forced into
a swap — no clean matching video candidate was found for that specific sub-topic and
inventing one would repeat the underlying failure mode. Module 6's swap draws on a second
provider, **Señor Jordan**, cross-verified via WebFetch of his companion lesson page, to
avoid a fourth LightSpeed citation in a single module. Net effect: 27 resources across 9
modules (2–4 each), of which **20 are genuine video (74.1%)**, verified either as
YouTube-hosted (video-hosting platform by construction) or, for the two Rick Steves/BBC
non-YouTube video citations, previously WebFetch/WebSearch-confirmed. This clears gate
G8's 70% floor by a margin of one full resource (19/27 would be the bare minimum; this
run has 20), a genuine margin rather than a repeat of attempt 2's false confidence. 6
resources are audio (all disclosed, all genuinely audio-only) and 1 is text. Cost position
is unchanged: every cited resource is free, so the run spends **EUR 0 of the EUR 50
budget**. No two modules share a URL (G6). Every citation carries a `verified:` marker
naming its method and this run's date. A minor data-quality item flagged by the validator
— module 1's Coverage-check subtotal read "~2.5h" against a reproducible "~1.667h" — is
corrected in this revision's table below.

## Findings

### Module 1: Sounds, Script & Survival Basics
- [Absolute Beginners Spanish 4-10 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb9T_CxcHYbsKNJRgLY4wAEJ) — LightSpeed Spanish (YouTube) · 2020s · video playlist (~7 lessons) · ~1.5h (est.) · free · verified: websearch 2026-08-18 — alphabet continuation, greetings and numbers, taught by Spain-based Cynthia (native Peninsular speaker) and Gordon; auto-captions available on YouTube.
- [Complete Spanish, Track 1 — Language Transfer, The Thinking Method](https://soundcloud.com/languagetransfer/complete-spanish-track-1-language-transfer-the-thinking-method) — Language Transfer (SoundCloud) · ongoing/free · audio · unknown (typically ~20–30 min per track; SoundCloud's player requires JavaScript this tool does not execute) · free · verified: websearch 2026-08-18 — foundational sound/structure induction; audio only, used sparingly against the video quota; a volunteer transcript exists (see Open Questions) for accessibility.
- [Mi Vida Loca — BBC Spanish Learning Ep.1 full](https://www.youtube.com/watch?v=J85JdNuCQ6I) — BBC (produced) / unofficial YouTube reupload · 2009 (production) · video · ~10 min · free · verified: websearch 2026-08-18 — Madrid-set beginner drama, Episode 1 survival basics/greetings; see Open Questions on official-site discontinuation.

### Module 2: Being & Describing
- [42 Beginners Understanding SER and ESTAR in Spanish — LightSpeed Spanish](https://www.youtube.com/watch?v=ENOX40X20-s) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — dedicated ser/estar contrast lesson at absolute-beginner tier.
- [47 Easily Learn Spanish, YOU ARE / VOSOTROS ESTÁIS — LightSpeed Spanish](https://www.youtube.com/watch?v=cXT06H3x9GI) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — vosotros conjugation of estar, explicit Peninsular-register content.
- [Absolute Beginners Spanish 11-15 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb-UBdc_Mj-htkVGp3-ea5gA) — LightSpeed Spanish (YouTube) · 2020s · video playlist (5 lessons) · ~1h (est.) · free · verified: websearch 2026-08-18 — gender/number agreement and self-introductions building on module 1.

### Module 3: Present-Tense Action
- [Absolute Beginners Spanish 16-20 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb86MxcytqlICBUNe_CAyjUy) — LightSpeed Spanish (YouTube) · 2020s · video playlist (5 lessons) · ~1h (est.) · free · verified: websearch 2026-08-18 — regular -ar/-er/-ir conjugation and common irregular verbs (tener, ir, querer, poder, hacer).
- [Beginners Spanish Podcast 16: Spanish Question Words — LightSpeed Spanish](https://lightspeedspanish.co.uk/beginners/beginners-spanish-podcast-16-spanish-question-words/) — LightSpeed Spanish (own site) · 2020s · **audio** · unknown · free · verified: webfetch 2026-08-19 — qué/dónde/cuándo/cómo/quién and question word order. **Corrected this attempt:** the validator's element-level WebFetch (and my own repeat check on two comparable own-site pages, see Summary) found the "Video for This Spanish Lesson" heading on this page is empty; only an MP3 player is present. Honestly relabeled `audio`, kept rather than dropped — no equivalent-quality Peninsular video on this exact sub-topic (question-word order specifically) was found this attempt; the module's other two resources are genuine video.
- [58 Beginners Spanish ¿Qué vs Cuál? — LightSpeed Spanish](https://www.youtube.com/watch?v=eQ9-w8brxyU) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — reinforces question-word nuance ahead of the module's unscripted Q&A objective.

### Module 4: Daily Life & Routine
- [14 Tell Time in Spanish — LightSpeed Spanish](https://www.youtube.com/watch?v=3K1PpC-gT0c) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — telling time, matching objective 2 directly.
- [44 Beginners Verbs like Gustar — LightSpeed Spanish](https://www.youtube.com/watch?v=vNEzUTNSHwU) — LightSpeed Spanish (YouTube) · 2021-03-05 · video · unknown · free · verified: websearch 2026-08-18 — gustar-type verbs for likes/dislikes.
- [Spanish Lesson Early Inter 6 Reflexive Verbs — LightSpeed Spanish](https://www.youtube.com/watch?v=Vl8BcH5lgCw) — LightSpeed Spanish (YouTube) · 2011 (production) · video · unknown · free · verified: websearch 2026-08-19 — **replaces "Free Spanish Podcast 17: Daily Routine"**, which the validator's element-level WebFetch confirmed is audio-only despite its "video" label (empty heading, MP3 player only). This is a genuinely YouTube-hosted LightSpeed video on the same topic (reflexive verbs for daily routine); cross-referenced against LightSpeed's own-site companion post ("Lesson 6: Reflexive Verbs in Spanish," webfetch-confirmed free and on-topic, though — consistent with the domain-wide pattern — that companion page's own embed is audio-only, which is exactly why the YouTube URL, not the own-site URL, is the cited resource here).
- [30 Beginners Test your listening skills — LightSpeed Spanish](https://www.youtube.com/watch?v=JqBVaAQzOVQ) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — listening review consolidating routine vocabulary before module 5.

### Module 5: Getting Around
- [Spanish Lesson 35 Abs Beginner Spanish Prepositions — LightSpeed Spanish](https://www.youtube.com/watch?v=E5SHi-vo978) — LightSpeed Spanish (YouTube) · 2015 (production) · video · unknown · free · verified: websearch 2026-08-19 — **replaces "Directions in Spanish"**, which the validator's element-level WebFetch confirmed is audio-only despite its "video" label. Genuinely YouTube-hosted; matches objective 1 (prepositions of place) directly. Cross-referenced against LightSpeed's own-site companion post ("35 Beginners Spanish Prepositions – The Small Important Words," webfetch-confirmed free and on-topic; again, that companion page's own embed is audio-only — the YouTube URL is what is cited).
- [Superbeginner Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7GbOHc3siOGQ5KmVSngZucl) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable (self-paced) · free (up to ~1,000 videos on the free tier) · verified: websearch 2026-08-18 — comprehensible-input listening; filter to Spain-accent hosts on the platform for Peninsular pronunciation exposure.
- [BBC Spanish - 'Mi Vida Loca'. Full Story (All Episodes). English Commentary, Spanish Subtitles](https://www.youtube.com/watch?v=_th2tbkpZ8c) — BBC (produced) / unofficial YouTube reupload · 2009 (production) · video · ~220 min (22 episodes × ~10 min) · free · verified: websearch 2026-08-18 — Episode 3 of this compilation covers street/subway directions; watch from that segment for module 5's role-play objective.

### Module 6: Eating, Shopping & Lodging
- [How to Order Food in Spanish | Restaurants — LightSpeed Spanish](https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lesson-3-how-to-order-food-in-spanish-restaurant/) — LightSpeed Spanish (own site) · 2020s · audio · unknown · free · verified: webfetch 2026-08-19 — restaurant ordering and polite request forms; unchanged, correctly labeled since attempt 2 (page has only an audio player, no video element).
- [Beginner Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7HWrrenMs3-nuhxgzyAiA-C) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable (self-paced) · free (up to ~1,000 videos on the free tier) · verified: websearch 2026-08-18 — shopping/food-themed comprehensible-input listening, Spain-accent filterable.
- [Make Comparisons in Spanish — SpanishDict Grammar Guide](https://www.spanishdict.com/guide/make-comparisons-in-spanish) — SpanishDict · current · text article · ~15 min read · free · verified: webfetch 2026-08-18 — más/menos...que and tan...como comparatives; kept as a reading-reference companion, the module's one non-video, non-audio resource.
- [01 Spanish Lesson – Unequal Comparisons (part 1): Más/menos ___ que](https://www.youtube.com/watch?v=gHYUjQZhtSk) — Señor Jordan (YouTube) · 2013 (production) · video · unknown · free · verified: websearch 2026-08-19, cross-referenced webfetch 2026-08-19 — **replaces "Making Comparisons in Spanish" (LightSpeed own-site)**, which the validator's element-level WebFetch confirmed is audio-only despite its "video" label. Genuinely YouTube-hosted; covers más/menos...que directly, matching objective 2. Drawn from a second provider (Señor Jordan, a long-running independent Spanish-teaching channel) rather than a fourth LightSpeed citation in one module; his companion page (senorjordan.com) was WebFetched and confirms the lesson is free and on the stated topic. Note: Señor Jordan's Spanish is general/neutral rather than Peninsular-accented — acceptable here because the objective is the comparative *grammar structure* (dialect-invariant), and this module's Peninsular listening exposure is already covered by the Dreaming Spanish entry above; flagged in Open Questions for transparency.

### Module 7: Talking About the Past
- [Gordon's Diaries Help with the Spanish past 2 Preterite — LightSpeed Spanish](https://www.youtube.com/watch?v=k9BPcxMKhrU) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18 — regular and irregular preterite conjugation walkthrough.
- [Complete Spanish, Track 58 — Language Transfer, The Thinking Method](https://soundcloud.com/languagetransfer/complete-spanish-track-58) — Language Transfer (SoundCloud) · ongoing/free · audio · unknown (typically ~20–30 min per track) · free · verified: websearch 2026-08-18 — "the dot in the past" (preterite) for -ar verbs, taught through the Thinking Method; deliberately picked over Language Transfer's earlier "line in the past" tracks (44–53), which teach the imperfect — out of this curriculum's scope.

### Module 8: Plans, Requests & Unexpected Situations
- [Complete Spanish, Track 7 — Language Transfer, The Thinking Method](https://soundcloud.com/languagetransfer/complete-spanish-track-7-language-transfer-the-thinking-method) — Language Transfer (SoundCloud) · ongoing/free · audio · unknown (typically ~20–30 min per track) · free · verified: websearch 2026-08-18 — "Voy a: Moving Toward Action," the near-future ir a + infinitive construction.
- [Spanish Language for Travelers — Rick Steves' Europe, Travel Talks](https://www.ricksteves.com/watch-read-listen/video/travel-talks/spanish-language) — Rick Steves' Europe · current · video · unknown · free · verified: webfetch 2026-08-18 — practical travel Spanish incl. requests and problem situations, taught in English by instructor Trish Feaster; covers "Spain and Latin America" together rather than Peninsular-exclusive — flagged as a partial regional mismatch in Open Questions; module 8 remains the weakest-covered module (see below).

### Module 9: Conversation Consolidation
- [Learning Spanish "Mi Vida Loca" BBC — full episode playlist](https://www.youtube.com/playlist?list=PL2k7gzcwtLTMgQpcYZSC5qCVz46bchbU4) — BBC (produced) / unofficial YouTube reupload · 2009 (production) · video playlist (22 episodes) · ~220 min · free · verified: websearch 2026-08-18 — cumulative review across transport, restaurant, shop and mystery-plot scenarios for consolidated listening.
- [Intermediate Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7Gssxi9f72cZktgOb4Vpdoy) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable (self-paced) · free (up to ~1,000 videos on the free tier) · verified: websearch 2026-08-18 — natural-pace listening without drawings/scaffolding, matching the A2.3→B1-threshold target; filter to Spain-accent hosts.
- [Complete Spanish, Track 90 (End) — Language Transfer, The Thinking Method](https://soundcloud.com/languagetransfer/complete-spanish-track-90-end) — Language Transfer (SoundCloud) · ongoing/free · audio · unknown (typically ~20–30 min per track) · free · verified: websearch 2026-08-18 — final lesson of the course, reviewing the grammar built across all 90 tracks; capstone-listening bookend to Track 1 in module 1.

### Coverage check

| Module | Resources | Video | Non-video | Approx. resource hours | Cost |
|---|---|---|---|---|---|
| 1. Sounds, Script & Survival Basics | 3 | 2 | 1 (audio) | ~1.667h known (1.5h + 0.167h) + 1 unknown | free |
| 2. Being & Describing | 3 | 3 | 0 | ~1h known (est.) + 2 unknown | free |
| 3. Present-Tense Action | 3 | 2 | 1 (audio) | ~1h known (est.) + 2 unknown | free |
| 4. Daily Life & Routine | 4 | 4 | 0 | 4 unknown | free |
| 5. Getting Around | 3 | 3 | 0 | ~3.67h known + 1 unknown + 1 variable (self-paced) | free |
| 6. Eating, Shopping & Lodging | 4 | 2 | 2 (1 audio, 1 text) | ~0.25h known + 2 unknown + 1 variable (self-paced) | free |
| 7. Talking About the Past | 2 | 1 | 1 (audio) | 2 unknown | free |
| 8. Plans, Requests & Unexpected | 2 | 1 | 1 (audio) | 2 unknown | free |
| 9. Conversation Consolidation | 3 | 2 | 1 (audio) | ~3.67h known + 1 unknown + 1 variable (self-paced) | free |
| **Total** | **27** | **20 (74.1%)** | **7 (6 audio, 1 text)** | **honestly incomplete — see note** | **EUR 0** |

**Video ratio for gate G8: 20/27 = 74.07%**, clearing the 70% floor with a genuine margin
of one full resource above the 19/27 bare minimum. Unlike attempt 2's 77.8% figure, every
`video` label in this table has now been checked either as YouTube-hosted (a video-hosting
platform by construction — no ambiguity possible) or, for the two non-YouTube video
citations (Rick Steves, and BBC's Ep.1 which is also YouTube-hosted), previously
WebFetch/WebSearch-confirmed. No resource in this table is labeled `video` on the strength
of an unpopulated page-template heading.

**Module 1 hours correction (validator-flagged):** attempt 2's Coverage-check row stated
module 1's resource hours as "~2.5h"; the three citation lines actually sum to 1.5h
(playlist, est.) + 0.167h (Mi Vida Loca Ep.1, 10 min) = **1.667h** of known duration, plus
one `unknown`-duration audio track. Corrected in the table above.

Note on hours: 17 of the 27 resources carry `unknown` individual duration (LightSpeed
YouTube videos without a stated runtime in search snippets, and Language Transfer's
SoundCloud tracks, whose player requires JavaScript this tool cannot execute). A further 3
resources (the three Dreaming Spanish playlists) are self-paced and marked `variable`
rather than `unknown`, since that is a property of the resource, not a data gap. This table
is resource **viewing** time only — it is not the full per-module hour budget in
`curriculum.md`, which also includes the practice `exercise-designer` adds separately.

## Sources
- [Absolute Beginners Spanish 4-10 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb9T_CxcHYbsKNJRgLY4wAEJ) — LightSpeed Spanish (YouTube) · 2020s · video playlist · ~1.5h (est.) · free · verified: websearch 2026-08-18
- [Complete Spanish, Track 1 — Language Transfer](https://soundcloud.com/languagetransfer/complete-spanish-track-1-language-transfer-the-thinking-method) — Language Transfer (SoundCloud) · ongoing · audio · unknown · free · verified: websearch 2026-08-18
- [Mi Vida Loca — BBC Spanish Learning Ep.1 full](https://www.youtube.com/watch?v=J85JdNuCQ6I) — BBC/unofficial reupload · 2009 · video · ~10 min · free · verified: websearch 2026-08-18
- [42 Beginners Understanding SER and ESTAR in Spanish — LightSpeed Spanish](https://www.youtube.com/watch?v=ENOX40X20-s) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [47 Easily Learn Spanish, YOU ARE / VOSOTROS ESTÁIS — LightSpeed Spanish](https://www.youtube.com/watch?v=cXT06H3x9GI) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [Absolute Beginners Spanish 11-15 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb-UBdc_Mj-htkVGp3-ea5gA) — LightSpeed Spanish (YouTube) · 2020s · video playlist · ~1h (est.) · free · verified: websearch 2026-08-18
- [Absolute Beginners Spanish 16-20 — LightSpeed Spanish](https://www.youtube.com/playlist?list=PL_7rDJ7DORb86MxcytqlICBUNe_CAyjUy) — LightSpeed Spanish (YouTube) · 2020s · video playlist · ~1h (est.) · free · verified: websearch 2026-08-18
- [Beginners Spanish Podcast 16: Spanish Question Words — LightSpeed Spanish](https://lightspeedspanish.co.uk/beginners/beginners-spanish-podcast-16-spanish-question-words/) — LightSpeed Spanish · 2020s · audio · unknown · free · verified: webfetch 2026-08-19
- [58 Beginners Spanish ¿Qué vs Cuál? — LightSpeed Spanish](https://www.youtube.com/watch?v=eQ9-w8brxyU) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [14 Tell Time in Spanish — LightSpeed Spanish](https://www.youtube.com/watch?v=3K1PpC-gT0c) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [44 Beginners Verbs like Gustar — LightSpeed Spanish](https://www.youtube.com/watch?v=vNEzUTNSHwU) — LightSpeed Spanish (YouTube) · 2021-03-05 · video · unknown · free · verified: websearch 2026-08-18
- [Spanish Lesson Early Inter 6 Reflexive Verbs — LightSpeed Spanish](https://www.youtube.com/watch?v=Vl8BcH5lgCw) — LightSpeed Spanish (YouTube) · 2011 · video · unknown · free · verified: websearch 2026-08-19
- [30 Beginners Test your listening skills — LightSpeed Spanish](https://www.youtube.com/watch?v=JqBVaAQzOVQ) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [Spanish Lesson 35 Abs Beginner Spanish Prepositions — LightSpeed Spanish](https://www.youtube.com/watch?v=E5SHi-vo978) — LightSpeed Spanish (YouTube) · 2015 · video · unknown · free · verified: websearch 2026-08-19
- [Superbeginner Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7GbOHc3siOGQ5KmVSngZucl) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable · free · verified: websearch 2026-08-18
- [BBC Spanish - 'Mi Vida Loca'. Full Story (All Episodes)](https://www.youtube.com/watch?v=_th2tbkpZ8c) — BBC/unofficial reupload · 2009 · video · ~220 min · free · verified: websearch 2026-08-18
- [How to Order Food in Spanish | Restaurants — LightSpeed Spanish](https://lightspeedspanish.co.uk/early-intermediate/intermediate-spanish-lesson-3-how-to-order-food-in-spanish-restaurant/) — LightSpeed Spanish · 2020s · audio · unknown · free · verified: webfetch 2026-08-19
- [Beginner Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7HWrrenMs3-nuhxgzyAiA-C) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable · free · verified: websearch 2026-08-18
- [Make Comparisons in Spanish — SpanishDict Grammar Guide](https://www.spanishdict.com/guide/make-comparisons-in-spanish) — SpanishDict · current · text article · ~15 min read · free · verified: webfetch 2026-08-18
- [01 Spanish Lesson – Unequal Comparisons (part 1): Más/menos ___ que](https://www.youtube.com/watch?v=gHYUjQZhtSk) — Señor Jordan (YouTube) · 2013 · video · unknown · free · verified: websearch 2026-08-19
- [Gordon's Diaries Help with the Spanish past 2 Preterite — LightSpeed Spanish](https://www.youtube.com/watch?v=k9BPcxMKhrU) — LightSpeed Spanish (YouTube) · 2020s · video · unknown · free · verified: websearch 2026-08-18
- [Complete Spanish, Track 58 — Language Transfer](https://soundcloud.com/languagetransfer/complete-spanish-track-58) — Language Transfer (SoundCloud) · ongoing · audio · unknown · free · verified: websearch 2026-08-18
- [Complete Spanish, Track 7 — Language Transfer](https://soundcloud.com/languagetransfer/complete-spanish-track-7-language-transfer-the-thinking-method) — Language Transfer (SoundCloud) · ongoing · audio · unknown · free · verified: websearch 2026-08-18
- [Spanish Language for Travelers — Rick Steves' Europe](https://www.ricksteves.com/watch-read-listen/video/travel-talks/spanish-language) — Rick Steves' Europe · current · video · unknown · free · verified: webfetch 2026-08-18
- [Learning Spanish "Mi Vida Loca" BBC — full episode playlist](https://www.youtube.com/playlist?list=PL2k7gzcwtLTMgQpcYZSC5qCVz46bchbU4) — BBC/unofficial reupload · 2009 · video playlist · ~220 min · free · verified: websearch 2026-08-18
- [Intermediate Dreaming Spanish](https://www.youtube.com/playlist?list=PLlpPf-YgbU7Gssxi9f72cZktgOb4Vpdoy) — Dreaming Spanish (YouTube) · ongoing · video playlist · variable · free · verified: websearch 2026-08-18
- [Complete Spanish, Track 90 (End) — Language Transfer](https://soundcloud.com/languagetransfer/complete-spanish-track-90-end) — Language Transfer (SoundCloud) · ongoing · audio · unknown · free · verified: websearch 2026-08-18

## Open Questions
- **Attempt 2 → attempt 3 changes, summarised for the coordinator.** (1) Relabeled
  "Beginners Spanish Podcast 16" (module 3) from `video` to `audio` and kept it — the
  validator's element-level WebFetch found no video element, only an MP3 player, and no
  equally strong replacement video on this specific sub-topic (question-word order) was
  found. (2) Replaced "Free Spanish Podcast 17: Daily Routine" (module 4) — also
  audio-only despite its label — with a genuine YouTube-hosted LightSpeed video, "Spanish
  Lesson Early Inter 6 Reflexive Verbs." (3) Replaced "Directions in Spanish" (module 5) —
  also audio-only — with a genuine YouTube-hosted LightSpeed video, "Spanish Lesson 35 Abs
  Beginner Spanish Prepositions." (4) Replaced "Making Comparisons in Spanish" (module 6) —
  also audio-only — with a genuine YouTube-hosted video from a second provider, Señor
  Jordan, "Unequal Comparisons (part 1)." Net effect: video ratio moved from the
  validator's re-derived 17/27 (62.96%, failing) to **20/27 (74.07%, passing with a
  one-resource margin)**. (5) Corrected module 1's Coverage-check hours subtotal from a
  stale "~2.5h" to the reproducible "~1.667h," per the validator's flagged data-quality
  item.
- **Why I stopped trusting lightspeedspanish.co.uk for video labels entirely.** Beyond the
  four pages the validator checked, I independently re-checked two more own-site pages
  this attempt ("Lesson 6: Reflexive Verbs" and "35 Beginners Spanish Prepositions," the
  companion pages for module 4 and module 5's new YouTube citations) using the same
  element-level method, and found the identical empty-heading, audio-only pattern both
  times — six own-site pages checked across two attempts, six confirmed audio-only. I am
  treating this as a structural property of the domain, not page-specific bad luck: this
  run no longer cites any lightspeedspanish.co.uk page as `video`, only as `audio` (two
  remain, correctly labeled: "Beginners Spanish Podcast 16" and "How to Order Food in
  Spanish"). All LightSpeed video in this artifact is now exclusively YouTube-hosted.
- **YouTube verification method, stated once for the coordinator/validator.** Per this
  run's explicit tooling guidance, YouTube watch/playlist pages cannot be WebFetched
  (consent-wall loop) but are inherently video-hosting; WebSearch confirming the exact
  title and URL exist is the sanctioned verification method and is what every YouTube
  citation in this artifact carries. Where a companion non-YouTube page could be
  WebFetched (LightSpeed's own-site posts for the module 4/5 replacements; Señor Jordan's
  site for the module 6 replacement), I did so for extra corroboration of topic and free
  access, and disclosed what that companion page's own embed actually contains in each
  case above, rather than let it imply the YouTube video's format.
- **Module 6's "Unequal Comparisons" video is not Peninsular-accented.** Señor Jordan
  teaches general/neutral Spanish rather than Castilian specifically. Used here because
  the objective it serves (más/menos...que comparative structure) is dialect-invariant
  grammar, and this module's Peninsular *listening* exposure is already carried by the
  Dreaming Spanish entry (Spain-accent filterable) in the same module. Flagging this as a
  deliberate, disclosed trade-off, not an oversight.
- **BBC Mi Vida Loca's official home is gone.** `bbc.co.uk/languages` was abandoned by the
  BBC around 2014 (confirmed via websearch of Association for Language Learning coverage
  in attempt 1); the content now survives only through third-party YouTube reuploads
  (English commentary, Spanish subtitles). Authority for the *content* is still BBC, but
  the *distribution* is unofficial and could disappear without notice. Unchanged from
  attempts 1–2.
- **Module 8 remains the weakest-covered module,** unchanged from attempts 1–2: neither
  resource is a clean Peninsular-only, video, service/emergency-specific lesson —
  Language Transfer Track 7 is audio and covers only the ir a + infinitive sub-objective,
  and the Rick Steves video is region-mixed ("Spain and Latin America"). A targeted search
  for a Spain-based creator's "reporting a problem"/emergency-request video would be the
  next thing to try if the coordinator wants a stronger match here; I did not spend this
  attempt's search budget on it because module 8's 2 resources (1 video, 1 audio) were not
  the constraint on gate G8 — the LightSpeed own-site mislabeling was.
- **SpanishPod101** has an explicitly labeled "Absolute Beginner European Spanish" series
  (webfetch-confirmed in attempt 1) that would suit module 8 well, but its free tier covers
  only lessons 1–3 of each series while the matching content is lesson #55 — excluded on
  the free-budget instruction. Recorded here in case the learner later spends part of the
  EUR 50 budget on it.
- **Duration honesty.** 17 of 27 resources carry `unknown` duration (LightSpeed/Rick Steves
  YouTube videos without a stated runtime in available page text, and Language Transfer's
  SoundCloud tracks, whose player renders duration only via JavaScript this tool cannot
  execute). 3 further resources (Dreaming Spanish's three playlists) are marked `variable`
  (self-paced) rather than `unknown`, since that is intrinsic to the resource, not a data
  gap. This is unchanged in kind from attempts 1–2, and remains a genuine tooling limit,
  not an unexamined gap.
- **Speaking practice is intentionally out of scope for this artifact.** None of the cited
  resources are interactive — LightSpeed, BBC, Dreaming Spanish and the two YouTube
  replacements are all receptive (listening/watching) even where they model spoken
  dialogue. Per `requirements.md`, target outcomes 1–3 require dedicated speaking practice
  a video resource cannot itself provide; `exercise-designer` is expected to build the
  role-play, shadowing and self-recording exercises the curriculum's modules 2–9 all name
  as spoken-production objectives.
- **Captions:** Dreaming Spanish confirms English/Spanish subtitles across its library; the
  BBC Mi Vida Loca reuploads explicitly advertise "English Commentary, Spanish Subtitles";
  LightSpeed's and Señor Jordan's YouTube videos carry YouTube's standard auto-captions
  (not individually verified per video). Language Transfer is audio-only; a volunteer-made
  transcript PDF for the Complete Spanish course exists online, partially offsetting the
  lack of captions, though not verified as officially maintained.
- **SoundCloud citations (4 Language Transfer tracks)** still could not be fully verified
  by WebFetch — page/title existence confirmed via websearch, actual audio streaming not —
  a tooling limitation carried over from attempts 1–2, not a finding against the resources
  themselves.
