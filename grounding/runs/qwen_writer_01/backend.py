"""The writer on the self-hosted Qwen3.8-27B in Claude Code; every other role on Muse, as Phase 4 ran it.

`install()` replaces `autogen_01.kit.agent.run` with a dispatcher:
- **role "writer"**: `claude -p` with the kit's own flags (`agent._command`: restricted mode, file tools only, no MCP,
  edits accepted inside the workspace, the writer prompt appended to the system prompt, `--resume` for every repair
  round), the model `qwen3.8-27b` served at http://127.0.0.1:18000 through its Anthropic Messages endpoint,
  `--autocompact 131k` (the served window, which Claude Code cannot know) and `--effort medium` (the level
  OpenClaw's Qwen rounds run at; see EFFORT). Changed from the kit's call: a per-call limit of WRITER_TIMEOUT
  instead of the kit's 3600 s and a reply cap of MAX_OUTPUT_TOKENS instead of Claude Code's 32,000 (see there); the
  output is stream-json, so each call's init event is checked and kept; and the process runs in a clean environment
  of its own (none of the launching session's variables) with a configuration directory per brief: no login, no
  account, no user settings, kept for the brief's resumed rounds and outside the writer's workspace.
- **every other role** (the cold reader): the kit's Muse path unchanged, refused once the readers' billed cost in
  this study reaches the cap ($3).

A writer call whose init event shows any tool beyond those asked for, or any MCP server, fails the brief.
Cost: the model is self-hosted, so `total_cost_usd` is 0 with `cost_basis: "self-host"`; Claude Code's own estimate
(priced for a model it does not know) is kept only as `claude_code_estimate_usd`.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.qwen_writer_01.backend probe OUT_DIR
runs a trivial two-turn writer call (read, write, then an edit in the resumed session) and prints its init check.
"""
from __future__ import annotations

import http.client
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from grounding.runs.autogen_01.kit import agent

HERE = Path(__file__).resolve().parent
MODEL = "qwen3.8-27b"
BASE_URL = os.environ.get("SELFHOST_ANTHROPIC_URL", "http://127.0.0.1:18000")
KEY_FILE = Path(os.environ.get("SELFHOST_KEY_FILE", Path.home() / "qwen-selfhost" / "secrets" / "api_key"))
WINDOW = "131k"
# The level OpenClaw's Qwen rounds run at (integrations/openclaw/runtime.py: "medium" thinking). The self-host accepts
# xhigh (its default), medium or low; without --effort, Claude Code sends "high", which it refuses. The served default
# was tried first (runs/gen_01_xhigh, 2026-09-30): each first design step took 29-32k tokens and 34-43 minutes at the
# ~10 tokens/s per stream the shared server gave, two of four ended at Claude Code's 32,000-token output cap with
# only reasoning, and the window (131k) would not hold two repair rounds of that size.
EFFORT = "medium"
# Claude Code caps each reply at 32,000 output tokens for a model it does not know. Qwen drafts the whole scenario in its
# reasoning, and some first design steps reached the cap with nothing but reasoning, at xhigh and at medium alike
# (runs/gen_01_xhigh, runs/gen_02); Claude Code then asks it to resume, and it began again. The cap changes only the
# request's max_tokens (thinking stays "adaptive", effort as set; captured 2026-09-30), so below it nothing changes.
# 64,000 leaves room for long steps; the window relay (below) lowers it per request to what the window has left.
MAX_OUTPUT_TOKENS = 64000
# The kit's 3600 s per writer call was sized for API models; at the self-host's speed (7-13 tokens/s per stream on the
# shared server) it would measure throughput. A first call can hold two long steps, so 4 hours.
WRITER_TIMEOUT = 14400
MUSE_CAP_BILLED = 3.0
CLAUDE_BIN = shutil.which(agent.CLAUDE) or agent.CLAUDE
_kit_run = agent.run


def selfhost_key() -> str:
    return KEY_FILE.read_text().strip()


def config_dir(call: agent.Call) -> Path:
    """One per brief (the writer's workspace is <work>/<run>/<brief>/writer), beside the workspace, not in it."""
    return call.workspace.parent / "claude-config"


# ---------------------------------------------------------------- the window relay
# The server refuses a request whose prompt and max_tokens together exceed its window (131,072 tokens): "This model's
# maximum context length is 131072 tokens. However, you requested 64000 output tokens and your prompt contains at
# least 67073 input tokens" (runs/gen_03, 2026-09-30). Claude Code sends the same max_tokens whatever the prompt's size
# and does not recover from that message. (The message's "at least N input tokens" is only the window less the output
# asked for, plus one, not the prompt's size.) So the writer talks to a relay in this process that passes every
# request to the server unchanged, and when the server refuses one for that reason, counts the prompt's tokens with
# the server's own counter (/v1/messages/count_tokens), lowers max_tokens to the room left (the window, less the
# prompt, less a margin) and sends it again; each such lowering is logged. Responses stream through as they come.
TOO_LONG = re.compile(rb"maximum context length is (\d+) tokens\. However, you requested (\d+) output tokens")
COUNTED_FIELDS = ("model", "messages", "system", "tools", "tool_choice", "thinking")
CLAMP_MARGIN = 256
CLAMP_FLOOR = 1024
HOP = {"connection", "keep-alive", "proxy-authenticate", "proxy-authorization", "te", "trailers", "transfer-encoding",
       "upgrade", "content-length", "host"}
RELAY = {"url": None, "log": None}
_relay_lock = threading.Lock()


def _log_clamp(row: dict):
    if RELAY["log"]:
        with _relay_lock, open(RELAY["log"], "a") as fh:
            fh.write(json.dumps(row) + "\n")


class _Relay(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args):
        pass

    def do_GET(self):
        self._relay("GET")

    def do_POST(self):
        self._relay("POST")

    def _relay(self, method: str):
        length = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(length) if length else None
        headers = {k: v for k, v in self.headers.items() if k.lower() not in HOP}
        up = urlsplit(BASE_URL)
        for attempt in range(4):
            conn = http.client.HTTPConnection(up.hostname, up.port, timeout=900)
            conn.request(method, self.path, body=body, headers=headers)
            resp = conn.getresponse()
            if resp.status == 400 and body:
                text = resp.read()
                m = TOO_LONG.search(text)
                if m and attempt < 3:
                    window, asked = int(m.group(1)), int(m.group(2))
                    data = json.loads(body)
                    prompt = self._count(up, data, headers)
                    margin = CLAMP_MARGIN * 8 ** attempt  # 256, 2048, 16384
                    room = window - prompt - margin if prompt else asked // 2
                    if CLAMP_FLOOR <= room < asked:
                        data["max_tokens"] = room
                        body = json.dumps(data).encode()
                        try:
                            session = json.loads((data.get("metadata") or {}).get("user_id") or "{}").get("session_id")
                        except ValueError:
                            session = None
                        _log_clamp({"utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                    "session_id": session, "asked": asked, "prompt_tokens": prompt,
                                    "window": window, "margin": margin, "max_tokens": room})
                        conn.close()
                        continue
                self._whole(resp, text)
                conn.close()
                return
            self._stream(resp)
            conn.close()
            return

    @staticmethod
    def _count(up, data: dict, headers: dict) -> int | None:
        """The prompt's tokens by the server's own counter, or None."""
        try:
            conn = http.client.HTTPConnection(up.hostname, up.port, timeout=300)
            conn.request("POST", "/v1/messages/count_tokens",
                         body=json.dumps({k: data[k] for k in COUNTED_FIELDS if k in data}).encode(),
                         headers={k: v for k, v in headers.items() if k.lower() != "accept-encoding"})
            resp = conn.getresponse()
            out = json.loads(resp.read()) if resp.status == 200 else {}
            conn.close()
            return int(out["input_tokens"]) if "input_tokens" in out else None
        except (OSError, ValueError, http.client.HTTPException):
            return None

    def _headers(self, resp):
        self.send_response(resp.status)
        for k, v in resp.getheaders():
            if k.lower() not in HOP:
                self.send_header(k, v)

    def _whole(self, resp, text: bytes):
        self._headers(resp)
        self.send_header("Content-Length", str(len(text)))
        self.end_headers()
        self.wfile.write(text)

    def _stream(self, resp):
        self._headers(resp)
        self.send_header("Transfer-Encoding", "chunked")
        self.end_headers()
        try:
            while True:
                chunk = resp.read1(65536)
                if not chunk:
                    break
                self.wfile.write(b"%x\r\n%s\r\n" % (len(chunk), chunk))
                self.wfile.flush()
            self.wfile.write(b"0\r\n\r\n")
            self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            self.close_connection = True


def start_relay(log: Path | None = None) -> str:
    """The relay's URL; started on first use, on a free local port, in a daemon thread of this process."""
    with _relay_lock:
        if log is not None:
            RELAY["log"] = log
        if RELAY["url"] is None:
            server = ThreadingHTTPServer(("127.0.0.1", 0), _Relay)
            server.daemon_threads = True
            threading.Thread(target=server.serve_forever, daemon=True).start()
            RELAY["url"] = f"http://127.0.0.1:{server.server_address[1]}"
    return RELAY["url"]


def writer_env(config: Path) -> dict:
    node_bin = str(Path(os.path.realpath(shutil.which("node") or "/usr/bin/node")).parent)
    return {"HOME": str(Path.home()), "USER": os.getenv("USER", "yusf"), "LANG": "C.UTF-8", "TERM": "dumb",
            "PATH": os.pathsep.join([str(Path(CLAUDE_BIN).parent), node_bin, "/usr/local/bin", "/usr/bin", "/bin"]),
            "CLAUDE_CONFIG_DIR": str(config), "ENABLE_CLAUDEAI_MCP_SERVERS": "false", "DISABLE_AUTOUPDATER": "1",
            "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
            # "Authorization: Bearer", which the self-host checks (ANTHROPIC_API_KEY would go out as x-api-key: 401)
            "ANTHROPIC_BASE_URL": start_relay(), "ANTHROPIC_AUTH_TOKEN": selfhost_key(),
            # any model alias Claude Code resolves on its own goes to the same served model
            "ANTHROPIC_DEFAULT_HAIKU_MODEL": MODEL, "ANTHROPIC_DEFAULT_SONNET_MODEL": MODEL,
            "ANTHROPIC_DEFAULT_OPUS_MODEL": MODEL, "CLAUDE_CODE_MAX_OUTPUT_TOKENS": str(MAX_OUTPUT_TOKENS)}


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
        stdout, stderr, code = run_process(cmd, env, call.workspace, call.prompt, WRITER_TIMEOUT)
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
                  "claude_config_dir": str(config), "base_url": BASE_URL, "timeout_s": WRITER_TIMEOUT,
                  "kit_timeout_s": call.timeout, "max_output_tokens": MAX_OUTPUT_TOKENS,
                  "relay": "window relay (max_tokens lowered to the room left when the server refuses)"}
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


def install(clamp_log: Path | None = None):
    if agent.BACKEND != "muse":
        raise SystemExit("set AUTOGEN_BACKEND=muse: every role but the writer stays on Muse")
    start_relay(clamp_log)
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
