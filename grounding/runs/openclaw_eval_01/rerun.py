"""The regular suite's runs after the discussion of 6a (2026-09-28), with opaque ids and test-side clocks. No model
or replica calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.rerun [full_03|full_04] [index]

full_03 (the default) is 6a's re-run: the Calendar, Linear and Slack tests of suite_opaque/cases (Box's tests are
unchanged, their ids are numbers, and keep full_02's results). full_04 is roadmap 6b: every test of
completion_01/suite/cases. Copies the tests the rulings keep (`rulings.test_exclusion`, the known defects' "leave
out", "dropped" and flawed near misses) to runs/<run>_cases/<domain>/, so the blind sample is drawn from exactly the
tests that run, and writes the list with the ones left out and why. `index` (also run by default) writes the run's
suite index, runs/<run>_cases/suite.json, which judge v2's selection and the score read: the source's index
restricted to these tests, with their digests.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.openclaw_eval_01 import rulings

HERE = Path(__file__).resolve().parent
RUNS = {"full_03": (HERE / "suite_opaque" / "cases", ("calendar", "linear", "slack")),
        "full_04": (HERE.parent / "completion_01" / "suite" / "cases", ("box", "calendar", "linear", "slack"))}


def index(run: str):
    source, dest = RUNS[run][0], HERE / "runs" / f"{run}_cases"
    kept = set(json.loads((dest.parent / f"{run}_cases.json").read_text())["tests"])
    rows = [m for m in json.loads((source / "suite.json").read_text()) if m["case_id"] in kept]
    (dest / "suite.json").write_text(json.dumps(rows, indent=1) + "\n")
    print(f"index: {len(rows)} tests -> {(dest / 'suite.json').relative_to(HERE)}")


def main(run: str):
    (source, domains), dest = RUNS[run], HERE / "runs" / f"{run}_cases"
    if dest.exists():
        raise SystemExit(f"{dest} exists")
    kept, left_out = [], {}
    for domain in domains:
        for path in sorted((source / domain).glob("*.json")):
            case = json.loads(path.read_text())
            why = rulings.test_exclusion(case)
            if why:
                left_out[case["case_id"]] = why
                continue
            out = dest / domain / path.name
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(path.read_text())
            kept.append(case["case_id"])
    (dest.parent / f"{run}_cases.json").write_text(json.dumps(
        {"source": str(source.relative_to(HERE.parent)), "domains": domains, "tests": kept, "left_out": left_out},
        indent=1) + "\n")
    print(f"{len(kept)} tests -> {dest.relative_to(HERE)}; {len(left_out)} left out")
    for cid, why in sorted(left_out.items()):
        print("  LEFT OUT", cid, "|", why)


if __name__ == "__main__":
    args = sys.argv[1:]
    run = args.pop(0) if args and args[0] in RUNS else "full_03"
    if args == ["index"]:
        index(run)
    else:
        main(run)
        index(run)
