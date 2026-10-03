"""Run one of our AgentDiff cases through a vendor agent harness: Claude Code (`claude -p`) or Codex (`codex exec`).

A smoke adapter for harness_scout_01, built on OpenClaw's (grounding/integrations/openclaw/runtime.py), whose
environment, state export, clock and judge-step helpers it imports unchanged. One attempt:
1. installs the case seed as a UUID-named template, opens a fresh environment, checks it equals the installed state;
2. builds a neutral run directory (~/.cc-state/<hex> or ~/.cx-state/<hex>): a working directory, the four API skills
   (the same files OpenClaw's runs read), and a curl shim with the run's environment written into it;
3. launches the harness headless on the case prompt (with OpenClaw's domain prefix), limited to TIMEOUT_SECONDS;
4. records the state after the run, the diff, the raw transcript and its judge steps, usage, flags (clock suspects,
   context leaks), then deletes the environment, the template and the run directory.

Evidence follows OpenClaw's judge layout (openclaw_eval_01): environment/{initial,final}_state.json, diff_run.json;
solver/<case_id>.json (the record, steps in the toy format), final_response.md, config.json; solver/<harness>/ raw
files; execution_summary.json.

Backends: "plan" (Claude Code on the Claude login of this machine; Codex on the ChatGPT login) and "selfhost" (the
self-hosted Qwen: Claude Code through its Anthropic Messages endpoint, Codex through its Responses endpoint).
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
CODEX_BIN = str(Path.home() / ".vscode-server/extensions/openai.chatgpt-26.917.62051-linux-x64/bin/linux-x86_64/codex")
FAKECLOCK_SRC = HERE / "clock" / "fakeclock.c"
FAKECLOCK_SO = Path.home() / ".cache" / "harness-clock" / "fakeclock.so"
TIMEOUT_SECONDS = 600  # OpenClaw's turn limit, the PI's 10-minute budget
SELFHOST_URL = "http://127.0.0.1:18000"
SELFHOST_MODEL = "qwen3.8-27b"
SELFHOST_KEY_FILE = Path.home() / "qwen-selfhost" / "secrets" / "api_key"
CODEX_AUTH = Path.home() / ".codex" / "auth.json"
STATE_ROOTS = {"claude": Path.home() / ".cc-state", "codex": Path.home() / ".cx-state"}
# Claude Code: only what a run needs (the lead, 2026-09-30): Bash for curl, Read and Skill for the API docs. No web,
# no sub-agents, no file writing tools. MCP: none, and the account's claude.ai connectors off.
CLAUDE_TOOLS = "Bash,Read,Skill"
# Codex: the same boundary. Its account-linked apps (ChatGPT connectors), plugins, browser, computer use, image
# generation and sub-agents are turned off; web search too. The shell and skills stay.
CODEX_DISABLE = ("apps", "plugins", "remote_plugin", "browser_use", "browser_use_external", "computer_use",
                 "image_generation", "multi_agent", "in_app_browser", "tool_suggest", "goals", "memories")
LEAK_TOKENS = oc.LEAK_TOKENS + ("harness_scout", "smoke")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def selfhost_key() -> str:
    return SELFHOST_KEY_FILE.read_text().strip()


def fakeclock() -> Path:
    """The LD_PRELOAD clock shift (clock/fakeclock.c), compiled once per source version."""
    digest = hashlib.sha256(FAKECLOCK_SRC.read_bytes()).hexdigest()[:12]
    so = FAKECLOCK_SO.with_name(f"fakeclock-{digest}.so")
    if not so.exists():
        so.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["gcc", "-shared", "-fPIC", "-O2", "-o", str(so), str(FAKECLOCK_SRC), "-ldl"], check=True)
    return so


# ---------------------------------------------------------------- the run directory


def curl_shim(dest: Path, backend_url: str, env_id: str) -> Path:
    """OpenClaw's curl shim with the run's environment written in and its comments dropped, so neither harness's
    rules for passing environment variables to its shell matter."""
    text = (oc.SHIM_DIR / "curl").read_text()
    text = text.replace('if [[ -z "${AGENTDIFF_BACKEND_URL:-}" || -z "${AGENTDIFF_ENV_ID:-}" ]]; then\n  exec "$real" "$@"\nfi\n', "")
    text = text.replace("${AGENTDIFF_BACKEND_URL}", backend_url).replace("${AGENTDIFF_ENV_ID}", env_id)
    text = text.replace('if [[ -n "${AGENTDIFF_API_KEY:-}" ]]; then\n  new_args+=("-H" "Authorization: Bearer ${AGENTDIFF_API_KEY}")\nfi\n', "")
    lines = [line for i, line in enumerate(text.splitlines(keepends=True))
             if not line.lstrip().startswith("#") or (i == 0 and line.startswith("#!"))]
    text = "".join(lines)
    if "AGENTDIFF" in text.upper() or "agent_diff" in text:
        raise ValueError("curl shim: a benchmark reference survived the rewrite")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text)
    dest.chmod(0o755)
    return dest


def copy_skills(dest: Path) -> dict:
    shutil.copytree(SKILLS, dest)
    return {str(p.relative_to(dest)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(dest.rglob("*.md"))}


def base_env(root: Path, domain: str, fake_now: datetime | None) -> tuple[dict, dict | None]:
    """A clean environment (nothing of this session's variables), the shim first on PATH, and for a test with a
    clock: the clock shift (Claude Code only; see clock/fakeclock.c) and, for Calendar, Los Angeles time."""
    node_bin = str(Path(os.path.realpath(shutil.which("node") or "/usr/bin/node")).parent)
    env = {"HOME": str(Path.home()), "USER": os.getenv("USER", "yusf"), "LANG": "C.UTF-8", "TERM": "dumb",
           "PATH": os.pathsep.join([str(root / "bin"), node_bin, "/usr/local/bin", "/usr/bin", "/bin"])}
    clock = None
    if fake_now is not None:
        if domain == "calendar":
            env["TZ"] = oc.CALENDAR_TZ
        clock = {"start": fake_now.isoformat(), "timezone": env.get("TZ", "the machine's")}
    return env, clock


def shift_clock(env: dict, fake_now: datetime, shared_login: bool) -> dict:
    """Shift clock_gettime's wall clock only: Claude Code's date, `date`, Python and Node children follow it, while
    `time()` stays real so TLS certificate checks (BoringSSL) still pass.

    On the shared login, a shifted process believes the access token is valid for years and never refreshes it; if it
    expired mid-run, the refresh would write an expiry computed from the shifted clock into the file every session
    shares. So the run starts only with more than the run's limit left on the token."""
    if shared_login:
        oauth = json.loads((Path.home() / ".claude" / ".credentials.json").read_text())["claudeAiOauth"]
        left = oauth["expiresAt"] / 1000 - time.time()
        if left < TIMEOUT_SECONDS + 600:
            raise RuntimeError(f"shared Claude token expires in {left / 60:.0f} min; a shifted run waits for a refresh")
    offset = int(fake_now.timestamp() - time.time())
    env.update(LD_PRELOAD=str(fakeclock()), SHIFT_OFFSET=str(offset), SHIFT_FUNCS="clock_gettime")
    return {"method": "LD_PRELOAD clock_gettime shift", "offset_s": offset}


# ---------------------------------------------------------------- Claude Code


def claude_setup(root: Path, backend: str, model: str | None, effort: str) -> dict:
    work = root / "work"
    skills = copy_skills(work / ".claude" / "skills")
    spec = {"work": work, "skills_sha256": skills, "config_dir": None, "model": model or "claude-sonnet-5-5"}
    if backend == "selfhost":
        # A fresh configuration directory: no login, no account email, no user settings; the key goes to the
        # self-hosted endpoint only.
        spec["config_dir"] = root / "config"
        spec["config_dir"].mkdir(parents=True)
        spec["model"] = model or SELFHOST_MODEL
    # Claude Code does not know this model's window; it would compact against its default. The served window is
    # 131,072 tokens.
    window = ["--autocompact", "131k"] if backend == "selfhost" else []
    spec["cmd"] = [CLAUDE_BIN, "-p", None, "--model", spec["model"], "--effort", effort, *window,
                   "--output-format", "stream-json", "--verbose", "--strict-mcp-config", "--mcp-config",
                   '{"mcpServers":{}}', "--setting-sources", "project", "--tools", CLAUDE_TOOLS,
                   "--permission-mode", "bypassPermissions"]
    return spec


def claude_env(env: dict, spec: dict, backend: str) -> dict:
    env = dict(env, ENABLE_CLAUDEAI_MCP_SERVERS="false", DISABLE_AUTOUPDATER="1",
               CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1")
    if backend == "selfhost":
        # ANTHROPIC_AUTH_TOKEN goes out as "Authorization: Bearer", which the self-host checks (ANTHROPIC_API_KEY
        # would go out as x-api-key and get 401).
        env.update(CLAUDE_CONFIG_DIR=str(spec["config_dir"]), ANTHROPIC_BASE_URL=SELFHOST_URL,
                   ANTHROPIC_AUTH_TOKEN=selfhost_key())
    return env


def claude_session_file(spec: dict, session_id: str | None) -> Path | None:
    base = (spec["config_dir"] or Path.home() / ".claude") / "projects"
    slug = re.sub(r"[^A-Za-z0-9-]", "-", str(spec["work"]))  # Claude Code's project folder name
    folder = base / slug
    if session_id and (folder / f"{session_id}.jsonl").exists():
        return folder / f"{session_id}.jsonl"
    found = sorted(folder.glob("*.jsonl")) if folder.exists() else []
    return found[-1] if found else None


def claude_steps(events: list[dict]) -> tuple[list[dict], dict]:
    """Steps from Claude Code's stream-json: one per tool call with its result; text and thinking kept alongside.
    Content blocks of one API response arrive as separate events with the same message id; usage is counted once
    per message id."""
    steps, by_id, seen = [], {}, set()
    usage = {"requests": 0, "input_tokens": 0, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0,
             "output_tokens": 0}
    pending_text, pending_thinking = [], []
    result = {}
    for ev in events:
        kind = ev.get("type")
        if kind == "assistant":
            msg = ev.get("message") or {}
            mid = msg.get("id")
            if mid and mid not in seen:
                seen.add(mid)
                u = msg.get("usage") or {}
                usage["requests"] += 1
                for key in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "output_tokens"):
                    usage[key] += int(u.get(key) or 0)
            for block in msg.get("content") or []:
                if block.get("type") == "text":
                    pending_text.append(block.get("text") or "")
                elif block.get("type") == "thinking":
                    pending_thinking.append(block.get("thinking") or "")
                elif block.get("type") == "tool_use":
                    args = block.get("input") or {}
                    step = {"turn": 1, "tool": block.get("name"), "arguments": args,
                            "action": args.get("command") if block.get("name") == "Bash" else
                            f"{block.get('name')} {json.dumps(args)}",
                            "text": "\n".join(t for t in pending_text if t).strip(),
                            "thinking": "\n".join(t for t in pending_thinking if t).strip(), "message_id": mid}
                    pending_text, pending_thinking = [], []
                    steps.append(step)
                    by_id[block.get("id")] = step
        elif kind == "user":
            for block in (ev.get("message") or {}).get("content") or []:
                if isinstance(block, dict) and block.get("type") == "tool_result":
                    content = block.get("content")
                    if isinstance(content, list):
                        content = "\n".join(c.get("text", "") for c in content if isinstance(c, dict))
                    step = by_id.get(block.get("tool_use_id"))
                    if step is not None:
                        step["observation"] = {"stdout": content or "", "is_error": bool(block.get("is_error"))}
        elif kind == "result":
            result = ev
    if pending_text or pending_thinking:
        steps.append({"turn": 1, "tool": None, "text": "\n".join(t for t in pending_text if t).strip(),
                      "thinking": "\n".join(t for t in pending_thinking if t).strip()})
    if result:
        usage.update(result_usage=result.get("usage"), model_usage=result.get("modelUsage"),
                     total_cost_usd_list=result.get("total_cost_usd"), num_turns=result.get("num_turns"),
                     duration_api_ms=result.get("duration_api_ms"))
    return steps, usage


def claude_context(session_rows: list[dict]) -> dict:
    """What Claude Code put around the prompt: the system prompt snapshot and the rendered context attachments."""
    system, attachments = None, []
    for row in session_rows:
        if row.get("type") != "attachment":
            continue
        a = row.get("attachment") or {}
        if a.get("type") == "prompt_snapshot" and system is None:
            system = "\n".join(a.get("systemPrompt") or [])
        elif a.get("type") != "prompt_snapshot":
            rendered = [r.get("content") if isinstance(r, dict) else r for r in row.get("rendered") or []]
            attachments.append({"type": a.get("type"), "rendered": rendered or None,
                                "raw": None if rendered else a})
    return {"system_prompt": system, "attachments": attachments}


# ---------------------------------------------------------------- Codex


def codex_setup(root: Path, backend: str, model: str | None, effort: str) -> dict:
    work, home = root / "work", root / "home"
    work.mkdir(parents=True)
    home.mkdir(parents=True)
    skills = copy_skills(home / "skills")
    spec = {"work": work, "home": home, "skills_sha256": skills}
    lines = []
    if backend == "selfhost":
        spec["model"] = model or SELFHOST_MODEL
        # Codex has no metadata for this model and would fall back to generic defaults; the served context is
        # 131,072 tokens (OpenClaw's rounds also capped output at 8,192, which Codex cannot set).
        lines += ['model_provider = "selfhost"', "model_context_window = 131072", "",
                  "[model_providers.selfhost]", 'name = "selfhost"',
                  f'base_url = "{SELFHOST_URL}/v1"', 'env_key = "SELFHOST_KEY"', 'wire_api = "responses"']
    else:
        spec["model"] = model or "gpt-6.1-sol"
        # A copy of the ChatGPT login. Its access token lasts until 2026-10-06 and its last refresh was 2026-09-26,
        # so Codex does not refresh it in a run (a refresh would rotate the token under the PI's own login).
        target = home / "auth.json"
        shutil.copyfile(CODEX_AUTH, target)
        target.chmod(0o600)
        spec["auth_sha256"] = hashlib.sha256(CODEX_AUTH.read_bytes()).hexdigest()
    (home / "config.toml").write_text("\n".join(lines) + "\n")
    cmd = [CODEX_BIN, "exec", "--json", "-m", spec["model"], "-c", f'model_reasoning_effort="{effort}"',
           "-c", 'web_search="disabled"', "--skip-git-repo-check", "--dangerously-bypass-approvals-and-sandbox",
           "-C", str(work), "-o", str(root / "last_message.txt")]
    for feature in CODEX_DISABLE:
        cmd += ["--disable", feature]
    spec["cmd"] = cmd + [None]
    return spec


def codex_env(env: dict, spec: dict, backend: str) -> dict:
    env = dict(env, CODEX_HOME=str(spec["home"]))
    if backend == "selfhost":
        env["SELFHOST_KEY"] = selfhost_key()
    return env


def codex_steps(events: list[dict]) -> tuple[list[dict], dict]:
    """Steps from `codex exec --json`: one per command (or other tool item), with reasoning and messages kept
    alongside, in the order the items completed."""
    steps, pending_text, pending_thinking = [], [], []
    usage = {"turns": 0, "input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0, "reasoning_output_tokens": 0,
             "warnings": []}
    for ev in events:
        kind = ev.get("type")
        if kind == "item.completed":
            item = ev.get("item") or {}
            itype = item.get("type") or item.get("item_type")
            if itype == "reasoning":
                pending_thinking.append(item.get("text") or "")
            elif itype in ("agent_message", "assistant_message"):
                pending_text.append(item.get("text") or "")
            elif itype == "error":  # Codex's own notices (e.g. missing model metadata), not the agent's actions
                usage["warnings"].append(item.get("message"))
            else:
                if itype == "command_execution":
                    tool, args, action = "exec", {"command": item.get("command")}, item.get("command")
                    obs = {"stdout": item.get("aggregated_output") or "",
                           "is_error": (item.get("exit_code") not in (0, None)) or item.get("status") == "failed"}
                else:
                    tool, args = itype, {k: v for k, v in item.items() if k not in ("id", "type", "item_type")}
                    action = f"{itype} {json.dumps(args)[:2000]}"
                    obs = {"stdout": json.dumps(args)[:4000], "is_error": item.get("status") == "failed"}
                steps.append({"turn": 1, "tool": tool, "arguments": args, "action": action,
                              "text": "\n".join(t for t in pending_text if t).strip(),
                              "thinking": "\n".join(t for t in pending_thinking if t).strip(), "observation": obs})
                pending_text, pending_thinking = [], []
        elif kind == "turn.completed":
            u = ev.get("usage") or {}
            usage["turns"] += 1
            for key in ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens"):
                usage[key] += int(u.get(key) or 0)
    if pending_text or pending_thinking:
        steps.append({"turn": 1, "tool": None, "text": "\n".join(t for t in pending_text if t).strip(),
                      "thinking": "\n".join(t for t in pending_thinking if t).strip()})
    return steps, usage


def codex_rollout(home: Path) -> tuple[Path | None, list[dict]]:
    files = sorted((home / "sessions").rglob("rollout-*.jsonl")) if (home / "sessions").exists() else []
    if not files:
        return None, []
    return files[-1], [json.loads(line) for line in files[-1].read_text().splitlines() if line.strip()]


def codex_rollout_usage(rows: list[dict]) -> dict:
    """Per-request usage and the plan's rate-limit record, from the rollout's token_count events."""
    out = {"requests": 0, "last_total": None, "rate_limits_first": None, "rate_limits_last": None}
    for row in rows:
        payload = row.get("payload") or {}
        if row.get("type") == "event_msg" and payload.get("type") == "token_count":
            info = payload.get("info") or {}
            if info.get("last_token_usage"):
                out["requests"] += 1
                out["last_total"] = info.get("total_token_usage")
            if payload.get("rate_limits"):
                out["rate_limits_first"] = out["rate_limits_first"] or payload["rate_limits"]
                out["rate_limits_last"] = payload["rate_limits"]
    return out


def codex_context(rows: list[dict]) -> dict:
    """The base instructions, the developer and user messages before the model's first answer, and the turn context."""
    base, opening, turn_context = None, [], None
    for row in rows:
        payload = row.get("payload") or {}
        if row.get("type") == "session_meta":
            base = (payload.get("base_instructions") or {}).get("text")
        elif row.get("type") == "turn_context" and turn_context is None:
            turn_context = {k: payload.get(k) for k in ("cwd", "current_date", "timezone", "approval_policy",
                                                        "sandbox_policy", "model", "personality")}
        elif row.get("type") == "response_item" and payload.get("type") == "message":
            if payload.get("role") == "assistant":
                break
            opening.append({"role": payload.get("role"),
                            "text": "\n".join(c.get("text", "") for c in payload.get("content") or [])})
        elif row.get("type") == "response_item" and payload.get("type") in ("function_call", "custom_tool_call",
                                                                            "reasoning", "local_shell_call"):
            break
    return {"base_instructions": base, "opening": opening, "turn_context": turn_context}


# ---------------------------------------------------------------- the process


def run_process(cmd: list[str], env: dict, cwd: Path, timeout_s: int, stdout_path: Path, stderr_path: Path) -> dict:
    """Run the harness in its own process group; kill the group at the limit."""
    started = time.time()
    with open(stdout_path, "wb") as out, open(stderr_path, "wb") as err:
        proc = subprocess.Popen(cmd, cwd=cwd, env=env, stdout=out, stderr=err, stdin=subprocess.DEVNULL,
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


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(errors="replace").splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


EMAIL_LINE = re.compile(r"(The user's email address is )(\S+@\S+?)(\. Use it)")


def redact_account_email(folder: Path) -> int:
    """Claude Code tells the model the login's email address; the evidence keeps the sentence without the address."""
    found, changed = set(), 0
    files = [p for p in folder.rglob("*") if p.is_file() and p.suffix in (".json", ".jsonl", ".txt")]
    for path in files:
        found.update(m.group(2) for m in EMAIL_LINE.finditer(path.read_text(errors="replace")))
    for path in files:
        text = path.read_text(errors="replace")
        new = EMAIL_LINE.sub(r"\1[account email]\3", text)
        for address in found:
            new = new.replace(address, "[account email]")
        if new != text:
            path.write_text(new)
            changed += 1
    return changed


def leaks(text: str, case_id: str) -> list[str]:
    body = text.lower()
    scenario = re.sub(r"^(at|fp|p|uc|u|h)-", "", case_id.lower())
    m = re.match(r"((?:[a-z]+\d?-)?[a-z]{3}-\d+)", scenario)
    tokens = list(LEAK_TOKENS) + [case_id.lower()] + ([m.group(1)] if m else [])
    return sorted({t for t in tokens if t in body})


# ---------------------------------------------------------------- one attempt


def run_attempt(case: dict, attempt: Path, *, harness: str, backend: str, database_url: str, backend_url: str,
                model: str | None = None, effort: str = "medium", timeout_s: int = TIMEOUT_SECONDS,
                keep_state: bool = False) -> dict:
    from agent_diff import AgentDiff
    domain = case["domain"]
    summary = {"case_id": case["case_id"], "harness": harness, "backend": backend, "started_at": now_iso()}
    environment_dir, solver_dir = attempt / "environment", attempt / "solver"
    raw_dir = solver_dir / harness
    raw_dir.mkdir(parents=True, exist_ok=True)
    engine = engine_for(database_url)
    client = AgentDiff(base_url=backend_url)
    env = prepared = None
    root = STATE_ROOTS[harness] / uuid.uuid4().hex[:16]
    try:
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
        Path(prepared["initial_state_path"]).unlink()
        run = client.start_run(envId=env.environmentId)

        root.mkdir(parents=True)
        curl_shim(root / "bin" / "curl", backend_url, env.environmentId)
        case, dates_info = oc.for_run(case, attempt)   # discontinued clock shift: the test's dates are rendered
        fake_now = None
        proc_env, clock = base_env(root, domain, fake_now)
        if dates_info:
            proc_env["TZ"] = dates_info["zone"]
        spec = claude_setup(root, backend, model, effort) if harness == "claude" else codex_setup(root, backend, model, effort)
        if fake_now is not None and harness == "claude":
            clock.update(shift_clock(proc_env, fake_now, shared_login=backend == "plan"))
        elif fake_now is not None:
            clock.update(method="none: Codex is a static binary, its clock cannot be shifted")
        proc_env = claude_env(proc_env, spec, backend) if harness == "claude" else codex_env(proc_env, spec, backend)
        prompt = oc.PREFIX[domain] + case["prompt"]
        cmd = [prompt if part is None else part for part in spec["cmd"]]
        version = subprocess.run([cmd[0], "--version"], capture_output=True, text=True,
                                 env={k: v for k, v in proc_env.items() if k != "LD_PRELOAD"}).stdout.strip()
        write(solver_dir / "config.json", {
            "harness": harness, "version": version, "backend": backend, "model": spec["model"], "effort": effort,
            "command": [("<prompt>" if part == prompt else part) for part in cmd], "prompt": prompt,
            "prompt_prefix": oc.PREFIX[domain], "timeout_seconds": timeout_s, "clock": clock,
            "env_keys": sorted(proc_env),
            "secrets": "self-host key from ~/qwen-selfhost/secrets/api_key" if backend == "selfhost" else
            ("the Claude login of this machine (shared, not copied)" if harness == "claude" else
             "a copy of ~/.codex/auth.json in the run's CODEX_HOME, deleted after the run"),
            "state_dir": str(root), "work_dir": str(spec["work"]), "skills_sha256": spec["skills_sha256"],
            "curl_shim_sha256": hashlib.sha256((root / "bin" / "curl").read_bytes()).hexdigest(),
            "environment_id": env.environmentId, "run_id": run.runId, "case_sha256": case.get("case_sha256")})
        summary.update(status="solver_running", environment_id=env.environmentId)
        write(attempt / "execution_summary.json", summary)

        proc = run_process(cmd, proc_env, spec["work"], timeout_s, raw_dir / "stdout.jsonl", raw_dir / "stderr.txt")
        after = oc.export(domain, engine, schema)
        write(environment_dir / "final_state.json", after)
        try:
            write(environment_dir / "diff_run.json", client.diff_run(runId=run.runId).model_dump(mode="json"))
        except Exception as exc:
            summary["diff_error"] = f"{type(exc).__name__}: {exc}"
        client.evaluate_run(runId=run.runId, expectedOutput={"assertions": []})

        events = read_jsonl(raw_dir / "stdout.jsonl")
        flags = {}
        if harness == "claude":
            steps, usage = claude_steps(events)
            result = next((e for e in events if e.get("type") == "result"), {})
            init = next((e for e in events if e.get("type") == "system" and e.get("subtype") == "init"), {})
            final = result.get("result") or ""
            flags["init"] = {k: init.get(k) for k in ("model", "permissionMode", "tools", "mcp_servers", "skills",
                                                     "agents", "plugins", "apiKeySource", "claude_code_version")}
            session = claude_session_file(spec, init.get("session_id"))
            context = {}
            if session is not None:
                rows = read_jsonl(session)
                context = claude_context(rows)
                target = raw_dir / "session"
                shutil.move(str(session.parent), str(target))  # this run's own project folder
            write(raw_dir / "context.json", context)
            opening = json.dumps(context)
            error = bool(result.get("is_error")) and bool(re.search(r"API Error|Failed to authenticate", final))
            termination = "timeout" if proc["killed"] else ("error" if error or not result else "done")
        else:
            steps, usage = codex_steps(events)
            rollout, rows = codex_rollout(spec["home"])
            if rollout is not None:
                shutil.copyfile(rollout, raw_dir / "rollout.jsonl")
            usage["rollout"] = codex_rollout_usage(rows)
            context = codex_context(rows)
            write(raw_dir / "context.json", context)
            opening = json.dumps(context)
            last = Path(root / "last_message.txt")
            final = last.read_text() if last.exists() else ""
            failed = [e for e in events if e.get("type") in ("turn.failed", "error")]
            if failed:
                flags["errors"] = [json.dumps(e)[:500] for e in failed[:5]]
            termination = "timeout" if proc["killed"] else ("error" if failed and not final else "done")
            if backend == "plan":
                flags["auth_unchanged"] = hashlib.sha256(CODEX_AUTH.read_bytes()).hexdigest() == spec["auth_sha256"]
            if fake_now is not None:  # Codex tells the model the real date; record the mismatch with the test's clock
                shown = (context.get("turn_context") or {}).get("current_date")
                flags["context_date"] = {"shown": shown, "test_clock": fake_now.date().isoformat(),
                                         "mismatch": shown != fake_now.date().isoformat()}
        (solver_dir / "final_response.md").write_text(final + "\n")
        record = {"test_id": case["case_id"], "question": prompt, "harness": harness, "termination": termination,
                  "final": final, "turns": [{"label": "turn1", "message": prompt, "text": final,
                                             "termination": termination, **proc}],
                  "steps": oc.judge_steps(steps), "followup_steps": []}
        write(solver_dir / f"{case['case_id']}.json", record)
        flags["tool_calls"] = len([s for s in steps if s.get("tool")])
        flags["prompt_leaks"] = leaks(opening, case["case_id"])
        flags["account_email_in_context"] = bool(EMAIL_LINE.search(opening))
        if flags["account_email_in_context"]:
            flags["account_email_redacted_files"] = redact_account_email(raw_dir)
        if fake_now is not None:
            flags["clock_suspects"] = oc.clock_scan(steps, [final], real_year=domain == "calendar")
        summary.update(status="completed" if termination != "error" else "infrastructure_error",
                       termination=termination, duration_s=proc["duration_s"], flags=flags, usage=usage)
        if flags["prompt_leaks"]:
            summary.update(status="infrastructure_error", error=f"prompt leak: {flags['prompt_leaks']}")
    except Exception as exc:
        summary.update(status="infrastructure_error", error=f"{type(exc).__name__}: {exc}")
    finally:
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
        auth_copy = root / "home" / "auth.json"
        if auth_copy.exists():
            auth_copy.unlink()
        if root.exists() and not keep_state:
            shutil.rmtree(root, ignore_errors=True)
        summary["finished_at"] = now_iso()
        write(attempt / "execution_summary.json", summary)
    return summary
