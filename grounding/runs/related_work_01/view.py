"""Show one trial's evidence for labelling by hand: the request, what the test names, the trajectory, the final
answer and the net state changes. No verdict of any grader is read or shown.

    python -m grounding.runs.related_work_01.view RUN_DIR/t1/CASE_ID [--full]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from grounding.runs.boundary_02.oracle import net_changes


def show(case_dir: Path, full: bool = False) -> str:
    att = sorted(case_dir.glob("attempt-*"))[-1]
    case = json.loads((att / "case.json").read_text())
    summary = json.loads((att / "execution_summary.json").read_text())
    record_path = next((p for p in (att / "solver").glob("*.json") if p.name not in ("config.json", "b1_mask.json")),
                       None)
    record = json.loads(record_path.read_text()) if record_path else {}
    out = [f"# {case_dir.parent.name}/{case['case_id']} ({case['domain']}), {att.name}: status {summary.get('status')}, "
           f"termination {summary.get('termination')}, turn {summary.get('turn_durations_s')}",
           f"## Request\n{case['prompt']}"]
    mask = att / "solver" / "b1_mask.json"
    if mask.exists():
        out.append(f"## Masked (B1)\n{json.loads(mask.read_text()).get('refused')}")
    for ref in case.get("references", [])[:4]:
        out.append(f"- reference {ref['id'].split('.')[-1]} ({ref.get('use')}) in {ref['query']['table']}: "
                   f"expected {ref.get('expected')}")
    out.append("## Trajectory")
    limit = 1500 if full else 500
    for s in (record.get("steps") or []) + (record.get("followup_steps") or []):
        args = s.get("arguments") or {}
        cmd = args.get("command") or json.dumps(args)[:300]
        obs = s.get("observation") or {}
        text = obs.get("stdout") if isinstance(obs, dict) else str(obs)
        out.append(f"[{s.get('turn')}] {s.get('tool')}: {cmd[:limit]}")
        if text:
            out.append(f"    -> {str(text)[:limit]}")
        if s.get("text"):
            out.append(f"    says: {s['text'][:limit]}")
    out.append(f"## Final answer\n{(record.get('final') or '').strip()[:3000]}")
    try:
        diff = (json.loads((att / "environment/diff_run.json").read_text()) or {}).get("diff") or {}
        ch = net_changes(diff, set())
        out.append("## Net changes\n" + ("\n".join(f"- {c['kind']} {c['table']} {c['key']} "
                                                   f"{ {k: c['row'].get(k) for k in c['cols']} if c['kind'] == 'update' else ''}"[:400]
                                                   for c in ch) or "(none)"))
    except FileNotFoundError:
        out.append("## Net changes\n(no diff)")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("case_dir", type=Path)
    ap.add_argument("--full", action="store_true")
    args = ap.parse_args()
    print(show(args.case_dir, args.full))


if __name__ == "__main__":
    main()
