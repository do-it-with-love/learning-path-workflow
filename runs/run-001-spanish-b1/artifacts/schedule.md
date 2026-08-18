---
artifact: schedule
owner: schedule-planner
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
generated: 2026-08-19T12:00:00Z
---

# Schedule — Conversational European Spanish for Travel

## Summary
This is a **revision** of the attempt-1 schedule, triggered because `resources.md` was
rewritten upstream to fix gates G7 and G8 (a dead citation replaced, two resources
correctly relabeled, one resource added). The schedule's shape is unchanged: **exactly 26
weeks** (matching `horizon_weeks`, gate G2 satisfied with zero weeks to spare), the same
78-session / 26-week structure driven by `exercises.md`'s fixed session counts (unchanged
from attempt 1), and the same three-sessions-a-week pattern — two ~1.5h weekday evenings,
one ~2h weekend block, 5h/week nominal. Re-summing the **real** hours reported by the
revised `resources.md` + `exercises.md` (unchanged) + `assessments.md` (unchanged) gives
**40.90 hours** of accounted content, down **0.20h** from attempt 1's 41.10h — the only
arithmetic change, and it moves in the honest direction, not a convenient one: module 4's
"Free Spanish Podcast 17" had its false "10 min 38 sec (confirmed)" duration corrected to
`unknown`, so its 0.20h no longer counts toward the quantified floor. Everything else that
changed in `resources.md` (module 5's dead citation replaced with "Directions in Spanish";
module 6 gaining "Making Comparisons in Spanish"; "How to Order Food" correctly relabeled
`audio`) involved resources that were already `unknown`-duration or already had no numeric
contribution, so those changes are reflected in this schedule's session **content** but not
its **arithmetic**. Every week still clears gate G1 with large margin — the heaviest week
(26) uses 3.17h against the 5h budget (2.33h under the 5.5h/+10% ceiling, unchanged from
attempt 1), and the one week whose numbers moved (week 11) only gained margin (4.10h →
4.30h). **How unknown-duration resources are handled, stated explicitly per this attempt's
instruction:** every resource `resources.md` marks `unknown` contributes **zero** hours to
this schedule's quantified per-module and per-week totals — durations are never invented.
Where an unknown-duration resource is the only new material in a session, that session's
quantified time reflects only the recurring drill and any `exercises.md` application task,
and the resource is scheduled as self-paced viewing "at whatever length it actually runs,"
flagged inline. This is deliberately conservative: it means the true time spent some weeks
will run a little higher than the table shows, not lower — and because the smallest margin
anywhere in the path is still 2.33h against the 5.5h ceiling (week 26), that gap is
comfortably absorbed. Speaking practice is scheduled every week without exception, because
`exercises.md`'s recurring warm-up drill runs at the start of every session in every module.
The schedule fits the deadline exactly (26 of 26 weeks) and does not use anywhere near the
full weekly budget — that is flagged, not hidden.

## Findings

### Real hours per module (the arithmetic)

Resource hours are `resources.md`'s own "Approx. resource hours" figures per module (the
**quantified** portion only — every `unknown`-duration resource contributes 0, per the
unknown-duration handling rule stated in the Summary and repeated in Open Questions).
Practice hours are `exercises.md`'s per-module practice-load table, taken as reported
(unchanged from attempt 1). Checkpoint hours are `assessments.md`'s per-checkpoint minutes,
converted to hours and taken as reported (unchanged from attempt 1).

| Module | Resource h (resources.md, attempt 2) | Practice h (exercises.md) | Checkpoint h (assessments.md) | Total h | Changed from attempt 1? |
|---|---|---|---|---|---|
| 1. Sounds, Script & Survival Basics | 2.50 | 2.17 | 0.33 (20 min) | 5.00 | no |
| 2. Being & Describing | 1.00 | 2.33 | 0.33 (20 min) | 3.66 | no |
| 3. Present-Tense Action | 1.00 | 2.50 | 0.42 (25 min) | 3.92 | no |
| 4. Daily Life & Routine | **0.00** | 2.67 | 0.33 (20 min) | **3.00** | **yes — was 0.20; "Free Spanish Podcast 17"'s duration was corrected from a false "confirmed" figure to honest `unknown`** |
| 5. Getting Around | 3.70 | 2.75 | 0.42 (25 min) | 6.87 | no (dead citation replaced with an equally-unknown one — see Open Questions) |
| 6. Eating, Shopping & Lodging | 0.25 | 2.58 | 0.42 (25 min) | 3.25 | no (new video added, but it is unknown-duration; audio relabel is a modality fix, not an hours fix) |
| 7. Talking About the Past | 0 (unquantified) | 2.83 | 0.33 (20 min) | 3.16 | no |
| 8. Plans, Requests & Unexpected Situations | 0 (unquantified) | 1.92 | 0.42 (25 min) | 2.34 | no |
| 9. Conversation Consolidation | 3.70 | 3.50 | 0.50 (30 min) | 7.70 | no |
| Cumulative reviews (after M3, M6, M9 — 25 min each) | — | — | 1.25 (75 min) | 1.25 | no |
| Final check (full-path assessment) | — | — | 0.75 (45 min) | 0.75 | no |
| **Total** | **12.15** | **23.25** | **5.50 (330 min)** | **40.90** | **down 0.20 from 41.10** |

Column checks: resource 2.50+1.00+1.00+**0.00**+3.70+0.25+0+0+3.70 = **12.15** (was 12.35).
Practice 2.17+2.33+2.50+2.67+2.75+2.58+2.83+1.92+3.50 = **23.25** (matches `exercises.md`'s
own stated total exactly, unchanged). Checkpoint
0.33+0.33+0.42+0.33+0.42+0.42+0.33+0.42+0.50+1.25+0.75 = **5.50** (unchanged). Grand total
12.15+23.25+5.50 = **40.90h** against a 130h budget (26 weeks × 5h) — **89.10h** of headroom
(up from 88.90h in attempt 1, because the schedule now claims 0.20h less certainty).

### What changed in `resources.md` and how it was handled here

| Change in `resources.md` (attempt 2) | Effect on this schedule |
|---|---|
| Module 5: dead "Perfecting the Prepositions in Spanish" citation removed, replaced with "Directions in Spanish" (LightSpeed) | Both were/are `unknown` duration — **no hour change**. Week 13's session content updated to name the new resource. |
| Module 6: new video "Making Comparisons in Spanish" (LightSpeed) added | `unknown` duration — **no hour change**. Added to week 16–17 session content as a supplementary video alongside the existing SpanishDict article, both covering the same comparatives objective. |
| Module 6: "How to Order Food in Spanish" relabeled from ambiguous "video/podcast" to `audio` | Modality bookkeeping only (relevant to gate G8, owned by `curator`) — **no hour or session-placement change**; it was already `unknown` duration. |
| Module 4: "Free Spanish Podcast 17" relabeled from `audio` to `video`, and its duration corrected from a false "10 min 38 sec (confirmed)" to honest `unknown` | **Hour change**: module 4's resource-hour floor drops from 0.20h to 0.00h. This is the only arithmetic change in the whole schedule — reflected in week 11 below. |

### Module → week apportionment

Unchanged from attempt 1: each module's exercises are designed around a fixed session
count (9 sessions for every module except module 8's 6), and the learner has exactly 3
sessions/week — so weeks per module are fixed at session-count ÷ 3, not a free scheduling
choice, and `exercises.md` was not revised this attempt:

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
with no spare week (see Open Questions on why a literal extra buffer week isn't
structurally possible here, and how week 26 substitutes for one).

### Week-by-week plan

Each week: two weekday evening sessions (drills, vocabulary, shadowing — short and
retrieval-heavy) and one weekend session (new resource material, longer application/
synthesis speaking tasks, checkpoints). Every session opens with that module's recurring
speaking drill, so speaking practice appears in all 78 sessions across all 26 weeks. Only
week 11 differs numerically from attempt 1; every other week below is unchanged, with weeks
13, 16 and 17 updated in content (not hours) to reflect the revised resource list.

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
- Weekday A (0.25h): Drill + LightSpeed question-words podcast (confirmed by WebFetch in
  `resources.md` attempt 2 to be genuine video; unknown duration, self-paced).
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
- Weekday B (0.15h): Drill + brief vocabulary review (module 4's resources are now, per
  `resources.md` attempt 2, entirely unknown-duration — see Open Questions; treat this slot
  as light self-paced viewing).
- Weekend (0.17h): Drill + "14 Tell Time in Spanish."
- Week total: **0.57h**. No checkpoint.

#### Week 11 — Module 4, wk 2/3 — *the one week with a numeric change this attempt*
- Weekday A (0.25h): Drill + "44 Verbs like Gustar."
- Weekday B (0.33h): Drill + **Application — Narrate Your Actual Day** (20 min, first
  occurrence, recorded).
- Weekend (**0.12h**, down from 0.32h): Drill only. "Free Spanish Podcast 17" (Daily
  Routine) is now genuinely video (corrected from a mislabeled "audio podcast") but its
  duration is now honestly `unknown` — the attempt-1 figure of "10 min 38 sec (confirmed)"
  could not actually be verified (the page's player renders via JavaScript this run's tools
  do not execute) and has been withdrawn by the curator. Watch it self-paced, at whatever
  length it actually runs; not counted in the quantified total, the same treatment given to
  every other unknown-duration resource in this path (e.g. modules 7 and 8 below).
- Week total: **0.70h** (down from 0.90h in attempt 1 — the full 0.20h reduction lands
  here, since this is where the corrected resource sits).
- No checkpoint.

#### Week 12 — Module 4, wk 3/3
- Weekday A (0.25h): Drill + "30 Test your listening skills."
- Weekday B (0.33h): Drill + **Application — Narrate Your Actual Day** (20 min, second
  occurrence, different day).
- Weekend (1.15h): Drill + **Synthesis — The Full Day, In Character** (30 min) +
  **Module 4 checkpoint** (20 min: 60-sec routine narration).
- Week total: **1.73h**. **Checkpoint: Module 4 check.**

#### Week 13 — Module 5, wk 1/3 (A2.1)
- Weekday A (0.25h): Drill — directions warm-up.
- Weekday B (0.25h): Drill + **"Directions in Spanish"** (LightSpeed) — *new this
  attempt, replacing the dead "Perfecting the Prepositions in Spanish" citation, which
  resolved to a paid Amazon workbook page and has been removed from `resources.md`.* The
  replacement is WebFetch-confirmed free and covers the same objective (prepositions of
  place, imperative direction-giving); duration is `unknown`, same as the citation it
  replaces, so this session's hour figure is unchanged.
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
- Weekday B (0.25h): Drill + SpanishDict comparatives article (~15 min) + **"Making
  Comparisons in Spanish"** (LightSpeed) — *new video resource this attempt*, watched as
  reinforcement immediately after the article since both cover más/menos...que and
  tan...como; duration is `unknown`, so it adds no quantified hours to this session, but is
  a genuine additional resource, not a placeholder.
- Weekend (0.08h): Drill + begin "How to Order Food in Spanish" lesson (now correctly
  labeled `audio` in `resources.md` attempt 2 — it was never a video, only the label was
  wrong; no change to what is actually being listened to or when).
- Week total: **0.58h**. No checkpoint.

#### Week 17 — Module 6, wk 2/3
- Weekday A (0.25h): Drill + continue "How to Order Food" audio lesson.
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
Only week 11 differs from attempt 1 (0.90h → 0.70h, margin 4.10h → 4.30h); every other row
is unchanged.

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
| 11 | 4 | **0.70** | 5.0 | **4.30** |
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
| **Total** | — | **~40.89** (rounding; component sum = 40.90) | **130.0** | **~89.11** |

No week exceeds 5.0h, let alone the 5.5h G1 ceiling; the heaviest week (26) uses 63% of
budget and has a 2.33h margin against the 5.5h ceiling — the smallest such margin in the
path, and unchanged from attempt 1 since week 26 was not affected by the resources.md
revision. Gate G1: **pass, with large margin**.

### Deadline check

Total scheduled weeks: **26**. `horizon_weeks`: **26**. 26 ≤ 26 — the path fits inside the
deadline with **zero weeks of calendar slack** (see Open Questions on why a literal extra
buffer week isn't structurally possible here, and how week 26 substitutes for one). This is
unchanged from attempt 1: the module→week apportionment is driven by `exercises.md`'s
session counts, which were not revised this attempt. Gate G2: **pass, exactly at the
limit, not exceeded**.

## Sources
None.

## Open Questions
- **How unknown-duration resources are handled (restated here per this attempt's explicit
  instruction, in addition to the Summary).** 17 of `resources.md`'s 27 resources (up from
  15 of 26 in attempt 1) carry `unknown` individual duration — a net increase, but an
  honest one: the curator's attempt-2 revision corrected a false "confirmed" duration
  (module 4) to `unknown` rather than inventing new false precision. Every one of these 17
  contributes **exactly 0 hours** to this schedule's quantified totals; none is estimated
  or guessed. Modules 7 and 8 still have **zero** quantified resource duration at all (both
  their resources are unknown); module 4 now joins them at zero (down from a false 0.20h).
  Modules 2, 3, 5, 6, and 9 each carry a mix of one "(est.)" figure plus additional unknown
  resources on top. This means the schedule's 40.90h total and ~89.1h of apparent slack
  should be read as a **floor**, not a ceiling: actual time spent most weeks will likely run
  somewhat higher than the table shows, especially in weeks 10–11, 19, and 22 where no
  resource duration is quantified at all. This is safe precisely because margins are wide —
  the smallest margin anywhere in the path is 2.33h against the 5.5h G1 ceiling (week 26)
  and 1.83h against the 5.0h nominal budget — comfortably able to absorb generous real
  lengths for 17 unquantified resources without any week coming close to breaching gate G1.
  I did not close this gap by estimating; per instruction, that is `resources.md`'s data to
  supply, not this artifact's to invent.
- **Module 5's reported resource figure (~3.7h) still looks wrong, not just incomplete —
  unchanged from attempt 1.** `resources.md`'s own annotation for the Mi Vida Loca
  compilation cited in module 5 says to "watch from that segment" (Episode 3, ~10 minutes)
  for the directions/transport role-play objective — but the coverage table counts the full
  ~220-minute (22-episode) compilation length toward module 5's resource hours. This was
  not touched in the attempt-2 revision (the curator's changes to module 5 were limited to
  replacing the dead "Perfecting the Prepositions" citation). If corrected to the actual
  assigned segment (~0.17h instead of 3.7h), weeks 13–15 would drop by roughly 3.5h
  combined, further flattening an already light stretch of the path. I used the reported
  3.7h as instructed rather than silently overriding it, but flag it again as the single
  number in `resources.md` I'm most confident is a data-entry error.
- **No literal, wholly separate buffer week exists, by structural necessity, not
  oversight.** `exercises.md`'s own module-to-week apportionment (9, 9, 9, 9, 9, 9, 9, 6, 9
  sessions ÷ the learner's fixed 3 sessions/week) sums to exactly 26 weeks — the same as
  `horizon_weeks` — leaving no room for an additional calendar week without either
  exceeding the horizon (gate G2) or shortening a module's designed session count, which is
  `exercises.md`'s content to own, not this artifact's to change. Instead, week 26 is
  stripped of all new resource content (module 9's viewing is front-loaded into weeks
  24–25) so it functions as the de facto buffer/deadline week — consolidation, catch-up,
  the module 9 checkpoint, the cumulative review, and the final check only. Unchanged from
  attempt 1.
- **Minor rounding note, unchanged from attempt 1:** `assessments.md`'s summary prose
  states "about 5.5 hours (~325 minutes)" of total assessment time, but its own itemized
  checkpoints, cumulative reviews, and final check sum to exactly 330 minutes (5.50h). I
  used the itemized total (directly computable and verified above) rather than the
  summary's rounded figure.
- **If the resource-hour gaps above turn out to be real** (i.e., the true per-video
  durations really are this short, and module 5's figure really is corrected downward), the
  path has even more slack than the ~15%+ a 26-week beginner plan should need. In that
  case, the recommendation is unchanged from attempt 1: the recovered time should **not**
  go toward additional grammar scope — `curriculum.md` deliberately excluded the imperfect
  tense, subjunctive, and compound tenses as out of reach for the honest 130-hour budget,
  and that reasoning does not change because resource-viewing turned out to be shorter than
  expected. The better use, per Open Questions independently raised in `exercises.md` and
  `assessments.md`, is a live conversation partner or tutor session near the end of the
  path (modules 8–9) — the one gap self-study and self-scored recordings cannot close.
