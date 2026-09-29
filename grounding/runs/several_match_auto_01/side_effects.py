"""The judge's blind spot: changes outside the target table (a comment added, a record created) in trials it passes.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.side_effects

grade.py compares the set of records of the request's kind that were acted on with the targets. A trial can meet
that and still change something else. For every trial the judge passes (complete and clean), this lists the diff's
inserts, updates and deletes in other tables, leaving out the noise the replicas make on any write (etags,
timestamps, sequence numbers, sync tokens, the Box Favorites collection, a Slack reaction row that is the requested
action). A trial with such a change is a candidate false negative; I review each. Writes side_effects.json.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOISE_TABLES = {"calendar_sync_tokens", "box_collections", "box_file_versions", "box_file_contents"}
NOISE_COLS = {"etag", "updated_at", "updatedAt", "sequence", "sequence_id", "modified_at", "content_modified_at",
              "editedAt", "__table__", "tags"}


def main():
    grades = json.loads((HERE / "grades.json").read_text())
    out = {}
    for t in grades["trials"]:
        if t["diligence"] != "complete" or t["discrimination"] != "clean" or t["other_acted"]:
            continue
        tk, cid = t["trial"].split("/")
        att = sorted((HERE / "runs" / t["run"] / tk / cid).glob("attempt-*"))[-1]
        case = json.loads((att / "case.json").read_text())
        table = case["references"][0]["query"]["table"]
        effect = (case["references"][0].get("effect") or {}).get("table")
        diff = (json.loads((att / "environment/diff_run.json").read_text()) or {}).get("diff") or {}
        extra = []
        for kind in ("inserts", "updates", "deletes"):
            for row in diff.get(kind) or []:
                a = row.get("after", row) if kind != "deletes" else row.get("before", row)
                tab = a.get("__table__") or row.get("__table__")
                if tab in NOISE_TABLES or tab in (table, effect):
                    continue
                if kind == "updates":
                    b = row.get("before") or {}
                    cols = [c for c in a if c not in NOISE_COLS and a.get(c) != b.get(c)]
                    if not cols:
                        continue
                    extra.append(f"update {tab} {cols}")
                else:
                    extra.append(f"{kind[:-1]} {tab}")
        if extra:
            out[t["trial"]] = {"extra": extra[:8], "final": t["final"][:300]}
    (HERE / "side_effects.json").write_text(json.dumps(out, indent=1) + "\n")
    print(len(out), "passed trials with changes outside the target table")
    for k, v in out.items():
        print(" ", k, v["extra"][:4])


if __name__ == "__main__":
    main()
