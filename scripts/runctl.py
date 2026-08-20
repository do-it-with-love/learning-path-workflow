#!/usr/bin/env python3
"""Run control for the learning-path workflow.

The coordinator drives the run through this script rather than editing
``workflow-state.json`` by hand. State that a model hand-edits is state that
drifts, and every reliability property here — resume, retry limits, staleness —
depends on that file being right.

Subcommands:
    init <slug>                     create a run, print its id
    status <run-id>                 what is done, what is runnable, what is blocked
    verify <run-id>                 re-check artifact digests on disk, demote mismatches
    select <run-id> [--curator X] [--skip S ...]   record dynamic agent selection
    mark <run-id> <step> <status> [--reason R]     mark a step pending/failed/stale
    request-approval <run-id>       publish the digest a human must approve
    gate <run-id> --pass | --fail G1=... [...]     record gate results
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".claude" / "hooks"))

from wfstate import (  # noqa: E402
    load_pipeline,
    load_state,
    new_state,
    repo_root,
    save_state,
    sha256_file,
    state_lock,
    transitive_dependents,
    utcnow,
)

ROOT = repo_root(Path(__file__).resolve())
RUNNABLE_BLOCKERS = {"pending", "stale", "failed"}


def run_dir_for(run_id: str) -> Path:
    path = ROOT / "runs" / run_id
    if not path.is_dir():
        sys.exit(f"ERROR: no such run: runs/{run_id}")
    return path


# ------------------------------------------------------------------------- init


def cmd_init(args: argparse.Namespace) -> int:
    from datetime import date

    pipeline = load_pipeline(ROOT)
    slug = "".join(c if c.isalnum() or c == "-" else "-" for c in args.slug.lower()).strip("-")

    existing = sorted((ROOT / "runs").glob("run-*")) if (ROOT / "runs").is_dir() else []
    seq = len(existing) + 1
    run_id = args.run_id or f"run-{seq:03d}-{slug}"[:60]

    run_dir = ROOT / "runs" / run_id
    if run_dir.exists():
        sys.exit(f"ERROR: run {run_id} already exists")

    for sub in ("artifacts", "output", "state"):
        (run_dir / sub).mkdir(parents=True)

    (run_dir / "input.md").write_text(
        f"# Request\n\nSubmitted {date.today().isoformat()}\n\n{args.request or ''}\n",
        encoding="utf-8",
    )

    state = new_state(run_id, pipeline)
    save_state(run_dir, state)
    print(run_id)
    return 0


# ----------------------------------------------------------------------- status


def runnable_steps(pipeline: dict, state: dict) -> list[str]:
    """Steps whose dependencies are all satisfied and which still need work."""
    steps = state.get("steps", {})
    skipped = set(state.get("skipped_steps", []))
    ready: list[str] = []
    for name, spec in pipeline["steps"].items():
        if name in skipped:
            continue
        status = steps.get(name, {}).get("status", "pending")
        if status not in RUNNABLE_BLOCKERS:
            continue
        deps = [d for d in spec.get("depends_on", []) if d not in skipped]
        if all(steps.get(d, {}).get("status") == "done" for d in deps):
            ready.append(name)
    return ready


def cmd_status(args: argparse.Namespace) -> int:
    run_dir = run_dir_for(args.run_id)
    pipeline = load_pipeline(ROOT)
    state = load_state(run_dir)
    if not state:
        sys.exit(f"ERROR: run {args.run_id} has no state file")

    limit = state.get("retry_limit", 3)
    print(f"run:      {state['run_id']}")
    print(f"status:   {state.get('status')}")
    print(f"requirements confirmed: {state.get('requirements_confirmed')}")
    if state.get("selected_agents"):
        print(f"selected: {json.dumps(state['selected_agents'])}")
    if state.get("skipped_steps"):
        print(f"skipped:  {', '.join(state['skipped_steps'])}")

    print("\nsteps:")
    for name in pipeline["steps"]:
        entry = state.get("steps", {}).get(name, {})
        status = "skipped" if name in state.get("skipped_steps", []) else entry.get("status", "pending")
        attempts = entry.get("attempts", 0)
        flag = "  <-- RETRY LIMIT REACHED" if attempts >= limit and status != "done" else ""
        cause = f"  (stale via {entry['stale_cause']})" if entry.get("stale_cause") and status == "stale" else ""
        print(f"  {status:<8} {name:<28} attempts={attempts}{cause}{flag}")

    ready = runnable_steps(pipeline, state)
    group_of = {n: s.get("group") for n, s in pipeline["steps"].items()}
    if ready:
        groups: dict[int, list[str]] = {}
        for name in ready:
            groups.setdefault(group_of[name], []).append(name)
        first = min(groups)
        parallel = sorted(groups[first])
        print(f"\nnext (group {first}, dispatch these {'in parallel' if len(parallel) > 1 else 'now'}):")
        for name in parallel:
            spec = pipeline["steps"][name]
            agent = state.get("selected_agents", {}).get(name) or spec.get("agent") or "UNSELECTED"
            print(f"  {name} -> agent {agent} -> {spec.get('artifact')}")
    else:
        print("\nnext: nothing runnable")

    failed = [g for g, info in (state.get("gates") or {}).items() if info.get("status") == "fail"]
    if failed:
        print(f"\nfailing gates: {', '.join(sorted(failed))}")

    approval = state.get("approval", {})
    print(f"\napproval: {approval.get('status')}")
    if approval.get("feedback"):
        print(f"  latest feedback: {approval['feedback'][-1]['text']}")
    return 0


# ----------------------------------------------------------------------- verify


def cmd_verify(args: argparse.Namespace) -> int:
    """Resume safety: trust the disk, not the state file."""
    run_dir = run_dir_for(args.run_id)
    pipeline = load_pipeline(ROOT)
    changed: list[str] = []

    with state_lock(run_dir):
        state = load_state(run_dir)
        if not state:
            sys.exit(f"ERROR: run {args.run_id} has no state file")

        for name in pipeline["steps"]:
            entry = state.get("steps", {}).get(name)
            if not entry or entry.get("status") != "done":
                continue
            artifact = entry.get("artifact")
            if not artifact:
                continue
            actual = sha256_file(run_dir / artifact)
            if actual is None:
                entry["status"] = "pending"
                entry["stale_cause"] = "artifact missing on disk"
                changed.append(f"{name}: artifact missing -> pending")
            elif actual != entry.get("digest"):
                entry["status"] = "stale"
                entry["stale_cause"] = "artifact modified outside the workflow"
                changed.append(f"{name}: digest mismatch -> stale")

        # A step demoted here invalidates everything downstream of it.
        for line in list(changed):
            step = line.split(":")[0]
            for dependent in transitive_dependents(pipeline, step):
                entry = state.get("steps", {}).get(dependent, {})
                if entry.get("status") == "done":
                    entry["status"] = "stale"
                    entry["stale_cause"] = step
                    changed.append(f"{dependent}: stale via {step}")

        # Log the check either way. A resume that found everything intact is
        # exactly the evidence that completed work was not repeated, and it is
        # invisible if only corrections are recorded.
        state.setdefault("history", []).append(
            {"at": utcnow(), "event": "verify",
             "result": "corrected" if changed else "clean",
             "changes": changed}
        )
        save_state(run_dir, state)

    if changed:
        print("state corrected against disk:")
        for line in changed:
            print(f"  {line}")
    else:
        print("state matches disk; all completed artifacts intact")
    return 0


# ----------------------------------------------------------------------- select


def cmd_select(args: argparse.Namespace) -> int:
    run_dir = run_dir_for(args.run_id)
    pipeline = load_pipeline(ROOT)

    with state_lock(run_dir):
        state = load_state(run_dir)
        if args.curator:
            choices = pipeline["steps"]["curator"].get("agent_choices", [])
            if args.curator not in choices:
                sys.exit(f"ERROR: curator must be one of: {', '.join(choices)}")
            state.setdefault("selected_agents", {})["curator"] = args.curator
        for step in args.skip or []:
            if step not in pipeline["steps"]:
                sys.exit(f"ERROR: unknown step: {step}")
            if not pipeline["steps"][step].get("optional"):
                sys.exit(f"ERROR: step '{step}' is not optional and cannot be skipped")
            if step not in state.setdefault("skipped_steps", []):
                state["skipped_steps"].append(step)
        if args.confirm_requirements:
            state["requirements_confirmed"] = True
        state.setdefault("history", []).append({
            "at": utcnow(), "event": "plan_selected",
            "selected": state.get("selected_agents"), "skipped": state.get("skipped_steps"),
        })
        save_state(run_dir, state)

    print(f"selected: {json.dumps(state.get('selected_agents', {}))}")
    print(f"skipped:  {', '.join(state.get('skipped_steps', [])) or 'none'}")
    print(f"requirements confirmed: {state.get('requirements_confirmed')}")
    return 0


# ------------------------------------------------------------------------- mark


def cmd_mark(args: argparse.Namespace) -> int:
    run_dir = run_dir_for(args.run_id)
    pipeline = load_pipeline(ROOT)
    if args.step not in pipeline["steps"]:
        sys.exit(f"ERROR: unknown step: {args.step}")

    with state_lock(run_dir):
        state = load_state(run_dir)
        entry = state.setdefault("steps", {}).setdefault(
            args.step, {"status": "pending", "attempts": 0})
        limit = state.get("retry_limit", 3)
        if args.status in RUNNABLE_BLOCKERS and entry.get("attempts", 0) >= limit:
            sys.exit(
                f"REFUSED: {args.step} has already used {entry['attempts']} of {limit} "
                f"attempts. The retry limit is reached — stop dependent execution and "
                f"report the unresolved failure to the user."
            )
        entry["status"] = args.status
        if args.reason:
            entry["stale_cause"] = args.reason
        state.setdefault("history", []).append({
            "at": utcnow(), "event": "mark", "step": args.step,
            "status": args.status, "reason": args.reason,
        })
        save_state(run_dir, state)

    print(f"{args.step} -> {args.status} (attempts={entry.get('attempts', 0)})")
    return 0


# ------------------------------------------------------------------------- gate


def cmd_gate(args: argparse.Namespace) -> int:
    run_dir = run_dir_for(args.run_id)
    with state_lock(run_dir):
        state = load_state(run_dir)
        gates = state.setdefault("gates", {})
        if args.all_pass:
            for gate in list(gates):
                gates[gate] = {"status": "pass", "at": utcnow()}
            gates["_summary"] = {"status": "pass", "at": utcnow()}
        for item in args.fail or []:
            gate, _, detail = item.partition("=")
            owner, _, finding = detail.partition(":")
            gates[gate.strip()] = {
                "status": "fail", "owner": owner.strip(),
                "finding": finding.strip(), "at": utcnow(),
            }
            gates.pop("_summary", None)
        save_state(run_dir, state)

    failing = sorted(g for g, i in gates.items() if i.get("status") == "fail")
    print(f"gates failing: {', '.join(failing) if failing else 'none'}")
    if failing:
        owners = sorted({gates[g].get("owner") for g in failing if gates[g].get("owner")})
        print(f"re-run these steps: {', '.join(owners)}")
    return 0


# ---------------------------------------------------------------------- recount


def cmd_recount(args: argparse.Namespace) -> int:
    """Rebuild attempt counters by replaying the run's own history log.

    Repairs runs recorded before post_write_state.py stopped counting every write
    as an attempt. This is deliberately NOT a way to reset the retry limit: it
    derives each count from the logged events, so a step that genuinely burned
    three dispatches still reads three afterwards.
    """
    run_dir = run_dir_for(args.run_id)
    pipeline = load_pipeline(ROOT)

    with state_lock(run_dir):
        state = load_state(run_dir)
        history = state.get("history") or []
        if not history:
            sys.exit("ERROR: this run has no history log; nothing to replay")

        status: dict[str, str] = {name: "pending" for name in pipeline["steps"]}
        attempts: dict[str, int] = {name: 0 for name in pipeline["steps"]}

        for event in history:
            kind = event.get("event")
            step = event.get("step")
            if kind == "artifact_written" and step in status:
                if status[step] != "done":
                    attempts[step] += 1
                status[step] = "done"
                for dependent in event.get("invalidated") or []:
                    if dependent in status:
                        status[dependent] = "stale"
            elif kind == "mark" and step in status:
                if event.get("status") in status.values() or event.get("status"):
                    status[step] = event["status"]
            elif kind == "verify":
                for change in event.get("changes") or []:
                    name, _, rest = change.partition(":")
                    name = name.strip()
                    if name in status and "->" in rest:
                        status[name] = rest.rsplit("->", 1)[1].strip()

        changed = []
        for name, count in attempts.items():
            entry = state.get("steps", {}).get(name)
            if entry is None:
                continue
            if int(entry.get("attempts", 0)) != count:
                changed.append(f"{name}: {entry.get('attempts')} -> {count}")
                entry["attempts"] = count

        if changed:
            state.setdefault("history", []).append({
                "at": utcnow(), "event": "recount",
                "reason": args.reason or "replayed history after attempt-counting fix",
                "changes": changed,
            })
            save_state(run_dir, state)

    if changed:
        print("attempt counters corrected from the history log:")
        for line in changed:
            print(f"  {line}")
    else:
        print("attempt counters already match the history log")
    return 0


# -------------------------------------------------------------- request approval


def cmd_request_approval(args: argparse.Namespace) -> int:
    run_dir = run_dir_for(args.run_id)
    pipeline = load_pipeline(ROOT)

    source = None
    for spec in pipeline["steps"].values():
        if spec.get("requires_approval"):
            parent = (spec.get("depends_on") or [None])[0]
            source = pipeline["steps"].get(parent, {}).get("artifact")
    source = source or "output/learning-path.md"

    source_path = run_dir / source
    if not source_path.is_file():
        sys.exit(f"ERROR: {source} does not exist yet; there is nothing to approve")

    digest = sha256_file(source_path)
    request = {"source": source, "digest": digest, "requested_at": utcnow()}
    (run_dir / "state" / "approval-request.json").write_text(
        json.dumps(request, indent=2) + "\n", encoding="utf-8")

    with state_lock(run_dir):
        state = load_state(run_dir)
        state["status"] = "awaiting_approval"
        state.setdefault("approval", {})["status"] = "pending"
        state["approval"]["requested_digest"] = digest
        save_state(run_dir, state)

    print(f"Approval requested for {args.run_id}")
    print(f"  document: {source_path}")
    print(f"  digest:   {digest}")
    print("\nAsk the user to review it and run one of:")
    print(f"  /approve-learning-path {args.run_id}")
    print(f'  /approve-learning-path {args.run_id} --reject "<what to change>"')
    return 0


# ------------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init"); p.add_argument("slug")
    p.add_argument("--request", default=""); p.add_argument("--run-id")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("status"); p.add_argument("run_id"); p.set_defaults(func=cmd_status)
    p = sub.add_parser("verify"); p.add_argument("run_id"); p.set_defaults(func=cmd_verify)

    p = sub.add_parser("select"); p.add_argument("run_id")
    p.add_argument("--curator"); p.add_argument("--skip", action="append")
    p.add_argument("--confirm-requirements", action="store_true")
    p.set_defaults(func=cmd_select)

    p = sub.add_parser("mark"); p.add_argument("run_id"); p.add_argument("step")
    p.add_argument("status", choices=["pending", "running", "done", "failed", "stale"])
    p.add_argument("--reason"); p.set_defaults(func=cmd_mark)

    p = sub.add_parser("gate"); p.add_argument("run_id")
    p.add_argument("--all-pass", action="store_true")
    p.add_argument("--fail", action="append", metavar="G1=owner:finding")
    p.set_defaults(func=cmd_gate)

    p = sub.add_parser("recount"); p.add_argument("run_id"); p.add_argument("--reason")
    p.set_defaults(func=cmd_recount)

    p = sub.add_parser("request-approval"); p.add_argument("run_id")
    p.set_defaults(func=cmd_request_approval)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
