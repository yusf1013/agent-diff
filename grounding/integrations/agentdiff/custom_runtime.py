"""Custom-seed lifecycle for Box/Calendar/Linear cases (grounding harness).

Extends the native-case smoke runner (smoke_runtime.py) to install a case's own
seed instead of a fixed backend template. Everything else is reused unchanged:
the backend seed scripts' create/insert functions, the Purdue client and shared
limiter, the 40-turn/480s episode loop, snapshots, diff capture and cleanup of
only the UUID-named template this runner creates.

prepare_custom() makes no model calls: it installs the seed, opens a probe
environment, exports its actual state, runs the case's read probes (recording
responses), checks that the probes did not change state, and deletes the probe
environment while keeping the template. run_custom() is the model boundary.
"""
from __future__ import annotations

import asyncio
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from uuid import uuid4

import requests

from grounding.integrations.agentdiff import smoke_runtime as smoke
from grounding.integrations.agentdiff.runtime import (ddl_lock, digest, engine_for, environment_schema,
                                                      serialized_ddl, write)

SERVICE_PREFIX = {"box": "/2.0", "calendar": "", "linear": ""}


class _LockedAgentDiff(smoke.AgentDiff):
    """Serialize environment creation/deletion across concurrent episodes (schema cloning is DDL)."""

    @serialized_ddl
    def init_env(self, *args, **kwargs):
        return super().init_env(*args, **kwargs)

    @serialized_ddl
    def delete_env(self, *args, **kwargs):
        return super().delete_env(*args, **kwargs)


smoke.AgentDiff = _LockedAgentDiff  # run_episode resolves AgentDiff from its module globals
NATIVE_ASSERTIONS = json.dumps({"assertions": []})  # grounding is judged manually, not by native assertions


@serialized_ddl
def install_custom_template(service: str, seed_data: dict, engine, case_id: str) -> dict:
    """Create a UUID-named template schema from a case seed (no model calls)."""
    from sqlalchemy import text
    from src.platform.db.schema import TemplateEnvironment

    seed_module = smoke.load_seed_module(service)
    # The loader's order inserts two referenced Linear tables after their referrers; move them first.
    order = list(seed_module.TABLE_ORDER)
    for referenced, referrer in (("project_statuses", "projects"), ("initiatives", "documents")):
        if referenced in order and referrer in order and order.index(referenced) > order.index(referrer):
            order.remove(referenced)
            order.insert(order.index(referrer), referenced)
    # The loader's order omits the declared issue-subscriber association; load it after issue labels.
    if service == "linear" and "issue_subscriber_user_association" not in order:
        order.insert(order.index("issue_label_issue_association") + 1, "issue_subscriber_user_association")
    seed_module.TABLE_ORDER = order
    unknown = set(seed_data) - set(seed_module.TABLE_ORDER)
    if unknown:
        raise ValueError(f"Unknown {service} tables: {sorted(unknown)}")
    schema = f"{service}_campaign_{uuid4().hex}"
    template_id = uuid4()
    with engine.begin() as conn:
        conn.execute(text(f"SELECT pg_advisory_xact_lock({smoke._ADVISORY_LOCKS[service]})"))
        seed_module.create_schema(conn, schema)
        seed_module.create_tables(conn, schema)
        seed_module.insert_seed_data(conn, schema, copy.deepcopy(seed_data))
        scoped = conn.execution_options(schema_translate_map={None: schema})
        scoped.execute(TemplateEnvironment.__table__.insert().values(
            id=template_id, service=service, name=schema, version="v1", visibility="public", kind="schema",
            location=schema, description=f"Isolated custom {service} case {case_id}",
            table_order=list(seed_module.TABLE_ORDER)))
    return {"template_name": schema, "template_id": str(template_id), "table_order": list(seed_module.TABLE_ORDER)}


def service_url(base_url: str, env_id: str, service: str) -> str:
    return f"{base_url}/api/env/{env_id}/services/{service}{SERVICE_PREFIX[service]}"


def run_probes(client, env_id: str, service: str, probes) -> dict:
    """Execute read probes; record status and bodies. Never raises."""
    base = service_url(client.base_url, env_id, service)
    results, errors = [], []
    for probe in probes:
        method, path, payload = probe[:3]
        headers = {**client._headers(), **(probe[3] if len(probe) > 3 else {})}
        try:
            if method == "GET":
                response = requests.get(base + path, params=payload, headers=headers, timeout=60)
            else:
                response = requests.post(base + path, json=payload, headers=headers, timeout=60)
            try:
                body = response.json()
            except ValueError:
                body = {"non_json_response": response.text[:2000]}
            results.append({"method": method, "path": path, "payload": payload, "status": response.status_code,
                            "body": body})
            if response.status_code >= 400 or (isinstance(body, dict) and body.get("errors")):
                errors.append(f"{method} {path} -> {response.status_code}")
        except Exception as exc:  # recorded, not raised
            errors.append(f"{method} {path} raised {type(exc).__name__}: {exc}")
    return {"probes": results, "errors": errors}


def prepare_custom(case: dict, out: Path, database_url: str, base_url: str) -> dict:
    from agent_diff import AgentDiff
    service = case["domain"]
    out = Path(out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    engine = engine_for(database_url)
    client = AgentDiff(base_url=base_url)
    template = env = None
    try:
        template = install_custom_template(service, case["seed"], engine, case["case_id"])
        with ddl_lock():
            env = client.init_env(templateService=service, templateName=template["template_name"],
                                  impersonateUserId=case["acting_user_id"])
        schema = environment_schema(engine, env.environmentId, template["template_id"])
        metadata = smoke.load_seed_module(service).Base.metadata
        state = smoke.export_state(engine, schema, metadata)
        write(out / "initial_state.json", state)
        report = run_probes(client, env.environmentId, service, case.get("probes", []))
        write(out / "probes.json", report)
        if report["errors"]:
            raise ValueError("Probe failed: " + "; ".join(report["errors"]))
        volatile = smoke.VOLATILE_TABLES.get(service, set())
        after = smoke.export_state(engine, schema, metadata)
        if digest({k: v for k, v in after.items() if k not in volatile}) != digest(
                {k: v for k, v in state.items() if k not in volatile}):
            raise ValueError("Read-only probes changed environment state")
        prepared = {**template, "service": service, "case_id": case["case_id"], "case_sha256": case["case_sha256"],
                    "acting_user_id": case["acting_user_id"], "base_url": base_url,
                    "initial_state_path": str(out / "initial_state.json"), "initial_state_sha256": digest(state),
                    "prepared_at": datetime.now(timezone.utc).isoformat()}
        write(out / "prepared.json", prepared)
        return prepared
    except Exception:
        if env:
            with ddl_lock():
                client.delete_env(envId=env.environmentId)
            env = None
        if template:
            smoke.cleanup_isolated_template({**template, "service": service}, database_url)
        raise
    finally:
        if env:
            with ddl_lock():
                client.delete_env(envId=env.environmentId)
        engine.dispose()


async def run_custom(case: dict, prepared: dict, out: Path, database_url: str, *, model: str = smoke.QWEN_MODEL,
                     max_output_tokens: int = smoke.QWEN_MAX_OUTPUT_TOKENS) -> dict:
    """Run the established episode loop against the prepared template, then clean it up."""
    service = case["domain"]
    if prepared["case_sha256"] != case["case_sha256"]:
        raise ValueError("Case changed since preparation")
    out = Path(out).resolve()
    env_out = out / "environment"
    solver_out = out / "solver"
    solver_out.mkdir(parents=True, exist_ok=False)
    env_out.mkdir(parents=True, exist_ok=True)
    prompt = smoke.official_prompt(service)
    (solver_out / "system_prompt.txt").write_text(prompt)
    write(solver_out / "config.json", {
        "service": service, "model": model, "turn_limit": smoke.TURN_LIMIT,
        "timeout_seconds": smoke.EPISODE_TIMEOUT_SECONDS, "max_output_tokens_per_call": max_output_tokens,
        "ceiling_seconds": smoke.EPISODE_CEILING_SECONDS, "clock": smoke.CLOCK_RULE,
        "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
        "episode_loop": "grounding.integrations.agentdiff.smoke_runtime.run_episode (unchanged; its clock leaves out "
                        "Purdue waiting since 2026-09-27)",
        "custom_runtime_sha256": smoke.sha_file(Path(__file__).resolve()),
        "prompt_caching": "none on Purdue GenAI Studio; same prompt bytes, no cache markers",
        "qwen_settings": "Provider defaults; no thinking/temperature overrides",
        "native_assertions": "empty assertion list; native score is not a grounding judgment",
        "cost_source": smoke.COST_SOURCE, "case_sha256": case["case_sha256"]})
    row = {"test_id": case["case_id"], "test_name": case["case_id"], "#": None, "question": case["prompt"],
           "info": json.dumps({"seed_template": prepared["template_name"], "impersonate_user_id": case["acting_user_id"]}),
           "answer": NATIVE_ASSERTIONS}

    def pre_cleanup(env_id: str) -> None:
        engine = engine_for(database_url)
        try:
            schema = environment_schema(engine, env_id, prepared["template_id"])
            metadata = smoke.load_seed_module(service).Base.metadata
            write(env_out / "final_state.json", smoke.export_state(engine, schema, metadata))
        finally:
            engine.dispose()

    try:
        write(env_out / "initial_state.json", json.loads(Path(prepared["initial_state_path"]).read_text()))
        record = await smoke.run_episode(service, row, prompt, solver_out, base_url=prepared["base_url"], model=model,
                                         max_output_tokens=max_output_tokens, record_requests=True,
                                         pre_cleanup=pre_cleanup)
        if record.get("diff") is not None:
            write(env_out / "diff_run.json", record["diff"])
        if "final" in record:
            (solver_out / "final_response.md").write_text(record["final"] + "\n")
        return record
    finally:
        await asyncio.to_thread(smoke.cleanup_isolated_template, prepared, database_url)
