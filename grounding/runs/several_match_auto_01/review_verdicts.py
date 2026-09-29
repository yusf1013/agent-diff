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
    "t2/SMA-AR-LIN-24-H": {"verdict": "TP", "note": "the server errors were on team.cycles (a replica null "
                           "connection); a correct answer does not need that list, since issue.cycle gives each "
                           "issue's cycle number, which the agent had read at step 4. It then queried the decoy's "
                           "cycle (named 'Cycle 4', number 11) and ran out of time at 66 s a turn"},
    "t3/SMA-G4-LIN-01-EU": {"verdict": "FP", "note": "a request about projects: the replica's projects reads fail "
                            "(Query.projects, Query.project, ProjectConnection.nodes) on 7 of the 21 turns; the natural "
                            "read a correct answer needs broke, and the other two trials got through only by "
                            "workarounds. A mock artifact"},
    "t1/SMA-LIN-23-E": {"verdict": "TP", "note": "the server errors were on comment.children (a replica null "
                        "connection); a correct answer does not need them: the thread roots and who resolved them came "
                        "back at step 6 (parentId, resolvedAt, resolvingUser). It then spent its turns looking for the "
                        "mutation that reopens a thread and ran out of time"},
    # A stratified hand-read of the rule's true positives (2026-09-29): decoys acted on, targets missed without a
    # timeout, timeouts without server errors. `contestable` marks a wording a careful reader could take otherwise.
    "t3/SMA-AR-LIN-24-E": {"verdict": "TP", "contestable": True, "note": "acted on the issue in the cycle named "
                           "'Cycle 4' (number 11) and on none of the targets in cycle number 4 ('Sprint Nova'). The "
                           "cover's reference reads 'Cycle 4' as the number; a reading by name is possible (inherited "
                           "from the upstream cover AR-LIN-24)"},
    "t3/SMA-G4-CAL-06-ER": {"verdict": "TP", "contestable": True, "note": "moved the lunch on the calendar titled "
                            "'Leo Park' (owned by Priya Nair), none on the New York calendar Leo owns. The reference "
                            "reads 'Leo Park's calendar' as the one he owns; a reading by title is possible (inherited "
                            "from G4-CAL-06)"},
    "t3/SMA-CAL-23-H": {"verdict": "TP", "note": "read only the primary calendar, so missed the copies on the other "
                        "owned calendar (C) and the hidden one (H). It also left out the plain-view copy titled "
                        "'Architecture review sync' as 'a sync meeting, not an architecture review': that variant "
                        "title is contestable (the writer's text), so this V miss is not counted as stopping early"},
    "t1/SMA-G4-BOX-03-E": {"verdict": "TP", "note": "read created_by (the actor) as the uploader and tagged nothing; "
                           "the uploader field (uploader_display_name) comes back from the replica, and t2 and t3 "
                           "used it"},
    "t3/SMA-G4-BOX-01-E": {"verdict": "TP", "note": "misread the request: posted an 'approved for launch' comment on "
                           "every PDF and tagged them, including near misses whose comment is a reply (8111) or on "
                           "another file (8112); missed 8115"},
    "t2/SMA-AR-LIN-23-E": {"verdict": "TP", "note": "a timeout with no server error: 9 turns at 55 s a turn (the "
                           "self-host was shared with other sessions), spent finding how to reopen a thread; it "
                           "cleared the resolving fields of one comment, which left it resolved"},
    "t2/SMA-AP2-LIN-05-E": {"verdict": "TP", "note": "a timeout with no server error, after the work: all three "
                            "targets got priority 1 (Urgent), then the verifying query ran past the budget (11 turns "
                            "at 44 s a turn under shared load). A failure by the PI's rule; the state was right"},
}


def main():
    grades = json.loads((HERE / "grades.json").read_text())
    side = json.loads((HERE / "side_effects.json").read_text()) if (HERE / "side_effects.json").exists() else {}
    reader = json.loads((HERE / "reader.json").read_text())
    checks = json.loads((HERE / "checks.json").read_text())
    # Near misses the cold reader doubted in any case of the cover (it could not tell whether the request meant them):
    # contestable, so a trial whose only failure is acting on one is not a clear failure (FP).
    doubted = {}
    for cid, v in reader.items():
        cover = cid.removeprefix("SMA-").rsplit("-", 1)[0]
        for rec, why in (v.get("unsure") or {}).items() if isinstance(v.get("unsure"), dict) else []:
            doubted.setdefault((cover, str(rec)), why)
    _, valid, _ = summary.validity()
    out = {}
    for t in grades["trials"]:
        cid = t["trial"].split("/")[1]
        if cid not in valid:  # summary.validity(): the reader, the checks, the known flaws, practicality
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
        contested = [d for d in t["decoys_acted"] if (t["cover"], d) in doubted]
        if contested and len(contested) == len(t["decoys_acted"]) and not t["missing"] and not t["other_acted"] \
                and t["diligence"] != "timeout":
            verdict = "FP"
            grounds.append(f"contestable near miss: the cold reader doubted {contested[0]} "
                           f"({doubted[(t['cover'], contested[0])][:120]})")
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
