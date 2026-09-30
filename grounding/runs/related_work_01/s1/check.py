"""S1: our several-match shortcut check, run on Agent-Diff's own plural requests and their shared seeds.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.related_work_01.s1.check [TEST ...]

For each included plural obligation (the cards' referent set is the target set): the route table of its kind of
request (several_match_02/strategies.py, with several_match_auto_01's channel table), run as API calls on a fresh
environment of the service's shared seed. A lazy route that misses a target is defeated; the thorough route must find
every target. Routes whose parameter the request does not supply (a person's name, search words) are recorded as not
applicable, not as defeated. No model calls. Writes checks.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.several_match_02 import strategies
from grounding.runs.several_match_auto_01 import checks as sma_checks  # noqa: F401  (registers slack-channels-any)

REPO = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent
SEEDS = {"slack": "examples/slack/seeds/slack_bench_v2.json", "box": "examples/box/seeds/box_default.json",
         "linear": "examples/linear/seeds/linear_expanded.json"}
ACTOR = {"slack": "U01AGENBOT9", "box": "27512847635", "linear": "2790a7ee-fde0-4537-9588-e233aa5a68d1"}

from grounding.runs.related_work_01.s1.probes import LEFT_OUT, PROBES, SAME_AS  # noqa: E402,F401

NEEDS = {"search": "search", "words": "words", "ext": "ext"}


def entry_for(service, kind, params, seed, targets):
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
        name = params["team"]
        return {"team": name, "filtered":
                f'{{ issues(first: 250, filter: {{team: {{name: {{eq: "{name}"}}}}}}) {{ nodes {{ id }} }} }}'}
    raise ValueError(kind)


def not_applicable(kind, route, params):
    """Routes that need a parameter the request does not give."""
    if "person" in route:
        return "the request names no person"
    if "search" in route and not (params.get("search") or params.get("words")):
        return "the request gives no search words"
    if "extension" in route and not params.get("ext"):
        return "the request names no extension"
    return None


def main(only):
    from agent_diff import AgentDiff
    client, engine = AgentDiff(base_url=sma_checks.BASE), strategies.engine_for(sma_checks.DB)
    out_path = HERE / "checks.json"
    done = json.loads(out_path.read_text()) if out_path.exists() else {}
    for tid, oi, kind, params in PROBES:
        if only and tid not in only:
            continue
        service = tid.split("_")[0]
        seed = json.loads((REPO / SEEDS[service]).read_text())
        card = next(t for t in json.loads((REPO / f"grounding/domains/{service}/analysis/analysis.json").read_text())
                    if t["test_id"] == tid)["obligations"][oi - 1]["card"]
        targets = [str(t) for t in card["Referent set"]]
        entry = entry_for(service, kind, params, seed, targets)
        probe = {"id": f"S1-{tid}-O{oi}", "domain": service, "place": "Agent-Diff's shared seed",
                 "seed_tables": seed, "actor": ACTOR[service], "targets": targets, "entry": entry, "strategies": kind}
        try:
            r = strategies.run_probe(client, engine, probe)
        except Exception as exc:  # recorded: the probe could not run
            done[f"{tid} O{oi}"] = {"error": f"{type(exc).__name__}: {exc}"[:400]}
            print(tid, "ERROR", done[f"{tid} O{oi}"]["error"][:200])
            out_path.write_text(json.dumps(done, indent=1, default=str) + "\n")
            continue
        s = r["strategies"]
        na = {n: why for n in s if (why := not_applicable(kind, n, params))}
        lazy = {n: v for n, v in s.items() if not v.get("thorough") and n not in na}
        done[f"{tid} O{oi}"] = {
            "kind": kind, "params": params, "targets": len(targets),
            "thorough_finds_all": any(not v.get("missed") and "error" not in v for v in s.values() if v.get("thorough")),
            "defeated": sorted(n for n, v in lazy.items() if v.get("missed")),
            "not_defeated": sorted(n for n, v in lazy.items() if not v.get("missed") and "error" not in v),
            "not_applicable": na, "errors": sorted(n for n, v in s.items() if "error" in v),
            "missed_by_route": {n: len(v.get("missed", [])) for n, v in s.items() if "error" not in v}}
        out_path.write_text(json.dumps(done, indent=1, default=str) + "\n")
        d = done[f"{tid} O{oi}"]
        print(f"{tid:<10} O{oi} {kind:<18} targets={len(targets):<3} thorough={d['thorough_finds_all']} "
              f"defeated={d['defeated']} errors={d['errors']}")
    engine.dispose()


if __name__ == "__main__":
    main(set(sys.argv[1:]))
