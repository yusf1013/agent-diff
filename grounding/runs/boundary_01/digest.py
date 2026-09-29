"""A per-trial digest of the boundary runs for hand grading (plan.md, "Grading").

    python grounding/runs/boundary_01/digest.py [RUN_DIR]      # default runs/main

For each trial: the test's cell and kind, every state change in the run's diff (tables and rows; calendar sync tokens
are ignored, a read side effect of the replica), the API calls that the service refused, and the final answer.
The grades themselves are written by hand into grades.json after reading this digest and the trajectories.
Writes digest.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
IGNORE = {"calendar_sync_tokens"}
REFUSED = ("\"ok\": false", "\"ok\":false", "\"errors\"", "403", "Insufficient permissions", "not_archived",
           "is_archived", "cant_update_message", "cant_delete_message", "invalid_name")


def changes(att: Path) -> list[dict]:
    diff = (json.loads((att / "environment/diff_run.json").read_text()) or {}).get("diff") or {}
    out = []
    for kind in ("inserts", "updates", "deletes"):
        for row in diff.get(kind) or []:
            if row.get("__table__") in IGNORE:
                continue
            after, before = row.get("after") or row, row.get("before") or {}
            changed = {k: [before.get(k), v] for k, v in after.items() if before and before.get(k) != v}
            rid = after.get("id") or after.get("channel_id") or after.get("message_id")
            out.append({"kind": kind[:-1], "table": row.get("__table__"), "id": rid,
                        "fields": changed if kind == "updates" else None})
    return out


def main(run: Path):
    rows = []
    for att in sorted(run.glob("t*/*/attempt-*")):
        summary_p = att / "execution_summary.json"
        if att != sorted(att.parent.glob("attempt-*"))[-1] or not summary_p.exists() or \
                "termination" not in json.loads(summary_p.read_text()):  # still running
            continue
        case = json.loads((att / "case.json").read_text())
        traj = next((p for p in (att / "solver").glob("*.json") if p.name != "config.json"), None)
        if traj is None:  # the episode failed before the solver ran; the retry pass reruns it
            summary = json.loads((att / "execution_summary.json").read_text())
            print(f"\n== {att.relative_to(run)}: no trajectory ({summary.get('status')}: {summary.get('error')})")
            continue
        d = json.loads(traj.read_text())
        refused = []
        for i, s in enumerate(d.get("steps") or [], 1):
            o = (s.get("observation") or {}).get("stdout", "")
            if any(x in o for x in REFUSED):
                refused.append({"step": i, "call": (s.get("action") or "")[:220], "response": o[:220]})
        b = case["boundary"]
        rows.append({"trial": f"{att.parent.parent.name}/{case['case_id']}", "cell": b["cell"], "kind": b["kind"],
                     "class": b["class"], "request": case["prompt"], "named": b["named"], "decoys": b["decoys"],
                     "termination": d.get("termination"), "steps": len(d.get("steps") or []),
                     "changes": changes(att), "refused": refused, "final": str(d.get("final") or "")[:900]})
    (HERE / "digest.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    for r in rows:
        ch = [(c["kind"], c["table"], c["id"], list((c["fields"] or {}).keys())[:4]) for c in r["changes"]]
        print(f"\n== {r['trial']} [{r['kind']}] {r['request']}\n   changes: {ch}\n   refused: "
              f"{[x['step'] for x in r['refused']]}  term={r['termination']} steps={r['steps']}\n   final: "
              f"{r['final'][:420]}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "runs/main")
