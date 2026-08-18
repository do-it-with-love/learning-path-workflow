---
name: resource-vetting
description: Rubric for finding, judging and citing learning resources for any subject — authority, recency, level fit, cost, accessibility — plus the rule that every recommendation must be verified against a live external source this run. Load before sourcing any learning resource and when checking gate G7 or G8.
---

# Resource vetting

The workflow's credibility rests on one rule:

> **Never recommend a resource from memory.** Every resource must be confirmed to
> exist during this run, via an MCP server, WebSearch, or WebFetch, and the
> confirmation method recorded in its citation.

A plausible-sounding course that does not exist is worse than a mediocre one that does.

## Where to look, in order of preference

| Source | Use for | Records |
|---|---|---|
| `openlibrary` MCP (custom) | Books, textbooks, workbooks | Title, authors, year, ISBN, subjects, ebook availability |
| `wikipedia` MCP (community) | Subject decomposition, terminology, canonical topic structure, named methods and schools | Article existence and section structure |
| WebSearch | Courses, videos, interactive platforms, articles | Live URLs |
| WebFetch | Confirming a specific page exists and says what you claim | HTTP reachability + content |

Prefer an MCP-verified resource over a search-only one when both fit; MCP results carry
structured metadata that survives into the citation.

## The rubric

Score every candidate on all six. Reject anything scoring `poor` on **Authority**,
**Level fit**, or **Accessibility**.

1. **Authority** — Who made it? A recognised institution, publisher, standards body, or
   a practitioner with a track record. Anonymous content farms and AI-generated listicles
   are rejected.
2. **Recency** — Does the subject decay? Software and exam syllabi decay fast; music
   theory and classical languages barely at all. Judge against the subject, not the
   calendar. Note the year in the citation either way.
3. **Level fit** — Matches the learner's assessed baseline for the module it serves,
   not the subject overall. A superb advanced text is a *poor* fit for module 1.
4. **Cost** — Must fit the run's budget. When the budget is `free`, a resource with a
   paywalled core is rejected even if a free sample exists. Note free tiers explicitly.
5. **Accessibility** — Available in the learner's stated language, in their region, and
   without an institutional login they do not have. Note captions or transcripts when
   the learner asked for video.
6. **Time honesty** — Record the *real* time to work through it, including exercises,
   not the marketing "2 hours". If unknown, write `unknown` rather than inventing a number.

## Coverage rules

- Every module gets **at least one** resource and **at most four**. More than four is
  not thoroughness, it is an unmade decision.
- Do not reuse a URL across modules (gate G6). Cite a specific chapter or lesson anchor
  when the same work legitimately serves two modules.
- At least **70%** of resources must match the learner's confirmed preferred modality
  (gate G8). The remainder may differ where the subject demands it — say why in
  `## Open Questions`.
- Spread across providers. Six modules all pointing at one YouTube channel is a
  single point of failure, not a curriculum.

## Citation

Use the format defined in the `artifact-validator` skill:

```
- [Title](https://url) — provider · year · format · duration · cost · verified: <method> <YYYY-MM-DD>
```

Write `unknown` for any field you could not establish. Guessing a field is a G7 failure
just as surely as inventing the resource.
