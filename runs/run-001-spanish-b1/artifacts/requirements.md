---
artifact: requirements
owner: requirements-formalizer
run_id: run-001-spanish-b1
status: final
attempt: 1
inputs: []
generated: 2026-08-18T00:00:00Z
---

# Requirements — Conversational European Spanish for Travel

## Summary
The learner wants practical, spoken European (Castilian) Spanish for an upcoming trip to
Spain, starting from an absolute-beginner baseline (~200 words, no grammar), studying 5
hours/week for 26 weeks (~130 hours total) on a €50 budget, primarily via video lessons
with dedicated speaking practice. The original request named "conversational Spanish
(B1)" as the goal; after being shown that certified B1 typically requires 350–400 hours
of study against a budget of only ~130 hours, the learner explicitly chose to keep the
5h/week and 26-week constraints fixed and retarget the goal to a realistic **strong
A2 / B1-threshold** level — practical conversational competence for travel, not a
certified full B1. This retargeting is a stated decision, not a default. Two defaults
were proposed and accepted implicitly by omission: `budget` currency is EUR as stated
(no ambiguity), and no other fields required defaulting — all ten fields were either
stated directly or resolved through the clarifying Q&A.

## Findings

| Field | Value | Basis |
|---|---|---|
| `goal` | Reach practical conversational competence in European (Castilian) Spanish for travel in Spain — a realistic strong-A2/B1-threshold level, not certified full B1 | inferred (retargeted from stated goal after feasibility check; confirmed by user) |
| `target_outcomes` | See list below | inferred (derived from goal, modality, and speaking-practice requirement) |
| `subject` | Spanish — European/Castilian variant specifically (pronunciation, vocabulary, register); Latin American variants out of scope | stated |
| `current_level` | Absolute beginner — ~200 words from casual exposure, no grammar, no prior study or classes | stated |
| `weekly_hours` | 5 hours/week | stated |
| `horizon_weeks` | 26 weeks (6 months) | stated |
| `budget` | EUR 50 total | stated |
| `preferred_modality` | video (primary) | stated |
| `language` | English (language of instruction/resources) | stated |
| `wants_assessments` | true — include checkpoints and quizzes | stated |

### Target outcomes
1. Hold a 3–5 minute spoken conversation in European Spanish covering daily routine,
   personal introductions, and travel needs (ordering food, asking directions, checking
   into lodging), using present tense and common past-tense forms.
2. Understand and respond appropriately to slow-to-natural-paced spoken Spanish from a
   native (Peninsular) speaker in common travel scenarios (transport, restaurants,
   shops, emergencies).
3. Produce correct basic grammar in speech: present tense conjugation (regular and
   common irregular verbs), ser/estar distinction, basic past tense (pretérito), and
   simple future/near-future (ir a + infinitive).
4. Read and understand short everyday texts (menus, signs, simple messages, basic
   travel information) in European Spanish.
5. Demonstrate active vocabulary of approximately 800–1000 words centered on travel,
   daily life, and social interaction, with pronunciation and register matching
   Peninsular Spanish (vosotros forms, distinción/ceceo-relevant listening exposure).

## Sources
None.

## Open Questions
- **Feasibility arithmetic (resolved):** Certified B1 typically requires ~350–400 hours
  of instruction; at 5h/week × 26 weeks the learner has ~130 hours available — roughly a
  third of what full B1 needs. The learner was shown this and chose option (c): keep
  5h/week and the 26-week horizon fixed, and retarget the goal to strong A2/B1-threshold
  practical conversational competence rather than scale up hours or extend the horizon.
  This is recorded here so curriculum-architect and validator (gates G1/G2) plan and
  check against the honest target, not the originally stated "B1" label.
- **Secondary modality preference:** The learner named "video lessons and speaking
  practice" — `preferred_modality` is resolved to `video` as the single primary curator
  variant, but speaking/conversation practice is carried as a first-class requirement in
  target outcomes 1–3 above so that `exercise-designer` builds dedicated speaking
  practice into the plan even though the curator sources video resources. The curator
  should note in `resources.md` if any sourced videos include interactive/conversation
  components.
- **Budget allocation:** €50 total is a small budget for 6 months of content; it is
  assumed to cover optional paid subscriptions, apps, or one-off resource purchases,
  not tutoring. Not confirmed with the learner beyond the stated figure — curator should
  favor free resources and treat €50 as a ceiling, not a target to spend.
- **Assessor mode:** Because `current_level` is confirmed absolute beginner with no
  prior study, `knowledge-assessor` should run in `light` mode with a zero baseline
  asserted rather than running a full diagnostic.
