"""Our side of the comparison, from existing records only (no model calls).

    python3 grounding/runs/baselines_01/ours.py          # writes ours.json and prints it

- **Tests:** the frozen suite's regular tests (openclaw_eval_01/suite), split by source. Phase 4's are the ones Muse
  wrote, the same agent N0 runs on.
- **Facts exercised:** the facts the reference queries are labelled with, plus the claims. **With a near miss:** each
  test's `coverage_claims` (any family). **Exercised properly:** claims of families F1 to F8 only (the credit rule
  asks for a designated substitute; F0 is plain). Their near misses passed the mechanical witness check
  when the suite was derived, and every regular test's form is fact-sensitive (a cover has its target; a probe and a
  fact probe permit absence). Claims the validity reviews ruled out are not removed here; `adjudicated` below is.
- **Facts exposed:** openclaw_eval_01's `full_02.adjudicated.json` (detect@3 and detect@1).
- **Equal budget:** the expected number of distinct facts exercised properly and exposed by 12 tests drawn at random
  from a domain's tests (2,000 draws, seed 1).
- **Generation cost:** Phase 4's writer and reader calls (`autogen_02/runs/phase4_gen/calls.jsonl`), list and billed,
  per accepted scenario and per derived regular test.
"""
from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
OC = RUNS / "openclaw_eval_01"
BUDGET, DRAWS = 12, 2000


def query_facts(node) -> set:
    """Every catalog fact a reference query's filters and edges are labelled with."""
    found = set()
    if isinstance(node, dict):
        if isinstance(node.get("fact"), str):
            found.add(node["fact"])
        for value in node.values():
            found |= query_facts(value)
    elif isinstance(node, list):
        for value in node:
            found |= query_facts(value)
    return found


def main():
    index = json.loads((OC / "suite" / "suite.json").read_text())
    exposure = {t["case_id"]: t for t in json.loads((OC / "runs" / "full_02.adjudicated.json").read_text())["tests"]}
    claims, proper_claims, exercised = {}, {}, {}
    for path in (OC / "suite" / "cases").glob("*/*.json"):
        case = json.loads(path.read_text())
        claims[case["case_id"]] = case.get("coverage_claims", [])
        refs = case.get("references", [])
        proper_claims[case["case_id"]] = sorted({c["requirement"] for r in refs for c in r.get("claims", [])
                                                 if c.get("family") not in (None, "F0")})
        exercised[case["case_id"]] = sorted(query_facts([r.get("query") for r in refs]) |
                                            set(claims[case["case_id"]]))
    rng = random.Random(1)
    out = {}
    for label, keep in (("phase4_muse", lambda t: t["source"].endswith("phase4_gen")), ("all", lambda t: True)):
        per = defaultdict(list)
        for t in index:
            if keep(t) and t["case_id"] in exposure:  # exposure leaves out the 2 tests the reviews invalidated
                per[t["domain"]].append(t["case_id"])
        section = {}
        for domain, ids in sorted(per.items()):
            ex3 = set().union(*(exposure[i]["exposed"] for i in ids))
            ex1 = set().union(*(exposure[i]["exposed_t1"] for i in ids))
            near = set().union(*(claims[i] for i in ids))
            proper = set().union(*(proper_claims[i] for i in ids))
            used = set().union(*(exercised[i] for i in ids))
            draws = {"exercised": 0, "near_miss_any_family": 0, "proper": 0, "exposed3": 0, "exposed1": 0,
                     "tests_exposing": 0}
            for _ in range(DRAWS):
                pick = rng.sample(ids, min(BUDGET, len(ids)))
                draws["exercised"] += len(set().union(*(exercised[i] for i in pick)))
                draws["near_miss_any_family"] += len(set().union(*(claims[i] for i in pick)))
                draws["proper"] += len(set().union(*(proper_claims[i] for i in pick)))
                draws["exposed3"] += len(set().union(*(exposure[i]["exposed"] for i in pick)))
                draws["exposed1"] += len(set().union(*(exposure[i]["exposed_t1"] for i in pick)))
                draws["tests_exposing"] += sum(1 for i in pick if exposure[i]["exposed"])
            section[domain] = {
                "tests": len(ids), "facts_exercised": len(used), "facts_with_a_near_miss": len(near),
                "facts_exercised_properly": len(proper),
                "facts_exposed_detect3": len(ex3), "facts_exposed_detect1": len(ex1),
                "tests_exposing": sum(1 for i in ids if exposure[i]["exposed"]),
                f"per_{BUDGET}_tests": {k: round(v / DRAWS, 2) for k, v in draws.items()}}
        out[label] = section
    calls = [json.loads(line) for line in (RUNS / "autogen_02/runs/phase4_gen/calls.jsonl").read_text().splitlines()]
    scenarios = {t["scenario"] for t in index if t["source"].endswith("phase4_gen")}
    tests = sum(1 for t in index if t["source"].endswith("phase4_gen"))
    list_cost = sum(c.get("cost_usd_list_price") or 0 for c in calls)
    billed = sum(c.get("cost_usd_billed") or 0 for c in calls)
    out["phase4_generation_cost"] = {
        "calls": len(calls), "list_usd": round(list_cost, 2), "billed_usd": round(billed, 3),
        "accepted_scenarios": len(scenarios), "regular_tests": tests,
        "list_per_scenario": round(list_cost / len(scenarios), 3), "list_per_test": round(list_cost / tests, 3),
        "billed_per_test": round(billed / tests, 4),
        "note": "all writer and reader calls of phase4_gen, including briefs that were rejected"}
    (HERE / "ours.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
