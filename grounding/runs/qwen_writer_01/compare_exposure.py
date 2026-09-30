"""The exposure half: Qwen's tests on OpenClaw with the self-hosted Qwen (runs/<RUN>, judged by judge v2 on Muse,
under this study's rulings) against Muse's tests on the same briefs (openclaw_eval_01: full_02 for Box, full_03 for
Calendar, Linear and Slack, under the PI's rulings). No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.qwen_writer_01.compare_exposure [RUN]

A test exposes a fact when a counted trial fails on it (detect@3 over the 3 trials, detect@1 on the first); the
rulings and the solver's budget are applied by each run's adjudication (openclaw_eval_01/adjudicate.py; for Qwen's
run through adjudicate.py in this folder). The denominators: the drawn briefs' facts, and for each side the facts
its suite tests validly (a kept scenario with a valid near miss on the fact).

Writes eval/exposure.json and prints the tables for the README.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
OC = RUNS / "openclaw_eval_01" / "runs"
MUSE_RUN = {"box": "full_02", "calendar": "full_03", "linear": "full_03", "slack": "full_03"}


def drawn() -> dict[str, str]:
    plan = json.loads((HERE / "plan.json").read_text())
    return {sid: domain for domain, ids in plan["drawn"].items() for sid in ids}


def tests_of(adjudicated: dict, scenarios: set[str]) -> list[dict]:
    return [t for t in adjudicated["tests"] if t["scenario"] in scenarios]


def summary(tests: list[dict], facts: dict[str, list[str]], valid: dict[str, list[str]]) -> dict:
    brief_facts = {(s, f) for s, fs in facts.items() for f in fs}
    exposed3 = {(t["scenario"], f) for t in tests for f in t["exposed"]}
    exposed1 = {(t["scenario"], f) for t in tests for f in t["exposed_t1"]}
    valid_pairs = {(s, f) for s, fs in valid.items() for f in fs}
    by_form = defaultdict(lambda: {"tests": 0, "exposing": 0})
    for t in tests:
        by_form[t["form"]]["tests"] += 1
        by_form[t["form"]]["exposing"] += bool(t["exposed"])
    return {"tests": len(tests), "tests_exposing": sum(1 for t in tests if t["exposed"]),
            "tests_exposing_t1": sum(1 for t in tests if t["exposed_t1"]),
            "brief_facts": len(brief_facts), "facts_tested_validly": len(valid_pairs & brief_facts),
            "facts_detect3": len(exposed3 & brief_facts), "facts_detect1": len(exposed1 & brief_facts),
            "exposed_outside_brief": sorted(f"{s}:{f}" for s, f in exposed3 - brief_facts),
            "by_form": dict(by_form),
            "facts_exposed": sorted(f"{s}:{f}" for s, f in exposed3 & brief_facts)}


def main():
    run = sys.argv[1] if len(sys.argv) > 1 else "oc_01"
    scenarios = drawn()
    gen = json.loads((HERE / "eval" / "generation.json").read_text())["briefs"]
    facts = {sid: gen[sid]["facts"] for sid in scenarios}
    valid = {who: {sid: gen[sid][who]["facts_covered_validly"] for sid in scenarios} for who in ("muse", "qwen")}
    muse_tests = []
    for name in sorted(set(MUSE_RUN.values())):
        adjudicated = json.loads((OC / f"{name}.adjudicated.json").read_text())
        wanted = {sid for sid, d in scenarios.items() if MUSE_RUN[d] == name}
        muse_tests += tests_of(adjudicated, wanted)
    qwen_adjudicated = json.loads((HERE / "runs" / f"{run}.adjudicated.json").read_text())
    qwen_tests = tests_of(qwen_adjudicated, set(scenarios))
    result = {"muse": {"runs": MUSE_RUN, **summary(muse_tests, facts, valid["muse"])},
              "qwen": {"run": run, **summary(qwen_tests, facts, valid["qwen"])},
              "qwen_left_out_tests": qwen_adjudicated["left_out_tests"],
              "qwen_trials_not_counted": qwen_adjudicated["trials_not_counted"],
              "qwen_trials_over_budget": qwen_adjudicated["trials_over_budget"], "by_brief": {}}
    for sid in scenarios:
        row = {}
        for who, tests in (("muse", muse_tests), ("qwen", qwen_tests)):
            mine = [t for t in tests if t["scenario"] == sid]
            row[who] = {"tests": len(mine), "exposing": sum(1 for t in mine if t["exposed"]),
                        "facts_detect3": sorted({f for t in mine for f in t["exposed"]} & set(facts[sid])),
                        "facts_detect1": sorted({f for t in mine for f in t["exposed_t1"]} & set(facts[sid]))}
        result["by_brief"][sid] = {"facts": facts[sid], **row}
    (HERE / "eval" / "exposure.json").write_text(json.dumps(result, indent=1) + "\n")
    rows = [f"| {sid} | {len(b['facts'])} | {b['muse']['tests']} | {b['muse']['exposing']} | "
            f"{len(b['muse']['facts_detect3'])} | {b['qwen']['tests']} | {b['qwen']['exposing']} | "
            f"{len(b['qwen']['facts_detect3'])} |" for sid, b in result["by_brief"].items()]
    print("| Brief | Facts | Muse tests | Muse exposing | Muse facts d@3 | Qwen tests | Qwen exposing | Qwen facts d@3 |")
    print("|---|---|---|---|---|---|---|---|")
    print("\n".join(rows))
    print(json.dumps({k: {x: v for x, v in result[k].items() if x != "facts_exposed"} for k in ("muse", "qwen")},
                     indent=1))


if __name__ == "__main__":
    main()
