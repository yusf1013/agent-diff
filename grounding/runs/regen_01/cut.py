"""The cases folders the runs read, as openclaw_eval_01/rerun.py cut 6b's for `full_04`: the tests and policy units the
rulings keep (rules.py: roadmap_01/known_defects.json with this study's opaque ids), each run's list with the ones left
out and why, and the regular run's suite index. No model or replica calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.cut

Writes runs/<run>_cases/<domain>/ and runs/<run>_cases.json for:
- `full_01`: every regular test of suite/cases (covers, probes, fact probes), with runs/full_01_cases/suite.json, the
  suite index restricted to them, which judge v2's selection and the score read;
- `absence_01`: the absence twins of suite/units (AT-);
- `underspecified_01`: the drop-F variants of suite/units (U-).
Refuses to overwrite a folder that exists: a run's cases are cut once, before its blind sample and its run.
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.regen_01 import rules

HERE = Path(__file__).resolve().parent
SUITE = HERE / "suite"
RUNS = {"full_01": (SUITE / "cases", lambda stem: True),
        "absence_01": (SUITE / "units", lambda stem: stem.startswith("AT-")),
        "underspecified_01": (SUITE / "units", lambda stem: stem.startswith("U-"))}
DOMAINS = ("box", "calendar", "linear", "slack")


def cut(run: str) -> None:
    source, wanted = RUNS[run]
    dest = HERE / "runs" / f"{run}_cases"
    if dest.exists():
        raise SystemExit(f"{dest} exists")
    kept, left_out = [], {}
    for domain in DOMAINS:
        for path in sorted((source / domain).glob("*.json")):
            if not wanted(path.stem):
                continue
            case = json.loads(path.read_text())
            why = rules.rulings.test_exclusion(case)
            if why:
                left_out[case["case_id"]] = why
                continue
            out = dest / domain / path.name
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(path.read_text())
            kept.append(case["case_id"])
    (dest.parent / f"{run}_cases.json").write_text(json.dumps(
        {"source": str(source.relative_to(HERE.parent)), "tests": kept, "left_out": left_out}, indent=1) + "\n")
    if run == "full_01":
        rows = [m for m in json.loads((source / "suite.json").read_text()) if m["case_id"] in set(kept)]
        (dest / "suite.json").write_text(json.dumps(rows, indent=1) + "\n")
    print(f"{run}: {len(kept)} to run, {len(left_out)} left out -> {dest.relative_to(HERE)}")
    for cid, why in sorted(left_out.items()):
        print("  LEFT OUT", cid, "|", why)


if __name__ == "__main__":
    for name in RUNS:
        cut(name)
