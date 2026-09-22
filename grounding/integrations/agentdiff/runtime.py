"""Install generated Slack cases, probe them, and reuse the baseline solver loop.

No model calls occur in ``prepare``. ``run_prepared`` is the paid boundary.
The database must be the local backend's database. Only fresh campaign-owned
schemas are created/dropped; baseline schemas are never written. Each solver
invocation imports its own baseline module, so concurrent cases share no patched
module globals. The baseline episode defaults, prompt, and sandbox remain
unchanged; model options may be explicitly overridden. Its platform client
redirects native assertion evaluation to diffRun.
"""
from __future__ import annotations

import argparse
import asyncio
from contextlib import contextmanager
from datetime import datetime, timezone
from enum import Enum
import hashlib
import importlib.util
import fcntl
import json
import os
from pathlib import Path
import re
import threading
from types import SimpleNamespace
from typing import Callable
from uuid import UUID, uuid4

from grounding.paths import REPO_ROOT as ROOT
BASELINE = ROOT / "grounding/solver/slack/run.py"
DOCS = ROOT / "examples/slack/testsuites/slack_docs/slack_api_full_docs.json"
PREFIX = "slack_campaign_"
_DDL_THREAD_LOCK = threading.RLock()
_DDL_LOCAL = threading.local()
_DDL_LOCK_FILE = Path("/tmp/agent-diff-slack-campaign-ddl.lock")
READ_METHODS = {
    "auth.test", "users.info", "users.list", "users.conversations", "users.getPresence",
    "conversations.info", "conversations.list", "conversations.members",
    "conversations.history", "conversations.replies", "reactions.get",
    "search.messages", "search.all",
}


@contextmanager
def ddl_lock():
    """Serialize schema lifecycle across campaign threads/processes, not agents.

    Backend schema cloning inspects PostgreSQL's global catalogs, so a concurrent
    drop can invalidate a catalog relation during introspection. Nested same-
    thread callers share one flock; model calls and ordinary Slack reads/writes
    never hold this lock.
    """
    with _DDL_THREAD_LOCK:
        depth = getattr(_DDL_LOCAL, "depth", 0)
        if depth == 0:
            lock_file = _DDL_LOCK_FILE.open("a+")
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
            _DDL_LOCAL.file = lock_file
        _DDL_LOCAL.depth = depth + 1
        try:
            yield
        finally:
            _DDL_LOCAL.depth -= 1
            if _DDL_LOCAL.depth == 0:
                fcntl.flock(_DDL_LOCAL.file.fileno(), fcntl.LOCK_UN)
                _DDL_LOCAL.file.close()
                del _DDL_LOCAL.file


def serialized_ddl(function):
    from functools import wraps
    @wraps(function)
    def wrapped(*args, **kwargs):
        with ddl_lock():
            return function(*args, **kwargs)
    return wrapped


def json_default(value):
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, UUID):
        return str(value)
    raise TypeError(f"Not JSON serializable: {type(value).__name__}")


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False, default=json_default) + "\n")
    tmp.replace(path)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, default=json_default).encode()).hexdigest()


def dependencies():
    import sys
    for path in (ROOT / "backend", ROOT / "sdk/agent-diff-python"):
        if str(path) not in sys.path:
            sys.path.insert(0, str(path))
    from sqlalchemy import create_engine
    from src.services.slack.database.base import Base
    from src.services.slack.database import schema  # noqa: F401
    from agent_diff import AgentDiff
    return create_engine, Base.metadata, AgentDiff


def engine_for(database_url=None):
    create_engine, _, _ = dependencies()
    url = database_url or os.environ.get("DATABASE_URL")
    if not url:
        raise ValueError("Supply DATABASE_URL for the local backend database")
    from sqlalchemy.engine import make_url
    parsed = make_url(url)
    if parsed.host not in (None, "localhost", "127.0.0.1", "::1"):
        raise ValueError("Campaign runtime only accepts a local database host")
    return create_engine(url, pool_pre_ping=True)


def seed_tables(case):
    seed = case["seed"]
    tables = seed.get("tables", seed)
    if not isinstance(tables, dict) or not all(isinstance(v, list) for v in tables.values()):
        raise ValueError("seed must map real Slack tables to lists of rows")
    return tables


def ordered_messages(rows):
    """Preserve insertion order while placing parents before children."""
    pending = list(rows)
    done = set()
    ordered = []
    while pending:
        ready = [r for r in pending if not r.get("parent_id") or r["parent_id"] in done]
        if not ready:
            raise ValueError("Message parents contain a cycle or missing parent")
        for row in ready:
            ordered.append(row)
            done.add(row["message_id"])
            pending.remove(row)
    return ordered


def normalize_row(table, row):
    from sqlalchemy import DateTime
    unknown = set(row) - set(table.columns.keys())
    if unknown:
        raise ValueError(f"Unknown {table.name} fields: {sorted(unknown)}")
    value = dict(row)
    for column in table.columns:
        if isinstance(column.type, DateTime) and isinstance(value.get(column.name), str):
            dt = datetime.fromisoformat(value[column.name].replace("Z", "+00:00"))
            if dt.tzinfo is not None and not column.type.timezone:
                dt = dt.astimezone(timezone.utc).replace(tzinfo=None)
            value[column.name] = dt
    return value


@serialized_ddl
def install_template(case, engine):
    from sqlalchemy import text, bindparam
    _, metadata, _ = dependencies()
    tables = seed_tables(case)
    unknown = set(tables) - set(metadata.tables)
    if unknown:
        raise ValueError(f"Unknown Slack tables: {sorted(unknown)}")
    if not any(r.get("user_id") == case["acting_user_id"] for r in tables.get("users", [])):
        raise ValueError("acting_user_id is absent from seed users")
    # UUID is generated here, never taken from author/model input.
    schema = PREFIX + uuid4().hex
    template_id = uuid4()
    from src.platform.db.schema import TemplateEnvironment
    with engine.begin() as conn:
        # Model enum types live in public; serialize their check/create on first use.
        conn.execute(text("SELECT pg_advisory_xact_lock(726411930)"))
        conn.execute(text(f'CREATE SCHEMA "{schema}"'))
        scoped = conn.execution_options(schema_translate_map={None: schema})
        metadata.create_all(scoped)
        for table in metadata.sorted_tables:
            rows = tables.get(table.name, [])
            if table.name == "messages":
                rows = ordered_messages(rows)
            for row in rows:
                # Match the benchmark seed loader: omitted columns use database
                # defaults, never ORM Python defaults. Typed binds preserve JSONB
                # and datetime values without inserting executable author SQL.
                values = normalize_row(table, row)
                fields = list(values)
                if fields:
                    columns = ", ".join(f'"{field}"' for field in fields)
                    binds = ", ".join(f":v{i}" for i in range(len(fields)))
                    statement = text(f'INSERT INTO "{schema}"."{table.name}" ({columns}) VALUES ({binds})')
                    statement = statement.bindparams(*(bindparam(f"v{i}", type_=table.c[field].type)
                                                        for i, field in enumerate(fields)))
                    scoped.execute(statement, {f"v{i}": values[field] for i, field in enumerate(fields)})
                else:
                    scoped.execute(text(f'INSERT INTO "{schema}"."{table.name}" DEFAULT VALUES'))
        scoped.execute(TemplateEnvironment.__table__.insert().values(
            id=template_id, service="slack", name=schema, version="v1",
            visibility="public", kind="schema", location=schema,
            description="Isolated generated Slack campaign case",
            table_order=[t.name for t in metadata.sorted_tables],
        ))
    return {"template_name": schema, "template_id": str(template_id)}


def export_state(engine, schema):
    from sqlalchemy import select
    _, metadata, _ = dependencies()
    with engine.connect() as connection:
        conn = connection.execution_options(schema_translate_map={None: schema})
        result = {}
        for table in metadata.sorted_tables:
            query = select(table).order_by(*table.primary_key.columns)
            result[table.name] = [dict(row) for row in conn.execute(query).mappings()]
    return json.loads(json.dumps(result, default=json_default))


def environment_schema(engine, env_id, template_id):
    from sqlalchemy import select
    from src.platform.db.schema import RunTimeEnvironment
    with engine.connect() as conn:
        row = conn.execute(select(RunTimeEnvironment.schema, RunTimeEnvironment.template_id)
                           .where(RunTimeEnvironment.id == UUID(env_id))).one()
    if str(row.template_id) != template_id or not row.schema.startswith("state_"):
        raise ValueError("Environment did not originate from the prepared campaign template")
    return row.schema


@serialized_ddl
def cleanup(prepared, database_url=None):
    """Only drop the exact UUID-named template created by this runtime."""
    from sqlalchemy import text, select
    engine = engine_for(database_url)
    from src.platform.db.schema import TemplateEnvironment, RunTimeEnvironment, EnvironmentPoolEntry
    name = prepared["template_name"]
    if not re.fullmatch(PREFIX + r"[0-9a-f]{32}", name):
        raise ValueError("Refusing cleanup outside campaign schema namespace")
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
            # deleteEnv drops the clone but retains its historical pool entry.
            pool = EnvironmentPoolEntry.__table__
            entries = conn.execute(select(pool.c.schema_name).where(
                pool.c.template_id == UUID(prepared["template_id"]))).scalars().all()
            for clone in entries:
                if not re.fullmatch(r"state_[0-9a-f]{32}", clone):
                    raise ValueError("Unexpected campaign clone schema name")
                conn.execute(text(f'DROP SCHEMA IF EXISTS "{clone}" CASCADE'))
            conn.execute(pool.delete().where(pool.c.template_id == UUID(prepared["template_id"])))
            conn.execute(table.delete().where(table.c.id == UUID(prepared["template_id"])))
            conn.execute(text(f'DROP SCHEMA IF EXISTS "{name}" CASCADE'))
    finally:
        engine.dispose()


def _lookup(value, path):
    for piece in path:
        value = value[int(piece)] if isinstance(value, list) else value[piece]
    return value


def probe_environment(client, env_id, case, state, *, get=None):
    """Record API visibility, not merely whether a corresponding DB row exists.

    Generic optional probes expose access gaps to validation without requiring
    all irrelevant background to be visible. Author-supplied required probes
    can enforce route-specific access using checks of exact response fields.
    These observations are private construction data and never solver context.
    """
    import requests
    get = get or requests.get
    plans = [
        {"method": "auth.test", "required": True},
        {"method": "users.info", "params": {"user": case["acting_user_id"]}, "required": True},
        {"method": "users.list", "params": {"limit": 1000}},
        {"method": "conversations.list", "params": {"limit": 1000, "types": "public_channel,private_channel,mpim,im"}},
    ]
    plans.extend({"method": "users.info", "params": {"user": row["user_id"]}}
                 for row in state.get("users", []) if row["user_id"] != case["acting_user_id"])
    for row in state.get("channels", []):
        for method in ("conversations.info", "conversations.members", "conversations.history"):
            plans.append({"method": method, "params": {"channel": row["channel_id"], "limit": 999 if method == "conversations.history" else 1000}})
    parents = {row["parent_id"] for row in state.get("messages", []) if row.get("parent_id")}
    for row in state.get("messages", []):
        plans.append({"method": "reactions.get", "params": {
            "channel": row["channel_id"], "timestamp": row["message_id"]}})
        if row["message_id"] in parents:
            plans.append({"method": "conversations.replies", "params": {
                "channel": row["channel_id"], "ts": row["message_id"], "limit": 1000}})
    plans.extend(case.get("visibility_probes", []))
    observations = []
    for plan in plans:
        method = plan["method"]
        if method not in READ_METHODS:
            raise ValueError(f"Visibility probe is not an allowlisted read: {method}")
        params = dict(plan.get("params", {}))
        pages = []
        errors = []
        cursors = set()
        for _ in range(50):
            response = get(f"{client.base_url}/api/env/{env_id}/services/slack/{method}",
                                    params=params, headers=client._headers(), timeout=60)
            try:
                body = response.json()
            except ValueError:
                body = {"non_json_response": response.text[:1000]}
            pages.append({"status_code": response.status_code, "body": body})
            if not response.ok or not body.get("ok"):
                errors.append(f"{method} returned HTTP {response.status_code}, error={body.get('error')}")
                break
            cursor = body.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                if body.get("has_more"):
                    errors.append(f"{method} has_more without cursor: visibility incomplete")
                break
            if cursor in cursors:
                errors.append(f"{method} repeated pagination cursor")
                break
            cursors.add(cursor)
            params["cursor"] = cursor
        else:
            errors.append(f"{method} exceeded 50-page probe bound")
        for check in plan.get("checks", []):
            try:
                got = _lookup(pages[0]["body"], check["path"])
                if "equals" in check and got != check["equals"]:
                    errors.append(f"{method} field {check['path']} did not equal expected value")
                if "contains" in check and check["contains"] not in got:
                    errors.append(f"{method} field {check['path']} did not contain expected value")
            except (KeyError, IndexError, TypeError, ValueError):
                errors.append(f"{method} missing expected path {check['path']}")
        observations.append({"probe": plan, "pages": pages, "errors": errors})
    required_errors = [error for item in observations if item["probe"].get("required")
                       for error in item["errors"]]
    return {"probes": observations, "required_errors": required_errors,
            "note": "Optional probe errors require route-specific review; success alone is not semantic validity."}


def reverse_channel_anchor(case, state, report, discoverable, observed, complete_history):
    """Narrow reverse proof: named channel catalog -> complete message histories.

    No hidden channel names or message attributes are used to waive API evidence.
    Decline unsupported selectors; the general checker/reviewer retains authority.
    """
    from grounding.generation.selection import SCHEMA, _compare, evaluate_selector
    selector = case["private"]["selector"]
    focal, auxiliary = selector["focal"], selector["auxiliary"]
    if (selector["root_table"] != "messages" or focal["path"] != ["messages", "channels"]
            or focal["joins"] != ["messages.channel_id"] or "count" in focal
            or any(q["path"] != ["messages"] or q["joins"] or "count" in q for q in auxiliary)):
        return None
    terminal = [f for f in focal["filters"] if f["node"] == 1]
    anchors = [f for f in terminal if f["field"] == "channel_name" and f["op"] in {"eq", "in"}]
    if not anchors:
        return None
    anchor = anchors[0]
    names = set(anchor["value"] if anchor["op"] == "in" else [anchor["value"]])
    if not names:
        return None
    channel_ids = {r["channel_id"] for r in state.get("channels", [])}
    # This bounded proof is restricted to one workspace; it must not turn an
    # actor-local catalog into a claim about other or unassigned workspaces.
    workspaces = {r.get("team_id") for r in state.get("channels", [])}
    if len(workspaces) != 1 or None in workspaces:
        return None
    catalogs = [i for i in discoverable if report["probes"][i]["probe"]["method"] == "conversations.list"
                and {c["id"] for p in report["probes"][i]["pages"] for c in p["body"].get("channels", [])} == channel_ids]
    if not catalogs:
        return None
    channels = {r["channel_id"]: r for r in observed["channels"]}
    # All catalog entries belong to its API-selected workspace. The real unique
    # (team_id,channel_name) constraint excludes unnamed entries from names already
    # observed on another entry. If a name has no observed match, do not infer absence.
    named = {name: [r for r in channels.values() if r.get("channel_name") == name] for name in names}
    if any(len(rows) != 1 for rows in named.values()):
        return None
    candidate_channels = {rows[0]["channel_id"] for rows in named.values()}
    root_filters = [*selector["scope"], *[f for f in focal["filters"] if f["node"] == 0],
                    *[f for query in auxiliary for f in query["filters"]]]
    fields = {f["field"] for f in root_filters} | {"message_id", "channel_id"}
    if any(SCHEMA["messages"].columns[f].kind == "datetime" for f in fields):
        return None
    seed_channels = {r["channel_id"]: r for r in state.get("channels", [])}
    selected_channels = set()
    for cid in candidate_channels:
        row = channels[cid]
        if any(f["field"] not in row or row[f["field"]] != seed_channels[cid].get(f["field"]) for f in terminal):
            return None
        if all(_compare(row[f["field"]], f["op"], f["value"]) for f in terminal):
            selected_channels.add(cid)
    if not selected_channels <= complete_history:
        return None
    messages = {r["message_id"]: r for r in observed["messages"]}
    source_messages = {r["message_id"]: r for r in state.get("messages", [])}
    expected_rows = {mid for mid, r in source_messages.items() if r["channel_id"] in selected_channels}
    actual_rows = {mid for mid, r in messages.items() if r["channel_id"] in selected_channels}
    if expected_rows != actual_rows:
        return None
    needed = expected_rows | set(case["private"].get("near_misses", []))
    if any(mid not in messages or any(f not in messages[mid] or messages[mid][f] != source_messages[mid].get(f)
                                    for f in fields) for mid in needed):
        return None
    def passes(row, filters):
        return all(_compare(row[f["field"]], f["op"], f["value"]) for f in filters)
    found = {mid for mid in expected_rows if passes(messages[mid], root_filters)}
    actual = evaluate_selector(state, selector)
    if found != set(actual["matches"]):
        return None
    for mid in case["private"].get("near_misses", []):
        row = messages[mid]
        # Non-anchor names are excluded by catalog uniqueness, while selected
        # channels require an observed false root-field focal predicate.
        if row["channel_id"] in candidate_channels - selected_channels:
            terminal_false = True
        elif row["channel_id"] not in candidate_channels:
            terminal_false = row["channel_id"] in channels
        else:
            terminal_false = False
        root_focal = [f for f in focal["filters"] if f["node"] == 0]
        if not (terminal_false or not passes(row, root_focal)) or not passes(row, selector["scope"]):
            return None
        if not all(passes(row, q["filters"]) for q in auxiliary):
            return None
    evidence = sorted(set(catalogs + [i for i in discoverable if report["probes"][i]["probe"]["method"] == "conversations.history"
                          and report["probes"][i]["probe"].get("params", {}).get("channel") in
                          (selected_channels | {messages[mid]["channel_id"] for mid in case["private"].get("near_misses", [])})]))
    return {"certified": True, "method": "reverse_channel_anchor", "errors": [], "limitations": [],
            "matches": sorted(found), "focal_negatives": case["private"].get("near_misses", []),
            "evidence_probe_indices": evidence, "discoverable_probe_indices": discoverable,
            "note": "Complete API channel catalog and matching histories; named-anchor exclusion uses real workspace/name uniqueness, not hidden field values. Negative proof covers declared negatives only."}


def certify_visibility(case, state, report):
    """Certify selector-relevant seed facts against discoverable live API projections.

    This is a bounded API/data check, not a natural-language interpretation or
    proof that a solver will perform the available reads. Unknown-ID probes do
    not establish discoverability. Irrelevant inaccessible background is ignored.
    Field comparisons certify only fields required by scope/focal/auxiliary
    predicates; complete adjacency sets certify joins, counts and empty matches.
    """
    from grounding.generation.selection import (SCHEMA, canonical_handle, handle_key, evaluate_selector, query_matches,
                                                _compare, _field_value, _join_fields)
    selector = case.get("private", {}).get("selector")
    errors, limitations = [], []
    if selector is None:
        return {"certified": False, "errors": ["No private.selector supplied"], "limitations": []}
    try:
        expected = evaluate_selector(state, selector)
    except ValueError as exc:
        return {"certified": False, "errors": [f"Invalid selector: {exc}"], "limitations": []}
    tables = ("teams", "users", "channels", "messages", "user_teams", "channel_members", "message_reactions")
    visible = {table: {} for table in tables}
    known_users, known_channels, known_messages = {case["acting_user_id"]}, set(), set()
    # Explicit native IDs in the request are legitimate initial discovery anchors.
    for table, field, known in (("users", "user_id", known_users), ("channels", "channel_id", known_channels)):
        for row in state.get(table, []):
            if re.search(r"(?<![A-Za-z0-9_])" + re.escape(row[field]) + r"(?![A-Za-z0-9_])", case["prompt"]):
                known.add(row[field])
    complete_members, complete_history, complete_replies, complete_reactions = set(), set(), set(), set()

    def key(table, row):
        return handle_key(table, canonical_handle(table, row))

    def put(table, row):
        visible[table].setdefault(key(table, row), {}).update(row)

    def workspace(team_id):
        if team_id:
            put("teams", {"team_id": team_id})

    def user(payload):
        uid = payload.get("id")
        if not uid:
            return
        known_users.add(uid)
        profile = payload.get("profile", {})
        value = {"user_id": uid}
        for field, api in (("username", "name"), ("real_name", "real_name"), ("timezone", "tz"), ("is_bot", "is_bot")):
            if api in payload:
                value[field] = payload[api]
        for field, api in (("email", "email"), ("display_name", "display_name"), ("title", "title")):
            if api in profile:
                value[field] = profile[api]
        if "deleted" in payload:
            value["is_active"] = not payload["deleted"]
        if "updated" in payload:
            value["created_at"] = datetime.fromtimestamp(payload["updated"], timezone.utc).replace(tzinfo=None).isoformat()
        put("users", value)
        tid = payload.get("team_id")
        workspace(tid)
        if tid:
            put("user_teams", {"user_id": uid, "team_id": tid,
                "role": "owner" if payload.get("is_owner") else "admin" if payload.get("is_admin") else "__non_admin__"})

    def channel(payload):
        cid = payload.get("id")
        if not cid:
            return
        known_channels.add(cid)
        value = {"channel_id": cid}
        for field, api in (("channel_name", "name"), ("is_private", "is_private"), ("is_archived", "is_archived"), ("is_dm", "is_im"), ("is_gc", "is_mpim")):
            if api in payload:
                value[field] = payload[api]
        for field, api in (("topic_text", "topic"), ("purpose_text", "purpose")):
            if api in payload:
                value[field] = payload[api].get("value")
        if "created" in payload:
            value["created_at"] = datetime.fromtimestamp(payload["created"], timezone.utc).replace(tzinfo=None).isoformat()
        if "context_team_id" in payload:
            value["team_id"] = payload["context_team_id"]
            workspace(value["team_id"])
        put("channels", value)

    def message(payload, cid, *, reaction_response=False):
        mid = payload.get("ts")
        if not mid:
            return
        known_messages.add((cid, mid))
        value = {"message_id": mid, "channel_id": cid}
        if not reaction_response:
            value.update(parent_id=payload.get("thread_ts") if payload.get("thread_ts") != mid else None,
                         blocks=payload.get("blocks"))
        for field, api in (("user_id", "user"), ("message_text", "text"), ("type", "type")):
            if api in payload:
                value[field] = payload[api]
        if value.get("user_id"):
            known_users.add(value["user_id"])
        put("messages", value)
        reactions_complete = reaction_response or "reactions" in payload
        for reaction in payload.get("reactions", []):
            reactors = reaction.get("users", [])
            if reaction.get("count") != len(set(reactors)):
                reactions_complete = False
            for uid in reactors:
                known_users.add(uid)
                put("message_reactions", {"message_id": mid, "user_id": uid, "reaction_type": reaction["name"]})
        if reactions_complete:
            complete_reactions.add(mid)

    pending = list(enumerate(report.get("probes", [])))
    used = []
    while pending:
        progressed = False
        for indexed in list(pending):
            index, item = indexed
            plan = item["probe"]
            method, params = plan["method"], plan.get("params", {})
            allowed = method in {"auth.test", "users.list", "conversations.list"}
            allowed |= method == "users.info" and params.get("user") in known_users
            allowed |= method in {"conversations.info", "conversations.members", "conversations.history"} and params.get("channel") in known_channels
            allowed |= method == "conversations.replies" and (params.get("channel"), params.get("ts")) in known_messages
            allowed |= method == "reactions.get" and (params.get("channel"), params.get("timestamp")) in known_messages
            if not allowed:
                continue
            pending.remove(indexed)
            progressed = True
            if item.get("errors"):
                continue
            used.append(index)
            for page in item["pages"]:
                body = page["body"]
                if not body.get("ok"):
                    continue
                if method == "auth.test":
                    known_users.add(body.get("user_id"))
                    workspace(body.get("team_id"))
                elif method == "users.list":
                    for payload in body.get("members", []):
                        user(payload)
                elif method == "users.info":
                    user(body["user"])
                elif method == "conversations.list":
                    for payload in body.get("channels", []):
                        channel(payload)
                elif method == "conversations.info":
                    channel(body["channel"])
                elif method == "conversations.members":
                    cid = params["channel"]
                    for uid in body.get("members", []):
                        known_users.add(uid)
                        put("channel_members", {"channel_id": cid, "user_id": uid})
                    complete_members.add(cid)
                elif method in {"conversations.history", "conversations.replies"}:
                    cid = params["channel"]
                    for payload in body.get("messages", []):
                        message(payload, cid)
                    if method == "conversations.history":
                        complete_history.add(cid)
                    else:
                        complete_replies.add((cid, params["ts"]))
                elif method == "reactions.get":
                    message(body["message"], params["channel"], reaction_response=True)
        if not progressed:
            break

    observed = {table: list(rows.values()) for table, rows in visible.items()}
    required = {table: set() for table in tables}
    checked_fields, checked_edges = set(), set()

    def field_check(table, row, field, predicate=None):
        marker = (table, key(table, row), field)
        checked_fields.add(marker)
        got = visible[table].get(key(table, row), {})
        if field not in got:
            errors.append(f"API does not expose needed {table} {canonical_handle(table, row)!r} field {field}")
            return
        actual = _field_value(table, row, field)
        if table == "user_teams" and field == "role":
            values = predicate["value"] if predicate and predicate["op"] in {"in", "not_in"} else [predicate["value"]] if predicate else []
            if not predicate or predicate["op"] not in {"eq", "ne", "in", "not_in"} or not set(values) <= {"owner", "admin"}:
                limitations.append("Workspace membership roles expose owner/admin distinctions, not member versus guest")
                return
            actual = actual if actual in {"owner", "admin"} else "__non_admin__"
        if SCHEMA[table].columns[field].kind == "datetime" and actual is not None:
            # API integer timestamps lose subsecond information; exact preservation is required.
            actual = datetime.fromisoformat(actual.replace("Z", "+00:00")).replace(tzinfo=None).isoformat()
        if predicate and _compare(actual, predicate["op"], predicate["value"]) == _compare(got[field], predicate["op"], predicate["value"]):
            # A selection predicate needs the same truth value, not identical
            # presentation (e.g. a default timezone on a null stored profile).
            return
        if actual != got[field]:
            errors.append(f"API projection differs for {table} {canonical_handle(table, row)!r} field {field}: seed={actual!r}, API={got[field]!r}")

    root_table = selector["root_table"]
    population_keys = {handle_key(root_table, h) for h in expected["population"]}
    roots = [row for row in state.get(root_table, []) if key(root_table, row) in population_keys]
    # Scope predicates must also be observable for excluded roots that were enumerated.
    for row in state.get(root_table, []):
        if key(root_table, row) in visible[root_table] or key(root_table, row) in population_keys:
            for predicate in selector["scope"]:
                field_check(root_table, row, predicate["field"], predicate)
    missing_roots = population_keys - set(visible[root_table])
    if missing_roots:
        errors.append(f"Scoped {root_table} population has {len(missing_roots)} undiscoverable API referents: {sorted(missing_roots)}")

    def inspect_query(root, query):
        start_errors, start_limitations = len(errors), len(limitations)
        path = query["path"]
        current = [root]
        for node, table in enumerate(path):
            predicates = [f for f in query["filters"] if f["node"] == node]
            accepted = []
            for row in current:
                required[table].add(key(table, row))
                if key(table, row) not in visible[table]:
                    errors.append(f"Required {table} referent {canonical_handle(table, row)!r} is not discoverable through recorded APIs")
                predicate_errors, predicate_limits = len(errors), len(limitations)
                proven_false = False
                for predicate in predicates:
                    before_e, before_l = len(errors), len(limitations)
                    field_check(table, row, predicate["field"], predicate)
                    if len(errors) == before_e and len(limitations) == before_l and not _compare(
                            _field_value(table, row, predicate["field"]), predicate["op"], predicate["value"]):
                        proven_false = True
                if proven_false:
                    # One observed false conjunct excludes this row. Other
                    # unknown fields on that same row need not be retrieved.
                    del errors[predicate_errors:]
                    del limitations[predicate_limits:]
                elif all(_compare(_field_value(table, row, f["field"]), f["op"], f["value"]) for f in predicates):
                    accepted.append(row)
                if table == "user_teams":
                    memberships = [r for r in state.get(table, []) if r["user_id"] == row["user_id"]]
                    if len(memberships) > 1:
                        limitations.append(f"Profile workspace selection is ambiguous for {row['user_id']}: {len(memberships)} memberships; full roster is not exposed")
            if node == len(path) - 1:
                break
            target = path[node + 1]
            left, right = _join_fields(table, target, query["joins"][node])
            following = {}
            for row in accepted:
                marker = (table, key(table, row), query["joins"][node], target)
                checked_edges.add(marker)
                field_check(table, row, left)
                value = _field_value(table, row, left)
                neighbors = [r for r in state.get(target, []) if value is not None and _field_value(target, r, right) == value]
                exposed = [r for r in observed[target] if value is not None and r.get(right) == value]
                if {key(target, r) for r in neighbors} != {key(target, r) for r in exposed}:
                    errors.append(f"API adjacency differs for {table} {canonical_handle(table, row)!r} via {query['joins'][node]} to {target}")
                # API absence/counts need a complete collection response, including zero neighbors.
                if table == "channels" and target == "channel_members" and row["channel_id"] not in complete_members:
                    errors.append(f"No complete member listing for {row['channel_id']}")
                if table == "channels" and target == "messages" and row["channel_id"] not in complete_history:
                    errors.append(f"No complete message history for {row['channel_id']}")
                if table == "messages" and target == "message_reactions" and row["message_id"] not in complete_reactions:
                    errors.append(f"No complete reaction listing for {row['message_id']}")
                for neighbor in neighbors:
                    field_check(target, neighbor, right)
                    following[key(target, neighbor)] = neighbor
            current = list(following.values())
        # Returning a DB-computed truth is safe only after its necessary fields
        # and edges have been established by live API observations above.
        if len(errors) == start_errors and len(limitations) == start_limitations:
            return query_matches(state, root, query)
        return None

    claimed_negatives = {handle_key(root_table, handle) for handle in case.get("private", {}).get("near_misses", [])}
    for root in roots:
        required[root_table].add(key(root_table, root))
        focal = inspect_query(root, selector["focal"])
        # An API-established false conjunct already excludes this root. We still
        # prove auxiliary conditions for claimed focal negatives, since their
        # required resemblance is a separate construction claim.
        if focal is False and (case.get("private", {}).get("workflow_version") == 2 or key(root_table, root) not in claimed_negatives):
            continue
        for query in selector["auxiliary"]:
            if inspect_query(root, query) is False:
                break
    proven_negatives = []
    if case.get("private", {}).get("workflow_version") == 2:
        for row in state.get(root_table, []):
            if key(root_table, row) not in claimed_negatives:
                continue
            start_errors, start_limits = len(errors), len(limitations)
            scope_false = False
            for predicate in selector["scope"]:
                field_check(root_table, row, predicate["field"], predicate)
                scope_false |= not _compare(_field_value(root_table, row, predicate["field"]), predicate["op"], predicate["value"])
            excluded = scope_false and len(errors) == start_errors and len(limitations) == start_limits
            if not excluded:
                # Any independently API-established false conjunct suffices.
                for query in [selector["focal"], *selector["auxiliary"]]:
                    if inspect_query(row, query) is False:
                        excluded = True
                        break
            if excluded:
                proven_negatives.append(canonical_handle(root_table, row))
            # These optional additional proofs do not alter the original access verdict.
            del errors[start_errors:]
            del limitations[start_limits:]
    errors = sorted(set(errors))
    limitations = sorted(set(limitations))
    result = {"proven_negatives": proven_negatives, "certified": not errors and not limitations, "errors": errors, "limitations": limitations,
            "required_rows": {table: len(keys) for table, keys in required.items() if keys},
            "checked_fields": len(checked_fields), "checked_adjacencies": len(checked_edges),
            "discoverable_probe_indices": used,
            "note": "Certifies the declared selector against live API projections, not prompt/selector equivalence or semantic realism."}
    if not result["certified"]:
        reverse = reverse_channel_anchor(case, state, report, used, observed, complete_history)
        if reverse:
            reverse["prior_forward_check"] = result
            reverse["proven_negatives"] = proven_negatives
            return reverse
    return result


def prepare(case, out, database_url=None, base_url="http://127.0.0.1:18000"):
    """Install and inspect a case without solver calls; leaves its template for run."""
    _, _, AgentDiff = dependencies()
    out = Path(out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    engine = engine_for(database_url)
    template = None
    env = None
    client = AgentDiff(base_url=base_url)
    try:
        template = install_template(case, engine)
        with ddl_lock():
            env = client.init_env(templateService="slack", templateName=template["template_name"],
                                  impersonateUserId=case["acting_user_id"])
        schema = environment_schema(engine, env.environmentId, template["template_id"])
        state = export_state(engine, schema)
        write(out / "initial_state.json", state)
        probes = probe_environment(client, env.environmentId, case, state)
        write(out / "visibility.json", probes)
        certification = certify_visibility(case, state, probes) if case.get("private", {}).get("selector") else None
        if certification is not None:
            write(out / "visibility_certification.json", certification)
        if probes["required_errors"]:
            raise ValueError("Required visibility probes failed: " + "; ".join(probes["required_errors"]))
        # Read-only probes must not change the seed.
        if digest(export_state(engine, schema)) != digest(state):
            raise ValueError("Read-only visibility probes changed environment state")
        prepared = {**template, "case_id": case["case_id"], "case_sha256": digest(case),
                    "base_url": base_url, "initial_state_path": str(out / "initial_state.json"),
                    "initial_state_sha256": digest(state), "visibility_path": str(out / "visibility.json"),
                    "visibility_certification_path": str(out / "visibility_certification.json") if certification is not None else None,
                    "prepared_at": datetime.now(timezone.utc).isoformat()}
        write(out / "prepared.json", prepared)
        write(out / "case.json", case)
        return prepared
    except Exception:
        if env:
            with ddl_lock():
                client.delete_env(envId=env.environmentId)
            env = None
        if template:
            cleanup(template, database_url)
        raise
    finally:
        if env:
            with ddl_lock():
                client.delete_env(envId=env.environmentId)
        engine.dispose()


def load_baseline():
    dependencies()
    spec = importlib.util.spec_from_file_location("slack_baseline_" + uuid4().hex, BASELINE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


async def run_prepared(case, prepared, out, database_url=None,
                       model="us.anthropic.claude-sonnet-5", validate_installed: Callable | None = None,
                       *, environment_out=None, evaluation_inputs=None,
                       max_output_tokens=128000, thinking_budget=None, rates=None,
                       record_requests=False):
    """Run the original episode using the private prepared template, then cleanup.

    validate_installed is an optional synchronous callback(case, initial_state).
    It must raise to block the solver. The caller should separately accept the
    semantic generation review before invoking this paid operation.

    max_output_tokens includes the optional thinking_budget, rather than adding
    to it. rates overrides estimated USD-per-million prices for this invocation
    only. record_requests saves gzipped logical SDK requests before each call.
    """
    if digest(case) != prepared["case_sha256"]:
        raise ValueError("Case changed since installation/preflight; prepare it again")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", case["case_id"]):
        raise ValueError("case_id must be a safe filename component")
    baseline = load_baseline()
    args = SimpleNamespace(base_url=prepared["base_url"], model=model,
                           max_output_tokens=max_output_tokens, thinking_budget=thinking_budget,
                           record_requests=record_requests)
    options = baseline.model_options(args)
    if rates is not None:
        baseline.RATES = dict(rates)  # This invocation's private imported module.
    BaseClient = baseline.AgentDiff
    engine = engine_for(database_url)
    out = Path(out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    environment_out = Path(environment_out) if environment_out else out
    environment_out.mkdir(parents=True, exist_ok=True)
    evaluation_inputs = Path(evaluation_inputs) if evaluation_inputs else out / "oracle_input"
    installed_state = json.loads(Path(prepared["initial_state_path"]).read_text())
    if digest(installed_state) != prepared["initial_state_sha256"]:
        raise ValueError("Prepared snapshot content changed")
    if validate_installed:
        validate_installed(case, installed_state)
    certification_path = prepared.get("visibility_certification_path")
    if certification_path:
        certification = json.loads(Path(certification_path).read_text())
        if not certification.get("certified"):
            raise ValueError("Selector API visibility is not certified; repair and prepare the case again")
    write(environment_out / "initial_state.json", installed_state)
    final_schema = None

    class CampaignClient(BaseClient):
        @serialized_ddl
        def init_env(self, *args, **kwargs):
            nonlocal final_schema
            env = super().init_env(*args, **kwargs)
            try:
                final_schema = environment_schema(engine, env.environmentId, prepared["template_id"])
                actual = export_state(engine, final_schema)
                if digest(actual) != prepared["initial_state_sha256"]:
                    raise ValueError("Solver clone differs from inspected initial state")
            except Exception:
                super().delete_env(envId=env.environmentId)
                raise
            return env

        @serialized_ddl
        def start_run(self, *args, **kwargs):
            return super().start_run(*args, **kwargs)

        @serialized_ddl
        def delete_env(self, *args, **kwargs):
            return super().delete_env(*args, **kwargs)

        @serialized_ddl
        def evaluate_run(self, *, runId, expectedOutput):
            # Baseline already stopped its sandbox before this hook.
            write(environment_out / "final_state.json", export_state(engine, final_schema))
            self.campaign_diff = super().diff_run(runId=runId)
            write(environment_out / "diff_run.json", self.campaign_diff.model_dump(mode="json"))
            return self.campaign_diff

        def get_results_for_run(self, *, runId):
            return self.campaign_diff

    baseline.AgentDiff = CampaignClient  # Local imported module only; no global patch.
    prompt = baseline.official_prompt()
    (out / "system_prompt.txt").write_text(prompt)
    config = {"model": model, "baseline_runner": str(BASELINE),
              "baseline_runner_sha256": hashlib.sha256(BASELINE.read_bytes()).hexdigest(),
              "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
              "turn_limit": 40, "timeout_seconds": 480,
              "max_output_tokens_per_call": options["max_tokens"],
              "temperature": options.get("temperature", "provider_default"),
              "thinking": options.get("thinking", "provider_default"),
              "record_requests": record_requests, "effort": "provider_default",
              "prompt_caching": "explicit_5m", "native_assertions": False,
              "case_sha256": prepared["case_sha256"],
              "cost_source": "baseline runner estimate; not provider-billed dollars",
              "rates_usd_per_million": baseline.RATES}
    write(out / "config.json", config)
    row = {"test_id": case["case_id"], "test_name": case.get("name", case["case_id"]),
           "#": None, "question": case["prompt"],
           "info": json.dumps({"seed_template": prepared["template_name"],
                                "impersonate_user_id": case["acting_user_id"]}),
           "answer": "{}"}
    try:
        record = await baseline.episode(row, args, prompt, out)
        record["campaign"] = {"case_sha256": prepared["case_sha256"],
                              "initial_state": str(environment_out / "initial_state.json"),
                              "final_state": str(environment_out / "final_state.json"),
                              "native_assertions_evaluated": False}
        write(out / (case["case_id"] + ".json"), record)
        if "evaluation" in record:
            prepare_oracle(case, record, environment_out / "initial_state.json", evaluation_inputs)
        return record
    finally:
        engine.dispose()
        cleanup(prepared, database_url)


def prepare_oracle(case, record, initial_state_path, out, docs_path=DOCS):
    """Same bundle contract as oracle_bedrock.prepare, excluding author trace."""
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    write(out / "task.json", {"test_id": case["case_id"], "run_id": record["run_id"],
          "prompt": case["prompt"], "acting_user_id": case["acting_user_id"],
          "seed_template": "campaign_isolated", "termination": record.get("termination"),
          "final_response_recorded": "final" in record})
    write(out / "cards.json", case["cards"])
    write(out / "task_spec.json", case["task_spec"])
    write(out / "initial_state.json", json.loads(Path(initial_state_path).read_text()))
    write(out / "recorded_diff.json", record["evaluation"]["diff"])
    write(out / "response.json", {"final": record["final"]} if "final" in record else {})
    steps = []
    for step in record["steps"]:
        value = {key: step[key] for key in ("turn", "action", "observation") if key in step}
        value["assistant_text"] = [b["text"] for b in step.get("response", {}).get("content", []) if b.get("type") == "text"]
        steps.append(value)
    write(out / "trajectory.json", {"steps": steps, "termination": record.get("termination")})
    docs = json.loads(Path(docs_path).read_text())
    for i, (name, value) in enumerate(docs.items()):
        filename = name if "/" not in name and "\\" not in name and name not in (".", "..") else f"document_{i}"
        write(out / "api_docs" / (filename + ".json"), value)
    write(out / "api_docs/index.json", list(docs))
    write(out / "provenance.json", {"case_sha256": digest(case),
          "initial_state": str(Path(initial_state_path).resolve()), "docs": str(Path(docs_path).resolve()),
          "omitted": "Author traces/validation, coverage targets, native assertions/scores, solver thinking/usage. Actual installed seed supplied."})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["prepare", "run", "cleanup"])
    parser.add_argument("--case", type=Path)
    parser.add_argument("--prepared", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--base-url", default="http://127.0.0.1:18000")
    parser.add_argument("--model", default="us.anthropic.claude-sonnet-5")
    args = parser.parse_args()
    if args.command == "prepare":
        if not args.case or not args.out:
            parser.error("prepare requires --case and --out")
        manifest = prepare(json.loads(args.case.read_text()), args.out, base_url=args.base_url)
        print(json.dumps(manifest))
    elif args.command == "run":
        if not args.case or not args.prepared or not args.out:
            parser.error("run requires --case, --prepared and --out")
        asyncio.run(run_prepared(json.loads(args.case.read_text()), json.loads(args.prepared.read_text()),
                                 args.out, model=args.model))
    else:
        if not args.prepared:
            parser.error("cleanup requires --prepared")
        cleanup(json.loads(args.prepared.read_text()))


if __name__ == "__main__":
    main()
