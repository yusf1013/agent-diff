"""Facts exposed at the policy level by the baselines (the PI's counting rule, 2026-09-29, via the lead session).

    python3 grounding/runs/baselines_01/policy_facts.py      # writes policy_facts.json and prints it

A failing trial of a presupposing test (no target, no escape clause) is not one generic "absence policy" with no
fact: the near miss the agent acted on realizes a catalog fact when it is a designated alternative (F1 to F8), as our
absence twins do, one per (scenario, fact). Per baseline: those facts at detect@3 and detect@1, kept apart from the
fact-sensitive exposures (which stay as labelled). A failing trial whose acted-on record is a plain near miss (F0),
outside the catalog, a far competitor, or a record the agent created counts as "no fact", by reason. Set and
underspecified tests are counted the same way (none failed; no baseline wrote an underspecified test).
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
MISTAKE = {"incorrect", "presented"}
POLICY_FORMS = {"absence_presupposed", "set", "underspecified"}
GENS = {"N0": "n0/runs/gen_01", "N1": "n1/runs/gen_01", "N0M": "twin2/n0m/runs/gen_01", "N1M": "twin2/n1m/runs/gen_01"}


def main():
    out = {}
    for name, gen in GENS.items():
        review = {r["test"]: r for r in json.loads((HERE / gen / "review.json").read_text())}
        labels = {k: v for k, v in json.loads((HERE / gen / "labels.json").read_text()).items()
                  if not k.startswith("_")}
        facts3, facts1, no_fact, trials = set(), set(), Counter(), []
        for key, label in sorted(labels.items()):
            _, trial, case = key.split("/")
            r = review[case]
            if r["form"] not in POLICY_FORMS or label["outcome"] not in MISTAKE or not r["valid"]:
                continue
            near = {str(n["record"]): n for n in r["near_misses"]}
            acted = [near.get(str(a)) for a in label.get("acted_on", [])]
            if not acted or all(n is None for n in acted):
                reason = "acted on a far competitor or a record it created"
                no_fact[reason] += 1
                trials.append({"trial": key, "fact": None, "why": reason})
                continue
            for n in (n for n in acted if n):
                if n["family"] != "F0" and not n["fact"].startswith("("):
                    facts3.add(n["fact"])
                    if trial == "t1":
                        facts1.add(n["fact"])
                    trials.append({"trial": key, "fact": n["fact"], "family": n["family"]})
                else:
                    reason = "outside the catalog" if n["fact"].startswith("(") else "plain near miss (F0)"
                    no_fact[reason] += 1
                    trials.append({"trial": key, "fact": None, "why": reason, "near_miss_fact": n["fact"]})
        out[name] = {"presupposing_tests": sum(1 for r in review.values() if r["form"] == "absence_presupposed"),
                     "set_tests": sum(1 for r in review.values() if r["form"] == "set"),
                     "failing_policy_trials": len(trials),
                     "policy_facts_detect3": sorted(facts3), "policy_facts_detect1": sorted(facts1),
                     "no_fact_trials": dict(no_fact), "trials": trials}
    (HERE / "policy_facts.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "trials"} for k, v in out.items()}, indent=1))


if __name__ == "__main__":
    main()
