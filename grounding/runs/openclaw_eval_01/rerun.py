"""The regular suite's re-run with opaque ids and test-side clocks (the discussion after 6a, 2026-09-28). No model
or replica calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.rerun

Copies the Calendar, Linear and Slack tests of suite_opaque/cases that the rulings keep (`rulings.test_exclusion`,
the known defects' "leave out" and "dropped") to runs/full_03_cases/<domain>/, so the blind sample is drawn from
exactly the tests that run, and writes the list with the ones left out and why. Box's tests are unchanged (their ids
are numbers) and keep full_02's results.
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.openclaw_eval_01 import rulings

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "suite_opaque" / "cases"
DEST = HERE / "runs" / "full_03_cases"
DOMAINS = ("calendar", "linear", "slack")


def main():
    if DEST.exists():
        raise SystemExit(f"{DEST} exists")
    kept, left_out = [], {}
    for domain in DOMAINS:
        for path in sorted((SOURCE / domain).glob("*.json")):
            case = json.loads(path.read_text())
            why = rulings.test_exclusion(case)
            if why:
                left_out[case["case_id"]] = why
                continue
            out = DEST / domain / path.name
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(path.read_text())
            kept.append(case["case_id"])
    (DEST.parent / "full_03_cases.json").write_text(json.dumps(
        {"source": str(SOURCE.relative_to(HERE)), "domains": DOMAINS, "tests": kept, "left_out": left_out},
        indent=1) + "\n")
    print(f"{len(kept)} tests -> {DEST.relative_to(HERE)}; {len(left_out)} left out")
    for cid, why in sorted(left_out.items()):
        print("  LEFT OUT", cid, "|", why)


if __name__ == "__main__":
    main()
