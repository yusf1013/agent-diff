"""Replica pre-checks on three fact_coverage_02 exemplar cases (Linear and Slack), with hand-written write calls.

    python -m grounding.runs.autogen_01.kit.preflight_exemplars OUT_DIR
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import preflight
from grounding.runs.autogen_01.kit.preflight_selftest import BASE, DB

FC2 = Path(__file__).resolve().parents[2] / "fact_coverage_02" / "cases_new"
WRITES = {
    "linear/LIN-22.json": {"graphql": 'mutation { documentUpdate(id: "d-21", input: {title: "Checkout QA plan"}) '
                                      "{ success } }"},
    "slack/SLK-22.json": {"slack": "reactions.add", "params": {"channel": "C_INC", "timestamp": "1790000400.000002",
                                                                "name": "eyes"}},
    "linear/LIN-25.json": {"graphql": 'mutation { issueAddLabel(id: "i-mob-3", labelId: '
                                      '"8e029f25-bad4-557c-8189-a7d6348259a3") { success } }'},
}


def main():
    out = Path(sys.argv[1])
    for rel, call in WRITES.items():
        case = json.loads((FC2 / rel).read_text())
        case["write_check"] = call
        report, problems = preflight.check(case, out / case["case_id"], DB, BASE)
        print(case["case_id"], "problems:", problems or "none")
        for row in report.get("observability", []):
            print("   ", row["witness"], row["fact"], "groups", [g[:4] for g in row["groups"]], "missing", row["missing"])
        print("    write:", {k: report.get("write", {}).get(k) for k in ("status", "acted", "targets")},
              str(report.get("write", {}).get("body"))[:300])
        print("    read errors:", report.get("read_errors", [])[:8])


if __name__ == "__main__":
    main()
