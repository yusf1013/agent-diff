"""Per-test outcomes across trials (diff-based attribution, for manual confirmation). No service calls.

    python -m grounding.runs.fact_coverage_02.analyze RUN_DIR [RUN_DIR ...] > attribution.json

For each trial directory (t1, t2, ...) and case, the latest attempt is attributed with the pilot's analyzer
(acting on a claim's witness exposes that claim's fact). References are refreshed from the current case files
when the request and seed are unchanged. Outcomes are provisional labels, not verdicts.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot import analyze as pilot

HERE = Path(__file__).resolve().parent
SOURCES = [HERE / "cases_new", HERE / "cases_pilot", HERE / "cases_factprobe", HERE / "cases_hidden",
           HERE.parent / "fact_coverage_01/pilot/cases"]


def current(case):
    for root in SOURCES:
        path = root / case["domain"] / f"{case['case_id']}.json"
        if path.exists():
            newer = json.loads(path.read_text())
            if newer["prompt"] == case["prompt"] and newer["seed"] == case["seed"]:
                return {**case, "references": newer["references"]}
    return case


def trial_rows(run: Path):
    for trial in sorted(run.glob("t*")):
        for case_dir in sorted(p for p in trial.iterdir() if p.is_dir()):
            attempts = sorted(case_dir.glob("attempt-*"))
            if not attempts:
                continue
            attempt = attempts[-1]
            summary = json.loads((attempt / "execution_summary.json").read_text())
            row = {"run": run.name, "trial": trial.name, "case_id": summary["case_id"], "attempts": len(attempts),
                   "status": summary.get("status"), "usage": summary.get("usage") or {}}
            if summary.get("status") == "completed":
                case = current(json.loads((attempt / "case.json").read_text()))
                row.update(pilot.attribute(case, attempt))
            else:
                row["error"] = (summary.get("error") or "")[:300]
            yield row


def main():
    rows = [row for run in sys.argv[1:] for row in trial_rows(Path(run))]
    print(json.dumps(rows, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
