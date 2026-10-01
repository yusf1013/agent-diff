"""Two things the PI asked on 2026-10-01 (afternoon). No model calls.

1. **The single-decoy denominator.** The catalog names each fact's designated alternatives (the lures: a sibling
   field, an indirection, a direction, ...). One single-decoy probe per (fact, designated alternative) is a fixed
   number: 286 over the 213 servable facts (a fact with no named alternative gets one plain-difference probe; a
   hierarchy, binding or derived fact has its one lure in its kind). Against it: the valid single-decoy probes of
   the adopted set (the Muse pipeline's designated scenario per fact), counted per fact and capped at the fact's
   prescribed number, since a decoy is not labelled with the catalog alternative it realizes.
2. **Why the derivation dropped the packed probes** of a hub item's file (G4-BOX-17) and a message's reactions
   (G4-SLK-16), and the probe of a comment's file (G4-BOX-13): the witness check's own messages, recomputed.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.denominator_01.kit.single_decoy
"""
from __future__ import annotations

import copy
import json
from collections import Counter, defaultdict
from pathlib import Path

import grounding.runs.regen_01.rules  # noqa: F401
from grounding.runs.autogen_01.kit import derive
from grounding.runs.openclaw_eval_01 import rulings
from grounding.runs.report_01.kit.common import DOMAINS, RUNS, catalog, fact_id, load, replica_gaps

HERE = Path(__file__).resolve().parents[1]
SUITES = [(RUNS / "openclaw_eval_01/suite/suite.json", RUNS / "openclaw_eval_01/suite/cases"),
          (RUNS / "completion_01/suite/cases/suite.json", RUNS / "completion_01/suite/cases"),
          (RUNS / "regen_01/runs/full_01_cases/suite.json", RUNS / "regen_01/runs/full_01_cases")]
CAT = catalog()


def base_fact(d, f):
    f = fact_id(d, f)
    if f in CAT[d]:
        return f
    parts = f.split(":")
    return ":".join(parts[:2]) if len(parts) > 2 else f


def prescribed(d, f):
    r = CAT[d][f]
    if r["kind"] in "HBD":
        return 1
    n = len(r.get("alternatives") or []) + len(r.get("sibling_alternatives") or [])
    return n or 1


def main():
    gaps = replica_gaps()
    servable = {(d, f) for d in DOMAINS for f in CAT[d] if f not in set(gaps[d])}
    filling = load(HERE / "numbers/filling.json")["final+retry"]
    des_scenario = {k.split(" ", 2)[2]: v for k, v in filling["designated_tests"].items() if k.startswith("probe ")}
    chosen = set(des_scenario.values())
    # valid single-decoy probes per (scenario, fact), and the cover's valid decoys
    singles = defaultdict(set)
    for index, folder in SUITES:
        doc = load(index)
        for m in (doc["tests"] if isinstance(doc, dict) else doc):
            if isinstance(m, str) or m["form"] != "probe" or m["scenario"] not in chosen:
                continue
            case = load(folder / m["domain"] / f"{m['case_id']}.json")
            if rulings.test_exclusion(case):
                continue
            bad = rulings.flawed(rulings.scenario_of(case["case_id"]))
            for ref in case["references"]:
                for c in ref.get("claims", []):
                    if str(c["witness"]) not in bad:
                        singles[(m["scenario"], base_fact(case["domain"], c["requirement"]))].add(str(c["witness"]))
    per_domain = {d: {"prescribed": 0, "built_valid": 0, "filled_capped": 0, "facts": 0} for d in DOMAINS}
    for (d, f) in sorted(servable):
        n = prescribed(d, f)
        sid = des_scenario.get(f)
        built = len(singles.get((sid, f), set())) if sid else 0
        per_domain[d]["prescribed"] += n
        per_domain[d]["built_valid"] += built
        per_domain[d]["filled_capped"] += min(built, n)
        per_domain[d]["facts"] += 1
    tot = {k: sum(v[k] for v in per_domain.values()) for k in ("prescribed", "built_valid", "filled_capped", "facts")}
    print("single-decoy probes, per service: prescribed (fact x designated alternative) | built and valid in the designated scenario | filled, capped per fact")
    for d in DOMAINS:
        v = per_domain[d]; print(f"  {d}: {v['prescribed']} | {v['built_valid']} | {v['filled_capped']}")
    print("  all:", tot)

    # 2. the derivation's own reasons for the dropped probes
    folders = [RUNS / "regen_01/suite/cases", RUNS / "completion_01/suite/cases", RUNS / "openclaw_eval_01/suite/cases"]
    reasons = {}
    for sid in ("G4-BOX-17", "G4-SLK-16", "G4-BOX-13", "G4-LIN-01"):
        for f in folders:
            hits = list(f.glob(f"*/{sid}.json"))
            if hits:
                case = load(hits[0])
                out = derive.suite_with_dropped(copy.deepcopy(case)) if hasattr(derive, "suite_with_dropped") else None
                if out is None:
                    reasons[sid] = "derive.suite_with_dropped not found"
                    break
                dropped = out[1] if isinstance(out, tuple) else out.get("dropped", out)
                reasons[sid] = [{"case_id": test.get("case_id"), "form": meta.get("form"), "fact": meta.get("fact"),
                                 "errors": meta.get("errors")} for test, meta in dropped]
                break
    for sid, r in reasons.items():
        print(f"\n{sid}:")
        print("  ", json.dumps(r, default=str)[:1500])
    (HERE / "numbers/single_decoy.json").write_text(json.dumps({"per_domain": per_domain, "total": tot, "dropped_probe_reasons": reasons}, indent=1, default=str) + "\n")


if __name__ == "__main__":
    main()
