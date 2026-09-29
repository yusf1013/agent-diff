"""Build the several_match_02 scenarios into cover cases, with the kit's checks and replica pre-checks.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_02.build [SCENARIO_ID ...]

As several_match_01/build.py: `scenario.build` (format, seed, reference and claim checks, anchors, replica rules,
lint), the cover from `derive.suite`, and `preflight.check` (reads, observability, write feasibility). Writes
cases/<domain>/<id>.json and checks/<id>/.
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
    for path in sorted((HERE / "scenarios").glob("*.json")):
        s = json.loads(path.read_text())
        sid = s["scenario_id"]
        if ids and sid not in ids:
            continue
        out = HERE / "checks" / sid
        out.mkdir(parents=True, exist_ok=True)
        case, problems = scenario.build({k: v for k, v in s.items() if k != "strategy_entry"},
                                        {"scenario_id": sid, "domain": s["domain"], "facts": []})
        record = {"scenario": sid, "build_problems": problems}
        if case is not None and not problems:
            _report, pre = preflight.check(dict(case), out / "preflight", DB, BASE)
            record["preflight_problems"] = pre
            cover = next(t for t, meta in derive.suite(case) if meta["form"] == "cover")
            if not pre:
                dest = HERE / "cases" / s["domain"] / f"{cover['case_id']}.json"
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(json.dumps(cover, indent=1) + "\n")
                record["case"] = dest.relative_to(HERE).as_posix()
        (out / "build.json").write_text(json.dumps(record, indent=1) + "\n")
        print(f"{sid}: build {problems or 'ok'}; preflight {record.get('preflight_problems', 'not run')}")


if __name__ == "__main__":
    main(set(sys.argv[1:]))
