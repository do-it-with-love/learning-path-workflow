# Personalized Learning Assistant

An agentic workflow for Claude Code that turns *"I want to learn X"* into a validated,
week-by-week study plan for any subject — languages, music, exam prep, software — delivered
as Markdown and a standalone HTML guide.

```
/build-learning-path I want to reach conversational Spanish (B1) in 6 months.
                     I know about 200 words and no grammar. 5 hours a week,
                     budget around €50, I learn best from video and speaking practice.
```

A coordinator gathers requirements, plans the work, picks which subagents to run, executes
them in parallel where the dependencies allow, enforces nine quality gates with targeted
retries, and refuses to produce the final guide until a human has explicitly approved it.

**The reliability guarantees are enforced by hooks and scripts, not by prompting.** A model
cannot approve its own output, cannot skip a quality gate, cannot write another agent's
artifact, and cannot render a document that differs by one byte from what a human approved.
See [CLAUDE.md](CLAUDE.md) for how each guarantee is implemented.

---

## Prerequisites

| Requirement | Notes |
|---|---|
| **Claude Code** | The workflow is a set of Claude Code commands, agents, skills and hooks |
| **Python 3.10+** | `python3 --version`. Hooks use only the standard library |
| **Internet access** | For Wikipedia, Open Library, and web search |

**No API keys or credentials are required.** Both MCP servers use public, key-free APIs.
That is a deliberate design constraint: a clean checkout runs with nothing to configure.

## Setup

```bash
git clone git@github.com:do-it-with-love/learning-path-workflow.git
cd learning-path-workflow

# Virtual environment for the two MCP servers.
# The hooks deliberately do not need this — they are stdlib-only.
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Optional: identify yourself to Open Library (they ask, and rate-limit anonymous traffic)
cp .env.example .env      # then edit OPENLIBRARY_USER_AGENT
```

Verify the setup:

```bash
python3 tests/test_hooks.py     # 40 tests, no network, no venv needed
python3 tests/test_wiring.py    # 58 tests, checks the components still agree
claude mcp list                 # both servers should report connected
```

If `claude mcp list` shows a server failing to start, the usual cause is that MCP servers
were not launched from the project root, so the relative paths in `.mcp.json` did not
resolve. Replace them with absolute paths to `.venv/bin/`.

### Known issues

**`search_wikipedia` returns no results.** In the current `wikipedia-mcp` release the
search tool answers every query with `"status": "no_results"`, while `get_summary` and
`get_article` work normally against exact article titles. This is upstream, not a
configuration problem, and it does not block the workflow: the two agents that use
Wikipedia are instructed to go straight to titles they can name, and explicitly told not
to read an empty search as evidence that a field has no standard structure. If a future
release fixes it, nothing here needs changing.

**Newly added components need a restart.** Claude Code registers subagents, MCP servers
and hooks at session start. After a fresh clone — or after editing anything in
`.claude/agents/`, `.claude/hooks/` or `.mcp.json` — restart Claude Code before running
the workflow, or the agent types will not resolve and the hooks will not fire.

## Running

```bash
claude
```

then:

```
/build-learning-path <what you want to learn, your level, hours per week, deadline, budget, how you like to learn>
```

The workflow will:

1. **Ask you clarifying questions** and show you a requirements table to confirm. Nothing
   proceeds until you confirm it.
2. **Plan and execute** — around ten subagents, with independent ones running in parallel.
   You will see the run id; note it down.
3. **Run quality gates** and retry only the affected work if any fail, up to three attempts
   per step. If something cannot be fixed, it stops and tells you rather than shipping a
   broken plan.
4. **Stop and ask for your approval**, showing you `runs/<run-id>/output/learning-path.md`.
5. **Render the HTML guide** once you approve.

### Approving

```
/approve-learning-path <run-id>
/approve-learning-path <run-id> --reject "too theory-heavy, I want weekly practice pieces"
```

Rejection routes your feedback to whichever step owns the problem, revises, and asks again.

Approval is bound to a SHA-256 of the document you read. If the Markdown changes after you
approve it, the render is blocked and you are asked to approve again — so the HTML always
matches the bytes you actually saw.

### Resuming

If a run is interrupted — a crash, a closed terminal, a restarted machine:

```
/resume-learning-path <run-id>
```

It re-hashes every completed artifact against the disk, drops anything missing or modified
back to unfinished along with everything downstream of it, and continues from there.
Completed work is never repeated.

```bash
ls runs/                                        # find a run id
python3 scripts/runctl.py status <run-id>       # inspect it without starting Claude
```

## What is in here

```
.claude/
  commands/       3 slash commands — build, resume, approve (the coordinator)
  agents/        13 subagent definitions filling 11 pipeline slots
  skills/         3 reusable skills — artifact contract, resource vetting, HTML theme
  hooks/          2 PreToolUse guards + 1 PostToolUse state recorder
  workflow/       pipeline.json (the step graph) and gates.md (the 9 quality gates)
scripts/          runctl.py (run control) and approve.py (human approval)
mcp-servers/      custom Open Library MCP server
runs/             recorded runs: inputs, artifacts, state, outputs
tests/            hook tests (40) and wiring tests (58)
```

## Architecture in one diagram

```
[1] requirements-formalizer            ← clarifying Q&A, you confirm
[2] knowledge-assessor                   full or light mode
[3] curriculum-architect
[4] <modality>-curator ‖ exercise-designer ‖ assessment-designer      PARALLEL
[5] schedule-planner ‖ effort-budget-aggregator                       PARALLEL
[6] validator                          ← 9 gates; targeted retry, max 3, cascades
[7] learning-path-builder              ← synthesis
[8] HUMAN APPROVAL                     ← digest-verified; reject → revision loop
[9] html-builder
```

Exactly one curator runs per path — `video-curator`, `reading-curator`, or
`project-curator` — chosen from your confirmed learning preference.

## External data sources

Nothing a learner will act on comes from the model's memory.

- **Wikipedia MCP** (community, [wikipedia-mcp](https://pypi.org/project/wikipedia-mcp/)) —
  grounds subject decomposition and level frameworks in how a field is really structured.
- **Open Library MCP** (custom, in this repo) — real catalogue records for every book:
  ISBN, year, page count, and whether it can be borrowed free. Books are the easiest
  resource for a model to invent convincingly, which is why this server exists.
- **Web search and fetch** — courses, platforms and articles, plus link-liveness checks.

Every recommendation carries a marker recording how it was verified during that run. A
citation without one fails a quality gate.

## Secrets

None are required. `.env` is gitignored and `.env.example` documents the two optional
variables — a contact string for Open Library, and an escape hatch for absolute MCP paths.
No credentials are committed anywhere in this repository or its history.

## Development

```bash
python3 tests/test_hooks.py     # 40 tests — hooks, approval, rejection loop
python3 tests/test_wiring.py    # 58 tests — pipeline/agents/skills/hooks agree
```

The hooks are the reliability layer; changing one without running the tests is how the
guarantees quietly stop holding.
