"""Cycle 2, content ablation: plain twins of our probes. Each twin is the same probe (same request, same seed) except
that its near miss no longer offers the substitute: it fails the same condition with simply another value (F0).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_01.plain_twins

Sample (plain_pick.json): F1-F8 probes of the frozen suite that exposed a fact on OpenClaw in full_02 (adjudicated),
flawed scenarios left out, a seeded draw stratified by family. The question it answers: of the facts our probes
exposed, would a plain near miss on the same fact, in the same test, have exposed them too? Both arms run again
the same day: `ablation/alt/` holds the original probes unchanged, `ablation/plain/` the twins.

EDITS are mine, by hand, from each probe's claim; each keeps every other condition true of the near miss.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

from grounding.runs.autogen_01.kit import derive

HERE = Path(__file__).resolve().parent
SUITE = HERE.parent / "openclaw_eval_01" / "suite" / "cases"
OUT = HERE / "ablation"

# case id -> (note, [("set", table, match, values) | ("delete", table, match)])
EDITS = {
    "P-AR-BOX-21-I11": ("the folder was modified on June 12, so no date of it is June 3",
                        [("set", "box_folders", {"id": "9501"}, {"modified_at": "2026-06-12T09:00:00+00:00"})]),
    "P-AR-SLK-23-I11": ("hr-general's topic no longer mentions onboarding",
                        [("set", "channels", {"channel_id": "C_HRGEN"}, {"topic_text": "People team updates"})]),
    "P-G4-BOX-04-I14": ("Priya both created and assigned the task; Leo appears nowhere on it",
                        [("set", "box_tasks", {"id": "9105"}, {"created_by_id": "30000000006"})]),
    "P-AP-BOX-01-I14": ("modified in March, far before the August 15 cutoff",
                        [("set", "box_folders", {"id": "9005"}, {"modified_at": "2026-03-02T09:00:00+00:00"})]),
    "P-AP-LIN-05-I11": ("Priya's comment was posted January 14 and resolved January 15; no March date",
                        [("set", "comments", {"id": "c-2"}, {"createdAt": "2026-01-14T09:15:00",
                                                             "updatedAt": "2026-01-14T09:15:00",
                                                             "resolvedAt": "2026-01-15T11:00:00"})]),
    "P-AP-SLK-01-I13": ("the eyes reaction is Leo Park's, not a look-alike account's",
                        [("set", "message_reactions", {"message_id": "1772378100.000004", "user_id": "U_NADIA2"},
                          {"user_id": "U_LEO"})]),
    "P-G4-LIN-01-I11": ("Beacon Refresh's milestone is named Harbor launch; no Meridian",
                        [("set", "project_milestones", {"id": "m-beacon1"}, {"name": "Harbor launch"})]),
    "P-AR-BOX-23-I14": ("two top-level comments and no reply: simply another count",
                        [("delete", "box_comments", {"id": "82143"}),
                         ("set", "box_files", {"id": "8214"}, {"comment_count": 2})]),
    "P-AR-BOX-24-I14": ("the task has no due date, so June 3 appears nowhere on it",
                        [("set", "box_tasks", {"id": "9105"}, {"due_at": None})]),
    "P-G4-BOX-08-I12": ("Leo added the brand guidelines item too; Maya appears nowhere on the hub",
                        [("set", "box_hub_items", {"id": "8303"}, {"added_by_id": "30000000004"})]),
    "P-G4-BOX-01-I11": ("Dana's approving reply is gone; only Priya's question remains",
                        [("delete", "box_comments", {"id": "81204"}),
                         ("set", "box_files", {"id": "8111"}, {"comment_count": 1})]),
    "P-G4-BOX-01-I12": ("Leo's comment says something else; no comment says 'approved for launch'",
                        [("set", "box_comments", {"id": "81206"}, {"message": "Budget numbers look fine."})]),
}


def matches(row: dict, match: dict) -> bool:
    return all(str(row.get(k)) == str(v) for k, v in match.items())


def apply(case: dict, edits: list) -> dict:
    twin = copy.deepcopy(case)
    for edit in edits:
        kind, table, match = edit[0], edit[1], edit[2]
        rows = twin["seed"][table]
        hits = [r for r in rows if matches(r, match)]
        if len(hits) != 1:
            raise SystemExit(f"{case['case_id']}: {table} {match} matches {len(hits)} rows")
        if kind == "delete":
            rows.remove(hits[0])
        else:
            for k in edit[3]:
                if k not in hits[0]:
                    raise SystemExit(f"{case['case_id']}: {table} has no column {k}")
            hits[0].update(edit[3])
    return twin


def main():
    pick = json.loads((HERE / "plain_pick.json").read_text())["pick"]
    wanted = sorted(c for ids in pick.values() for c in ids)
    if sorted(EDITS) != wanted:
        raise SystemExit(f"EDITS and the pick differ: {sorted(set(EDITS) ^ set(wanted))}")
    for cid in wanted:
        path = next(SUITE.glob(f"*/{cid}.json"))
        case = json.loads(path.read_text())
        domain = case["domain"]
        (OUT / "alt" / domain).mkdir(parents=True, exist_ok=True)
        (OUT / "alt" / domain / path.name).write_text(path.read_text())
        note, edits = EDITS[cid]
        twin = apply(case, edits)
        twin["case_id"] = f"{cid}-PL"
        for ref in twin.get("references", []):
            for claim in ref.get("claims", []):
                claim["family"] = "F0"
                claim["explanation"] = f"Plain twin: {note}."
        twin["plain_twin"] = {"of": cid, "note": note, "edits": [list(e) for e in edits]}
        twin["case_sha256"] = derive.digest({k: v for k, v in twin.items() if k != "case_sha256"})
        (OUT / "plain" / domain).mkdir(parents=True, exist_ok=True)
        (OUT / "plain" / domain / f"{twin['case_id']}.json").write_text(
            json.dumps(twin, indent=1, ensure_ascii=False) + "\n")
        print(cid, "->", twin["case_id"], "|", note)


if __name__ == "__main__":
    main()
