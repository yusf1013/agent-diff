"""Attribute each executed case to the facts it exposed (diff-based, then reviewed manually).

    python -m grounding.runs.fact_coverage_01.pilot.analyze <run dir> [...]

For every reference with an `effect` locator, the changed/inserted/deleted rows of
the effect table identify which candidates the agent acted on. Acting on a claim's
witness is attributed to that claim's requirement (the fact the agent dropped or
confused). Read-only references are matched by candidate labels in the final
answer. These are provisional labels for manual confirmation, not verdicts.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def rows_by_key(rows, key):
    out = {}
    for r in rows:
        k = r[key[0]] if len(key) == 1 else json.dumps({x: r[x] for x in key}, sort_keys=True)
        out[str(k)] = r
    return out


def changed(initial, final, table, key, field=None, columns=None):
    """Handles of rows inserted, deleted or updated in `table` (optionally mapped through `field`)."""
    a = rows_by_key(initial.get(table, []), key)
    b = rows_by_key(final.get(table, []), key)
    out = {"insert": set(), "delete": set(), "update": set()}
    for k in b.keys() - a.keys():
        out["insert"].add(str(b[k][field]) if field else k)
    for k in a.keys() - b.keys():
        out["delete"].add(str(a[k][field]) if field else k)
    for k in a.keys() & b.keys():
        if json.dumps(a[k], sort_keys=True, default=str) != json.dumps(b[k], sort_keys=True, default=str):
            diffs = sorted(c for c in set(a[k]) | set(b[k]) if a[k].get(c) != b[k].get(c)
                           and c not in {"modified_at", "updated_at", "etag", "sequence_id", "updatedAt"})
            if diffs and (not columns or set(diffs) & set(columns)):
                out["update"].add(str(b[k][field]) if field else k)
    return out


def refresh(case):
    """Same request and seed as the current case file: reuse its newer effect locators/labels."""
    current = HERE / "cases" / case["domain"] / f"{case['case_id']}.json"
    if current.exists():
        newer = json.loads(current.read_text())
        if newer["prompt"] == case["prompt"] and newer["seed"] == case["seed"]:
            return {**case, "references": newer["references"]}
    return case


def attribute(case, attempt: Path):
    case = refresh(case)
    env = attempt / "environment"
    record_path = attempt / "solver" / f"{case['case_id']}.json"
    record_path = record_path if record_path.exists() else None
    final_text = ""
    if (attempt / "solver/final_response.md").exists():
        final_text = (attempt / "solver/final_response.md").read_text()
    try:
        initial = json.loads((env / "initial_state.json").read_text())
        final = json.loads((env / "final_state.json").read_text())
    except FileNotFoundError:
        return {"case_id": case["case_id"], "status": "no_state"}
    results = []
    for ref in case["references"]:
        witnesses = {str(c["witness"]): c["requirement"] for c in ref["claims"]}
        expected = {str(x) for x in ref["expected"]}
        labels = ref.get("labels", {})
        effect = ref.get("effect")
        acted = set()
        if effect:
            ch = changed(initial, final, effect["table"], effect.get("key", ["id"]), effect.get("field"),
                         effect.get("columns"))
            for kind in effect.get("changes", ["insert", "delete", "update"]):
                acted |= ch[kind]
            # keep every acted-on handle: unclaimed or unrelated records land in "other"
        elif labels and final_text:
            acted = {h for h, label in labels.items() if label.lower() in final_text.lower()}
        wrong = sorted(acted - expected)
        results.append({
            "reference": ref["id"], "expected": sorted(expected), "acted": sorted(acted),
            "exposed": [{"witness": w, "requirement": witnesses[w]} for w in wrong if w in witnesses],
            "other": [w for w in wrong if w not in witnesses],
            "missed": sorted(expected - acted),
        })
    record = json.loads(record_path.read_text()) if record_path else {}
    termination = record.get("termination")
    for r in results:
        # Provisional outcome; absence is only credited when the run finished and said so (checked manually).
        if r["exposed"] or r["other"]:
            r["provisional"] = "incorrect"
        elif r["missed"]:
            r["provisional"] = "not_established" if termination != "done" else "incomplete"
        elif not r["expected"]:
            r["provisional"] = "absent_reported?" if termination == "done" else "not_established"
        else:
            r["provisional"] = "correct"
    return {"case_id": case["case_id"], "domain": case["domain"], "form": case["form"],
            "termination": record.get("termination"), "turns": len(record.get("steps", [])),
            "final": final_text.strip()[:600], "references": results}


def main():
    rows = []
    for run in sys.argv[1:]:
        for attempt in sorted(Path(run).glob("*/attempt-*")):
            summary = json.loads((attempt / "execution_summary.json").read_text())
            if summary.get("status") != "completed":
                rows.append({"case_id": summary["case_id"], "status": summary.get("status"), "error": summary.get("error")})
                continue
            case = json.loads((attempt / "case.json").read_text())
            rows.append(attribute(case, attempt))
    print(json.dumps(rows, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
