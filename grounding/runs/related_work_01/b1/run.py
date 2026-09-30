"""B1, step 4, for a later session: the items through OpenClaw with their masks, k trials each. Not run here.

    SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py grounding.runs.related_work_01.b1.run \
        --out grounding/runs/related_work_01/b1/runs/<run> [--items selection|all] [--trials 3] [--concurrency 12]
    python -m grounding.runs.related_work_01.b1.oracle --run grounding/runs/related_work_01/b1/runs/<run>

It is openclaw_eval_01's runner, unchanged (the self-hosted Qwen through the proxy, the judge layout, no follow-up,
the frozen suite's rulings, completed attempts never redone), with two hooks set here and no change to shared code:
- every attempt gets the workspace variant "b1:<case_id>", which the runtime records in solver/config.json;
- the state directory, once built, gets the item's mask (install.py), and the attempt records it in
  solver/b1_mask.json.

The cases are the covers exactly as they ran (each attempt's case.json), written to <out>/cases/ at the start.
Start the self-host proxy first (openclaw_eval_01/run.py says how).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from grounding.integrations.agentdiff.runtime import write
from grounding.integrations.openclaw import runtime as oc
from grounding.runs.openclaw_eval_01 import run as base
from grounding.runs.related_work_01.b1.install import apply_mask
from grounding.runs.related_work_01.b1.masks import attempt as source_attempt

HERE = Path(__file__).parent
ITEMS = {i["case_id"]: i for i in json.loads((HERE / "items.json").read_text()) if i["verdict"] == "valid"}
_build_state_dir, _run_attempt = oc.build_state_dir, oc.run_attempt
_masks: dict[str, dict] = {}


def build_state_dir(state, route, domain, variant=None, backend="purdue", neutral=False):
    item = None
    if variant and variant.startswith("b1:"):
        item, variant = ITEMS[variant[3:]], None
    config = _build_state_dir(state, route, domain, variant, backend, neutral)
    if item:
        _masks[str(state)] = {"case_id": item["case_id"], "capability": item["capability"],
                              **apply_mask(state, config, item)}
    return config


def run_attempt(case, attempt, **kw):
    kw["variant"] = f"b1:{case['case_id']}"
    try:
        return _run_attempt(case, attempt, **kw)
    finally:
        record = next((m for m in _masks.values() if m["case_id"] == case["case_id"]), None)
        if record:
            write(attempt / "solver" / "b1_mask.json", record)


def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--items", choices=("selection", "all"), default="selection")
    known, rest = ap.parse_known_args()
    chosen = json.loads((HERE / "selection.json").read_text()) if known.items == "selection" else sorted(ITEMS)
    cases = known.out.resolve() / "cases"
    for cid in chosen:
        item = ITEMS[cid]
        src = source_attempt(item["run"], "t1", cid) / "case.json"
        dest = cases / item["domain"] / f"{cid}.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(src.read_text())
    write(known.out.resolve() / "b1_plan.json", {"items": chosen, "masks": {c: ITEMS[c]["refuse"] for c in chosen},
                                                 "grading": "b1/oracle.py (boundary_02's oracle, F per item)"})
    oc.build_state_dir, oc.run_attempt = build_state_dir, run_attempt
    sys.argv = [sys.argv[0], "--out", str(known.out), "--cases-dir", str(cases), *rest]
    base.main()


if __name__ == "__main__":
    main()
