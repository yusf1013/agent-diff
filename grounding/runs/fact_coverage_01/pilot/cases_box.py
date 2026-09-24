"""Box pilot cases (manual design). Each seed is fresh; IDs are case-local."""
from __future__ import annotations

import json
from functools import partial

from grounding.runs.fact_coverage_01.pilot.common import (DROP, REPLACE, SPLIT, SUB, claim, e, f, n, q, ref)

ACTOR = "30000000001"
USERS = {
    "JL": ("30000000001", "Jordan Lee"), "MC": ("30000000002", "Maya Chen"), "ML": ("30000000003", "Maya Lopez"),
    "LP": ("30000000004", "Leo Park"), "DW": ("30000000005", "Dana Whitfield"), "PN": ("30000000006", "Priya Nair"),
    "OH": ("30000000007", "Omar Haddad"), "SR": ("30000000008", "Sam Rivera"),
}
U = {k: v[0] for k, v in USERS.items()}
T0 = "2026-06-01T09:00:00+00:00"


def seed():
    s = {t: [] for t in ["box_users", "box_collections", "box_folders", "box_files", "box_file_versions",
                         "box_comments", "box_tasks", "box_task_assignments", "box_hubs", "box_hub_items"]}
    for uid, name in USERS.values():
        s["box_users"].append({"id": uid, "type": "user", "name": name,
                               "login": name.lower().replace(" ", ".") + "@northwind.example",
                               "status": "active", "role": "admin" if uid == ACTOR else "user",
                               "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"})
    s["box_folders"].append({"id": "0", "type": "folder", "name": "All Files", "parent_id": None,
                             "owned_by_id": ACTOR, "description": "", "item_status": "active", "size": 0})
    return s


def folder(s, fid, name, parent="0", owner="JL", creator=None, modifier=None, description="", tags=None,
           collections=None, created=T0, modified=T0):
    s["box_folders"].append({"id": fid, "type": "folder", "name": name, "parent_id": parent,
                             "owned_by_id": U[owner], "created_by_id": U[creator or owner],
                             "modified_by_id": U[modifier or creator or owner], "description": description,
                             "item_status": "active", "size": 0, "tags": json.dumps(tags or []),
                             "collections": json.dumps(collections or []),
                             "created_at": created, "modified_at": modified, "sequence_id": "0", "etag": "0"})


def file(s, fid, name, parent, owner, creator=None, modifier=None, *, description="", tags=None, collections=None,
         version=1, shared=False, locked=False, uploader=None, created=T0, modified=T0, size=48213):
    ext = name.rsplit(".", 1)[-1].lower()
    row = {"id": fid, "type": "file", "name": name, "parent_id": parent, "owned_by_id": U[owner],
           "created_by_id": U[creator or owner], "modified_by_id": U[modifier or creator or owner],
           "description": description, "size": size, "extension": ext, "item_status": "active",
           "version_number": str(version), "comment_count": 0, "tags": json.dumps(tags or []),
           "collections": json.dumps(collections or []),
           "created_at": created, "modified_at": modified, "sequence_id": "0", "etag": "0",
           "uploader_display_name": USERS[uploader or modifier or creator or owner][1]}
    if shared:
        row["shared_link"] = json.dumps({"url": f"https://app.box.com/s/{fid}", "access": "company",
                                         "effective_access": "company"})
    if locked:
        row["lock"] = json.dumps({"type": "lock", "id": "L" + fid, "created_by": {"type": "user", "id": U[owner]},
                                  "created_at": T0, "is_download_prevented": False})
    s["box_files"].append(row)
    s["box_file_versions"].append({"id": "9" + fid, "type": "file_version", "file_id": fid, "name": name,
                                   "size": size, "version_number": str(version), "created_at": modified,
                                   "modified_at": modified, "modified_by_id": row["modified_by_id"]})


def comment(s, cid, file_id, author, message, reply_to=None, created="2026-06-10T15:00:00+00:00"):
    s["box_comments"].append({"id": cid, "type": "comment", "file_id": file_id,
                              "item_id": reply_to or file_id, "item_type": "comment" if reply_to else "file",
                              "message": message, "created_by_id": U[author], "created_at": created,
                              "modified_at": created, "is_reply_comment": bool(reply_to)})
    for row in s["box_files"]:
        if row["id"] == file_id:
            row["comment_count"] += 1


def task(s, tid, file_id, creator, message, action="review", done=False, due=None, created=T0):
    s["box_tasks"].append({"id": tid, "type": "task", "item_id": file_id, "item_type": "file", "message": message,
                           "action": action, "is_completed": done, "completion_rule": "all_assignees",
                           "due_at": due, "created_by_id": U[creator], "created_at": created})


def assign(s, aid, tid, file_id, to, by, state="incomplete"):
    s["box_task_assignments"].append({"id": aid, "type": "task_assignment", "task_id": tid, "item_id": file_id,
                                      "item_type": "file", "assigned_to_id": U[to], "assigned_by_id": U[by],
                                      "resolution_state": state, "assigned_at": T0})


HUB_FLAGS = {"is_ai_enabled": False, "is_collaboration_restricted_to_enterprise": False,
             "can_non_owners_invite": True, "can_shared_link_be_created": True, "view_count": 0}


def flip(case, base_form, form, expected_by_ref):
    """Environment-only variant: same request, target rows added or removed."""
    if form in (None, base_form):
        return case
    base_id = case["case_id"]
    case["case_id"] += "-A" if form == "absent" else "-P"
    case["form"] = form
    case["mode"] = "absent" if form == "absent" else "single"
    case["variant_of"] = base_id
    for r in case["references"]:
        if r["id"] in expected_by_ref:
            r["expected"] = expected_by_ref[r["id"]]
            r["resolution"] = "resolved" if r["expected"] else "absent"
            r["description"] += " [" + ("Target removed: no match." if form == "absent" else "Target added.") + "]"
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
    return case


def user_is(key, name, fact=None):
    return n("box_users", [f(key, "name", "eq", name, fact)])


FILES = "box_files"
FOLDERS = "box_folders"
PATH_FILE_OWNER = {"entities": ["box_files", "box_users"], "relationships": ["box_files.owned_by_id"]}


# ---------------------------------------------------------------------------
def box_01(form=None):
    s = seed()
    folder(s, "100", "Finance Reports")
    folder(s, "101", "Drafts", parent="100")
    folder(s, "102", "Finance Archive")
    if form != "absent":
        file(s, "1001", "Q3 revenue summary.pdf", "100", "MC", "DW", "LP")  # target
    file(s, "1002", "Q3 expense summary.pdf", "100", "DW", "MC", "LP")      # creator, not owner
    file(s, "1003", "Q3 revenue summary.xlsx", "100", "MC", "MC", "LP")     # not a PDF
    file(s, "1004", "Q3 forecast.pdf", "101", "MC", "MC", "LP")             # nested under Drafts
    file(s, "1005", "Q3 payroll summary.pdf", "100", "MC", "LP", "MC")      # Leo created, Maya modified
    file(s, "1006", "Q3 vendor summary.pdf", "102", "MC", "MC", "LP")       # other folder
    file(s, "1007", "Q3 travel summary.pdf", "100", "ML", "ML", "LP")       # other Maya
    file(s, "1008", "Board notes.docx", "100", "DW")
    query = q(FILES, [f("f_ext", "extension", "eq", "pdf", "A:File.extension")], [
        e("e_owner", "owned_by_id", "id", user_is("f_owner", "Maya Chen", "A:User.name"), "R:File.owned_by_id"),
        e("e_mod", "modified_by_id", "id", user_is("f_mod", "Leo Park"), "R:File.modified_by_id"),
        e("e_parent", "parent_id", "id", n(FOLDERS, [f("f_folder", "name", "eq", "Finance Reports", "A:Folder.name")]),
          "R:File.parent_id"),
    ])
    nested = q(FILES, [f("f_ext", "extension", "eq", "pdf")], [
        e("e_owner", "owned_by_id", "id", user_is("f_owner", "Maya Chen")),
        e("e_mod", "modified_by_id", "id", user_is("f_mod", "Leo Park")),
        e("e_parent", "parent_id", "id", n(FOLDERS, [], [
            e("e_anc", "parent_id", "id", n(FOLDERS, [f("f_folder", "name", "eq", "Finance Reports")]), closure="star")])),
    ])
    claims = [
        claim("R:File.owned_by_id", "1002", SUB("e_owner", e("e_owner", "created_by_id", "id", user_is("x", "Maya Chen"))),
              "Maya Chen created 1002 but Dana owns it; listings show creator, only file details show owner.",
              alternative="File.created_by_id"),
        claim("A:File.extension", "1003", DROP("f_ext"), "Same owner/modifier/folder, but a spreadsheet."),
        claim("H:Folder.parent_id", "1004", REPLACE(nested, "direct parent replaced by ancestor-or-self"),
              "Matches everything except that it sits in Finance Reports/Drafts, which the request excludes."),
        claim("R:File.modified_by_id", "1005", SUB("e_mod", e("e_mod", "created_by_id", "id", user_is("x", "Leo Park"))),
              "Leo created 1005; Maya modified it last.", alternative="File.created_by_id"),
        claim("A:Folder.name", "1006", DROP("f_folder"), "Same file facts in Finance Archive."),
        claim("A:User.name", "1007", DROP("f_owner"), "Owned by Maya Lopez, not Maya Chen."),
    ]
    return flip({
        "case_id": "BOX-01", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Add the tag q3-close to the PDF that Maya Chen owns directly in the Finance Reports folder "
                  "(not in its subfolders) and that Leo Park modified last.",
        "references": [ref("BOX-01.r1", "Resolve the tagged PDF",
                           "The PDF directly in Finance Reports owned by Maya Chen and last modified by Leo Park; only 1001.",
                           "target", query, ["1001"], claims,
                           paths=[{"entities": ["box_files", "box_users"], "relationships": ["box_files.owned_by_id"]},
                                  {"entities": ["box_files", "box_users"], "relationships": ["box_files.modified_by_id"]},
                                  {"entities": ["box_files", "box_folders"], "relationships": ["box_files.parent_id"]}],
                           identifying=["box_files.extension", "box_files.owned_by_id", "box_users.name",
                                        "box_files.modified_by_id", "box_files.parent_id", "box_folders.name"],
                           written=["box_files.tags"], effect={"table": "box_files", "changes": ["update"]})],
        "probes": [("GET", "/folders/100/items", None), ("GET", "/files/1002", None)],
    }, "present", form, {"BOX-01.r1": []})


# ---------------------------------------------------------------------------
def box_02(form=None):
    s = seed()
    folder(s, "100", "Finance Reports")
    folder(s, "102", "Finance Archive")
    file(s, "2001", "Team budget.xlsx", "100", "DW")
    comment(s, "2101", "2001", "PN", "Can we revisit the hiring plan before we lock this?")
    comment(s, "2102", "2001", "OH", "Travel costs look high this quarter.")
    file(s, "2002", "Events budget.xlsx", "100", "PN")
    comment(s, "2103", "2002", "OH", "Travel costs are over plan for the offsite.")
    file(s, "2003", "Marketing budget.xlsx", "100", "DW")
    comment(s, "2104", "2003", "PN", "Please double-check the hiring plan numbers.")
    file(s, "2004", "Q3 budget.xlsx", "100", "DW")
    file(s, "2005", "Q3 budget.xlsx", "102", "DW")
    comment(s, "2105", "2005", "PN", "Travel costs need a second look before approval.")
    file(s, "2006", "Travel policy.docx", "100", "DW")
    comment(s, "2106", "2006", "PN", "Travel costs should follow the new per-diem.")
    if form == "present":
        file(s, "2007", "Q3 travel budget.xlsx", "100", "DW")
        comment(s, "2107", "2007", "PN", "Travel costs for the offsite look high to me.")
    author_priya = e("e_author", "created_by_id", "id", user_is("f_author", "Priya Nair"), "R:Comment.created_by_id")
    comments = n("box_comments", [f("f_msg", "message", "contains_ci", "travel", "A:Comment.message")], [author_priya])
    query = q(FILES, [f("f_ext", "extension", "eq", "xlsx", "A:File.extension")], [
        e("e_parent", "parent_id", "id", n(FOLDERS, [f("f_folder", "name", "eq", "Finance Reports", "A:Folder.name")]),
          "R:File.parent_id"),
        e("e_comment", "id", "file_id", comments, "R:Comment.file_id"),
    ])
    owner_priya = e("e_author", "file_id", "id", n(FILES, [], [e("e_fo", "owned_by_id", "id", user_is("x", "Priya Nair"))]))
    claims = [
        claim("B:Comment.file_id", "2001", SPLIT("e_comment", ["f_msg"], ["e_author"]),
              "Priya commented on 2001 and a travel comment exists on it, but Omar wrote the travel comment."),
        claim("R:Comment.created_by_id", "2002", SUB("e_author", owner_priya),
              "Priya owns 2002; Omar wrote its travel comment.", alternative="File.owned_by_id of the commented file"),
        claim("A:Comment.message", "2003", DROP("f_msg"), "Priya's comment on 2003 is about hiring, not travel."),
        claim("R:Comment.file_id", "2004", DROP("e_comment"),
              "2004 has no comments; its namesake 2005 in Finance Archive carries Priya's travel comment."),
        claim("R:File.parent_id", "2005", DROP("e_parent"), "Priya's travel comment is on the Finance Archive copy."),
        claim("A:File.extension", "2006", DROP("f_ext"), "Priya's travel comment is on a document, not a spreadsheet."),
    ]
    return flip({
        "case_id": "BOX-02", "domain": "box", "form": "absent", "mode": "absent", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Find the spreadsheet in the Finance Reports folder that Priya Nair commented on about travel costs, "
                  "and add \" - travel reviewed\" to the end of its name.",
        "references": [ref("BOX-02.r1", "Resolve the spreadsheet with Priya's travel comment",
                           "A spreadsheet directly in Finance Reports with a comment written by Priya Nair about travel "
                           "costs. None exists: Priya's travel comments are on the Finance Archive copy and a document; "
                           "the Finance Reports travel comments are Omar's.",
                           "target", query, [], claims,
                           paths=[{"entities": ["box_files", "box_comments", "box_users"],
                                   "relationships": ["box_comments.file_id", "box_comments.created_by_id"]},
                                  {"entities": ["box_files", "box_folders"], "relationships": ["box_files.parent_id"]}],
                           identifying=["box_files.extension", "box_files.parent_id", "box_folders.name",
                                        "box_comments.file_id", "box_comments.message", "box_comments.created_by_id",
                                        "box_users.name"],
                           written=["box_files.name"], effect={"table": "box_files", "changes": ["update"]})],
        "probes": [("GET", "/folders/100/items", None), ("GET", "/files/2001/comments", None),
                   ("GET", "/files/2005/comments", None)],
    }, "absent", form, {"BOX-02.r1": ["2007"]})


# ---------------------------------------------------------------------------
def box_03(form=None):
    s = seed()
    folder(s, "100", "Vendor Contracts")
    file(s, "3100", "Acme vendor contract.pdf", "100", "DW")
    file(s, "3200", "Globex vendor contract.pdf", "100", "DW")
    if form != "absent":
        task(s, "3001", "3100", "DW", "Review indemnity clause")                 # target
        assign(s, "3301", "3001", "3100", "OH", "DW")
    task(s, "3002", "3100", "DW", "Sign off on payment terms", action="complete")
    assign(s, "3302", "3002", "3100", "OH", "DW")
    task(s, "3003", "3100", "SR", "Review renewal dates")
    assign(s, "3303", "3003", "3100", "OH", "DW")
    task(s, "3004", "3100", "DW", "Review liability caps")
    assign(s, "3304", "3004", "3100", "SR", "OH")
    task(s, "3005", "3100", "DW", "Review data-processing addendum")
    assign(s, "3305", "3005", "3100", "OH", "DW", state="completed")
    task(s, "3006", "3100", "DW", "Review termination terms")
    assign(s, "3306", "3006", "3100", "OH", "DW", state="completed")
    assign(s, "3307", "3006", "3100", "SR", "DW")
    task(s, "3007", "3200", "DW", "Review indemnity clause")
    assign(s, "3308", "3007", "3200", "OH", "DW")
    asg = n("box_task_assignments", [f("f_state", "resolution_state", "eq", "incomplete", "A:TaskAssignment.resolution_state")],
            [e("e_to", "assigned_to_id", "id", user_is("f_to", "Omar Haddad"), "R:TaskAssignment.assigned_to_id")])
    query = q("box_tasks", [f("f_action", "action", "eq", "review", "A:Task.action")], [
        e("e_creator", "created_by_id", "id", user_is("f_creator", "Dana Whitfield"), "R:Task.created_by_id"),
        e("e_file", "item_id", "id", n(FILES, [f("f_file", "name", "contains_ci", "Acme vendor contract")]), "R:Task.item_id"),
        e("e_asg", "id", "task_id", asg, "B:TaskAssignment.task_id"),
    ])
    by_dana = e("e_creator", "id", "task_id", n("box_task_assignments", [], [
        e("e_by", "assigned_by_id", "id", user_is("x", "Dana Whitfield"))]))
    claims = [
        claim("A:Task.action", "3002", DROP("f_action"), "A completion task, not a review task."),
        claim("R:Task.created_by_id", "3003", SUB("e_creator", by_dana),
              "Sam created 3003; Dana only assigned it to Omar.", alternative="TaskAssignment.assigned_by_id"),
        claim("R:TaskAssignment.assigned_to_id", "3004",
              SUB("e_asg", e("e_asg", "id", "task_id", n("box_task_assignments",
                  [f("f_state", "resolution_state", "eq", "incomplete")],
                  [e("e_to", "assigned_by_id", "id", user_is("x", "Omar Haddad"))]))),
              "Omar assigned 3004 to Sam; he is not the assignee.", alternative="TaskAssignment.assigned_by_id"),
        claim("A:TaskAssignment.resolution_state", "3005", DROP("f_state"), "Omar already completed 3005."),
        claim("B:TaskAssignment.task_id", "3006", SPLIT("e_asg", ["f_state"], ["e_to"]),
              "Omar's assignment on 3006 is completed; Sam's is the incomplete one."),
        claim("R:Task.item_id", "3007", DROP("e_file"), "Same task pattern on the Globex contract."),
    ]
    return flip({
        "case_id": "BOX-03", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Set the due date to October 9, 2026 on the review task Dana Whitfield created on the Acme vendor "
                  "contract that's assigned to Omar Haddad and that Omar hasn't completed yet.",
        "references": [ref("BOX-03.r1", "Resolve the task to update",
                           "Dana's review task on the Acme vendor contract with an incomplete assignment to Omar; only 3001.",
                           "target", query, ["3001"], claims,
                           paths=[{"entities": ["box_tasks", "box_users"], "relationships": ["box_tasks.created_by_id"]},
                                  {"entities": ["box_tasks", "box_files"], "relationships": ["box_tasks.item_id"]},
                                  {"entities": ["box_tasks", "box_task_assignments", "box_users"],
                                   "relationships": ["box_task_assignments.task_id", "box_task_assignments.assigned_to_id"]}],
                           identifying=["box_tasks.action", "box_tasks.created_by_id", "box_tasks.item_id", "box_files.name",
                                        "box_task_assignments.task_id", "box_task_assignments.assigned_to_id",
                                        "box_task_assignments.resolution_state", "box_users.name"],
                           written=["box_tasks.due_at"], effect={"table": "box_tasks", "changes": ["delete", "update"]})],
        "probes": [("GET", "/files/3100/tasks", None)],
        "notes": "Action changed from delete to due-date update after DELETE /tasks returned 500 in qwen_box_02.",
    }, "present", form, {"BOX-03.r1": []})


# ---------------------------------------------------------------------------
def box_04(form=None):
    s = seed()
    folder(s, "4000", "Marketing")
    folder(s, "4001", "Launch assets", parent="4000")
    folder(s, "4002", "Q4 campaign", parent="4000")
    folder(s, "4030", "Brand guidelines", parent="4000", owner="MC", creator="DW")   # target folder
    folder(s, "4031", "Brand guidelines", parent="0", owner="SR", creator="MC")      # created, not owned, by Maya
    file(s, "4010", "Launch assets.pdf", "4002", "LP")
    s["box_hubs"] += [
        {"id": "5002", "type": "hubs", "title": "Launch kit", "description": "Everything for the launch",
         "created_by_id": U["DW"], "updated_by_id": U["LP"], "created_at": T0, "updated_at": T0, **HUB_FLAGS},
        {"id": "5003", "type": "hubs", "title": "Campaign board", "description": "Campaign planning",
         "created_by_id": U["LP"], "updated_by_id": U["LP"], "created_at": T0, "updated_at": T0, **HUB_FLAGS},
        {"id": "5004", "type": "hubs", "title": "Marketing hub", "description": "Marketing team materials",
         "created_by_id": U["LP"], "updated_by_id": U["LP"], "created_at": T0, "updated_at": T0, **HUB_FLAGS},
    ]
    s["box_hub_items"] += [
        {"id": "5101", "type": "hub_item", "added_at": T0, "added_by_id": U["DW"], "hub_id": "5002", "item_id": "4001", "item_type": "folder", "item_name": "Launch assets", "position": 1},
        {"id": "5102", "type": "hub_item", "added_at": T0, "added_by_id": U["LP"], "hub_id": "5003", "item_id": "4002", "item_type": "folder", "item_name": "Q4 campaign", "position": 1},
        {"id": "5103", "type": "hub_item", "added_at": T0, "added_by_id": U["LP"], "hub_id": "5003", "item_id": "4010", "item_type": "file", "item_name": "Launch assets.pdf", "position": 2},
        {"id": "5104", "type": "hub_item", "added_at": T0, "added_by_id": U["LP"], "hub_id": "5004", "item_id": "4000", "item_type": "folder", "item_name": "Marketing", "position": 1},
    ]
    if form == "present":
        s["box_hubs"].append({"id": "5005", "type": "hubs", "title": "Launch hub", "description": "Launch materials",
                              "created_by_id": U["LP"], "updated_by_id": U["LP"], "created_at": T0, "updated_at": T0,
                              **HUB_FLAGS})
        s["box_hub_items"].append({"id": "5105", "type": "hub_item", "added_at": T0, "added_by_id": U["LP"],
                                   "hub_id": "5005", "item_id": "4001", "item_type": "folder",
                                   "item_name": "Launch assets", "position": 1})
    items = n("box_hub_items", [f("f_type", "item_type", "eq", "folder"),
                                f("f_name", "item_name", "contains_ci", "Launch assets")])
    hub_query = q("box_hubs", [], [
        e("e_hcreator", "created_by_id", "id", user_is("f_hc", "Leo Park"), "R:Hub.created_by_id"),
        e("e_item", "id", "hub_id", items, "R:HubItem.folder"),
    ])
    nested_items = n("box_hub_items", [f("f_type", "item_type", "eq", "folder")], [
        e("e_hf", "item_id", "id", n(FOLDERS, [], [
            e("e_sub", "id", "parent_id", n(FOLDERS, [f("f_name", "name", "eq", "Launch assets")]), closure="star")]))])
    hub_claims = [
        claim("R:Hub.created_by_id", "5002", SUB("e_hcreator", e("e_hcreator", "updated_by_id", "id", user_is("x", "Leo Park"))),
              "Dana created Launch kit; Leo only updated it.", alternative="Hub.updated_by_id"),
        claim("B:HubItem.hub_id", "5003", SPLIT("e_item", ["f_type"], ["f_name"]),
              "Campaign board has a folder entry and a Launch-assets entry, but the latter is a file."),
        claim("R:HubItem.folder", "5004", REPLACE(q("box_hubs", [], [
                  e("e_hcreator", "created_by_id", "id", user_is("f_hc", "Leo Park")), e("e_item", "id", "hub_id", nested_items)]),
                  "hub entry replaced by a folder whose subtree contains Launch assets"),
              "Marketing hub includes the Marketing folder, inside which Launch assets lives.",
              alternative="folder nested inside a hub folder"),
    ]
    folder_query = q(FOLDERS, [f("f_fname", "name", "eq", "Brand guidelines")], [
        e("e_fowner", "owned_by_id", "id", user_is("f_fo", "Maya Chen"), "R:Folder.owned_by_id")])
    folder_claims = [
        claim("R:Folder.owned_by_id", "4031", SUB("e_fowner", e("e_fowner", "created_by_id", "id", user_is("x", "Maya Chen"))),
              "Maya created the other Brand guidelines folder; Sam owns it.", alternative="Folder.created_by_id"),
    ]
    return flip({
        "case_id": "BOX-04", "domain": "box", "form": "absent", "mode": "absent", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Add the Brand guidelines folder that Maya Chen owns to the hub Leo Park created that already "
                  "includes the Launch assets folder.",
        "references": [
            ref("BOX-04.r1", "Resolve the destination hub",
                "A hub created by Leo Park with a folder entry named Launch assets. None: Launch kit was created by Dana; "
                "Leo's hubs contain a Launch-assets file or the Marketing folder.",
                "target", hub_query, [], hub_claims,
                paths=[{"entities": ["box_hubs", "box_users"], "relationships": ["box_hubs.created_by_id"]},
                       {"entities": ["box_hubs", "box_hub_items"], "relationships": ["box_hub_items.hub_id"]}],
                identifying=["box_hubs.created_by_id", "box_users.name", "box_hub_items.hub_id",
                             "box_hub_items.item_type", "box_hub_items.item_name"], written=[],
                effect={"table": "box_hub_items", "changes": ["insert"], "field": "hub_id", "all": True}),
            ref("BOX-04.r2", "Resolve the Brand guidelines folder",
                "The Brand guidelines folder owned by Maya Chen; only 4030.", "target", folder_query, ["4030"], folder_claims,
                paths=[{"entities": ["box_folders", "box_users"], "relationships": ["box_folders.owned_by_id"]}],
                identifying=["box_folders.name", "box_folders.owned_by_id", "box_users.name"],
                written=["box_hub_items.item_id"],
                effect={"table": "box_hub_items", "changes": ["insert"], "field": "item_id", "all": True}),
        ],
        "probes": [("GET", "/hubs", None, {"box-version": "2025.0"}),
                   ("GET", "/hub_items", {"hub_id": "5003"}, {"box-version": "2025.0"}),
                   ("GET", "/folders/4031", None)],
    }, "absent", form, {"BOX-04.r1": ["5005"]})


# ---------------------------------------------------------------------------
def box_05(form=None):
    s = seed()
    s["box_collections"] += [{"id": "9101", "type": "collection", "name": "Favorites", "collection_type": "favorites"}]
    folder(s, "100", "Planning")
    folder(s, "6100", "Budget pack", parent="100", collections=["9101"])
    if form != "absent":
        file(s, "6001", "Headcount plan.xlsx", "100", "JL", collections=["9101"], shared=True, locked=True)  # target
        file(s, "6002", "Vendor spend.xlsx", "100", "JL", collections=["9101"], shared=True, locked=True)    # target
    file(s, "6003", "Pack summary.xlsx", "6100", "JL", shared=True, locked=True)          # inside collected folder
    file(s, "6004", "Travel spend.xlsx", "100", "JL", collections=["9101"], locked=True)   # no shared link
    file(s, "6005", "Office spend.xlsx", "100", "JL", collections=["9101"], shared=True)   # not locked
    file(s, "6007", "Pricing.pdf", "100", "JL", collections=["9101"], shared=True, locked=True)
    query = q(FILES, [f("f_ext", "extension", "eq", "xlsx", "A:File.extension"),
                      f("f_lock", "lock", "not_null", None, "A:File.lock"),
                      f("f_link", "shared_link", "not_null", None, "A:File.shared_link")], [
        e("e_coll", "collections", "id", n("box_collections", [f("f_cname", "name", "eq", "Favorites")]),
          "R:File.collections", op="json_contains")])
    in_folder = e("e_coll", "parent_id", "id", n(FOLDERS, [], [
        e("e_fc", "collections", "id", n("box_collections", [f("x", "name", "eq", "Favorites")]), op="json_contains")]))
    claims = [
        claim("R:File.collections", "6003", SUB("e_coll", in_folder),
              "6003 is inside the Budget pack folder, which is in Favorites; the file itself is not.",
              alternative="file inside a collected folder"),
        claim("A:File.shared_link", "6004", DROP("f_link"), "Locked and in Favorites, but has no shared link to remove."),
        claim("A:File.lock", "6005", DROP("f_lock"), "Shared and in Favorites, but not locked."),
        claim("A:File.extension", "6007", DROP("f_ext"), "A PDF, not a spreadsheet."),
    ]
    return flip({
        "case_id": "BOX-05", "domain": "box", "form": "present", "mode": "multiple", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Remove the shared links from the locked spreadsheets in my Favorites collection.",
        "references": [ref("BOX-05.r1", "Resolve the spreadsheets to unshare",
                           "Every locked spreadsheet with a shared link that is itself in the Favorites collection: 6001 and 6002.",
                           "target", query, ["6001", "6002"], claims,
                           paths=[{"entities": ["box_files", "box_collections"], "relationships": ["box_files.collections"]}],
                           identifying=["box_files.extension", "box_files.lock", "box_files.shared_link",
                                        "box_files.collections"],
                           written=["box_files.shared_link"], effect={"table": "box_files", "changes": ["update"]})],
        "probes": [("GET", "/collections", None), ("GET", "/collections/9101/items", None), ("GET", "/files/6004", None)],
        "notes": "Replica quirk: PUT /files without a lock field clears the lock; lock changes on the targets are collateral.",
    }, "present", form, {"BOX-05.r1": []})


# ---------------------------------------------------------------------------
def box_06(form=None):
    s = seed()
    folder(s, "7000", "Projects")
    folder(s, "7090", "Archive", parent="7000")
    common = dict(tags=["client"])
    folder(s, "7002", "Atlas launch", parent="7000", owner="SR", creator="DW", description="Atlas rollout workspace", **common)
    folder(s, "7003", "Atlas team", parent="7000", owner="SR", creator="SR", description="Borealis migration notes", **common)
    folder(s, "7004", "Atlas rollout", parent="7000", owner="SR", creator="SR", description="Atlas rollout plan", **common)
    folder(s, "7005", "Atlas rollout (old)", parent="7090", owner="SR", creator="SR", description="Atlas rollout drafts", **common)
    folder(s, "7006", "Atlas internal", parent="7000", owner="SR", creator="SR", description="Atlas rollout checklist",
           tags=["internal"])
    file(s, "7102", "Rollout plan.pdf", "7002", "MC")
    file(s, "7103", "Migration plan.pdf", "7003", "MC")
    file(s, "7104", "Rollout budget.pdf", "7004", "DW")
    file(s, "7105", "Rollout notes.docx", "7004", "MC")
    file(s, "7106", "Old rollout plan.pdf", "7005", "MC")
    file(s, "7107", "Checklist.pdf", "7006", "MC")
    if form == "present":
        folder(s, "7007", "Rollout Q3", parent="7000", owner="SR", creator="SR", description="Atlas rollout tracking",
               tags=["client"])
        file(s, "7108", "Rollout tracker.pdf", "7007", "MC")
    files = n(FILES, [f("f_pdf", "extension", "eq", "pdf")], [
        e("e_powner", "owned_by_id", "id", user_is("f_po", "Maya Chen"))])
    query = q(FOLDERS, [f("f_desc", "description", "contains_ci", "Atlas rollout", "A:Folder.description"),
                        f("f_tags", "tags", "json_has", "client", "A:Folder.tags")], [
        e("e_fcreator", "created_by_id", "id", user_is("f_fc", "Sam Rivera"), "R:Folder.created_by_id"),
        e("e_fparent", "parent_id", "id", n(FOLDERS, [f("f_proj", "name", "eq", "Projects")]), "H:Folder.parent_id"),
        e("e_files", "id", "parent_id", files, "B:File.parent_id"),
    ])
    nested = q(FOLDERS, [f("f_desc", "description", "contains_ci", "Atlas rollout"), f("f_tags", "tags", "json_has", "client")], [
        e("e_fcreator", "created_by_id", "id", user_is("f_fc", "Sam Rivera")),
        e("e_fparent", "parent_id", "id", n(FOLDERS, [f("f_proj", "name", "eq", "Projects")]), closure=True),
        e("e_files", "id", "parent_id", files)])
    claims = [
        claim("R:Folder.created_by_id", "7002", SUB("e_fcreator", e("e_fcreator", "owned_by_id", "id", user_is("x", "Sam Rivera"))),
              "Sam owns Atlas launch, but Dana created it.", alternative="Folder.owned_by_id"),
        claim("A:Folder.description", "7003", DROP("f_desc"), "Description is about the Borealis migration."),
        claim("B:File.parent_id", "7004", SPLIT("e_files", ["f_pdf"], ["e_powner"]),
              "Atlas rollout holds a PDF (Dana's) and a Maya-owned file (a document)."),
        claim("H:Folder.parent_id", "7005", REPLACE(nested, "direct parent replaced by ancestor"),
              "Under Projects/Archive, not directly under Projects."),
        claim("A:Folder.tags", "7006", DROP("f_tags"), "Tagged internal, not client."),
    ]
    return flip({
        "case_id": "BOX-06", "domain": "box", "form": "absent", "mode": "absent", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Sam Rivera created a client-tagged folder directly under Projects for the Atlas rollout (its "
                  "description says so) that holds a PDF Maya Chen owns. Add the tag atlas-q3 to that folder.",
        "references": [ref("BOX-06.r1", "Resolve the Atlas rollout folder",
                           "A client-tagged folder directly under Projects, created by Sam Rivera, whose description "
                           "mentions the Atlas rollout and which contains a PDF owned by Maya Chen. None exists.",
                           "target", query, [], claims,
                           paths=[{"entities": ["box_folders", "box_users"], "relationships": ["box_folders.created_by_id"]},
                                  {"entities": ["box_folders", "box_folders"], "relationships": ["box_folders.parent_id"]},
                                  {"entities": ["box_folders", "box_files", "box_users"],
                                   "relationships": ["box_files.parent_id", "box_files.owned_by_id"]}],
                           identifying=["box_folders.description", "box_folders.tags", "box_folders.created_by_id",
                                        "box_folders.parent_id", "box_files.parent_id", "box_files.extension",
                                        "box_files.owned_by_id", "box_users.name"],
                           written=["box_folders.tags"], effect={"table": "box_folders", "changes": ["update"]})],
        "probes": [("GET", "/folders/7000/items", None), ("GET", "/folders/7002", None), ("GET", "/folders/7004/items", None)],
    }, "absent", form, {"BOX-06.r1": ["7007"]})


# ---------------------------------------------------------------------------
def box_07(form=None):
    s = seed()
    folder(s, "100", "Legal")
    if form != "absent":
        file(s, "8001", "Acme contract.pdf", "100", "DW", "DW", "LP", tags=["legal"], version=3, uploader="LP",
             modified="2026-09-20T10:00:00+00:00")                                                        # target
    file(s, "8002", "Globex contract.pdf", "100", "DW", "LP", "DW", tags=["legal"], version=4, uploader="DW",
         modified="2026-09-10T10:00:00+00:00")
    file(s, "8003", "Initech contract.pdf", "100", "DW", "DW", "LP", tags=["finance"], version=3, uploader="LP",
         modified="2026-09-12T10:00:00+00:00")
    file(s, "8004", "Umbrella contract.pdf", "100", "DW", "DW", "LP", tags=["legal"], version=2, uploader="LP",
         modified="2026-09-15T10:00:00+00:00")
    file(s, "8005", "Stark contract.pdf", "100", "DW", "DW", "LP", tags=["legal"], version=5, uploader="LP",
         modified="2026-08-28T10:00:00+00:00")
    file(s, "8006", "Contract checklist.docx", "100", "DW", tags=["legal"], version=1)
    base = [f("f_name", "name", "contains_ci", "contract"), f("f_tags", "tags", "json_has", "legal", "A:File.tags"),
            f("f_ver", "version_number", "ge", "3", "A:File.version_number"),
            f("f_from", "modified_at", "ge", "2026-09-01T00:00:00+00:00", "A:File.modified_at"),
            f("f_to", "modified_at", "lt", "2026-10-01T00:00:00+00:00")]
    query = q(FILES, base + [f("f_up", "uploader_display_name", "eq", "Leo Park", "A:File.uploader_display_name")])
    by_creator = q(FILES, base, [e("e_cr", "created_by_id", "id", user_is("x", "Leo Park"))])
    claims = [
        claim("A:File.uploader_display_name", "8002", REPLACE(by_creator, "latest-version uploader replaced by file creator"),
              "Leo created Globex contract, but Dana uploaded its latest version.", alternative="File.created_by_id"),
        claim("A:File.tags", "8003", DROP("f_tags"), "Tagged finance, not legal."),
        claim("A:File.version_number", "8004", DROP("f_ver"), "Still on version 2."),
        claim("A:File.modified_at", "8005", DROP("f_from"), "Last modified in August."),
    ]
    return flip({
        "case_id": "BOX-07", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Add FINAL to the end of the name of the legal-tagged contract whose latest version Leo Park "
                  "uploaded - it's on version 3 or later and was last modified in September 2026.",
        "references": [ref("BOX-07.r1", "Resolve the contract to rename",
                           "The legal-tagged contract on version 3+ last modified in September 2026 whose latest version "
                           "Leo Park uploaded; only 8001.", "target", query, ["8001"], claims,
                           paths=[{"entities": ["box_files"], "relationships": []}],
                           identifying=["box_files.name", "box_files.tags", "box_files.version_number",
                                        "box_files.modified_at", "box_files.uploader_display_name"],
                           answer=["box_files.name"], written=["box_files.name"], effect={"table": "box_files", "changes": ["update"]})],
        "probes": [("GET", "/folders/100/items", None), ("GET", "/files/8002", None)],
    }, "present", form, {"BOX-07.r1": []})


# ---------------------------------------------------------------------------
def box_08(form=None):
    s = seed()
    folder(s, "100", "Pricing")
    if form != "absent":
        file(s, "9001", "Enterprise pricing.xlsx", "100", "DW")      # target
        task(s, "9101", "9001", "DW", "Review discount tiers", due="2026-09-25T17:00:00+00:00")
        assign(s, "9201", "9101", "9001", "OH", "DW")
        assign(s, "9202", "9101", "9001", "SR", "DW")
    file(s, "9002", "SMB pricing.xlsx", "100", "DW")                 # split across two tasks
    task(s, "9102", "9002", "DW", "Review SMB tiers", due="2026-09-20T17:00:00+00:00")
    assign(s, "9203", "9102", "9002", "OH", "DW")
    task(s, "9103", "9002", "DW", "Review SMB promo", done=True, due="2026-09-01T17:00:00+00:00")
    assign(s, "9204", "9103", "9002", "OH", "DW", state="completed")
    assign(s, "9205", "9103", "9002", "SR", "DW", state="completed")
    file(s, "9003", "Partner pricing.xlsx", "100", "DW")             # completed task
    task(s, "9104", "9003", "DW", "Review partner margins", done=True, due="2026-09-20T17:00:00+00:00")
    assign(s, "9206", "9104", "9003", "OH", "DW", state="completed")
    assign(s, "9207", "9104", "9003", "SR", "DW", state="completed")
    file(s, "9004", "Education pricing.xlsx", "100", "DW")           # due later
    task(s, "9105", "9004", "DW", "Review education discounts", due="2026-10-15T17:00:00+00:00")
    assign(s, "9208", "9105", "9004", "OH", "DW")
    assign(s, "9209", "9105", "9004", "SR", "DW")
    file(s, "9005", "Nonprofit pricing.xlsx", "100", "DW")           # one assignee
    task(s, "9106", "9005", "DW", "Review nonprofit tiers", due="2026-09-20T17:00:00+00:00")
    assign(s, "9210", "9106", "9005", "OH", "DW")
    file(s, "9006", "Government pricing.xlsx", "100", "DW")          # Dana created, Sam assigned
    task(s, "9107", "9006", "DW", "Review government tiers", due="2026-09-20T17:00:00+00:00")
    assign(s, "9211", "9107", "9006", "OH", "SR")
    assign(s, "9212", "9107", "9006", "LP", "SR")
    asg = n("box_task_assignments", [], [e("e_by", "assigned_by_id", "id", user_is("f_by", "Dana Whitfield"),
                                           "R:TaskAssignment.assigned_by_id")])
    task_node = n("box_tasks", [f("f_open", "is_completed", "eq", False, "A:Task.is_completed"),
                                f("f_due", "due_at", "lt", "2026-10-01T00:00:00+00:00", "A:Task.due_at"),
                                f("f_action", "action", "eq", "review")],
                  [e("e_asg", "id", "task_id", asg, "D:Task.assignment_count", count={"op": "ge", "value": 2})])
    query = q(FILES, [], [e("e_task", "id", "item_id", task_node, "B:Task.item_id")])

    def variant(count=2, creator_alt=False):
        inner = n("box_task_assignments") if creator_alt else asg
        t = n("box_tasks", [f("f_open", "is_completed", "eq", False), f("f_due", "due_at", "lt", "2026-10-01T00:00:00+00:00"),
                            f("f_action", "action", "eq", "review")],
              ([e("e_cr", "created_by_id", "id", user_is("x", "Dana Whitfield"))] if creator_alt else [])
              + [e("e_asg", "id", "task_id", inner, count={"op": "ge", "value": count})])
        return q(FILES, [], [e("e_task", "id", "item_id", t)])
    claims = [
        claim("B:Task.item_id", "9002", SPLIT("e_task", ["f_open", "f_due", "f_action"], ["e_asg"]),
              "One open task due Sept 20 with one assignee; the two-assignee task is completed."),
        claim("A:Task.is_completed", "9003", DROP("f_open"), "Its task is already completed."),
        claim("A:Task.due_at", "9004", DROP("f_due"), "Due October 15."),
        claim("D:Task.assignment_count", "9005", REPLACE(variant(count=1), "two or more assignees replaced by at least one"),
              "Only one assignee."),
        claim("R:TaskAssignment.assigned_by_id", "9006", REPLACE(variant(creator_alt=True), "assigner replaced by task creator"),
              "Dana created the task, but Sam made both assignments.", alternative="Task.created_by_id"),
    ]
    return flip({
        "case_id": "BOX-08", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Add the tag escalate to the file that has an open review task, due before October 1, 2026, "
                  "which Dana Whitfield assigned to two or more people.",
        "references": [ref("BOX-08.r1", "Resolve the file to escalate",
                           "The file with one open review task due before October 1, 2026 that Dana assigned to at least "
                           "two people; only 9001.", "target", query, ["9001"], claims,
                           paths=[{"entities": ["box_files", "box_tasks", "box_task_assignments", "box_users"],
                                   "relationships": ["box_tasks.item_id", "box_task_assignments.task_id",
                                                     "box_task_assignments.assigned_by_id"]}],
                           identifying=["box_tasks.item_id", "box_tasks.is_completed", "box_tasks.due_at",
                                        "box_tasks.action", "box_task_assignments.task_id",
                                        "box_task_assignments.assigned_by_id", "box_users.name"],
                           written=["box_files.tags"], effect={"table": "box_files", "changes": ["update"]})],
        "probes": [("GET", "/files/9002/tasks", None), ("GET", "/files/9006/tasks", None)],
    }, "present", form, {"BOX-08.r1": []})


BASE = [box_01, box_02, box_03, box_04, box_05, box_06, box_07, box_08]
FLIPS = [partial(box_01, form="absent"), partial(box_02, form="present"), partial(box_03, form="absent"),
         partial(box_04, form="present"), partial(box_05, form="absent"), partial(box_06, form="present"),
         partial(box_07, form="absent"), partial(box_08, form="absent")]
CASES = BASE + FLIPS


# ---------------------------------------------------------------------------
# Round 4: W08 pattern, target present. The near-miss matches on the surface (it sits in the named folder);
# the target needs two reads (the folder's owner, then each PDF's creator).
def box_09(form=None):
    s = seed()
    folder(s, "100", "Finance Reports", owner="MC", creator="LP")
    folder(s, "200", "Planning")
    if form != "absent":
        file(s, "9901", "Budget model.pdf", "200", "DW", "MC", "DW")                  # target: created by Maya
    file(s, "9902", "Q3 summary.pdf", "100", "DW", "DW", "DW")                        # in the folder, by Dana
    file(s, "9903", "Headcount forecast.pdf", "200", "LP", "LP", "LP")                # by the folder's creator
    file(s, "9904", "Vendor list.pdf", "200", "MC", "DW", "DW")                       # owned (not created) by Maya
    file(s, "9905", "Travel policy.docx", "200", "DW", "MC", "DW")                    # Maya created, not a PDF
    owner = e("e_fo", "owned_by_id", "id", n("box_users"), "R:Folder.owned_by_id")
    fr = n(FOLDERS, [f("f_fr", "name", "eq", "Finance Reports")], [owner])
    # creator of the file = owner of Finance Reports (same user): express as a join through the users table
    query = q(FILES, [f("f_ext", "extension", "eq", "pdf")], [
        e("e_cr", "created_by_id", "id", n("box_users", [], [
            e("e_owns", "id", "owned_by_id", n(FOLDERS, [f("f_fr", "name", "eq", "Finance Reports")]))]),
          "R:File.created_by_id")])
    in_folder = q(FILES, [f("f_ext", "extension", "eq", "pdf")], [
        e("e_cr", "parent_id", "id", n(FOLDERS, [f("f_fr", "name", "eq", "Finance Reports")]))])
    folder_creator = q(FILES, [f("f_ext", "extension", "eq", "pdf")], [
        e("e_cr", "created_by_id", "id", n("box_users", [], [
            e("e_owns", "id", "created_by_id", n(FOLDERS, [f("f_fr", "name", "eq", "Finance Reports")]))]))])
    claims = [
        claim("R:File.created_by_id", "9902", REPLACE(in_folder, "created by the folder's owner replaced by located in the folder"),
              "Q3 summary.pdf sits in Finance Reports but Dana created it.", alternative="File.parent_id (location)"),
        claim("R:Folder.owned_by_id", "9903", REPLACE(folder_creator, "folder owner replaced by folder creator"),
              "Leo created Finance Reports; Maya owns it.", alternative="Folder.created_by_id"),
        claim("R:File.owned_by_id", "9904", SUB("e_cr", e("e_cr", "owned_by_id", "id", n("box_users", [], [
            e("e_owns", "id", "owned_by_id", n(FOLDERS, [f("f_fr", "name", "eq", "Finance Reports")]))]))),
              "Maya owns Vendor list.pdf; Dana created it.", alternative="File.owned_by_id"),
        claim("A:File.extension", "9905", DROP("f_ext"), "Maya created it, but it is a document."),
    ]
    return flip({
        "case_id": "BOX-09", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Add the tag owner-draft to the PDF that the owner of the Finance Reports folder created.",
        "references": [ref("BOX-09.r1", "Resolve the PDF", "The PDF whose creator is the owner of the Finance "
                           "Reports folder (Maya Chen); only 9901.", "target", query, ["9901"], claims,
                           paths=[{"entities": ["box_files", "box_users", "box_folders"],
                                   "relationships": ["box_files.created_by_id", "box_folders.owned_by_id"]}],
                           identifying=["box_files.extension", "box_files.created_by_id", "box_folders.owned_by_id",
                                        "box_folders.name"], written=["box_files.tags"],
                           effect={"table": "box_files", "changes": ["update"]})],
        "probes": [("GET", "/folders/100", None), ("GET", "/folders/200/items", None)],
    }, "present", form, {"BOX-09.r1": []})


CASES += [box_09, partial(box_09, form="absent")]


def box_10(form=None):
    """W08 pattern: the near-miss comment is by the file's owner / the folder's creator; the request's person is
    the folder's owner (two reads: folder owner, then comment authors)."""
    s = seed()
    folder(s, "100", "Vendor Contracts", owner="MC", creator="DW")
    file(s, "3100", "Acme vendor contract.pdf", "100", "LP", "LP", "LP")
    if form != "absent":
        comment(s, "3201", "3100", "MC", "Please confirm the renewal notice period.")        # target: folder owner
    comment(s, "3202", "3100", "LP", "I uploaded the signed copy.")                           # file owner
    comment(s, "3203", "3100", "DW", "Legal wants a second look at clause 9.")                # folder creator
    comment(s, "3204", "3100", "OH", "Maya asked me to check the indemnity cap.")             # mentions Maya
    owner_of_folder = n("box_users", [], [e("e_own", "id", "owned_by_id", n(FOLDERS, [f("f_fn", "name", "eq", "Vendor Contracts")]))])
    query = q("box_comments", [], [
        e("e_author", "created_by_id", "id", owner_of_folder, "R:Comment.created_by_id"),
        e("e_file", "file_id", "id", n(FILES, [f("f_file", "name", "contains_ci", "Acme vendor contract")]))])

    def alt(author_edge):
        return q("box_comments", [], [author_edge, e("e_file", "file_id", "id", n(FILES, [f("f_file", "name", "contains_ci", "Acme")]))])
    file_owner = e("e_author", "created_by_id", "id", n("box_users", [], [
        e("e_fo", "id", "owned_by_id", n(FILES, [f("x", "name", "contains_ci", "Acme vendor contract")]))]))
    folder_creator = e("e_author", "created_by_id", "id", n("box_users", [], [
        e("e_fc", "id", "created_by_id", n(FOLDERS, [f("y", "name", "eq", "Vendor Contracts")]))]))
    claims = [
        claim("R:File.owned_by_id", "3202", REPLACE(alt(file_owner), "folder owner replaced by the file's owner"),
              "Leo owns the contract file, not the folder.", alternative="owner of the file instead of the folder"),
        claim("R:Folder.created_by_id", "3203", REPLACE(alt(folder_creator), "folder owner replaced by folder creator"),
              "Dana created the folder; Maya owns it.", alternative="Folder.created_by_id"),
    ]
    return flip({
        "case_id": "BOX-10", "domain": "box", "form": "present", "variant_of": "arrangement:W08",  "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Reply \"Noted, thanks.\" to the comment that the owner of the Vendor Contracts folder left on the "
                  "Acme vendor contract.",
        "references": [ref("BOX-10.r1", "Resolve the comment", "The comment on the Acme contract written by the owner of "
                           "the Vendor Contracts folder (Maya Chen); only 3201.", "target", query, ["3201"], claims,
                           paths=[{"entities": ["box_comments", "box_users", "box_folders"],
                                   "relationships": ["box_comments.created_by_id", "box_folders.owned_by_id"]}],
                           identifying=["box_comments.created_by_id", "box_folders.owned_by_id", "box_folders.name",
                                        "box_comments.file_id", "box_files.name"], written=["box_comments.item_id"],
                           effect={"table": "box_comments", "changes": ["insert"], "field": "item_id", "all": True})],
        "probes": [("GET", "/folders/100", None), ("GET", "/files/3100/comments", None)],
    }, "present", form, {"BOX-10.r1": []})


CASES += [box_10]


def box_11(form=None):
    """Reply direction: 'the comment Omar replied to' vs Omar's reply itself."""
    s = seed()
    folder(s, "100", "Vendor Contracts")
    file(s, "3100", "Acme vendor contract.pdf", "100", "DW")
    if form != "absent":
        comment(s, "3301", "3100", "PN", "Is the renewal notice 60 or 90 days?", created="2026-06-10T15:00:00+00:00")  # target
        comment(s, "3302", "3100", "OH", "It's 90 days, see clause 12.", reply_to="3301", created="2026-06-10T16:00:00+00:00")
    else:
        comment(s, "3302", "3100", "OH", "Clause 12 sets a 90-day notice period.", created="2026-06-10T16:00:00+00:00")
    comment(s, "3303", "3100", "PN", "Thanks Omar, that settles it.", reply_to="3302", created="2026-06-10T17:00:00+00:00")
    comment(s, "3304", "3100", "DW", "Uploading the countersigned copy tomorrow.", created="2026-06-11T09:00:00+00:00")
    query = q("box_comments", [], [e("e_reply", "id", "item_id", n("box_comments", [], [
        e("e_ra", "created_by_id", "id", user_is("f_ra", "Omar Haddad"))]), "H:Comment.item_id:comment")])
    replied_by = q("box_comments", [], [e("e_reply", "item_id", "id", n("box_comments", [], [
        e("e_ra", "created_by_id", "id", user_is("f_ra", "Omar Haddad"))]))])
    claims = [claim("H:Comment.item_id:comment", "3303", REPLACE(replied_by, "comment Omar replied to replaced by the reply to Omar"),
                    "Priya's comment replies to Omar; Omar did not reply to it.", alternative="reply to Omar (reversed)")]
    return flip({
        "case_id": "BOX-11", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "variant_of": "arrangement:direction", "seed": s,
        "prompt": "On the Acme vendor contract, delete the comment that Omar Haddad replied to.",
        "references": [ref("BOX-11.r1", "Resolve the comment", "The comment whose reply was written by Omar Haddad.",
                           "target", query, ["3301"], claims,
                           paths=[{"entities": ["box_comments", "box_comments", "box_users"],
                                   "relationships": ["box_comments.item_id", "box_comments.created_by_id"]}],
                           identifying=["box_comments.item_id", "box_comments.created_by_id", "box_users.name"],
                           effect={"table": "box_comments", "changes": ["delete", "update"]})],
        "probes": [("GET", "/files/3100/comments", None), ("GET", "/comments/3303", None)],
    }, "present", form, {"BOX-11.r1": []})


CASES += [box_11, partial(box_11, form="absent")]
