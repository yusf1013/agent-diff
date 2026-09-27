"""Replica pre-checks on the worked examples (no model calls; needs the local backend and database).

    python -m grounding.runs.autogen_01.kit.preflight_selftest OUT_DIR [scenario.json ...]
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import preflight, scenario

KIT = Path(__file__).resolve().parent
DB = os.environ.get("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
BASE = os.environ.get("AGENTDIFF_BASE_URL", "http://127.0.0.1:18001")


def main():
    out = Path(sys.argv[1])
    paths = [Path(p) for p in sys.argv[2:]] or sorted((KIT / "examples").glob("*.json"))
    for path in paths:
        s = json.loads(path.read_text())
        brief = {"scenario_id": s["scenario_id"], "domain": s["domain"], "facts": []}
        case, problems = scenario.build(s, brief)
        if problems:
            print(path.name, "BUILD PROBLEMS", problems)
            continue
        report, problems = preflight.check(case, out / s["scenario_id"], DB, BASE)
        print(path.name, "preflight problems:", problems or "none")
        for row in report.get("observability", []):
            print("   ", row["witness"], row["fact"], "groups", row["groups"], "missing", row["missing"])
        print("    write:", {k: report.get("write", {}).get(k) for k in ("status", "acted", "targets")})
        print("    read errors:", report.get("read_errors", [])[:5])


if __name__ == "__main__":
    main()
