"""S1: our several-match shortcut check, run on Agent-Diff's own plural requests and their shared seeds.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.related_work_01.s1.check [TEST ...]

For each probe (probes.py: an obligation whose request needs every one of the cards' referent set): the route table
of its kind of request (several_match_02/strategies.py, with several_match_auto_01's channel table), run as API calls
on a fresh environment of the service's shared seed. A lazy route that misses a target is defeated; a complete route
must find every target. Each route carries its behaviour (scope, pages, visibility, filter, selection) from
several_match_02/route_table.py. Routes whose parameter the request does not give are not applicable; search rows the
replica cannot decide are void (probes.VOID_SEARCH). No model calls. Writes checks.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.several_match_02 import route_table, strategies
from grounding.runs.several_match_auto_01 import checks as sma_checks  # noqa: F401  (registers slack-channels-any)
from grounding.runs.related_work_01.s1.probes import PERMISSIVE, PROBES, VOID_SEARCH

REPO = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent
SEEDS = {"slack": "examples/slack/seeds/slack_bench_v2.json", "box": "examples/box/seeds/box_default.json",
         "linear": "examples/linear/seeds/linear_expanded.json"}
ACTOR = {"slack": "U01AGENBOT9", "box": "27512847635", "linear": "2790a7ee-fde0-4537-9588-e233aa5a68d1"}
# Routes of the "anywhere" and "channels" tables, which route_table.ALIAS does not list, with the behaviour they are.
LOCAL_BEHAVIOUR = {
    ("box", "list the guessed folder (default page)"): "scope",
    ("box", "list the guessed folder (limit 1000)"): "scope",
    ("box", "list the guessed folder's tree (limit 1000)"): "scope",
    ("box", "search words (limit 200)"): "filter",
    ("slack", "channel list (default types)"): "visibility",
    # the table's complete Linear routes, which read a named team's tree: a guess when the request names no team
    ("linear", "all issues (first 1000) -> keep the team tree [thorough]"): "selection",
    ("linear", "team tree's issues (first 250) [thorough]"): "scope",
}
LINEAR_TEAM_ROUTES = {"named team's issues (first 250)", "all issues (first 1000) -> keep the named team",
                      "all issues (first 1000) -> keep the team tree [thorough]",
                      "team tree's issues (first 250) [thorough]"}


def behaviour(service: str, route: str) -> str:
    generated = {name: b for b, name in route_table.generate(service)}
    alias = route_table.ALIAS.get((service, route))
    return generated.get(alias) or LOCAL_BEHAVIOUR.get((service, route), "?")


def entry_for(kind, params, seed, targets):
    if kind == "slack":
        ch = next(c for c in seed["channels"] if c["channel_name"] == params["channel"])
        return {"prefix": ch["channel_name"], "channel": ch["channel_id"], "search": params["search"] or ""}
    if kind in ("slack-messages", "slack-channels-any"):
        return {"search": params["search"] or ""}
    if kind == "box":
        folders = [f for f in seed["box_folders"] if f["name"] == params["folder"]]
        assert len(folders) == 1, (params["folder"], len(folders))
        return {"folder": folders[0]["id"], "words": params["words"] or "", "ext": params["ext"] or "",
                "person": ""}
    if kind == "box-anywhere":
        first = next(f for f in seed["box_files"] if f["id"] == targets[0])
        return {"folder": "0", "guess": first["parent_id"], "words": params["words"] or "", "ext": params["ext"] or ""}
    if kind == "linear":
        return {"team": params["team"],
                "filtered": f'{{ issues(first: 250, filter: {{{params["filter"]}}}) {{ nodes {{ id }} }} }}'}
    raise ValueError(kind)


def not_applicable(kind, route, params):
    """Routes that need a parameter the request does not give (the extension and person checks come first: their
    names also contain "search")."""
    if "person" in route:
        return "the request names no person"
    if "extension" in route:
        return None if params.get("ext") else "the request names no extension"
    if "search" in route and not (params.get("search") or params.get("words")):
        return "the request gives no search words"
    return None


def alternatives(params):
    """One parameter set per alternative the request names (a list-valued parameter), for combining the hits."""
    listed = [k for k, v in params.items() if isinstance(v, list)]
    assert len(listed) <= 1, params
    if not listed:
        return [params]
    return [{**params, listed[0]: v} for v in params[listed[0]]]


def run_one(client, engine, tid, oi, kind, params):
    service = tid.split("_")[0]
    seed = json.loads((REPO / SEEDS[service]).read_text())
    card = next(t for t in json.loads((REPO / f"grounding/domains/{service}/analysis/analysis.json").read_text())
                if t["test_id"] == tid)["obligations"][oi - 1]["card"]
    targets = [str(t) for t in card["Referent set"]]
    missed = {}
    for alt in alternatives(params):  # a target is missed only if every alternative's run misses it
        probe = {"id": f"S1-{tid}-O{oi}", "domain": service, "place": "Agent-Diff's shared seed",
                 "seed_tables": seed, "actor": ACTOR[service], "targets": targets,
                 "entry": entry_for(kind, alt, seed, targets), "strategies": kind}
        r = strategies.run_probe(client, engine, probe)
        for name, v in r["strategies"].items():
            got = {"thorough": v["thorough"], "error": v.get("error"), "missed": set(v.get("missed", []))}
            if name in missed:
                missed[name]["missed"] &= got["missed"]
                missed[name]["error"] = missed[name]["error"] or got["error"]
            else:
                missed[name] = got
    return service, targets, missed


def summarize(service, kind, params, targets, routes, tid):
    na = {n: why for n in routes if (why := not_applicable(kind, n, params))}
    void = {n: VOID_SEARCH[tid] for n in routes if tid in VOID_SEARCH and "search" in n and n not in na}
    guessed_team = kind == "linear" and params.get("team_named") is False
    complete = {n for n, v in routes.items() if v["thorough"]}
    if guessed_team:  # the table's complete routes assume a named team; this request names none
        complete = {"all issues (first 1000)"}
    labels = {n: behaviour(service, n) + (" (guessed team)" if guessed_team and n in LINEAR_TEAM_ROUTES else "")
              for n in routes}
    counted = {n: v for n, v in routes.items() if n not in na and n not in void and not v["error"]}
    lazy = {n: v for n, v in counted.items() if n not in complete}
    return {
        "kind": kind, "params": params, "targets": len(targets),
        "complete_routes": sorted(complete),
        "complete_finds_all": any(not counted[n]["missed"] for n in complete if n in counted),
        "complete_routes_missing": {n: len(routes[n]["missed"]) for n in complete if routes[n]["missed"]},
        "defeated": {n: {"behaviour": labels[n], "missed": len(v["missed"])} for n, v in lazy.items() if v["missed"]},
        "not_defeated": {n: labels[n] for n, v in lazy.items() if not v["missed"]},
        "not_applicable": na, "void": void, "errors": sorted(n for n, v in routes.items() if v["error"]),
        "missed_by_route": {n: len(v["missed"]) for n, v in routes.items() if not v["error"]},
        "missed_ids": {n: sorted(v["missed"]) for n, v in routes.items() if v["missed"] and not v["error"]}}


def main(only):
    from agent_diff import AgentDiff
    client, engine = AgentDiff(base_url=sma_checks.BASE), strategies.engine_for(sma_checks.DB)
    out_path = HERE / "checks.json"
    done = json.loads(out_path.read_text()) if out_path.exists() else {}
    for counted, rows in ((True, PROBES), (False, PERMISSIVE)):
        for tid, oi, kind, params in rows:
            if only and tid not in only:
                continue
            key = f"{tid} O{oi}"
            try:
                service, targets, routes = run_one(client, engine, tid, oi, kind, params)
            except Exception as exc:  # recorded: the probe could not run
                done[key] = {"error": f"{type(exc).__name__}: {exc}"[:400]}
                print(tid, "ERROR", done[key]["error"][:200])
                out_path.write_text(json.dumps(done, indent=1, default=str) + "\n")
                continue
            done[key] = {"counted": counted, **summarize(service, kind, params, targets, routes, tid)}
            out_path.write_text(json.dumps(done, indent=1, default=str) + "\n")
            d = done[key]
            print(f"{tid:<10} O{oi} {kind:<18} targets={len(targets):<3} complete={d['complete_finds_all']} "
                  f"defeated={ {n: v['behaviour'] for n, v in d['defeated'].items()} } void={sorted(d['void'])} "
                  f"errors={d['errors']}")
    engine.dispose()


if __name__ == "__main__":
    main(set(sys.argv[1:]))
