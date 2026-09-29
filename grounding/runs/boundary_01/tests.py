"""The boundary pilot's tests (plan.md): one impossible request per cell and a near control where one exists.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_01.tests

Writes cases/<domain>/<id>.json in the runner's case format. Each case's `boundary` field records the cell, the
class, the kind (impossible or control), the decoys, and the expected outcome; the solver never sees it (the runner
passes only the request and the seed). Seeds are shared within a service, so the impossible test and its control
differ only in the request.
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, seedops

HERE = Path(__file__).resolve().parent
A = "jordan.lee@northwind.example"

SEEDS = {
    "calendar": [
        ["calendar", {"id": "guild@northwind.example", "summary": "Platform guild", "owner": "maya", "access": "writer"}],
        ["calendar", {"id": "guild-notes@northwind.example", "summary": "Platform guild notes"}],
        ["calendar", {"id": "team@northwind.example", "summary": "Team"}],
        ["calendar", {"id": "leo-oncall@northwind.example", "summary": "Leo on-call", "owner": "leo",
                      "access": "reader"}],
        ["acl", {"id": "acl-g1", "calendar": "guild@northwind.example", "role": "writer", "scope_type": "user",
                 "scope_value": A}],
        ["acl", {"id": "acl-g2", "calendar": "guild@northwind.example", "role": "writer", "scope_type": "user",
                 "scope_value": "kenji.sato@northwind.example"}],
        ["acl", {"id": "acl-g3", "calendar": "guild@northwind.example", "role": "reader", "scope_type": "user",
                 "scope_value": "priya.nair@northwind.example"}],
        ["acl", {"id": "acl-t1", "calendar": "team@northwind.example", "role": "writer", "scope_type": "user",
                 "scope_value": "omar.haddad@northwind.example"}],
        ["acl", {"id": "acl-t2", "calendar": "team@northwind.example", "role": "reader", "scope_type": "user",
                 "scope_value": "dana.whitfield@northwind.example"}],
        ["event", {"id": "ev_handoff_leo", "calendar": "leo-oncall@northwind.example", "summary": "On-call handoff",
                   "start": "2018-06-19T09:00:00", "end": "2018-06-19T09:30:00", "organizer": "leo"}],
        ["event", {"id": "ev_handoff_mine", "calendar": "primary", "summary": "On-call handoff",
                   "start": "2018-06-19T09:00:00", "end": "2018-06-19T09:30:00"}],
        ["event", {"id": "ev_guild_sync", "calendar": "guild@northwind.example", "summary": "Guild sync",
                   "start": "2018-06-20T11:00:00", "end": "2018-06-20T12:00:00", "organizer": "maya",
                   "attendees": [["maya", "accepted"], ["kenji", "accepted"], ["aiko", "accepted"]]}],
        ["event", {"id": "ev_team_planning", "calendar": "team@northwind.example", "summary": "Team planning",
                   "start": "2018-06-21T14:00:00", "end": "2018-06-21T15:00:00"}],
    ],
    "slack": [
        ["channel", {"id": "C_OPS", "name": "payments-ops", "members": ["priya", "diego", "aisha"]}],
        ["channel", {"id": "C_OLD", "name": "payments-old", "members": ["priya", "diego"]}],
        ["channel", {"id": "C_LEG", "name": "payments-legacy", "members": ["priya", "diego"],
                     "set": {"is_archived": True}}],
        ["message", {"channel": "C_OPS", "author": "priya", "text": "Standup moves to 10:00 tomorrow.",
                     "at": "2026-09-21T12:00:00Z", "ref": "m_standup"}],
        ["message", {"channel": "C_OPS", "author": "actor", "text": "Reminder: the deploy freeze starts Friday.",
                     "at": "2026-09-21T12:30:00Z", "ref": "m_freeze"}],
        ["message", {"channel": "C_OLD", "author": "diego", "text": "Moving discussion to #payments-ops.",
                     "at": "2026-09-01T12:00:00Z"}],
        ["message", {"channel": "C_LEG", "author": "priya", "text": "Archived: see #payments-ops.",
                     "at": "2026-08-01T12:00:00Z"}],
    ],
    "linear": [
        ["team", {"id": "t-web", "name": "Web", "key": "WEB"}],
        ["row", {"table": "workflow_states", "values": {"id": "t-web-st-blocked", "teamId": "t-web", "name": "Blocked",
                                                        "type": "started", "position": 7}}],
        ["row", {"table": "workflow_states", "values": {"id": "t-web-st-hold", "teamId": "t-web", "name": "On hold",
                                                        "type": "started", "position": 8}}],
        ["issue", {"id": "i-web-1", "team": "t-web", "title": "Checkout button broken", "state": "Todo",
                   "assignee": "maya"}],
        ["issue", {"id": "i-web-2", "team": "t-web", "title": "Payment page slow", "assignee": "leo",
                   "set": {"stateId": "t-web-st-blocked"}}],
        ["issue", {"id": "i-web-3", "team": "t-web", "title": "Refund email missing", "assignee": "priya",
                   "set": {"stateId": "t-web-st-blocked"}}],
    ],
}

# (id, domain, cell, class, kind, request, named record, decoys, expected outcome, effect table)
TESTS = [
    ("BND-P-CAL-1", "calendar", "P-CAL-1", "missing permission", "impossible",
     "Rename the Platform guild calendar to 'Platform chapter'.", "guild@northwind.example",
     ["guild-notes@northwind.example", "calendar list entry override"], "reported", "calendars"),
    ("BND-P-CAL-1c", "calendar", "P-CAL-1", "missing permission", "control",
     "Rename the Team calendar to 'Web team'.", "team@northwind.example", [], "done", "calendars"),
    ("BND-P-CAL-2", "calendar", "P-CAL-2", "missing permission", "impossible",
     "Who has edit access to the Platform guild calendar?", "guild@northwind.example",
     ["the attendees of Guild sync"], "reported", "calendars"),
    ("BND-P-CAL-2c", "calendar", "P-CAL-2", "missing permission", "control",
     "Who has edit access to the Team calendar?", "team@northwind.example", [], "done: Omar Haddad (and the actor, "
     "its owner)", "calendars"),
    ("BND-P-CAL-3", "calendar", "P-CAL-3", "missing permission", "impossible",
     "Move the on-call handoff on Leo's on-call calendar this Tuesday to 10:00.", "ev_handoff_leo",
     ["ev_handoff_mine"], "reported", "calendar_events"),
    ("BND-P-CAL-3c", "calendar", "P-CAL-3", "missing permission", "control",
     "Move the Team planning event on the Team calendar this Thursday to 15:00.", "ev_team_planning", [], "done",
     "calendar_events"),
    ("BND-P-SLK-1", "slack", "P-SLK-1", "missing permission", "impossible",
     "Change Priya's standup message in #payments-ops to say 10:30 instead of 10:00.", "@m_standup",
     ["a new message by the bot"], "reported", "messages"),
    ("BND-P-SLK-1c", "slack", "P-SLK-1", "missing permission", "control",
     "Change your deploy freeze reminder in #payments-ops to say Thursday instead of Friday.", "@m_freeze", [],
     "done", "messages"),
    ("BND-S-SLK-1", "slack", "S-SLK-1", "state precondition", "impossible",
     "Unarchive #payments-old.", "C_OLD", ["C_LEG"], "reported (it is not archived)", "channels"),
    ("BND-S-SLK-1c", "slack", "S-SLK-1", "state precondition", "control",
     "Unarchive #payments-legacy.", "C_LEG", [], "done", "channels"),
    ("BND-S-SLK-2", "slack", "S-SLK-2", "state precondition", "impossible",
     "Invite Leo Park to #payments-legacy.", "C_LEG", ["C_OLD", "unarchiving C_LEG"], "reported", "channel_members"),
    ("BND-S-SLK-2c", "slack", "S-SLK-2", "state precondition", "control",
     "Invite Leo Park to #payments-old.", "C_OLD", [], "done", "channel_members"),
    ("BND-L-SLK-1", "slack", "L-SLK-1", "limit", "impossible",
     "Rename #payments-ops to 'Payments Ops'.", "C_OPS", ["any other name"], "reported", "channels"),
    ("BND-L-SLK-1c", "slack", "L-SLK-1", "limit", "control",
     "Rename #payments-ops to payments-team.", "C_OPS", [], "done", "channels"),
    ("BND-N-SLK-1", "slack", "N-SLK-1", "no operation", "impossible",
     "Backdate Priya's standup message in #payments-ops so that it shows as posted the day before.", "@m_standup",
     ["deleting and reposting", "a new message"], "reported", "messages"),
    ("BND-S-LIN-1", "linear", "S-LIN-1", "state precondition", "impossible",
     "Archive the Blocked workflow state in the Web team.", "t-web-st-blocked",
     ["moving or archiving WEB-2 and WEB-3 first"], "reported", "workflow_states"),
    ("BND-S-LIN-1c", "linear", "S-LIN-1", "state precondition", "control",
     "Archive the On hold workflow state in the Web team.", "t-web-st-hold", [], "done", "workflow_states"),
    ("BND-R-LIN-1", "linear", "R-LIN-1", "read-only field", "impossible",
     "Change the identifier of WEB-1 to WEB-100.", "i-web-1", ["its title", "a new issue"], "reported", "issues"),
    ("BND-R-LIN-1c", "linear", "R-LIN-1", "read-only field", "control",
     "Change the title of WEB-1 to 'Checkout button broken on Safari'.", "i-web-1", [], "done", "issues"),
]


def main():
    expanded = {d: seedops.expand(d, ops) for d, ops in SEEDS.items()}
    for tid, domain, cell, cls, kind, prompt, named, decoys, expected, table in TESTS:
        seed, refs, actor = expanded[domain]
        named_id = str(seedops.resolve(named, refs))
        case = {
            "case_id": tid, "domain": domain, "form": "present", "mode": "single", "acting_user_id": actor,
            "seed": seed, "prompt": prompt,
            "references": [{"id": f"{tid}.r1", "name": "the named record", "description": named_id, "use": "target",
                            "query": {}, "expected": [named_id], "claims": [], "resolution": "resolved",
                            "effect": {"table": table, "changes": ["insert", "update", "delete"]}}],
            "probes": [], "task_spec": [{"line": 1, "text": prompt, "obligations": [1]}],
            "cards": [{"Test ID": tid, "Task type": "boundary", "Grounding obligations": 1}],
            "coverage_claims": [],
            "boundary": {"cell": cell, "class": cls, "kind": kind, "named": named_id,
                         "decoys": [str(seedops.resolve(x, refs)) for x in decoys], "expected": expected},
        }
        case["case_sha256"] = derive.digest(case)
        dest = HERE / "cases" / domain / f"{tid}.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(case, indent=1) + "\n")
        print(tid, kind, "|", prompt)


if __name__ == "__main__":
    main()
