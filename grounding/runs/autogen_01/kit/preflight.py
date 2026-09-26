"""Replica pre-checks for a built scenario (no model calls): install, read, observability, write feasibility.

    report, problems = check(case, out_dir, database_url, base_url)

1. Install the seed as a template and open an environment as the acting user.
2. Run read probes: the natural detail and listing reads of every seeded record (derived from the seed), plus the
   writer's own probes. Slack uses the runtime's visibility probes.
3. **Observability:** every decoy's deciding value (the value of the field its mutation changes, read on the decoy
   or on the related record) appears somewhere in the recorded responses. A value that never appears means the
   solver cannot tell the decoy apart, as with the Linear project lead.
4. **Write feasibility:** in a fresh environment, perform the scenario's write call and require that it succeeds and
   changes the target in the effect table (id formats, accepted values, permissions).
Everything is recorded in `out_dir`; the template and environments are removed afterwards.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote

import requests

from grounding.integrations.agentdiff import custom_runtime, runtime
from grounding.integrations.agentdiff import smoke_runtime as smoke
from grounding.integrations.agentdiff.runtime import ddl_lock, engine_for, environment_schema, write
from grounding.runs.fact_coverage_01 import fdc
from grounding.runs.fact_coverage_01.pilot.analyze import changed
from grounding.runs.fact_coverage_01.pilot.variants import PRIMARY_KEYS

BOX_HUB = {"box-version": "2025.0"}
IDENT_FIELDS = ("name", "title", "summary", "login", "email", "identifier", "key", "display_name", "real_name",
                "username", "channel_name", "displayName", "message_text", "body", "message")
LINEAR_PROBES = [
    "{ issues(first: 250) { nodes { id identifier title description priority priorityLabel estimate dueDate createdAt "
    "updatedAt completedAt canceledAt state { name type } team { key name } } } }",
    "{ issues(first: 250) { nodes { identifier assignee { name email displayName } creator { name email displayName } "
    "project { name } projectMilestone { name } cycle { number name } parent { identifier title } } } }",
    "{ issues(first: 250) { nodes { identifier labels { nodes { name parent { name } } } subscribers { nodes { name } } "
    "children { nodes { identifier } } } } }",
    "{ comments(first: 250) { nodes { id body createdAt resolvedAt issue { identifier } user { name } "
    "resolvingUser { name } parent { id } } } }",
    "{ issueRelations(first: 250) { nodes { id type issue { identifier title } relatedIssue { identifier title } } } }",
    "{ attachments(first: 250) { nodes { id title url issue { identifier } creator { name } } } }",
    "{ users { nodes { id name displayName email active admin guest app timezone statusLabel } } }",
    "{ teams { nodes { id name key description private parent { name } members { nodes { name } } "
    "labels { nodes { name isGroup } } } } }",
    "{ issueLabels(first: 250) { nodes { id name isGroup team { name } parent { name } } } }",
    "{ cycles(first: 100) { nodes { id number name startsAt endsAt isActive team { name } } } }",
    "{ searchProjects(term: \"\") { nodes { id name description state priority health startDate targetDate "
    "lead { name } creator { name } } } }",
    "{ projectMilestones(first: 100) { nodes { id name status targetDate project { name } } } }",
    "{ documents(first: 100) { nodes { id title content creator { name } updatedBy { name } project { name } "
    "team { name } initiative { name } } } }",
    "{ initiatives(first: 100) { nodes { id name description status health targetDate owner { name } "
    "creator { name } parentInitiative { name } } } }",
    "{ projectRelations(first: 100) { nodes { id type project { name } relatedProject { name } } } }",
    "{ initiativeToProjects(first: 100) { nodes { id initiative { name } project { name } } } }",
    "{ notifications(first: 100) { nodes { id type title readAt actor { name } } } }",
    "{ organizationInvites(first: 100) { nodes { id email role acceptedAt inviter { name } invitee { name } } } }",
]


def auto_probes(case: dict) -> list:
    seed, domain = case["seed"], case["domain"]
    probes = []
    if domain == "box":
        probes.append(("GET", "/users/me", None))
        for r in seed.get("box_folders", []):
            probes += [("GET", f"/folders/{r['id']}", None), ("GET", f"/folders/{r['id']}/items", None)]
        commented = {r["file_id"] for r in seed.get("box_comments", [])}
        tasked = {r["item_id"] for r in seed.get("box_tasks", [])}
        for r in seed.get("box_files", []):
            probes.append(("GET", f"/files/{r['id']}", None))
            if r["id"] in commented:
                probes.append(("GET", f"/files/{r['id']}/comments", None))
            if r["id"] in tasked:
                probes.append(("GET", f"/files/{r['id']}/tasks", None))
        if seed.get("box_hubs"):
            probes.append(("GET", "/hubs", None, BOX_HUB))
            for r in seed["box_hubs"]:
                probes += [("GET", f"/hubs/{r['id']}", None, BOX_HUB), ("GET", "/hub_items", {"hub_id": r["id"]}, BOX_HUB)]
        if seed.get("box_collections"):
            probes.append(("GET", "/collections", None))
            for r in seed["box_collections"]:
                probes.append(("GET", f"/collections/{r['id']}/items", None))
    elif domain == "calendar":
        window = {"timeMin": "2017-01-01T00:00:00Z", "timeMax": "2020-01-01T00:00:00Z", "maxResults": 2500}
        probes.append(("GET", "/users/me/calendarList", None))
        for r in seed.get("calendars", []):
            cid = quote(r["id"], safe="@")
            probes += [("GET", f"/calendars/{cid}", None), ("GET", f"/calendars/{cid}/events", window),
                       ("GET", f"/calendars/{cid}/acl", None)]
        for r in seed.get("calendar_events", []):
            if r.get("recurrence"):
                probes.append(("GET", f"/calendars/{quote(r['calendar_id'], safe='@')}/events/{r['id']}/instances",
                               window))
    elif domain == "linear":
        probes += [("POST", "/graphql", {"query": q}) for q in LINEAR_PROBES]
    return probes


def run_reads(client, env_id, service, probes):
    """Like custom_runtime.run_probes, but GraphQL errors are kept as data (a probe's failure is not fatal)."""
    base = custom_runtime.service_url(client.base_url, env_id, service)
    out = []
    for probe in probes:
        method, path, payload = probe[:3]
        headers = {**client._headers(), **(probe[3] if len(probe) > 3 else {})}
        try:
            if method == "GET":
                resp = requests.get(base + path, params=payload, headers=headers, timeout=60)
            else:
                resp = requests.post(base + path, json=payload, headers=headers, timeout=60)
            try:
                body = resp.json()
            except ValueError:
                body = {"non_json_response": resp.text[:4000]}
            out.append({"method": method, "path": path, "payload": payload, "status": resp.status_code, "body": body})
        except Exception as exc:  # recorded
            out.append({"method": method, "path": path, "payload": payload, "status": None,
                        "error": f"{type(exc).__name__}: {exc}"})
    return out


# -- observability ---------------------------------------------------------------------------------------------
def _reach(seed, table, rows, path_edges):
    """Rows reached from `rows` of `table` by following the join of each edge in order."""
    current, current_table = rows, table
    for edge in path_edges:
        child_table = edge["node"]["table"]
        join = edge.get("join")
        if join is None:
            return [], child_table
        nxt = []
        for r in current:
            nxt += fdc._joined(seed, current_table, r, edge)
        current, current_table = nxt, child_table
    return current, current_table


def _path_to(node, key, path=()):
    """(edges from the root to the node holding `key`, what it is: ('filter', f) or ('edge', e))."""
    for f in node.get("filters", []):
        if f.get("key") == key:
            return list(path), ("filter", f)
    for e in node.get("edges", []):
        if e.get("key") == key:
            return list(path), ("edge", e)
        found = _path_to(e["node"], key, path + (e,))
        if found:
            return found
    return None


def _render(value, field=None):
    if value is None or isinstance(value, bool):
        return []
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    if isinstance(value, (int, float)):
        return [str(value)]
    if isinstance(value, str):
        m = re.match(r"^(\d{4}-\d{2}-\d{2})[T ]", value)
        return [m.group(1)] if m else [value]
    return []


def deciding_values(case: dict, claim: dict) -> list[list[str]]:
    """For one decoy: groups of strings, each group satisfied when any member appears in the responses."""
    seed, domain = case["seed"], case["domain"]
    ref = next(r for r in case["references"] if claim in r["claims"])
    query = ref["query"]
    table = query["table"]
    key = query.get("key", ["id"])[0]
    root = [r for r in seed.get(table, []) if str(r.get(key)) == str(claim["witness"])]
    groups = [[str(claim["witness"])] + [str(root[0][f]) for f in ("identifier", "ts") if root and root[0].get(f)]]
    mutation = claim["mutation"]
    if mutation["type"] == "REPLACE" and root:
        # Added after the main runs (report §7): the root filters of the original query that the decoy fails
        # hold its deciding values. The check is a text search over every response, so it cannot verify flags
        # (true/false appear everywhere); a flag the API reports differently (a group DM shown as private) still
        # needs a per-record check.
        for f in query.get("filters", []):
            if not fdc.compare(fdc.get_field(root[0], f["field"]), f["op"], f.get("value")):
                vals = _render(fdc.get_field(root[0], f["field"]), f["field"])
                if vals:
                    groups.append(vals)
        return groups
    if mutation["type"] not in ("DROP", "SUB", "SPLIT") or not root:
        return groups
    found = _path_to(query, mutation["target"])
    if not found:
        return groups
    edges, (kind, item) = found
    rows, t = _reach(seed, table, root, edges)
    if kind == "filter":
        field = item["field"]
        if domain == "slack" and t == "messages" and field == "created_at":
            vals = [str(r.get("ts")) for r in rows]
        else:
            vals = [v for r in rows for v in _render(fdc.get_field(r, field), field)]
        if vals:
            groups.append(sorted(set(vals)))
    else:  # an edge: what the decoy is related to through the original join
        related, _ = _reach(seed, t, rows, [item])
        vals = [str(r[f]) for r in related for f in IDENT_FIELDS if isinstance(r.get(f), str) and len(r[f]) >= 2]
        if related and vals:
            groups.append(sorted(set(vals)))
    return groups


def observability(case: dict, responses_text: str) -> tuple[list, list]:
    text = responses_text.casefold()
    rows, problems = [], []
    for ref in case["references"]:
        for claim in ref["claims"]:
            groups = deciding_values(case, claim)
            missing = [g for g in groups if not any(v.casefold() in text for v in g)]
            rows.append({"witness": claim["witness"], "fact": claim["requirement"], "groups": groups,
                         "missing": missing})
            if missing:
                problems.append(f"Observability: for the decoy `{claim['witness']}` ({claim['requirement']}), none of "
                                f"{missing} appears in any read of the replica, so the solver cannot see what sets "
                                "it apart. Use a field the API returns, or a record the reads show.")
    return rows, problems


# -- write feasibility -----------------------------------------------------------------------------------------
def perform_write(client, env_id, service, call):
    if service == "slack":
        url = f"{client.base_url}/api/env/{env_id}/services/slack/{call['slack']}"
        resp = requests.post(url, data=call.get("params", {}), headers=client._headers(), timeout=60)
    elif service == "linear" or "graphql" in call:
        base = custom_runtime.service_url(client.base_url, env_id, service)
        resp = requests.post(base + "/graphql", json={"query": call["graphql"], "variables": call.get("variables", {})},
                             headers=client._headers(), timeout=60)
    else:
        base = custom_runtime.service_url(client.base_url, env_id, service)
        headers = {**client._headers(), **(call.get("headers") or {})}
        resp = requests.request(call["method"], base + call["path"], params=call.get("params"),
                                json=call.get("body"), headers=headers, timeout=60)
    try:
        body = resp.json()
    except ValueError:
        body = {"non_json_response": resp.text[:4000]}
    return resp.status_code, body


def _write_ok(status, body, service):
    if status is None or status >= 400:
        return False
    if isinstance(body, dict):
        if body.get("errors"):
            return False
        if service == "slack" and body.get("ok") is False:
            return False
    return True


def check(case: dict, out: Path, database_url: str, base_url: str) -> tuple[dict, list[str]]:
    from agent_diff import AgentDiff
    service = case["domain"]
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    engine = engine_for(database_url)
    client = AgentDiff(base_url=base_url)
    template, envs = None, []
    report, problems = {"case_id": case["case_id"]}, []
    try:
        if service == "slack":
            metadata = runtime.dependencies()[1]
            template = runtime.install_template(case, engine)
        else:
            metadata = smoke.load_seed_module(service).Base.metadata
            template = custom_runtime.install_custom_template(service, case["seed"], engine, case["case_id"])

        def open_env():
            with ddl_lock():
                env = client.init_env(templateService=service, templateName=template["template_name"],
                                      impersonateUserId=case["acting_user_id"])
            envs.append(env)
            schema = environment_schema(engine, env.environmentId, template["template_id"])
            state = runtime.export_state(engine, schema) if service == "slack" else \
                smoke.export_state(engine, schema, metadata)
            return env, schema, state

        env, schema, state = open_env()
        if service == "slack":
            vis = runtime.probe_environment(client, env.environmentId, case, state)
            write(out / "visibility.json", vis)
            reads = [page for item in vis["probes"] for page in item["pages"]]
            read_errors = [e for item in vis["probes"] for e in item["errors"]]
        else:
            auto = run_reads(client, env.environmentId, service, auto_probes(case))
            own = run_reads(client, env.environmentId, service, [tuple(p) for p in case.get("probes", [])])
            reads = [{**r, "source": "auto"} for r in auto] + [{**r, "source": "writer"} for r in own]
            write(out / "reads.json", reads)

            def failed(r):
                return r.get("status") is None or r["status"] >= 400 or (
                    isinstance(r.get("body"), dict) and bool(r["body"].get("errors")))

            def describe(r):
                errs = r.get("body", {}).get("errors") if isinstance(r.get("body"), dict) else r.get("error")
                return (f"{r['method']} {r['path']} {json.dumps(r.get('payload'))[:160]} -> {r.get('status')} "
                        f"{json.dumps(errs)[:240]}")
            read_errors = [describe(r) for r in reads if failed(r)]
            problems += [f"Your probe failed: {describe(r)}" for r in reads if r["source"] == "writer" and failed(r)]
        report["read_errors"] = read_errors
        text = json.dumps(reads, ensure_ascii=False, default=str)
        report["observability"], obs_problems = observability(case, text)
        problems += obs_problems
        # write feasibility, in a fresh environment
        call = case.get("write_check") or {}
        env2, schema2, before = open_env()
        if call:
            status, body = perform_write(client, env2.environmentId, service, call)
            after = runtime.export_state(engine, schema2) if service == "slack" else \
                smoke.export_state(engine, schema2, metadata)
            ref = case["references"][0]
            effect = ref.get("effect") or {}
            key = effect.get("key") or ([PRIMARY_KEYS.get(service, {}).get(effect.get("table"), "id")])
            ch = changed(before, after, effect.get("table"), key, effect.get("field"), effect.get("columns")) \
                if effect.get("table") else {"insert": set(), "delete": set(), "update": set()}
            acted = set().union(*[ch[k] for k in effect.get("changes", ["insert", "delete", "update"])])
            targets = {str(x) for x in ref["expected"]}
            report["write"] = {"call": call, "status": status, "body": body if len(json.dumps(body)) < 6000 else
                               json.dumps(body)[:6000], "acted": sorted(acted), "targets": sorted(targets)}
            if not _write_ok(status, body, service) and not targets & acted:
                problems.append(f"Write feasibility: the write call failed on the replica (HTTP {status}): "
                                f"{json.dumps(body)[:600]}")
            elif not _write_ok(status, body, service):
                report.setdefault("warnings", []).append(
                    f"The write changed the target but the replica answered with an error (HTTP {status}): "
                    f"{json.dumps(body)[:300]}")
            elif not targets & acted:
                problems.append(f"Write feasibility: the write call succeeded but did not change the target in "
                                f"`{effect.get('table')}` as the effect locator expects (changed: {sorted(acted)[:5]}).")
            elif acted - targets:
                problems.append(f"Write feasibility: the write changed records other than the target: "
                                f"{sorted(acted - targets)[:5]}.")
        else:
            problems.append("Write feasibility: the scenario has no write call.")
    except Exception as exc:
        problems.append(f"Replica install or read failed: {type(exc).__name__}: {str(exc)[:800]}")
    finally:
        for env in envs:
            try:
                with ddl_lock():
                    client.delete_env(envId=env.environmentId)
            except Exception as exc:  # recorded
                report.setdefault("cleanup_errors", []).append(str(exc)[:300])
        if template:
            try:
                if service == "slack":
                    runtime.cleanup(template, database_url)
                else:
                    smoke.cleanup_isolated_template({**template, "service": service}, database_url)
            except Exception as exc:
                report.setdefault("cleanup_errors", []).append(str(exc)[:300])
        engine.dispose()
    report["problems"] = problems
    write(out / "preflight.json", report)
    return report, problems
