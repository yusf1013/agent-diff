"""S1's numbers, from checks.json and omissions.json, set beside our automation's (several_match_auto_01/summary.json).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.related_work_01.s1.summary

The comparable measure: of the lazy shortcuts our automation counts as practical to defeat (19 over six request kinds;
the rest are impractical on these replicas or not lazy for the requests), how many Agent-Diff's seeds defeat for at
least one of its plural requests, faithfully (void and not-applicable rows out). Calendar has no cards, so its four
are not checkable here. Writes summary.json.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from grounding.runs.several_match_02 import strategies
from grounding.runs.several_match_auto_01 import checks as _sma  # noqa: F401  (registers slack-channels-any)

REPO = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent


def practical() -> dict[str, list[str]]:
    auto = json.loads((REPO / "grounding/runs/several_match_auto_01/summary.json").read_text())["coverage by request kind"]
    out = {}
    for kind, row in auto.items():
        lazy = [n for n, (thorough, _f) in strategies.STRATEGIES[kind].items() if not thorough]
        out[kind] = [n for n in lazy if not str(row["not defeated"].get(n, "")).startswith(("impractical", "not lazy"))]
    return out


def main():
    checks = json.loads((HERE / "checks.json").read_text())
    counted = {k: v for k, v in checks.items() if v.get("counted")}
    defeated_by = defaultdict(lambda: defaultdict(list))  # kind -> route -> [obligations]
    behaviours = defaultdict(set)  # behaviour -> obligations with a faithful defeat of it
    for key, v in counted.items():
        for route, d in v["defeated"].items():
            defeated_by[v["kind"]][route].append(key)
            behaviours[d["behaviour"]].add(key)
    table = {}
    for kind, routes in practical().items():
        probed = [k for k, v in counted.items() if v["kind"] == kind]
        hit = {r: defeated_by[kind][r] for r in routes if defeated_by[kind].get(r)}
        table[kind] = {"practical shortcuts": len(routes), "probes of this kind": len(probed),
                       "defeated on Agent-Diff's seeds": hit, "count": f"{len(hit)} of {len(routes)}"
                       + ("" if probed else " (no probe of this kind)")}
    om = json.loads((HERE / "omissions.json").read_text())
    out = {
        "probes counted": len(counted), "run, not counted (permissive)": len(checks) - len(counted),
        "obligations with a faithful defeat": sorted({k for ks in behaviours.values() for k in ks}),
        "by behaviour": {b: sorted(ks) for b, ks in sorted(behaviours.items())},
        "void rows": {k: sorted(v["void"]) for k, v in counted.items() if v["void"]},
        "complete routes that missed a target": {k: v["complete_routes_missing"] for k, v in checks.items()
                                                  if v.get("complete_routes_missing")},
        "practical shortcuts, per request kind": table,
        "practical shortcuts defeated (checkable kinds)": (
            sum(len(t["defeated on Agent-Diff's seeds"]) for k, t in table.items() if t["probes of this kind"]),
            sum(t["practical shortcuts"] for k, t in table.items() if t["probes of this kind"])),
        "omissions": {"obligations": len(om), "targets": sum(r["targets"] for r in om),
                      "unnoticed if omitted": sum(r["unnoticed_if_omitted"] for r in om),
                      "noticed by a count only": sum(r["pinned_by_count_only"] for r in om),
                      "obligations with an unnoticed target": sum(r["unnoticed_if_omitted"] > 0 for r in om)},
    }
    (HERE / "summary.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
