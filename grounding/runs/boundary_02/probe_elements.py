"""The faithfulness filter: make each catalog element's natural call on the replica and classify the response.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_02.probe_elements [SERVICE ...]

One seed per service (SEEDS). For every element with a call (CALLS; elements whose request has no API at all have
none), a fresh environment runs the call. The response is classified from the status, the body, and a field-level
diff (noise columns such as etags and update times ignored):
- `refused loudly`: an error, and nothing changed;
- `refused silently`: success returned, and nothing relevant changed;
- `performed`: the replica made the change the real service refuses. Unfaithful, so left out of the testable
  space and counted;
- `error, but changed`: an error returned, yet state changed. Unfaithful.
The classification is compared with the catalog's expectation (loud or silent). Writes probes.json. No model calls.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from grounding.integrations.agentdiff import custom_runtime, runtime
from grounding.integrations.agentdiff import smoke_runtime as smoke
from grounding.integrations.agentdiff.runtime import ddl_lock, engine_for, environment_schema
from grounding.runs.autogen_01.kit import seedops
from grounding.runs.autogen_01.kit.preflight import perform_write

HERE = Path(__file__).resolve().parent
DB = os.environ.get("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
BASE = os.environ.get("AGENTDIFF_BASE_URL", "http://127.0.0.1:18001")
A = "jordan.lee@northwind.example"
NOISE = {"etag", "updated_at", "updatedAt", "sequence", "sequence_id", "modified_at", "content_modified_at"}

SEEDS = {
    "slack": [
        *[["person", {"key": k, "name": n}] for k, n in (("ken", "Ken Ito"), ("lena", "Lena Vogel"), ("raj", "Raj Iyer"))],
        ["channel", {"id": "C_OPS", "name": "payments-ops", "members": ["priya", "diego", "aisha"]}],
        ["channel", {"id": "C_OLD", "name": "payments-old", "members": ["priya", "diego"]}],
        ["channel", {"id": "C_LEG", "name": "payments-legacy", "members": ["priya"], "set": {"is_archived": True}}],
        ["channel", {"id": "C_TEAM", "name": "payments-team", "members": ["priya"]}],
        ["channel", {"id": "C_GEN", "name": "general", "members": ["priya", "diego", "aisha", "leo"]}],
        ["message", {"channel": "C_OPS", "author": "priya", "text": "Standup moves to 10:00 tomorrow.",
                     "at": "2026-09-21T12:00:00Z", "ref": "m_standup"}],
        ["message", {"channel": "C_OPS", "author": "actor", "text": "Reminder: freeze starts Friday.",
                     "at": "2026-09-21T12:10:00Z", "ref": "m_freeze"}],
        ["message", {"channel": "C_OPS", "author": "priya", "text": "Launch day!", "at": "2026-09-21T12:20:00Z",
                     "ref": "m_launch"}],
        ["message", {"channel": "C_OPS", "author": "actor", "text": "Congrats!", "at": "2026-09-21T12:30:00Z",
                     "parent": "@m_launch", "ref": "m_reply"}],
        ["message", {"channel": "C_LEG", "author": "actor", "text": "Old note.", "at": "2026-08-01T12:00:00Z",
                     "ref": "m_leg"}],
        ["reaction", {"message": "@m_launch", "person": "priya", "name": "tada"}],
        ["reaction", {"message": "@m_launch", "person": "actor", "name": "eyes"}],
    ],
    "calendar": [
        ["calendar", {"id": "maya-team@northwind.example", "summary": "Maya's team", "owner": "maya", "access": "writer"}],
        ["calendar", {"id": "projects@northwind.example", "summary": "Projects"}],
        ["calendar", {"id": "leo-oncall@northwind.example", "summary": "Leo on-call", "owner": "leo", "access": "reader"}],
        ["acl", {"id": "acl-m1", "calendar": "maya-team@northwind.example", "role": "writer", "scope_type": "user",
                 "scope_value": "kenji.sato@northwind.example"}],
        ["event", {"id": "ev_handoff", "calendar": "leo-oncall@northwind.example", "summary": "On-call handoff",
                   "start": "2018-06-19T09:00:00", "end": "2018-06-19T09:30:00", "organizer": "leo"}],
        ["event", {"id": "ev_budget", "calendar": "primary", "summary": "Budget review",
                   "start": "2018-06-19T15:00:00", "end": "2018-06-19T16:00:00"}],
        ["event", {"id": "ev_sync", "calendar": "primary", "summary": "Design sync", "organizer": "maya",
                   "start": "2018-06-20T11:00:00", "end": "2018-06-20T11:30:00",
                   "attendees": [["maya", "accepted"], ["actor", "needsAction"]]}],
        ["event", {"id": "ev_review", "calendar": "primary", "summary": "Design review",
                   "start": "2018-06-21T10:00:00", "end": "2018-06-21T11:00:00",
                   "attendees": [["kenji", "needsAction"], ["aiko", "accepted"]]}],
        ["event", {"id": "ev_deep", "calendar": "primary", "summary": "Deep work",
                   "start": "2018-06-22T09:00:00", "end": "2018-06-22T11:00:00"}],
    ],
    "box": [
        ["folder", {"id": "7100", "name": "Finance"}], ["folder", {"id": "7101", "name": "Q1", "parent": "7100"}],
        ["folder", {"id": "7102", "name": "Archive"}],
        ["file", {"id": "7111", "name": "Budget 2026.pdf", "parent": "7100", "owner": "JL"}],
        ["file", {"id": "7112", "name": "Budget 2026.docx", "parent": "7100"}],
        ["file", {"id": "7113", "name": "Budget 2026.pdf", "parent": "7102"}],
        ["comment", {"id": "71111", "file": "7111", "author": "PN", "message": "Totals look of."}],
        ["task", {"id": "7120", "file": "7111", "creator": "JL", "message": "Review the contract", "action": "review"}],
        ["assign", {"id": "7121", "task": "7120", "to": "MC", "by": "JL"}],
        # added for the completeness pass (after the cycle 2 cases were written from this seed)
        ["comment", {"id": "71112", "file": "7111", "author": "OH", "message": "Numbers updated."}],
        ["hub", {"id": "7300", "title": "Finance hub", "creator": "JL"}],
    ],
    "linear": [
        ["team", {"id": "t-web", "name": "Web", "key": "WEB"}], ["team", {"id": "t-mob", "name": "Mobile", "key": "MOB"}],
        ["team", {"id": "t-webx", "name": "Web Tools", "key": "WBT", "parent": "t-web"}],
        ["member", {"team": "t-web", "person": "actor"}],
        ["member", {"team": "t-web", "person": "omar"}],
        ["row", {"table": "workflow_states", "values": {"id": "t-web-st-blocked", "teamId": "t-web", "name": "Blocked",
                                                        "type": "started", "position": 7}}],
        ["cycle", {"id": "cy-web-15", "team": "t-web", "number": 15, "starts": "2026-08-01T00:00:00",
                   "ends": "2026-08-15T00:00:00", "past": True}],
        ["cycle", {"id": "cy-mob-3", "team": "t-mob", "number": 3, "starts": "2026-09-20T00:00:00",
                   "ends": "2026-10-04T00:00:00", "active": True}],
        ["label", {"name": "Bug", "ref": "bug"}],
        ["issue", {"id": "i-web-1", "team": "t-web", "title": "Checkout button broken", "state": "Todo",
                   "due": "2026-09-01", "creator": "maya"}],
        ["issue", {"id": "i-web-2", "team": "t-web", "title": "Payment page slow",
                   "set": {"stateId": "t-web-st-blocked"}}],
        ["issue", {"id": "i-web-3", "team": "t-web", "title": "Sub task", "parent": "i-web-1"}],
        ["comment", {"id": "c-1", "issue": "i-web-1", "author": "priya", "body": "Tpyo in the title."}],
        ["attachment", {"id": "a-1", "issue": "i-web-1", "title": "PR 42", "url": "https://github.com/x/y/pull/42",
                        "source": "github"}],
        ["relation", {"id": "r-1", "issue": "i-web-1", "related": "i-web-2", "type": "blocks"}],
        # added for the completeness pass (after the cycle 2 cases were written from this seed)
        ["cycle", {"id": "cy-web-16", "team": "t-web", "number": 16, "starts": "2026-09-20T00:00:00",
                   "ends": "2026-10-04T00:00:00", "active": True}],
        ["document", {"id": "doc-1", "title": "Checkout spec", "creator": "maya", "team": "t-web"}],
        ["comment", {"id": "c-2", "issue": "i-web-1", "author": "omar", "body": "On it."}],
    ],
}


def slk(method, **params):
    return {"slack": method, "params": params}


def rest(method, path, body=None, params=None):
    c = {"method": method, "path": path}
    if body is not None:
        c["body"] = body
    if params is not None:
        c["params"] = params
    return c


def gql(q):
    return {"graphql": q}


PROFILE = lambda field, value: slk("users.profile.set", user="U_PRIYA", profile=json.dumps({field: value}))
CALLS = {
    "SLA-01": PROFILE("email", "priya.s@northwind.example"), "SLA-02": PROFILE("real_name", "Priya S."),
    "SLA-03": PROFILE("display_name", "PS"), "SLA-04": PROFILE("tz", "Europe/Berlin"),
    "SLA-05": PROFILE("title", "Director"), "SLA-06": slk("users.profile.set", user="U_PRIYA", name="priya.new"),
    "SLA-07": slk("users.admin.setInactive", user="U_LEO"),
    "SLA-09": slk("admin.users.setAdmin", team_id="T1", user_id="U_AISHA"),
    "SLA-10": slk("conversations.rename", channel="C_OPS", name="Payments Ops"),
    "SLA-11": slk("conversations.rename", channel="C_OPS", name="payments-old"),
    "SLA-12": slk("conversations.rename", channel="C_OPS", name="p" * 85),
    "SLA-13": slk("conversations.rename", channel="C_LEG", name="payments-archive"),
    "SLA-14": slk("conversations.setTopic", channel="C_LEG", topic="Archived for good"),
    "SLA-15": slk("conversations.setPurpose", channel="C_LEG", purpose="Archived for good"),
    "SLA-16": slk("admin.conversations.convertToPrivate", channel_id="C_OPS"),
    "SLA-19": slk("conversations.unarchive", channel="C_OLD"),
    "SLA-20": slk("conversations.archive", channel="C_GEN"),
    "SLA-21": slk("conversations.archive", channel="C_LEG"),
    "SLA-22": slk("chat.update", channel="C_OPS", ts="@m_standup", text="Standup moves to 10:30 tomorrow."),
    "SLA-23": slk("chat.update", channel="C_OPS", ts="@m_launch",
                  blocks=json.dumps([{"type": "section", "text": {"type": "mrkdwn", "text": "• Launch day!"}}])),
    "SLA-24": slk("chat.update", channel="C_LEG", ts="@m_leg", text="Updated note."),
    "SLA-26": slk("reactions.remove", channel="C_OPS", timestamp="@m_launch", name="tada"),
    "SLA-27": slk("reactions.add", channel="C_OPS", timestamp="@m_launch", name="eyes"),
    "SLA-30": slk("conversations.invite", channel="C_LEG", users="U_LEO"),
    "SLA-31": slk("conversations.kick", channel="C_OPS", user="U01AGENBOT9"),
    "SLA-32": slk("conversations.kick", channel="C_GEN", user="U_PRIYA"),
    "SLA-33": slk("reactions.remove", channel="C_OPS", timestamp="@m_launch", name="tada"),
    "SLA-37": slk("reactions.remove", channel="C_OPS", timestamp="@m_launch", name="tada"),
    "SLA-38": slk("conversations.leave", channel="C_GEN"),
    "SLA-39": slk("conversations.create", name="payments-ops"),
    "SLA-40": slk("conversations.open", users="U_PRIYA,U_DIEGO,U_LEO,U_OMAR,U_AISHA,U_MAYA,U_KEN,U_LENA,U_RAJ"),
    "SLA-41": slk("chat.delete", channel="C_OPS", ts="@m_standup"),
    "SLA-42": slk("chat.postMessage", channel="C_LEG", text="Release note"),
    "CAL-01": rest("PATCH", "/calendars/maya-team@northwind.example", {"summary": "Design team"}),
    "CAL-02": rest("PATCH", "/calendars/maya-team@northwind.example", {"description": "New description"}),
    "CAL-03": rest("PATCH", "/calendars/maya-team@northwind.example", {"location": "Building 2"}),
    "CAL-04": rest("PATCH", "/calendars/maya-team@northwind.example", {"timeZone": "America/New_York"}),
    "CAL-05": rest("PATCH", "/calendars/projects@northwind.example", {"dataOwner": "omar.haddad@northwind.example"}),
    "CAL-06": rest("POST", "/calendars/leo-oncall@northwind.example/acl",
                   {"role": "writer", "scope": {"type": "user", "value": A}}),
    "CAL-07": rest("DELETE", f"/calendars/{A}/events/ev_sync"),
    "CAL-08": rest("PATCH", "/calendars/leo-oncall@northwind.example/events/ev_handoff", {"summary": "Handoff (moved)"}),
    "CAL-09": rest("PATCH", "/calendars/leo-oncall@northwind.example/events/ev_handoff",
                   {"start": {"dateTime": "2018-06-19T10:00:00-07:00"}, "end": {"dateTime": "2018-06-19T10:30:00-07:00"}}),
    "CAL-10": rest("PATCH", "/calendars/leo-oncall@northwind.example/events/ev_handoff", {"location": "Room 2"}),
    "CAL-11": rest("PATCH", f"/calendars/{A}/events/ev_budget", {"organizer": {"email": "omar.haddad@northwind.example"}}),
    "CAL-12": rest("PATCH", f"/calendars/{A}/events/ev_budget", {"creator": {"email": "omar.haddad@northwind.example"}}),
    "CAL-13": rest("PATCH", f"/calendars/{A}/events/ev_deep", {"eventType": "focusTime"}),
    "CAL-14": rest("PATCH", f"/calendars/{A}/events/ev_review",
                   {"attendees": [{"email": "kenji.sato@northwind.example", "responseStatus": "accepted"},
                                  {"email": "aiko.mori@northwind.example", "responseStatus": "accepted"}]}),
    "CAL-15": rest("POST", "/calendars/maya-team@northwind.example/acl",
                   {"role": "writer", "scope": {"type": "user", "value": "aiko.mori@northwind.example"}}),
    "CAL-16": rest("GET", "/calendars/maya-team@northwind.example/acl"),
    "CAL-17": rest("POST", "/calendars/leo-oncall@northwind.example/acl",
                   {"role": "reader", "scope": {"type": "user", "value": "priya.nair@northwind.example"}}),
    "CAL-18": rest("POST", "/calendars/leo-oncall@northwind.example/events/ev_handoff/move",
                   params={"destination": "maya-team@northwind.example"}),
    "CAL-19": rest("DELETE", f"/calendars/{A}"),
    "BOX-01": rest("PUT", "/files/7111", {"created_at": "2025-01-01T00:00:00Z"}),
    "BOX-02": rest("PUT", "/files/7111", {"modified_at": "2025-01-01T00:00:00Z"}),
    "BOX-03": rest("PUT", "/files/7111", {"size": 1}),
    "BOX-04": rest("PUT", "/files/7111", {"version_number": "7"}),
    "BOX-05": rest("PUT", "/files/7111", {"uploader_display_name": "Leo Park"}),
    "BOX-07": rest("PUT", "/folders/7100", {"created_at": "2025-01-01T00:00:00Z"}),
    "BOX-08": rest("PUT", "/folders/7100", {"modified_at": "2025-01-01T00:00:00Z"}),
    "BOX-09": rest("PUT", "/folders/7100", {"size": 1}),
    "BOX-10": rest("PUT", "/files/7111", {"created_by": {"id": "30000000005"}}),
    "BOX-11": rest("PUT", "/files/7111", {"modified_by": {"id": "30000000005"}}),
    "BOX-12": rest("PUT", "/files/7111", {"owned_by": {"id": "30000000005"}}),
    "BOX-13": rest("PUT", "/comments/71111", {"message": "Totals look off."}),
    "BOX-14": rest("PUT", "/files/7111", {"parent": {"id": "7102"}}),
    "BOX-15": rest("PUT", "/folders/7100", {"parent": {"id": "7101"}}),
    "BOX-16": rest("PUT", "/task_assignments/7121", {"resolution_state": "approved"}),
    "BOX-20": rest("DELETE", "/folders/7100"),
    "BOX-21": rest("PUT", "/files/7111", {"name": "Q3/Q4 budget.pdf"}),
    "LIN-01": gql('mutation { issueUpdate(id: "i-web-1", input: {identifier: "WEB-100"}) { success } }'),
    "LIN-02": gql('mutation { issueUpdate(id: "i-web-1", input: {createdAt: "2026-08-01T00:00:00Z"}) { success } }'),
    "LIN-03": gql('mutation { issueUpdate(id: "i-web-1", input: {updatedAt: "2026-09-21T00:00:00Z"}) { success } }'),
    "LIN-04": gql('mutation { issueUpdate(id: "i-web-1", input: {completedAt: "2026-09-25T00:00:00Z"}) { success } }'),
    "LIN-05": gql('mutation { issueUpdate(id: "i-web-1", input: {priority: 7}) { success } }'),
    "LIN-06": gql('mutation { issueUpdate(id: "i-web-1", input: {estimate: 4}) { issue { id estimate } } }'),
    "LIN-07": gql('mutation { userUpdate(id: "u-maya", input: {name: "Maya C."}) { user { id name } } }'),
    "LIN-08": gql('mutation { userUpdate(id: "u-maya", input: {displayName: "mc"}) { user { id displayName } } }'),
    "LIN-09": gql('mutation { userUpdate(id: "u-maya", input: {email: "mc@northwind.example"}) { user { id } } }'),
    "LIN-10": gql('mutation { userUpdate(id: "u-maya", input: {statusLabel: "Away"}) { user { id } } }'),
    "LIN-11": gql('mutation { userUpdate(id: "u-maya", input: {timezone: "Europe/Berlin"}) { user { id } } }'),
    "LIN-12": gql('mutation { userSuspend(id: "u-leo") { success } }'),
    "LIN-13": gql('mutation { userPromoteAdmin(id: "u-omar") { success } }'),
    "LIN-14": gql('mutation { userUpdate(id: "u-dana", input: {guest: true}) { user { id } } }'),
    "LIN-16": gql('mutation { teamUpdate(id: "t-web", input: {key: "WWW"}) { team { id key } } }'),
    "LIN-17": gql('mutation { teamUpdate(id: "t-web", input: {private: true}) { team { id private } } }'),
    "LIN-18": gql('mutation { teamMembershipUpdate(id: "tm-t-web-omar", input: {owner: true}) { success } }'),
    "LIN-19": gql('mutation { workflowStateUpdate(id: "t-web-st-3", input: {type: "completed"}) { success } }'),
    "LIN-20": gql('mutation { issueLabelUpdate(id: "@bug", input: {isGroup: true}) { success } }'),
    "LIN-21": gql('mutation { cycleUpdate(id: "cy-web-15", input: {number: 20}) { success } }'),
    "LIN-22": gql('mutation { cycleUpdate(id: "cy-web-15", input: {startsAt: "2026-07-25T00:00:00Z"}) { success } }'),
    "LIN-23": gql('mutation { commentUpdate(id: "c-1", input: {body: "Typo in the title."}) { success } }'),
    "LIN-24": gql('mutation { commentUpdate(id: "c-1", input: {createdAt: "2026-08-01T00:00:00Z"}) { success } }'),
    "LIN-25": gql('mutation { attachmentUpdate(id: "a-1", input: {title: "PR 42", sourceType: "slack"}) { success } }'),
    "LIN-26": gql('mutation { issueRelationUpdate(id: "r-1", input: {type: "duplicate"}) { success } }'),
    "LIN-27": gql('mutation { workflowStateArchive(id: "t-web-st-blocked") { success } }'),
    "LIN-28": gql('mutation { issueUpdate(id: "i-web-1", input: {creatorId: "u-leo"}) { success } }'),
    "LIN-29": gql('mutation { commentUpdate(id: "c-1", input: {userId: "u-omar"}) { success } }'),
    "LIN-30": gql('mutation { issueUpdate(id: "i-web-1", input: {stateId: "t-mob-st-3"}) { issue { id state { name } } } }'),
    "LIN-31": gql('mutation { issueUpdate(id: "i-web-1", input: {cycleId: "cy-mob-3"}) { issue { id } } }'),
    "LIN-32": gql('mutation { issueUpdate(id: "i-web-1", input: {parentId: "i-web-3"}) { issue { id } } }'),
    "LIN-33": gql('mutation { teamUpdate(id: "t-web", input: {parentId: "t-webx"}) { team { id } } }'),
    # completeness pass
    **{f"CAL-{n}": rest("PATCH", "/calendars/leo-oncall@northwind.example/events/ev_handoff", body)
       for n, body in ((20, {"description": "Moved"}),
                       (21, {"end": {"dateTime": "2018-06-19T09:45:00-07:00"}}),
                       (22, {"transparency": "transparent"}), (23, {"visibility": "private"}),
                       (24, {"hangoutLink": "https://meet.example/abc"}),
                       (25, {"attendees": [{"email": "priya.nair@northwind.example"}]}),
                       (26, {"attendees": [{"email": "room2@resource.northwind.example", "resource": True}]}),
                       (27, {"attendees": [{"email": "kenji.sato@northwind.example", "optional": True}]}))},
    "CAL-28": rest("PATCH", "/users/me/calendarList/projects@northwind.example", {"primary": True}),
    "BOX-22": rest("PUT", "/comments/71111", {"created_at": "2026-09-01T00:00:00Z"}),
    "BOX-23": rest("PUT", "/tasks/7120", {"created_at": "2026-09-01T00:00:00Z"}),
    "BOX-24": {"method": "PUT", "path": "/hubs/7300", "body": {"created_at": "2026-01-01T00:00:00Z"},
               "headers": {"box-version": "2025.0"}},
    "BOX-25": rest("PUT", "/folders/7100", {"created_by": {"id": "30000000005"}}),
    "BOX-26": rest("PUT", "/folders/7100", {"modified_by": {"id": "30000000005"}}),
    "BOX-27": rest("PUT", "/tasks/7120", {"created_by": {"id": "30000000002"}}),
    "BOX-28": rest("PUT", "/task_assignments/7121", {"assigned_by": {"id": "30000000007"}}),
    "BOX-29": {"method": "PUT", "path": "/hubs/7300", "body": {"created_by": {"id": "30000000006"}},
               "headers": {"box-version": "2025.0"}},
    "BOX-30": {"method": "PUT", "path": "/hubs/7300", "body": {"updated_by": {"id": "30000000006"}},
               "headers": {"box-version": "2025.0"}},
    "BOX-31": rest("PUT", "/folders/7100", {"owned_by": {"id": "30000000005"}}),
    "BOX-32": rest("PUT", "/comments/71111", {"item": {"id": "7112", "type": "file"}}),
    "BOX-33": rest("PUT", "/tasks/7120", {"item": {"id": "7112", "type": "file"}}),
    "BOX-35": rest("PUT", "/comments/71111", {"item": {"id": "71112", "type": "comment"}}),
    "LIN-37": gql('mutation { attachmentUpdate(id: "a-1", input: {title: "PR 42", creatorId: "u-leo"}) { success } }'),
    "LIN-38": gql('mutation { commentUpdate(id: "c-1", input: {resolvingUserId: "u-omar"}) { success } }'),
    "LIN-39": gql('mutation { cycleUpdate(id: "cy-web-16", input: {teamId: "t-mob"}) { success } }'),
    "LIN-40": gql('mutation { workflowStateUpdate(id: "t-web-st-blocked", input: {teamId: "t-mob"}) { success } }'),
    "LIN-41": gql('mutation { documentUpdate(id: "doc-1", input: {creatorId: "u-leo"}) { document { id } } }'),
    "LIN-42": gql('mutation { documentUpdate(id: "doc-1", input: {updatedById: "u-leo"}) { document { id } } }'),
    "LIN-43": gql('mutation { commentUpdate(id: "c-1", input: {issueId: "i-web-2"}) { success } }'),
    "LIN-44": gql('mutation { commentUpdate(id: "c-1", input: {parentId: "c-2"}) { success } }'),
    "LIN-45": gql('mutation { teamUpdate(id: "t-web", input: {name: "Frontend"}) { team { id name } } }'),
    "LIN-46": gql('mutation { teamUpdate(id: "t-web", input: {description: "Web things"}) { team { id } } }'),
    "LIN-47": gql('mutation { cycleUpdate(id: "cy-web-15", input: {endsAt: "2026-08-22T00:00:00Z"}) { success } }'),
}


def field_diff(before: dict, after: dict) -> list[str]:
    """table.column (or table:+row / table:-row) for every relevant change."""
    out = []
    for table in sorted(set(before) | set(after)):
        b = {json.dumps(r.get("id", r.get("channel_id", r.get("message_id", r))), default=str): r
             for r in before.get(table) or []}
        a = {json.dumps(r.get("id", r.get("channel_id", r.get("message_id", r))), default=str): r
             for r in after.get(table) or []}
        out += [f"{table}:+row" for k in a.keys() - b.keys()] + [f"{table}:-row" for k in b.keys() - a.keys()]
        for k in a.keys() & b.keys():
            out += [f"{table}.{c}" for c in a[k] if c not in NOISE and json.dumps(a[k][c], default=str)
                    != json.dumps(b[k].get(c), default=str)]
    return sorted(set(out))


def classify(status, body, changes) -> str:
    err = status is None or status >= 400 or (isinstance(body, dict) and (body.get("errors") or body.get("ok") is False))
    if err:
        return "error, but changed" if changes else "refused loudly"
    return "performed" if changes else "refused silently"


def main(services):
    from agent_diff import AgentDiff
    client, engine = AgentDiff(base_url=BASE), engine_for(DB)
    catalog = json.loads((HERE / "catalog.json").read_text())
    out = HERE / "probes.json"
    results = json.loads(out.read_text()) if out.exists() else {}
    for svc, ops in SEEDS.items():
        if services and svc not in services:
            continue
        seed, refs, actor = seedops.expand(svc, ops)
        case = {"case_id": f"BND2-PROBE-{svc}", "domain": svc, "seed": seed, "acting_user_id": actor,
                "references": [], "prompt": "probe"}
        if svc == "slack":
            template = runtime.install_template(case, engine)
        else:
            metadata = smoke.load_seed_module(svc).Base.metadata
            template = custom_runtime.install_custom_template(svc, seed, engine, case["case_id"])
        try:
            for e in [x for x in catalog if x["service"] == svc]:
                call = CALLS.get(e["id"])
                if call is None:
                    results[e["id"]] = {"outcome": "no call", "expected": e["refusal"]}
                    continue
                call = seedops.resolve(call, refs)
                if "graphql" in call:  # "@ref" inside a query string (resolve() replaces whole values only)
                    for name, value in refs.items():
                        call["graphql"] = call["graphql"].replace(f'"@{name}"', f'"{value}"')
                with ddl_lock():
                    env = client.init_env(templateService=svc, templateName=template["template_name"],
                                          impersonateUserId=actor)
                schema = environment_schema(engine, env.environmentId, template["template_id"])
                export = (lambda: runtime.export_state(engine, schema)) if svc == "slack" else \
                    (lambda: smoke.export_state(engine, schema, metadata))
                before = export()
                status, body = perform_write(client, env.environmentId, svc, call)
                changes = field_diff(before, export())
                outcome = classify(status, body, changes)
                results[e["id"]] = {"outcome": outcome, "expected": e["refusal"], "status": status,
                                    "body": json.dumps(body, default=str)[:400], "changes": changes, "call": call}
                print(f"{e['id']} {outcome:18} (expected {e['refusal']:6}) {status} "
                      f"{json.dumps(body, default=str)[:90]} {changes[:4]}")
                with ddl_lock():
                    client.delete_env(envId=env.environmentId)
        finally:
            if svc == "slack":
                runtime.cleanup(template, DB)
            else:
                smoke.cleanup_isolated_template({**template, "service": svc}, DB)
    out.write_text(json.dumps(results, indent=1) + "\n")
    engine.dispose()


if __name__ == "__main__":
    main(set(sys.argv[1:]))
