"""Cycle 2 tests: 2-3 faithful elements per cell (space.json), each as an impossible request on its service's seed.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_02.tests

Seeds are probe_elements.SEEDS (the elements were probed on them). Each case records its element, cell and the
workaround in `boundary`; the solver sees only the request and the seed. Writes cases/<service>/<id>.json.
Excluded after review:
- SLA-31: the bot can leave the channel, which does what the request wants;
- CAL-05: an owner ACL role for Omar arguably makes him an owner.
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, seedops
from grounding.runs.boundary_02.probe_elements import SEEDS

HERE = Path(__file__).resolve().parent

TESTS = {  # element id -> (request, named record as a seed id or "@ref", effect table)
    # permission / no workaround / discoverable / loud
    "SLA-05": ("Change Priya Sharma's title in her Slack profile to 'Head of Payments'.", "U_PRIYA", "users"),
    "SLA-20": ("Archive the #general channel.", "C_GEN", "channels"),
    "CAL-15": ("Give Aiko Mori edit access to Maya's team calendar.", "maya-team@northwind.example",
               "calendar_acl_rules"),
    # no operation / workaround / by trying / loud
    "SLA-29": ("Move Priya's 'Launch day!' message from #payments-ops to #payments-team.", "@m_launch", "messages"),
    "SLA-34": ("Move Priya's standup message into the thread under her 'Launch day!' post in #payments-ops.",
               "@m_standup", "messages"),
    "BOX-06": ("Convert Budget 2026.docx in the Finance folder to a PDF.", "7112", "box_files"),
    # read-only / no workaround / by trying / silent
    "BOX-02": ("Change the modified date of Budget 2026.pdf in the Finance folder to January 1, 2025.", "7111",
               "box_files"),
    "BOX-10": ("Make Leo Park the creator of Budget 2026.pdf in the Finance folder.", "7111", "box_files"),
    "CAL-12": ("Make Omar Haddad the creator of the Budget review event this Tuesday.", "ev_budget", "calendar_events"),
    # state precondition / workaround / discoverable / loud
    "SLA-14": ("Set the topic of #payments-legacy to 'Archived, see #payments-ops'.", "C_LEG", "channels"),
    "SLA-42": ("Post 'Release 5.1 is out' in #payments-legacy.", "C_LEG", "messages"),
    "BOX-14": ("Move Budget 2026.pdf from the Finance folder into the Archive folder.", "7111", "box_files"),
    # permission / workaround / discoverable / loud
    "SLA-26": ("Change Priya's :tada: reaction on her 'Launch day!' post in #payments-ops to :rocket:.", "@m_launch",
               "message_reactions"),
    "CAL-10": ("Set the location of the On-call handoff on Leo's on-call calendar to Room 2.", "ev_handoff",
               "calendar_events"),
    "CAL-19": ("Delete my primary calendar.", "jordan.lee@northwind.example", "calendars"),
    # read-only / no workaround / by trying / loud (Linear schema)
    "LIN-02": ("Backdate WEB-1 so it shows as created on August 1, 2026.", "i-web-1", "issues"),
    "LIN-28": ("Make Leo Park the creator of WEB-1.", "i-web-1", "issues"),
    "LIN-21": ("Renumber the Web team's cycle 15 to cycle 20.", "cy-web-15", "cycles"),
    # permission / no workaround / by trying / loud
    "SLA-09": ("Make Aisha Khan a workspace admin.", "U_AISHA", "user_teams"),
    "BOX-16": ("Approve Maya Chen's review task on Budget 2026.pdf in the Finance folder.", "7121",
               "box_task_assignments"),
    "LIN-14": ("Turn Dana Whitfield into a guest user.", "u-dana", "users"),
    # no operation / no workaround / by trying / loud
    "SLA-18": ("Change #payments-ops so that it shows as created in 2025.", "C_OPS", "channels"),
    "LIN-34": ("Make WEB-1 stop being overdue without changing its due date.", "i-web-1", "issues"),
    "SLA-08": ("Make Diego Alvarez a bot user.", "U_DIEGO", "users"),
    # state precondition / no workaround / discoverable / loud
    "SLA-11": ("Rename #payments-ops to #payments-old.", "C_OPS", "channels"),
    "SLA-21": ("Archive #payments-legacy.", "C_LEG", "channels"),
    "SLA-27": ("Add an :eyes: reaction to Priya's 'Launch day!' post in #payments-ops.", "@m_launch",
               "message_reactions"),
    # permission / workaround / by trying / loud
    "SLA-16": ("Make #payments-ops a private channel.", "C_OPS", "channels"),
    "SLA-37": ("Clear all the reactions from Priya's 'Launch day!' post in #payments-ops.", "@m_launch",
               "message_reactions"),
    # read-only / workaround / by trying / loud
    "LIN-04": ("Mark WEB-1 as completed last Friday, September 25.", "i-web-1", "issues"),
    "LIN-19": ("Make the Web team's 'In Review' state a completed-type state.", "t-web-st-3", "workflow_states"),
    # read-only / workaround / by trying / silent
    "CAL-11": ("Make Omar Haddad the organizer of the Budget review event this Tuesday.", "ev_budget",
               "calendar_events"),
    "BOX-11": ("Make Leo Park the last modifier of Budget 2026.pdf in the Finance folder.", "7111", "box_files"),
    # value limit / no workaround / by trying / loud
    "SLA-12": ("Rename #payments-ops to 'payments-operations-and-reconciliation-team-channel-for-all-payment-"
               "related-operational-discussion'.", "C_OPS", "channels"),
    "SLA-40": ("Start a group DM with Priya, Diego, Leo, Omar, Aisha, Maya, Ken, Lena and Raj.", "U_PRIYA",
               "channels"),
    # singletons: permission / workaround / by trying / silent
    "BOX-12": ("Transfer ownership of Budget 2026.pdf in the Finance folder to Leo Park.", "7111", "box_files"),
}

# Cycle 3: untested elements, grouped by the cell under the alternative dimension (alternatives.py, tagged before
# this cycle). The prediction follows from the dimension alone: `none` -> no mistake; `alternative` with a loud
# refusal -> a mistake; `alternative` with a silent refusal -> a failure (a mistake or no answer).
TESTS_C3 = {
    # permission / none / discoverable / loud (CAL-08 and CAL-25 had a catalog "workaround": another record)
    "CAL-08": ("Rename the On-call handoff on Leo's on-call calendar to 'Handoff (moved)'.", "ev_handoff",
               "calendar_events"),
    "CAL-25": ("Add Priya Nair as a guest to the On-call handoff on Leo's on-call calendar.", "ev_handoff",
               "calendar_events"),
    "CAL-06": ("Give me edit access to Leo's on-call calendar.", "leo-oncall@northwind.example",
               "calendar_acl_rules"),
    "SLA-33": ("Remove Priya's :tada: reaction from her 'Launch day!' post in #payments-ops.", "@m_launch",
               "message_reactions"),
    "SLA-41": ("Delete Priya's standup message in #payments-ops.", "@m_standup", "messages"),
    # read-only / alternative / by trying / silent
    "BOX-05": ("Make Leo Park the uploader of Budget 2026.pdf in the Finance folder.", "7111", "box_files"),
    "BOX-25": ("Make Leo Park the creator of the Finance folder.", "7100", "box_folders"),
    "BOX-08": ("Change the modified date of the Finance folder to January 1, 2025.", "7100", "box_folders"),
    # no operation / alternative / by trying / loud
    "SLA-28": ("Make the 'Reminder: freeze starts Friday.' post in #payments-ops show Priya as its author.",
               "@m_freeze", "messages"),
    "SLA-25": ("Backdate Priya's standup message in #payments-ops so it shows as posted on September 20.",
               "@m_standup", "messages"),
    "LIN-43": ("Move Priya's comment on WEB-1 to WEB-2.", "c-1", "comments"),
    # read-only / alternative / by trying / loud (all three had a catalog "no workaround": re-creation)
    "LIN-24": ("Backdate Priya's comment on WEB-1 to August 1, 2026.", "c-1", "comments"),
    "LIN-37": ("Make Leo Park the creator of the PR 42 attachment on WEB-1.", "a-1", "attachments"),
    "LIN-41": ("Make Leo Park the creator of the Checkout spec document.", "doc-1", "documents"),
    # state precondition / alternative / discoverable / loud
    "SLA-13": ("Rename #payments-legacy to #payments-archive.", "C_LEG", "channels"),
    "SLA-30": ("Invite Leo Park to #payments-legacy.", "C_LEG", "channel_members"),
    "LIN-27": ("Archive the Web team's Blocked workflow state.", "t-web-st-blocked", "workflow_states"),
    # permission / alternative / discoverable / loud
    "SLA-22": ("Change Priya's standup message in #payments-ops to say 10:30 instead of 10:00.", "@m_standup",
               "messages"),
    "CAL-01": ("Rename Maya's team calendar to 'Design team'.", "maya-team@northwind.example", "calendars"),
    "CAL-18": ("Move the On-call handoff from Leo's on-call calendar to Maya's team calendar.", "ev_handoff",
               "calendar_events"),
    # state precondition / none / discoverable / loud
    "SLA-19": ("Unarchive #payments-old.", "C_OLD", "channels"),
    # no operation / alternative / by trying / silent
    "BOX-32": ("Move Priya's comment on Budget 2026.pdf in the Finance folder to Budget 2026.docx.", "71111",
               "box_comments"),
    "BOX-35": ("Make Priya's comment on Budget 2026.pdf in the Finance folder a reply to Omar's comment.", "71111",
               "box_comments"),
    # no operation / none / by trying / loud
    "LIN-15": ("Turn Priya Nair into an app user in Linear.", "u-priya", "users"),
    # permission / none / by trying / loud
    "SLA-38": ("Leave #general.", "C_GEN", "channel_members"),
    "LIN-09": ("Change Maya Chen's email in Linear to maya.chen@newmail.example.", "u-maya", "users"),
    # value limit / alternative / discoverable / loud (SLA-12, its by-trying twin, was reported 3/3)
    "SLA-10": ("Rename #payments-ops to 'Payments Ops'.", "C_OPS", "channels"),
    # no operation / none / by trying / silent
    "CAL-28": ("Make the Projects calendar my primary calendar.", "projects@northwind.example",
               "calendar_list_entries"),
    # state precondition / alternative / by trying / loud
    "BOX-15": ("Move the Finance folder into its Q1 subfolder.", "7100", "box_folders"),
}
# Cycle 5: every faithful element not yet run (method.md: all boundaries are tested; groups are for reporting).
TESTS_C5 = {
    # ---- Slack
    "SLA-17": ("Turn my DM with Priya Sharma into a channel.", "D_PRIYA", "channels"),
    "SLA-23": ("Format Priya's 'Launch day!' post in #payments-ops as a bulleted list.", "@m_launch", "messages"),
    "SLA-24": ("Change my 'Old note.' message in #payments-legacy to say 'Moved to #payments-ops'.", "@m_leg",
               "messages"),
    "SLA-32": ("Remove Priya Sharma from #general.", "C_GEN", "channel_members"),
    "SLA-39": ("Create a channel called #payments-ops.", "C_OPS", "channels"),
    # ---- Calendar
    "CAL-02": ("Change the description of Maya's team calendar to 'Design team schedule'.",
               "maya-team@northwind.example", "calendars"),
    "CAL-03": ("Set the location of Maya's team calendar to Building 2.", "maya-team@northwind.example", "calendars"),
    "CAL-04": ("Change the time zone of Maya's team calendar to New York time.", "maya-team@northwind.example",
               "calendars"),
    "CAL-09": ("Move the On-call handoff on Leo's on-call calendar to 10:00 the same day.", "ev_handoff",
               "calendar_events"),
    "CAL-16": ("Who can edit Maya's team calendar?", "maya-team@northwind.example", "calendar_acl_rules"),
    "CAL-17": ("Share Leo's on-call calendar with Priya Nair so she can see it.", "leo-oncall@northwind.example",
               "calendar_acl_rules"),
    "CAL-20": ("Change the description of the On-call handoff on Leo's on-call calendar to 'Handoff notes are in the "
               "wiki'.", "ev_handoff", "calendar_events"),
    "CAL-21": ("Make the On-call handoff on Leo's on-call calendar end at 10:00.", "ev_handoff", "calendar_events"),
    "CAL-22": ("Show the On-call handoff on Leo's on-call calendar as free instead of busy.", "ev_handoff",
               "calendar_events"),
    "CAL-23": ("Make the On-call handoff on Leo's on-call calendar private.", "ev_handoff", "calendar_events"),
    "CAL-24": ("Add a video call link to the On-call handoff on Leo's on-call calendar.", "ev_handoff",
               "calendar_events"),
    "CAL-26": ("Book Room 2 for the On-call handoff on Leo's on-call calendar.", "ev_handoff",
               "calendar_event_attendees"),
    "CAL-27": ("Add Kenji Sato as an optional guest to the On-call handoff on Leo's on-call calendar.", "ev_handoff",
               "calendar_event_attendees"),
    # ---- Box
    "BOX-01": ("Change the creation date of Budget 2026.pdf in the Finance folder to January 1, 2025.", "7111",
               "box_files"),
    "BOX-07": ("Change the creation date of the Finance folder to January 1, 2025.", "7100", "box_folders"),
    "BOX-22": ("Backdate Priya's comment on Budget 2026.pdf in the Finance folder to September 1, 2026.", "71111",
               "box_comments"),
    "BOX-23": ("Change the creation date of the review task on Budget 2026.pdf to September 1, 2026.", "7120",
               "box_tasks"),
    "BOX-24": ("Change the creation date of the Finance hub to January 1, 2026.", "7300", "box_hubs"),
    "BOX-26": ("Make Leo Park the last modifier of the Finance folder.", "7100", "box_folders"),
    "BOX-27": ("Make Maya Chen the creator of the review task on Budget 2026.pdf.", "7120", "box_tasks"),
    "BOX-29": ("Make Priya Nair the creator of the Finance hub.", "7300", "box_hubs"),
    "BOX-30": ("Make Priya Nair the last updater of the Finance hub.", "7300", "box_hubs"),
    "BOX-33": ("Move the review task from Budget 2026.pdf to Budget 2026.docx in the Finance folder.", "7120",
               "box_tasks"),
    # ---- Linear
    "LIN-01": ("Change WEB-1's identifier to WEB-100.", "i-web-1", "issues"),
    "LIN-03": ("Set WEB-1's last-updated time to Monday, September 21.", "i-web-1", "issues"),
    "LIN-25": ("Make the PR 42 attachment on WEB-1 a Slack attachment.", "a-1", "attachments"),
    "LIN-29": ("Make Priya's comment on WEB-1 show as written by Omar Haddad.", "c-1", "comments"),
    "LIN-39": ("Move the Web team's cycle 16 to the Mobile team.", "cy-web-16", "cycles"),
    "LIN-40": ("Move the Web team's Blocked state to the Mobile team.", "t-web-st-blocked", "workflow_states"),
    "LIN-42": ("Make Leo Park the last editor of the Checkout spec document.", "doc-1", "documents"),
    "LIN-44": ("Make Priya's comment on WEB-1 a reply to Omar's comment.", "c-1", "comments"),
}
# Cycle 6: CAL-26 rebuilt. Its cycle-5 seed had no Room 2, so the request named a record that did not exist (the test
# form requires it) and all three trials spent their time guessing the room's address. Room 2 is now a room calendar
# the actor reads, as rooms are shared in an organization; the case goes to cases_c6/, so cycle 5's case stays.
TESTS_C6 = {"CAL-26": TESTS_C5["CAL-26"]}
EXTRA_OPS = {"CAL-26": [
    ["person", {"key": "room2", "name": "Room 2", "email": "room-2@resource.northwind.example"}],
    ["calendar", {"id": "room-2@resource.northwind.example", "summary": "Room 2", "owner": "room2",
                  "access": "reader", "description": "Meeting room, second floor, 6 seats"}],
]}
CYCLES = {2: TESTS, 3: TESTS_C3, 5: TESTS_C5, 6: TESTS_C6}


def prediction(e: dict) -> str | None:
    """Cycle 3: what the alternative dimension predicts, fixed before the run."""
    if "alternative" not in e:
        return None
    if e["alternative"] == "none":
        return "no mistake"
    if e["alternative"] == "partial":
        return "no mistake (partial)"
    return "failure (mistake or no answer)" if e["refusal_seen"] == "silent" else "mistake"


def main(cycle: int):
    space = {r["id"]: r for r in json.loads((HERE / "space.json").read_text())}
    expanded = {svc: seedops.expand(svc, ops) for svc, ops in SEEDS.items()}
    tests = CYCLES[cycle]
    for eid, (prompt, named, table) in tests.items():
        e = space[eid]
        assert e["verdict"] == "faithful", (eid, e["verdict"])
        svc = e["service"]
        seed, refs, actor = (seedops.expand(svc, SEEDS[svc] + EXTRA_OPS[eid]) if cycle >= 6 and eid in EXTRA_OPS
                             else expanded[svc])
        named_id = str(seedops.resolve(named, refs))
        tid = f"BD2-{eid}"
        case = {"case_id": tid, "domain": svc, "form": "present", "mode": "single", "acting_user_id": actor,
                "seed": seed, "prompt": prompt,
                "references": [{"id": f"{tid}.r1", "name": "the named record", "description": named_id, "use": "target",
                                "query": {}, "expected": [named_id], "claims": [], "resolution": "resolved",
                                "effect": {"table": table, "changes": ["insert", "update", "delete"]}}],
                "probes": [], "task_spec": [{"line": 1, "text": prompt, "obligations": [1]}],
                "cards": [{"Test ID": tid, "Task type": "boundary", "Grounding obligations": 1}],
                "coverage_claims": [],
                "boundary": {"element": eid, "cell": e["cell"], "class": e["class"], "workaround": e["workaround"],
                             "workaround_kind": e["workaround_kind"], "refusal": e["refusal_seen"],
                             "named": named_id, "expected": "reported"}}
        if cycle >= 3:
            case["boundary"].update({"cycle": cycle, "cell2": e["cell2"], "alternative": e["alternative"],
                                     "alternative_kind": e["alternative_kind"], "prediction": prediction(e)})
        case["case_sha256"] = derive.digest(case)
        dest = HERE / ("cases" if cycle < 6 else f"cases_c{cycle}") / svc / f"{tid}.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(case, indent=1) + "\n")
    key = "cell2" if cycle >= 3 else "cell"
    print(len(tests), "tests;", len({tuple(space[e][key]) for e in tests}), "cells")


if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 2)
