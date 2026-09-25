"""The review listing used for every verdict: trials that are not clean and have no manual label yet. No service calls.

    python -m grounding.runs.fact_coverage_02.review RUN_NAME [CASE_SUBSTRING]

For each such trial it prints the case prompt (once per case), the trial's provisional outcome, the acted-on
records with the claim explanation of each decoy, every write command (clipped) and the answer. Verdicts go into
manual_labels.json with a note; a label always refers to the trial's latest attempt.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from grounding.runs.fact_coverage_02 import score
from grounding.runs.fact_coverage_02.analyze import current, trial_rows

HERE = Path(__file__).resolve().parent


def main():
    run = HERE / "runs" / sys.argv[1]
    substring = sys.argv[2] if len(sys.argv) > 2 else ""
    manual = json.loads((HERE / "manual_labels.json").read_text())
    seen = set()
    for row in trial_rows(run):
        if substring not in row["case_id"] or f"{run.name}/{row['trial']}/{row['case_id']}" in manual:
            continue
        attempt = sorted((run / row["trial"] / row["case_id"]).glob("attempt-*"))[-1]
        case = current(json.loads((attempt / "case.json").read_text()))
        result = score.classify(row, case, {}, attempt)
        if result["outcome"] in ("correct", "correct_absent"):
            continue
        if row["case_id"] not in seen:
            seen.add(row["case_id"])
            print(f"\n##### {row['case_id']}: {case['prompt']}")
        claims = {str(c["witness"]): c for r in case["references"] for c in r["claims"]}
        acted = [a for r in row.get("references", []) for a in r["acted"]]
        print(f"--- {row['case_id']} {row['trial']} outcome={result['outcome']} acted={acted} "
              f"exposed={result['exposed']}")
        for a in acted:
            if a in claims:
                print(f"    decoy {a}: {claims[a]['requirement']} -- {claims[a]['explanation']}")
        record = next((p for p in (attempt / "solver").glob("*.json") if p.name != "config.json"), None)
        if record:
            for step in json.loads(record.read_text()).get("steps", []):
                action = str(step.get("action") or "")
                if score.WRITES[case["domain"]].search(action):
                    print("    write:", re.sub(r"\s+", " ", action)[-200:])
        answer = result.get("final") or f"(none; {result.get('error') or row.get('status')})"
        print("    answer:", re.sub(r"\s+", " ", answer)[:420])


if __name__ == "__main__":
    main()
