"""Cycle 3 tests: one per service, each hiding matches in the lazy-proof place that cycles 1-2 found.

    python grounding/runs/several_match_02/scenarios.py      # writes scenarios/<id>.json and placements.json

Placement classes: V visible on the natural first query; C1/C2 one or two levels into a container the scope
includes; H behind a visibility default (a hidden calendar, a private channel). Near misses fail one condition each.
Each scenario also records `strategy_entry`: the parameters the strategy runner uses to check, on the built seed,
that every lazy strategy misses a match (probes.py loads them).
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.several_match_01.scenarios import edge, filt, node

HERE = Path(__file__).resolve().parent
A = "jordan.lee@northwind.example"


def box():
    leo = node("box_users", [filt("f_mod", "name", "eq", "Leo Park", "A:User.name")])
    finance = node("box_folders", [filt("f_folder", "name", "eq", "Finance", "A:Folder.name")])
    in_finance = edge("e_parent", "parent_id", "id",
                      node("box_folders", [], [edge("e_anc", "parent_id", "id", finance, "H:Folder.parent_id",
                                                    closure="star")]), "R:File.parent_id")
    query = {"table": "box_files", "filters": [],
             "edges": [edge("e_mod", "modified_by_id", "id", leo, "R:File.modified_by_id"), in_finance]}
    seed = [["folder", {"id": "6100", "name": "Finance"}],
            ["folder", {"id": "6101", "name": "Q1", "parent": "6100"}],
            ["folder", {"id": "6102", "name": "Q2", "parent": "6100"}],
            ["folder", {"id": "6103", "name": "Receipts", "parent": "6102"}],
            ["folder", {"id": "6104", "name": "Finance Archive"}],
            ["file", {"id": "6111", "name": "Budget 2026.pdf", "parent": "6100", "creator": "MC", "modifier": "LP"}],
            ["file", {"id": "6112", "name": "Cash forecast.xlsx", "parent": "6100", "creator": "DW", "modifier": "LP"}],
            ["file", {"id": "6113", "name": "Q1 close summary.docx", "parent": "6101", "creator": "PN",
                      "modifier": "LP"}],
            ["file", {"id": "6114", "name": "Q2 plan.xlsx", "parent": "6102", "creator": "OH", "modifier": "LP"}],
            ["file", {"id": "6115", "name": "Travel receipts June.pdf", "parent": "6103", "creator": "SR",
                      "modifier": "LP"}],
            ["file", {"id": "6121", "name": "Headcount plan.xlsx", "parent": "6100", "creator": "LP", "modifier": "MC"}],
            ["file", {"id": "6122", "name": "Audit notes.docx", "parent": "6104", "creator": "MC", "modifier": "LP"}],
            ["file", {"id": "6123", "name": "Vendor list.pdf", "parent": "6102", "creator": "LP", "modifier": "DW"}],
            ["file", {"id": "6131", "name": "Invoices.xlsx", "parent": "6101", "creator": "DW", "modifier": "DW"}],
            ["file", {"id": "6132", "name": "Q2 forecast.pdf", "parent": "6102", "creator": "PN", "modifier": "PN"}],
            ["file", {"id": "6133", "name": "Hotel receipts May.pdf", "parent": "6103", "creator": "OH",
                      "modifier": "OH"}]]
    creator_leo = lambda: edge("e_mod", "created_by_id", "id", node("box_users", [filt("x", "name", "eq", "Leo Park")]))
    return {
        "scenario_id": "SM2-BOX-01", "domain": "box",
        "request": "Add the tag q3-review to every file anywhere in the Finance folder that Leo Park modified last.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every file anywhere in the Finance folder",
             "facts": ["R:File.parent_id", "A:Folder.name", "H:Folder.parent_id"]},
            {"id": "c2", "text": "that Leo Park modified last", "facts": ["R:File.modified_by_id", "A:User.name"]},
        ],
        "reference": {
            "name": "the files to tag", "target": ["6111", "6112", "6113", "6114", "6115"], "query": query,
            "decoys": [
                {"witness": "6121", "fact": "R:File.modified_by_id", "family": "F1", "substitute": "File.created_by_id",
                 "mutation": {"type": "SUB", "target": "e_mod", "replacement": creator_leo()},
                 "explanation": "In Finance; Leo Park created it, but Maya Chen modified it last."},
                {"witness": "6123", "fact": "R:File.modified_by_id", "family": "F1", "substitute": "File.created_by_id",
                 "mutation": {"type": "SUB", "target": "e_mod", "replacement": creator_leo()},
                 "explanation": "In Finance/Q2; Leo Park created it, but Dana Whitfield modified it last."},
                {"witness": "6122", "fact": "A:Folder.name", "family": "F0", "substitute": "Folder named Finance Archive",
                 "mutation": {"type": "SUB", "target": "e_parent",
                              "replacement": edge("e_parent", "parent_id", "id",
                                                  node("box_folders", [filt("x", "name", "eq", "Finance Archive")]))},
                 "explanation": "Leo Park modified it last, but it is in the separate Finance Archive folder."},
            ],
            "effect": {"table": "box_files", "changes": ["update"]}, "written": ["box_files.tags"],
        },
        "write": {"method": "PUT", "path": "/files/6111", "body": {"tags": ["q3-review"]}},
        "strategy_entry": {"folder": "6100", "words": "Finance", "ext": "pdf", "person": "Leo Park"},
    }, {"6111": "V", "6112": "V", "6113": "C1", "6114": "C1", "6115": "C2"}


def cal_owned_wording():
    """Cycle 4: SM2-CAL-01 with the scope stated as "the calendars I own" (cycle 3's "my calendars" was contestable
    for a calendar the actor can edit but does not own). Everything else is unchanged."""
    s, place = cal()
    s = {**s, "scenario_id": "SM2-CAL-02",
         "request": "Delete every 'Vendor sync' event from Monday, June 18 through Friday, June 22 on the calendars "
                    "I own.",
         "conditions": [{**c, "text": "on the calendars I own"} if c["id"] == "c3" else c for c in s["conditions"]]}
    return s, place


def cal():
    owned = node("calendars", [filt("f_owner", "data_owner", "eq", A, "A:Calendar.data_owner")])
    query = {"table": "calendar_events",
             "filters": [filt("f_title", "summary", "eq", "Vendor sync", "A:Event.summary"),
                         filt("f_from", "start_datetime", "ge", "2018-06-18T00:00:00", "A:Event.start"),
                         filt("f_to", "start_datetime", "lt", "2018-06-23T00:00:00")],
             "edges": [edge("e_cal", "calendar_id", "id", owned, "R:Event.calendar_id")]}
    ev = lambda i, c, day, hour, title="Vendor sync", **kw: ["event", {
        "id": i, "calendar": c, "summary": title, "start": f"2018-06-{day}T{hour}:00:00",
        "end": f"2018-06-{day}T{hour}:30:00", **kw}]
    seed = [["calendar", {"id": "projects@northwind.example", "summary": "Projects"}],
            ["calendar", {"id": "vendors@northwind.example", "summary": "Vendors", "hidden": True}],
            ["calendar", {"id": "maya-team@northwind.example", "summary": "Maya's team", "owner": "maya",
                          "access": "writer"}],
            ev("ev_vs_mon", "primary", "18", "10"), ev("ev_vs_wed", "primary", "20", "10"),
            ev("ev_vs_proj", "projects@northwind.example", "19", "14"),
            ev("ev_vs_vend", "vendors@northwind.example", "21", "09"),
            ev("ev_vs_late", "primary", "25", "10"),
            ev("ev_vs_maya", "maya-team@northwind.example", "19", "11", organizer="maya"),
            ev("ev_vs_prep", "primary", "20", "09", title="Vendor sync prep"),
            ev("ev_budget", "primary", "19", "15", title="Budget review"),
            ev("ev_demo", "projects@northwind.example", "21", "13", title="Sprint demo"),
            ev("ev_onboard", "vendors@northwind.example", "20", "11", title="Supplier onboarding")]
    return {
        "scenario_id": "SM2-CAL-01", "domain": "calendar",
        "request": "Delete every 'Vendor sync' event from Monday, June 18 through Friday, June 22 on my calendars.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every 'Vendor sync' event", "facts": ["A:Event.summary"]},
            {"id": "c2", "text": "from Monday, June 18 through Friday, June 22", "facts": ["A:Event.start"]},
            {"id": "c3", "text": "on my calendars", "facts": ["R:Event.calendar_id", "A:Calendar.data_owner"]},
        ],
        "reference": {
            "name": "the Vendor sync events to delete",
            "target": ["ev_vs_mon", "ev_vs_wed", "ev_vs_proj", "ev_vs_vend"], "query": query,
            "decoys": [
                {"witness": "ev_vs_late", "fact": "A:Event.start", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_to"},
                 "explanation": "A Vendor sync on the primary calendar, but on Monday, June 25."},
                {"witness": "ev_vs_maya", "fact": "A:Calendar.data_owner", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_owner"},
                 "explanation": "A Vendor sync that week, on Maya Chen's calendar, which the actor can edit but does "
                                "not own."},
                {"witness": "ev_vs_prep", "fact": "A:Event.summary", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_title"},
                 "explanation": "On the primary calendar that week, but titled 'Vendor sync prep'."},
            ],
            "effect": {"table": "calendar_events", "changes": ["update", "delete"]}, "written": [],
        },
        "write": {"method": "DELETE", "path": f"/calendars/{A}/events/ev_vs_mon"},
        "strategy_entry": {"from": "2018-06-18T00:00:00-07:00", "to": "2018-06-23T00:00:00-07:00", "q": "Vendor sync"},
    }, {"ev_vs_mon": "V", "ev_vs_wed": "V", "ev_vs_proj": "C1", "ev_vs_vend": "H"}


def lin():
    payments = node("teams", [filt("f_team", "name", "eq", "Payments", "A:Team.name")])
    in_payments = edge("e_team", "teamId", "id",
                       node("teams", [], [edge("e_anc", "parentId", "id", payments, "H:Team.parentId",
                                               closure="star")]), "R:Issue.teamId")
    bug = edge("e_label", "id", "issue_id",
               node("issue_label_issue_association", [], [edge("e_lab", "issue_label_id", "id",
                    node("issue_labels", [filt("f_label", "name", "eq", "Bug", "A:IssueLabel.name")]))]),
               "R:issue_label_issue_association")
    state = edge("e_state", "stateId", "id",
                 node("workflow_states", [filt("f_open", "type", "not_in", ["completed", "canceled"],
                                               "A:WorkflowState.type")]), "R:Issue.stateId")
    query = {"table": "issues", "filters": [], "edges": [state, bug, in_payments]}
    seed = [["team", {"id": "t-pay", "name": "Payments", "key": "PAY"}],
            ["team", {"id": "t-paym", "name": "Payments Mobile", "key": "PAYM", "parent": "t-pay"}],
            ["team", {"id": "t-pios", "name": "Payments iOS", "key": "PIOS", "parent": "t-paym"}],
            ["team", {"id": "t-payw", "name": "Payments Web", "key": "PAYW", "parent": "t-pay"}],
            ["team", {"id": "t-plat", "name": "Platform", "key": "PLAT"}],
            ["label", {"name": "Bug", "ref": "bug"}], ["label", {"name": "Feature", "ref": "feature"}],
            ["issue", {"id": "i-pay-1", "team": "t-pay", "title": "Refund totals off by one cent", "state": "Todo",
                       "assignee": "leo", "labels": ["@bug"]}],
            ["issue", {"id": "i-pay-2", "team": "t-pay", "title": "Duplicate charge on retry", "state": "In Progress",
                       "assignee": "dana", "labels": ["@bug"]}],
            ["issue", {"id": "i-paym-1", "team": "t-paym", "title": "Wallet sheet closes on rotate", "state": "Todo",
                       "assignee": "omar", "labels": ["@bug"]}],
            ["issue", {"id": "i-pios-1", "team": "t-pios", "title": "Apple Pay button misaligned", "state": "Todo",
                       "labels": ["@bug"]}],
            ["issue", {"id": "i-payw-1", "team": "t-payw", "title": "Card field loses focus", "state": "Todo",
                       "assignee": "maya", "labels": ["@bug"]}],
            ["issue", {"id": "i-pay-3", "team": "t-pay", "title": "Payout report timezone wrong", "state": "Done",
                       "assignee": "leo", "labels": ["@bug"]}],
            ["issue", {"id": "i-pay-4", "team": "t-pay", "title": "Support split payments", "state": "Todo",
                       "assignee": "dana", "labels": ["@feature"]}],
            ["issue", {"id": "i-plat-1", "team": "t-plat", "title": "Payment worker leaks connections",
                       "state": "Todo", "assignee": "omar", "labels": ["@bug"]}]]
    people = ["maya", "leo", "dana", "omar", "sam"]
    for i in range(1, 21):
        seed.append(["issue", {"id": f"i-plat-f{i:02d}", "team": "t-plat", "title": f"Platform chore {i}",
                               "state": ["Todo", "In Progress", "Done", "Backlog"][i % 4], "assignee": people[i % 5],
                               "labels": ["@feature"] if i % 3 else []}])
    return {
        "scenario_id": "SM2-LIN-01", "domain": "linear",
        "request": "Assign every open Bug issue in the Payments team or any team under it to Priya Nair.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every open", "facts": ["R:Issue.stateId", "A:WorkflowState.type"]},
            {"id": "c2", "text": "Bug issue", "facts": ["R:issue_label_issue_association", "A:IssueLabel.name"]},
            {"id": "c3", "text": "in the Payments team or any team under it",
             "facts": ["R:Issue.teamId", "A:Team.name", "H:Team.parentId"]},
        ],
        "reference": {
            "name": "the issues to assign",
            "target": ["i-pay-1", "i-pay-2", "i-paym-1", "i-pios-1", "i-payw-1"], "query": query,
            "decoys": [
                {"witness": "i-pay-3", "fact": "A:WorkflowState.type", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_open"}, "explanation": "A Payments bug, but already Done."},
                {"witness": "i-pay-4", "fact": "A:IssueLabel.name", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_label"},
                 "explanation": "An open Payments issue labelled Feature, not Bug."},
                {"witness": "i-plat-1", "fact": "H:Team.parentId", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_team"},
                 "explanation": "An open Bug about payments, but in Platform, which is not under Payments."},
            ],
            "effect": {"table": "issues", "changes": ["update"]}, "written": ["issues.assigneeId"],
        },
        "write": {"graphql": "mutation { issueUpdate(id: \"i-pay-1\", input: {assigneeId: \"u-priya\"}) "
                             "{ issue { id assignee { name } } } }"},
        "strategy_entry": {"team": "Payments", "filtered": (
            '{ issues(first: 250, filter: {team: {name: {eq: "Payments"}}, labels: {some: {name: {eq: "Bug"}}}, '
            'state: {type: {nin: ["completed", "canceled"]}}}) { nodes { id } } }')},
    }, {"i-pay-1": "V", "i-pay-2": "V", "i-paym-1": "C1", "i-payw-1": "C1", "i-pios-1": "C2"}


def slk():
    query = {"table": "channels", "key": ["channel_id"],
             "filters": [filt("f_topic", "topic_text", "contains_ci", "q3 migration", "A:Conversation.topic_text")],
             "edges": []}
    members = ["omar", "leo", "priya"]
    chans = [("C_MIG1", "infra-migration", False, "Tracking the Q3 migration cutover", ""),
             ("C_MIG2", "db-upgrade", False, "Q3 migration: database steps", ""),
             ("C_MIG3", "payments-cutover", True, "Payments track of the Q3 migration", ""),
             ("C_MIG4", "auth-cutover", True, "Auth work for the Q3 migration", ""),
             ("C_NM1", "migration-planning", False, "Planning notes", "Planning the Q3 migration"),
             ("C_NM2", "q4-prep", False, "Q4 migration prep", ""),
             ("C_GEN", "general", False, "Company announcements", ""),
             ("C_RND", "random", False, "Anything goes", "")]
    seed = [["channel", {"id": c, "name": n, "members": members, "private": p, "topic": t, "purpose": pu}]
            for c, n, p, t, pu in chans]
    seed += [["message", {"channel": c, "author": "omar", "text": "Kickoff notes are in the shared doc.",
                          "at": f"2026-09-1{i}T12:00:00Z"}] for i, (c, *_rest) in enumerate(chans[:5], 1)]
    return {
        "scenario_id": "SM2-SLK-01", "domain": "slack",
        "request": "Invite Aisha Khan to every channel whose topic mentions the Q3 migration.",
        "answer": "all", "seed": seed,
        "conditions": [{"id": "c1", "text": "every channel whose topic mentions the Q3 migration",
                        "facts": ["A:Conversation.topic_text"]}],
        "reference": {
            "name": "the channels to invite Aisha to", "target": ["C_MIG1", "C_MIG2", "C_MIG3", "C_MIG4"],
            "query": query,
            "decoys": [
                {"witness": "C_NM1", "fact": "A:Conversation.topic_text", "family": "F1",
                 "substitute": "Conversation.purpose_text",
                 "mutation": {"type": "REPLACE", "note": "the purpose instead of the topic",
                              "query": {"table": "channels", "key": ["channel_id"], "edges": [],
                                        "filters": [filt("x", "purpose_text", "contains_ci", "q3 migration")]}},
                 "explanation": "Its purpose mentions the Q3 migration; its topic is 'Planning notes'."},
                {"witness": "C_NM2", "fact": "A:Conversation.topic_text", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_topic"},
                 "explanation": "Its topic mentions the Q4 migration, not Q3."},
            ],
            "effect": {"table": "channel_members", "changes": ["insert"], "key": ["channel_id", "user_id"],
                       "field": "channel_id"},
            "written": [],
        },
        "write": {"slack": "conversations.invite", "params": {"channel": "C_MIG1", "users": "U_AISHA"}},
        "strategy_entry": {"topic": "Q3 migration"},
    }, {"C_MIG1": "V", "C_MIG2": "V", "C_MIG3": "H", "C_MIG4": "H"}


# ------------------------------------------------------------------ cycle 5
def cal_explicit_hidden():
    """Control: the hidden calendar named by the request's scope. If Qwen then finds it, the cycle 3-4 misses come
    from the default, not from an inability."""
    s, place = cal_owned_wording()
    req = ("Delete every 'Vendor sync' event from Monday, June 18 through Friday, June 22 on the calendars I own, "
           "including any I have hidden.")
    return {**s, "scenario_id": "SM2-CAL-03", "request": req,
            "conditions": [{**c, "text": "on the calendars I own, including any I have hidden"} if c["id"] == "c3"
                           else c for c in s["conditions"]]}, place


def slk_explicit_private():
    """Control: private channels named by the request's scope."""
    s, place = slk()
    return {**s, "scenario_id": "SM2-SLK-02",
            "request": "Invite Aisha Khan to every channel, public or private, whose topic mentions the Q3 migration.",
            "conditions": [{**s["conditions"][0], "text": "every channel, public or private, whose topic mentions "
                                                          "the Q3 migration"}]}, place


def box_pages():
    """A 1,150-file folder: the largest page (1000) leaves 2 matches for a second page. The condition (the last
    modifier) is one no search can express."""
    leo = node("box_users", [filt("f_mod", "name", "eq", "Leo Park", "A:User.name")])
    contracts = node("box_folders", [filt("f_folder", "name", "eq", "Contracts", "A:Folder.name")])
    query = {"table": "box_files", "filters": [],
             "edges": [edge("e_mod", "modified_by_id", "id", leo, "R:File.modified_by_id"),
                       edge("e_parent", "parent_id", "id", contracts, "R:File.parent_id")]}
    seed = [["folder", {"id": "8200", "name": "Contracts"}], ["folder", {"id": "8299", "name": "Contracts Archive"}],
            ["file", {"id": "8201", "name": "Acme MSA.pdf", "parent": "8200", "creator": "MC", "modifier": "LP"}],
            ["file", {"id": "8202", "name": "Birch lease.docx", "parent": "8200", "creator": "DW", "modifier": "LP"}],
            ["file", {"id": "8203", "name": "Zenith SOW.pdf", "parent": "8200", "creator": "PN", "modifier": "LP"}],
            ["file", {"id": "8204", "name": "Zeta NDA.docx", "parent": "8200", "creator": "OH", "modifier": "LP"}],
            ["file", {"id": "8211", "name": "Acme MSA amendment.pdf", "parent": "8200", "creator": "LP",
                      "modifier": "MC"}],
            ["file", {"id": "8212", "name": "Cedar NDA.pdf", "parent": "8299", "creator": "MC", "modifier": "LP"}]]
    others = ["MC", "DW", "PN", "OH", "SR"]
    seed += [["file", {"id": str(90000 + i), "name": f"M-{i:04d} supplier terms.docx", "parent": "8200",
                       "creator": others[i % 5], "modifier": others[(i + 2) % 5]}] for i in range(1, 1145)]
    return {
        "scenario_id": "SM2-BOX-02", "domain": "box",
        "request": "Add the tag legal-hold to every file in the Contracts folder that Leo Park modified last.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every file in the Contracts folder", "facts": ["R:File.parent_id", "A:Folder.name"]},
            {"id": "c2", "text": "that Leo Park modified last", "facts": ["R:File.modified_by_id", "A:User.name"]},
        ],
        "reference": {
            "name": "the files to tag", "target": ["8201", "8202", "8203", "8204"], "query": query,
            "decoys": [
                {"witness": "8211", "fact": "R:File.modified_by_id", "family": "F1", "substitute": "File.created_by_id",
                 "mutation": {"type": "SUB", "target": "e_mod", "replacement": edge(
                     "e_mod", "created_by_id", "id", node("box_users", [filt("x", "name", "eq", "Leo Park")]))},
                 "explanation": "Leo Park created it, but Maya Chen modified it last."},
                {"witness": "8212", "fact": "A:Folder.name", "family": "F0", "substitute": "Folder named Contracts Archive",
                 "mutation": {"type": "SUB", "target": "e_parent", "replacement": edge(
                     "e_parent", "parent_id", "id", node("box_folders", [filt("x", "name", "eq", "Contracts Archive")]))},
                 "explanation": "Leo Park modified it last, but it is in Contracts Archive."},
            ],
            "effect": {"table": "box_files", "changes": ["update"]}, "written": ["box_files.tags"],
        },
        "write": {"method": "PUT", "path": "/files/8201", "body": {"tags": ["legal-hold"]}},
        "strategy_entry": {"folder": "8200", "words": "Contracts", "ext": "pdf", "person": "Leo Park"},
    }, {"8201": "V", "8202": "V", "8203": "P", "8204": "P"}


def slk_pages():
    """An 1,100-message channel: the largest history page (999) leaves 2 matches for a second page. The condition
    (Leo's :rocket: reaction) is one search cannot express."""
    rocket = node("message_reactions", [filt("f_rtype", "reaction_type", "eq", "rocket", "A:Reaction.reaction_type")],
                  [edge("e_ruser", "user_id", "user_id",
                        node("users", [filt("f_ruser", "real_name", "eq", "Leo Park", "A:User.real_name")]),
                        "B:message_reactions.user")])
    query = {"table": "messages", "key": ["message_id"], "filters": [],
             "edges": [edge("e_chan", "channel_id", "channel_id",
                            node("channels", [filt("f_chan", "channel_name", "eq", "deploys",
                                                   "A:Conversation.channel_name")]), "R:messages.channel_id"),
                       edge("e_react", "message_id", "message_id", rocket, "R:message_reactions")]}
    seed = [["channel", {"id": "C_DEP", "name": "deploys", "members": ["priya", "diego", "leo", "omar", "aisha"]}],
            ["channel", {"id": "C_STG", "name": "deploys-staging", "members": ["diego", "leo"]}]]
    authors = ["diego", "omar", "aisha", "priya"]

    def at(i):  # message i of 1100, one every 30 minutes from 2026-07-01
        m = 30 * (i - 1)
        return f"2026-{7 + m // (60 * 24 * 31):02d}-{1 + (m // (60 * 24)) % 31:02d}T{(m // 60) % 24:02d}:{m % 60:02d}:00Z"
    special = {10: ("t1", "leo", "rocket"), 40: ("t2", "leo", "rocket"), 1050: ("t3", "leo", "rocket"),
               1080: ("t4", "leo", "rocket"), 1090: ("nm_priya", "priya", "rocket"), 1095: ("nm_tada", "leo", "tada")}
    for i in range(1, 1101):
        msg = {"channel": "C_DEP", "author": authors[i % 4], "text": f"Deployed build {5000 + i}.", "at": at(i)}
        if i in special:
            msg["ref"] = special[i][0]
        seed.append(["message", msg])
        if i in special:
            seed.append(["reaction", {"message": f"@{special[i][0]}", "person": special[i][1], "name": special[i][2]}])
    seed.append(["message", {"channel": "C_STG", "author": "diego", "text": "Staging build 77 is up.",
                             "at": at(1099), "ref": "nm_chan"}])
    seed.append(["reaction", {"message": "@nm_chan", "person": "leo", "name": "rocket"}])
    return {
        "scenario_id": "SM2-SLK-03", "domain": "slack",
        "request": "Add an :eyes: reaction to every message in #deploys that Leo Park reacted to with :rocket:.",
        "answer": "all", "seed": seed,
        "conditions": [
            {"id": "c1", "text": "every message in #deploys", "facts": ["R:messages.channel_id",
                                                                     "A:Conversation.channel_name"]},
            {"id": "c2", "text": "that Leo Park reacted to with :rocket:",
             "facts": ["R:message_reactions", "A:Reaction.reaction_type", "B:message_reactions.user",
                       "A:User.real_name"]},
        ],
        "reference": {
            "name": "the messages to react to", "target": ["@t1", "@t2", "@t3", "@t4"], "query": query,
            "decoys": [
                {"witness": "@nm_priya", "fact": "B:message_reactions.user", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_ruser"},
                 "explanation": "A #deploys message with a :rocket:, but from Priya Sharma, not Leo."},
                {"witness": "@nm_tada", "fact": "A:Reaction.reaction_type", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_rtype"},
                 "explanation": "Leo reacted to it, but with :tada:."},
                {"witness": "@nm_chan", "fact": "A:Conversation.channel_name", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_chan"},
                 "explanation": "Leo's :rocket:, but in #deploys-staging."},
            ],
            "effect": {"table": "message_reactions", "changes": ["insert"],
                       "key": ["message_id", "user_id", "reaction_type"], "field": "message_id"},
            "written": [],
        },
        "write": {"slack": "reactions.add", "params": {"channel": "C_DEP", "timestamp": "@t3", "name": "eyes"}},
        "strategy_entry": {"prefix": "deploys", "search": "rocket", "channel": "C_DEP"},
    }, {"@t1": "P", "@t2": "P", "@t3": "V", "@t4": "V"}


def box_pages_pdf():
    """SM2-BOX-02's folder with a condition the listing shows. Cycle 5 found that the Box replica's folder listing
    returns only the mini fields, whatever `fields` asks for, so the last modifier took one call per file. The file
    type is in every listed name, so two pages of listing answer the request."""
    s, _ = box_pages()
    contracts = node("box_folders", [filt("f_folder", "name", "eq", "Contracts", "A:Folder.name")])
    query = {"table": "box_files", "filters": [filt("f_ext", "extension", "eq", "pdf", "A:File.extension")],
             "edges": [edge("e_parent", "parent_id", "id", contracts, "R:File.parent_id")]}
    seed = [["file", {**row, "name": "Zeta NDA.pdf"}] if kind == "file" and row["id"] == "8204" else [kind, row]
            for kind, row in s["seed"]]
    return {
        **s, "scenario_id": "SM2-BOX-03", "seed": seed,
        "request": "Add the tag legal-hold to every PDF in the Contracts folder.",
        "conditions": [
            {"id": "c1", "text": "every PDF", "facts": ["A:File.extension"]},
            {"id": "c2", "text": "in the Contracts folder", "facts": ["R:File.parent_id", "A:Folder.name"]},
        ],
        "reference": {
            **s["reference"], "target": ["8201", "8211", "8203", "8204"], "query": query,
            "decoys": [
                {"witness": "8202", "fact": "A:File.extension", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_ext"},
                 "explanation": "In the Contracts folder, but a Word document."},
                {"witness": "8212", "fact": "A:Folder.name", "family": "F0", "substitute": "Folder named Contracts Archive",
                 "mutation": {"type": "SUB", "target": "e_parent", "replacement": edge(
                     "e_parent", "parent_id", "id", node("box_folders", [filt("x", "name", "eq", "Contracts Archive")]))},
                 "explanation": "A PDF, but in Contracts Archive."},
            ],
        },
    }, {"8201": "V", "8211": "V", "8203": "P", "8204": "P"}


def slk_pages_author():
    """SM2-SLK-03's channel with a condition history shows. Cycle 5 found that the Slack replica's history returns
    no reactions, so Leo's :rocket: took one call per message. The author is in every history message (and search's
    `from:` finds them too), so two pages of history answer the request."""
    s, _ = slk_pages()
    leo = node("users", [filt("f_author", "real_name", "eq", "Leo Park", "A:User.real_name")])
    query = {"table": "messages", "key": ["message_id"], "filters": [],
             "edges": [edge("e_chan", "channel_id", "channel_id",
                            node("channels", [filt("f_chan", "channel_name", "eq", "deploys",
                                                   "A:Conversation.channel_name")]), "R:messages.channel_id"),
                       edge("e_author", "user_id", "user_id", leo, "R:messages.user_id")]}
    seed = []
    for kind, row in s["seed"]:
        if kind == "reaction":  # this test's condition is the author
            continue
        if kind == "message" and row.get("ref") in ("t1", "t2", "t3", "t4", "nm_chan"):
            row = {**row, "author": "leo", "text": row["text"].replace("Deployed", "Leo deployed")
                   if row.get("ref") != "nm_chan" else row["text"]}
        elif kind == "message" and row.get("ref") == "nm_priya":
            row = {**row, "author": "priya", "text": "Leo, can you check the build before 6 pm?"}
        elif kind == "message" and row.get("ref") == "nm_tada":
            row = {k: v for k, v in row.items() if k != "ref"}
        seed.append([kind, row])
    return {
        **s, "scenario_id": "SM2-SLK-04", "seed": seed,
        "request": "Add an :eyes: reaction to every message Leo Park posted in #deploys.",
        "conditions": [
            {"id": "c1", "text": "every message in #deploys", "facts": ["R:messages.channel_id",
                                                                     "A:Conversation.channel_name"]},
            {"id": "c2", "text": "that Leo Park posted", "facts": ["R:messages.user_id", "A:User.real_name"]},
        ],
        "reference": {
            **s["reference"], "query": query,
            "decoys": [
                {"witness": "@nm_priya", "fact": "A:User.real_name", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_author"},
                 "explanation": "A #deploys message addressed to Leo, but posted by Priya Sharma."},
                {"witness": "@nm_chan", "fact": "A:Conversation.channel_name", "family": "F0",
                 "mutation": {"type": "DROP", "target": "f_chan"},
                 "explanation": "Posted by Leo, but in #deploys-staging."},
            ],
        },
        "strategy_entry": {"prefix": "deploys", "search": "build", "channel": "C_DEP"},
    }, {"@t1": "P", "@t2": "P", "@t3": "V", "@t4": "V"}


SCENARIOS = [box, cal, lin, slk, cal_owned_wording, cal_explicit_hidden, slk_explicit_private, box_pages, slk_pages,
             box_pages_pdf, slk_pages_author]


def main():
    out = HERE / "scenarios"
    out.mkdir(exist_ok=True)
    placements = {}
    for make in SCENARIOS:
        s, place = make()
        (out / f"{s['scenario_id']}.json").write_text(json.dumps(s, indent=1) + "\n")
        placements[s["scenario_id"]] = place
        print(s["scenario_id"], "targets", len(s["reference"]["target"]), "near misses", len(s["reference"]["decoys"]))
    (HERE / "placements.json").write_text(json.dumps(placements, indent=1) + "\n")


if __name__ == "__main__":
    main()
