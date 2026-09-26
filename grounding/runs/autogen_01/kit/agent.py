"""Run one headless Claude Code agent turn and keep its evidence.

    result = run(Call(role="writer", workspace=ws, prompt=text, log_dir=out, tools=FILE_TOOLS, write=True))
    result = run(Call(..., resume=result["session_id"]))          # a repair continues the same conversation

Every call runs `claude -p` with its working directory in a clean workspace outside any repository, in restricted
mode (file tools confined to the workspace, no Bash, user/project settings ignored) and with no MCP servers, so no
project instructions, memory or other files reach the agent. The prompt goes in on stdin. Saved per call, under
`log_dir`:
- `<n>-<role>.prompt.md` (the text sent);
- `<n>-<role>.result.json` (the CLI's JSON result: usage, cost estimate, session id, structured output);
- `<n>-<role>.transcript.jsonl` (the session transcript).

A line of usage is also appended to the run's `calls.jsonl`.
"""
from __future__ import annotations

import json
import os
import subprocess
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

CLAUDE = os.environ.get("CLAUDE_BIN", "claude")
MODEL = os.environ.get("AUTOGEN_MODEL", "sonnet")
FILE_TOOLS = ["Read", "Write", "Edit", "Glob", "Grep"]
READ_TOOLS = ["Read", "Glob", "Grep"]
PROJECTS = Path.home() / ".claude" / "projects"
# Never handed to an agent process: solver and database credentials, and anything that would switch billing.
WITHHELD = {"GENAI_API_KEY", "PURDUE_GENAI_STUDIO_API_KEY", "DATABASE_URL", "ANTHROPIC_API_KEY",
            "ANTHROPIC_AUTH_TOKEN", "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN",
            "PURDUE_RATE_LIMIT_FILE", "PYTHONPATH"}


def agent_env() -> dict:
    return {k: v for k, v in os.environ.items() if k not in WITHHELD}


@dataclass
class Call:
    role: str                      # writer, reader, judge
    workspace: Path                # cwd; must be outside any repository and outside ~/.claude
    prompt: str
    log_dir: Path                  # where this call's evidence goes
    calls_log: Path | None = None  # run-level usage log (JSONL)
    tools: list = field(default_factory=list)   # [] = no tools
    write: bool = False            # allow Write/Edit inside the workspace
    schema: dict | None = None     # JSON schema for structured output
    system_append: str | None = None  # role instructions appended to Claude Code's system prompt
    resume: str | None = None      # session id to continue
    effort: str | None = None
    label: str = ""                # scenario or trial id, for the usage log
    timeout: int = 1800
    retries: int = 2


def _command(call: Call, system_file: Path | None) -> list:
    cmd = [CLAUDE, "-p", "--model", MODEL, "--output-format", "json", "--restricted", "--strict-mcp-config",
           "--permission-prompts", "none", "--tools", ",".join(call.tools)]
    if call.write:
        cmd += ["--permission-mode", "acceptEdits", "--allowedTools=Write,Edit"]
    if call.schema:
        cmd += ["--json-schema", json.dumps(call.schema)]
    if system_file:
        cmd += ["--append-system-prompt-file", str(system_file)]
    if call.effort:
        cmd += ["--effort", call.effort]
    if call.resume:
        cmd += ["--resume", call.resume]
    return cmd


def _next_index(log_dir: Path) -> int:
    return 1 + len(list(log_dir.glob("*.result.json"))) + len(list(log_dir.glob("*.failed.json")))


def _transcript(session_id: str) -> Path | None:
    hits = sorted(PROJECTS.glob(f"*/{session_id}.jsonl"))
    return hits[0] if hits else None


def usage_row(call: Call, result: dict, index: int, seconds: float, attempt: int) -> dict:
    usage = result.get("usage") or {}
    models = result.get("modelUsage") or {}
    return {"utc": datetime.now(timezone.utc).isoformat(), "role": call.role, "label": call.label, "index": index,
            "attempt": attempt, "resumed": bool(call.resume), "session_id": result.get("session_id"),
            "models": sorted(models), "num_turns": result.get("num_turns"), "seconds": round(seconds, 1),
            "is_error": result.get("is_error"), "subtype": result.get("subtype"),
            "input_tokens": usage.get("input_tokens", 0), "output_tokens": usage.get("output_tokens", 0),
            "cache_creation_input_tokens": usage.get("cache_creation_input_tokens", 0),
            "cache_read_input_tokens": usage.get("cache_read_input_tokens", 0),
            "cost_usd_list_price": result.get("total_cost_usd"),
            "cost_basis": next((m.get("costBasis") for m in models.values()), None)}


def run(call: Call) -> dict:
    """One agent turn. Returns the CLI result dict (with `structured_output` when a schema was given)."""
    call.workspace.mkdir(parents=True, exist_ok=True)
    call.log_dir.mkdir(parents=True, exist_ok=True)
    system_file = None
    if call.system_append:
        system_file = call.log_dir / f"{call.role}.system.md"
        system_file.write_text(call.system_append)
    last_error = None
    for attempt in range(1, call.retries + 2):
        index = _next_index(call.log_dir)
        stem = f"{index:02}-{call.role}"
        (call.log_dir / f"{stem}.prompt.md").write_text(call.prompt)
        cmd = _command(call, system_file)
        start = time.time()
        try:
            proc = subprocess.run(cmd, cwd=call.workspace, input=call.prompt, capture_output=True, text=True,
                                  timeout=call.timeout, env=agent_env())
            stdout, stderr, code = proc.stdout, proc.stderr, proc.returncode
        except subprocess.TimeoutExpired as exc:
            stdout, stderr, code = exc.stdout or "", f"timeout after {call.timeout}s", -1
            stdout = stdout.decode() if isinstance(stdout, bytes) else stdout
        seconds = time.time() - start
        try:
            result = json.loads(stdout)
        except ValueError:
            result = None
        record = {"command": cmd, "cwd": str(call.workspace), "exit": code, "stderr": stderr[-4000:]}
        if result is None or code != 0 or result.get("is_error"):
            # Kept on disk; a failed first turn is retried fresh, a failed resume resumes again.
            last_error = {"stdout_tail": (stdout or "")[-4000:], **record, "result": result}
            (call.log_dir / f"{stem}.failed.json").write_text(json.dumps(last_error, indent=1))
            if call.calls_log and result:
                with call.calls_log.open("a") as fh:
                    fh.write(json.dumps({**usage_row(call, result, index, seconds, attempt), "failed": True}) + "\n")
            time.sleep(20 * attempt)
            continue
        result["_call"] = record
        (call.log_dir / f"{stem}.result.json").write_text(json.dumps(result, indent=1, ensure_ascii=False))
        transcript = _transcript(result.get("session_id", ""))
        if transcript:
            (call.log_dir / f"{stem}.transcript.jsonl").write_text(transcript.read_text())
        if call.calls_log:
            with call.calls_log.open("a") as fh:
                fh.write(json.dumps(usage_row(call, result, index, seconds, attempt)) + "\n")
        return result
    raise RuntimeError(f"{call.role} {call.label}: agent call failed after retries: "
                       f"{json.dumps(last_error)[:1500] if last_error else ''}")


def structured(result: dict):
    """The schema-constrained answer of a call (falls back to parsing `result` text)."""
    out = result.get("structured_output")
    if out is not None:
        return out
    text = (result.get("result") or "").strip()
    try:
        return json.loads(text)
    except ValueError:
        return None
