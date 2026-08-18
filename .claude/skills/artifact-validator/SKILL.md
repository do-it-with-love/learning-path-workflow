---
name: artifact-validator
description: The canonical structure every workflow artifact must follow, plus the structural and citation check applied to an artifact before dependent work proceeds. Load this before writing ANY artifact under runs/<run-id>/artifacts/ or runs/<run-id>/output/, and before validating one.
---

# Artifact contract

Every artifact in this workflow is a human-readable Markdown file with the exact
structure below. Structure is what makes repeated runs on the same input produce
comparable documents, and it is enforced by `no_leak_guard.py` — a write that breaks
the frontmatter rules is denied, not silently accepted.

## Required shape

```markdown
---
artifact: <slug matching the filename stem, e.g. curriculum>
owner: <the step name from pipeline.json that owns this file>
run_id: <run-id>
status: draft | final
attempt: <integer, 1 on first write, incremented on each retry>
inputs:
  - artifacts/requirements.md
  - artifacts/baseline-assessment.md
generated: <UTC ISO-8601, e.g. 2026-08-18T14:02:11Z>
---

# <Human title>

## Summary
## Findings
## Sources
## Open Questions
```

### Rules

1. **`owner` must match** the owning step in `.claude/workflow/pipeline.json` for this
   artifact path. For the `curator` slot, `owner` is `curator` regardless of which
   variant agent ran; name the variant in `## Summary`.
2. **All four `##` sections are mandatory** and appear in that order. A section with
   nothing to say contains the single line `None.` — never omit the heading.
3. **`inputs` lists every artifact you actually read.** This is what makes the
   dependency graph auditable after the fact.
4. **`attempt`** must equal the attempt number the coordinator gave you. It is how a
   reader tells a first draft from a gate-driven revision.
5. Content beyond the four sections is allowed *inside* them (sub-headings, tables,
   checklists) but no new top-level `##` sections.

### Section meanings

- **Summary** — 3–6 sentences. What this artifact decides, and the one or two
  judgement calls a reader should know about. For `curator`, state which variant ran.
- **Findings** — the actual substance: the modules, the resources, the schedule.
  Use tables where the data is tabular.
- **Sources** — every external source used, in the citation format below. `None.` is
  only acceptable for artifacts that consume no external data
  (`exercises`, `assessments`, `schedule`, `effort-budget`).
- **Open Questions** — anything you had to assume. Assumptions belong here, never
  buried in prose. Downstream agents read this section.

## Citation format

One source per line, in `## Sources` and inline where a claim depends on it:

```
- [Title](https://url) — provider · year · format · duration · cost · verified: <method> <YYYY-MM-DD>
```

`<method>` is one of `mcp:wikipedia`, `mcp:openlibrary`, `webfetch`, `websearch`.
It records **how the URL was confirmed to exist during this run**. A citation whose
method is missing, or that was written from model memory, fails gate G7.

Unknown fields are written as `unknown`, never guessed. `cost` uses the run's currency
or the literal `free`.

# Validation procedure

Apply this when checking an artifact, whether as its author before writing or as the
`validator` step.

## Structural checks

- [ ] Frontmatter parses as YAML and has all seven keys.
- [ ] `artifact` matches the filename stem; `owner` matches `pipeline.json`.
- [ ] All four `##` sections present, in order, none empty.
- [ ] Every path in `inputs` exists in this run.
- [ ] No internal machinery leaks into `output/` files: no `artifacts/` paths, no
      `state/` paths, no agent or step names. Those belong to the workflow, not the
      learner.

## Citation checks

- [ ] Every resource line matches the citation format.
- [ ] Every line carries a `verified:` method and a date from **this run**.
- [ ] No two resources share a URL (gate G6).
- [ ] URLs are specific pages, not bare domains or search-result URLs.

## Reporting

Report each problem as one line:

```
<ARTIFACT> <SECTION> — <what is wrong> — fix: <the concrete correction>
```

Never fix an artifact you do not own. Report it and let the coordinator re-run the
owning step.
