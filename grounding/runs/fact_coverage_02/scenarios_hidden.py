"""Hidden-target scenarios for the pilot (method.md, "hidden-target tests"; manual design). No service calls.

Each builder returns a target-present case with one decoy on an easy path and the target off every easy path.
- Arm A reuses a pilot scenario and one of its decoys: the other decoys are removed and, where needed, the target
  moves (CAL-09: from the primary calendar to a shared calendar). The request is unchanged.
- Arm B builds a scenario on one easy path of the domain table: BOX-31 (search matches file names, never comments),
  BOX-32 (a folder's items rather than its owner's files), LIN-31 (Maya's issues rather than her issue's sub-issues).
`probes` record the easy-path calls and one call that follows the stated relation, for the replica check.
"""
from __future__ import annotations

from grounding.runs.fact_coverage_01.pilot import cases_calendar as C
from grounding.runs.fact_coverage_01.pilot.cases_box import ACTOR, FILES, FOLDERS, comment, file, folder, seed, user_is
from grounding.runs.fact_coverage_01.pilot.cases_linear import ACTOR as LIN_ACTOR, Seed as LinearSeed, gql, user_named
from grounding.runs.fact_coverage_01.pilot.common import REPLACE, claim, e, f, n, q, ref
from grounding.runs.fact_coverage_02.scenarios_box import fam


def _drop_events(case, ids):
    s = case["seed"]
    s["calendar_events"] = [r for r in s["calendar_events"] if r["id"] not in ids]
    s["calendar_event_attendees"] = [r for r in s["calendar_event_attendees"] if r["event_id"] not in ids]


def _keep_claims(case, keep):
    ref_ = case["references"][0]
    ref_["claims"] = [c for i, c in enumerate(ref_["claims"]) if i in keep]
    return case


# --- Arm A ------------------------------------------------------------------------------------------------------
def h_cal_02():
    """The series-for-occurrence decoy: the default listing returns the series, the target is its Tuesday session.
    The other series are removed; next week's session of the same series stays (it cannot be removed).
    Dropped from the pilot: the replica check failed. The replica lists a recurring series only when the window
    covers its first start, and a windowed singleEvents query returns nothing, so the default listing shows
    neither the decoy nor the target (runs/prepare_hidden)."""
    case = C.cal_02()
    _drop_events(case, {"ev_psync2", "ev_pstand"})
    case["derived_rows"]["occurrences"] = [r for r in case["derived_rows"]["occurrences"]
                                           if r["recurring_event_id"] == "ev_psync"]
    case = _keep_claims(case, {0, 3})  # D:occurrence (the series) and A:Event.start (next week's session)
    window = {"timeMin": "2018-06-18T00:00:00-07:00", "timeMax": "2018-06-21T00:00:00-07:00"}
    case["probes"] = [("GET", C.EVENTS, None), ("GET", C.EVENTS, window),
                      ("GET", C.EVENTS, dict(window, singleEvents="true"))]
    return case


def h_cal_09():
    """The event on the calendar named "Priya Nair" (organized by Omar); Priya's own meeting sits on a shared
    "Vendor programs" calendar instead of the primary calendar. The lure is the calendar named after her."""
    case = C.cal_09()
    _drop_events(case, {"ev_p_att", "ev_p_wed"})
    s = case["seed"]
    vendor = f"vendor-programs@{C.DOMAIN}"
    s["calendars"].append({"id": vendor, "summary": "Vendor programs", "description": "Vendor onboarding and reviews",
                           "time_zone": C.TZ, "owner_id": "u_dana", "etag": f'"etag_{vendor}"',
                           "data_owner": C.email("dana"), "deleted": False, "created_at": "2018-01-01T00:00:00",
                           "updated_at": "2018-01-01T00:00:00"})
    s["calendar_list_entries"].append({"id": f"cle_{vendor}", "user_id": C.ACTOR, "calendar_id": vendor,
                                       "access_role": "writer", "primary": False, "selected": True, "hidden": False,
                                       "deleted": False, "etag": f'"etag_cle_{vendor}"',
                                       "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"})
    for row in s["calendar_events"]:
        if row["id"] == "ev_p_target":
            row["calendar_id"] = vendor
    s["calendar_event_attendees"] = [r for r in s["calendar_event_attendees"]
                                     if not (r["event_id"] == "ev_p_target" and r["self"])]
    att = max(r["id"] for r in s["calendar_event_attendees"]) + 1
    s["calendar_event_attendees"].append({"id": att, "event_id": "ev_p_target", "email": C.email("sam"),
                                          "display_name": C.PEOPLE["sam"], "response_status": "accepted",
                                          "optional": False, "organizer": False, "self": False, "resource": False})
    case = _keep_claims(case, {0})
    case["lures"] = [{"path": "calendar_named", "phrase": "Priya Nair"}]
    thursday = {"timeMin": "2018-06-21T00:00:00-07:00", "timeMax": "2018-06-22T00:00:00-07:00"}
    case["probes"] = [("GET", "/users/me/calendarList", None), ("GET", C.EVENTS, thursday),
                      ("GET", f"/calendars/priya-team@{C.DOMAIN}/events", thursday),
                      ("GET", f"/calendars/{vendor}/events", thursday)]
    return case


# --- Arm B ------------------------------------------------------------------------------------------------------
def box_31():
    """A comment's text: Box search matches file names and descriptions, never comments. The decoy's file is named
    for the phrase; Priya's comment on it is about something else."""
    s = seed()
    folder(s, "3100", "Finance")
    file(s, "3101", "Q3 forecast.xlsx", "3100", "DW")                                        # target
    comment(s, "3111", "3101", "PN", "Can you double-check the travel costs in this forecast?")
    file(s, "3102", "Travel costs 2026.xlsx", "3100", "DW")                                  # decoy: named for it
    comment(s, "3112", "3102", "PN", "Please add the hiring plan numbers.")
    author = e("e_author", "created_by_id", "id", user_is("f_author", "Priya Nair"), "R:Comment.created_by_id")
    comments = n("box_comments", [f("f_msg", "message", "contains_ci", "travel cost", "A:Comment.message")], [author])
    query = q(FILES, [f("f_ext", "extension", "eq", "xlsx", "A:File.extension")], [
        e("e_comment", "id", "file_id", comments, "R:Comment.file_id")])
    by_name = q(FILES, [f("f_ext", "extension", "eq", "xlsx"), f("f_name", "name", "contains_ci", "travel cost")], [
        e("e_comment", "id", "file_id", n("box_comments", [], [
            e("e_author", "created_by_id", "id", user_is("f_author", "Priya Nair"))]))])
    claims = [fam(claim("A:Comment.message", "3102", REPLACE(by_name, "the comment's text replaced by the file's name"),
                        "The file is named Travel costs 2026; Priya's comment on it is about the hiring plan.",
                        alternative="File.name of the commented file"), "F1")]
    return {
        "case_id": "BOX-31", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Add the tag travel-reviewed to the spreadsheet Priya Nair commented on about travel costs.",
        "references": [ref("BOX-31.r1", "Resolve the spreadsheet", "The spreadsheet with Priya Nair's comment about "
                           "travel costs; only 3101.", "target", query, ["3101"], claims,
                           paths=[{"entities": ["box_files", "box_comments", "box_users"],
                                   "relationships": ["box_comments.file_id", "box_comments.created_by_id"]}],
                           identifying=["box_files.extension", "box_comments.message", "box_comments.created_by_id",
                                        "box_users.name"],
                           written=["box_files.tags"], effect={"table": "box_files", "changes": ["update"]})],
        "probes": [("GET", "/search", {"query": "travel costs"}), ("GET", "/search", {"query": "travel"}),
                   ("GET", "/folders/3100/items", None), ("GET", "/files/3101/comments", None)],
    }


def box_32():
    """A file's last modifier: a folder's easy path is its items. The decoy is the only PDF in the named folder;
    the PDF its owner last modified sits in another folder."""
    s = seed()
    folder(s, "3200", "Budget", owner="MC", creator="LP")
    folder(s, "3300", "Planning")
    file(s, "3301", "Headcount plan.pdf", "3300", "DW", "LP", "MC")                           # target: Maya modified it
    file(s, "3201", "Q4 summary.pdf", "3200", "DW", "DW", "DW")                               # decoy: in Budget
    owner_of_budget = n("box_users", [], [e("e_owns", "id", "owned_by_id", n(FOLDERS, [f("f_b", "name", "eq", "Budget")]))])
    query = q(FILES, [f("f_ext", "extension", "eq", "pdf", "A:File.extension")], [
        e("e_mod", "modified_by_id", "id", owner_of_budget, "R:File.modified_by_id")])
    in_folder = q(FILES, [f("f_ext", "extension", "eq", "pdf")], [
        e("e_mod", "parent_id", "id", n(FOLDERS, [f("f_b", "name", "eq", "Budget")]))])
    claims = [fam(claim("R:File.modified_by_id", "3201",
                        REPLACE(in_folder, "last modified by the folder's owner replaced by located in the folder"),
                        "Q4 summary.pdf sits in Budget, but Dana modified it last.",
                        alternative="File.parent_id (location)"), "F2")]
    return {
        "case_id": "BOX-32", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Add the tag owner-edit to the PDF that the owner of the Budget folder last modified.",
        "references": [ref("BOX-32.r1", "Resolve the PDF", "The PDF last modified by the owner of the Budget folder "
                           "(Maya Chen); only 3301.", "target", query, ["3301"], claims,
                           paths=[{"entities": ["box_files", "box_users", "box_folders"],
                                   "relationships": ["box_files.modified_by_id", "box_folders.owned_by_id"]}],
                           identifying=["box_files.extension", "box_files.modified_by_id", "box_folders.owned_by_id",
                                        "box_folders.name"],
                           written=["box_files.tags"], effect={"table": "box_files", "changes": ["update"]})],
        "probes": [("GET", "/folders/3200/items", None), ("GET", "/folders/3200", None),
                   ("GET", "/folders/3300/items", None), ("GET", "/files/3301", None)],
    }


def lin_31():
    """A sub-issue's parent: a person's easy path is the issues assigned to them. The decoy is a sub-issue assigned to
    Maya (its parent is Sam's); the target is the sub-issue of Maya's issue, assigned to Leo."""
    s = LinearSeed()
    s.team("t-web", "Web", "WEB")
    s.issue("i-31", "t-web", "Checkout redesign", assignee="maya", creator="sam")                          # Maya's issue
    s.issue("i-32", "t-web", "Update the payment form copy", assignee="leo", creator="sam", parent="i-31")  # target
    s.issue("i-33", "t-web", "Cart improvements", assignee="sam", creator="sam")
    s.issue("i-34", "t-web", "Fix the cart badge count", assignee="maya", creator="sam", parent="i-33")    # decoy
    query = q("issues", [], [e("e_parent", "parentId", "id", n("issues", [], [
        e("e_assignee", "assigneeId", "id", user_named("f_maya", "Maya Chen"), "R:Issue.assigneeId")]),
        "H:Issue.parentId")])
    own = q("issues", [f("f_sub", "parentId", "not_null")], [
        e("e_assignee", "assigneeId", "id", user_named("f_maya", "Maya Chen"))])
    claims = [fam(claim("H:Issue.parentId", "i-34", REPLACE(own, "the parent's assignee read as the sub-issue's own"),
                        "Maya is assigned to this sub-issue itself; its parent is Sam's.",
                        alternative="the sub-issue's own assignee"), "F4")]
    return {
        "case_id": "LIN-31", "domain": "linear", "form": "present", "mode": "single", "acting_user_id": LIN_ACTOR,
        "seed": s.seed(), "prompt": "Set the priority to High on the sub-issue whose parent issue is assigned to Maya Chen.",
        "references": [ref("LIN-31.r1", "Resolve the sub-issue", "The sub-issue of the issue assigned to Maya Chen "
                           "(Checkout redesign); only i-32.", "target", query, ["i-32"], claims,
                           paths=[{"entities": ["issues", "users"], "relationships": ["issues.parentId", "issues.assigneeId"]}],
                           identifying=["issues.parentId", "issues.assigneeId", "users.name"],
                           written=["issues.priority"],
                           effect={"table": "issues", "changes": ["update"], "columns": ["priority"]})],
        "probes": [gql('{ issues(filter: { assignee: { name: { eq: "Maya Chen" } } }) '
                       '{ nodes { identifier title parent { identifier } } } }'),
                   gql('{ issues { nodes { identifier title assignee { name } parent { identifier } } } }')],
    }


ARM_A = [(h_cal_09, 0, "CAL-09")]  # builder, claim index of the hidden decoy, scenario (h_cal_02: dropped)
ARM_B = [box_31, box_32, lin_31]
