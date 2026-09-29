"""Run retrieval strategies against the replica and record which matches each one finds (plan.md, method step 1).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_02.strategies [PROBE_ID ...]

A strategy is an ordered list of API calls, some built from earlier responses (the subfolders a listing returned,
the calendars on the calendar list). A strategy "finds" a record when the record's id appears in one of its
responses. For every probe in probes.py: install its seed, open one environment (strategies only read), run every
strategy of its service, and report the targets each one misses. The thorough strategy must find them all, or the
probe is invalid. Writes matrix.json. No model calls; the local replica only.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.parse import quote

from grounding.integrations.agentdiff import custom_runtime, runtime
from grounding.integrations.agentdiff import smoke_runtime as smoke
from grounding.integrations.agentdiff.runtime import ddl_lock, engine_for
from grounding.runs.autogen_01.kit import seedops
from grounding.runs.autogen_01.kit.preflight import perform_write

HERE = Path(__file__).resolve().parent
DB = os.environ.get("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
BASE = os.environ.get("AGENTDIFF_BASE_URL", "http://127.0.0.1:18001")
ID_KEYS = {"id", "ts", "message_id"}


def ids_in(obj) -> set[str]:
    out, stack = set(), [obj]
    while stack:
        x = stack.pop()
        if isinstance(x, dict):
            out |= {str(v) for k, v in x.items() if k in ID_KEYS and isinstance(v, (str, int))}
            stack += list(x.values())
        elif isinstance(x, list):
            stack += x
    return out


class Api:
    """Calls into one environment; keeps every response for the record."""

    def __init__(self, client, env_id, domain):
        self.client, self.env_id, self.domain, self.log = client, env_id, domain, []

    def __call__(self, call: dict):
        status, body = perform_write(self.client, self.env_id, self.domain, call)
        self.log.append({"call": call, "status": status})
        return body if isinstance(body, dict) else {}


# ------------------------------------------------------------------ Box
def box_list(api, fid, limit=None):
    params = {"limit": limit} if limit else {}
    return api({"method": "GET", "path": f"/folders/{fid}/items", "params": params})


def box_tree(api, fid, limit=1000):
    found, queue = set(), [fid]
    while queue:
        f = queue.pop(0)
        body = box_list(api, f, limit)
        found |= ids_in(body)
        queue += [e["id"] for e in body.get("entries", []) if e.get("type") == "folder"]
    return found


def box_list_paged(api, fid, limit=1000):
    """Every page of a folder's listing (offset paging)."""
    found, offset = set(), 0
    while True:
        body = api({"method": "GET", "path": f"/folders/{fid}/items", "params": {"limit": limit, "offset": offset}})
        entries = body.get("entries", [])
        found |= ids_in(entries)
        offset += len(entries)
        if not entries or offset >= int(body.get("total_count", 0)):
            return found


def box_tree_paged(api, fid, limit=1000):
    """Every page of every folder in the tree."""
    found, queue = set(), [fid]
    while queue:
        f, offset = queue.pop(0), 0
        while True:
            body = api({"method": "GET", "path": f"/folders/{f}/items", "params": {"limit": limit, "offset": offset}})
            entries = body.get("entries", [])
            found |= ids_in(entries)
            queue += [x["id"] for x in entries if x.get("type") == "folder"]
            offset += len(entries)
            if not entries or offset >= int(body.get("total_count", 0)):
                break
    return found


def box_search(api, query, **params):
    return api({"method": "GET", "path": "/search", "params": {"query": query, "type": "file", **params}})


# Cycle 8: a request about files anywhere (no folder named). A lazy route lists the folder the request's words
# suggest (e["guess"]); the thorough one walks every folder from the root, or searches when the condition is text.
def box_search_paged(api, query, limit=30):
    found, offset = set(), 0
    while True:
        body = box_search(api, query, limit=limit, offset=offset)
        found |= ids_in(body)
        offset += limit
        if offset >= (body.get("total_count") or 0):
            return found


BOX_ANYWHERE = {
    "list the guessed folder (default page)": (False, lambda api, e: ids_in(box_list(api, e["guess"]))),
    "list the guessed folder (limit 1000)": (False, lambda api, e: ids_in(box_list(api, e["guess"], 1000))),
    "list the guessed folder's tree (limit 1000)": (False, lambda api, e: box_tree(api, e["guess"])),
    "search words (default limit)": (False, lambda api, e: ids_in(box_search(api, e["words"]))),
    # Cycle 8b: the largest search page is a shortcut too; a crowd over 200 hits would be needed to defeat it.
    "search words (limit 200)": (False, lambda api, e: ids_in(box_search(api, e["words"], limit=200))),
    "list every folder from the root, every page [thorough]": (True, lambda api, e: box_tree_paged(api, "0")),
    # The search returns description, size and comment count; the replica's listings return mini fields only.
    "search words, every page [thorough]": (True, lambda api, e: box_search_paged(api, e["words"])),
}


BOX = {
    "list named (default page)": (False, lambda api, e: ids_in(box_list(api, e["folder"]))),
    "list named (limit 1000)": (False, lambda api, e: ids_in(box_list(api, e["folder"], 1000))),
    "search words (default limit)": (False, lambda api, e: ids_in(box_search(api, e["words"]))),
    "search words under folder (limit 200)": (False, lambda api, e: ids_in(box_search(
        api, e["words"], ancestor_folder_ids=e["folder"], limit=200))),
    "search extension under folder (limit 200)": (False, lambda api, e: ids_in(box_search(
        api, e["ext"], file_extensions=e["ext"], ancestor_folder_ids=e["folder"], limit=200))),
    "search person's name under folder (limit 200)": (False, lambda api, e: ids_in(box_search(
        api, e.get("person", "Leo"), ancestor_folder_ids=e["folder"], limit=200))),
    # Cycle 6: a route thorough in one respect only is lazy in the other (the tree, one page per folder; every
    # page, one folder). The thorough route covers both.
    "list tree, one page per folder (limit 1000)": (False, lambda api, e: box_tree(api, e["folder"])),
    "list named, every page (limit 1000)": (False, lambda api, e: box_list_paged(api, e["folder"])),
    "list tree, every page (limit 1000) [thorough]": (True, lambda api, e: box_tree_paged(api, e["folder"])),
}


# ------------------------------------------------------------------ Calendar
def cal_events(api, cal, e, q=None, max_results=None):
    params = {"timeMin": e["from"], "timeMax": e["to"], "singleEvents": "true"}
    if q:
        params["q"] = q
    if max_results:
        params["maxResults"] = max_results
    return api({"method": "GET", "path": f"/calendars/{quote(cal, safe='')}/events", "params": params})


def cal_each(api, e, list_params):
    found = set()
    body = api({"method": "GET", "path": "/users/me/calendarList", "params": list_params})
    for item in body.get("items", []):
        found |= ids_in(cal_events(api, item["id"], e, max_results=2500))
    return found


CALENDAR = {
    "primary only": (False, lambda api, e: ids_in(cal_events(api, "primary", e))),
    "primary, text search": (False, lambda api, e: ids_in(cal_events(api, "primary", e, q=e.get("q")))),
    "calendar list (default) -> each": (False, lambda api, e: cal_each(api, e, {})),
    "calendar list (owner only) -> each": (False, lambda api, e: cal_each(api, e, {"minAccessRole": "owner"})),
    "calendar list (showHidden) -> each [thorough]": (True, lambda api, e: cal_each(api, e, {"showHidden": "true"})),
}


# ------------------------------------------------------------------ Linear
def gql(api, query):
    return api({"graphql": query})


def lin_team_tree(api, e):
    teams = gql(api, "{ teams(first: 250) { nodes { id name parent { id } } } }")
    nodes = (((teams.get("data") or {}).get("teams") or {}).get("nodes")) or []
    root = [t["id"] for t in nodes if t["name"] == e["team"]]
    keep, grew = set(root), True
    while grew:
        grew = False
        for t in nodes:
            if (t.get("parent") or {}).get("id") in keep and t["id"] not in keep:
                keep.add(t["id"])
                grew = True
    ids = ", ".join(f'"{t}"' for t in sorted(keep))
    return ids_in(gql(api, f"{{ issues(first: 250, filter: {{team: {{id: {{in: [{ids}]}}}}}}) {{ nodes {{ id }} }} }}"))


def lin_all_keep(api, e, tree: bool):
    """Retrieve every issue (first 1000), then keep those in the named team, or in its whole tree."""
    teams = gql(api, "{ teams(first: 250) { nodes { id name parent { id } } } }")
    nodes = (((teams.get("data") or {}).get("teams") or {}).get("nodes")) or []
    keep = {t["id"] for t in nodes if t["name"] == e["team"]}
    while tree:
        more = {t["id"] for t in nodes if (t.get("parent") or {}).get("id") in keep} - keep
        if not more:
            break
        keep |= more
    body = gql(api, "{ issues(first: 1000) { nodes { id team { id } } } }")
    issues = (((body.get("data") or {}).get("issues") or {}).get("nodes")) or []
    return {i["id"] for i in issues if (i.get("team") or {}).get("id") in keep}


LINEAR = {
    "all issues (first 1000) -> keep the named team": (False, lambda api, e: lin_all_keep(api, e, False)),
    "all issues (first 1000) -> keep the team tree [thorough]": (True, lambda api, e: lin_all_keep(api, e, True)),
    "all issues (default page)": (False, lambda api, e: ids_in(gql(api, "{ issues { nodes { id } } }"))),
    "all issues (first 250)": (False, lambda api, e: ids_in(gql(api, "{ issues(first: 250) { nodes { id } } }"))),
    "all issues (first 1000)": (False, lambda api, e: ids_in(gql(api, "{ issues(first: 1000) { nodes { id } } }"))),
    "named team's issues (first 250)": (False, lambda api, e: ids_in(gql(
        api, f'{{ issues(first: 250, filter: {{team: {{name: {{eq: "{e["team"]}"}}}}}}) {{ nodes {{ id }} }} }}'))),
    "server filter, all conditions (first 250)": (False, lambda api, e: ids_in(gql(api, e["filtered"]))),
    "team tree's issues (first 250) [thorough]": (True, lin_team_tree),
}


# ------------------------------------------------------------------ Slack
def slk(api, method, **params):
    return api({"slack": method, "params": params})


def slk_hist_paged(api, channel, limit=999):
    """Every page of a channel's history (cursor paging)."""
    found, cursor = set(), None
    while True:
        params = {"channel": channel, "limit": limit}
        if cursor:
            params["cursor"] = cursor
        body = slk(api, "conversations.history", **params)
        found |= ids_in(body.get("messages", []))
        cursor = (body.get("response_metadata") or {}).get("next_cursor")
        if not cursor or not body.get("has_more"):
            return found


def slk_hist_matching(api, e, types, every_page=False, **extra):
    found = set()
    params = {"limit": 1000, **extra}
    if types:
        params["types"] = types
    body = slk(api, "conversations.list", **params)
    for ch in body.get("channels", []):
        if ch.get("name", "").startswith(e["prefix"]):
            found |= slk_hist_paged(api, ch["id"]) if every_page else \
                ids_in(slk(api, "conversations.history", channel=ch["id"], limit=999))
    return found


def slk_channels_with(api, e, types):
    """Channel-level requests: the channels whose topic or purpose contains the words."""
    params = {"limit": 1000}
    if types:
        params["types"] = types
    body = slk(api, "conversations.list", **params)
    words = e["topic"].lower()
    return {ch["id"] for ch in body.get("channels", [])
            if words in ((ch.get("topic") or {}).get("value", "") + " " + (ch.get("purpose") or {}).get("value", "")
                         ).lower()}


def slk_channels_of_hits(api, e):
    body = slk(api, "search.messages", query=e["topic"], count=100)
    return {(m.get("channel") or {}).get("id") for m in ((body.get("messages") or {}).get("matches") or [])}


SLACK = {
    "search words (default count)": (False, lambda api, e: ids_in(slk(api, "search.messages", query=e["search"]))),
    "search words (count 100)": (False, lambda api, e: ids_in(slk(api, "search.messages", query=e["search"],
                                                                   count=100))),
    "named channel history (default)": (False, lambda api, e: ids_in(slk(api, "conversations.history",
                                                                          channel=e["channel"]))),
    "named channel history (limit 999)": (False, lambda api, e: ids_in(slk(api, "conversations.history",
                                                                            channel=e["channel"], limit=999))),
    "channel list (default types) -> history": (False, lambda api, e: slk_hist_matching(api, e, None)),
    "channel list (exclude archived) -> history": (False, lambda api, e: slk_hist_matching(
        api, e, "public_channel,private_channel", exclude_archived="true")),
    # Cycle 6: as for Box, the thorough route covers private channels and every page.
    "channel list (public+private) -> one page of history": (False, lambda api, e: slk_hist_matching(
        api, e, "public_channel,private_channel")),
    "named channel history, every page (limit 999)": (False, lambda api, e: slk_hist_paged(api, e["channel"])),
    "channel list (public+private) -> every page of history [thorough]": (True, lambda api, e: slk_hist_matching(
        api, e, "public_channel,private_channel", every_page=True)),
}
def slk_hist_all(api, types):
    """Every conversation of the given types (all of them, no name filter) -> its history."""
    found = set()
    params = {"limit": 1000}
    if types:
        params["types"] = types
    for ch in slk(api, "conversations.list", **params).get("channels", []):
        found |= ids_in(slk(api, "conversations.history", channel=ch["id"], limit=999))
    return found


SLACK_MESSAGES = {  # a message-level request with no channel scope ("every message Priya posted about …")
    "search words (count 100)": (False, lambda api, e: ids_in(slk(api, "search.messages", query=e["search"],
                                                                   count=100))),
    "conversations (default types) -> history": (False, lambda api, e: slk_hist_all(api, None)),
    "conversations (public+private) -> history": (False, lambda api, e: slk_hist_all(
        api, "public_channel,private_channel")),
    "conversations (all four types) -> history [thorough]": (True, lambda api, e: slk_hist_all(
        api, "public_channel,private_channel,mpim,im")),
}
SLACK_CHANNELS = {
    "search words -> channels of the hits": (False, slk_channels_of_hits),
    "channel list (default types) -> topics": (False, lambda api, e: slk_channels_with(api, e, None)),
    "channel list (public+private) -> topics [thorough]": (True, lambda api, e: slk_channels_with(
        api, e, "public_channel,private_channel")),
}
STRATEGIES = {"box": BOX, "calendar": CALENDAR, "linear": LINEAR, "slack": SLACK, "slack-channels": SLACK_CHANNELS,
              "slack-messages": SLACK_MESSAGES, "box-anywhere": BOX_ANYWHERE}


def run_probe(client, engine, probe) -> dict:
    domain = probe["domain"]
    if "seed_tables" in probe:  # cycle 8: a case's own seed, already table rows
        seed, refs, actor = probe["seed_tables"], {}, probe["actor"]
    else:
        seed, refs, actor = seedops.expand(domain, probe["seed"])
    targets = [str(seedops.resolve(t, refs)) for t in probe["targets"]]
    entry = seedops.resolve(probe["entry"], refs)
    case = {"case_id": f"SM2-{probe['id']}", "domain": domain, "seed": seed, "acting_user_id": actor,
            "references": [], "prompt": "probe"}
    template = runtime.install_template(case, engine) if domain == "slack" else \
        custom_runtime.install_custom_template(domain, seed, engine, case["case_id"])
    result = {"probe": probe["id"], "domain": domain, "place": probe["place"], "targets": targets, "strategies": {}}
    try:
        with ddl_lock():
            env = client.init_env(templateService=domain, templateName=template["template_name"],
                                  impersonateUserId=actor)
        for name, (thorough, run) in STRATEGIES[probe.get("strategies", domain)].items():
            api = Api(client, env.environmentId, domain)
            try:
                found = run(api, entry)
                missed = [t for t in targets if t not in found]
                result["strategies"][name] = {"thorough": thorough, "missed": missed, "calls": len(api.log),
                                              "errors": [c for c in api.log if (c["status"] or 500) >= 400]}
            except Exception as exc:  # recorded; the strategy is reported as failed
                result["strategies"][name] = {"thorough": thorough, "error": f"{type(exc).__name__}: {exc}"[:300]}
        with ddl_lock():
            client.delete_env(envId=env.environmentId)
    finally:
        if domain == "slack":
            runtime.cleanup(template, DB)
        else:
            smoke.cleanup_isolated_template({**template, "service": domain}, DB)
    return result


def main(ids):
    from agent_diff import AgentDiff
    from grounding.runs.several_match_02.probes import PROBES
    client, engine = AgentDiff(base_url=BASE), engine_for(DB)
    out = HERE / "matrix.json"
    results = json.loads(out.read_text()) if out.exists() else {}
    for probe in PROBES:
        if ids and probe["id"] not in ids:
            continue
        r = run_probe(client, engine, probe)
        results[probe["id"]] = r
        print(f"\n== {r['probe']} ({r['domain']}): {r['place']}  targets={len(r['targets'])}")
        for name, s in r["strategies"].items():
            if "error" in s:
                print(f"   {name:48} ERROR {s['error'][:120]}")
            else:
                mark = "MISSES " + str(len(s["missed"])) if s["missed"] else "finds all"
                bad = " <- INVALID PROBE" if s["thorough"] and s["missed"] else ""
                errs = f" ({len(s['errors'])} call errors)" if s["errors"] else ""
                print(f"   {name:48} {mark}{errs}{bad}")
    out.write_text(json.dumps(results, indent=1) + "\n")
    engine.dispose()


if __name__ == "__main__":
    main(set(sys.argv[1:]))
