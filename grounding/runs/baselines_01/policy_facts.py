"""Facts exposed at the policy level by the baselines, under two readings (2026-09-29).

    python3 grounding/runs/baselines_01/policy_facts.py      # writes policy_facts.json and prints it

A failing trial of a presupposing test (no target, no escape clause) is not one generic "absence policy" with no
fact: the near miss the agent acted on realizes a catalog fact (the PI's rule). Which near misses count has two
readings, both kept apart from the fact-sensitive exposures (which stay as labelled):
- **designated** (the rule as the lead session relayed it): only a designated alternative (F1 to F8), as our absence
  twins do, one per (scenario, fact). Keys `policy_facts_detect3`, `policy_facts_detect1`, `no_fact_trials`, and
  each trial's `fact`.
- **any family** (the lead session's reading, one rule for both forms): any near miss that fails exactly one
  condition, F0 included, as the failure-to-fact rule counts them in probe form. Keys `any_family_facts_detect3`,
  `any_family_facts_detect1`, `any_family_no_fact_trials`, and each trial's `any_family_fact`.
Under both, a failing trial whose acted-on record is outside the catalog, a far competitor, or a record the agent
created counts as "no fact", by reason. Set and underspecified tests are counted the same way (none failed; no
baseline wrote an underspecified test). Each trial carries its label's mechanism.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
MISTAKE = {"incorrect", "presented"}
POLICY_FORMS = {"absence_presupposed", "set", "underspecified"}
GENS = {"N0": "n0/runs/gen_01", "N1": "n1/runs/gen_01", "N0M": "twin2/n0m/runs/gen_01", "N1M": "twin2/n1m/runs/gen_01"}
READINGS = ("designated", "any_family")


def main():
    out = {}
    for name, gen in GENS.items():
        review = {r["test"]: r for r in json.loads((HERE / gen / "review.json").read_text())}
        labels = {k: v for k, v in json.loads((HERE / gen / "labels.json").read_text()).items()
                  if not k.startswith("_")}
        facts3 = {reading: set() for reading in READINGS}
        facts1 = {reading: set() for reading in READINGS}
        no_fact = {reading: Counter() for reading in READINGS}
        trials = []

        def credit(reading, fact, trial):
            facts3[reading].add(fact)
            if trial == "t1":
                facts1[reading].add(fact)

        for key, label in sorted(labels.items()):
            _, trial, case = key.split("/")
            r = review[case]
            if r["form"] not in POLICY_FORMS or label["outcome"] not in MISTAKE or not r["valid"]:
                continue
            near = {str(n["record"]): n for n in r["near_misses"]}
            acted = [near.get(str(a)) for a in label.get("acted_on", [])]
            mechanism = label.get("mechanism")
            if not acted or all(n is None for n in acted):
                reason = "acted on a far competitor or a record it created"
                for reading in READINGS:
                    no_fact[reading][reason] += 1
                trials.append({"trial": key, "fact": None, "why": reason, "any_family_fact": None,
                               "mechanism": mechanism})
                continue
            for n in (n for n in acted if n):
                if n["fact"].startswith("("):
                    reason = "outside the catalog"
                    for reading in READINGS:
                        no_fact[reading][reason] += 1
                    trials.append({"trial": key, "fact": None, "why": reason, "near_miss_fact": n["fact"],
                                   "any_family_fact": None, "mechanism": mechanism})
                elif n["family"] != "F0":
                    for reading in READINGS:
                        credit(reading, n["fact"], trial)
                    trials.append({"trial": key, "fact": n["fact"], "family": n["family"],
                                   "any_family_fact": n["fact"], "mechanism": mechanism})
                else:
                    credit("any_family", n["fact"], trial)
                    no_fact["designated"]["plain near miss (F0)"] += 1
                    trials.append({"trial": key, "fact": None, "why": "plain near miss (F0)",
                                   "near_miss_fact": n["fact"], "family": "F0", "any_family_fact": n["fact"],
                                   "mechanism": mechanism})
        out[name] = {"presupposing_tests": sum(1 for r in review.values() if r["form"] == "absence_presupposed"),
                     "set_tests": sum(1 for r in review.values() if r["form"] == "set"),
                     "failing_policy_trials": len(trials),
                     "policy_facts_detect3": sorted(facts3["designated"]),
                     "policy_facts_detect1": sorted(facts1["designated"]),
                     "no_fact_trials": dict(no_fact["designated"]),
                     "any_family_facts_detect3": sorted(facts3["any_family"]),
                     "any_family_facts_detect1": sorted(facts1["any_family"]),
                     "any_family_no_fact_trials": dict(no_fact["any_family"]),
                     "trials": trials}
    (HERE / "policy_facts.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "trials"} for k, v in out.items()}, indent=1))


if __name__ == "__main__":
    main()
