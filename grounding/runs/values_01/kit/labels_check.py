"""Recall against the existing blind labels: which value, reply and side-effect issues did the labellers record, and do
this study's checks flag those executions? No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.labels_check

- blind_review_01 records such issues in `secondary_issues` (9 of 200 labels).
- openclaw_eval_01's labels (`eval/labels_*/*_blind.json`) are grounding labels whose notes sometimes mention them; a
  note is read as mentioning one when it matches the patterns below (then every match is listed for a reader).
Only labels on the 3,018 final executions count. A silent label is no evidence that nothing else went wrong: the
labels were written for grounding.

Writes data/labels_check.json.
"""
from __future__ import annotations

import json
import re

from grounding.runs.report_01.kit.common import RUNS, load
from grounding.runs.values_01.kit.common import DATA, executions, read

MENTION = re.compile(r"priorit|wrong value|value|also (?:changed|posted|added|removed|unchecked|set)|side effect|"
                     r"revert|restor|undo|undid|posted a comment|comment it posted|claims?|claimed|falsely|misreport|"
                     r"shared link|\block\b|notif|renamed .* back|icon|assignee", re.I)


def main():
    final = {e["key"]: e for e in executions()}
    values, writes, reply = read("values"), read("writes"), read("reply")

    def flags(key):
        v, w, r = values[key], writes[key], reply[key]
        out = []
        out += [f"V:{x['field']}:{x['verdict']}" for x in v.get("values", []) if x["verdict"] not in ("ok", "normalized")]
        out += [f"S:{k}" for k in ("other_fields", "other_records", "other_tables", "no_net_change", "replica_effects")
                if v.get(k)]
        out += ["T:not_in_diff"] * bool(w.get("not_in_diff"))
        out += [f"R:{f['check']}" for f in r.get("flags", [])]
        return sorted(set(out))

    rows = []
    manifest = {s["blind_id"]: s["key"] for s in load(RUNS / "blind_review_01/manifest.json")["sample"]}
    for lab in load(RUNS / "blind_review_01/effective_labels.json"):
        key = manifest[lab["blind_id"]]
        if key in final and (lab.get("secondary_issues") or MENTION.search(lab.get("note") or "")):
            rows.append({"source": "blind_review_01", "id": lab["blind_id"], "key": key,
                         "secondary_issues": lab.get("secondary_issues"), "note": lab.get("note"),
                         "flags": flags(key)})
    for f in sorted((RUNS / "openclaw_eval_01/eval").glob("labels_*/*_blind.json")):
        for key, lab in load(f).items():
            if key in final and isinstance(lab, dict) and MENTION.search(lab.get("note") or ""):
                rows.append({"source": "openclaw_eval_01", "id": key, "key": key, "note": lab.get("note"),
                             "flags": flags(key)})
    (DATA / "labels_check.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    print(len(rows), "labels mention something beyond grounding (patterns); flagged by a check:",
          sum(1 for r in rows if r["flags"]))
    for r in rows:
        print(f"{r['source'][:8]} {r['id'][:40]:40} flags={r['flags']}\n    {r.get('secondary_issues') or ''} "
              f"{(r['note'] or '')[:260]}")


if __name__ == "__main__":
    main()
