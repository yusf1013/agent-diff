"""RQ3: the generator's funnel per writer, from the suites. Scenarios, near misses (a cover's claims) and the ones
the PI's rulings find flawed, regular tests derived by form, tests the derivation's witness check dropped, tests the
rulings leave out, valid tests; per writer, the facts its valid tests cover.

The steps before the suite (briefs, acceptance, manual validity review) are in the generation studies' reports and
are quoted by the report with their sources; this script counts what the suites hold.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.generator

Writes numbers/generator.json.
"""
from __future__ import annotations

from collections import Counter, defaultdict

from grounding.runs.openclaw_eval_01 import rulings
from grounding.runs.report_01.kit.common import RUNS, WRITER_ORDER, WRITERS, load, suite_tests, write


def main():
    stats = defaultdict(Counter)
    scenarios = defaultdict(set)
    left_out = defaultdict(list)
    for m, case in suite_tests():
        w = WRITERS[m["source"]]
        sid = rulings.scenario_of(case["case_id"])
        scenarios[w].add(sid)
        stats[w][f"kept {m['form']}"] += 1
        why = rulings.test_exclusion(case)
        if why:
            stats[w]["left out"] += 1
            stats[w][f"left out {m['form']}"] += 1
            left_out[w].append({"case_id": case["case_id"], "why": why})
        if m["form"] == "cover":
            bad = rulings.flawed(sid)
            for ref in case["references"]:
                for c in ref.get("claims", []):
                    stats[w]["near misses"] += 1
                    stats[w]["flawed near misses"] += str(c["witness"]) in bad
    for d in load(RUNS / "openclaw_eval_01/suite/suite_dropped.json"):
        stats[WRITERS[d["source"]]]["dropped"] += 1
        stats[WRITERS[d["source"]]][f"dropped {d['form']}"] += 1
    for cid in load(RUNS / "completion_01/suite/check.json")["dropped"]:
        stats["Muse 6b"]["dropped"] += 1
        stats["Muse 6b"]["dropped " + ("fact probe" if cid.startswith("FP-") else "probe")] += 1

    out = {}
    for w in WRITER_ORDER:
        s = stats[w]
        kept = {f: s[f"kept {f}"] for f in ("cover", "probe", "fact probe")}
        derived = {f: kept[f] + s[f"dropped {f}"] for f in kept}
        out[w] = {"scenarios": len(scenarios[w]), "near_misses": s["near misses"],
                  "flawed_near_misses": s["flawed near misses"], "derived": derived,
                  "derived_total": sum(derived.values()), "dropped_by_witness_check": s["dropped"],
                  "left_out_by_rulings": s["left out"],
                  "valid": {f: kept[f] - s[f"left out {f}"] for f in kept},
                  "valid_total": sum(kept.values()) - s["left out"], "left_out": left_out[w]}
    out["all"] = {k: sum(out[w][k] for w in WRITER_ORDER)
                  for k in ("scenarios", "near_misses", "flawed_near_misses", "derived_total",
                            "dropped_by_witness_check", "left_out_by_rulings", "valid_total")}
    print(write("generator", out))
    for w, r in out.items():
        print(w, {k: v for k, v in r.items() if k != "left_out"})


if __name__ == "__main__":
    main()
