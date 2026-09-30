"""Print an accepted scenario for my validity review: the generation history, the request and conditions, the target
and every near miss with the writer's explanation and any reader flag, then every seed row, compactly (bookkeeping
fields left out). Only I read this; it never reaches an agent. No model calls; plain python3 is enough.

    python3 grounding/runs/regen_01/view.py SCENARIO_ID [ROW_WIDTH]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKIP = {"etag", "sequence", "ical_uid", "organizationId", "customerTicketCount", "priorityLabel", "sortOrder",
        "progress", "currentProgress", "progressHistory", "completedIssueCountHistory", "completedScopeHistory",
        "inProgressScopeHistory", "issueCountHistory", "scopeHistory", "trashed_at", "purged_at", "item_status",
        "sequence_id", "content_created_at", "content_modified_at", "boardOrder", "subIssueSortOrder",
        "prioritySortOrder", "creator_display_name", "organizer_display_name", "html_link", "hangout_link_meta",
        "color", "icon", "created_by_display_name"}


def compact(row: dict, width: int) -> str:
    kept = {k: v for k, v in row.items() if k not in SKIP and v not in (None, "", [], {})}
    text = json.dumps(kept, ensure_ascii=False)
    return text if len(text) <= width else text[:width] + "…"


def main():
    sid = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    folders = sorted(p for p in (HERE / "runs").glob(f"gen_*/{sid}") if (p / "outcome.json").exists())
    for folder in folders:
        o = json.loads((folder / "outcome.json").read_text())
        print(f"## {sid} in {folder.parent.name} [{o['status']}] v{o['versions']} (checks {o['check_rounds']}, "
              f"reader {o['reader_rounds']}, {o['seconds']}s) brief {o['brief']['facts']}")
        for h in o["history"]:
            if h.get("problems"):
                print(f"   v{h['version']} {h['stage']}: " + " | ".join(p[:300] for p in h["problems"]))
        if not (folder / "case.json").exists():
            continue
        case = json.loads((folder / "case.json").read_text())
        ref = case["references"][0]
        print(f"REQUEST: {case['prompt']}\nACTOR: {case.get('acting_user_id')}  WRITE: {case.get('write_check')}")
        for c in case.get("conditions", []):
            print(f"  {c['id']}: {c['text']}  {c['facts']}")
        print(f"  TARGET {ref['expected']}")
        for cl in ref["claims"]:
            flag = f"\n      [reader: {cl['contestable']}]" if cl.get("contestable") else ""
            print(f"  NEAR MISS {cl['witness']} ({cl['requirement']}, {cl.get('family')}): {cl.get('explanation')}{flag}")
        for table, rows in case["seed"].items():
            if not isinstance(rows, list):
                continue
            print(f"-- {table} ({len(rows)})")
            for r in rows:
                print("   " + compact(r, width))


if __name__ == "__main__":
    main()
