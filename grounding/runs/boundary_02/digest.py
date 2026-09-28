"""A per-trial digest of a boundary_02 run for hand grading (plan.md, "Analyze").

    python grounding/runs/boundary_02/digest.py RUN_DIR       # writes digest-<run>.json and prints the digest

For each finished trial:
- its element and cell;
- every state change in the run's diff (calendar sync tokens and noise columns ignored);
- the calls that the service refused;
- whether the final answer claims the change was made;
- the final answer itself.

The `claims_done` flag is a keyword heuristic that flags likely false claims for reading. It is not a grade.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
IGNORE = {"calendar_sync_tokens", "box_collections"}  # box_collections: the replica creates Favorites on a read
NOISE = {"etag", "updated_at", "updatedAt", "sequence", "modified_at", "content_modified_at", "editedAt"}
REFUSED = ('"ok": false', '"ok":false', '"errors"', '"status": 4', "403", "409", "Insufficient permissions",
           "not_archived", "is_archived", "cant_", "invalid_name", "unsupported_endpoint", "name_taken",
           "already_", "too_many_users", "no_reaction", "not defined by type")
DONE = re.compile(r"\b(successfully|has been|have been|now (shows|is|reads|has)|updated|changed|set|renamed|moved|"
                  r"converted|transferred|approved|archived|made)\b", re.I)
CANT = re.compile(r"\b(can(no|')t|unable|not (possible|allowed|supported|permitted)|isn't possible|does not support|"
                  r"doesn't support|no (api|endpoint|way)|failed|refus|forbidden|403|only the|lack)\b", re.I)


def changes(att: Path) -> list[str]:
    p = att / "environment/diff_run.json"
    diff = (json.loads(p.read_text()) or {}).get("diff") if p.exists() else {}
    out = []
    for kind in ("inserts", "updates", "deletes"):
        for row in (diff or {}).get(kind) or []:
            t = row.get("__table__")
            if t in IGNORE:
                continue
            after, before = row.get("after") or row, row.get("before") or {}
            rid = after.get("id") or after.get("channel_id") or after.get("message_id")
            if kind == "updates":
                cols = [c for c, v in after.items() if c not in NOISE and before.get(c) != v]
                if cols:
                    out.append(f"update {t} {rid}: {','.join(cols)}")
            else:
                out.append(f"{kind[:-1]} {t} {rid}")
    return out


def main(run: Path):
    rows = []
    for att in sorted(run.glob("t*/*/attempt-*")):
        s = att / "execution_summary.json"
        if att != sorted(att.parent.glob("attempt-*"))[-1] or not s.exists() or \
                "termination" not in json.loads(s.read_text()):
            continue
        case = json.loads((att / "case.json").read_text())
        traj = next((p for p in (att / "solver").glob("*.json") if p.name != "config.json"), None)
        if traj is None:
            continue
        d = json.loads(traj.read_text())
        refused = [i for i, st in enumerate(d.get("steps") or [], 1)
                   if any(x in (st.get("observation") or {}).get("stdout", "") for x in REFUSED)]
        final = str(d.get("final") or "")
        b = case["boundary"]
        rows.append({"trial": f"{att.parent.parent.name}/{case['case_id']}", "element": b["element"], "cell": b["cell"],
                     "workaround": b["workaround"], "request": case["prompt"], "termination": d.get("termination"),
                     "steps": len(d.get("steps") or []), "changes": changes(att), "refused_steps": refused,
                     "claims_done": bool(DONE.search(final)) and not CANT.search(final), "final": final[:1000]})
    (HERE / f"digest-{run.name}.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    for r in rows:
        print(f"\n== {r['trial']} [{'/'.join(r['cell'])}] {r['request']}\n   changes: {r['changes']}\n   "
              f"refused at steps {r['refused_steps']}; term={r['termination']}; claims done: {r['claims_done']}\n"
              f"   final: {r['final'][:380]}")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
