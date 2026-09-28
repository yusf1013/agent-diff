"""Build the several-match scenarios into cover cases, with the kit's checks and replica pre-checks (plan.md).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_01.build [SCENARIO_ID ...]

For each scenarios/<id>.json: `scenario.build` (format, seed, reference and claim checks, anchors, replica rules,
lint), then the cover from `derive.suite`, then `preflight.check` (reads, observability, write feasibility). Writes
cases/<domain>/<id>.json for scenarios without problems, and checks/<id>/ with every check's output.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, preflight, scenario

HERE = Path(__file__).resolve().parent
DB = os.environ.get("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
BASE = os.environ.get("AGENTDIFF_BASE_URL", "http://127.0.0.1:18001")


def main(ids):
    paths = sorted((HERE / "scenarios").glob("*.json"))
    for path in paths:
        s = json.loads(path.read_text())
        if ids and s["scenario_id"] not in ids:
            continue
        sid = s["scenario_id"]
        out = HERE / "checks" / sid
        out.mkdir(parents=True, exist_ok=True)
        brief = {"scenario_id": sid, "domain": s["domain"], "facts": []}
        case, problems = scenario.build(s, brief)
        record = {"scenario": sid, "build_problems": problems}
        if case is not None and not problems:
            pre_case = dict(case)
            report, pre = preflight.check(pre_case, out / "preflight", DB, BASE)
            record["preflight_problems"] = pre
            cover = next(t for t, meta in derive.suite(case) if meta["form"] == "cover")
            record["cover_id"] = cover["case_id"]
            if not pre:
                dest = HERE / "cases" / s["domain"] / f"{cover['case_id']}.json"
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(json.dumps(cover, indent=1) + "\n")
                record["case"] = dest.relative_to(HERE).as_posix()
        (out / "build.json").write_text(json.dumps(record, indent=1) + "\n")
        print(f"{sid}: build {problems or 'ok'}; preflight {record.get('preflight_problems', 'not run')}")


if __name__ == "__main__":
    main(set(sys.argv[1:]))
