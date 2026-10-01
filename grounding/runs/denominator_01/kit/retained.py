"""Every valid test on record, sorted into the denominator's forms (the adopted set) or the remaining kinds, with what
each agent's runs gave on it: tests run, tests with a failure, and the facts exposed (regular) or the failing trials
(policy). The PI's question of 2026-10-01: how many failures the denominator retains and how many it excludes.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.denominator_01.kit.retained

Regular tests: a test "with a failure" exposes a fact in some trial (the adjudicated lists, rulings and budget
applied). Policy units: a unit with a failing trial (judge v2's incorrect or presented, or a trial over the budget).
Boundary: the elements with a failing trial in the automated boundary study's round 1 (the bare toy loop on the
self-hosted Qwen; no agent-under-test run). Writes numbers/retained.json.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import grounding.runs.regen_01.rules  # noqa: F401
from grounding.runs.autogen_02.kit import sampler
from grounding.runs.denominator_01.kit.outcomes import (QWEN_REGEN_POLICY, QWEN_SCORES, SOL_POLICY, SOL_SCORES, SUITES,
                                                       base_fact, scores)
from grounding.runs.denominator_01.kit.single_decoy import prescribed
from grounding.runs.openclaw_eval_01 import policy, rulings
from grounding.runs.report_01.kit.common import RUNS, load
from grounding.runs.sol_eval_01.kit import policy as solpolicy

HERE = Path(__file__).resolve().parents[1]


def main():
    filling = load(HERE / "numbers/filling.json")["final+retry"]
    designated = filling["designated_tests"]
    from grounding.runs.denominator_01.kit.outcomes import single_scenarios
    des_units = {m: set() for m in ("absence", "underspecified")}
    for k, v in designated.items():
        form = k.split(" ", 1)[0]
        if form in des_units:
            des_units[form].add(v)

    # ---- regular tests, classified ------------------------------------------------------------------------------
    test_meta, rows_by_scenario = {}, defaultdict(list)
    cover_decoys = {}
    for index, folder in SUITES:
        doc = load(index)
        for m in (doc["tests"] if isinstance(doc, dict) else doc):
            if isinstance(m, str):
                continue
            case = load(folder / m["domain"] / f"{m['case_id']}.json")
            if rulings.test_exclusion(case):
                continue
            bad = rulings.flawed(rulings.scenario_of(case["case_id"]))
            d = case["domain"]
            facts = {base_fact(d, c["requirement"]) for ref in case["references"] for c in ref.get("claims", []) if str(c["witness"]) not in bad}
            test_meta[m["case_id"]] = {"domain": d, "form": m["form"], "scenario": m["scenario"], "facts": facts, "muse": m["scenario"].startswith("G4-")}
            rows_by_scenario[m["scenario"]].append(m["case_id"])
            if m["form"] == "cover":
                dv = defaultdict(set)
                for ref in case["references"]:
                    for c in ref.get("claims", []):
                        if str(c["witness"]) not in bad:
                            dv[base_fact(d, c["requirement"])].add(str(c["witness"]))
                for f, ws in dv.items():
                    cover_decoys[(m["scenario"], f)] = ws
    des_scenario = single_scenarios(designated, test_meta, rows_by_scenario)
    packed_scenario = {tuple(k.split(" ", 2)[1:]): v for k, v in designated.items() if k.startswith("probe ")}
    packed, counted_singles = set(), set()
    for (d, f), sid in packed_scenario.items():
        cands = [c for c in rows_by_scenario[sid] if test_meta[c]["form"] in ("probe", "fact probe") and f in test_meta[c]["facts"]]
        fp = [c for c in cands if test_meta[c]["form"] == "fact probe"]
        if fp:
            packed.add(fp[0])
        elif len(cover_decoys.get((sid, f), ())) == 1 and cands:
            packed.add(cands[0])
    for (d, f), sid in des_scenario.items():
        singles = sorted(c for c in rows_by_scenario[sid] if test_meta[c]["form"] == "probe" and f in test_meta[c]["facts"])
        counted_singles.update(singles[:prescribed(d, f)])
    counted_singles -= packed
    kind = {}
    for cid, meta in test_meta.items():
        if not meta["muse"]:
            kind[cid] = f"remaining: Sonnet-written {meta['form']} (the writer comparison)"
        elif meta["form"] == "cover":
            kind[cid] = "denominator: cover"          # one cover per brief: every usable Muse scenario's cover counts
        elif cid in packed:
            kind[cid] = "denominator: packed probe"
        elif cid in counted_singles:
            kind[cid] = "denominator: single-decoy probe (counted)"
        elif meta["form"] == "fact probe":
            kind[cid] = "remaining: packed probe of another scenario for a fact already filled"
        else:
            kind[cid] = "remaining: single-decoy probe beyond the counted ones"
    # what the "beyond the counted ones" probes are: the fact, its family, whether the probe sits in the fact's
    # designated scenario (then the writer built more decoys than the catalog names alternatives) or in another
    # scenario that also claims the fact
    family_of = {}
    for index, folder in SUITES:
        doc = load(index)
        for m in (doc["tests"] if isinstance(doc, dict) else doc):
            if not isinstance(m, str):
                family_of[m["case_id"]] = m.get("family")
    beyond = []
    for cid, k in kind.items():
        if k != "remaining: single-decoy probe beyond the counted ones":
            continue
        meta = test_meta[cid]
        for f in sorted(meta["facts"]):
            d = meta["domain"]
            beyond.append({"test": cid, "fact": f, "family": family_of.get(cid), "in_the_designated_scenario": des_scenario.get((d, f)) == meta["scenario"],
                           "prescribed_for_the_fact": prescribed(d, f) if f in __import__("grounding.runs.denominator_01.kit.single_decoy", fromlist=["CAT"]).CAT[d] else None,
                           "decoys_in_the_designated_scenario": len(cover_decoys.get((des_scenario.get((d, f)), f), ()))})

    # ---- policy units, classified -------------------------------------------------------------------------------
    unit_meta = {}
    for mode in ("absence", "underspecified"):
        for cell, seq in policy.population_plan(mode)["cells"].items():
            for u in seq:
                unit_meta[u["unit"]] = {**u, "mode": mode}
        for u in load(RUNS / "regen_01/suite/units.json")["units"]:
            if u["mode"] == mode:
                unit_meta[u["unit"]] = dict(u)
    def unit_case(m):
        p = RUNS / "regen_01/suite/units" / m["domain"] / f"{m['unit']}.json"
        return load(p) if p.exists() else policy.unit_case(m)
    ukind = {}
    for uid, m in unit_meta.items():
        valid = rulings.test_exclusion(unit_case(m)) is None
        if not valid:
            continue
        muse = m["scenario"].startswith("G4-")
        if uid in rulings.DUPLICATE_UNITS:
            ukind[uid] = f"remaining: duplicate {m['mode']} unit (same request as another)"
        elif not muse:
            ukind[uid] = f"remaining: Sonnet-written {m['mode']} unit (the writer comparison)"
        elif uid in des_units[m["mode"]]:
            ukind[uid] = f"denominator: {m['mode']} test"
        else:
            ukind[uid] = f"remaining: {m['mode']} unit of a fact already filled"

    # ---- outcomes per agent ----------------------------------------------------------------------------------
    result = {}
    for agent, score_paths in (("qwen", QWEN_SCORES), ("sol", SOL_SCORES)):
        sc, _ = scores(score_paths)
        rows = defaultdict(lambda: {"tests": 0, "ran": 0, "with_a_failure": 0, "facts": set()})
        for cid, k in kind.items():
            r = rows[k]; r["tests"] += 1
            t = sc.get(cid)
            if not t:
                continue
            r["ran"] += 1
            d = test_meta[cid]["domain"]
            e = {(d, base_fact(d, x)) for x in t.get("exposed", [])}
            if e:
                r["with_a_failure"] += 1; r["facts"] |= e
        outcomes = {}
        for mode in ("absence", "underspecified"):
            if agent == "qwen":
                o = solpolicy.qwen_outcomes(mode); o.update(policy.population_outcomes([QWEN_REGEN_POLICY[mode]]))
            else:
                o = solpolicy.outcomes_of([d for d in SOL_POLICY[mode] if d.exists()])
            outcomes.update(o)
        urows = defaultdict(lambda: {"tests": 0, "ran": 0, "with_a_failure": 0, "failing_trials": 0, "usable_trials": 0})
        for uid, k in ukind.items():
            r = urows[k]; r["tests"] += 1
            outs = [x for x in outcomes.get(uid, {}).values() if x in sampler.FAIL | sampler.PASS]
            if not outs:
                continue
            r["ran"] += 1
            fails = sum(1 for x in outs if x in sampler.FAIL)
            r["failing_trials"] += fails; r["usable_trials"] += len(outs)
            r["with_a_failure"] += 1 if fails else 0
        result[agent] = {"regular": {k: {**v, "facts": len(v["facts"]), "_facts": sorted(v["facts"])} for k, v in sorted(rows.items())},
                         "policy": {k: dict(v) for k, v in sorted(urows.items())}}
    # boundary: the automated study's round 1, valid requests, on the toy loop
    bsum = load(RUNS / "boundary_auto_01/summary.json")
    result["boundary"] = {"valid_round1": bsum["valid (reader agreed)"], "elements_with_a_failing_trial": bsum["elements with a failing trial"],
                          "harness": "bare toy loop on the self-hosted Qwen (8-minute budget, 40 turns); not run on OpenClaw, not run on Sol"}
    result["beyond_the_counted_single_decoy_probes"] = beyond
    (HERE / "numbers/retained.json").write_text(json.dumps(result, indent=1) + "\n")
    for agent in ("qwen", "sol"):
        print(f"\n== {agent}")
        for k, v in result[agent]["regular"].items():
            print(f"  {k}: tests {v['tests']}, ran {v['ran']}, with a failure {v['with_a_failure']}, facts {v['facts']}")
        for k, v in result[agent]["policy"].items():
            print(f"  {k}: units {v['tests']}, ran {v['ran']}, with a failure {v['with_a_failure']}, failing/usable trials {v['failing_trials']}/{v['usable_trials']}")
    print("\nboundary:", result["boundary"])


if __name__ == "__main__":
    main()
