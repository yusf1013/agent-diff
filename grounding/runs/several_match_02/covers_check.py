"""Cycle 8: method.md's checks on the plural cover cases (cases_cover/), before any run.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_02.covers_check [CASE_ID ...]

1. The fact method's checks (fdc.check_reference): the reference selects exactly the targets, and every decoy claim
   is killed by its witness. For every case.
2. Every relevant shortcut, run as API calls on the hard case's seed, misses at least one target; the thorough
   route finds them all (strategies.py, with the table and entry from covers_entries.json).
3. The kit's preflight: reads, observability, write feasibility (checks/<case>/preflight).
Writes covers_check.json.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import preflight
from grounding.runs.fact_coverage_01 import fdc
from grounding.runs.several_match_02 import strategies

HERE = Path(__file__).resolve().parent
DB = os.environ.get("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
BASE = os.environ.get("AGENTDIFF_BASE_URL", "http://127.0.0.1:18001")


def main(ids):
    from agent_diff import AgentDiff
    entries = json.loads((HERE / "covers_entries.json").read_text())
    client, engine = AgentDiff(base_url=BASE), strategies.engine_for(DB)
    out = {}
    for path in sorted((HERE / "cases_cover").glob("*/*.json")):
        case = json.loads(path.read_text())
        cid = case["case_id"]
        if ids and cid not in ids:
            continue
        ref = case["references"][0]
        _, errors = fdc.check_reference(case["seed"], ref)
        row = {"fdc_errors": errors}
        if cid in entries:
            probe = {"id": cid, "domain": case["domain"], "place": "the plural cover's own seed",
                     "seed_tables": case["seed"], "actor": case["acting_user_id"], "targets": ref["expected"],
                     "entry": entries[cid]["entry"], "strategies": entries[cid]["table"]}
            r = strategies.run_probe(client, engine, probe)
            row["strategies"] = r["strategies"]
        _report, pre = preflight.check(dict(case), HERE / "checks" / cid / "preflight", DB, BASE)
        row["preflight"] = pre
        out[cid] = row
        print(f"\n== {cid}: fdc errors {errors or 'none'}; preflight {pre or 'ok'}")
        for name, s in (row.get("strategies") or {}).items():
            if "error" in s:
                print(f"   {name:60} ERROR {s['error'][:100]}")
            else:
                mark = f"MISSES {len(s['missed'])}" if s["missed"] else "finds all"
                bad = " <- INVALID" if s["thorough"] and s["missed"] else ""
                print(f"   {name:60} {mark}{bad}")
    prev = json.loads((HERE / "covers_check.json").read_text()) if (HERE / "covers_check.json").exists() else {}
    (HERE / "covers_check.json").write_text(json.dumps({**prev, **out}, indent=1, default=str) + "\n")
    engine.dispose()


if __name__ == "__main__":
    main(set(sys.argv[1:]))
