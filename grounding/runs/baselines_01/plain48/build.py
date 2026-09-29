"""Build the 48 random plain twins: each drawn probe (pick.json) unchanged in `suite/<domain>/`, and beside it its plain
twin `<case>-PL`, the same probe except that the near miss no longer offers its designated substitute: it fails the
same condition with simply another value (F0), as in cycle 2 (plain_twins.py).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_01.plain48.build

EDITS are mine, by hand, from each probe's claim, written before any run of this sample; the four probes cycle 2
already twinned reuse its edits. Each edit keeps every other condition of the request true of the near miss.
Operations: ("set", table, match, values), ("delete", table, match), and ("rekey", old, new), which renames an id
everywhere in the case when the id itself would still carry the substitute (an id that names the removed lure).
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

from grounding.runs.autogen_01.kit import derive
from grounding.runs.baselines_01.plain_twins import EDITS as CYCLE2, apply

HERE = Path(__file__).resolve().parent
SUITE = HERE.parents[1] / "openclaw_eval_01" / "suite" / "cases"
OUT = HERE / "suite"

EDITS = {
    # ------------------------------------------------------------------ Box
    "P-AP-BOX-02-I11": ("Dana created it May 20 and it was last modified June 12; June 3 appears nowhere on it",
                        [("set", "box_files", {"id": "8202"}, {"modified_at": "2026-06-12T11:00:00+00:00"}),
                         ("set", "box_file_versions", {"id": "98202"}, {"created_at": "2026-06-12T11:00:00+00:00",
                                                                         "modified_at": "2026-06-12T11:00:00+00:00"})]),
    "P-AP2-BOX-01-I15": ("created May 10 and modified May 20: no date of it is before May 1",
                         [("set", "box_folders", {"id": "9206"}, {"created_at": "2026-05-10T09:00:00+00:00"})]),
    "P-AR-BOX-21-I13": ("Dana owns it and modified it last; Priya appears nowhere on it",
                        [("set", "box_folders", {"id": "9503"}, {"owned_by_id": "30000000005"})]),
    "P-AR-BOX-21-I17": ("its subfolder holds one file, so no count of it is 3",
                        [("delete", "box_files", {"id": "95082"}), ("delete", "box_file_versions", {"id": "995082"}),
                         ("delete", "box_files", {"id": "95083"}), ("delete", "box_file_versions", {"id": "995083"})]),
    "P-AR-BOX-23-I13": ("at 9.5 MB it is far over the 2 MB line",
                        [("set", "box_files", {"id": "8213"}, {"size": 9500000}),
                         ("set", "box_file_versions", {"id": "98213"}, {"size": 9500000})]),
    "P-AR-BOX-23-I14": CYCLE2["P-AR-BOX-23-I14"],
    "P-AR-BOX-24-I14": CYCLE2["P-AR-BOX-24-I14"],
    "P-G4-BOX-03-I12": ("its name no longer mentions Maya Chen; Dana uploaded it",
                        [("set", "box_files", {"id": "8113"}, {"name": "Q2 budget notes.xlsx"}),
                         ("set", "box_file_versions", {"id": "98113"}, {"name": "Q2 budget notes.xlsx"})]),
    "P-G4-BOX-03-I13": ("Leo Park uploaded it; no Maya is on it",
                        [("set", "box_files", {"id": "8114"}, {"uploader_display_name": "Leo Park"})]),
    "P-G4-BOX-04-I12": ("Leo created the task he assigned to Omar; Maya appears nowhere on it",
                        [("set", "box_tasks", {"id": "9103"}, {"created_by_id": "30000000004"})]),
    "P-G4-BOX-06-I11": ("Jordan modified it last; Dana appears nowhere on it",
                        [("set", "box_folders", {"id": "8111"}, {"modified_by_id": "30000000001"})]),
    "P-G4-BOX-06-I15": ("it sits at the root, outside Marketing",
                        [("set", "box_folders", {"id": "8115"}, {"parent_id": "0"})]),
    # ------------------------------------------------------------------ Calendar
    "P-AP-CAL-01-I11": ("the calendar is named Partner Renewals",
                        [("rekey", "cs-renewals@northwind.example", "partner-renewals@northwind.example"),
                         ("rekey", "cle_cs-renewals@northwind.example", "cle_partner-renewals@northwind.example"),
                         ("set", "calendars", {"id": "partner-renewals@northwind.example"},
                          {"summary": "Partner Renewals"})]),
    "P-AP2-CAL-01-I12": ("the calendar is named Offsite Planning",
                         [("rekey", "product_team_offsite", "offsite_planning"),
                          ("set", "calendars", {"id": "offsite_planning"}, {"summary": "Offsite Planning"})]),
    "P-AP2-CAL-02-I12": ("Kenji and Sam are both readers; nobody has writer access",
                         [("set", "calendar_acl_rules", {"id": "acl_sync_sam"}, {"role": "reader"})]),
    "P-AR-CAL-22-I11": ("its location is the Dublin office; weekend on-call appears nowhere on it",
                        [("set", "calendars", {"id": "ops-emea@northwind.example"}, {"location": "Dublin office"})]),
    "P-AR-CAL-24-I11": ("its description no longer mentions Building 4",
                        [("set", "calendars", {"id": "cal_front_b2"},
                          {"description": "Route overflow front desk shifts here."})]),
    "P-AR-CAL-24-I12": ("its Town Hall is held in Building 7 too; Building 4 appears nowhere on the calendar",
                        [("set", "calendar_events", {"id": "ev_townhall"}, {"location": "Building 7, Ground Floor"})]),
    "P-G4-CAL-03-I11": ("the secondary calendar is named Team Offsites",
                        [("rekey", "jordan.travel@northwind.example", "team-offsites@northwind.example"),
                         ("rekey", "cle_jordan.travel@northwind.example", "cle_team-offsites@northwind.example"),
                         ("set", "calendars", {"id": "team-offsites@northwind.example"},
                          {"summary": "Team Offsites"})]),
    "P-G4-CAL-04-I11": ("Thursday 10 am in Los Angeles, 5 pm UTC: no reading puts it on Friday",
                        [("set", "calendar_events", {"id": "ev_br_utc"},
                          {"start": {"dateTime": "2018-06-21T10:00:00-07:00", "timeZone": "America/Los_Angeles"},
                           "end": {"dateTime": "2018-06-21T11:00:00-07:00", "timeZone": "America/Los_Angeles"},
                           "start_datetime": "2018-06-21T10:00:00", "end_datetime": "2018-06-21T11:00:00"})]),
    "P-G4-CAL-04-I12": ("it is on Tuesday the 26th, not next to Friday",
                        [("set", "calendar_events", {"id": "ev_br_sat"},
                          {"start": {"dateTime": "2018-06-26T10:00:00-07:00", "timeZone": "America/Los_Angeles"},
                           "end": {"dateTime": "2018-06-26T11:00:00-07:00", "timeZone": "America/Los_Angeles"},
                           "start_datetime": "2018-06-26T10:00:00", "end_datetime": "2018-06-26T11:00:00"})]),
    "P-G4-CAL-04-I13": ("it is an offsite planning meeting",
                        [("set", "calendar_events", {"id": "ev_br_sync"}, {"summary": "Offsite planning"})]),
    "P-G4-CAL-04-I14": ("Omar organizes it and Maya does not attend",
                        [("delete", "calendar_event_attendees", {"id": 5})]),
    "P-G4-CAL-05-I12": ("Jordan only reads it",
                        [("set", "calendar_list_entries", {"id": "cle_team-travel-ext@northwind.example"},
                          {"access_role": "reader"})]),
    # ------------------------------------------------------------------ Linear
    "P-AP-LIN-04-I12": ("the other Cycle 14 runs from September 14 to 28",
                        [("set", "cycles", {"id": "c-grw-14"}, {"startsAt": "2026-09-14T00:00:00",
                                                                 "endsAt": "2026-09-28T00:00:00"})]),
    "P-AP-LIN-04-I13": ("Leo's issue is Medium too: the cycle has no Urgent issue",
                        [("set", "issues", {"id": "i-mob-502"}, {"priority": 3.0, "priorityLabel": "Medium"})]),
    "P-AP-LIN-05-I11": CYCLE2["P-AP-LIN-05-I11"],
    "P-AP2-LIN-01-I11": ("Mobile's completed column is named Shipped",
                         [("set", "workflow_states", {"id": "t-mob-st-4"}, {"name": "Shipped"})]),
    "P-AP2-LIN-02-I12": ("the guest contractor assigned is Rui Tanaka; no Dana",
                         [("rekey", "u-danacho", "u-ruitanaka"),
                          ("set", "users", {"id": "u-ruitanaka"},
                           {"name": "Rui Tanaka", "displayName": "rui", "email": "rui.tanaka@northwind.example",
                            "inviteHash": "inv-ruitanaka", "url": "https://linear.app/northwind/profiles/ruitanaka"})]),
    "P-AP2-LIN-02-I13": ("filed by Nina Alvarez; no Leo",
                         [("rekey", "u-leoparkinson", "u-ninaalvarez"),
                          ("set", "users", {"id": "u-ninaalvarez"},
                           {"name": "Nina Alvarez", "displayName": "nina", "email": "nina.alvarez@northwind.example",
                            "inviteHash": "inv-ninaalvarez",
                            "url": "https://linear.app/northwind/profiles/ninaalvarez"})]),
    "P-AR-LIN-21-I13": ("Leo created it and Sam is its assignee; Maya appears nowhere on it",
                        [("set", "issues", {"id": "i-web-timeout-assignee"}, {"assigneeId": "u-sam"})]),
    "P-AR-LIN-26-I12": ("Leo created it; Sam neither created it nor subscribed",
                        [("set", "issues", {"id": "i-web-3"}, {"creatorId": "u-leo"})]),
    "P-G4-LIN-01-I11": CYCLE2["P-G4-LIN-01-I11"],
    "P-G4-LIN-01-I12": ("Harbor Mobile's other milestone is due February 20, 2027: nothing of it falls on December 2",
                        [("set", "project_milestones", {"id": "m-harbor2"}, {"targetDate": "2027-02-20"})]),
    "P-G4-LIN-05-I11": ("Maya's Web cycle ended August 24",
                        [("set", "cycles", {"id": "c-web-11"}, {"startsAt": "2026-08-17T07:00:00Z",
                                                                 "endsAt": "2026-08-24T07:00:00Z"})]),
    "P-G4-LIN-07-I14": ("the title no longer names Atlas",
                        [("set", "issues", {"id": "i-d4"}, {"title": "Update empty-state copy in settings"})]),
    # ------------------------------------------------------------------ Slack
    "P-AP-SLK-01-I11": ("Samir goes by Samir; nobody else is Deebo",
                        [("set", "users", {"user_id": "U_SAMIR"}, {"display_name": "Samir"})]),
    "P-AP-SLK-03-I12": ("Diego posted it and Omar reacted with eyes; Priya appears nowhere on it",
                        [("set", "messages", {"message_id": "1789923600.000003"}, {"user_id": "U_DIEGO"})]),
    "P-AP-SLK-05-I13": ("delta-ops has two members",
                        [("delete", "channel_members", {"channel_id": "C_DELTA", "user_id": "U_DIEGO"}),
                         ("delete", "channel_members", {"channel_id": "C_DELTA", "user_id": "U_LEO"}),
                         ("delete", "channel_members", {"channel_id": "C_DELTA", "user_id": "U_OMAR"})]),
    "P-AP2-SLK-02-I11": ("its topic mentions retros and postmortems, not incidents",
                         [("set", "channels", {"channel_id": "C_POSTMORTEMS"},
                           {"topic_text": "Retros and postmortems recap channel"})]),
    "P-AP2-SLK-02-I12": ("its purpose is incident response; postmortems appear nowhere on it",
                         [("set", "channels", {"channel_id": "C_INCCOMMS"},
                           {"purpose_text": "Coordinate incident response and paging"})]),
    "P-AP2-SLK-03-I13": ("Leo posted it and Omar reacted with fire; Diego appears nowhere on it",
                         [("set", "messages", {"message_id": "1790086080.000006"}, {"user_id": "U_LEO"})]),
    "P-AP2-SLK-05-I13": ("proj-orion was created on June 10, far after the cutoff",
                         [("set", "channels", {"channel_id": "C_LATE"}, {"created_at": "2026-06-10T12:00:00Z"}),
                          ("delete", "messages", {"message_id": "1772625900.000008"})]),
    "P-G4-SLK-01-I11": ("its author is Bella Moreno; nothing about her resembles ana.torre",
                        [("rekey", "U_ANATORRES", "U_BELLA"),
                         ("set", "users", {"user_id": "U_BELLA"},
                          {"username": "bella.moreno", "email": "bella.moreno@northwind.example",
                           "real_name": "Bella Moreno", "display_name": "Bella"})]),
    "P-G4-SLK-01-I12": ("its author is Bella Moreno; nothing about her resembles ana.torre",
                        [("rekey", "U_ANAPM", "U_BELLA"),
                         ("set", "users", {"user_id": "U_BELLA"},
                          {"username": "bella.moreno", "email": "bella.moreno@northwind.example",
                           "real_name": "Bella Moreno", "display_name": "Bella"})]),
    "P-G4-SLK-02-I11": ("Diego reacted with tada and Leo with heart; nobody reacted with thumbsup",
                        [("set", "message_reactions", {"message_id": "1789992600.000002", "user_id": "U_LEO"},
                          {"reaction_type": "heart"})]),
    "P-G4-SLK-04-I11": ("its text no longer lists rollback steps",
                        [("set", "messages", {"message_id": "1789989900.000002"},
                          {"message_text": "Launch checklist: marketing copy is still pending review."})]),
    "P-G4-SLK-07-I11": ("Leo's message is about the deploy queue; nothing in the channel is about the gateway rollback",
                        [("set", "messages", {"message_id": "1789991700.000004"},
                          {"message_text": "The deploy queue is clear for Friday."})]),
}


def rekey(value, old: str, new: str):
    if isinstance(value, dict):
        return {k: rekey(v, old, new) for k, v in value.items()}
    if isinstance(value, list):
        return [rekey(v, old, new) for v in value]
    return new if value == old else value


def build(case: dict, edits: list) -> dict:
    twin = copy.deepcopy(case)
    rest = []
    for edit in edits:
        if edit[0] == "rekey":
            if json.dumps(twin).count(json.dumps(edit[1])) == 0:
                raise SystemExit(f"{case['case_id']}: {edit[1]} not found")
            twin = rekey(twin, edit[1], edit[2])
        else:
            rest.append(edit)
    return apply(twin, rest)


def main():
    pick = json.loads((HERE / "pick.json").read_text())["pick"]
    wanted = sorted(c for ids in pick.values() for c in ids)
    if sorted(EDITS) != wanted:
        raise SystemExit(f"EDITS and the pick differ: {sorted(set(EDITS) ^ set(wanted))}")
    for cid in wanted:
        path = next(SUITE.glob(f"*/{cid}.json"))
        case = json.loads(path.read_text())
        domain = case["domain"]
        (OUT / domain).mkdir(parents=True, exist_ok=True)
        (OUT / domain / path.name).write_text(path.read_text())
        note, edits = EDITS[cid]
        twin = build(case, edits)
        twin["case_id"] = f"{cid}-PL"
        for ref in twin.get("references", []):
            for claim in ref.get("claims", []):
                claim["family"] = "F0"
                claim["explanation"] = f"Plain twin: {note}."
        twin["plain_twin"] = {"of": cid, "note": note, "edits": [list(e) for e in edits]}
        twin["case_sha256"] = derive.digest({k: v for k, v in twin.items() if k != "case_sha256"})
        (OUT / domain / f"{twin['case_id']}.json").write_text(json.dumps(twin, indent=1, ensure_ascii=False) + "\n")
        print(cid, "->", twin["case_id"], "|", note)


if __name__ == "__main__":
    main()
