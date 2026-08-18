"""Shared helpers for the workflow hooks and scripts.

Standard library only, on purpose: the hooks must keep working even when the
project venv is missing or broken. If a hook cannot import, Claude Code sees a
crashing hook and the reliability guarantees quietly evaporate — so this module
has no dependencies and every entry point fails closed.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

PIPELINE_REL = Path(".claude/workflow/pipeline.json")
STATE_REL = Path("state/workflow-state.json")
RUN_DIR_RE = re.compile(r"^(?P<root>.*?[/\\]runs[/\\][^/\\]+)[/\\](?P<rest>.*)$")


# --------------------------------------------------------------------------- paths


def repo_root(start: Path | None = None) -> Path:
    """Walk up from this file until we find the pipeline definition."""
    here = (start or Path(__file__).resolve()).parent
    for candidate in [here, *here.parents]:
        if (candidate / PIPELINE_REL).is_file():
            return candidate
    # Fall back to two levels up from .claude/hooks/
    return Path(__file__).resolve().parents[2]


def split_run_path(file_path: str) -> tuple[Path, str] | None:
    """Split an absolute path into (run_dir, path-relative-to-run-dir).

    Returns None for anything outside a runs/<run-id>/ directory.
    """
    match = RUN_DIR_RE.match(str(Path(file_path)))
    if not match:
        return None
    return Path(match.group("root")), match.group("rest").replace("\\", "/")


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: Path) -> str | None:
    try:
        return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


# ------------------------------------------------------------------------ pipeline


def load_pipeline(root: Path | None = None) -> dict:
    root = root or repo_root()
    return json.loads((root / PIPELINE_REL).read_text(encoding="utf-8"))


def artifact_owners(pipeline: dict) -> dict[str, str]:
    """artifact path (relative to run dir) -> owning step name."""
    return {
        spec["artifact"]: step
        for step, spec in pipeline["steps"].items()
        if "artifact" in spec
    }


def transitive_dependents(pipeline: dict, step: str) -> set[str]:
    """Every step that transitively depends on `step`."""
    steps = pipeline["steps"]
    direct: dict[str, set[str]] = {name: set() for name in steps}
    for name, spec in steps.items():
        for parent in spec.get("depends_on", []):
            if parent in direct:
                direct[parent].add(name)

    seen: set[str] = set()
    queue = list(direct.get(step, ()))
    while queue:
        current = queue.pop()
        if current in seen:
            continue
        seen.add(current)
        queue.extend(direct.get(current, ()))
    return seen


# --------------------------------------------------------------------------- state


@contextmanager
def state_lock(run_dir: Path):
    """Serialise state writes.

    Parallel subagents in one group write their artifacts concurrently, so the
    PostToolUse hook can fire several times at once. Without this lock the last
    writer wins and the other steps silently lose their 'done' marks.
    """
    lock_path = run_dir / "state" / ".state.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with open(lock_path, "w") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def load_state(run_dir: Path) -> dict:
    path = run_dir / STATE_REL
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def save_state(run_dir: Path, state: dict) -> None:
    path = run_dir / STATE_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = utcnow()
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)  # atomic: a crash mid-write cannot truncate the state


def new_state(run_id: str, pipeline: dict) -> dict:
    return {
        "run_id": run_id,
        "schema_version": pipeline.get("schema_version", 1),
        "status": "running",
        "created_at": utcnow(),
        "updated_at": utcnow(),
        "requirements_confirmed": False,
        "selected_agents": {},
        "skipped_steps": [],
        "steps": {
            name: {"status": "pending", "attempts": 0, "artifact": spec.get("artifact")}
            for name, spec in pipeline["steps"].items()
        },
        "gates": {},
        "approval": {"status": "pending", "digest": None, "decided_at": None, "feedback": []},
        "retry_limit": pipeline.get("retry_limit", 3),
    }


# ---------------------------------------------------------------------- hook I/O


def read_hook_input() -> dict:
    import sys

    try:
        return json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        return {}


def target_path(payload: dict) -> str | None:
    """The file a Write/Edit/MultiEdit call is aimed at."""
    tool_input = payload.get("tool_input") or {}
    return tool_input.get("file_path") or tool_input.get("notebook_path")


def written_content(payload: dict) -> str:
    """Best-effort view of the content a tool call would put on disk."""
    tool_input = payload.get("tool_input") or {}
    parts = [tool_input.get("content") or "", tool_input.get("new_string") or ""]
    for edit in tool_input.get("edits") or []:
        parts.append(edit.get("new_string") or "")
    return "\n".join(part for part in parts if part)


def deny(reason: str) -> None:
    """Block the tool call and tell the model exactly why."""
    import sys

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }
        )
    )
    sys.exit(0)


def allow() -> None:
    """Stay silent so normal permission handling continues."""
    import sys

    sys.exit(0)
