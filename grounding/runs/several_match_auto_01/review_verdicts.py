"""Record the review of the judge's reported failures (true or false positives) and of the passes (false negatives).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.review_verdicts

For every trial the judge fails on a valid case (summary.py's validity), the ground is checked:
- a near miss or another record acted on: it fails a condition of the reference query (fdc) -> TP; a record that
  meets every condition would mean the targets are incomplete -> FP;
- a missed target: the case is valid and the target meets every condition -> TP, unless the trajectory holds a
  replica server error (a call the real service would answer) -> FP (a mock artifact);
- a timeout: a failure by the PI's rule -> TP, unless replica server errors -> FP.
The rules' verdicts are recorded with their grounds; `note` says where I read the trajectory myself. Every passed
trial is checked for changes outside the target table (side_effects.json); such a change would be a false negative.
Writes review.json.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from grounding.runs.fact_coverage_01 import fdc
from grounding.runs.several_match_auto_01 import summary
from grounding.runs.several_match_auto_01.review import failing_conditions

HERE = Path(__file__).resolve().parent
SERVER_ERROR = re.compile(r"Cannot return null for non-nullable|internal_error|Internal Server Error")
# Trajectories I read myself (the rules' verdicts confirmed or overturned), with what I found. The void rule (a mock
# artifact) applies only when the replica's server error was on a call a correct answer needs.
READ = {
    "t1/SMA-AP2-LIN-01-E": {"verdict": "FP", "note": "the condition names a project; the replica's projects query "
                            "fails (Query.projects, ProjectConnection.nodes): a needed read broke, a mock artifact"},
    "t3/SMA-AP2-LIN-05-E": {"verdict": "FP", "note": "the condition is Priya's comment; the replica's comments query "
                            "fails (CommentConnection.nodes): a needed read broke, a mock artifact"},
    "t1/SMA-AP2-LIN-05-H": {"verdict": "TP", "note": "the server error was on issuePriorityValues, which a correct "
                            "answer does not need; the timeout stands"},
}


def main():
    grades = json.loads((HERE / "grades.json").read_text())
    side = json.loads((HERE / "side_effects.json").read_text()) if (HERE / "side_effects.json").exists() else {}
    reader = json.loads((HERE / "reader.json").read_text())
    checks = json.loads((HERE / "checks.json").read_text())
    out = {}
    for t in grades["trials"]:
        cid = t["trial"].split("/")[1]
        if not (reader.get(cid) or {}).get("agreed") or cid in summary.FLAWED or \
                (cid.rsplit("-", 1)[1].startswith("H") and not (checks.get(cid) or {}).get("thorough_finds_all")):
            continue
        tk = t["trial"].split("/")[0]
        att = sorted((HERE / "runs" / t["run"] / tk / cid).glob("attempt-*"))[-1]
        failed = t["diligence"] != "complete" or t["discrimination"] != "clean" or t["other_acted"]
        if not failed:
            out[t["trial"]] = {"sample": "pass", "verdict": "FN" if t["trial"] in side else "TN",
                               "ground": side.get(t["trial"], {}).get("extra", [])}
            continue
        case = json.loads((att / "case.json").read_text())
        q, seed = case["references"][0]["query"], case["seed"]
        rows = {str(fdc.handle(q, r)): r for r in seed.get(q["table"]) or []}
        traj = next(p for p in (att / "solver").glob("*.json") if p.name != "config.json").read_text()
        errors = len(SERVER_ERROR.findall(traj))
        grounds, verdict = [], "TP"
        for d in list(t["decoys_acted"]) + t["other_acted"]:
            fails = failing_conditions(seed, q, rows[d]) if d in rows else ["not a record of the kind"]
            grounds.append(f"acted on {d}: fails {fails}")
            if not fails:
                verdict = "FP"
        for m, place in t["missing"].items():
            grounds.append(f"missed {m} ({place}): {'seen' if m in traj else 'never seen'} in the trajectory")
        if t["diligence"] == "timeout":
            grounds.append("timeout")
        if errors and (t["missing"] or t["diligence"] == "timeout") and not t["decoys_acted"]:
            verdict = "FP"
            grounds.append(f"replica server errors in the trajectory: {errors} (a mock artifact)")
        out[t["trial"]] = {"verdict": READ.get(t["trial"], {}).get("verdict", verdict), "grounds": grounds,
                           "note": READ.get(t["trial"], {}).get("note", "")}
    (HERE / "review.json").write_text(json.dumps(out, indent=1) + "\n")
    fails = [v for v in out.values() if v.get("verdict") in ("TP", "FP")]
    print(len(fails), "failures reviewed:", sum(1 for v in fails if v["verdict"] == "TP"), "TP,",
          sum(1 for v in fails if v["verdict"] == "FP"), "FP;", sum(1 for v in out.values() if v.get("sample")),
          "passes checked:", sum(1 for v in out.values() if v.get("verdict") == "FN"), "FN")
    for k, v in out.items():
        if v.get("verdict") == "FP":
            print("  FP", k, v["grounds"][-2:])


if __name__ == "__main__":
    main()
