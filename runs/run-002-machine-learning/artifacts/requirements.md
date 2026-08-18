---
artifact: requirements
owner: requirements-formalizer
run_id: run-002-machine-learning
status: final
attempt: 1
inputs: []
generated: 2026-08-18T00:00:00Z
---

# Requirements — Machine Learning (classical, project-based)

## Summary

The learner wants to reach the point of being able to build and evaluate their own
machine learning models, working from a Python-basics background with no prior
statistics or ML exposure. The confirmed scope is classical machine learning on
tabular data using scikit-learn: training and evaluating both a classifier and a
regressor, with train/test methodology, standard evaluation metrics, and an
understanding of overfitting. Statistics is not a separate module; it is woven into
the modeling modules at the point each concept is first needed. The learner learns
best by building, so the plan is project-first. Two defaults were proposed and
accepted by the user rather than stated up front: the original 4-week deadline was
arithmetically infeasible against the stated 3 hours/week (12 hours total vs. a
25–40 hour minimum for this scope), so the horizon was extended to 10 weeks
(~30 hours total) while keeping weekly hours and the full goal intact; and because
the goal names concrete deliverables (a working classifier and a working regressor),
a capstone was added to the curriculum-architect brief.

## Findings

| Field | Value | Basis |
|---|---|---|
| `goal` | Build and evaluate my own machine learning models | stated |
| `target_outcomes` | See below | inferred |
| `subject` | Machine learning — classical / tabular, scikit-learn ecosystem | inferred (narrowed from user's Q2 answer) |
| `current_level` | Beginner: knows Python basics; no statistics background; no prior ML exposure | stated |
| `weekly_hours` | 3 hours/week | stated |
| `horizon_weeks` | 10 weeks | inferred (user chose to extend the horizon rather than narrow the goal, after being shown the arithmetic; supersedes the original "4 weeks" — see Open Questions) |
| `budget` | 0 — free resources only (hard constraint) | stated |
| `preferred_modality` | project | stated |
| `language` | English | inferred (request was in English; not contradicted) |
| `wants_assessments` | true — lightweight checkpoint after each module | stated |

### Target outcomes

1. Explain and correctly apply a train/test split (and recognize when cross-validation
   is warranted) to a tabular dataset before training a model.
2. Train a classification model with scikit-learn on a tabular dataset and evaluate it
   using accuracy, precision, and recall, interpreting what each metric means for the
   dataset at hand.
3. Train a regression model with scikit-learn on a tabular dataset and evaluate it
   using an appropriate error metric (e.g., MAE or RMSE), interpreting the result.
4. Diagnose overfitting vs. underfitting in a trained model (e.g., via train/test
   performance gap or a learning curve) and describe at least one mitigation.
5. Apply just-enough statistics — mean/variance, basic probability, and distributions —
   correctly in context when preparing data or interpreting model output, without a
   standalone statistics module.
6. Complete a capstone project: build and evaluate at least one classifier and one
   regressor end-to-end on a self-chosen or provided tabular dataset, using only free
   resources and tools.

## Sources

None.

## Open Questions

- **Original deadline superseded.** The raw request stated "done in 4 weeks." At
  3 hours/week that is 12 total hours against an estimated 25–40 hour minimum for this
  scope (classifier + regressor + evaluation + woven-in statistics + capstone). The
  user was shown this arithmetic and chose option A: extend the horizon to 10 weeks
  (top of the offered 8–10 week range), keep weekly hours at 3, and keep the goal
  fully intact. **Gate G2 (deadline) must check against horizon_weeks = 10, not the
  original 4 weeks.** This is a deliberate, explicit user decision, not a scaled-down
  goal.
- **Free-only is a hard constraint.** `budget = 0` means every single resource in
  `resources.md` must be free to access — no paid courses, no paywalled books, no
  trial-only platforms. Gate G3 should treat `0` as "free-only," not "unspecified."
- **Scope boundary.** Deep learning, neural networks, and non-tabular data (images,
  text, etc.) are explicitly out of scope per the user's Q2 answer. The
  curriculum-architect should not introduce them even as stretch content, since the
  time budget (30 hours) has no room for it.
- **No standalone statistics module.** Per the user's Q3 answer, statistics content
  (mean/variance, probability basics, distributions) must be distributed across the
  modeling modules at the point of need, not built as its own module or week. This is
  a structural instruction for `curriculum-architect`.
- **Secondary modality.** None stated — the user gave a single clear preference
  (project-based) with no secondary modality mentioned. `preferred_modality = project`
  is unambiguous; no fallback needed for the curator selection.
- **Capstone.** The goal explicitly names concrete deliverables (a working classifier,
  a working regressor, both evaluated), so a capstone project is warranted and should
  be included in the `curriculum-architect` brief, most likely as the final module
  within the 10-week horizon.
