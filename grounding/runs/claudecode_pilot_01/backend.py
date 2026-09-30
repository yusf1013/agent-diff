"""Claude Code (`claude -p`) as a solver backend of our runner, with the contract of OpenClaw's adapter.

`run_attempt(case, attempt, ...)` mirrors `grounding/integrations/openclaw/runtime.run_attempt(..., layout="judge")`:
the same environment side (imported from it), the same skills and curl shim, the same evidence layout, so judge v2,
the scoring, `blind_sample.py` and `adjudicate.py` read a Claude Code run as they read an OpenClaw run. One attempt:

1. installs the case seed as a UUID-named template, opens a fresh environment, checks it equals the installed state;
2. builds a run directory `~/.cc-state/<hex>/` with nothing of the benchmark in its names: a working directory with
   the four API skills in `.claude/skills/` (the files OpenClaw's runs read), a curl shim with the run's environment
   written in, and a fresh Claude Code configuration directory (`CLAUDE_CONFIG_DIR`): no user settings, no account
   skills, no memory, no history;
3. runs `claude -p` once on the prefixed prompt (no follow-up turn) with only the Bash, Read and Skill tools, no MCP
   servers and the claude.ai connectors off, for at most TIMEOUT_SECONDS; for a test with a clock (Calendar, and the
   tests the rulings gave one) the wall clock is shifted (clock/fakeclock.c);
4. records the state after the run, the diff, the transcript as judge steps, the context Claude Code put around the
   prompt, usage and the plan's rate-limit windows, then deletes the environment, the template and the run directory.

Authentication (never a copy of the login's credentials file; nothing a run does can refresh or rotate the login):
- `token-file`: a long-lived token made once by the PI with `claude setup-token`, read from TOKEN_FILE;
- `login`: the current access token of this machine's Claude login, read from `~/.claude/.credentials.json` at
  launch and passed as `CLAUDE_CODE_OAUTH_TOKEN`; the refresh token is never read. A run starts only with more than
  its limit plus ten minutes left on the token;
- `selfhost`: the self-hosted Qwen through its Anthropic Messages endpoint (`ANTHROPIC_AUTH_TOKEN`).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

from grounding.integrations.agentdiff.runtime import ddl_lock, engine_for, environment_schema, write
from grounding.integrations.openclaw import runtime as oc

HERE = Path(__file__).resolve().parent
SKILLS = oc.HERE / "skills"
CLAUDE_BIN = shutil.which("claude") or str(Path.home() / ".nvm/versions/node/v24.19.0/bin/claude")
STATE_ROOT = Path.home() / ".cc-state"
TIMEOUT_SECONDS = 600  # the PI's 10-minute budget, OpenClaw's turn limit
MODEL = "claude-sonnet-5-5"
EFFORT = "medium"  # the label the Qwen and Sol rounds carry
TOOLS = "Bash,Read,Skill"  # the lead's boundary (2026-09-30): curl, the docs, the skills; no web, no sub-agents
TOKEN_FILE = Path(os.getenv("CLAUDE_SOLVER_TOKEN_FILE", Path.home() / ".config" / "claude-solver" / "oauth_token"))
LOGIN_CREDENTIALS = Path.home() / ".claude" / ".credentials.json"
SELFHOST_URL = "http://127.0.0.1:18000"
SELFHOST_MODEL = "qwen3.8-27b"
SELFHOST_KEY_FILE = Path.home() / "qwen-selfhost" / "secrets" / "api_key"
FAKECLOCK_SRC = HERE / "clock" / "fakeclock.c"
FAKECLOCK_DIR = Path.home() / ".cache" / "harness-clock"
LEAK_TOKENS = oc.LEAK_TOKENS + ("claudecode_pilot", "harness_scout")
EMAIL_LINE = re.compile(r"(The user's email address is )(\S+@\S+?)(\. Use it)")
PROVIDER_ERROR = re.compile(r"API Error|Failed to authenticate|usage limit|limit reached|Overloaded|overloaded_error|"
                            r"Connection error|rate.?limit|Invalid API key|OAuth token|credit balance", re.I)
DEBUG_API_ERROR = re.compile(r"^(\S+) \[ERROR\] API error \(attempt (\d+)/(\d+)\)")
DEBUG_TIME = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z) ")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------- authentication


def auth_env(mode: str, timeout_s: int) -> tuple[dict, str]:
    """The variables that authenticate one run, and a description of them without the secret."""
    if mode == "selfhost":
        key = SELFHOST_KEY_FILE.read_text().strip()
        return ({"ANTHROPIC_BASE_URL": SELFHOST_URL, "ANTHROPIC_AUTH_TOKEN": key},
                f"self-hosted Qwen, key from {SELFHOST_KEY_FILE}")
    if mode == "token-file":
        token = TOKEN_FILE.read_text().strip()
        return {"CLAUDE_CODE_OAUTH_TOKEN": token}, f"`claude setup-token` token from {TOKEN_FILE}"
    if mode == "login":
        oauth = json.loads(LOGIN_CREDENTIALS.read_text())["claudeAiOauth"]
        left = oauth["expiresAt"] / 1000 - time.time()
        if left < timeout_s + 600:
            raise RuntimeError(f"R4 login token: {left / 60:.0f} min left, too little for a run; retry after the login "
                               "refreshes it (any Claude Code session does), or use a setup-token")
        return ({"CLAUDE_CODE_OAUTH_TOKEN": oauth["accessToken"]},
                f"the Claude login's current access token, read-only ({left / 60:.0f} min left at launch; the "
                "refresh token is never read)")
    raise ValueError(f"unknown auth mode {mode!r}")


def default_auth(backend: str) -> str:
    if backend == "selfhost":
        return "selfhost"
    return "token-file" if TOKEN_FILE.exists() else "login"


# ---------------------------------------------------------------- the run directory


def fakeclock() -> Path:
    """The LD_PRELOAD wall-clock shift, compiled once per source version."""
    digest = hashlib.sha256(FAKECLOCK_SRC.read_bytes()).hexdigest()[:12]
    so = FAKECLOCK_DIR / f"fakeclock-{digest}.so"
    if not so.exists():
        so.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["gcc", "-shared", "-fPIC", "-O2", "-o", str(so), str(FAKECLOCK_SRC), "-ldl"], check=True)
    return so


def curl_shim(dest: Path, backend_url: str, env_id: str) -> Path:
    """OpenClaw's curl shim with the run's environment written in and its comments dropped, so no variable has to
    reach Claude Code's shell."""
    text = (oc.SHIM_DIR / "curl").read_text()
    text = text.replace('if [[ -z "${AGENTDIFF_BACKEND_URL:-}" || -z "${AGENTDIFF_ENV_ID:-}" ]]; then\n'
                        '  exec "$real" "$@"\nfi\n', "")
    text = text.replace("${AGENTDIFF_BACKEND_URL}", backend_url).replace("${AGENTDIFF_ENV_ID}", env_id)
    text = text.replace('if [[ -n "${AGENTDIFF_API_KEY:-}" ]]; then\n'
                        '  new_args+=("-H" "Authorization: Bearer ${AGENTDIFF_API_KEY}")\nfi\n', "")
    text = "".join(line for i, line in enumerate(text.splitlines(keepends=True))
                   if not line.lstrip().startswith("#") or (i == 0 and line.startswith("#!")))
    if "AGENTDIFF" in text.upper() or "agent_diff" in text:
        raise ValueError("curl shim: a benchmark reference survived the rewrite")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text)
    dest.chmod(0o755)
    return dest


def build_run_dir(root: Path, backend_url: str, env_id: str) -> dict:
    work, config = root / "work", root / "config"
    shutil.copytree(SKILLS, work / ".claude" / "skills")
    config.mkdir(parents=True)
    curl_shim(root / "bin" / "curl", backend_url, env_id)
    skills = {str(p.relative_to(work / ".claude" / "skills")): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted((work / ".claude" / "skills").rglob("*.md"))}
    return {"work": work, "config": config, "bin": root / "bin", "skills_sha256": skills}


def process_env(run: dict, domain: str, fake_now: datetime | None, auth: dict) -> tuple[dict, dict | None]:
    """A clean environment: none of the launching session's variables, the shim first on PATH, a fresh
    configuration directory, the claude.ai connectors and non-essential traffic off. For a test with a clock, the
    wall clock is shifted and Calendar gets Los Angeles time, as OpenClaw's runs do."""
    node_bin = str(Path(os.path.realpath(shutil.which("node") or "/usr/bin/node")).parent)
    env = {"HOME": str(Path.home()), "USER": os.getenv("USER", "yusf"), "LANG": "C.UTF-8", "TERM": "dumb",
           "PATH": os.pathsep.join([str(run["bin"]), node_bin, "/usr/local/bin", "/usr/bin", "/bin"]),
           "CLAUDE_CONFIG_DIR": str(run["config"]), "ENABLE_CLAUDEAI_MCP_SERVERS": "false",
           "DISABLE_AUTOUPDATER": "1", "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1", **auth}
    clock = None
    if fake_now is not None:
        if domain == "calendar":
            env["TZ"] = oc.CALENDAR_TZ
        offset = int(fake_now.timestamp() - time.time())
        # clock_gettime only: Claude Code's date and its shell's follow it; time(), which TLS uses, stays real.
        env.update(LD_PRELOAD=str(fakeclock()), SHIFT_OFFSET=str(offset), SHIFT_FUNCS="clock_gettime")
        clock = {"start": fake_now.isoformat(), "timezone": env.get("TZ", "the machine's"),
                 "method": "LD_PRELOAD clock_gettime shift (clock/fakeclock.c)", "offset_s": offset}
    return env, clock


def command(prompt: str, model: str, effort: str, backend: str) -> list[str]:
    window = ["--autocompact", "131k"] if backend == "selfhost" else []  # Claude Code does not know Qwen's window
    return [CLAUDE_BIN, "-p", prompt, "--model", model, "--effort", effort, *window, "--output-format", "stream-json",
            "--verbose", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}', "--setting-sources", "project",
            "--tools", TOOLS, "--permission-mode", "bypassPermissions", "--debug-file", "DEBUG_FILE"]


def run_process(cmd: list[str], env: dict, cwd: Path, timeout_s: int, out: Path) -> dict:
    """Run the harness in its own process group; kill the group at the limit."""
    started = time.time()
    with open(out / "stdout.jsonl", "wb") as stdout, open(out / "stderr.txt", "wb") as stderr:
        proc = subprocess.Popen(cmd, cwd=cwd, env=env, stdout=stdout, stderr=stderr, stdin=subprocess.DEVNULL,
                                start_new_session=True)
        killed = None
        try:
            proc.wait(timeout=timeout_s)
        except subprocess.TimeoutExpired:
            killed = "timeout"
            try:
                os.killpg(proc.pid, signal.SIGTERM)
                proc.wait(timeout=15)
            except (ProcessLookupError, subprocess.TimeoutExpired):
                try:
                    os.killpg(proc.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                proc.wait()
    return {"returncode": proc.returncode, "killed": killed, "duration_s": round(time.time() - started, 1)}


# ---------------------------------------------------------------- the transcript


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(errors="replace").splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


def steps_from_stream(events: list[dict]) -> list[dict]:
    """One step per tool call with its result, in OpenClaw's step shape (turn, tool, arguments, action, text,
    thinking, usage, observation); the model's text and thinking before a call ride on that call's step, and a final
    answer without a call becomes a step of its own. Content blocks of one API response arrive as separate events
    sharing a message id; the response's usage is kept once, on its first step."""
    steps, by_id, seen = [], {}, set()
    text, thinking = [], []
    for ev in events:
        if ev.get("type") == "assistant":
            msg = ev.get("message") or {}
            mid = msg.get("id")
            usage = None
            if mid not in seen:
                seen.add(mid)
                usage = msg.get("usage")
            for block in msg.get("content") or []:
                kind = block.get("type")
                if kind == "text":
                    text.append(block.get("text") or "")
                elif kind == "thinking":
                    thinking.append(block.get("thinking") or "")
                elif kind == "tool_use":
                    args = block.get("input") or {}
                    name = block.get("name")
                    step = {"turn": 1, "tool": name, "arguments": args,
                            "action": args.get("command") if name == "Bash" else f"{name} {json.dumps(args)}",
                            "text": "\n".join(t for t in text if t).strip(),
                            "thinking": "\n".join(t for t in thinking if t).strip(), "usage": usage}
                    usage = None
                    text, thinking = [], []
                    steps.append(step)
                    by_id[block.get("id")] = step
        elif ev.get("type") == "user":
            for block in (ev.get("message") or {}).get("content") or []:
                if isinstance(block, dict) and block.get("type") == "tool_result":
                    content = block.get("content")
                    if isinstance(content, list):
                        content = "\n".join(c.get("text", "") for c in content if isinstance(c, dict))
                    step = by_id.get(block.get("tool_use_id"))
                    if step is not None:
                        step["observation"] = {"stdout": content or "", "is_error": bool(block.get("is_error"))}
    if text or thinking:
        steps.append({"turn": 1, "tool": None, "text": "\n".join(t for t in text if t).strip(),
                      "thinking": "\n".join(t for t in thinking if t).strip()})
    return steps


def stream_usage(events: list[dict]) -> dict:
    """Usage from the transcript: per API response (by message id), the run's totals as Claude Code reports them,
    its list-price estimate, and the plan's rate-limit windows as the run saw them first and last."""
    totals = {"requests": 0, "input_tokens": 0, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0,
              "output_tokens": 0, "source": "claude -p stream-json (per-response usage, deduplicated by message id)"}
    seen = set()
    windows = []
    result = {}
    for ev in events:
        if ev.get("type") == "assistant":
            msg = ev.get("message") or {}
            if msg.get("id") in seen:
                continue
            seen.add(msg.get("id"))
            usage = msg.get("usage") or {}
            totals["requests"] += 1
            for key in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "output_tokens"):
                totals[key] += int(usage.get(key) or 0)
        elif ev.get("type") == "rate_limit_event" and (ev.get("rate_limit_info") or {}).get("unifiedWindows"):
            info = ev.get("rate_limit_info") or {}
            windows.append({"status": info.get("status"), "type": info.get("rateLimitType"),
                            "overage": info.get("overageStatus"),
                            "windows": {k: {"utilization": v.get("utilization"), "resets_at": v.get("resetsAt")}
                                        for k, v in (info.get("unifiedWindows") or {}).items()}})
        elif ev.get("type") == "result":
            result = ev
    # Per-response output counts in the stream are partial (they are taken when a response starts); the result's
    # totals are Claude Code's own final counts.
    final = result.get("usage") or {}
    totals.update(result_usage={k: final.get(k) for k in ("input_tokens", "cache_read_input_tokens",
                                                          "cache_creation_input_tokens", "output_tokens")},
                  thinking_tokens=(final.get("output_tokens_details") or {}).get("thinking_tokens"),
                  model_usage=result.get("modelUsage"), list_cost_usd=result.get("total_cost_usd"),
                  num_turns=result.get("num_turns"), duration_api_ms=result.get("duration_api_ms"),
                  plan_windows_first=windows[0] if windows else None,
                  plan_windows_last=windows[-1] if windows else None, rate_limit_events=len(windows))
    return totals


def session_file(run: dict, session_id: str | None) -> Path | None:
    folder = run["config"] / "projects" / re.sub(r"[^A-Za-z0-9-]", "-", str(run["work"]))
    if session_id and (folder / f"{session_id}.jsonl").exists():
        return folder / f"{session_id}.jsonl"
    found = sorted(folder.glob("*.jsonl")) if folder.exists() else []
    return found[-1] if found else None


def context_of(rows: list[dict]) -> dict:
    """What Claude Code put around the prompt: the system prompt snapshot and the rendered context attachments."""
    system, attachments = None, []
    for row in rows:
        if row.get("type") != "attachment":
            continue
        a = row.get("attachment") or {}
        if a.get("type") == "prompt_snapshot":
            system = system or "\n".join(a.get("systemPrompt") or [])
            continue
        rendered = [r.get("content") if isinstance(r, dict) else r for r in row.get("rendered") or []]
        attachments.append({"type": a.get("type"), "rendered": rendered or None, "raw": None if rendered else a})
    return {"system_prompt": system, "attachments": attachments}


def leaks(text: str, case_id: str) -> list[str]:
    body = text.lower()
    scenario = re.sub(r"^(at|fp|p|uc|u|h)-", "", case_id.lower())
    m = re.match(r"((?:[a-z]+\d?-)?[a-z]{3}-\d+)", scenario)
    tokens = list(LEAK_TOKENS) + [case_id.lower()] + ([m.group(1)] if m else [])
    return sorted({t for t in tokens if t in body})


def redact_account_email(folder: Path) -> int:
    """Keep an account email Claude Code may put in context out of the evidence (the sentence stays)."""
    files = [p for p in folder.rglob("*") if p.is_file()]
    found = set()
    for path in files:
        found.update(m.group(2) for m in EMAIL_LINE.finditer(path.read_text(errors="replace")))
    changed = 0
    for path in files:
        text = path.read_text(errors="replace")
        new = EMAIL_LINE.sub(r"\1[account email]\3", text)
        for address in found:
            new = new.replace(address, "[account email]")
        if new != text:
            path.write_text(new)
            changed += 1
    return changed


def api_error_seconds(debug_log: Path) -> tuple[float, int]:
    """Seconds spent in streaks of failed API requests (Claude Code retries them itself), from its debug log."""
    if not debug_log.exists():
        return 0.0, 0
    lines = debug_log.read_text(errors="replace").splitlines()
    stamps = []
    for line in lines:
        m = DEBUG_TIME.match(line)
        if m:
            stamps.append((datetime.fromisoformat(m.group(1).replace("Z", "+00:00")), bool(DEBUG_API_ERROR.match(line))))
    spent, errors, start = 0.0, 0, None
    for stamp, is_error in stamps:
        if is_error:
            errors += 1
            start = start or stamp
        elif start is not None:
            spent += (stamp - start).total_seconds()
            start = None
    if start is not None and stamps:
        spent += (stamps[-1][0] - start).total_seconds()
    return round(spent, 1), errors


def infrastructure(proc: dict, result: dict, windows: list, error_s: float, timeout_s: int) -> str | None:
    """Ours to re-run, never the agent's failure:
    R1 no result: the process ended without a result, and not at the limit;
    R3 provider: the result is an error from the API, the login or the plan's limits;
    R5 plan window: the plan refused a request (a window full);
    R2 provider time: the run hit the limit after more than a quarter of it in failing, retried API requests."""
    text = str(result.get("result") or "")
    if not proc["killed"] and not result:
        return f"R1 no result: claude exited with code {proc['returncode']} and no result"
    if result.get("is_error") and (PROVIDER_ERROR.search(text) or result.get("subtype") == "error_during_execution"):
        return f"R3 provider error: {text[:200] or result.get('subtype')}"
    if any(w.get("status") == "rejected" for w in windows):
        return "R5 plan window: a request was refused by the plan's rate limits"
    if proc["killed"] and error_s > 0.25 * timeout_s:
        return f"R2 provider time: the run hit the {timeout_s} s limit after {error_s:.0f} s of failing API requests"
    return None


# ---------------------------------------------------------------- one attempt


def run_attempt(case: dict, attempt: Path, *, database_url: str, backend_url: str,
                timeout_s: int = TIMEOUT_SECONDS, followup: bool = False, keep_state: bool = False,
                summary: dict | None = None, backend: str = "plan", layout: str = "judge", model: str | None = None,
                effort: str = EFFORT, auth: str | None = None) -> dict:
    """Run one case through `claude -p`; write evidence under `attempt`; return the execution summary. The keyword
    arguments follow OpenClaw's run_attempt; `followup` must be False (the judge grades turn 1), and the layout is
    always the judge's."""
    from agent_diff import AgentDiff
    if followup or layout != "judge":
        raise ValueError("the Claude Code backend runs one turn in the judge layout")
    domain = case["domain"]
    summary = summary if summary is not None else {}
    environment_dir, solver_dir = attempt / "environment", attempt / "solver"
    raw_dir = solver_dir / "claude"
    raw_dir.mkdir(parents=True, exist_ok=True)
    engine = engine_for(database_url)
    client = AgentDiff(base_url=backend_url)
    env = prepared = None
    root = STATE_ROOT / uuid.uuid4().hex[:16]
    auth = auth or default_auth(backend)
    model = model or (SELFHOST_MODEL if backend == "selfhost" else MODEL)
    try:
        auth_vars, auth_note = auth_env(auth, timeout_s)
        prepared = oc.prepare(case, environment_dir / "preflight", database_url, backend_url)
        with ddl_lock():
            env = client.init_env(templateService=domain, templateName=prepared["template_name"],
                                  impersonateUserId=case["acting_user_id"])
        schema = environment_schema(engine, env.environmentId, prepared["template_id"])
        initial = oc.export(domain, engine, schema)
        installed = json.loads(Path(prepared["initial_state_path"]).read_text())
        if oc.semantic_digest(domain, initial) != oc.semantic_digest(domain, installed):
            raise ValueError("Fresh environment differs from the prepared initial state")
        write(environment_dir / "initial_state.json", initial)
        Path(prepared["initial_state_path"]).unlink()  # identical to initial_state.json; prepared.json keeps its sha256
        summary.setdefault("compacted", []).append("environment/preflight/initial_state.json")
        run_id = client.start_run(envId=env.environmentId).runId

        root.mkdir(parents=True)
        run = build_run_dir(root, backend_url, env.environmentId)
        fake_now = oc.case_clock(case)
        proc_env, clock = process_env(run, domain, fake_now, auth_vars)
        prompt = oc.PREFIX[domain] + case["prompt"]
        cmd = command(prompt, model, effort, backend)
        cmd[cmd.index("DEBUG_FILE")] = str(raw_dir / "debug.log")
        version = subprocess.run([CLAUDE_BIN, "--version"], capture_output=True, text=True,
                                 env={k: v for k, v in proc_env.items() if k != "LD_PRELOAD"}).stdout.strip()
        write(solver_dir / "config.json", {
            "harness": "claude-code", "claude_code_version": version, "backend": backend, "model": model,
            "effort": effort, "tools": TOOLS, "layout": layout, "auth": auth, "auth_note": auth_note,
            "command": ["<prompt>" if part == prompt else part for part in cmd], "prompt": prompt,
            "prompt_prefix": oc.PREFIX[domain], "follow_up": {"enabled": False},
            "timeout_seconds_per_turn": timeout_s, "fake_clock": clock,
            "env_keys": sorted(proc_env), "state_dir": str(root), "work_dir": str(run["work"]),
            "config_dir": str(run["config"]), "skills_sha256": run["skills_sha256"],
            "curl_shim_sha256": hashlib.sha256((run["bin"] / "curl").read_bytes()).hexdigest(),
            "fakeclock_sha256": hashlib.sha256(FAKECLOCK_SRC.read_bytes()).hexdigest() if clock else None,
            "environment_id": env.environmentId, "run_id": run_id, "case_sha256": case.get("case_sha256")})
        summary.update(status="solver_running", environment_id=env.environmentId)
        write(attempt / "execution_summary.json", summary)

        proc = run_process(cmd, proc_env, run["work"], timeout_s, raw_dir)
        write(environment_dir / "final_state.json", oc.export(domain, engine, schema))
        try:
            write(environment_dir / "diff_run.json", client.diff_run(runId=run_id).model_dump(mode="json"))
        except Exception as exc:  # recorded, not fatal: states are the grading evidence
            summary["diff_error"] = f"{type(exc).__name__}: {exc}"
        client.evaluate_run(runId=run_id, expectedOutput={"assertions": []})

        events = read_jsonl(raw_dir / "stdout.jsonl")
        result = next((e for e in events if e.get("type") == "result"), {})
        init = next((e for e in events if e.get("type") == "system" and e.get("subtype") == "init"), {})
        windows = [e.get("rate_limit_info") or {} for e in events if e.get("type") == "rate_limit_event"]
        session = session_file(run, init.get("session_id"))
        context = {}
        if session is not None:
            context = context_of(read_jsonl(session))
            shutil.copyfile(session, raw_dir / "session.jsonl")
        write(raw_dir / "context.json", context)
        opening = json.dumps(context) + "\n" + prompt
        steps = steps_from_stream(events)
        final = "" if proc["killed"] else str(result.get("result") or "")
        error_s, api_errors = api_error_seconds(raw_dir / "debug.log")
        infra = infrastructure(proc, result, windows, error_s, timeout_s)
        termination = "timeout" if proc["killed"] else ("error" if infra or result.get("is_error") else "done")
        (solver_dir / "final_response.md").write_text(final + "\n")
        record = {"test_id": case["case_id"], "question": prompt, "harness": "claude-code",
                  "termination": termination, "final": final,
                  "turns": [{"label": "turn1", "message": prompt, "text": final, "termination": termination,
                             "returncode": proc["returncode"], "killed": proc["killed"],
                             "duration_s": proc["duration_s"], "stop_reason": result.get("stop_reason"),
                             "result_subtype": result.get("subtype")}],
                  "steps": oc.judge_steps(steps), "followup_steps": []}
        write(solver_dir / f"{case['case_id']}.json", record)
        flags = {"init": {k: init.get(k) for k in ("model", "permissionMode", "tools", "mcp_servers", "skills",
                                                   "agents", "plugins", "apiKeySource", "claude_code_version")},
                 "tool_calls": len([s for s in steps if s.get("tool")]), "api_errors": api_errors,
                 "api_error_seconds": error_s, "prompt_leaks": leaks(opening, case["case_id"]),
                 "account_email_in_context": bool(EMAIL_LINE.search(opening)),
                 "unexpected_mcp_or_tools": bool(init) and (bool(init.get("mcp_servers")) or
                                                             sorted(init.get("tools") or []) != sorted(TOOLS.split(",")))}
        if fake_now is not None:
            flags["clock_suspects"] = oc.clock_scan(steps, [final], real_year=domain == "calendar")
            shown = [a for a in context.get("attachments", []) if a.get("type") == "date"]
            flags["context_date"] = (shown[0]["rendered"] or [None])[0] if shown else None
        summary.update(status="completed", termination=termination, flags=flags, turns=flags["tool_calls"],
                       usage=stream_usage(events), turn_durations_s=[proc["duration_s"]])
        if infra:
            summary.update(status="infrastructure_error", error=infra)
        elif flags["prompt_leaks"] or flags["unexpected_mcp_or_tools"]:
            summary.update(status="infrastructure_error",
                           error=f"isolation: leaks {flags['prompt_leaks']}, init tools {init.get('tools')}, "
                                 f"mcp {init.get('mcp_servers')}")
        if flags["account_email_in_context"]:
            flags["account_email_redacted_files"] = redact_account_email(raw_dir)
    except Exception as exc:
        summary.update(status="infrastructure_error", error=f"{type(exc).__name__}: {exc}")
    finally:
        try:
            for link in [p for p in raw_dir.iterdir() if p.is_symlink()] if raw_dir.exists() else []:
                link.unlink()  # Claude Code's "latest" pointer to the debug log
            if raw_dir.exists() and any(raw_dir.iterdir()):
                oc.bundle(raw_dir, solver_dir / "claude.tar.xz")
        except Exception as exc:
            summary["bundle_error"] = f"{type(exc).__name__}: {exc}"
        if env is not None:
            try:
                with ddl_lock():
                    client.delete_env(envId=env.environmentId)
            except Exception as exc:
                summary["delete_env_error"] = f"{type(exc).__name__}: {exc}"
        if prepared is not None:
            try:
                oc.cleanup_template(case, prepared, database_url)
            except Exception as exc:
                summary["cleanup_error"] = f"{type(exc).__name__}: {exc}"
        engine.dispose()
        if root.exists() and not keep_state:  # the evidence already holds the transcript and the context
            shutil.rmtree(root, ignore_errors=True)
    return summary
