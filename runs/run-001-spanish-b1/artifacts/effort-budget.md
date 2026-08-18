---
artifact: effort-budget
owner: effort-budget-aggregator
run_id: run-001-spanish-b1
status: final
attempt: 2
inputs:
  - artifacts/requirements.md
  - artifacts/curriculum.md
  - artifacts/resources.md
  - artifacts/exercises.md
  - artifacts/assessments.md
  - artifacts/validation-report.md
generated: 2026-08-19T00:00:00Z
---

# Effort & Budget — Conversational European Spanish for Travel

## Summary
Total money cost is **EUR 0** against a **EUR 50** budget — verified line-by-line against
the revised `resources.md`, where all **27** cited resources (up from 26 on attempt 1) are
marked `free`; gate G3 passes with the full EUR 50 unspent. Total time is a **floor of
exactly 40.00 hours** (11.25h resource-viewing + 23.25h practice + 5.50h assessment,
summed per module below) against **130 hours available** (5h/week × 26 weeks) and **108
hours** allocated by `curriculum.md` — both comparisons pass, with 90.00h of slack against
the available hours and 68.00h of slack against the curriculum allocation. The floor
understates true resource-viewing time: **17 of 27 resources** now carry `unknown`
individual durations (this artifact's own previous count of "14 of 26" was wrong — the
validator recounted 15 of 26 on attempt 1's resource set; the revised set changes the
denominator again, and I recounted directly against the current `resources.md` rather than
adjusting the old figure — see Open Questions for the module-by-module tally), plus 3 more
that are self-paced/`variable` (Dreaming Spanish, all three tiers used, modules 5/6/9). The
single biggest "cost driver" in this path is still not money — it is the unbudgeted
**tutor/conversation-partner gap**: `assessments.md` independently flags three things
self-assessment cannot verify (distinción/rr pronunciation, real-time unscripted listening,
and turn-taking in live conversation), all pointing to the same fix, and none of the EUR 50
is currently allocated toward it. The attempt-2 resource changes (module 5's dead citation
replaced with a real free lesson, module 6 gaining a video resource, two format
relabellings) narrow the *modality* gap that G8 was checking — they do nothing to close the
*interaction* gap that only a human conversation partner can close, so the conclusion that
the EUR 50 is best spent on conversation tutoring is unchanged from attempt 1.

## Findings

### Money

Every line below is taken directly from the revised `resources.md`; none is guessed or
converted (the run's currency is already EUR, matching `budget`, confirmed again in
`requirements.md`).

| # | Resource | Module | Type | Unit cost | Cost over path (26 wks) |
|---|---|---|---|---|---|
| 1 | Absolute Beginners Spanish 4-10 — LightSpeed Spanish | 1 | one-off (free) | EUR 0 | EUR 0 |
| 2 | Complete Spanish, Track 1 — Language Transfer | 1 | one-off (free) | EUR 0 | EUR 0 |
| 3 | Mi Vida Loca Ep.1 — BBC/unofficial reupload | 1 | one-off (free) | EUR 0 | EUR 0 |
| 4 | Ser and Estar #42 — LightSpeed Spanish | 2 | one-off (free) | EUR 0 | EUR 0 |
| 5 | Vosotros Estáis #47 — LightSpeed Spanish | 2 | one-off (free) | EUR 0 | EUR 0 |
| 6 | Absolute Beginners Spanish 11-15 — LightSpeed Spanish | 2 | one-off (free) | EUR 0 | EUR 0 |
| 7 | Absolute Beginners Spanish 16-20 — LightSpeed Spanish | 3 | one-off (free) | EUR 0 | EUR 0 |
| 8 | Question Words Podcast 16 — LightSpeed Spanish | 3 | one-off (free) | EUR 0 | EUR 0 |
| 9 | ¿Qué vs Cuál? #58 — LightSpeed Spanish | 3 | one-off (free) | EUR 0 | EUR 0 |
| 10 | Tell Time #14 — LightSpeed Spanish | 4 | one-off (free) | EUR 0 | EUR 0 |
| 11 | Gustar Verbs #44 — LightSpeed Spanish | 4 | one-off (free) | EUR 0 | EUR 0 |
| 12 | Daily Routine Podcast 17 — LightSpeed Spanish | 4 | one-off (free) | EUR 0 | EUR 0 |
| 13 | Listening Test #30 — LightSpeed Spanish | 4 | one-off (free) | EUR 0 | EUR 0 |
| 14 | Directions in Spanish — LightSpeed Spanish **(new this attempt, replaces the dead G7 citation)** | 5 | one-off (free) | EUR 0 | EUR 0 |
| 15 | Superbeginner Dreaming Spanish | 5 | one-off (free, tier-limited — see note) | EUR 0 | EUR 0 |
| 16 | Mi Vida Loca — Full Story | 5 | one-off (free) | EUR 0 | EUR 0 |
| 17 | Order Food in Spanish — LightSpeed Spanish | 6 | one-off (free) | EUR 0 | EUR 0 |
| 18 | Beginner Dreaming Spanish | 6 | one-off (free, tier-limited — see note) | EUR 0 | EUR 0 |
| 19 | Comparisons Guide — SpanishDict | 6 | one-off (free) | EUR 0 | EUR 0 |
| 20 | Making Comparisons in Spanish (video) — LightSpeed Spanish **(new this attempt)** | 6 | one-off (free) | EUR 0 | EUR 0 |
| 21 | Preterite Diaries — LightSpeed Spanish | 7 | one-off (free) | EUR 0 | EUR 0 |
| 22 | Complete Spanish, Track 58 — Language Transfer | 7 | one-off (free) | EUR 0 | EUR 0 |
| 23 | Complete Spanish, Track 7 — Language Transfer | 8 | one-off (free) | EUR 0 | EUR 0 |
| 24 | Spanish for Travelers — Rick Steves' Europe | 8 | one-off (free) | EUR 0 | EUR 0 |
| 25 | Mi Vida Loca — Full Playlist | 9 | one-off (free) | EUR 0 | EUR 0 |
| 26 | Intermediate Dreaming Spanish | 9 | one-off (free, tier-limited — see note) | EUR 0 | EUR 0 |
| 27 | Complete Spanish, Track 90 (End) — Language Transfer | 9 | one-off (free) | EUR 0 | EUR 0 |
| | | | **Total (27 rows)** | | **EUR 0 × 27 = EUR 0** |

**Arithmetic:** 27 resources × EUR 0 each = **EUR 0** total, one-off and recurring alike —
there are no subscriptions in this path (every resource is a standalone video, audio track,
or article, not a metered platform plan). This is unchanged in kind from attempt 1's 26
rows; the only change is one net additional free row (module 5's dead citation removed,
one replacement added; module 6 gained one new free resource) — 26 − 1 + 2 = 27, all still
EUR 0.

**Budget comparison:** EUR 0 (spent) vs EUR 50 (budget) → **passes gate G3** with EUR 50 of
headroom (100% of budget unspent). Unchanged from attempt 1.

**Conditional-free note (not a cost, a caveat):** Dreaming Spanish's free tier is capped at
"up to ~1,000 videos" per `resources.md`. This path uses it in 3 of 9 modules (5, 6, 9),
self-paced and filtered to Spain-accent hosts — nowhere near the cap for a 26-week beginner
path used this narrowly. Recorded because "free tier" claims need checking, not because
this one is actually at risk.

### Time

Resource hours are recomputed directly from each resource's own duration line in the
revised `resources.md` (not copied from that file's summary "Approx. resource hours"
column — see Open Questions for one discrepancy found there); practice hours are
`exercises.md`'s own per-module figures; assessment hours are the sum of each module's
`Check` plus any cumulative review that falls after it, from `assessments.md` (the final
check is attributed to module 9, the last module). Where a resource's duration is
`unknown` or self-paced/`variable`, it contributes 0 to the floor — every module total
below is a **floor**, marked `+`.

| Module | Resource hours (floor) | Practice hours | Assessment hours | Module total (floor) | Curriculum allocation | Exceeds allocation? |
|---|---|---|---|---|---|---|
| 1. Sounds, Script & Survival Basics | 1.67+ (1 unknown) | 2.17 | 0.33 (20 min check) | **4.17+** | 12 | No |
| 2. Being & Describing | 1.00+ (2 unknown) | 2.33 | 0.33 (20 min check) | **3.66+** | 11 | No |
| 3. Present-Tense Action | 1.00+ (2 unknown) | 2.50 | 0.83 (25 min check + 25 min cumulative review) | **4.33+** | 13 | No |
| 4. Daily Life & Routine | 0.00+ (4 unknown) | 2.67 | 0.33 (20 min check) | **3.00+** | 11 | No |
| 5. Getting Around | 3.67+ (1 unknown, 1 self-paced) | 2.75 | 0.42 (25 min check) | **6.84+** | 11 | No |
| 6. Eating, Shopping & Lodging | 0.25+ (2 unknown, 1 self-paced) | 2.58 | 0.83 (25 min check + 25 min cumulative review) | **3.66+** | 13 | No |
| 7. Talking About the Past | 0.00+ (2 unknown) | 2.83 | 0.33 (20 min check) | **3.16+** | 13 | No |
| 8. Plans, Requests & Unexpected | 0.00+ (2 unknown) | 1.92 | 0.42 (25 min check) | **2.34+** | 11 | No |
| 9. Conversation Consolidation | 3.67+ (1 unknown, 1 self-paced) | 3.50 | 1.67 (30 min check + 25 min cumulative review + 45 min final check) | **8.84+** | 13 | No |
| **Total** | **11.25+ (17 unknown, 3 self-paced)** | **23.25** | **5.50** | **40.00+** | **108** | **None** |

**Arithmetic — resource-hour floor, per module (known durations only, converted to hours):**
- M1: Absolute Beginners 4-10 playlist ~1.5h + Mi Vida Loca Ep.1 ~10min (0.167h) = **1.667h**. (Complete Spanish Track 1 is `unknown`.)
- M2: Absolute Beginners 11-15 playlist ~1h = **1.00h**. (SER/ESTAR #42, VOSOTROS ESTÁIS #47 both `unknown`.)
- M3: Absolute Beginners 16-20 playlist ~1h = **1.00h**. (Question Words Podcast 16, ¿Qué vs Cuál? #58 both `unknown`.)
- M4: **0h** — all four resources (Tell Time #14, Gustar #44, Daily Routine Podcast 17, Listening Test #30) are `unknown`. (Daily Routine Podcast 17's duration was corrected this attempt from a false "10 min 38 sec (confirmed)" to honest `unknown` — see resources.md — which is why M4's floor drops from attempt 1's 0.20h to 0.00h here.)
- M5: BBC Mi Vida Loca Full Story ~220min = **3.667h**. (Directions in Spanish is `unknown`; Superbeginner Dreaming Spanish is self-paced/variable.)
- M6: SpanishDict Comparisons Guide ~15min = **0.25h**. (Order Food in Spanish and the new Making Comparisons video are both `unknown`; Beginner Dreaming Spanish is self-paced/variable.)
- M7: **0h** — both resources (Preterite Diaries, Track 58) are `unknown`.
- M8: **0h** — both resources (Track 7, Rick Steves) are `unknown`.
- M9: Mi Vida Loca Full Playlist ~220min = **3.667h**. (Track 90 is `unknown`; Intermediate Dreaming Spanish is self-paced/variable.)
- Sum: 1.667 + 1.00 + 1.00 + 0 + 3.667 + 0.25 + 0 + 0 + 3.667 = **11.251h ≈ 11.25h**.

**Arithmetic — practice:** 2.17 + 2.33 + 2.50 + 2.67 + 2.75 + 2.58 + 2.83 + 1.92 + 3.50 =
**23.25h** (matches `exercises.md`'s own stated total exactly; unchanged from attempt 1,
since `exercises.md` was not revised).

**Arithmetic — assessment:** (20+20+25+25+20+25+25+25+20+25+30+25+45) minutes = 330 minutes
= **5.50h** (matches `assessments.md`'s itemised checkpoints; unchanged from attempt 1,
since `assessments.md` was not revised).

**Grand total floor:** 11.25 + 23.25 + 5.50 = **40.00h**. Per-module totals sum to the same
figure: 4.17+3.66+4.33+3.00+6.84+3.66+3.16+2.34+8.84 = **40.00h** ✓.

**Comparison against the 130h available (5h/week × 26 weeks):** 40.00h floor leaves
**90.00h of slack** even before any unknown resource duration is added back in —
comfortably inside budget.

**Comparison against the curriculum's 108h module allocation:** 40.00h floor is **68.00h
under** the 108h `curriculum.md` allocation. **No module exceeds its allocation** — all
nine are under, most by a wide margin. As on attempt 1, this gap is most plausibly
explained by two things this artifact's inputs don't fully itemise: (1) 17 of 27 resources
have `unknown` individual durations, so real resource-viewing time is higher than the floor
shown; and (2) `curriculum.md`'s per-module hour estimates likely assume some un-itemized
review/practice time (re-watching, vocabulary look-ups, note-taking) that none of
`resources.md`, `exercises.md`, or `assessments.md` separately budgets. See Open Questions.

**Modules with the least remaining headroom** (highest floor-to-allocation ratio, so the
ones to watch if unknown durations turn out larger than assumed): Module 9 (8.84 of 13h,
68.0%) and Module 5 (6.84 of 11h, 62.2%) — essentially unchanged from attempt 1's 68.2% and
62.5%. Both already carry the path's two Mi Vida Loca video blocks (~3.67h each), which are
also the resources flagged as continuity-risky below.

### Hidden costs

None of these appear as a priced line in `resources.md`; each is flagged here precisely
because it would otherwise surface unbudgeted, mid-path. All of attempt 1's findings still
hold — the attempt-2 resource changes fixed a dead citation and a modality-ratio shortfall,
neither of which touches these gaps.

- **Conversation partner / tutor (italki, Preply, or a language-exchange app).**
  `assessments.md` independently names this same fix in three separate places: the
  Peninsular distinción/rr sounds are "close to impossible to self-detect," real-time
  unpredictable listening comprehension "cannot be fully self-assessed," and turn-taking
  fluency is "only approximated by self-interview role-play." All three point to a native
  speaker or tutor, ideally around modules 1, 3, and 8–9 per `assessments.md`'s own
  suggestion. **No such resource is in `resources.md`, so its cost is unknown** — not
  zero, unknown. This is the most likely candidate for how the EUR 50 would actually get
  spent; see the free-only variant below and Open Questions for an unverified illustrative
  range.
- **DELE certification exam fee.** `requirements.md` explicitly retargets the goal away
  from certified B1 to a practical strong-A2/B1-threshold level, so a DELE fee is *not*
  part of this path's confirmed scope — but if the learner changes their mind after
  finishing (a plausible outcome, since the path stops one exam short of certification),
  this is a real cost with no resource line anywhere in this run. Cost: unknown, not
  sourced this run, and deliberately out of scope unless the learner asks to revisit
  `requirements.md`.
- **Vocabulary-logging tool.** `assessments.md`'s final check (part 5) depends on the
  learner having "kept a running vocabulary log" across all 9 modules, and flags that
  without one, "the final check's part 5 has no reliable method at all beyond free
  recall." No artifact in this run (curator, exercise-designer, or assessment-designer)
  names a tool for this — a notebook or spreadsheet is free and sufficient, but the
  dependency itself was never made explicit anywhere before now.
- **Recording equipment.** Both `exercises.md` and `assessments.md` build almost every
  checkpoint and practice task around self-recording (shadow-and-compare,
  record-and-transcribe). A phone microphone is adequate and is assumed here, but no
  artifact states this assumption; a learner without a working phone/computer mic would
  hit an unbudgeted equipment cost with no warning.
- **BBC "Mi Vida Loca" continuity risk (non-monetary), unchanged.** `resources.md` flags
  that the official `bbc.co.uk/languages` page was abandoned around 2014 and the content
  "survives only through third-party YouTube reuploads" which "could disappear without
  notice." This resource is used in 3 of 9 modules (1, 5, 9) and is one of the two largest
  resource-hour blocks in the whole path (~3.67h each in modules 5 and 9 — see Time
  above). If a reupload is taken down mid-path, the learner loses free content and would
  need to either find another reupload or spend money on a substitute — a real risk over
  26 weeks even though today's cost is EUR 0. This risk was not addressed by attempt 2's
  revision (which fixed module 5 and 6, not the Mi Vida Loca citations).
- **Remediation time (a hidden time cost, not a money one).** `assessments.md`'s go/no-go
  rules routinely prescribe redoing drills and re-recording a checkpoint on a "Not yet"
  result (e.g. modules 1, 2, 3, 5, 6, 7, 8, and 9 all have explicit redo instructions).
  None of that redo time is counted in the 5.50h assessment total above, which is
  checkpoint time only. Given the 90.00h of slack against the 130h available, there is
  room to absorb this — but it is not currently a line item anywhere.
- **SpanishPod101 (named but not taken).** `resources.md`'s Open Questions names a
  SpanishPod101 "Absolute Beginner European Spanish" series as an excellent fit for
  module 8, excluded because its free tier stops at lesson 3 and the needed lesson is
  #55; the curator notes its paid tiers ("$4–47/month") would technically fit the EUR 50
  ceiling. This is a real, already-scouted option if the learner wants to spend part of
  the budget rather than leave it unspent — recorded here so it isn't rediscovered from
  scratch. Unchanged from attempt 1; module 8 remains the weakest-covered module per
  `resources.md`'s own attempt-2 disclosure.

### Free-only variant

There is no distinction to compute here: **every resource in this path is already free,
so the free-only variant is this path, at EUR 0.** No coverage is lost by "dropping paid
resources" because none are paid — true on attempt 1 and still true after the revision
(module 5's replacement and module 6's addition are both free, WebFetch-confirmed).

The genuinely useful question for a EUR 50 budget that is entirely unspent is the
reverse one — what would the money best buy if the learner chose to spend some of it.
Based on the gaps `assessments.md` itself could not close through self-assessment (see
Hidden costs above), the highest-value use of the EUR 50 is very likely **one or a
handful of paid conversation-practice sessions** (italki, Preply, or a similar
platform), timed around modules 1, 3, and 8–9 as `assessments.md` itself suggests,
specifically to check distinción/rr pronunciation, unscripted listening, and real
turn-taking — the three things this path's own assessment design admits it cannot
verify alone. No specific number of sessions or exact price is stated here because no
such resource or price was sourced in `resources.md` this run (see Open Questions for
the unverified illustrative range and why it is not treated as a finding). This
conclusion is unchanged from attempt 1: the revised resource set improved format
coverage (G8) and fixed a dead link (G7), but neither of those touches the interaction
gap this budget question is actually about.

## Sources
None. No currency conversion was needed — `budget` is already stated in EUR (confirmed
again in `requirements.md`) and every resource cost sourced from `resources.md` is EUR 0.

## Open Questions
- **Correction to this artifact's own attempt-1 error.** Attempt 1 stated "14 of 26
  resources ... have `unknown` individual durations," which the validator corrected to 15
  of 26 (module 5's "Perfecting the Prepositions" resource was omitted from the tally).
  That resource no longer exists in this revision — it was replaced (G7 fix) — so neither
  the old "14" nor the validator's "15" applies to the current resource set. I recounted
  directly against the revised `resources.md`, module by module: M1×1, M2×2, M3×2, M4×4,
  M5×1, M6×2, M7×2, M8×2, M9×1 = **17 of 27**. This total does *not* change the resource-hour
  floor (unknowns already contributed 0 either way), but it does change how large the true
  gap between the floor and reality plausibly is (see next point).
- **Unknown resource durations understate the true resource-hour total.** I did not
  estimate the 17 `unknown`-duration items — per instruction, an unsourced duration is
  written as `unknown`/excluded, not guessed. Using `resources.md`'s own note that Language
  Transfer tracks and similar short lessons typically run ~20–30 minutes, a generous
  illustrative addition (17 items × 20–30 min) would add roughly **6–8.5 hours**, bringing
  the true floor to something like 46–48.5h — still comfortably under both the 108h
  curriculum allocation and the 130h available. Separately, the **3 self-paced Dreaming
  Spanish playlists** (modules 5, 6, 9) are not folded into that estimate at all — their
  actual viewing time depends entirely on how much comprehensible-input listening the
  learner chooses to do, from a few minutes to many hours, and no ceiling or typical-use
  figure exists in `resources.md` to estimate from.
- **A discrepancy in `resources.md`'s own coverage table for module 1.** Its "Coverage
  check" table states module 1's approx. resource hours as "~2.5h (2 est. + 1 unknown)."
  Summing the two individually-dated resources in module 1's own citation lines gives
  1.5h (playlist) + 10min (0.167h, Mi Vida Loca Ep.1) = **1.667h**, not 2.5h — a difference
  consistent with a units slip (1.5 + 1.0, as if "10 min" had been added as "1.0" rather
  than converted to hours). This appears to be an arithmetic error carried over from
  attempt 1 that neither that attempt's `effort-budget.md` (which independently reported
  the same wrong 2.50 figure) nor the validator's G1 pass caught, since G1 was checked
  against `schedule.md`'s totals, not `resources.md`'s per-module table directly. I used
  the bottom-up figure (1.667h) in the Time table above because it is reproducible from
  the individual citation lines shown in `resources.md`'s Findings section, and flag the
  coverage-table figure as needing a fix on `curator`'s next pass. This does not affect any
  gate: the correction only *lowers* module 1's floor, and G1 (weekly hours) already has
  large margin per `validation-report.md`.
- **Tutor/conversation-partner cost is unknown and not sourced this run.** `resources.md`
  contains no priced conversation-practice resource, so I am not stating a figure as a
  finding. For the learner's own planning, typical italki/Preply conversation-tutoring
  rates are commonly in the range of roughly EUR 8–20 per 30–45 minute session — this
  range is **not verified against a live source during this run** and must be treated as
  an unverified assumption, not a costed line item, until someone actually checks current
  listings. Unchanged from attempt 1.
- **DELE exam fee is unknown and out of current scope.** No fee was sourced this run
  because `requirements.md` explicitly places certified B1/DELE outside this path's
  confirmed goal. If the learner later asks to add it, `requirements.md` and downstream
  artifacts would need to be revisited before this artifact could cost it honestly.
- **Whether the curriculum's 108h allocation includes un-itemized review time.**
  The 68.00h gap between the 108h curriculum allocation and the 40.00h floor computed here
  could mean the curriculum estimate is generous, or it could mean real study time
  (re-watching videos, dictionary look-ups, vocabulary logging, redoing failed
  checkpoints per `assessments.md`'s go/no-go rules) is real but uncounted by any of the
  three producing artifacts. Not resolved either way — a genuine gap in what the
  pipeline's artifacts currently itemize, not an error fixable by re-estimating someone
  else's numbers.
