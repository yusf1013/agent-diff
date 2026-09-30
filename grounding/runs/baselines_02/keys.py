"""From the blind review to runnable, keyed cases: each valid Sonnet test gets the review's answer key as a reference.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.keys POOL REVIEW.json

- **Per arm, in baselines_01's shape:** `runs/<gen run>/review.json` holds the review's records with `test` set to the
  case id (the pool id kept), so baselines_01's structure measures (`compare.py`'s `structure`, `variety.py`) and
  `summarize_labels.py` read them unchanged.
- **The answer key** is one reference per test, as our cases carry them: `expected` is the review's intended target
  (empty for a test with no right record), `claims` are the review's near misses (the record, the fact of the one
  condition it fails, the family, the note), `query.table` is the table of the records acted on, and `effect` says
  how the diff shows an action on them (the table written, the change, and the column that points back to the record
  for an insert). The review wrote the key from the request, not from the test's own assertions.
- **Keyed cases** go to `runs/<suite>/<domain>/<case_id>.json`, valid tests only, with `case_sha256` recomputed.
  The runner never passes `references` or `baseline` to the agent under test (`openclaw/runtime.py`, `solver_case`).
- **Our tests in the pool** are only compared with their mechanical claims (the calibration of review rule 8):
  `runs/<pool>/calibration.json`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import derive

HERE = Path(__file__).resolve().parent
SUITES = {"SN0M": "suite_sn0m_01", "SN1M": "suite_sn1m_01"}


def reference(case: dict, rec: dict) -> dict:
    return {"id": f"{case['case_id']}.r1", "name": "the record the request acts on",
            "description": rec.get("note") or "the record the request acts on", "use": "target",
            "query": {"table": rec["table"], "key": ["id"]}, "expected": [str(x) for x in rec["target"]],
            "claims": [{"requirement": n["fact"], "witness": str(n["record"]), "family": n["family"],
                        "explanation": n["note"]} for n in rec["near_misses"]],
            "written": [], "effect": rec["effect"], "labels": rec.get("labels") or {}}


def calibration(case: dict, rec: dict) -> dict:
    """Our test's mechanical claims against the hand review: same target, same near misses, same facts."""
    ref = case["references"][0]
    mine = {str(n["record"]): n["fact"] for n in rec["near_misses"]}
    theirs = {str(c["witness"]): c["requirement"] for c in ref["claims"]}
    return {"case_id": case["case_id"], "form": case["form"], "valid_by_review": rec["valid"],
            "target_same": sorted(map(str, ref["expected"])) == sorted(rec["target"]),
            "near_misses_same_records": sorted(mine) == sorted(theirs),
            "facts_same": {w: mine[w] == theirs[w] for w in mine.keys() & theirs.keys()},
            "claimed_not_found": sorted(theirs.keys() - mine.keys()), "found_not_claimed": sorted(mine.keys() - theirs.keys()),
            "families_mine": {str(n["record"]): n["family"] for n in rec["near_misses"]},
            "families_claimed": {str(c["witness"]): c.get("family") for c in ref["claims"]}}


def main():
    pool, review_path = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    manifest = json.loads((pool / "manifest.json").read_text())
    review = {r["pool_id"]: r for r in json.loads(review_path.read_text())}
    missing = sorted(set(manifest) - set(review))
    if missing:
        raise SystemExit(f"not reviewed yet: {missing}")
    per_arm, cal, written = {}, [], {}
    for pid, entry in sorted(manifest.items()):
        rec, case = review[pid], json.loads(Path(entry["path"]).read_text())
        if entry["source"] == "ours":
            cal.append({"pool_id": pid, **calibration(case, rec)})
            continue
        gen_run = Path(entry["path"]).parents[2]
        per_arm.setdefault(gen_run, []).append({**rec, "test": case["case_id"]})
        if not rec["valid"]:
            continue
        keyed = {**case, "references": [reference(case, rec)]}
        keyed.pop("case_sha256", None)
        keyed["case_sha256"] = derive.digest(keyed)
        dest = HERE / "runs" / SUITES[entry["source"]] / case["domain"] / f"{case['case_id']}.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(keyed, indent=1, ensure_ascii=False) + "\n")
        written[entry["source"]] = written.get(entry["source"], 0) + 1
    for gen_run, recs in per_arm.items():
        (gen_run / "review.json").write_text(json.dumps(sorted(recs, key=lambda r: r["test"]), indent=1,
                                                        ensure_ascii=False) + "\n")
    (pool / "calibration.json").write_text(json.dumps(cal, indent=1) + "\n")
    print(json.dumps({"keyed_valid_cases": written, "reviewed": {str(k.name): len(v) for k, v in per_arm.items()},
                      "ours_calibrated": len(cal)}))


if __name__ == "__main__":
    main()
