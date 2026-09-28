"""Cycle 2, form ablation: N0's own target-present tests turned into probes, as our derivation turns a cover into
probes. The intended record is removed (with the seed operations that depend on it) and the request gets our probes'
escape clause, "If there isn't one, just tell me." The near misses N0 wrote stay as they are.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_01.n0.probe_form

Writes runs/gen_01/probe_suite/<domain>/P-<case>.json. TARGETS names the removed record of each converted test (from
my review, runs/gen_01/review.json). Left out: sets, tests whose only competitors are far, the invalid Slack tests,
N0-SLK-T04 (its target is a default person the seed builder always creates) and N0-LIN-T09 (the issue already sits
in the only other cycle).
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.baselines_01.n0 import cases

HERE = Path(__file__).resolve().parent
GEN = HERE / "runs" / "gen_01"
CLAUSE = " If there isn't one, just tell me."

TARGETS = {
    "box": {"T01": "8110", "T02": "8210", "T04": "8400", "T05": "8510", "T07": "8720", "T08": "8810",
            "T09": "8900", "T11": "9111"},
    "calendar": {"T01": "ev_lunch2", "T02": "ev_sync_a", "T03": "ev_board_b", "T04": "ev_kick_m", "T05": "ev_des_o",
                 "T06": "ev_sp_e", "T07": "ev_dr", "T08": "ev_dent_ok", "T09": "eng@northwind.example"},
    "linear": {"T01": "i-checkout", "T02": "i-web-push", "T03": "i-login-maya", "T04": "i-exp-bug", "T05": "i-a2",
               "T08": "lb-web", "T10": "p-app", "T11": "t-ios"},
    "slack": {"T01": "C_LP", "T06": "primsg", "T08": "checkout"},
}


def mentions(value, ident: str) -> bool:
    if isinstance(value, dict):
        return any(mentions(v, ident) for v in value.values())
    if isinstance(value, list):
        return any(mentions(v, ident) for v in value)
    return value in (ident, f"@{ident}")


def remove(seed: list, ident: str) -> tuple[list, list]:
    """(seed without the record and every operation that refers to it, the removed operations)."""
    kept, removed = [], []
    for op, args in seed:
        own = args.get("id") == ident or args.get("ref") == ident
        refers = any(mentions(v, ident) for k, v in args.items() if k not in ("id", "ref"))
        (removed if own or refers else kept).append([op, args])
    return kept, removed


def main():
    out = GEN / "probe_suite"
    report = {}
    for domain, targets in TARGETS.items():
        data = json.loads((GEN / domain / "workspace" / "round1" / "tests.json").read_text())
        by_id = {t["id"]: t for t in data["tests"]}
        probes = []
        for tid, ident in targets.items():
            test = json.loads(json.dumps(by_id[tid]))
            seed, removed = remove(test["seed"], ident)
            if not removed:
                raise SystemExit(f"{domain} {tid}: {ident} is not in the seed")
            test.update(id=f"P-{tid}", seed=seed, request=test["request"].rstrip() + CLAUSE,
                        expected="Change nothing and say that nothing matches the request.",
                        assertions=[], removed=removed)
            probes.append(test)
        built, errors = cases.from_tests(domain, {"tests": probes}, generator="N0")
        if errors:
            raise SystemExit(f"{domain}: {errors}")
        (out / domain).mkdir(parents=True, exist_ok=True)
        for case in built:
            (out / domain / f"{case['case_id']}.json").write_text(json.dumps(case, indent=1, ensure_ascii=False) + "\n")
        report[domain] = [c["case_id"] for c in built]
    print(json.dumps(report, indent=1), sum(len(v) for v in report.values()))


if __name__ == "__main__":
    main()
