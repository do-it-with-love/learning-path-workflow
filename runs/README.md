# Recorded runs

Each run directory is a complete, auditable execution:

```
runs/<run-id>/
├── input.md                        the original request, verbatim
├── artifacts/                      every intermediate artifact, in Markdown
├── output/learning-path.md         the document the human approved
├── output/learning-path.html       the final guide
└── state/
    ├── workflow-state.json         step statuses, digests, attempts, gates, history
    ├── approval-request.json       the digest a human was asked to approve
    └── approval.json               the recorded human decision
```

Inspect any run without starting Claude:

```bash
python3 ../scripts/runctl.py status <run-id>
```

## The three scenarios

These exist to demonstrate different failure and recovery behaviour, not just that the
happy path works. Run them in order; the run ids are assigned by `runctl.py init`.

### 1. `spanish-b1` — happy path, video modality

Exercises: clarifying Q&A, both parallel groups, all nine gates passing first time,
approval, render.

```
/build-learning-path I want to reach conversational Spanish (B1) in 6 months. I know about
200 words and no grammar. 5 hours a week, budget around €50, I learn best from video
lessons and speaking practice. I'm travelling to Spain so I want European Spanish.
```

### 2. `ml-crash` — gate failure, targeted retry, cascade

Deliberately over-constrained: the goal cannot fit the time budget, so gates G1 and G2
fail. Expect `schedule-planner` to be retried, then `curriculum-architect` to re-scope,
which cascades and regenerates groups 4 and 5 before the gates pass. The state file's
`attempts` counters and `stale_cause` fields are the evidence.

```
/build-learning-path I want to learn machine learning well enough to build and evaluate my
own models. I can do 3 hours a week and I want it done in 4 weeks. Free resources only.
I know Python basics but no statistics. I learn best by building projects.
```

### 3. `music-theory` — interruption, resume, and rejection

Exercises the reading curator (and therefore the Open Library MCP), recovery from an
interrupted run, and the human rejection loop.

```
/build-learning-path I want to understand music theory well enough to read a score and
analyse a simple piece — key, chords, form. About 4 hours a week for 12 weeks. I play
piano at a beginner-intermediate level and read treble clef slowly. Budget £30. I prefer
books and written material over video.
```

To exercise the interruption: interrupt the run after group 4 completes (Ctrl-C, or close
the session), then in a new session run `/resume-learning-path <run-id>`. Confirm from
`status` that the completed steps are not repeated.

To exercise the rejection loop, reject the first draft with concrete feedback:

```
/approve-learning-path <run-id> --reject "too much analysis theory up front — I want to be
playing and analysing real pieces from week 2, and add a short weekly practice piece"
```

then approve the revision.
