"""Offline check of cases.from_tests on one hand-written test per domain (no model calls, no database).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_01.n0.selftest
"""
from __future__ import annotations

from grounding.runs.baselines_01.n0 import cases

TESTS = {
    "box": [["folder", {"id": "8100", "name": "Contracts"}],
            ["file", {"id": "8101", "name": "Initech MSA.pdf", "parent": "8100", "ref": "msa"}]],
    "calendar": [["event", {"id": "ev_a", "calendar": "primary", "summary": "Budget review",
                            "start": "2018-06-21T10:00:00", "end": "2018-06-21T11:00:00", "ref": "a"}]],
    "linear": [["team", {"id": "t-web", "name": "Web", "key": "WEB"}],
               ["issue", {"id": "i-web-1", "team": "t-web", "title": "Checkout bug", "ref": "a"}]],
    "slack": [["channel", {"id": "C_INC", "name": "incidents", "members": ["leo"]}],
              ["message", {"channel": "C_INC", "author": "leo", "text": "Outage", "at": "2026-09-21T12:00:00Z",
                           "ref": "a"}]],
}


def main():
    for domain, seed in TESTS.items():
        data = {"tests": [{"id": "T01", "request": "Do the thing.", "seed": seed, "expected": "It does the thing.",
                           "assertions": [{"diff_type": "changed", "entity": "x", "where": {"id": "@a" if domain != "box" else "@msa"}}]}]}
        built, errors = cases.from_tests(domain, data)
        assert not errors, (domain, errors)
        case = built[0]
        where = case["baseline"]["assertions"][0]["where"]
        print(domain, case["case_id"], case["acting_user_id"], sorted(case["seed"])[:4], where)
    bad, errors = cases.from_tests("box", {"tests": [{"id": "T01", "request": "x", "seed": [["nope", {}]],
                                                     "expected": "x", "assertions": []}]})
    assert not bad and errors, errors
    print("rejected:", errors)


if __name__ == "__main__":
    main()
