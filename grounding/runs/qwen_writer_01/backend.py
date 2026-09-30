"""The writer on the self-hosted Qwen3.8-27B in Claude Code; every other role on Muse, as Phase 4 ran it.

`install()` replaces `autogen_01.kit.agent.run` with a dispatcher:
- **role "writer"**: `claude -p` with the kit's own flags (`agent._command`: restricted mode, file tools only, no MCP,
  edits accepted inside the workspace, the writer prompt appended to the system prompt, `--resume` for every repair
  round), the model `qwen3.8-27b` served at http://127.0.0.1:18000 through its Anthropic Messages endpoint,
  `--autocompact 131k` (the served window, which Claude Code cannot know) and `--effort xhigh` (the served default;
  Claude Code's own default, "high", is refused by the server). Changed from the kit's call: the output
  is stream-json, so each call's init event is checked and kept, and the process runs in a clean environment of its
  own (none of the launching session's variables) with a configuration directory per brief: no login, no account,
  no user settings, kept for the brief's resumed rounds and outside the writer's workspace.
- **every other role** (the cold reader): the kit's Muse path unchanged, refused once the readers' billed cost in
  this study reaches the cap ($3).

A writer call whose init event shows any tool beyond those asked for, or any MCP server, fails the brief.
Cost: the model is self-hosted, so `total_cost_usd` is 0 with `cost_basis: "self-host"`; Claude Code's own estimate
(priced for a model it does not know) is kept only as `claude_code_estimate_usd`.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.qwen_writer_01.backend probe OUT_DIR
runs a trivial two-turn writer call (read, write, then an edit in the resumed session) and prints its init check.
"""
from __future__ import annotations

import json
import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

from grounding.runs.autogen_01.kit import agent

HERE = Path(__file__).resolve().parent
MODEL = "qwen3.8-27b"
BASE_URL = os.environ.get("SELFHOST_ANTHROPIC_URL", "http://127.0.0.1:18000")
KEY_FILE = Path(os.environ.get("SELFHOST_KEY_FILE", Path.home() / "qwen-selfhost" / "secrets" / "api_key"))
WINDOW = "131k"
# The served default. Without --effort, Claude Code sends "high", which the self-host refuses ("Supported types are
# xhigh (default), medium, and low"); judge_qwen_01's judge ran at the served default too.
EFFORT = "xhigh"
MUSE_CAP_BILLED = 3.0
CLAUDE_BIN = shutil.which(agent.CLAUDE) or agent.CLAUDE
_kit_run = agent.run


def selfhost_key() -> str:
    return KEY_FILE.read_text().strip()


def config_dir(call: agent.Call) -> Path:
    """One per brief (the writer's workspace is <work>/<run>/<brief>/writer), beside the workspace, not in it."""
    return call.workspace.parent / "claude-config"


def writer_env(config: Path) -> dict:
    node_bin = str(Path(os.path.realpath(shutil.which("node") or "/usr/bin/node")).parent)
    return {"HOME": str(Path.home()), "USER": os.getenv("USER", "yusf"), "LANG": "C.UTF-8", "TERM": "dumb",
            "PATH": os.pathsep.join([str(Path(CLAUDE_BIN).parent), node_bin, "/usr/local/bin", "/usr/bin", "/bin"]),
            "CLAUDE_CONFIG_DIR": str(config), "ENABLE_CLAUDEAI_MCP_SERVERS": "false", "DISABLE_AUTOUPDATER": "1",
            "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
            # "Authorization: Bearer", which the self-host checks (ANTHROPIC_API_KEY would go out as x-api-key: 401)
            "ANTHROPIC_BASE_URL": BASE_URL, "ANTHROPIC_AUTH_TOKEN": selfhost_key(),
            # any model alias Claude Code resolves on its own goes to the same served model
            "ANTHROPIC_DEFAULT_HAIKU_MODEL": MODEL, "ANTHROPIC_DEFAULT_SONNET_MODEL": MODEL,
            "ANTHROPIC_DEFAULT_OPUS_MODEL": MODEL}


def writer_command(call: agent.Call, system_file: Path | None) -> list:
    if call.effort:
        raise ValueError("the kit's writer sets no effort level; this backend sets the served default")
    cmd = agent._command(call, system_file)
    cmd[0] = CLAUDE_BIN
    cmd[cmd.index("--model") + 1] = MODEL
    cmd[cmd.index("--output-format") + 1] = "stream-json"
    return cmd[:2] + ["--verbose", "--autocompact", WINDOW, "--effort", EFFORT] + cmd[2:]


def init_check(events: list, call: agent.Call) -> dict:
    init = next((e for e in events if e.get("type") == "system" and e.get("subtype") == "init"), None)
    if init is None:
        return {"ok": False, "problem": "no init event"}
    keep = ("claude_code_version", "model", "tools", "mcp_servers", "permissionMode", "apiKeySource", "agents",
            "plugins", "skills", "memory_paths", "cwd")
    seen = {k: init.get(k) for k in keep}
    problems = []
    if sorted(init.get("tools") or []) != sorted(call.tools):
        problems.append(f"tools {init.get('tools')} != {call.tools}")
    if init.get("mcp_servers"):
        problems.append(f"MCP servers {init.get('mcp_servers')}")
    if init.get("model") != MODEL:
        problems.append(f"model {init.get('model')}")
    return {"ok": not problems, "problems": problems, "init": seen}


def run_process(cmd: list, env: dict, cwd: Path, prompt: str, timeout: int) -> tuple[str, str, int]:
    """In its own process group, killed whole at the limit (the kit's subprocess.run kills only the direct child)."""
    proc = subprocess.Popen(cmd, cwd=cwd, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True, start_new_session=True)
    try:
        stdout, stderr = proc.communicate(prompt, timeout=timeout)
        return stdout, stderr, proc.returncode
    except subprocess.TimeoutExpired:
        try:
            os.killpg(proc.pid, signal.SIGTERM)
            stdout, stderr = proc.communicate(timeout=15)
        except (ProcessLookupError, subprocess.TimeoutExpired):
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            stdout, stderr = proc.communicate()
        return stdout or "", f"timeout after {timeout}s\n{stderr or ''}", -1


def transcript(config: Path, session_id: str) -> Path | None:
    hits = sorted((config / "projects").glob(f"*/{session_id}.jsonl")) if session_id else []
    return hits[0] if hits else None


def run_writer(call: agent.Call) -> dict:
    """agent.run's Claude path for the writer, on the self-host (see the module docstring)."""
    call.workspace.mkdir(parents=True, exist_ok=True)
    call.log_dir.mkdir(parents=True, exist_ok=True)
    config = config_dir(call)
    config.mkdir(parents=True, exist_ok=True)
    system_file = None
    if call.system_append:
        system_file = call.log_dir / f"{call.role}.system.md"
        system_file.write_text(call.system_append)
    env = writer_env(config)
    last_error = None
    for attempt in range(1, call.retries + 2):
        index = agent._next_index(call.log_dir)
        stem = f"{index:02}-{call.role}"
        (call.log_dir / f"{stem}.prompt.md").write_text(call.prompt)
        cmd = writer_command(call, system_file)
        start = time.time()
        stdout, stderr, code = run_process(cmd, env, call.workspace, call.prompt, call.timeout)
        seconds = time.time() - start
        (call.log_dir / f"{stem}.events.jsonl").write_text(stdout)
        events = []
        for line in stdout.splitlines():
            try:
                events.append(json.loads(line))
            except ValueError:
                pass
        check = init_check(events, call)
        if not check["ok"] and check.get("init"):
            (call.log_dir / f"{stem}.failed.json").write_text(json.dumps({"init_check": check}, indent=1))
            raise RuntimeError(f"writer {call.label}: the init event failed the isolation check: {check['problems']}")
        result = next((e for e in reversed(events) if e.get("type") == "result"), None)
        record = {"command": cmd, "cwd": str(call.workspace), "exit": code, "stderr": stderr[-4000:],
                  "claude_config_dir": str(config), "base_url": BASE_URL}
        if result is not None:
            result["claude_code_estimate_usd"] = result.get("total_cost_usd")
            result["total_cost_usd"] = 0.0
            result.update(backend="claude-code-selfhost", model=MODEL, init_check=check)
        row = None
        if result is not None:
            row = agent.usage_row(call, result, index, seconds, attempt)
            row.update(backend="claude-code-selfhost", cost_basis="self-host", cost_usd_list_price=0.0,
                       cost_usd_billed=0.0)
        if result is None or code != 0 or result.get("is_error"):
            # As the kit: kept on disk; a failed first turn is retried fresh, a failed resume resumes again.
            last_error = {"stdout_tail": stdout[-4000:], **record, "result": result, "init_check": check}
            (call.log_dir / f"{stem}.failed.json").write_text(json.dumps(last_error, indent=1))
            if call.calls_log and row:
                with call.calls_log.open("a") as fh:
                    fh.write(json.dumps({**row, "failed": True}) + "\n")
            time.sleep(20 * attempt)
            continue
        result["_call"] = record
        (call.log_dir / f"{stem}.result.json").write_text(json.dumps(result, indent=1, ensure_ascii=False))
        found = transcript(config, result.get("session_id", ""))
        if found:
            (call.log_dir / f"{stem}.transcript.jsonl").write_text(found.read_text())
        if call.calls_log:
            with call.calls_log.open("a") as fh:
                fh.write(json.dumps(row) + "\n")
        return result
    raise RuntimeError(f"{call.role} {call.label}: agent call failed after retries: "
                       f"{json.dumps(last_error)[:1500] if last_error else ''}")


def readers_billed() -> float:
    """The Muse readers' billed cost across this study's runs."""
    total = 0.0
    for log in (HERE / "runs").glob("*/calls.jsonl"):
        for line in log.read_text().splitlines():
            if line.strip():
                row = json.loads(line)
                if row.get("backend") == "muse" and row.get("role") == "reader":
                    total += row.get("cost_usd_billed") or 0.0
    return total


def dispatch(call: agent.Call) -> dict:
    if call.role == "writer":
        return run_writer(call)
    spent = readers_billed()
    if spent >= MUSE_CAP_BILLED - 0.05:
        raise RuntimeError(f"the Muse readers' cap: ${spent:.2f} billed of ${MUSE_CAP_BILLED:.2f}")
    return _kit_run(call)


def install():
    if agent.BACKEND != "muse":
        raise SystemExit("set AUTOGEN_BACKEND=muse: every role but the writer stays on Muse")
    agent.run = dispatch


def probe(out: Path):
    """Two trivial writer turns in a scratch workspace; prints the init check and the answers."""
    ws = Path("/tmp/qwen-writer-01/probe") / out.name / "writer"
    if ws.exists():
        shutil.rmtree(ws)
    ws.mkdir(parents=True)
    (ws / "note.txt").write_text("hello from the probe\n")
    call = dict(role="writer", workspace=ws, log_dir=out / "writer", calls_log=out / "calls.jsonl",
                tools=agent.FILE_TOOLS, write=True, system_append="You are a careful assistant. Keep replies short.",
                label="probe", timeout=900, retries=0)
    first = run_writer(agent.Call(prompt="Read note.txt, then write out.txt with the same text in upper case. "
                                         "Reply with one word: done.", **call))
    second = run_writer(agent.Call(prompt="Now use Edit to add a second line, SECOND, to out.txt. Reply: done.",
                                   resume=first["session_id"], **call))
    print(json.dumps({"init_check": first["init_check"], "answers": [first.get("result"), second.get("result")],
                      "same_session": first["session_id"] == second["session_id"],
                      "out.txt": (ws / "out.txt").read_text() if (ws / "out.txt").exists() else None,
                      "models": [sorted(first.get("modelUsage") or {}), sorted(second.get("modelUsage") or {})],
                      "turns": [first.get("num_turns"), second.get("num_turns")]}, indent=1))


if __name__ == "__main__":
    if sys.argv[1:2] == ["probe"]:
        probe(Path(sys.argv[2]).resolve())
