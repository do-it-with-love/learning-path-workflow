---
artifact: requirements
owner: requirements-formalizer
run_id: run-003-music-theory
status: final
attempt: 1
inputs: []
generated: 2026-08-18T15:00:00Z
---

# Requirements — Music Theory for Score Reading and Analysis

## Summary

The learner wants to build enough music theory to read a piano score fluently in both
clefs and analyse a simple piece for key, chords, and form, working toward a concrete
capstone analysis of a standard beginner-appropriate piece (e.g. a Bach minuet or
Clementi sonatina, chosen by the curriculum). They play piano at a beginner-intermediate
level, know note names and the major scale but not chord construction or Roman-numeral
analysis, and read both treble and bass clef slowly. They have 4 hours/week for 12
weeks (48 hours total), a £30 budget, want the plan built primarily from books and
written material, and want short quizzes/checkpoints included. One default was
proposed rather than stated: `language` is set to English, inferred from the request
language since no other language was mentioned.

## Findings

| Field | Value | Basis |
|---|---|---|
| `goal` | Understand music theory well enough to read a piano score in both clefs and analyse a simple piece — key, chords, form | stated |
| `subject` | Music theory (applied to piano score reading) | stated |
| `current_level` | Beginner in formal theory (knows note names and the major scale; no chord construction or Roman-numeral analysis yet); beginner-intermediate pianist; reads both treble and bass clef slowly, roughly equally | stated |
| `weekly_hours` | 4 hours/week | stated |
| `horizon_weeks` | 12 weeks (48 hours total budget) | stated |
| `budget` | £30 | stated |
| `preferred_modality` | reading (books and written material, explicitly preferred over video) | stated |
| `language` | English | defaulted |
| `wants_assessments` | Yes — short quizzes/checkpoints along the way | stated |

### Target outcomes

1. Read and correctly name notes and rhythms in both treble and bass clef for a simple
   piano piece at a comfortable working tempo, with noticeably improved speed over the
   starting "slow" baseline.
2. Given a simple piece's key signature and opening/closing cadence, correctly identify
   its key (including distinguishing relative major/minor where relevant).
3. Label the chords of a simple piece using triad identification and basic
   Roman-numeral or lead-sheet analysis (I, IV, V, vi and simple seventh chords).
4. Identify the formal structure of a simple piece (e.g. phrase structure, binary or
   ternary form) and describe how the sections relate.
5. Produce a written analysis of one capstone piece — a standard beginner-appropriate
   work such as a Bach minuet or Clementi sonatina, selected during curriculum design —
   that combines key, chord, and form analysis into a coherent whole.

## Sources

None.

## Open Questions

- **Capstone deliverable**: the learner did not name a specific piece. They asked the
  curriculum to choose one (example given: a Bach minuet or Clementi sonatina). This is
  treated as a concrete deliverable, so `curriculum-architect` should select and name a
  specific, appropriately simple piece and structure the capstone module around it.
- **Secondary modality preference**: none was stated. The learner's preference for
  books/written material over video was explicit and unqualified — no video component
  should be assumed. `preferred_modality` therefore resolves cleanly to `reading` with
  no secondary noted for the curators.
- **Language**: not stated by the learner; defaulted to English based on the language of
  the request. If the learner wants resources in another language, this should be
  raised before curation runs.
- **Feasibility check**: 4 hours/week x 12 weeks = 48 hours total against a beginner
  starting point (knows notes and major scale only) is a realistic budget for reaching
  basic key/chord/form analysis on simple repertoire; no arithmetic conflict was found
  between goal, hours, and horizon.
