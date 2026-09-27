"""Shared smoke-runner for Box/Calendar/Linear Qwen coverage (minimal scope).

Mirrors the proven Slack path:
- same PurdueClient (grounding/solver/slack/purdue_client.py),
- same shared cross-process limiter (acquired inside PurdueClient before
  every HTTP attempt, initial calls and retries alike),
- same first-<action>-per-turn episode loop as grounding/solver/slack/run.py,
- same env lifecycle: install isolated seed template, preflight, episode,
  snapshot/diff, cleanup.

Differences from Slack are isolated per-domain: prompt bytes (same notebook
template/formatter, domain SERVICE_CONFIG + domain docs), seed install
(backend seed scripts), and preflight probes. No model calls in prepare;
run_episode is the paid boundary.
"""
from __future__ import annotations

import argparse
import ast
import asyncio
from copy import deepcopy
from datetime import datetime, timezone
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from uuid import UUID, uuid4

from grounding.paths import REPO_ROOT as ROOT

for _path in (ROOT / "backend", ROOT / "sdk/agent-diff-python"):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from agent_diff import AgentDiff  # noqa: E402

from grounding.integrations.agentdiff.runtime import (  # noqa: E402
    ddl_lock,
    digest,
    engine_for,
    environment_schema,
    serialized_ddl,
    write,
)
from grounding.solver.slack.agent_clock import CEILING_SECONDS, DESCRIPTION as CLOCK_RULE, AgentClock  # noqa: E402
from grounding.solver.slack.purdue_client import PurdueClient  # noqa: E402

HERE = Path(__file__).resolve().parent
SLACK_SOLVER = ROOT / "grounding/solver/slack"
EXECUTOR_IMAGE = "agent-diff-slack-executor"
BRIDGE = SLACK_SOLVER / "sandbox_bridge.py"
CODE_EXECUTOR = ROOT / "sdk/agent-diff-python/agent_diff/code_executor.py"
NOTEBOOK = ROOT / "experiments/kdd 2026/agent-diff bench.ipynb"
DATASET = ROOT / "datasets/agent-diff-bench/all_numbered.jsonl"

# Same model/pricing contract as grounding/solver/slack/compare_purdue.py.
QWEN_MODEL = "qwen3.6:27b"
QWEN_MAX_OUTPUT_TOKENS = 16384
QWEN_RATES = {"input_tokens": 0.0, "output_tokens": 0.0,
              "cache_creation_input_tokens": 0.0, "cache_read_input_tokens": 0.0}
COST_SOURCE = ("Purdue GenAI Studio has no per-token charge to this account; "
               "tokens are provider-reported, cost is recorded as 0 (not an invoice)")
TURN_LIMIT = 40
EPISODE_TIMEOUT_SECONDS = 480  # the agent's own time; Purdue waiting is off it (agent_clock.py, since 2026-09-27)
EPISODE_CEILING_SECONDS = CEILING_SECONDS  # wall time, waiting included

# Advisory-lock keys (one per service) for first-use DDL serialization.
_ADVISORY_LOCKS = {"box": 726411931, "calendar": 726411932, "linear": 726411933}

# Bookkeeping tables a read probe is allowed to touch. Calendar's list
# endpoints mint a sync-token row on first read; that is backend-expected
# write-on-read, not semantic state. Excluded ONLY from the preflight
# stability comparison -- initial/final snapshots still record everything.
VOLATILE_TABLES = {"box": set(), "calendar": {"calendar_sync_tokens"}, "linear": set()}

_prompt_cache: dict[str, str] = {}


def official_prompt(service: str) -> str:
    """Build the domain prompt from the authors' notebook (same extraction).

    Same formatter (format_docs_markdown), same template constant
    (REACT_SYSTEM_PROMPT_WITH_API_DOCS), same SERVICE_CONFIG values as the
    notebook cell used by grounding/solver/slack/run.py -- only the service
    key and its docs file differ.
    """
    if service in _prompt_cache:
        return _prompt_cache[service]
    namespace: dict = {}
    template = config = None
    for cell in json.loads(NOTEBOOK.read_text())["cells"]:
        if cell["cell_type"] != "code":
            continue
        source = "".join(cell["source"])
        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name == "format_docs_markdown":
                exec(compile(ast.Module(body=[node], type_ignores=[]), str(NOTEBOOK), "exec"),
                     namespace)
            if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == "REACT_SYSTEM_PROMPT_WITH_API_DOCS"
                for target in node.targets
            ):
                template = ast.literal_eval(node.value)
            if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == "SERVICE_CONFIG"
                for target in node.targets
            ):
                config = ast.literal_eval(node.value)
    if template is None or "format_docs_markdown" not in namespace or config is None:
        raise RuntimeError("Official notebook prompt/formatter/service-config missing")
    if service not in config:
        raise ValueError(f"Unknown notebook service: {service}")
    docs_path = ROOT / f"examples/{service}/testsuites/{service}_docs/{service}_api_full_docs.json"
    docs = json.loads(docs_path.read_text())
    entry = config[service]
    prompt = template.format(
        service_name=entry["name"], base_url=entry["base_url"],
        service_description=entry["description"], extra_context=entry.get("extra_context", ""),
        api_docs=namespace["format_docs_markdown"](docs),
    )
    _prompt_cache[service] = prompt
    return prompt


def cost(tokens: dict) -> float:
    return sum(tokens.get(key, 0) * rate / 1_000_000 for key, rate in QWEN_RATES.items())


def save_purdue_request(llm: PurdueClient, messages, prompt: str, options: dict, path: Path) -> None:
    """Save the logical OpenAI-style request actually sent to Purdue."""
    body = {"model": llm.model_id,
            "messages": llm._openai_messages(messages, prompt),
            "max_tokens": min(options["max_tokens"], llm.max_output_tokens or options["max_tokens"]),
            "stream": False}
    request = deepcopy(body)
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as handle:
        json.dump(request, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def assistant_content(message):
    """Keep model content while removing response-only fields and empty text."""
    return [
        block.model_dump(mode="json", exclude={"parsed_output"}, exclude_none=True)
        for block in message.content
        if not (block.type == "text" and not block.text)
    ]


def sha_file(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_seed_module(service: str):
    """Import the backend seed script for a service (no main side effects)."""
    if service == "calendar" and not os.getenv("DATABASE_URL"):
        raise ValueError("DATABASE_URL must be set: src/services/calendar/database/db.py reads it at import time")
    path = ROOT / f"backend/utils/seed_{service}_template.py"
    spec = importlib.util.spec_from_file_location(f"seed_{service}_template_smoke", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def seed_path_for(service: str, seed_name: str) -> Path:
    return ROOT / f"backend/seeds/{service}/{seed_name}.json"


@serialized_ddl
def install_isolated_template(service: str, seed_name: str, engine):
    """Create a UUID-named template schema from a backend seed (no model calls).

    Mirrors runtime.install_template: fresh campaign-owned schema plus one
    TemplateEnvironment row. Seed loading reuses the backend seed script's
    own create_tables/insert_seed_data so inserts match benchmark semantics
    (box file contents, materialized paths, trigram indexes included).
    UUID is generated here, never taken from input.
    """
    from sqlalchemy import text

    seed_module = load_seed_module(service)
    seed_file = seed_path_for(service, seed_name)
    seed_data = json.loads(seed_file.read_text())
    schema = f"{service}_campaign_{uuid4().hex}"
    template_id = uuid4()
    from src.platform.db.schema import TemplateEnvironment
    with engine.begin() as conn:
        conn.execute(text(f"SELECT pg_advisory_xact_lock({_ADVISORY_LOCKS[service]})"))
        seed_module.create_schema(conn, schema)
        seed_module.create_tables(conn, schema)
        seed_module.insert_seed_data(conn, schema, seed_data)
        scoped = conn.execution_options(schema_translate_map={None: schema})
        scoped.execute(TemplateEnvironment.__table__.insert().values(
            id=template_id, service=service, name=schema, version="v1",
            visibility="public", kind="schema", location=schema,
            description=f"Isolated smoke-run {service} case (seed {seed_name})",
            table_order=list(seed_module.TABLE_ORDER),
        ))
    return {"template_name": schema, "template_id": str(template_id),
            "seed_name": seed_name, "table_order": list(seed_module.TABLE_ORDER)}


def _freeze(value):
    if isinstance(value, bytes):
        return {"__bytes_sha256__": hashlib.sha256(value).hexdigest(), "bytes": len(value)}
    if isinstance(value, dict):
        return {key: _freeze(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_freeze(item) for item in value]
    return value


def export_state(engine, schema: str, metadata) -> dict:
    """Export every service table ordered by primary key (bytes content-addressed)."""
    from sqlalchemy import select
    with engine.connect() as connection:
        conn = connection.execution_options(schema_translate_map={None: schema})
        result = {}
        for table in metadata.sorted_tables:
            query = select(table).order_by(*table.primary_key.columns)
            result[table.name] = [_freeze(dict(row)) for row in conn.execute(query).mappings()]
    return json.loads(json.dumps(result, default=_json_default))


def _json_default(value):
    from datetime import date as _date
    from datetime import datetime as _dt
    from enum import Enum as _Enum
    from uuid import UUID as _UUID
    if isinstance(value, _dt):
        return value.isoformat()
    if isinstance(value, _date):
        return value.isoformat()
    if isinstance(value, _Enum):
        return value.value
    if isinstance(value, _UUID):
        return str(value)
    raise TypeError(f"Not JSON serializable: {type(value).__name__}")


@serialized_ddl
def cleanup_isolated_template(prepared: dict, database_url: str | None = None) -> None:
    """Drop only the exact UUID-named template created by this runner."""
    from sqlalchemy import text, select
    engine = engine_for(database_url)
    from src.platform.db.schema import TemplateEnvironment, RunTimeEnvironment, EnvironmentPoolEntry
    service = prepared["service"]
    name = prepared["template_name"]
    if not re.fullmatch(service + r"_campaign_[0-9a-f]{32}", name):
        raise ValueError("Refusing cleanup outside smoke-run schema namespace")
    try:
        with engine.begin() as conn:
            table = TemplateEnvironment.__table__
            active = conn.execute(select(RunTimeEnvironment.id).where(
                RunTimeEnvironment.template_id == UUID(prepared["template_id"]),
                RunTimeEnvironment.status != "deleted")).first()
            if active:
                raise ValueError("Refusing template cleanup while a runtime environment remains active")
            existing = conn.execute(select(table.c.location).where(
                table.c.id == UUID(prepared["template_id"]))).scalar_one_or_none()
            if existing is not None and existing != name:
                raise ValueError("Template identity mismatch during cleanup")
            pool = EnvironmentPoolEntry.__table__
            entries = conn.execute(select(pool.c.schema_name).where(
                pool.c.template_id == UUID(prepared["template_id"]))).scalars().all()
            for clone in entries:
                if not re.fullmatch(r"state_[0-9a-f]{32}", clone):
                    raise ValueError("Unexpected smoke-run clone schema name")
                conn.execute(text(f'DROP SCHEMA IF EXISTS "{clone}" CASCADE'))
            conn.execute(pool.delete().where(pool.c.template_id == UUID(prepared["template_id"])))
            conn.execute(table.delete().where(table.c.id == UUID(prepared["template_id"])))
            conn.execute(text(f'DROP SCHEMA IF EXISTS "{name}" CASCADE'))
    finally:
        engine.dispose()


def load_bench_row(test_id: str) -> dict:
    for line in DATASET.read_text().splitlines():
        row = json.loads(line)
        if row["test_id"] == test_id:
            return row
    raise ValueError(f"Unknown bench test_id: {test_id}")


async def run_episode(service: str, row: dict, prompt: str, out: Path, *,
                      base_url: str, model: str = QWEN_MODEL,
                      max_output_tokens: int = QWEN_MAX_OUTPUT_TOKENS,
                      record_requests: bool = True,
                      pre_cleanup=None) -> dict:
    """Same 40-turn/480s episode loop as slack/run.py, on Purdue Qwen."""
    options = {"max_tokens": max_output_tokens}
    if options["max_tokens"] < 1:
        raise ValueError("max_output_tokens must be positive")
    client = AgentDiff(base_url=base_url)
    env = run = process = None
    record = {"test_id": row["test_id"], "test_name": row["test_name"],
              "row_number": row["#"], "question": row["question"], "steps": []}
    path = out / (row["test_id"] + ".json")
    llm = PurdueClient(model_id=model, timeout=EPISODE_TIMEOUT_SECONDS)
    clock = AgentClock(EPISODE_TIMEOUT_SECONDS, EPISODE_CEILING_SECONDS)
    llm.agent_clock = clock
    container = None
    try:
        info = json.loads(row["info"])
        env = await asyncio.to_thread(
            client.init_env, templateService=service,
            templateName=info["seed_template"],
            impersonateUserId=info["impersonate_user_id"])
        record["environment_id"] = env.environmentId
        container = f"ad-{service}10-" + env.environmentId
        process = await asyncio.create_subprocess_exec(
            "docker", "run", "--rm", "-i", "--name", container, "--network", "host",
            "-e", "EVAL_ENV_ID=" + env.environmentId,
            "-e", "EVAL_BASE_URL=" + base_url,
            "-v", str(CODE_EXECUTOR) + ":/opt/agent/code_executor.py:ro",
            "-v", str(BRIDGE) + ":/opt/agent/bridge.py:ro",
            EXECUTOR_IMAGE, "python", "-u", "/opt/agent/bridge.py",
            stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            limit=16 * 1024 * 1024,
        )
        run = await asyncio.to_thread(client.start_run, envId=env.environmentId)
        record["run_id"] = run.runId
        messages = [{"role": "user", "content": "Task: " + row["question"]}]
        started = time.monotonic()
        record["started_at"] = datetime.now(timezone.utc).isoformat()
        try:
            async with asyncio.timeout(EPISODE_TIMEOUT_SECONDS) as budget:
                clock.attach(budget)
                for turn in range(1, TURN_LIMIT + 1):
                    request_path = out / "requests" / row["test_id"] / f"turn-{turn:03d}.json.gz"
                    if record_requests:
                        save_purdue_request(llm, messages, prompt, options, request_path)
                    try:
                        response = await llm.create(messages, system=prompt, **options,
                                                    usage_label=row["test_id"])
                    except Exception as exc:
                        if record_requests:
                            write(request_path.with_name(f"turn-{turn:03d}.error.json"),
                                  {"error_type": type(exc).__name__, "error": str(exc),
                                   "usage": llm.usage.snapshot().to_dict()})
                        raise
                    text = response.text
                    step = {"turn": turn, "response": response.message.model_dump(mode="json"),
                            "usage": response.usage.to_dict()}
                    record["steps"].append(step)
                    record["usage"] = llm.usage.snapshot().to_dict()
                    write(path, record)
                    content = assistant_content(response.message)
                    if content:
                        messages.append({"role": "assistant", "content": content})
                    action = re.search(r"<action>(.*?)</action>", text, re.DOTALL)
                    done = re.search(r"<done>(.*?)</done>", text, re.DOTALL)
                    if action:
                        command = action.group(1).strip()
                        step["action"] = command
                        process.stdin.write((json.dumps({"command": command, "timeout": 30}) + "\n").encode())
                        await process.stdin.drain()
                        line = await process.stdout.readline()
                        if not line:
                            raise RuntimeError("Execution container exited: " + (await process.stderr.read()).decode())
                        observation = json.loads(line)
                        step["observation"] = observation
                        stdout, stderr = observation.get("stdout", ""), observation.get("stderr", "")
                        if observation.get("exit_code", 0) != 0:
                            obs = f"{stdout}\n[stderr]: {stderr}\n[exit_code]: {observation['exit_code']}".strip()
                        else:
                            obs = stdout.strip() if stdout else "(empty output)"
                        messages.append({"role": "user", "content": f"<observation>\n{obs}\n</observation>"})
                    elif done:
                        record["termination"] = "done"
                        record["final"] = done.group(1).strip()
                        break
                    else:
                        messages.append({"role": "user", "content": "Please respond with either an <action> to execute or <done> if the task is complete."})
                    write(path, record)
                else:
                    record["termination"] = "turn_limit"
        except TimeoutError:
            record["termination"] = clock.termination()  # "timeout" (the agent's budget) or "ceiling" (wall)
        except Exception as exc:
            record["termination"] = "error"
            record["error"] = f"{type(exc).__name__}: {exc}"
        record["elapsed_seconds"] = time.monotonic() - started
        record["clock"] = clock.summary()
        # Stop execution before taking the final snapshot, including on timeout.
        await asyncio.to_thread(subprocess.run, ["docker", "rm", "-f", container], capture_output=True)
        container = None
        await process.wait()
        if pre_cleanup is not None and env is not None:
            try:
                await asyncio.to_thread(pre_cleanup, env.environmentId)
            except Exception as exc:
                record["pre_cleanup_error"] = f"{type(exc).__name__}: {exc}"
        try:
            diff = await asyncio.to_thread(client.diff_run, runId=run.runId)
            record["diff"] = diff.model_dump(mode="json")
        except Exception as exc:
            record["diff_error"] = f"{type(exc).__name__}: {exc}"
        await asyncio.to_thread(client.evaluate_run, runId=run.runId,
                                expectedOutput=json.loads(row["answer"]))
        result = await asyncio.to_thread(client.get_results_for_run, runId=run.runId)
        record["evaluation"] = result.model_dump(mode="json")
    except Exception as exc:
        record["error"] = f"{type(exc).__name__}: {exc}"
        record.setdefault("termination", "setup_error")
    finally:
        record["usage"] = llm.usage.snapshot().to_dict()
        record["cost_usd"] = cost(record["usage"])
        await llm.close()
        if container:
            await asyncio.to_thread(subprocess.run, ["docker", "rm", "-f", container], capture_output=True)
        if env:
            try:
                await asyncio.to_thread(client.delete_env, envId=env.environmentId)
            except Exception as exc:
                record["cleanup_error"] = str(exc)
        write(path, record)
    evaluation = record.get("evaluation", {})
    print(json.dumps({"test_id": row["test_id"], "termination": record.get("termination"),
                      "score": evaluation.get("score"), "passed": evaluation.get("passed"),
                      "cost_usd": record["cost_usd"], "error": record.get("error")}), flush=True)
    return record


def prepare_isolated(service: str, seed_name: str, out: Path, database_url: str,
                     base_url: str, acting_user_id: str, preflight) -> dict:
    """Install isolated template and probe it (no model calls).

    Leaves the template registered for the later run; deletes only the
    preflight env. ``preflight`` is a sync callable
    (client, env_id) -> {"checks": [...], "errors": [...]} raising nothing.
    """
    out = Path(out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    engine = engine_for(database_url)
    template = None
    env = None
    client = AgentDiff(base_url=base_url)
    try:
        template = install_isolated_template(service, seed_name, engine)
        with ddl_lock():
            env = client.init_env(templateService=service, templateName=template["template_name"],
                                  impersonateUserId=acting_user_id)
        schema = environment_schema(engine, env.environmentId, template["template_id"])
        state = export_state(engine, schema, load_seed_module(service).Base.metadata)
        write(out / "initial_state.json", state)
        report = preflight(client, env.environmentId)
        write(out / "preflight.json", report)
        if report.get("errors"):
            raise ValueError("Preflight failed: " + "; ".join(report["errors"]))
        volatile = VOLATILE_TABLES.get(service, set())
        restated = export_state(engine, schema, load_seed_module(service).Base.metadata)
        stable_before = {table: rows for table, rows in state.items() if table not in volatile}
        stable_after = {table: rows for table, rows in restated.items() if table not in volatile}
        if digest(stable_after) != digest(stable_before):
            raise ValueError("Read-only preflight changed environment state")
        prepared = {**template, "service": service, "acting_user_id": acting_user_id,
                    "base_url": base_url, "initial_state_path": str(out / "initial_state.json"),
                    "initial_state_sha256": digest(state),
                    "preflight_path": str(out / "preflight.json"),
                    "prepared_at": datetime.now(timezone.utc).isoformat()}
        write(out / "prepared.json", prepared)
        return prepared
    except Exception:
        if env:
            with ddl_lock():
                client.delete_env(envId=env.environmentId)
            env = None
        if template:
            cleanup_isolated_template({**template, "service": service}, database_url)
        raise
    finally:
        if env:
            with ddl_lock():
                client.delete_env(envId=env.environmentId)
        engine.dispose()


def common_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--case", required=True, help="Bench test_id, e.g. box_116")
    parser.add_argument("--out", type=Path, required=True, help="Attempt output directory")
    parser.add_argument("--database-url", default="postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
    parser.add_argument("--base-url", default="http://127.0.0.1:18001")
    parser.add_argument("--model", default=QWEN_MODEL)
    parser.add_argument("--max-output-tokens", type=int, default=QWEN_MAX_OUTPUT_TOKENS)
    parser.add_argument("--prepare-only", action="store_true", help="Install + preflight only (no model calls)")
    parser.add_argument("--run-only", type=Path, help="Run episode from an existing prepared.json (no reinstall)")
    return parser


async def run_smoke(service: str, seed_name: str, preflight, args) -> dict:
    """Full smoke lifecycle for one bench case; saves evidence incrementally."""
    if not os.getenv("GENAI_API_KEY") and not args.prepare_only:
        raise ValueError("GENAI_API_KEY must be set for Purdue runs")
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    row = load_bench_row(args.case)
    if row["service"] != service:
        raise ValueError(f"Case {args.case} is service {row['service']}, not {service}")
    info = json.loads(row["info"])
    write(out / "case.json", row)
    prompt = official_prompt(service)
    (out / "system_prompt.txt").write_text(prompt)
    state = {"service": service, "case_id": args.case, "model": args.model,
             "status": "preflight", "started_utc": datetime.now(timezone.utc).isoformat()}
    write(out / "execution_summary.json", state)
    prepared = None
    fresh_template = False
    try:
        if args.run_only:
            prepared = json.loads(Path(args.run_only).read_text())
            if prepared.get("service") != service:
                raise ValueError("prepared.json service mismatch")
        else:
            prepared = await asyncio.to_thread(
                prepare_isolated, service, seed_name, out / "environment" / "preflight",
                args.database_url, args.base_url, info["impersonate_user_id"], preflight)
            fresh_template = True
        write(out / "prepared.json", prepared)
        state["status"] = "prepared"
        write(out / "execution_summary.json", state)
        if args.prepare_only:
            state["status"] = "prepared_only"
            write(out / "execution_summary.json", state)
            print(json.dumps({"case_id": args.case, "status": "prepared_only",
                              "template": prepared["template_name"]}), flush=True)
            return state
        config = {"service": service, "model": args.model, "seed_name": seed_name,
                  "smoke_runner": str(Path(__file__).resolve()),
                  "smoke_runner_sha256": sha_file(Path(__file__).resolve()),
                  "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
                  "turn_limit": TURN_LIMIT, "timeout_seconds": EPISODE_TIMEOUT_SECONDS,
                  "ceiling_seconds": EPISODE_CEILING_SECONDS, "clock": CLOCK_RULE,
                  "max_output_tokens_per_call": args.max_output_tokens,
                  "prompt_caching": "none on Purdue GenAI Studio; same prompt bytes, no cache markers",
                  "qwen_settings": "Provider defaults; no thinking/temperature overrides",
                  "rates_usd_per_million": QWEN_RATES, "cost_source": COST_SOURCE,
                  "executor_image": EXECUTOR_IMAGE,
                  "bridge_sha256": sha_file(BRIDGE),
                  "code_executor_sha256": sha_file(CODE_EXECUTOR),
                  "dataset_sha256": sha_file(DATASET)}
        write(out / "config.json", config)
        episode_row = dict(row)
        episode_info = dict(info, seed_template=prepared["template_name"])
        episode_row["info"] = json.dumps(episode_info)
        solver_out = out / "solver"
        solver_out.mkdir(parents=True, exist_ok=False)

        def _pre_cleanup(env_id: str) -> None:
            engine = engine_for(args.database_url)
            try:
                schema = environment_schema(engine, env_id, prepared["template_id"])
                metadata = load_seed_module(service).Base.metadata
                write(out / "environment" / "final_state.json", export_state(engine, schema, metadata))
            finally:
                engine.dispose()

        state["status"] = "solver_running"
        write(out / "execution_summary.json", state)
        record = await run_episode(service, episode_row, prompt, solver_out, base_url=args.base_url,
                                   model=args.model, max_output_tokens=args.max_output_tokens,
                                   record_requests=True, pre_cleanup=_pre_cleanup)
        record["smoke"] = {"seed_name": seed_name, "template_name": prepared["template_name"],
                           "isolated_template": True}
        write(solver_out / (args.case + ".json"), record)
        if record.get("diff") is not None:
            write(out / "environment" / "diff_run.json", record["diff"])
        if "evaluation" in record:
            write(out / "environment" / "evaluation.json", record["evaluation"])
        if "final" in record:
            (solver_out / "final_response.md").write_text(record["final"] + "\n")
        state.update(termination=record.get("termination"), error=record.get("error"),
                     usage=record.get("usage"), cost_usd=record.get("cost_usd"),
                     status="infrastructure_error" if record.get("termination") in ("error", "setup_error")
                     or ("evaluation" not in record and "diff" not in record) else "completed")
    except Exception as exc:
        state.update(status="infrastructure_error", error=f"{type(exc).__name__}: {exc}")
    finally:
        if prepared and fresh_template:
            try:
                await asyncio.to_thread(cleanup_isolated_template, prepared, args.database_url)
            except Exception as exc:
                state["template_cleanup_error"] = f"{type(exc).__name__}: {exc}"
        state["ended_utc"] = datetime.now(timezone.utc).isoformat()
        write(out / "execution_summary.json", state)
        print(json.dumps({key: state.get(key) for key in
                          ("service", "case_id", "status", "termination", "cost_usd", "error")}), flush=True)
    return state
