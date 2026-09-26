"""The exemplars' outcomes per new scenario (fact_coverage_02, manual labels), for the Arm R comparison.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.exemplars

Writes eval/exemplar_outcomes.json. For each of the 18 new scenarios:
- the facts tested;
- the cover and probe tests (reruns supersede v1, as in fact_coverage_02's tables);
- the facts exposed at 3 trials (all, and uncontested), and at trial 1;
- the fact probes' exposures, apart.

Slack's older fact names are mapped to catalog ids. Evaluation data only; no agent ever reads it.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from grounding.runs.autogen_01.inputs.make_briefs import SLACK_ALIASES
from grounding.runs.fact_coverage_02.tables import load

OUT = Path(__file__).resolve().parents[1] / "eval" / "exemplar_outcomes.json"


def canon(fact):
    return SLACK_ALIASES.get(fact, fact)


def main():
    main_tests = load(["method_new", "method_new_lin25", "method_new_slk21"])
    t1_tests = load(["method_new", "method_new_lin25", "method_new_slk21"], only=["t1"])
    fp_tests = load(["factprobe"])
    out = defaultdict(lambda: {"tests": 0, "probes": 0, "covers": 0, "facts_tested": set(), "exposed": set(),
                               "exposed_uncontested": set(), "exposed_t1": set(), "fact_probe_exposed": set(),
                               "by_test": {}})
    for t in main_tests:
        if t["form"] not in ("probe", "cover control") or not t.get("scenario"):
            continue
        s = out[t["scenario"]]
        s["tests"] += 1
        s["probes" if t["form"] == "probe" else "covers"] += 1
        if t.get("fact"):
            s["facts_tested"].add(canon(t["fact"]))
        s["exposed"] |= {canon(x) for x in t["exposed"] if not x.startswith("policy:")}
        s["exposed_uncontested"] |= {canon(x) for x in t["exposed_strict"] if not x.startswith("policy:")}
        s["by_test"][t["case_id"]] = {"form": t["form"], "fact": canon(t["fact"]) if t.get("fact") else None,
                                      "family": t.get("family"), "failures": t["failures"],
                                      "established": t["established"]}
    for t in t1_tests:
        if t.get("scenario") in out:
            out[t["scenario"]]["exposed_t1"] |= {canon(x) for x in t["exposed"] if not x.startswith("policy:")}
    for t in fp_tests:
        scenario = t["case_id"].split("-I")[0].replace("FP-", "")
        if scenario in out:
            out[scenario]["fact_probe_exposed"] |= {canon(x) for x in t["exposed"] if not x.startswith("policy:")}
    result = {k: {kk: sorted(vv) if isinstance(vv, set) else vv for kk, vv in v.items()} for k, v in sorted(out.items())}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=1) + "\n")
    total = {"scenarios": len(result), "tests": sum(v["tests"] for v in result.values()),
             "facts_tested": len({(k[:3], f) for k, v in result.items() for f in v["facts_tested"]}),
             "exposed": sorted({f for v in result.values() for f in v["exposed"]})}
    print(json.dumps(total, indent=1))


if __name__ == "__main__":
    main()
