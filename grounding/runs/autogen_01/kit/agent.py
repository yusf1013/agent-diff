"""Run one headless agent turn (Claude Code or Muse Code) and keep its evidence.

    result = run(Call(role="writer", workspace=ws, prompt=text, log_dir=out, tools=FILE_TOOLS, write=True))
    result = run(Call(..., resume=result["session_id"]))          # a repair continues the same conversation

**Claude Code** (the default, `AUTOGEN_BACKEND=claude`). Every call runs `claude -p` with its working directory in a
clean workspace outside any repository, in restricted mode (file tools confined to the workspace, no Bash,
user/project settings ignored) and with no MCP servers. So no project instructions, memory or other files reach the
agent. The prompt goes in on stdin.

**Muse Code** (`AUTOGEN_BACKEND=muse`; see `_run_muse`). Every session runs `muse exec` inside a bubblewrap sandbox. The
sandbox sees only the workspace (at `/work`), a private home for that session, and the system's read-only files. The
shell and web tools are off. The Meta API key goes in on stdin, and no key file exists inside the sandbox.
- **Why a sandbox:** Muse's own approval modes do not stop file reads outside the workspace.
- **Role instructions** are prepended to a session's first prompt; Muse has no system-prompt flag.
- **Reminders:** judge and reader sessions run without Muse's reminder subagents (a `settings.json` in the session's
  home sets an empty `run.reminder_roster`). The verify-reminder never changed a judge or reader call and cost about a
  fifth of the bill (roadmap_01, 2026-09-27). `AUTOGEN_MUSE_NO_REMINDER_ROLES=""` restores Muse's default.
- **Usage** comes from the session log's `model_completed` events, subagents included. It is priced at the model
  catalog's rates: billed (the contributor model), and list (the same model without "-contributor").

Saved per call, under `log_dir`:
- `<n>-<role>.prompt.md`: the text sent;
- `<n>-<role>.result.json`: the result (usage, cost estimate, session id, structured output);
- `<n>-<role>.transcript.jsonl`: the session transcript. Muse also keeps `<n>-<role>.events.jsonl`, its event stream.

A line of usage is also appended to the run's `calls.jsonl`.
"""
from __future__ import annotations

import json
import os
import subprocess
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

BACKEND = os.environ.get("AUTOGEN_BACKEND", "claude")
CLAUDE = os.environ.get("CLAUDE_BIN", "claude")
MODEL = os.environ.get("AUTOGEN_MODEL", "sonnet")
MUSE_MODEL = os.environ.get("AUTOGEN_MUSE_MODEL", "muse-spark-1.3-contributor")
MUSE_EFFORT = os.environ.get("AUTOGEN_MUSE_EFFORT", "high")
MUSE_MAX_STEPS = os.environ.get("AUTOGEN_MUSE_MAX_STEPS", "200")
MUSE_HOMES = Path(os.environ.get("AUTOGEN_MUSE_HOMES", "/tmp/autogen-muse-homes"))
MUSE_BIN_DIR = Path.home() / ".local" / "bin"
MUSE_AUTH = Path.home() / ".config" / "muse" / "auth.json"
MUSE_CATALOG = Path.home() / ".local" / "share" / "muse" / "model-catalog"
# Roles whose Muse sessions run without reminder subagents; "" keeps Muse's default roster for every role.
MUSE_NO_REMINDER_ROLES = {r.strip() for r in os.environ.get("AUTOGEN_MUSE_NO_REMINDER_ROLES", "judge,reader").split(",")
                          if r.strip()}
MUSE_SETTINGS_NO_REMINDERS = {"schema_version": 1, "run": {"reminder_roster": {"agents": []}}}
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
    if BACKEND == "muse":
        return _run_muse(call)
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


def _muse_binary() -> Path:
    """The Muse binary: `AUTOGEN_MUSE_BIN`, or the newest installed one. The launcher script auto-updates, so the binary
    is called directly and its name is logged with every call."""
    if os.environ.get("AUTOGEN_MUSE_BIN"):
        return Path(os.environ["AUTOGEN_MUSE_BIN"])
    bins = sorted(MUSE_BIN_DIR.glob("muse-bin-*"), key=lambda p: p.stat().st_mtime)
    if not bins:
        raise RuntimeError(f"no muse-bin-* in {MUSE_BIN_DIR}")
    return bins[-1]


def _muse_prices(model: str) -> dict:
    """USD per million tokens from Muse's model catalog: billed (this model) and list (without '-contributor')."""
    rows = {}
    for path in MUSE_CATALOG.glob("*.json"):
        for row in json.loads(path.read_text()).get("rows", []):
            rows[row["model_id"]] = {k: float(v) for k, v in row["cost"].items() if k != "currency"}
    billed = rows.get(model)
    listed = rows.get(model.removesuffix("-contributor"), billed)
    if not billed:
        raise RuntimeError(f"model {model} not in the Muse catalog")
    return {"billed": billed, "list": listed}


def _muse_cost(usage: dict, price: dict) -> float:
    cached = usage["cached_tokens"]
    return ((usage["input_tokens"] - cached) * price["input"] + cached * price["cached"]
            + usage["output_tokens"] * price["output"]) / 1e6


def _strict_schema(schema):
    """A copy of a JSON schema with `additionalProperties: false` on every object, which Meta's API requires. The
    kit's schemas already list every property as required."""
    if isinstance(schema, list):
        return [_strict_schema(x) for x in schema]
    if not isinstance(schema, dict):
        return schema
    out = {k: _strict_schema(v) for k, v in schema.items()}
    if out.get("type") == "object" or "properties" in out:
        out["additionalProperties"] = False
    return out


def _sandbox(home: Path, workspace: Path, binary: Path) -> list:
    """bubblewrap: read-only system files, the workspace at /work, a private home, nothing else of the host."""
    return ["bwrap", "--ro-bind", "/usr", "/usr", "--symlink", "usr/bin", "/bin", "--symlink", "usr/lib", "/lib",
            "--symlink", "usr/lib64", "/lib64", "--symlink", "usr/sbin", "/sbin", "--ro-bind", "/etc", "/etc",
            "--ro-bind-try", "/run/systemd/resolve", "/run/systemd/resolve", "--proc", "/proc", "--dev", "/dev",
            "--tmpfs", "/tmp", "--dir", "/home", "--bind", str(home), "/home/agent", "--bind", str(workspace), "/work",
            "--ro-bind", str(binary), "/opt/muse/muse", "--unshare-all", "--share-net", "--die-with-parent",
            "--new-session", "--clearenv", "--setenv", "HOME", "/home/agent", "--setenv", "PATH", "/usr/bin:/bin",
            "--setenv", "LANG", "C.UTF-8", "--setenv", "MUSE_AUTH_PATH", "/home/agent/.config/muse/auth.json",
            "--chdir", "/work", "/opt/muse/muse"]


def _session_logs(home: Path, session_id: str) -> list:
    root = home / ".local" / "share" / "muse" / "sessions"
    return sorted(p for d in root.rglob(session_id) if d.is_dir() for p in d.rglob("session.jsonl"))


def _muse_settings(home: Path, role: str) -> str:
    """Write the session's Muse settings when the role runs without reminders; returns "off" or "default"."""
    if role not in MUSE_NO_REMINDER_ROLES:
        return "default"
    path = home / ".config" / "muse" / "settings.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(MUSE_SETTINGS_NO_REMINDERS))
    return "off"


def _usage(lines_before: dict, logs: list) -> tuple[dict, dict, list]:
    """Sum the model_completed events written since `lines_before`; returns totals, per-model totals and new lines."""
    total = {"input_tokens": 0, "cached_tokens": 0, "output_tokens": 0, "reasoning_tokens": 0, "requests": 0}
    per_model, new_lines = {}, []
    for path in logs:
        lines = path.read_text().splitlines()
        fresh = lines[lines_before.get(str(path), 0):]
        new_lines += fresh
        for line in fresh:
            try:
                event = json.loads(line).get("payload", {}).get("event", {})
            except ValueError:
                continue
            if event.get("kind") != "model_completed":
                continue
            u, m = event.get("usage") or {}, event.get("model", "?")
            bucket = per_model.setdefault(m, {k: 0 for k in total})
            for k in ("input_tokens", "cached_tokens", "output_tokens", "reasoning_tokens"):
                total[k] += u.get(k) or 0
                bucket[k] += u.get(k) or 0
            total["requests"] += 1
            bucket["requests"] += 1
    return total, per_model, new_lines


def _run_muse(call: Call) -> dict:
    """One Muse Code turn in a bubblewrap sandbox (see the module docstring)."""
    call.workspace.mkdir(parents=True, exist_ok=True)
    call.log_dir.mkdir(parents=True, exist_ok=True)
    if call.system_append:
        (call.log_dir / f"{call.role}.system.md").write_text(call.system_append)
    binary = _muse_binary()
    prices = _muse_prices(MUSE_MODEL)
    key = json.loads(MUSE_AUTH.read_text())["providers"]["meta"]["api_key"]
    session_id = call.resume or str(uuid.uuid4())
    home = MUSE_HOMES / session_id
    (home / "prompts").mkdir(parents=True, exist_ok=True)
    reminders = _muse_settings(home, call.role)
    text = call.prompt if call.resume or not call.system_append else f"{call.system_append}\n\n---\n\n{call.prompt}"
    last_error = None
    for attempt in range(1, call.retries + 2):
        index = _next_index(call.log_dir)
        stem = f"{index:02}-{call.role}"
        (call.log_dir / f"{stem}.prompt.md").write_text(text)
        (home / "prompts" / f"{stem}.md").write_text(text)
        args = ["exec", "--json", "--api-key-stdin", "--prompt-file", f"/home/agent/prompts/{stem}.md",
                "--model", MUSE_MODEL, "--reasoning-effort", call.effort or MUSE_EFFORT, "--workspace", "/work",
                "--session-id", session_id, "--disable-shell", "--disable-web-tools", "--no-foreign-personal-context",
                "--approval-mode", "never", "--approval-judge", "off", "--max-model-steps", MUSE_MAX_STEPS]
        if not call.write:
            args.append("--disable-write")
        if call.schema:
            (home / "prompts" / f"{stem}.schema.json").write_text(json.dumps(_strict_schema(call.schema)))
            args += ["--output-schema", f"/home/agent/prompts/{stem}.schema.json"]
        cmd = _sandbox(home, call.workspace, binary) + args
        before = {str(p): len(p.read_text().splitlines()) for p in _session_logs(home, session_id)}
        start = time.time()
        try:
            proc = subprocess.run(cmd, input=key + "\n", capture_output=True, text=True, timeout=call.timeout)
            stdout, stderr, code = proc.stdout, proc.stderr, proc.returncode
        except subprocess.TimeoutExpired as exc:
            stdout, stderr, code = exc.stdout or "", f"timeout after {call.timeout}s", -1
            stdout = stdout.decode() if isinstance(stdout, bytes) else stdout
        seconds = time.time() - start
        (call.log_dir / f"{stem}.events.jsonl").write_text(stdout or "")
        events = []
        for line in (stdout or "").splitlines():
            try:
                events.append(json.loads(line))
            except ValueError:
                pass
        terminal = next((e["payload"] for e in reversed(events) if e.get("payload_type", "").startswith("run.terminal")),
                        {})
        usage, per_model, new_lines = _usage(before, _session_logs(home, session_id))
        final = terminal.get("text")
        failed = code != 0 or terminal.get("terminal") != "completed" or final is None
        structured_output = None
        if call.schema and not failed:
            try:
                structured_output = json.loads(final)
            except ValueError:
                failed = True
        result = {"session_id": session_id, "result": final, "structured_output": structured_output,
                  "is_error": failed, "subtype": terminal.get("terminal"), "num_turns": usage["requests"],
                  "backend": "muse", "muse_binary": binary.name, "model": MUSE_MODEL,
                  "reasoning_effort": call.effort or MUSE_EFFORT, "reminders": reminders,
                  "usage": {"input_tokens": usage["input_tokens"] - usage["cached_tokens"],
                            "cache_read_input_tokens": usage["cached_tokens"], "cache_creation_input_tokens": 0,
                            "output_tokens": usage["output_tokens"], "reasoning_tokens": usage["reasoning_tokens"]},
                  "modelUsage": per_model, "prices_per_mtok": prices,
                  "total_cost_usd": _muse_cost(usage, prices["list"]),
                  "cost_usd_billed": _muse_cost(usage, prices["billed"])}
        record = {"command": ["<bwrap sandbox>", *args], "cwd": str(call.workspace), "exit": code,
                  "stderr": (stderr or "")[-4000:]}
        (call.log_dir / f"{stem}.transcript.jsonl").write_text("\n".join(new_lines) + ("\n" if new_lines else ""))
        row = usage_row(call, result, index, seconds, attempt)
        row.update({"backend": "muse", "reasoning_tokens": usage["reasoning_tokens"],
                    "cost_usd_billed": result["cost_usd_billed"], "muse_binary": binary.name, "reminders": reminders})
        if failed:
            last_error = {"stdout_tail": (stdout or "")[-4000:], **record, "result": result}
            (call.log_dir / f"{stem}.failed.json").write_text(json.dumps(last_error, indent=1))
            if call.calls_log:
                with call.calls_log.open("a") as fh:
                    fh.write(json.dumps({**row, "failed": True}) + "\n")
            time.sleep(10 * attempt)
            continue
        result["_call"] = record
        (call.log_dir / f"{stem}.result.json").write_text(json.dumps(result, indent=1, ensure_ascii=False))
        if call.calls_log:
            with call.calls_log.open("a") as fh:
                fh.write(json.dumps(row) + "\n")
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
