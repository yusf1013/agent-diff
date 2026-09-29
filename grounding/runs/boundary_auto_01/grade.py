"""The judge for the automated boundary tests: the phase-1 oracle with the generated specs.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_auto_01.grade RUN_DIR

Per trial: a digest as boundary_02/digest.py makes it (the diff's changes, the final answer), then the oracle's
verdict (boundary_02/oracle.py: the state first, then the answer; the PI's rulings on round trips and re-creations)
with the element's generated spec (specs.py). A no-answer trial whose trajectory holds a replica server error is
flagged for review: the method voids it only if the error was on reading a named record or on the requested write.
Writes digest-<run>.json and grades-<run>.json.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

from grounding.runs.boundary_02 import digest as D
from grounding.runs.boundary_02 import oracle as O
from grounding.runs.boundary_auto_01.specs import spec_for

HERE = Path(__file__).resolve().parent
SERVER_ERROR = re.compile(r"Cannot return null for non-nullable|internal_error|Internal Server Error")


def digest(run: Path):
    rows = []
    for att in sorted(run.glob("t*/BDA-*/attempt-*")):
        s = att / "execution_summary.json"
        if att != sorted(att.parent.glob("attempt-*"))[-1] or not s.exists() or \
                "termination" not in json.loads(s.read_text()):
            continue
        case = json.loads((att / "case.json").read_text())
        traj = next((p for p in (att / "solver").glob("*.json") if p.name != "config.json"), None)
        if traj is None:
            continue
        d = json.loads(traj.read_text())
        final = str(d.get("final") or "")
        errors = sum(1 for st in d.get("steps") or []
                     if SERVER_ERROR.search(str((st.get("observation") or {}).get("stdout") or "")))
        rows.append({"trial": f"{att.parent.parent.name}/{case['case_id']}", "element": case["boundary"]["element"],
                     "request": case["prompt"], "termination": d.get("termination"), "steps": len(d.get("steps") or []),
                     "changes": D.changes(att), "server_error_steps": errors, "final": final[:1000]})
    (HERE / f"digest-{run.name}.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    return rows


def main(run: Path):
    space = {r["id"]: r for r in json.loads((HERE.parent / "boundary_02" / "space.json").read_text())}
    answers = json.loads((HERE / "writer.json").read_text())
    answers_w2 = json.loads((HERE / "writer_w2.json").read_text()) if (HERE / "writer_w2.json").exists() else {}
    out = {}
    for entry in digest(run):
        eid = entry["element"]
        att = sorted((run / entry["trial"]).glob("attempt-*"))[-1]
        target = (answers_w2 if entry["trial"].endswith("-W2") else answers)[eid]["target"]
        spec = spec_for(space[eid]["service"], target)
        v, info = O.verdict(spec, att, entry)
        if v == "fail: no answer" and entry["server_error_steps"]:
            v = "review: no answer after replica server errors"
        out[entry["trial"]] = {"oracle": v, **info, "server_error_steps": entry["server_error_steps"]}
    (HERE / f"grades-{run.name}.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    print(len(out), "trials", Counter(v["oracle"] for v in out.values()))


if __name__ == "__main__":
    main(Path(sys.argv[1]))
