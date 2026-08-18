---
artifact: schedule
owner: schedule-planner
run_id: run-001-spanish-b1
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

# Schedule — Conversational European Spanish for Travel

## Summary
This schedule runs **exactly 26 weeks** (matching `horizon_weeks`, gate G2 satisfied with
zero weeks to spare) in the learner's real session pattern — two ~1.5h weekday evenings
plus one ~2h weekend block, 5h/week nominal. Summing the **real** hours reported by
`resources.md` (resource viewing) + `exercises.md` (practice) + `assessments.md`
(checkpoints) gives **41.10 hours** of accounted content across the whole path — far under
the 130-hour budget, so **every single week clears gate G1 with large margin** (the heaviest
week, week 26, uses 3.17h against a 5h budget; no week comes close to the 5.5h/+10%
ceiling). Speaking practice is scheduled every week without exception, because
`exercises.md`'s recurring warm-up drill runs at the start of *every* session in every
module. The most important judgement call here is not scheduling arithmetic but a **data
quality flag**: `resources.md` itself calls its resource-hour figures "honestly
incomplete" — two modules (7, 8) have **zero** quantified resource duration, and five more
carry unquantified "+N unknown" videos on top of their reported figure — so the 41.10h
total is very likely a floor, not the true figure, and the very large apparent slack
(~89h, ~68% of budget) is partly a data gap rather than confirmed free time. I did not
invent durations to close that gap (see Open Questions); I used the three source
artifacts' own numbers as given, including the zeros. Because the module→week
apportionment already sums to exactly 26 weeks under the learner's fixed 3-sessions/week
pattern, there is no room for a wholly separate calendar buffer week without breaking G2
or altering `exercises.md`'s session counts (not this step's artifact to change) — instead,
week 26 is deliberately stripped of new resource content and used as the de facto
buffer/deadline week (cumulative review + final check + catch-up only). The schedule fits
the deadline. It does **not** currently use anywhere near the full weekly budget — that is
flagged, not hidden.

## Findings

### Real hours per module (the arithmetic)

Resource hours are `resources.md`'s own "Approx. resource hours" figures per module,
taken as reported. Practice hours are `exercises.md`'s per-module practice-load table,
taken as reported. Checkpoint hours are `assessments.md`'s per-checkpoint minutes,
converted to hours and taken as reported.

| Module | Resource h (resources.md) | Practice h (exercises.md) | Checkpoint h (assessments.md) | Total h |
|---|---|---|---|---|
| 1. Sounds, Script & Survival Basics | 2.50 | 2.17 | 0.33 (20 min) | 5.00 |
| 2. Being & Describing | 1.00 | 2.33 | 0.33 (20 min) | 3.66 |
| 3. Present-Tense Action | 1.00 | 2.50 | 0.42 (25 min) | 3.92 |
| 4. Daily Life & Routine | 0.20 | 2.67 | 0.33 (20 min) | 3.20 |
| 5. Getting Around | 3.70 | 2.75 | 0.42 (25 min) | 6.87 |
| 6. Eating, Shopping & Lodging | 0.25 | 2.58 | 0.42 (25 min) | 3.25 |
| 7. Talking About the Past | 0 (unquantified — see Open Questions) | 2.83 | 0.33 (20 min) | 3.16 |
| 8. Plans, Requests & Unexpected Situations | 0 (unquantified — see Open Questions) | 1.92 | 0.42 (25 min) | 2.34 |
| 9. Conversation Consolidation | 3.70 | 3.50 | 0.50 (30 min) | 7.70 |
| Cumulative reviews (after M3, M6, M9 — 25 min each) | — | — | 1.25 (75 min) | 1.25 |
| Final check (full-path assessment) | — | — | 0.75 (45 min) | 0.75 |
| **Total** | **12.35** | **23.25** | **5.50 (330 min)** | **41.10** |

Column checks: resource 2.50+1.00+1.00+0.20+3.70+0.25+0+0+3.70 = **12.35**. Practice
2.17+2.33+2.50+2.67+2.75+2.58+2.83+1.92+3.50 = **23.25** (matches `exercises.md`'s own
stated total exactly). Checkpoint 0.33+0.33+0.42+0.33+0.42+0.42+0.33+0.42+0.50+1.25+0.75 =
**5.50**. Grand total 12.35+23.25+5.50 = **41.10h** against a 130h budget (26 weeks × 5h) —
88.90h of headroom.

### Module → week apportionment

Each module's exercises are designed around a fixed session count (9 sessions for every
module except module 8's 6), and the learner has exactly 3 sessions/week — so weeks per
module are fixed at session-count ÷ 3, not a free scheduling choice:

| Module | Sessions | Weeks | Calendar weeks |
|---|---|---|---|
| 1. Sounds, Script & Survival Basics | 9 | 3 | 1–3 |
| 2. Being & Describing | 9 | 3 | 4–6 |
| 3. Present-Tense Action (+ cumulative review) | 9 | 3 | 7–9 |
| 4. Daily Life & Routine | 9 | 3 | 10–12 |
| 5. Getting Around | 9 | 3 | 13–15 |
| 6. Eating, Shopping & Lodging (+ cumulative review) | 9 | 3 | 16–18 |
| 7. Talking About the Past | 9 | 3 | 19–21 |
| 8. Plans, Requests & Unexpected Situations | 6 | 2 | 22–23 |
| 9. Conversation Consolidation (+ cumulative review + final check) | 9 | 3 | 24–26 |

9×8 + 6 = 78 sessions ÷ 3 sessions/week = **26 weeks exactly**, matching `horizon_weeks`
with no spare week (see Open Questions on the buffer-week implication).

### Week-by-week plan

Each week: two weekday evening sessions (drills, vocabulary, shadowing — short and
retrieval-heavy) and one weekend session (new resource material, longer application/
synthesis speaking tasks, checkpoints). Every session opens with that module's recurring
speaking drill, so speaking practice appears in all 78 sessions across all 26 weeks.

#### Week 1 — Module 1, wk 1/3 (Pre-A1 → A1.1)
- Weekday A (0.25h): Drill — sound & recall warm-up (distinción pairs). Begin Language
  Transfer Track 1 (audio induction).
- Weekday B (0.25h): Drill — pronouns/numbers/greetings recall. Finish Track 1.
- Weekend (0.83h): LightSpeed "Absolute Beginners 4–10" playlist, opening lessons.
- Week total: **1.33h**. No checkpoint.

#### Week 2 — Module 1, wk 2/3
- Weekday A (0.25h): Drill (distinción). Continue LightSpeed playlist.
- Weekday B (0.25h): Drill (pronouns/numbers). Mi Vida Loca Ep.1 (~10 min), shadow one line.
- Weekend (1.33h): Drill + finish LightSpeed playlist + **Application — Read-Aloud &
  Self-Introduction role-play** (30 min, recorded).
- Week total: **1.83h**. No checkpoint.

#### Week 3 — Module 1, wk 3/3
- Weekday A (0.25h): Drill + review distinción word list.
- Weekday B (0.42h): Drill + **Stretch (optional) — Alphabet Speed Spell** (10 min).
- Weekend (1.17h): Drill + light review of module 1 resources + **Module 1 checkpoint**
  (20 min: alphabet, 10 target-sound words, count 0–20, 30-sec greeting w/ vosotros).
- Week total: **1.83h**. **Checkpoint: Module 1 check.**

#### Week 4 — Module 2, wk 1/3 (A1.1 → A1.2)
- Weekday A (0.25h): Drill — ser/estar & agreement warm-up.
- Weekday B (0.25h): Drill + "42 Understanding SER and ESTAR" (LightSpeed).
- Weekend (0.33h): "47 VOSOTROS ESTÁIS" (LightSpeed) + drill.
- Week total: **0.83h**. No checkpoint.

#### Week 5 — Module 2, wk 2/3
- Weekday A (0.25h): Drill + continue "Absolute Beginners 11–15" playlist.
- Weekday B (0.25h): Drill + continue playlist.
- Weekend (0.83h): Drill + finish playlist + **Application — Introduce Yourself and a
  Friend** (60–90 sec recorded monologue).
- Week total: **1.33h**. No checkpoint.

#### Week 6 — Module 2, wk 3/3
- Weekday A (0.25h): Drill (ser/estar) + review.
- Weekday B (0.42h): Drill + **Synthesis — Sounds + Description Combo** (20 min).
- Weekend (0.83h): Drill + **Module 2 checkpoint** (20 min: 60–90 sec description of self
  + one other, vosotros form).
- Week total: **1.50h**. **Checkpoint: Module 2 check.**

#### Week 7 — Module 3, wk 1/3 (A1.2 → A1.3)
- Weekday A (0.25h): Drill — conjugation & question rotation.
- Weekday B (0.25h): Drill + "Absolute Beginners 16–20" playlist (start).
- Weekend (0.33h): Drill + continue playlist.
- Week total: **0.83h**. No checkpoint.

#### Week 8 — Module 3, wk 2/3
- Weekday A (0.25h): Drill + LightSpeed question-words podcast.
- Weekday B (0.25h): Drill + "¿Qué vs Cuál?" video.
- Weekend (0.83h): Drill + **Application — Unscripted Q&A With Yourself** (30 min, 8
  questions recorded).
- Week total: **1.33h**. No checkpoint.

#### Week 9 — Module 3, wk 3/3
- Weekday A (0.25h): Drill + review irregular verbs (tener/ir/querer/poder/hacer).
- Weekday B (0.25h): Drill + review question words.
- Weekend (1.67h): Drill + **Synthesis — Meet-and-Greet Chain** (30 min) + **Module 3
  checkpoint** (25 min: unscripted 8-question exchange) + **Cumulative review — modules
  1–3** (25 min: alphabet/count to 30, 5 ser/estar sentences, verb conjugations, vosotros
  sentence).
- Week total: **2.17h**. **Checkpoints: Module 3 check + Cumulative review (M1–3).**

#### Week 10 — Module 4, wk 1/3 (A1.3 → A2.1)
- Weekday A (0.25h): Drill — routine, time & gustar warm-up.
- Weekday B (0.15h): Drill + brief vocabulary review (module 4's video durations are
  largely unconfirmed — see Open Questions; treat this slot as light self-paced viewing).
- Weekend (0.17h): Drill + "14 Tell Time in Spanish."
- Week total: **0.57h**. No checkpoint.

#### Week 11 — Module 4, wk 2/3
- Weekday A (0.25h): Drill + "44 Verbs like Gustar."
- Weekday B (0.33h): Drill + **Application — Narrate Your Actual Day** (20 min, first
  occurrence, recorded).
- Weekend (0.32h): Drill + Free Spanish Podcast 17 (Daily Routine, ~10.5 min confirmed).
- Week total: **0.90h**. No checkpoint.

#### Week 12 — Module 4, wk 3/3
- Weekday A (0.25h): Drill + "30 Test your listening skills."
- Weekday B (0.33h): Drill + **Application — Narrate Your Actual Day** (20 min, second
  occurrence, different day).
- Weekend (1.15h): Drill + **Synthesis — The Full Day, In Character** (30 min) +
  **Module 4 checkpoint** (20 min: 60-sec routine narration).
- Week total: **1.73h**. **Checkpoint: Module 4 check.**

#### Week 13 — Module 5, wk 1/3 (A2.1)
- Weekday A (0.25h): Drill — directions warm-up.
- Weekday B (0.25h): Drill + "Perfecting the Prepositions in Spanish."
- Weekend (1.23h): Drill + Superbeginner Dreaming Spanish (self-paced comprehensible
  input, Spain-accent hosts).
- Week total: **1.73h**. No checkpoint.

#### Week 14 — Module 5, wk 2/3
- Weekday A (0.42h): Drill + **Application — Read a Sign, Then Ask** (25 min).
- Weekday B (0.33h): Drill + **Application — Shadow a Natural-Pace Exchange** (20 min).
- Weekend (1.73h): Drill + Mi Vida Loca compilation, Episode 3 segment (directions/
  transport — watch only that segment, not the full compilation; see Open Questions).
- Week total: **2.48h**. No checkpoint.

#### Week 15 — Module 5, wk 3/3
- Weekday A (0.25h): Drill + review prepositions/imperatives.
- Weekday B (0.5h): Drill + **Synthesis — Lost in Town Role-Play** (30 min).
- Weekend (1.90h): Drill + remaining Mi Vida Loca / Dreaming Spanish viewing +
  **Module 5 checkpoint** (25 min: directions role-play + listening/reading comprehension).
- Week total: **2.65h**. **Checkpoint: Module 5 check.**

#### Week 16 — Module 6, wk 1/3 (A2.1 → A2.2)
- Weekday A (0.25h): Drill — comparatives & polite requests warm-up.
- Weekday B (0.25h): Drill + SpanishDict comparatives article (~15 min).
- Weekend (0.08h): Drill + begin "How to Order Food" lesson.
- Week total: **0.58h**. No checkpoint.

#### Week 17 — Module 6, wk 2/3
- Weekday A (0.25h): Drill + continue "How to Order Food" lesson.
- Weekday B (0.25h): Drill + Beginner Dreaming Spanish (shopping/food, self-paced).
- Weekend (0.58h): Drill + **Application — Read Then Order** (30 min, recorded role-play).
- Week total: **1.08h**. No checkpoint.

#### Week 18 — Module 6, wk 3/3
- Weekday A (0.25h): Drill + review comparatives.
- Weekday B (0.58h): Drill + **Synthesis — Full Travel Day** (35 min).
- Weekend (1.18h): Drill + **Module 6 checkpoint** (25 min: order/check-in role-play +
  reading) + **Cumulative review — modules 1–6** (25 min, including a re-check of
  distinción against the module 1 clip).
- Week total: **2.01h**. **Checkpoints: Module 6 check + Cumulative review (M1–6).**

#### Week 19 — Module 7, wk 1/3 (A2.2)
- Weekday A (0.25h): Drill — pretérito warm-up.
- Weekday B (0.25h): Drill + review regular preterite forms.
- Weekend (0h): Drill only — module 7's two resources have no confirmed duration (see
  Open Questions); treat this slot as flexible self-paced viewing of "Gordon's Diaries...
  Preterite" at whatever length it actually runs.
- Week total: **0.50h**. No checkpoint.

#### Week 20 — Module 7, wk 2/3
- Weekday A (0.42h): Drill + **Application — Narrate a Real Past Weekend** (25 min, first
  occurrence).
- Weekday B (0.25h): Drill + Language Transfer Track 58 ("the dot in the past," self-paced
  length).
- Weekend (0.25h): Drill + review irregular preterites.
- Week total: **0.92h**. No checkpoint.

#### Week 21 — Module 7, wk 3/3
- Weekday A (0.42h): Drill + **Application — Narrate a Real Past Weekend** (25 min, second
  occurrence, different memory).
- Weekday B (0.5h): Drill + **Synthesis — Trip Story Chain** (30 min).
- Weekend (0.83h): Drill + **Module 7 checkpoint** (20 min: pretérito narration against
  pre-committed answer key).
- Week total: **1.75h**. **Checkpoint: Module 7 check.**

#### Week 22 — Module 8, wk 1/2 (A2.2 → A2.3)
- Weekday A (0.17h): Drill — near-future (ir a + infinitive) warm-up.
- Weekday B (0.17h): Drill + Language Transfer Track 7 ("Voy a," self-paced length).
- Weekend (0.58h): Drill + **Application — Report a Problem** (25 min, recorded
  service/emergency exchange). Rick Steves' travel-Spanish video (self-paced,
  unconfirmed length — flagged in Open Questions).
- Week total: **0.92h**. No checkpoint.

#### Week 23 — Module 8, wk 2/2
- Weekday A (0.17h): Drill + review ir a + infinitive forms.
- Weekday B (0.5h): Drill + **Synthesis — Invite, Plan, and Confirm** (30 min).
- Weekend (0.75h): Drill + **Module 8 checkpoint** (25 min: 3 plans, mock service
  scenario, listening comprehension).
- Week total: **1.42h**. **Checkpoint: Module 8 check.**

#### Week 24 — Module 9, wk 1/3 (A2.3 → B1-threshold)
- Weekday A (0.5h): Drill — self-correction loop + **Application — Listening Without a
  Transcript** (20 min, first scenario).
- Weekday B (0.25h): Drill + Mi Vida Loca full playlist (cumulative listening review,
  self-paced).
- Weekend (1.93h): Drill + Intermediate Dreaming Spanish (natural-pace listening,
  Spain-accent hosts).
- Week total: **2.68h**. No checkpoint.

#### Week 25 — Module 9, wk 2/3
- Weekday A (0.5h): Drill + **Application — Listening Without a Transcript** (20 min,
  second scenario).
- Weekday B (0.33h): Drill + Language Transfer Track 90 (End) — final review track.
- Weekend (2.18h): Drill + remaining Dreaming Spanish/Mi Vida Loca review +
  **Synthesis dry run** — 2-minute rehearsal of the final conversation (20 min).
- Week total: **3.02h**. No checkpoint.

#### Week 26 — Module 9, wk 3/3 — Buffer & final assessment week
No new resource material this week by design — all module 9 viewing is front-loaded into
weeks 24–25 so this week is free for consolidation, testing, and catch-up on anything
that scored "not yet" earlier in the path.
- Weekday A (0.25h): Drill — self-correction loop, final pass.
- Weekday B (0.42h): Catch-up slot — redo any earlier checkpoint or drill that is still
  shaky (Open Questions in `assessments.md` flags distinción and real-time listening as
  the likeliest candidates), or rest if on track.
- Weekend (2.5h): Drill + **Synthesis — The Full 3–5 Minute Conversation** (40 min final
  take) + **Module 9 checkpoint** (30 min) + **Cumulative review — modules 1–9** (25 min)
  + **Final check — full-path assessment** (45 min, may split across this session and the
  extra weekday time if needed).
- Week total: **3.17h** (of 5h budget — 1.83h margin, the largest single-week margin in
  the path, reserved deliberately as the buffer before the deadline).
- **Checkpoints: Module 9 check + Cumulative review (M1–9) + Final check.**

### Load check

Budget is `weekly_hours` = 5.0h; the G1 ceiling (no more than 10% over) is 5.5h. Margin
below is budget minus planned; every value is positive and no week approaches the ceiling.

| Week | Module(s) | Planned h | Budget h | Margin h |
|---|---|---|---|---|
| 1 | 1 | 1.33 | 5.0 | 3.67 |
| 2 | 1 | 1.83 | 5.0 | 3.17 |
| 3 | 1 (+checkpoint) | 1.83 | 5.0 | 3.17 |
| 4 | 2 | 0.83 | 5.0 | 4.17 |
| 5 | 2 | 1.33 | 5.0 | 3.67 |
| 6 | 2 (+checkpoint) | 1.50 | 5.0 | 3.50 |
| 7 | 3 | 0.83 | 5.0 | 4.17 |
| 8 | 3 | 1.33 | 5.0 | 3.67 |
| 9 | 3 (+checkpoint +CR1) | 2.17 | 5.0 | 2.83 |
| 10 | 4 | 0.57 | 5.0 | 4.43 |
| 11 | 4 | 0.90 | 5.0 | 4.10 |
| 12 | 4 (+checkpoint) | 1.73 | 5.0 | 3.27 |
| 13 | 5 | 1.73 | 5.0 | 3.27 |
| 14 | 5 | 2.48 | 5.0 | 2.52 |
| 15 | 5 (+checkpoint) | 2.65 | 5.0 | 2.35 |
| 16 | 6 | 0.58 | 5.0 | 4.42 |
| 17 | 6 | 1.08 | 5.0 | 3.92 |
| 18 | 6 (+checkpoint +CR2) | 2.01 | 5.0 | 2.99 |
| 19 | 7 | 0.50 | 5.0 | 4.50 |
| 20 | 7 | 0.92 | 5.0 | 4.08 |
| 21 | 7 (+checkpoint) | 1.75 | 5.0 | 3.25 |
| 22 | 8 | 0.92 | 5.0 | 4.08 |
| 23 | 8 (+checkpoint) | 1.42 | 5.0 | 3.58 |
| 24 | 9 | 2.68 | 5.0 | 2.32 |
| 25 | 9 | 3.02 | 5.0 | 1.98 |
| 26 | 9 (+checkpoint +CR3 +final check) | 3.17 | 5.0 | 1.83 |
| **Total** | — | **~41.09** (rounding; component sum = 41.10) | **130.0** | **~88.9** |

No week exceeds 5.0h, let alone the 5.5h G1 ceiling; the heaviest week (26) uses 63% of
budget. Gate G1: **pass, with large margin**.

### Deadline check

Total scheduled weeks: **26**. `horizon_weeks`: **26**. 26 ≤ 26 — the path fits inside the
deadline with **zero weeks of calendar slack** (see Open Questions on why a literal extra
buffer week isn't structurally possible here, and how week 26 substitutes for one). Gate
G2: **pass, exactly at the limit, not exceeded**.

## Sources
None.

## Open Questions
- **`resources.md`'s resource-hour data is materially incomplete, and this schedule's
  41.10h total should be read as a floor, not a ceiling.** Modules 7 and 8 have **zero**
  quantified resource duration ("2 unknown" each, no numeric estimate at all in
  `resources.md`'s own coverage table); modules 2, 3, 4, 6, and 9 each carry additional
  "+N unknown" videos on top of their reported partial figure. I did not invent durations
  to fill these gaps — per instruction, I used `resources.md`'s own numbers as given,
  including the zeros for modules 7–8 — but this means weeks 19–23 in particular (module
  7's and 8's weeks) are very likely under-reported, and the schedule's large apparent
  slack (~89h, ~68% of the 130h budget) is partly a measurement gap rather than confirmed
  free time. Recommend the coordinator send resources.md back to the curator for durations
  on the unconfirmed videos before treating this schedule's per-week hours as final; until
  then, the learner should expect actual time spent most weeks to run somewhat higher than
  the table shows, and should use the ample remaining weekly time to simply finish
  whatever length each assigned video/playlist actually is, rather than stopping at a
  quantity implied by this table.
- **Module 5's reported resource figure (~3.7h) looks wrong, not just incomplete.**
  `resources.md`'s own annotation for the Mi Vida Loca compilation cited in module 5 says
  to "watch from that segment" (Episode 3, ~10 minutes) for the directions/transport
  role-play objective — but the coverage table counts the full ~220-minute (22-episode)
  compilation length toward module 5's resource hours. If corrected to the actual assigned
  segment (~0.17h instead of 3.7h), weeks 13–15 would drop by roughly 3.5h combined,
  further flattening an already light stretch of the path. I used the reported 3.7h as
  instructed rather than silently overriding it, but flag it here as the single number in
  `resources.md` I'm most confident is a data-entry error (likely conflating the full
  compilation length with the single-episode segment actually assigned).
- **No literal, wholly separate buffer week exists, by structural necessity, not
  oversight.** `exercises.md`'s own module-to-week apportionment (9, 9, 9, 9, 9, 9, 9, 6, 9
  sessions ÷ the learner's fixed 3 sessions/week) sums to exactly 26 weeks — the same as
  `horizon_weeks` — leaving no room for an additional calendar week without either
  exceeding the horizon (gate G2) or shortening a module's designed session count, which is
  `exercises.md`'s content to own, not this artifact's to change. Instead, I removed all
  new resource content from week 26 (shifting module 9's remaining viewing into weeks
  24–25) so week 26 functions as the de facto buffer/deadline week — consolidation,
  catch-up, the module 9 checkpoint, the cumulative review, and the final check only. This
  achieves the intent of "a full buffer week before the deadline" within a fixed 26-week/
  78-session structure, but it is not literally an empty week; flagging so the validator
  can confirm this satisfies the requirement rather than assuming a blank week exists.
- **Minor rounding note:** `assessments.md`'s summary prose states "about 5.5 hours
  (~325 minutes)" of total assessment time, but its own itemized checkpoints, cumulative
  reviews, and final check sum to exactly 330 minutes (5.50h). I used the itemized total
  (directly computable and verified above) rather than the summary's rounded figure.
- **If the resource-hour gap above turns out to be real** (i.e., the true per-video
  durations really are this short), the path has far more slack than the ~15% a 26-week
  beginner plan should need. In that case, the first thing I would recommend spending the
  recovered time on is **not** additional grammar scope — `curriculum.md` already
  deliberately excluded the imperfect tense, subjunctive, and compound tenses as out of
  reach for the honest 130-hour budget, and that reasoning doesn't change just because
  resource-viewing turned out to be shorter than expected. The better use, per the Open
  Questions independently raised in both `exercises.md` and `assessments.md`, is a live
  conversation partner or tutor session near the end of the path (modules 8–9), since that
  is the one gap self-study and self-scored recordings cannot close at all.
