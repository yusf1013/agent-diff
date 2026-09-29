"""Model spend for the generation and judging agents, from every `calls.jsonl` under grounding/runs in this branch,
by component, at list price and as billed. Muse's calls carry both; autogen_01's Sonnet calls ran on the
subscription (billed nothing) and carry the list price only. The self-hosted Qwen (the agent under test on
OpenClaw) has no per-call charge.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.costs

Writes numbers/costs.json.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict

from grounding.runs.report_01.kit.common import RUNS, write

# Component by folder (the first pattern that matches, in order).
COMPONENTS = [
    ("Sonnet (autogen_01): generation, reader and judge, all runs", r"^autogen_01/"),
    ("Muse: scenario generation (writer and cold reader)", r"^(autogen_02/runs/phase4_gen|completion_01/runs/gen_0)"),
    ("Muse: policy variants (drop-F wording and reader; clones)",
     r"^(autogen_02/runs/phase[34]_(dropf|clone)|completion_01/runs/dropf_)"),
    ("Muse: drop-F and clone calibration (Phase 2)", r"^autogen_02/runs/phase2_"),
    ("Muse: judge v2 on OpenClaw trials", r"^openclaw_eval_01/runs/"),
    ("Muse: judge v2 on the toy harness's trials (Qwen, Purdue)",
     r"^autogen_02/runs/(judge2_phase|judge2_panel|phase4/judged)"),
    ("Muse: judge and generator development (smoke tests, judge v1, settings checks)",
     r"^(autogen_02/runs/(muse_|judge1_)|roadmap_01/)"),
    ("Muse: judge baselines J0 and J1 (6c)", r"^judge_baselines_01/"),
]


def main():
    rows = defaultdict(lambda: {"calls": 0, "list_usd": 0.0, "billed_usd": 0.0, "folders": set()})
    unmatched = set()
    for log in sorted(RUNS.rglob("calls.jsonl")):
        folder = str(log.parent.relative_to(RUNS))
        comp = next((name for name, rx in COMPONENTS if re.search(rx, folder)), None)
        if comp is None:
            unmatched.add(folder)
            continue
        for line in log.read_text().splitlines():
            try:
                d = json.loads(line)
            except ValueError:
                continue
            r = rows[comp]
            r["calls"] += 1
            r["list_usd"] += d.get("cost_usd_list_price") or d.get("total_cost_usd") or 0
            r["billed_usd"] += d.get("cost_usd_billed") or 0
            r["folders"].add(folder)
    out = {name: {"calls": r["calls"], "list_usd": round(r["list_usd"], 2), "billed_usd": round(r["billed_usd"], 2),
                  "folders": sorted(r["folders"])} for name, r in rows.items()}
    muse = [v for k, v in out.items() if k.startswith("Muse")]
    out["Muse total"] = {"calls": sum(v["calls"] for v in muse), "list_usd": round(sum(v["list_usd"] for v in muse), 2),
                         "billed_usd": round(sum(v["billed_usd"] for v in muse), 2)}
    out["unmatched_folders"] = sorted(unmatched)
    print(write("costs", out))
    for k, v in out.items():
        print(k, {x: y for x, y in v.items() if x != "folders"} if isinstance(v, dict) else v)


if __name__ == "__main__":
    main()
