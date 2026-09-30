"""The Sol round's case folders and suite indexes, in the layout openclaw_eval_01's judging and scoring read.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.prepare

For each regular set (`cases/regular_p4.txt`, `cases/regular_6b.txt`): copies the cases into cases/<set>/<domain>/,
and writes cases/<set>/suite.json, the source suite's index restricted to them (judge v2's selection and the score
read it, as runs/full_03_cases/suite.json served the Qwen round). The policy folders were built the same way from
the final manifest (cases/policy_selection.json). No model or replica calls.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
RUNS = HERE.parent
SETS = {"regular_p4": RUNS / "openclaw_eval_01" / "suite_opaque" / "cases",
        "regular_6b": RUNS / "completion_01" / "suite" / "cases"}


def main() -> None:
    for name, source in SETS.items():
        wanted = [line.strip() for line in (HERE / "cases" / f"{name}.txt").read_text().splitlines() if line.strip()]
        dest = HERE / "cases" / name
        rows = [m for m in json.loads((source / "suite.json").read_text()) if m["case_id"] in set(wanted)]
        by_id = {m["case_id"]: m for m in rows}
        missing = [c for c in wanted if c not in by_id]
        if missing:
            raise SystemExit(f"{name}: {len(missing)} cases not in {source / 'suite.json'}: {missing[:5]}")
        for case_id in wanted:
            path = source / by_id[case_id]["domain"] / f"{case_id}.json"
            (dest / by_id[case_id]["domain"]).mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, dest / by_id[case_id]["domain"] / path.name)
        (dest / "suite.json").write_text(json.dumps([by_id[c] for c in wanted], indent=1) + "\n")
        print(f"{name}: {len(wanted)} cases -> {dest.relative_to(RUNS)}, index {len(rows)} rows")


if __name__ == "__main__":
    main()
