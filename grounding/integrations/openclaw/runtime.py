"""Run AgentDiff cases through the real OpenClaw agent `agentdiff-qwen`, one isolated run per attempt.

Each attempt:
1. installs the case seed as a UUID-named template (custom_runtime for Box/Calendar/Linear,
   the Slack runtime for Slack) and records the probed initial state;
2. opens a fresh AgentDiff environment and starts a run;
3. builds a fresh OpenClaw state directory containing only agentdiff-qwen: its configuration
   from ~/.openclaw/openclaw.json, a copy of its workspace (bootstrap files and the four API
   skills), no channels, no ~/.openclaw/.env, empty memory and sessions;
4. sends the prefixed case prompt with `openclaw agent --local --json` (turn 1), then snapshots
   the state; if turn 1 changed nothing and ended with a question, sends "Yes, go ahead."
   (turn 2) and snapshots again;
5. records the native diff, OpenClaw's session transcript and trajectory, every model request
   (through the local Purdue proxy), effective settings and usage, then deletes the environment
   and the template.

Evidence layout matches the toy-harness runs, so the pilot analysis reads it unchanged:
environment/final_state.json is the state after turn 1 (graded); environment/followup_state.json
is the state after the follow-up; solver/final_response.md is the turn-1 reply.
"""
from __future__ import annotations

import copy
import gzip
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import threading
import time
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

from grounding.integrations.agentdiff import custom_runtime, runtime
from grounding.integrations.agentdiff import smoke_runtime as smoke
from grounding.integrations.agentdiff.runtime import ddl_lock, digest, engine_for, environment_schema, write
from grounding.integrations.openclaw.patterns import QUESTION
from grounding.integrations.openclaw.purdue_proxy import DEFAULT_PORT, SELFHOST_PORT, routes_dir

AGENT_ID = "agentdiff-qwen"
REAL_STATE = Path.home() / ".openclaw"
STATE_ROOT = Path.home() / ".openclaw-runs" / "agentdiff-openclaw"
HERE = Path(__file__).resolve().parent
SHIM_DIR = HERE / "bin"
FAKE_CLOCK = HERE / "fake_clock.cjs"
OPENCLAW_BIN = shutil.which("openclaw") or str(Path.home() / ".npm-global/bin/openclaw")
PREFIX = {"slack": "In Slack: ", "box": "In Box: ", "calendar": "In Google Calendar: ", "linear": "In Linear: "}
FOLLOW_UP = "Yes, go ahead."
# Where the agent's model requests go. "purdue" keeps agentdiff-qwen's configured model and provider entry. "selfhost"
# (since 2026-09-27) writes a provider for the self-hosted Qwen into each attempt's own configuration, from the purdue
# entry, with the served model's real limits (vLLM's max-model-len 131072; output capped at 8192 as on Purdue). The
# user's ~/.openclaw/openclaw.json is not changed. Both go through a local proxy, which holds the real key.
# The self-host generates about 24 tokens a second per conversation (fewer under load), so a full 8,192-token output
# takes over 300 s, the purdue entry's cap on one provider request. Its requests may take the whole turn instead
# (TIMEOUT_SECONDS), so the turn's clock is the only one that binds.
BACKENDS = {
    "purdue": {"provider": "purdue", "port": DEFAULT_PORT, "model": None, "provider_settings": {}},
    "selfhost": {"provider": "selfhost", "port": SELFHOST_PORT,
                 "model": {"id": "qwen3.8-27b", "name": "Qwen 3.8 27B (self-hosted)", "contextWindow": 131072,
                           "maxTokens": 8192},
                 "provider_settings": {"timeoutSeconds": 600}},
}
TIMEOUT_SECONDS = 600  # OpenClaw's default agent timeout
# The toy harness told the Calendar agent "Current Date/Time: Sunday, June 17, 2018 at 00:01 (midnight),
# timezone America/Los_Angeles"; OpenClaw gets the same moment from its (shifted) clock instead.
CALENDAR_NOW = datetime(2018, 6, 17, 7, 1, tzinfo=timezone.utc)
CALENDAR_TZ = "America/Los_Angeles"
TIME_COMMANDS = re.compile(r"(^|[\s;&|(`$])(date|timedatectl|hwclock|cal|ncal|uptime|stat)(\s|$)|datetime|time\.time|"
                           r"Date\.now|new Date|ls\s+-[a-zA-Z]*l|curl\s[^|]*\s-(i|I|v)\b|--include|--verbose", re.I)
REAL_YEAR = re.compile(r"\b202[3-9]\b")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------- isolated OpenClaw state


def real_config() -> dict:
    return json.loads((REAL_STATE / "openclaw.json").read_text())


# Optional workspace variants for harness-factor experiments (the default run uses the workspace unchanged).
# "no-ask" removes every instruction to ask before acting, per workspace file (the action-bias lines stay).
ASK_LINES = {"AGENTS.md": ("- Don't run destructive commands without asking.", "- When in doubt, ask.",
                           "**Ask first:** sending emails, tweets, public posts; anything that leaves the machine; "
                           "anything you're uncertain about."),
             "SOUL.md": ("- When in doubt, ask before acting externally.",)}
VARIANTS = {"no-ask": ASK_LINES, "verify": {}}
# "verify" adds one rule to the Red Lines list of AGENTS.md (a workspace instruction, as a user could write).
VERIFY_RULE = ("- Before changing anything, check every condition in the request against the record you found. "
               "If any condition does not hold, do not make the change; tell the user what does not match.\n")


def apply_variant(workspace: Path, variant: str | None) -> None:
    if not variant:
        return
    if variant == "verify":
        path = workspace / "AGENTS.md"
        text = path.read_text()
        anchor = "- When in doubt, ask.\n"
        if anchor not in text:
            raise ValueError("variant verify: Red Lines anchor not found in AGENTS.md")
        path.write_text(text.replace(anchor, anchor + VERIFY_RULE, 1))
        return
    for name, drop in VARIANTS[variant].items():
        path = workspace / name
        lines = path.read_text().splitlines(keepends=True)
        removed = [line for line in lines if line.strip() in drop]
        if len(removed) != len(drop):
            raise ValueError(f"variant {variant}: expected lines not all found in {name}")
        path.write_text("".join(line for line in lines if line.strip() not in drop))


def build_state_dir(state: Path, route: str, domain: str, variant: str | None = None,
                    backend: str = "purdue") -> dict:
    """Fresh state directory with only agentdiff-qwen; returns the written configuration."""
    real = real_config()
    spec = BACKENDS[backend]
    agent = copy.deepcopy(next(a for a in real["agents"]["list"] if a["id"] == AGENT_ID))
    workspace = state / f"workspace-{AGENT_ID}"
    agent_dir = state / "agents" / AGENT_ID / "agent"
    shutil.copytree(Path(agent["workspace"]), workspace, ignore=shutil.ignore_patterns(".git", "memory", "sessions"))
    apply_variant(workspace, variant)
    agent_dir.mkdir(parents=True)
    (state / "agents" / AGENT_ID / "sessions").mkdir(parents=True)
    agent.update(workspace=str(workspace), agentDir=str(agent_dir))
    defaults = {k: v for k, v in real["agents"].get("defaults", {}).items() if k not in ("model", "models", "workspace")}
    defaults["workspace"] = str(state / "workspace")
    if domain == "calendar":
        defaults["userTimezone"] = CALENDAR_TZ
    provider = copy.deepcopy(real["models"]["providers"]["purdue"])
    if spec["model"]:
        model = copy.deepcopy(provider["models"][0])
        model.update(spec["model"])
        provider["models"] = [model]
        agent["model"] = {"primary": f"{spec['provider']}/{model['id']}", "fallbacks": []}
    provider.update(spec["provider_settings"])
    provider["baseUrl"] = f"http://127.0.0.1:{spec['port']}/run/{route}/v1"
    provider["apiKey"] = "local-proxy"  # the proxy sends the real key; nothing secret is written here
    tools = copy.deepcopy(real.get("tools", {}))
    tools.setdefault("exec", {})["pathPrepend"] = [str(SHIM_DIR)]
    config = {
        "agents": {"defaults": defaults, "list": [agent]},
        "models": {"providers": {spec["provider"]: provider}},
        "tools": tools,
        "skills": copy.deepcopy(real.get("skills", {})),
        "plugins": {"entries": {"memory-core": copy.deepcopy(
            real.get("plugins", {}).get("entries", {}).get("memory-core", {"config": {}}))}},
        "commands": copy.deepcopy(real.get("commands", {})),
    }
    path = state / "openclaw.json"
    path.write_text(json.dumps(config, indent=2))
    path.chmod(0o600)
    return config


def register_route(token: str, log_dir: Path) -> Path:
    routes_dir().mkdir(parents=True, exist_ok=True)
    path = routes_dir() / f"{token}.json"
    path.write_text(json.dumps({"log_dir": str(log_dir)}))
    return path


def process_env(state: Path, env_id: str, backend_url: str, domain: str, fake_now: datetime | None) -> dict:
    node_bin = str(Path(os.path.realpath(shutil.which("node") or "/usr/bin/node")).parent)
    env = {"HOME": str(Path.home()), "LANG": "C.UTF-8", "USER": os.getenv("USER", "yusf"),
           "PATH": os.pathsep.join([node_bin, str(Path.home() / ".npm-global/bin"), "/usr/local/bin", "/usr/bin", "/bin"]),
           "OPENCLAW_STATE_DIR": str(state), "AGENTDIFF_BACKEND_URL": backend_url, "AGENTDIFF_ENV_ID": env_id}
    if domain == "calendar" and fake_now is not None:
        env.update(TZ=CALENDAR_TZ, NODE_OPTIONS=f"--require {FAKE_CLOCK}",
                   AGENTDIFF_FAKE_NOW=fake_now.isoformat().replace("+00:00", "Z"))
    return env


# ---------------------------------------------------------------- one OpenClaw turn


def run_turn(state: Path, env: dict, message: str, timeout_s: int, out: Path, label: str) -> dict:
    """Send one message; return the parsed --json envelope and how the process ended."""
    cmd = [OPENCLAW_BIN, "agent", "--agent", AGENT_ID, "--local", "--json", "--timeout", str(timeout_s),
           "--message", message]
    workspace = state / f"workspace-{AGENT_ID}"
    started = time.time()
    proc = subprocess.Popen(cmd, cwd=workspace, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            start_new_session=True)
    stdout = bytearray()
    stderr_path = out / f"openclaw_{label}.stderr.txt"
    envelope: dict | None = None
    parsed_at: float | None = None

    def drain_stderr():
        with open(stderr_path, "wb") as handle:
            for chunk in iter(lambda: proc.stderr.read1(65536), b""):
                handle.write(chunk)

    reader = threading.Thread(target=drain_stderr, daemon=True)
    reader.start()
    deadline = started + timeout_s + 120
    decoder = json.JSONDecoder()
    killed = None
    os.set_blocking(proc.stdout.fileno(), False)
    while True:
        chunk = None
        try:
            chunk = proc.stdout.read(65536)
        except BlockingIOError:
            pass
        if chunk:
            stdout += chunk
            if envelope is None:
                text = stdout.decode("utf-8", "replace")
                start = text.find("{")
                if start >= 0:
                    try:
                        envelope, _ = decoder.raw_decode(text[start:])
                        parsed_at = time.time()
                    except json.JSONDecodeError:
                        pass
        if proc.poll() is not None and not chunk:
            break
        # OpenClaw --local sometimes keeps a handle open after printing its reply (seen by SpecOps).
        if parsed_at and time.time() - parsed_at > 10:
            killed = "after_envelope"
            break
        if time.time() > deadline:
            killed = "hard_deadline"
            break
        if not chunk:
            time.sleep(0.2)
    if proc.poll() is None:
        try:
            os.killpg(proc.pid, signal.SIGTERM)
            proc.wait(timeout=15)
        except (ProcessLookupError, subprocess.TimeoutExpired):
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            proc.wait()
    reader.join(timeout=5)
    if envelope is not None:
        write(out / f"openclaw_{label}.json", envelope)
    # Keep raw stdout only when it holds more than the parsed envelope (or no envelope at all).
    text = stdout.decode("utf-8", "replace")
    start = text.find("{")
    extra = True
    if envelope is not None and start >= 0:
        try:
            _, end = decoder.raw_decode(text[start:])
            extra = bool(text[:start].strip() or text[start + end:].strip())
        except json.JSONDecodeError:
            extra = True
    if extra:
        (out / f"openclaw_{label}.stdout.txt").write_bytes(bytes(stdout))
    texts = [p.get("text") or "" for p in (envelope or {}).get("payloads", [])]
    meta = (envelope or {}).get("meta", {})
    stderr_text = stderr_path.read_text(errors="replace") if stderr_path.exists() else ""
    if envelope is None:
        termination = "timeout" if killed == "hard_deadline" else "error"
    elif meta.get("aborted") or re.search(r"timed out|timeout", json.dumps(meta.get("error") or ""), re.I):
        termination = "timeout" if re.search(r"timed out|timeout", stderr_text[-4000:] + json.dumps(meta), re.I) else "aborted"
    else:
        termination = "done"
    return {"label": label, "message": message, "text": "\n\n".join(t for t in texts if t).strip(),
            "termination": termination, "returncode": proc.returncode, "killed": killed,
            "duration_s": round(time.time() - started, 1), "meta_error": meta.get("error"),
            "stop_reason": (meta.get("agentMeta") or {}).get("stopReason") or meta.get("stopReason")}


# ---------------------------------------------------------------- transcript -> steps


def session_rows(state: Path) -> tuple[list[dict], list[Path]]:
    sessions = sorted((state / "agents" / AGENT_ID / "sessions").glob("*.jsonl"))
    main = [p for p in sessions if not p.name.endswith(".trajectory.jsonl")]
    rows = []
    for path in main:
        rows += [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    return rows, sessions


def steps_from_session(rows: list[dict]) -> list[dict]:
    """One step per tool call, with its result; assistant text and thinking kept alongside."""
    steps, by_id = [], {}
    user_turn = 0
    for row in rows:
        if row.get("type") != "message":
            continue
        message = row["message"]
        role = message.get("role")
        content = message.get("content")
        blocks = content if isinstance(content, list) else [{"type": "text", "text": content or ""}]
        if role == "user":
            user_turn += 1
        elif role == "assistant":
            thinking = "\n".join(b.get("thinking", "") for b in blocks if b.get("type") == "thinking").strip()
            text = "\n".join(b.get("text", "") for b in blocks if b.get("type") == "text").strip()
            calls = [b for b in blocks if b.get("type") == "toolCall"]
            if not calls:
                steps.append({"turn": user_turn, "tool": None, "text": text, "thinking": thinking,
                              "usage": message.get("usage")})
            for i, call in enumerate(calls):
                args = call.get("arguments") or {}
                action = args.get("command") if call.get("name") == "exec" else f"{call.get('name')} {json.dumps(args)}"
                step = {"turn": user_turn, "tool": call.get("name"), "arguments": args, "action": action,
                        "text": text if i == 0 else "", "thinking": thinking if i == 0 else "",
                        "usage": message.get("usage") if i == 0 else None}
                steps.append(step)
                by_id[call.get("id")] = step
        elif role == "toolResult":
            result = "\n".join(b.get("text", "") for b in blocks if b.get("type") == "text")
            step = by_id.get(message.get("toolCallId"))
            if step is not None:
                step["observation"] = {"stdout": result, "is_error": bool(message.get("isError"))}
        elif row.get("type") == "compaction" or role == "compactionSummary":
            steps.append({"turn": user_turn, "tool": None, "compaction": True})
    return steps


def judge_steps(steps: list[dict]) -> list[dict]:
    """Steps in the toy harness's record format, which the judge's bundle and the scoring read: `turn` numbers the
    step, `response.content` carries the visible reasoning (the model's thinking, then its text, as the toy's
    ReAct text did), `observation` is {status, stdout}. OpenClaw's own fields stay alongside; `user_turn` is the
    conversation turn. The input steps are not changed."""
    out = []
    for number, step in enumerate(steps, 1):
        new = dict(step, user_turn=step.get("turn"), turn=number)
        thinking, text = step.get("thinking") or "", step.get("text") or ""
        visible = (f"<thinking>\n{thinking}\n</thinking>\n" if thinking else "") + text
        new["response"] = {"content": [{"type": "text", "text": visible}]}
        if step.get("compaction"):
            new["action"], new["observation"] = "", {"status": "success", "stdout": "(OpenClaw compacted the conversation)"}
        elif isinstance(step.get("observation"), dict):
            obs = step["observation"]
            new["observation"] = {"status": "error" if obs.get("is_error") else "success", "stdout": obs.get("stdout", "")}
        out.append(new)
    return out


def compactions(rows: list[dict]) -> int:
    return sum(1 for r in rows if r.get("type") == "compaction" or "compaction" in str(r.get("customType", "")))


def clock_scan(steps: list[dict], replies: list[str]) -> list[dict]:
    """Places where a Calendar run could see the real (2026) clock: time commands and real-year text."""
    found = []
    for i, step in enumerate(steps):
        action = step.get("action") or ""
        if step.get("tool") == "exec" and TIME_COMMANDS.search(action):
            found.append({"step": i, "kind": "time_command", "action": action[:300]})
        observed = (step.get("observation") or {}).get("stdout", "")
        if REAL_YEAR.search(observed):
            found.append({"step": i, "kind": "real_year_in_tool_output",
                          "sample": observed[max(0, REAL_YEAR.search(observed).start() - 80):][:200]})
        said = (step.get("text") or "") + "\n" + (step.get("thinking") or "")
        if REAL_YEAR.search(said):
            found.append({"step": i, "kind": "real_year_in_model_text",
                          "sample": said[max(0, REAL_YEAR.search(said).start() - 80):][:200]})
    for reply in replies:
        if REAL_YEAR.search(reply or ""):
            found.append({"step": None, "kind": "real_year_in_reply"})
    return found


def bundle(directory: Path, archive: Path) -> None:
    """Replace `directory` by one tar.xz of its (decompressed) files: requests repeat the same long prompt,
    so xz over the whole attempt is ~15x smaller than per-file gzip."""
    import io
    import tarfile
    if not directory.exists():
        return
    with tarfile.open(archive, "w:xz", preset=9) as tar:
        for path in sorted(p for p in directory.rglob("*") if p.is_file() and p.name != ".counter"):
            data = path.read_bytes()
            name = str(path.relative_to(directory.parent))
            if path.suffix == ".gz":
                data, name = gzip.decompress(data), name[:-3]
            info = tarfile.TarInfo(name)
            info.size, info.mtime = len(data), int(path.stat().st_mtime)
            tar.addfile(info, io.BytesIO(data))
    shutil.rmtree(directory)


def cut_streams(log_dir: Path) -> list[str]:
    """Model requests whose stream the provider cut (HTTP 200 but no finish reason and no terminator)."""
    cut = []
    for meta_path in sorted(log_dir.glob("*.meta.json")):
        meta = json.loads(meta_path.read_text())
        if meta.get("final_status") == 200 and not meta.get("done_seen") and not meta.get("finish_reason"):
            cut.append(meta_path.name.split(".")[0])
    return cut


def proxy_usage(log_dir: Path) -> dict:
    totals = {"requests": 0, "attempts": 0, "input_tokens": 0, "output_tokens": 0, "reasoning_tokens": 0,
              "requests_without_usage": 0, "non_200": 0, "limiter_wait_s": 0.0}
    for meta_path in sorted(log_dir.glob("*.meta.json")):
        meta = json.loads(meta_path.read_text())
        totals["requests"] += 1
        totals["attempts"] += len(meta.get("attempts", []))
        totals["limiter_wait_s"] += sum(a.get("limiter_wait_s", 0) for a in meta.get("attempts", []))
        if meta.get("final_status") != 200:
            totals["non_200"] += 1
        usage = meta.get("usage")
        if not usage:
            totals["requests_without_usage"] += 1
            continue
        totals["input_tokens"] += usage.get("prompt_tokens", 0)
        totals["output_tokens"] += usage.get("completion_tokens", 0)
        totals["reasoning_tokens"] += (usage.get("completion_tokens_details") or {}).get("reasoning_tokens", 0) or 0
    totals["limiter_wait_s"] = round(totals["limiter_wait_s"], 1)
    return totals


# ---------------------------------------------------------------- AgentDiff environment


def solver_case(case: dict) -> dict:
    keep = ("case_id", "prompt", "acting_user_id", "seed", "cards", "task_spec", "private")
    return {k: case[k] for k in keep if k in case}


def export(domain: str, engine, schema: str) -> dict:
    if domain == "slack":
        return runtime.export_state(engine, schema)
    return smoke.export_state(engine, schema, smoke.load_seed_module(domain).Base.metadata)


def semantic_digest(domain: str, state: dict) -> str:
    volatile = smoke.VOLATILE_TABLES.get(domain, set())
    return digest({k: v for k, v in state.items() if k not in volatile})


def prepare(case: dict, out: Path, database_url: str, backend_url: str) -> dict:
    if case["domain"] == "slack":
        prepared = runtime.prepare(solver_case(case), out, database_url, backend_url)
        return {**prepared, "service": "slack"}
    return custom_runtime.prepare_custom(case, out, database_url, backend_url)


def cleanup_template(case: dict, prepared: dict, database_url: str) -> None:
    if case["domain"] == "slack":
        runtime.cleanup(prepared, database_url)
    else:
        smoke.cleanup_isolated_template({**prepared, "service": case["domain"]}, database_url)


# ---------------------------------------------------------------- one attempt


def run_attempt(case: dict, attempt: Path, *, database_url: str, backend_url: str,
                timeout_s: int = TIMEOUT_SECONDS, followup: bool = True, keep_state: bool = False,
                summary: dict | None = None, variant: str | None = None, backend: str = "purdue",
                layout: str = "transfer") -> dict:
    """Run one case through OpenClaw; write evidence under `attempt`; return the execution summary.

    `layout="judge"` (roadmap step 6) writes what the judge and scoring read: OpenClaw's raw turn files go under
    solver/openclaw/ (the readers take the first solver/*.json as the record), and the record's steps take the toy
    harness's format (`judge_steps`). The default keeps openclaw_transfer_01's layout."""
    from agent_diff import AgentDiff
    domain = case["domain"]
    summary = summary if summary is not None else {}
    environment_dir, solver_dir = attempt / "environment", attempt / "solver"
    solver_dir.mkdir(parents=True, exist_ok=True)
    (solver_dir / "requests").mkdir(exist_ok=True)
    raw_dir = solver_dir / "openclaw" if layout == "judge" else solver_dir
    raw_dir.mkdir(exist_ok=True)
    engine = engine_for(database_url)
    client = AgentDiff(base_url=backend_url)
    env = run = prepared = None
    route_file = None
    state = STATE_ROOT / attempt.parent.parent.name / attempt.parent.name / f"{attempt.name}-{uuid.uuid4().hex[:8]}"
    try:
        prepared = prepare(case, environment_dir / "preflight", database_url, backend_url)
        with ddl_lock():
            env = client.init_env(templateService=domain, templateName=prepared["template_name"],
                                  impersonateUserId=case["acting_user_id"])
        schema = environment_schema(engine, env.environmentId, prepared["template_id"])
        initial = export(domain, engine, schema)
        installed = json.loads(Path(prepared["initial_state_path"]).read_text())
        if semantic_digest(domain, initial) != semantic_digest(domain, installed):
            raise ValueError("Fresh environment differs from the prepared initial state")
        write(environment_dir / "initial_state.json", initial)
        Path(prepared["initial_state_path"]).unlink()  # identical to initial_state.json; prepared.json keeps its sha256
        summary.setdefault("compacted", []).append("environment/preflight/initial_state.json")
        run = client.start_run(envId=env.environmentId)
        token = uuid.uuid4().hex[:24]
        route_file = register_route(token, solver_dir / "requests")
        state.mkdir(parents=True)
        config = build_state_dir(state, token, domain, variant, backend)
        fake_now = CALENDAR_NOW if domain == "calendar" else None
        env_vars = process_env(state, env.environmentId, backend_url, domain, fake_now)
        prompt = PREFIX[domain] + case["prompt"]
        write(solver_dir / "config.json", {
            "harness": "openclaw", "openclaw_version": subprocess.run([OPENCLAW_BIN, "--version"], capture_output=True,
                                                                       text=True, env=env_vars).stdout.strip(),
            "agent_id": AGENT_ID, "model": config["agents"]["list"][0]["model"],
            "backend": backend, "layout": layout,
            "provider": {k: v for k, v in config["models"]["providers"][BACKENDS[backend]["provider"]].items()
                         if k != "apiKey"},
            "agent": config["agents"]["list"][0], "agents_defaults": config["agents"]["defaults"],
            "tools": config["tools"], "prompt": prompt, "prompt_prefix": PREFIX[domain],
            "follow_up": {"enabled": followup, "message": FOLLOW_UP,
                          "rule": "sent when turn 1 changed no state and its reply asks the user a question"},
            "timeout_seconds_per_turn": timeout_s, "workspace_variant": variant,
            "fake_clock": {"start": fake_now.isoformat(), "timezone": CALENDAR_TZ} if fake_now else None,
            "workspace_files": sorted(p.name for p in (state / f"workspace-{AGENT_ID}").iterdir()),
            "skills_sha256": {str(p.relative_to(state / f"workspace-{AGENT_ID}" / "skills")):
                              hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in sorted((state / f"workspace-{AGENT_ID}" / "skills").rglob("*.md"))},
            "curl_shim_sha256": hashlib.sha256((SHIM_DIR / "curl").read_bytes()).hexdigest(),
            "environment_id": env.environmentId, "run_id": run.runId, "state_dir": str(state),
            "case_sha256": case.get("case_sha256")})
        summary.update(status="solver_running", environment_id=env.environmentId)
        write(attempt / "execution_summary.json", summary)

        turn1 = run_turn(state, env_vars, prompt, timeout_s, raw_dir, "turn1")
        after1 = export(domain, engine, schema)
        write(environment_dir / "final_state.json", after1)
        (solver_dir / "final_response.md").write_text(turn1["text"] + "\n")
        turns = [turn1]
        changed1 = semantic_digest(domain, after1) != semantic_digest(domain, initial)
        asks = bool(turn1["text"]) and bool(QUESTION.search(turn1["text"]))
        followup_info = {"sent": False, "turn1_changed_state": changed1, "turn1_asks": asks}
        if followup and turn1["termination"] == "done" and not changed1 and asks:
            if fake_now is not None:
                env_vars = process_env(state, env.environmentId, backend_url, domain,
                                       fake_now + timedelta(seconds=turn1["duration_s"]))
            turn2 = run_turn(state, env_vars, FOLLOW_UP, timeout_s, raw_dir, "turn2")
            write(environment_dir / "followup_state.json", export(domain, engine, schema))
            (solver_dir / "followup_response.md").write_text(turn2["text"] + "\n")
            turns.append(turn2)
            followup_info.update(sent=True, termination=turn2["termination"], duration_s=turn2["duration_s"])
        try:
            write(environment_dir / "diff_run.json", client.diff_run(runId=run.runId).model_dump(mode="json"))
        except Exception as exc:  # recorded, not fatal: states are the grading evidence
            summary["diff_error"] = f"{type(exc).__name__}: {exc}"
        client.evaluate_run(runId=run.runId, expectedOutput={"assertions": []})

        rows, _ = session_rows(state)
        shutil.copytree(state / "agents" / AGENT_ID / "sessions", solver_dir / "openclaw_sessions",
                        ignore=shutil.ignore_patterns("*.lock"))
        steps = steps_from_session(rows)
        record = {"test_id": case["case_id"], "question": prompt, "harness": "openclaw",
                  "termination": turn1["termination"], "final": turn1["text"], "turns": turns,
                  "steps": [s for s in steps if s.get("turn", 1) <= 1],
                  "followup_steps": [s for s in steps if s.get("turn", 1) > 1]}
        if layout == "judge":
            record["steps"] = judge_steps(record["steps"])
            record["followup_steps"] = judge_steps(record["followup_steps"])
        write(solver_dir / f"{case['case_id']}.json", record)
        flags = {"compactions": compactions(rows), "tool_calls_turn1": len([s for s in record["steps"] if s.get("tool")]),
                 "read_skill": sorted({Path(s["arguments"].get("path", "")).parent.name for s in steps
                                       if s.get("tool") == "read" and str(s.get("arguments", {}).get("path", "")).endswith("SKILL.md")})}
        if domain == "calendar":
            flags["clock_suspects"] = clock_scan(steps, [t["text"] for t in turns])
        summary.update(status="completed", termination=turn1["termination"], followup=followup_info, flags=flags,
                       turns=flags["tool_calls_turn1"], usage=proxy_usage(solver_dir / "requests"),
                       turn_durations_s=[t["duration_s"] for t in turns])
        # Infrastructure rules (same as runs/openclaw_transfer_01/infra.py, which applies them to earlier runs).
        requests = sorted((solver_dir / "requests").glob("*.meta.json"))
        cut = cut_streams(solver_dir / "requests")
        if cut:
            flags["cut_streams"] = cut
        waited = summary["usage"].get("limiter_wait_s", 0)
        if turn1["termination"] == "done" and cut and requests and (
                cut[-1] == requests[-1].name.split(".")[0] or flags["compactions"]):
            # R1: the reply was built from a truncated stream, or from the compaction OpenClaw ran to recover from one.
            summary.update(status="infrastructure_error", error=f"R1 provider hang: model request {cut[-1]} came back as a cut stream")
        elif turn1["termination"] == "timeout" and waited > 0.25 * timeout_s:
            # R2: our shared request budget, not the agent, ran the clock out.
            summary.update(status="infrastructure_error", error=f"R2 rate-limit timeout: the turn hit the {timeout_s} s "
                                                                f"limit after {waited:.0f} s waiting for the shared rate limiter")
    except Exception as exc:
        summary.update(status="infrastructure_error", error=f"{type(exc).__name__}: {exc}")
    finally:
        summary["usage"] = proxy_usage(solver_dir / "requests") if summary.get("status") != "completed" else summary.get("usage")
        if route_file and route_file.exists():
            route_file.unlink()
        for name in ("requests", "openclaw_sessions"):
            try:
                bundle(solver_dir / name, solver_dir / f"{name}.tar.xz")
            except Exception as exc:
                summary[f"bundle_{name}_error"] = f"{type(exc).__name__}: {exc}"
        if env is not None:
            try:
                with ddl_lock():
                    client.delete_env(envId=env.environmentId)
            except Exception as exc:
                summary["delete_env_error"] = f"{type(exc).__name__}: {exc}"
        if prepared is not None:
            try:
                cleanup_template(case, prepared, database_url)
            except Exception as exc:
                summary["cleanup_error"] = f"{type(exc).__name__}: {exc}"
        engine.dispose()
        if not keep_state and state.exists() and summary.get("status") == "completed":
            shutil.rmtree(state, ignore_errors=True)
    return summary
