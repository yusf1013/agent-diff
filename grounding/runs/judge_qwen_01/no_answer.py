"""How each judge treats executions that ended without a user-facing answer (no model calls).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.judge_qwen_01.no_answer --out runs/selfhost

An execution "ended without an answer" when its final response is empty or is one of OpenClaw's failure notices
(a timed-out request, "Agent couldn't generate a response", "LLM request failed"). For those, the prompt's
not_established covers "a timeout or turn limit before any decision". Counts Muse's outcomes on all 2,139 judged
executions and Qwen's on those it has judged, with each execution's budget status (rulings.over_budget).
Writes <out>/no_answer.json.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

from grounding.runs.judge_qwen_01.common import HERE, attempt_path, judged_keys, kind_of, load, muse_verdict
from grounding.runs.openclaw_eval_01 import rulings

NOTICE = re.compile(r"request timed out|couldn't generate a response|llm request failed", re.I)


def final_answer(attempt: Path) -> str:
    path = attempt / "solver" / "final_response.md"
    if path.exists():
        return path.read_text().strip()
    records = [p for p in (attempt / "solver").glob("*.json") if p.name != "config.json"]
    return (load(records[0]).get("final") or "").strip() if records else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    out = args.out if args.out.is_absolute() else HERE / args.out
    rows = []
    for key in judged_keys():
        attempt = attempt_path(key)
        text = final_answer(attempt)
        if text and not NOTICE.search(text[:400]):
            continue
        q = out / key / "verdict.json"
        rows.append({"key": key, "kind": kind_of(key), "over_budget": rulings.over_budget(attempt),
                     "final": text[:120], "muse": muse_verdict(key).get("outcome"),
                     "qwen": load(q).get("outcome") if q.exists() else None})
    judged_by_both = [r for r in rows if r["qwen"]]
    summary = {"executions_without_an_answer": len(rows),
               "over_budget": sum(r["over_budget"] for r in rows),
               "muse_outcomes": dict(Counter(r["muse"] for r in rows)),
               "muse_outcomes_within_budget": dict(Counter(r["muse"] for r in rows if not r["over_budget"])),
               "judged_by_qwen": len(judged_by_both),
               "qwen_outcomes": dict(Counter(r["qwen"] for r in judged_by_both)),
               "muse_outcomes_same_executions": dict(Counter(r["muse"] for r in judged_by_both)),
               "muse_outcomes_by_kind": {k: dict(Counter(r["muse"] for r in rows if r["kind"] == k))
                                         for k in ("regular", "absence", "underspecified")}}
    (out / "no_answer.json").write_text(json.dumps({"summary": summary, "rows": rows}, indent=1) + "\n")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
