"""The several-match scenarios (plan.md), written by hand in the kit's scenario format with "answer": "all".

    python grounding/runs/several_match_01/scenarios.py      # writes scenarios/<id>.json and placements.json

Each scenario's targets carry a placement class (plan.md): V visible on the natural first query, C in another
container the request's scope includes, P beyond the first page of the natural listing. Near misses are visible.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def edge(key, parent, child, node, fact=None, **extra):
    e = {"key": key, "join": {"parent": parent, "child": child, "op": "eq"}, "node": node, **extra}
    if fact:
        e["fact"] = fact
    return e


def node(table, filters=(), edges=()):
    return {"table": table, "filters": list(filters), "edges": list(edges)}


def filt(key, field, op, value, fact=None):
    f = {"key": key, "field": field, "op": op, "value": value}
    if fact:
        f["fact"] = fact
    return f


# ---------------------------------------------------------------- SM-BOX-01: subfolders (V + C)
def box_01():
    maya = node("box_users", [filt("f_owner", "name", "eq", "Maya Chen", "A:User.name")])
    finance = node("box_folders", [filt("f_folder", "name", "eq", "Finance", "A:Folder.name")])
    in_finance = edge("e_parent", "parent_id", "id",
                      node("box_folders", [], [edge("e_anc", "parent_id", "id", finance, "H:Folder.parent_id",
                                                    closure="star")]), "R:File.parent_id")
    query = {"table": "box_files", "filters": [filt("f_ext", "extension", "eq", "pdf", "A:File.extension")],
             "edges": [edge("e_owner", "owned_by_id", "id", maya, "R:File.owned_by_id"), in_finance]}
    seed = [
        ["folder", {"id": "5100", "name": "Finance"}],
        ["folder", {"id": "5101", "name": "Q1", "parent": "5100"}],
        ["folder", {"id": "5102", "name": "Q2", "parent": "5100"}],
        ["folder", {"id": "5103", "name": "Receipts", "parent": "5102"}],
        ["folder", {"id": "5104", "name": "Finance Archive"}],
        ["file", {"id": "5111", "name": "Budget 2026.pdf", "parent": "5100", "owner": "MC"}],
        ["file", {"id": "5112", "name": "Cash forecast.pdf", "parent": "5100", "owner": "MC", "modifier": "LP"}],
        ["file", {"id": "5113", "name": "Q1 close summary.pdf", "parent": "5101", "owner": "MC"}],
        ["file", {"id": "5114", "name": "Travel receipts June.pdf", "parent": "5103", "owner": "MC",
                  "modifier": "PN"}],
        ["file", {"id": "5121", "name": "Budget 2026.xlsx", "parent": "5100", "owner": "MC"}],
        ["file", {"id": "5122", "name": "Payroll summary.pdf", "parent": "5100", "owner": "DW", "creator": "MC"}],
        ["file", {"id": "5123", "name": "Audit plan.pdf", "parent": "5104", "owner": "MC"}],
        ["file", {"id": "5131", "name": "Q2 close summary.pdf", "parent": "5102", "owner": "LP"}],
        ["file", {"id": "5132", "name": "Vendor invoices.xlsx", "parent": "5101", "owner": "DW"}],
        ["file", {"id": "5133", "name": "Hotel receipts May.pdf", "parent": "5103", "owner": "PN"}],
    ]
    return {
        "scenario_id": "SM-BOX-01", "domain": "box",
        "request": "Add the tag fy26-audit to every PDF that Maya Chen owns in the Finance folder, including the "
                   "ones in its subfolders.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every PDF", "facts": ["A:File.extension"]},
            {"id": "c2", "text": "that Maya Chen owns", "facts": ["R:File.owned_by_id", "A:User.name"]},
            {"id": "c3", "text": "in the Finance folder, including the ones in its subfolders",
             "facts": ["R:File.parent_id", "A:Folder.name", "H:Folder.parent_id"]},
        ],
        "reference": {
            "name": "the PDFs to tag", "target": ["5111", "5112", "5113", "5114"], "query": query,
            "decoys": [
                {"witness": "5121", "fact": "A:File.extension", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_ext"},
                 "explanation": "Maya Chen's file directly in Finance, but a spreadsheet."},
                {"witness": "5122", "fact": "R:File.owned_by_id", "family": "F1", "substitute": "File.created_by_id",
                 "mutation": {"type": "SUB", "target": "e_owner",
                              "replacement": edge("e_owner", "created_by_id", "id",
                                                  node("box_users", [filt("x", "name", "eq", "Maya Chen")]))},
                 "explanation": "A PDF in Finance that Maya Chen created; Dana Whitfield owns it."},
                {"witness": "5123", "fact": "A:Folder.name", "family": "F0", "substitute": "Folder named Finance Archive",
                 "mutation": {"type": "SUB", "target": "e_parent",
                              "replacement": edge("e_parent", "parent_id", "id",
                                                  node("box_folders", [filt("x", "name", "eq", "Finance Archive")]))},
                 "explanation": "Maya Chen's PDF, but in the separate top-level Finance Archive folder, not in "
                                "Finance or below it."},
            ],
            "effect": {"table": "box_files", "changes": ["update"]}, "written": ["box_files.tags"],
        },
        "write": {"method": "PUT", "path": "/files/5111", "body": {"tags": ["fy26-audit"]}},
    }, {"5111": "V", "5112": "V", "5113": "C", "5114": "C"}


# ---------------------------------------------------------------- SM-BOX-02: a long folder listing (V + P)
def box_02():
    leo = node("box_users", [filt("f_mod", "name", "eq", "Leo Park", "A:User.name")])
    contracts = node("box_folders", [filt("f_folder", "name", "eq", "Contracts", "A:Folder.name")])
    query = {"table": "box_files", "filters": [filt("f_ext", "extension", "eq", "pdf", "A:File.extension")],
             "edges": [edge("e_mod", "modified_by_id", "id", leo, "R:File.modified_by_id"),
                       edge("e_parent", "parent_id", "id", contracts, "R:File.parent_id")]}
    others = ["MC", "DW", "PN", "OH", "LP"]
    seed = [["folder", {"id": "5200", "name": "Contracts"}],
            ["folder", {"id": "5299", "name": "Contracts Archive"}],
            ["file", {"id": "5201", "name": "Acme MSA 2026.pdf", "parent": "5200", "creator": "MC", "modifier": "LP"}],
            ["file", {"id": "5202", "name": "Birchwood lease.pdf", "parent": "5200", "creator": "DW", "modifier": "LP"}],
            ["file", {"id": "5203", "name": "Walker NDA.pdf", "parent": "5200", "creator": "PN", "modifier": "LP"}],
            ["file", {"id": "5204", "name": "Zenith SOW.pdf", "parent": "5200", "creator": "OH", "modifier": "LP"}],
            ["file", {"id": "5211", "name": "Acme MSA 2026.docx", "parent": "5200", "creator": "MC",
                      "modifier": "LP"}],
            ["file", {"id": "5212", "name": "Birchwood lease amendment.pdf", "parent": "5200", "creator": "LP",
                      "modifier": "MC"}],
            ["file", {"id": "5213", "name": "Cedar NDA.pdf", "parent": "5299", "creator": "LP", "modifier": "LP"}]]
    for i in range(1, 111):  # supplier terms, all Word documents, between the B and W names in the listing
        seed.append(["file", {"id": str(5300 + i), "name": f"M-{i:03d} supplier terms.docx", "parent": "5200",
                              "creator": others[i % 5], "modifier": others[(i + 2) % 5]}])
    return {
        "scenario_id": "SM-BOX-02", "domain": "box",
        "request": "Add the tag legal-hold to every PDF in the Contracts folder that Leo Park modified last.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every PDF", "facts": ["A:File.extension"]},
            {"id": "c2", "text": "in the Contracts folder", "facts": ["R:File.parent_id", "A:Folder.name"]},
            {"id": "c3", "text": "that Leo Park modified last", "facts": ["R:File.modified_by_id", "A:User.name"]},
        ],
        "reference": {
            "name": "the PDFs to tag", "target": ["5201", "5202", "5203", "5204"], "query": query,
            "decoys": [
                {"witness": "5211", "fact": "A:File.extension", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_ext"},
                 "explanation": "Leo Park modified it last and it is in Contracts, but it is a Word document."},
                {"witness": "5212", "fact": "R:File.modified_by_id", "family": "F1",
                 "substitute": "File.created_by_id",
                 "mutation": {"type": "SUB", "target": "e_mod",
                              "replacement": edge("e_mod", "created_by_id", "id",
                                                  node("box_users", [filt("x", "name", "eq", "Leo Park")]))},
                 "explanation": "Leo Park created this PDF, but Maya Chen modified it last."},
                {"witness": "5213", "fact": "A:Folder.name", "family": "F0", "substitute": "Folder named Contracts Archive",
                 "mutation": {"type": "SUB", "target": "e_parent",
                              "replacement": edge("e_parent", "parent_id", "id",
                                                  node("box_folders", [filt("x", "name", "eq", "Contracts Archive")]))},
                 "explanation": "A PDF Leo Park modified last, but in the Contracts Archive folder."},
            ],
            "effect": {"table": "box_files", "changes": ["update"]}, "written": ["box_files.tags"],
        },
        "write": {"method": "PUT", "path": "/files/5201", "body": {"tags": ["legal-hold"]}},
    }, {"5201": "V", "5202": "V", "5203": "P", "5204": "P"}


# ---------------------------------------------------------------- Calendar helpers
ACTOR_EMAIL = "jordan.lee@northwind.example"


def owned_calendar():
    return node("calendars", [filt("f_owner", "data_owner", "eq", ACTOR_EMAIL, "A:Calendar.data_owner")])


def calendars_seed():
    return [["calendar", {"id": "projects@northwind.example", "summary": "Projects"}],
            ["calendar", {"id": "vendors@northwind.example", "summary": "Vendors"}],
            ["calendar", {"id": "maya-team@northwind.example", "summary": "Maya's team", "owner": "maya",
                          "access": "writer"}]]


# ---------------------------------------------------------------- SM-CAL-01: owned calendars (V + C)
def cal_01():
    query = {"table": "calendar_events",
             "filters": [filt("f_title", "summary", "eq", "Vendor sync", "A:Event.summary"),
                         filt("f_from", "start_datetime", "ge", "2018-06-18T00:00:00", "A:Event.start"),
                         filt("f_to", "start_datetime", "lt", "2018-06-23T00:00:00")],
             "edges": [edge("e_cal", "calendar_id", "id", owned_calendar(), "R:Event.calendar_id")]}
    ev = lambda i, cal, day, hour, title="Vendor sync", **kw: ["event", {
        "id": i, "calendar": cal, "summary": title, "start": f"2018-06-{day}T{hour}:00:00",
        "end": f"2018-06-{day}T{hour}:30:00", **kw}]
    seed = calendars_seed() + [
        ev("ev_vs_mon", "primary", "18", "10"), ev("ev_vs_wed", "primary", "20", "10"),
        ev("ev_vs_proj", "projects@northwind.example", "19", "14"),
        ev("ev_vs_vend", "vendors@northwind.example", "21", "09"),
        ev("ev_vs_late", "primary", "25", "10"),
        ev("ev_vs_maya", "maya-team@northwind.example", "19", "11", organizer="maya"),
        ev("ev_vs_prep", "primary", "20", "09", title="Vendor sync prep"),
        ev("ev_other1", "primary", "19", "15", title="Budget review"),
        ev("ev_other2", "projects@northwind.example", "21", "13", title="Sprint demo"),
    ]
    return {
        "scenario_id": "SM-CAL-01", "domain": "calendar",
        "request": "Delete every 'Vendor sync' event from Monday, June 18 through Friday, June 22 on the calendars "
                   "I own.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every 'Vendor sync' event", "facts": ["A:Event.summary"]},
            {"id": "c2", "text": "from Monday, June 18 through Friday, June 22", "facts": ["A:Event.start"]},
            {"id": "c3", "text": "on the calendars I own", "facts": ["R:Event.calendar_id", "A:Calendar.data_owner"]},
        ],
        "reference": {
            "name": "the Vendor sync events to delete",
            "target": ["ev_vs_mon", "ev_vs_wed", "ev_vs_proj", "ev_vs_vend"], "query": query,
            "decoys": [
                {"witness": "ev_vs_late", "fact": "A:Event.start", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_to"},
                 "explanation": "A Vendor sync on the actor's primary calendar, but on Monday, June 25."},
                {"witness": "ev_vs_maya", "fact": "A:Calendar.data_owner", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_owner"},
                 "explanation": "A Vendor sync that week, but on Maya Chen's calendar, which the actor can edit and "
                                "does not own."},
                {"witness": "ev_vs_prep", "fact": "A:Event.summary", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_title"},
                 "explanation": "On the primary calendar that week, but titled 'Vendor sync prep', a different "
                                "meeting."},
            ],
            "effect": {"table": "calendar_events", "changes": ["update", "delete"]}, "written": [],
        },
        "write": {"method": "DELETE", "path": f"/calendars/{ACTOR_EMAIL}/events/ev_vs_mon"},
    }, {"ev_vs_mon": "V", "ev_vs_wed": "V", "ev_vs_proj": "C", "ev_vs_vend": "C"}


# ---------------------------------------------------------------- SM-CAL-02: an attendee condition (V + C)
def cal_02():
    att = node("calendar_event_attendees",
               [filt("f_att", "email", "eq", "aiko.mori@northwind.example", "A:EventAttendee.email"),
                filt("f_req", "optional", "ne", True, "A:EventAttendee.optional")])
    query = {"table": "calendar_events",
             "filters": [filt("f_from", "start_datetime", "ge", "2018-06-19T00:00:00", "A:Event.start"),
                         filt("f_to", "start_datetime", "lt", "2018-06-20T00:00:00")],
             "edges": [edge("e_att", "id", "event_id", att, "B:EventAttendee.event_id"),
                       edge("e_cal", "calendar_id", "id", owned_calendar(), "R:Event.calendar_id")]}

    def ev(i, cal, day, hour, title, aiko="required", **kw):
        people = [["kenji", "accepted"], ["omar", "accepted"]]
        if aiko == "required":
            people.append(["aiko", "accepted"])
        elif aiko == "optional":
            people.append(["aiko", "accepted", "optional"])
        return ["event", {"id": i, "calendar": cal, "summary": title, "start": f"2018-06-{day}T{hour}:00:00",
                          "end": f"2018-06-{day}T{hour}:45:00", "attendees": people, **kw}]
    seed = calendars_seed() + [
        ev("ev_design", "primary", "19", "09", "Design review"),
        ev("ev_api", "primary", "19", "13", "API planning"),
        ev("ev_demo", "projects@northwind.example", "19", "11", "Sprint demo"),
        ev("ev_onboard", "vendors@northwind.example", "19", "15", "Supplier onboarding"),
        ev("ev_roadmap", "primary", "19", "10", "Roadmap sync", aiko="optional"),
        ev("ev_followup", "primary", "20", "09", "Design review follow-up"),
        ev("ev_standup", "maya-team@northwind.example", "19", "12", "Team standup", organizer="maya"),
        ev("ev_budget", "primary", "19", "16", "Budget review", aiko="none"),
    ]
    return {
        "scenario_id": "SM-CAL-02", "domain": "calendar",
        "request": "Set the location to Room 4B for every event on Tuesday, June 19 that Aiko Mori is a required "
                   "attendee of, on the calendars I own.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every event on Tuesday, June 19", "facts": ["A:Event.start"]},
            {"id": "c2", "text": "that Aiko Mori is a required attendee of",
             "facts": ["B:EventAttendee.event_id", "A:EventAttendee.email", "A:EventAttendee.optional"]},
            {"id": "c3", "text": "on the calendars I own", "facts": ["R:Event.calendar_id", "A:Calendar.data_owner"]},
        ],
        "reference": {
            "name": "the events to move to Room 4B",
            "target": ["ev_design", "ev_api", "ev_demo", "ev_onboard"], "query": query,
            "decoys": [
                {"witness": "ev_roadmap", "fact": "A:EventAttendee.optional", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_req"},
                 "explanation": "Aiko Mori is invited that Tuesday, but as an optional attendee."},
                {"witness": "ev_followup", "fact": "A:Event.start", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_to"},
                 "explanation": "Aiko Mori is a required attendee, but the event is on Wednesday, June 20."},
                {"witness": "ev_standup", "fact": "A:Calendar.data_owner", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_owner"},
                 "explanation": "Aiko Mori is required that Tuesday, but the event is on Maya Chen's calendar, "
                                "which the actor can edit and does not own."},
            ],
            "effect": {"table": "calendar_events", "changes": ["update", "delete"]},
            "written": ["calendar_events.location"],
        },
        "write": {"method": "PATCH", "path": f"/calendars/{ACTOR_EMAIL}/events/ev_design",
                  "body": {"location": "Room 4B"}},
    }, {"ev_design": "V", "ev_api": "V", "ev_demo": "C", "ev_onboard": "C"}


# ---------------------------------------------------------------- Linear helpers
def open_state():
    return edge("e_state", "stateId", "id",
                node("workflow_states", [filt("f_open", "type", "not_in", ["completed", "canceled"])]),
                "R:Issue.stateId")


# ---------------------------------------------------------------- SM-LIN-01: a long issue list (V + P)
def lin_01():
    query = {"table": "issues", "filters": [],
             "edges": [edge("e_team", "teamId", "id", node("teams", [filt("f_team", "name", "eq", "Platform",
                                                                            "A:Team.name")]), "R:Issue.teamId"),
                       edge("e_asg", "assigneeId", "id", node("users", [filt("f_asg", "name", "eq", "Sam Rivera",
                                                                           "A:User.name")]), "R:Issue.assigneeId"),
                       open_state()]}
    for n in query["edges"][2]["node"]["filters"]:
        n["fact"] = "A:WorkflowState.type"
    seed = [["team", {"id": "t-plat", "name": "Platform", "key": "PLAT"}],
            ["team", {"id": "t-web", "name": "Web", "key": "WEB"}]]
    people = ["maya", "priya", "leo", "dana", "omar"]
    states = ["Todo", "In Progress", "Backlog", "Done", "Todo"]
    titles = ["Rotate service certificates", "Trim log retention", "Upgrade the build image", "Tune pool sizes",
              "Document the deploy flow", "Fix flaky integration test", "Add health checks",
              "Split the config loader", "Profile cold starts", "Pin base images"]

    def day(i):  # creation order: day i of 2026 (the listing is ordered by creation time)
        return f"2026-{1 + (i - 1) // 28:02d}-{1 + (i - 1) % 28:02d}T09:00:00"
    targets = {1: ("i-plat-01", "Todo"), 2: ("i-plat-02", "In Progress"), 69: ("i-plat-69", "Todo"),
               70: ("i-plat-70", "In Progress")}
    for i in range(1, 71):
        if i in targets:
            iid, st = targets[i]
            seed.append(["issue", {"id": iid, "team": "t-plat", "title": f"Migrate queue consumer {i}",
                                   "state": st, "assignee": "sam", "created": day(i)}])
        elif i == 3:
            seed.append(["issue", {"id": "i-plat-03", "team": "t-plat", "title": "Retire the old cron host",
                                   "state": "Done", "assignee": "sam", "created": day(i)}])
        elif i == 4:
            seed.append(["issue", {"id": "i-plat-04", "team": "t-plat", "title": "Shard the metrics store",
                                   "state": "Todo", "assignee": "leo", "creator": "sam", "created": day(i)}])
        else:
            seed.append(["issue", {"id": f"i-plat-{i:02d}", "team": "t-plat", "title": f"{titles[i % 10]} ({i})",
                                   "state": states[i % 5], "assignee": people[i % 5], "created": day(i)}])
    seed.append(["issue", {"id": "i-web-01", "team": "t-web", "title": "Migrate queue consumer for web",
                           "state": "Todo", "assignee": "sam", "created": day(5)}])
    return {
        "scenario_id": "SM-LIN-01", "domain": "linear",
        "request": "Move every open Platform issue assigned to Sam Rivera to In Review.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every open", "facts": ["R:Issue.stateId", "A:WorkflowState.type"]},
            {"id": "c2", "text": "Platform issue", "facts": ["R:Issue.teamId", "A:Team.name"]},
            {"id": "c3", "text": "assigned to Sam Rivera", "facts": ["R:Issue.assigneeId", "A:User.name"]},
        ],
        "reference": {
            "name": "the issues to move", "target": ["i-plat-01", "i-plat-02", "i-plat-69", "i-plat-70"],
            "query": query,
            "decoys": [
                {"witness": "i-plat-03", "fact": "A:WorkflowState.type", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_open"},
                 "explanation": "Sam Rivera's Platform issue, but already Done."},
                {"witness": "i-plat-04", "fact": "R:Issue.assigneeId", "family": "F1", "substitute": "Issue.creatorId",
                 "mutation": {"type": "SUB", "target": "e_asg",
                              "replacement": edge("e_asg", "creatorId", "id",
                                                  node("users", [filt("x", "name", "eq", "Sam Rivera")]))},
                 "explanation": "An open Platform issue that Sam Rivera created; Leo Park is the assignee."},
                {"witness": "i-web-01", "fact": "A:Team.name", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_team"},
                 "explanation": "Sam Rivera's open issue, but in the Web team."},
            ],
            "effect": {"table": "issues", "changes": ["update"]}, "written": ["issues.stateId"],
        },
        "write": {"graphql": "mutation { issueUpdate(id: \"i-plat-01\", input: {stateId: \"t-plat-st-3\"}) "
                             "{ issue { id state { name } } } }"},
    }, {"i-plat-01": "V", "i-plat-02": "V", "i-plat-69": "P", "i-plat-70": "P"}


# ---------------------------------------------------------------- SM-LIN-02: sub-teams (V + C)
def lin_02():
    payments = node("teams", [filt("f_team", "name", "eq", "Payments", "A:Team.name")])
    in_payments = edge("e_team", "teamId", "id",
                       node("teams", [], [edge("e_anc", "parentId", "id", payments, "H:Team.parentId",
                                               closure="star")]), "R:Issue.teamId")
    bug = edge("e_label", "id", "issue_id",
               node("issue_label_issue_association", [], [edge("e_lab", "issue_label_id", "id",
                    node("issue_labels", [filt("f_label", "name", "eq", "Bug", "A:IssueLabel.name")]))]),
               "R:issue_label_issue_association")
    state = open_state()
    state["node"]["filters"][0]["fact"] = "A:WorkflowState.type"
    query = {"table": "issues", "filters": [], "edges": [state, bug, in_payments]}
    seed = [["team", {"id": "t-pay", "name": "Payments", "key": "PAY"}],
            ["team", {"id": "t-paym", "name": "Payments Mobile", "key": "PAYM", "parent": "t-pay"}],
            ["team", {"id": "t-payw", "name": "Payments Web", "key": "PAYW", "parent": "t-pay"}],
            ["team", {"id": "t-plat", "name": "Platform", "key": "PLAT"}],
            ["label", {"name": "Bug", "ref": "bug"}],
            ["label", {"name": "Feature", "ref": "feature"}],
            ["issue", {"id": "i-pay-1", "team": "t-pay", "title": "Refund totals off by one cent", "state": "Todo",
                       "assignee": "leo", "labels": ["@bug"]}],
            ["issue", {"id": "i-pay-2", "team": "t-pay", "title": "Duplicate charge on retry",
                       "state": "In Progress", "assignee": "dana", "labels": ["@bug"]}],
            ["issue", {"id": "i-paym-1", "team": "t-paym", "title": "Apple Pay sheet closes on rotate",
                       "state": "Todo", "assignee": "omar", "labels": ["@bug"]}],
            ["issue", {"id": "i-payw-1", "team": "t-payw", "title": "Card field loses focus on Safari",
                       "state": "Todo", "labels": ["@bug"]}],
            ["issue", {"id": "i-pay-3", "team": "t-pay", "title": "Payout report timezone wrong", "state": "Done",
                       "assignee": "leo", "labels": ["@bug"]}],
            ["issue", {"id": "i-pay-4", "team": "t-pay", "title": "Support split payments", "state": "Todo",
                       "assignee": "dana", "labels": ["@feature"]}],
            ["issue", {"id": "i-plat-1", "team": "t-plat", "title": "Payment worker leaks connections",
                       "state": "Todo", "assignee": "omar", "labels": ["@bug"]}],
            ["issue", {"id": "i-paym-2", "team": "t-paym", "title": "Add wallet onboarding", "state": "Todo",
                       "assignee": "maya", "labels": ["@feature"]}],
            ["issue", {"id": "i-payw-2", "team": "t-payw", "title": "Receipt email typo", "state": "Canceled",
                       "assignee": "sam", "labels": ["@bug"]}],
        ]
    return {
        "scenario_id": "SM-LIN-02", "domain": "linear",
        "request": "Assign every open Bug issue in the Payments team and its sub-teams to Priya Nair.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every open", "facts": ["R:Issue.stateId", "A:WorkflowState.type"]},
            {"id": "c2", "text": "Bug issue", "facts": ["R:issue_label_issue_association", "A:IssueLabel.name"]},
            {"id": "c3", "text": "in the Payments team and its sub-teams",
             "facts": ["R:Issue.teamId", "A:Team.name", "H:Team.parentId"]},
        ],
        "reference": {
            "name": "the issues to assign", "target": ["i-pay-1", "i-pay-2", "i-paym-1", "i-payw-1"], "query": query,
            "decoys": [
                {"witness": "i-pay-3", "fact": "A:WorkflowState.type", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_open"},
                 "explanation": "A Bug issue in Payments, but already Done."},
                {"witness": "i-pay-4", "fact": "A:IssueLabel.name", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_label"},
                 "explanation": "An open Payments issue labelled Feature, not Bug."},
                {"witness": "i-plat-1", "fact": "H:Team.parentId", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_team"},
                 "explanation": "An open Bug issue about payments, but in the Platform team, which is not a "
                                "sub-team of Payments."},
            ],
            "effect": {"table": "issues", "changes": ["update"]}, "written": ["issues.assigneeId"],
        },
        "write": {"graphql": "mutation { issueUpdate(id: \"i-pay-1\", input: {assigneeId: \"u-priya\"}) "
                             "{ issue { id assignee { name } } } }"},
    }, {"i-pay-1": "V", "i-pay-2": "V", "i-paym-1": "C", "i-payw-1": "C"}


# ---------------------------------------------------------------- SM-SLK-01: a long channel history (V + P)
def slk_01():
    query = {"table": "messages", "key": ["message_id"],
             "filters": [filt("f_text", "message_text", "contains_ci", "payments-api", "A:Message.message_text")],
             "edges": [edge("e_user", "user_id", "user_id",
                            node("users", [filt("f_user", "real_name", "eq", "Diego Alvarez", "A:User.real_name")]),
                            "R:messages.user_id"),
                       edge("e_chan", "channel_id", "channel_id",
                            node("channels", [filt("f_chan", "channel_name", "eq", "deploys",
                                                   "A:Conversation.channel_name")]), "R:messages.channel_id")]}
    seed = [["channel", {"id": "C_DEP", "name": "deploys", "members": ["priya", "diego", "leo", "omar", "aisha"]}],
            ["channel", {"id": "C_DEPS", "name": "deploys-staging", "members": ["diego", "leo"]}]]
    services = ["search-api", "auth-service", "billing-worker", "notifications", "web-frontend"]
    authors = ["leo", "omar", "aisha", "priya", "diego"]

    def at(i):  # message i of 140, one every 3 hours from Sept 1; the history lists the newest first
        h = 3 * (i - 1)
        return f"2026-09-{1 + h // 24:02d}T{h % 24:02d}:10:00Z"
    special = {
        3: ("diego", "Deploying payments-api 4.2.0 to production.", "old1"),
        6: ("diego", "payments-api 4.2.0 is live; error rate normal.", "old2"),
        134: ("diego", "Rolling out payments-api 4.3.1 now.", "new1"),
        137: ("diego", "payments-api 4.3.1 done, dashboards green.", "new2"),
        131: ("priya", "Heads up: payments-api migration runs tonight.", "nm_author"),
        135: ("diego", "Deploying payments-web 2.8.0.", "nm_text"),
    }
    for i in range(1, 141):
        if i in special:
            who, text, ref = special[i]
            seed.append(["message", {"channel": "C_DEP", "author": who, "text": text, "at": at(i), "ref": ref}])
        else:
            svc = services[i % 5]
            seed.append(["message", {"channel": "C_DEP", "author": authors[i % 5],
                                     "text": f"Deployed {svc} build {1000 + i}.", "at": at(i)}])
    seed.append(["message", {"channel": "C_DEPS", "author": "diego", "text": "payments-api 4.3.1 on staging.",
                             "at": at(133), "ref": "nm_chan"}])
    return {
        "scenario_id": "SM-SLK-01", "domain": "slack",
        "request": "Add an :eyes: reaction to every message Diego Alvarez posted in #deploys that mentions "
                   "payments-api.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every message Diego Alvarez posted", "facts": ["R:messages.user_id",
                                                                               "A:User.real_name"]},
            {"id": "c2", "text": "in #deploys", "facts": ["R:messages.channel_id", "A:Conversation.channel_name"]},
            {"id": "c3", "text": "that mentions payments-api", "facts": ["A:Message.message_text"]},
        ],
        "reference": {
            "name": "the messages to react to", "target": ["@old1", "@old2", "@new1", "@new2"], "query": query,
            "decoys": [
                {"witness": "@nm_author", "fact": "A:User.real_name", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_user"},
                 "explanation": "A #deploys message about payments-api, but Priya Sharma posted it."},
                {"witness": "@nm_text", "fact": "A:Message.message_text", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_text"},
                 "explanation": "Diego Alvarez's #deploys message, but about payments-web."},
                {"witness": "@nm_chan", "fact": "A:Conversation.channel_name", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_chan"},
                 "explanation": "Diego Alvarez's message about payments-api, but in #deploys-staging."},
            ],
            "effect": {"table": "message_reactions", "changes": ["insert"],
                       "key": ["message_id", "user_id", "reaction_type"], "field": "message_id"},
            "written": [],
        },
        "write": {"slack": "reactions.add", "params": {"channel": "C_DEP", "timestamp": "@new1", "name": "eyes"}},
    }, {"@old1": "P", "@old2": "P", "@new1": "V", "@new2": "V"}


# ---------------------------------------------------------------- SM-SLK-02: several channels by name (V only)
def slk_02():
    query = {"table": "messages", "key": ["message_id"],
             "filters": [filt("f_text", "message_text", "contains_ci", "rollback", "A:Message.message_text")],
             "edges": [edge("e_user", "user_id", "user_id",
                            node("users", [filt("f_user", "real_name", "eq", "Omar Haddad", "A:User.real_name")]),
                            "R:messages.user_id"),
                       edge("e_chan", "channel_id", "channel_id",
                            node("channels", [filt("f_chan", "channel_name", "in",
                                                   ["incident-db", "incident-auth", "incident-payments"],
                                                   "A:Conversation.channel_name")]), "R:messages.channel_id")]}
    members = ["omar", "leo", "priya", "diego"]
    seed = [["channel", {"id": "C_IDB", "name": "incident-db", "members": members}],
            ["channel", {"id": "C_IAU", "name": "incident-auth", "members": members}],
            ["channel", {"id": "C_IPY", "name": "incident-payments", "members": members}],
            ["channel", {"id": "C_IAR", "name": "incidents-archive", "members": members}],
            ["channel", {"id": "C_GEN", "name": "general", "members": members + ["aisha", "maya"]}]]
    msgs = [
        ("C_IDB", "omar", "Starting the rollback of migration 212.", "2026-09-14T12:05:00Z", "t_db"),
        ("C_IDB", "leo", "Replica lag back under a second.", "2026-09-14T12:20:00Z", None),
        ("C_IAU", "omar", "Rollback of auth-service 3.1 complete.", "2026-09-15T12:10:00Z", "t_auth"),
        ("C_IAU", "priya", "Login errors are gone.", "2026-09-15T12:30:00Z", None),
        ("C_IPY", "omar", "Payments rollback to 5.0.2 is underway.", "2026-09-16T11:40:00Z", "t_pay1"),
        ("C_IPY", "omar", "Rollback finished; refunds are processing again.", "2026-09-16T12:15:00Z", "t_pay2"),
        ("C_IPY", "diego", "Rollback plan approved by finance.", "2026-09-16T11:30:00Z", "nm_author"),
        ("C_IAR", "omar", "Closing out last month's rollback notes.", "2026-09-10T12:00:00Z", "nm_chan"),
        ("C_GEN", "omar", "Reminder: rollback drills on Friday.", "2026-09-17T12:00:00Z", "nm_gen"),
        ("C_IDB", "omar", "Index rebuild finished.", "2026-09-14T12:40:00Z", "nm_text"),
    ]
    for chan, who, text, at, ref in msgs:
        m = {"channel": chan, "author": who, "text": text, "at": at}
        if ref:
            m["ref"] = ref
        seed.append(["message", m])
    return {
        "scenario_id": "SM-SLK-02", "domain": "slack",
        "request": "Add a :thumbsup: reaction to every message Omar Haddad posted about a rollback in the "
                   "channels whose names start with incident-.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every message Omar Haddad posted", "facts": ["R:messages.user_id",
                                                                             "A:User.real_name"]},
            {"id": "c2", "text": "about a rollback", "facts": ["A:Message.message_text"]},
            {"id": "c3", "text": "in the channels whose names start with incident-",
             "facts": ["R:messages.channel_id", "A:Conversation.channel_name"]},
        ],
        "reference": {
            "name": "the messages to react to", "target": ["@t_db", "@t_auth", "@t_pay1", "@t_pay2"], "query": query,
            "decoys": [
                {"witness": "@nm_author", "fact": "A:User.real_name", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_user"},
                 "explanation": "A rollback message in #incident-payments, but Diego Alvarez posted it."},
                {"witness": "@nm_chan", "fact": "A:Conversation.channel_name", "family": "F0",
                 "mutation": {"type": "SUB", "target": "e_chan",
                              "replacement": edge("e_chan", "channel_id", "channel_id",
                                                  node("channels", [filt("x", "channel_name", "eq",
                                                                         "incidents-archive")]))},
                 "explanation": "Omar Haddad's rollback message, but in #incidents-archive, whose name starts with "
                                "incidents-, not incident-."},
                {"witness": "@nm_text", "fact": "A:Message.message_text", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_text"},
                 "explanation": "Omar Haddad's message in #incident-db, but about an index rebuild."},
            ],
            "effect": {"table": "message_reactions", "changes": ["insert"],
                       "key": ["message_id", "user_id", "reaction_type"], "field": "message_id"},
            "written": [],
        },
        "write": {"slack": "reactions.add", "params": {"channel": "C_IDB", "timestamp": "@t_db", "name": "thumbsup"}},
    }, {"@t_db": "V", "@t_auth": "V", "@t_pay1": "V", "@t_pay2": "V"}


SCENARIOS = [box_01, box_02, cal_01, cal_02, lin_01, lin_02, slk_01, slk_02]


def main():
    out = HERE / "scenarios"
    out.mkdir(exist_ok=True)
    placements = {}
    for make in SCENARIOS:
        s, place = make()
        (out / f"{s['scenario_id']}.json").write_text(json.dumps(s, indent=1) + "\n")
        placements[s["scenario_id"]] = place
        print(s["scenario_id"], "targets", len(s["reference"]["target"]), "decoys", len(s["reference"]["decoys"]))
    (HERE / "placements.json").write_text(json.dumps(placements, indent=1) + "\n")


if __name__ == "__main__":
    main()
