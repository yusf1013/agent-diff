"""Summarize hand labels of a baseline run: outcomes, failing tests, what the failures are, facts exposed.

    python3 grounding/runs/baselines_01/summarize_labels.py LABELS.json [REVIEW.json]    # prints JSON

- **Failing test:** at least one trial labelled incorrect or presented (detect@3); detect@1 uses trial 1 only.
- **Facts exposed:** the `exposed` facts of failing trials, by the failure-to-fact rule (n0/review_rules.md).
- **Policy failures:** failing trials whose label names a policy (acting when a presupposed match is missing, or on
  one of several full matches without asking); they expose no fact.
- **Value errors:** trials on the right record with a wrong written value, outside the grounding scope.
- With REVIEW.json, trials of tests the review found invalid are counted apart.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

MISTAKE = {"incorrect", "presented"}


def main():
    labels = {k: v for k, v in json.loads(Path(sys.argv[1]).read_text()).items() if not k.startswith("_")}
    invalid = set()
    if len(sys.argv) > 2:
        invalid = {r["test"] for r in json.loads(Path(sys.argv[2]).read_text()) if not r.get("valid", True)}
    by_test = defaultdict(dict)
    for key, label in labels.items():
        _, trial, case = key.split("/")
        by_test[case][trial] = label
    outcomes = Counter(l["outcome"] for l in labels.values())
    failing3, failing1, policy_tests, facts3, facts1 = [], [], [], set(), set()
    policy_trials = value_errors = 0
    for case, trials in sorted(by_test.items()):
        if case in invalid:
            continue
        bad = {t: l for t, l in trials.items() if l["outcome"] in MISTAKE}
        if bad:
            failing3.append(case)
            for l in bad.values():
                facts3.update(l.get("exposed", []))
            if all(l.get("policy") for l in bad.values()):
                policy_tests.append(case)
        if "t1" in bad:
            failing1.append(case)
            facts1.update(bad["t1"].get("exposed", []))
        policy_trials += sum(1 for l in bad.values() if l.get("policy"))
        value_errors += sum(1 for l in trials.values() if l.get("value_error"))
    print(json.dumps({
        "trials": len(labels), "tests": len(by_test), "invalid_tests": sorted(invalid & set(by_test)),
        "outcomes": dict(outcomes),
        "failing_tests_detect3": len(failing3), "failing_tests_detect1": len(failing1),
        "failing_tests": failing3, "failing_tests_all_policy": policy_tests,
        "failing_trials": sum(outcomes[o] for o in MISTAKE), "policy_failure_trials": policy_trials,
        "facts_exposed_detect3": sorted(facts3), "facts_exposed_detect1": sorted(facts1),
        "value_error_trials": value_errors}, indent=1))


if __name__ == "__main__":
    main()
