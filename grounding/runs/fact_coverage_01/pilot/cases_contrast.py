"""Alternative-vs-plain contrast with absence permitted: one near-miss, no target, "just tell me" prompt.

For each fact, ALT keeps the designated-alternative witness (e.g., created by the named person instead of owned);
PLAIN keeps a witness that fails the same condition without the alternative (the named person has no such role).
"""
from __future__ import annotations

import copy
from functools import partial

from grounding.runs.fact_coverage_01.pilot import cases_box as B
from grounding.runs.fact_coverage_01.pilot import cases_calendar as C
from grounding.runs.fact_coverage_01.pilot import cases_linear as L
from grounding.runs.fact_coverage_01.pilot.cases_isolated import (plain_description, plain_hub_folder, plain_modifier,
                                                                  plain_owner, _plain)
from grounding.runs.fact_coverage_01.pilot.cases_told import told
from grounding.runs.fact_coverage_01.pilot.variants import isolate


def iso(builder, k):
    return isolate(builder(), 0, k)


def plain_folder_creator():
    c = isolate(B.box_06(), 0, 0)
    return _plain(c, [("box_folders", "7002", {"owned_by_id": B.U["DW"]})], {"type": "DROP", "target": "e_fcreator"},
                  "[Plain: Dana owns and created it; Sam has no role.]")


def plain_task_creator():
    c = isolate(B.box_03(form="absent"), 0, 1)
    return _plain(c, [("box_task_assignments", "3303", {"assigned_by_id": B.U["SR"]})], {"type": "DROP", "target": "e_creator"},
                  "[Plain: Sam created and assigned it; Dana has no role.]")


def plain_event_creator():
    c = isolate(C.cal_06(form="absent"), 0, 1)
    c = _plain(c, [("calendar_events", "ev_off_org", {"organizer_email": C.email("sam"), "organizer_display_name": "Sam Rivera"})],
               {"type": "REPLACE", "query": c["references"][0]["query"] | {"filters": [
                   x for x in c["references"][0]["query"]["filters"] if x["key"] != "f_creator"]}, "note": "creator condition dropped"},
               "[Plain: Sam organized and created it; Maya has no role.]")
    return c


def plain_attendee_role():
    c = isolate(C.cal_01(form="absent"), 0, 2)
    for row in c["seed"]["calendar_events"]:
        if row["id"] == "ev_dr_billing":
            row.update(organizer_email=C.email("dana"), organizer_display_name="Dana Whitfield")
    q = copy.deepcopy(c["references"][0]["query"])
    q["edges"] = [{**edge, "node": {**edge["node"], "filters": [f for f in edge["node"]["filters"] if f["key"] != "f_att"]}}
                  for edge in q["edges"]]
    return _plain(c, [], {"type": "REPLACE", "query": q, "note": "attendee person condition dropped"},
                  "[Plain: Dana organizes it; Priya has no role; Omar declined.]")


PAIRS = {
    "owner": (partial(iso, partial(B.box_01, form="absent"), 0), plain_owner),
    "modifier": (partial(iso, partial(B.box_01, form="absent"), 3), plain_modifier),
    "folder-creator": (partial(iso, B.box_06, 0), plain_folder_creator),
    "task-creator": (partial(iso, partial(B.box_03, form="absent"), 1), plain_task_creator),
    "description": (partial(iso, B.box_06, 1), plain_description),
    "hub-inclusion": (partial(iso, B.box_04, 2), plain_hub_folder),
    "event-creator": (partial(iso, partial(C.cal_06, form="absent"), 1), plain_event_creator),
    "attendee-role": (partial(iso, partial(C.cal_01, form="absent"), 2), plain_attendee_role),
    "relation-direction": (partial(iso, L.lin_04, 0), partial(iso, L.lin_04, 3)),
}


def tag(builder, label, kind):
    case = told(builder)
    case["variant_of"] = case.get("variant_of") or case["case_id"]
    case["contrast"] = {"fact": label, "witness": kind}
    old = case["case_id"]
    case["case_id"] = f"CON-{label}-{kind}"
    for r in case["references"]:
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
    return case


CASES = [partial(tag, b, label, kind) for label, (alt, plain) in PAIRS.items()
         for b, kind in ((alt, "alt"), (plain, "plain"))]
