"""Build the automated boundary tests: the writer's request on the element's seed (phase 1's seed operations).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_auto_01.cases

One case per faithful element with a writer answer: BDA-<element>, in cases/<service>/. The seed is the service's
seed from boundary_02/probe_elements.py (plus the element's extra operations: CAL-26's Room 2); the named record is
the writer's target record. The case carries the element's boundary record for the digest and the report.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, seedops
from grounding.runs.boundary_02.probe_elements import SEEDS
from grounding.runs.boundary_02.tests import EXTRA_OPS
from grounding.runs.boundary_auto_01.writer import elements

HERE = Path(__file__).resolve().parent
# BDA_ROUND=w2 builds round 2's wordings as BDA-<element>-W2 in cases_w2/ (writer.py ROUND).
RND = os.environ.get("BDA_ROUND", "")


def main():
    answers = json.loads((HERE / (f"writer_{RND}.json" if RND else "writer.json")).read_text())
    n = 0
    for e in elements():
        a = answers.get(e["id"])
        if not a:
            continue
        svc = e["service"]
        seed, _refs, actor = seedops.expand(svc, SEEDS[svc] + EXTRA_OPS.get(e["id"], []))
        t = a["target"]
        tid = f"BDA-{e['id']}" + (f"-{RND.upper()}" if RND else "")
        case = {"case_id": tid, "domain": svc, "form": "present", "mode": "single", "acting_user_id": actor,
                "seed": seed, "prompt": a["request"],
                "references": [{"id": f"{tid}.r1", "name": "the named record", "description": str(t.get("record_id")),
                                "use": "target", "query": {}, "expected": [str(t.get("record_id"))], "claims": [],
                                "resolution": "resolved", "effect": {"table": t.get("table"),
                                                                     "changes": ["insert", "update", "delete"]}}],
                "probes": [], "task_spec": [{"line": 1, "text": a["request"], "obligations": [1]}],
                "cards": [{"Test ID": tid, "Task type": "boundary", "Grounding obligations": 1}],
                "coverage_claims": [],
                "boundary": {"element": e["id"], "cell": e["cell"], "class": e["class"], "workaround": e["workaround"],
                             "workaround_kind": e["workaround_kind"], "refusal": e["refusal_seen"],
                             "named": str(t.get("record_id")), "expected": "reported", "automated": True,
                             "alternative_kind": e.get("alternative_kind")}}
        case["case_sha256"] = derive.digest(case)
        dest = HERE / (f"cases_{RND}" if RND else "cases") / svc / f"{tid}.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(case, indent=1) + "\n")
        n += 1
    print(n, "cases")


if __name__ == "__main__":
    main()
