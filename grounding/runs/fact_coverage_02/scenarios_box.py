"""New Box scenarios for facts the pilot never tested (manual design). Each has its target; probes are derived.

Every claim carries its substitute family (method.md). Seeds reuse the pilot's Box helpers and people.
"""
from __future__ import annotations

from grounding.runs.fact_coverage_01.pilot.cases_box import (ACTOR, FILES, FOLDERS, HUB_FLAGS, T0, U, comment, file,
                                                             folder, seed, user_is)
from grounding.runs.fact_coverage_01.pilot.common import DROP, REPLACE, SUB, claim, e, f, n, q, ref

FAVORITES = "9101"


def fam(c, family):
    c["family"] = family
    return c


def favorites_is():
    return n("box_collections", [f("f_cname", "name", "eq", "Favorites")])


# ---------------------------------------------------------------------------
def box_21():
    """Folder in Favorites (itself), last modifier, creation month, number of files."""
    s = seed()
    s["box_collections"] += [{"id": FAVORITES, "type": "collection", "name": "Favorites", "collection_type": "favorites"}]
    aug = "2026-08-{:02d}T15:00:00+00:00"
    folder(s, "7100", "Compliance", owner="JL", modifier="DW", collections=[FAVORITES], created="2026-07-01T15:00:00+00:00")
    folder(s, "7101", "Audit binder", owner="JL", modifier="LP", collections=[FAVORITES], created=aug.format(20))  # target
    folder(s, "7102", "Audit prep", parent="7100", owner="JL", modifier="LP", created=aug.format(12))  # inside a favorite
    folder(s, "7103", "Audit notes", owner="JL", creator="LP", modifier="MC", collections=[FAVORITES], created=aug.format(5))
    folder(s, "7104", "Audit archive", owner="JL", modifier="LP", collections=[FAVORITES], created="2026-09-01T15:00:00+00:00")
    folder(s, "7105", "Audit evidence", owner="JL", modifier="LP", collections=[FAVORITES], created=aug.format(25))
    folder(s, "7106", "Audit templates", owner="JL", modifier="LP", collections=[FAVORITES], created="2026-03-10T15:00:00+00:00")
    counts = {"7100": 1, "7101": 2, "7102": 2, "7103": 2, "7104": 2, "7105": 3, "7106": 2}
    for fid, k in counts.items():
        for i in range(k):
            file(s, f"{fid[1:]}{i}", f"Evidence {fid}-{i + 1}.pdf", fid, "JL")
    query = q(FOLDERS, [f("f_created", "created_at", "contains_ci", "2026-08-", "A:Folder.created_at")], [
        e("e_coll", "collections", "id", favorites_is(), "R:Folder.collections", op="json_contains"),
        e("e_mod", "modified_by_id", "id", user_is("f_mod", "Leo Park"), "R:Folder.modified_by_id"),
        e("e_files", "id", "parent_id", n(FILES), "D:Folder.item_count", count={"op": "eq", "value": 2}),
    ])
    no_count = q(FOLDERS, [f("f_created", "created_at", "contains_ci", "2026-08-")], [
        e("e_coll", "collections", "id", favorites_is(), op="json_contains"),
        e("e_mod", "modified_by_id", "id", user_is("f_mod", "Leo Park"))])
    inside_favorite = e("e_coll", "parent_id", "id", n(FOLDERS, [], [
        e("e_pc", "collections", "id", n("box_collections", [f("x", "name", "eq", "Favorites")]), op="json_contains")]))
    claims = [
        fam(claim("R:Folder.collections", "7102", SUB("e_coll", inside_favorite),
                  "Audit prep is inside Compliance, which is in Favorites; the folder itself is not.",
                  alternative="folder inside a favorited folder"), "F2"),
        fam(claim("R:Folder.modified_by_id", "7103",
                  SUB("e_mod", e("e_mod", "created_by_id", "id", user_is("x", "Leo Park"))),
                  "Leo created Audit notes; Maya modified it last.", alternative="Folder.created_by_id"), "F1"),
        fam(claim("A:Folder.created_at", "7104", DROP("f_created"), "Created on September 1, the day after August.",
                  alternative="nearest date outside the month"), "F7"),
        fam(claim("D:Folder.item_count", "7105", REPLACE(no_count, "file count condition dropped"),
                  "Holds three files, one more than asked.",
                  alternative="nearest count"), "F7"),
        fam(claim("A:Folder.created_at", "7106", DROP("f_created"), "Created in March."), "F0"),
    ]
    return {
        "case_id": "BOX-21", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "In my Favorites, add the tag audit-ready to the folder Leo Park last modified that was created in "
                  "August 2026 and holds exactly two files.",
        "references": [ref("BOX-21.r1", "Resolve the folder to tag",
                           "The folder itself in Favorites, last modified by Leo Park, created in August 2026, holding "
                           "exactly two files; only 7101.", "target", query, ["7101"], claims,
                           paths=[{"entities": ["box_folders", "box_collections"], "relationships": ["box_folders.collections"]},
                                  {"entities": ["box_folders", "box_users"], "relationships": ["box_folders.modified_by_id"]},
                                  {"entities": ["box_folders", "box_files"], "relationships": ["box_files.parent_id"]}],
                           identifying=["box_folders.collections", "box_folders.modified_by_id", "box_folders.created_at",
                                        "box_files.parent_id"],
                           written=["box_folders.tags"], effect={"table": "box_folders", "changes": ["update"]})],
        "probes": [("GET", f"/collections/{FAVORITES}/items", None), ("GET", "/folders/7102", None),
                   ("GET", "/folders/7105/items", None), ("GET", "/folders/7104", None)],
    }


# ---------------------------------------------------------------------------
def box_22():
    """Hub last updater, and a hub including the file itself."""
    s = seed()
    folder(s, "8000", "Sales")
    file(s, "8010", "Pricing sheet.xlsx", "8000", "JL")
    file(s, "8011", "Pricing sheet 2025.xlsx", "8000", "JL")
    file(s, "8012", "Discount policy.pdf", "8000", "JL")

    def hub(hid, title, creator, updater):
        s["box_hubs"].append({"id": hid, "type": "hubs", "title": title, "description": f"{title} materials",
                              "created_by_id": U[creator], "updated_by_id": U[updater], "created_at": T0,
                              "updated_at": T0, **HUB_FLAGS})

    def item(iid, hid, target, kind, name):
        s["box_hub_items"].append({"id": iid, "type": "hub_item", "added_at": T0, "added_by_id": U["JL"], "hub_id": hid,
                                   "item_id": target, "item_type": kind, "item_name": name, "position": 1})

    hub("5201", "Sales kit", "LP", "DW")        # target
    item("5301", "5201", "8010", "file", "Pricing sheet.xlsx")
    hub("5202", "Deal desk", "DW", "LP")        # Dana created it; Leo updated it last
    item("5302", "5202", "8010", "file", "Pricing sheet.xlsx")
    hub("5203", "Sales hub", "LP", "DW")        # includes the folder that contains the file
    item("5303", "5203", "8000", "folder", "Sales")
    hub("5204", "Renewals", "LP", "DW")         # includes a similarly named file
    item("5304", "5204", "8011", "file", "Pricing sheet 2025.xlsx")
    items = n("box_hub_items", [f("f_type", "item_type", "eq", "file")], [
        e("e_file", "item_id", "id", n(FILES, [f("f_fname", "name", "eq", "Pricing sheet.xlsx", "A:File.name")]))])
    hub_query = q("box_hubs", [], [
        e("e_upd", "updated_by_id", "id", user_is("f_upd", "Dana Whitfield"), "R:Hub.updated_by_id"),
        e("e_item", "id", "hub_id", items, "R:HubItem.file"),
    ])
    folder_items = n("box_hub_items", [f("f_type", "item_type", "eq", "folder")], [
        e("e_hf", "item_id", "id", n(FOLDERS, [], [
            e("e_in", "id", "parent_id", n(FILES, [f("x", "name", "eq", "Pricing sheet.xlsx")]))]))])
    claims = [
        fam(claim("R:Hub.updated_by_id", "5202",
                  SUB("e_upd", e("e_upd", "created_by_id", "id", user_is("x", "Dana Whitfield"))),
                  "Dana created Deal desk; Leo updated it last.", alternative="Hub.created_by_id"), "F1"),
        fam(claim("R:HubItem.file", "5203", REPLACE(q("box_hubs", [], [
                      e("e_upd", "updated_by_id", "id", user_is("f_upd", "Dana Whitfield")),
                      e("e_item", "id", "hub_id", folder_items)]), "file entry replaced by the folder that contains it"),
                  "Sales hub includes the Sales folder, which contains Pricing sheet.xlsx; not the file itself.",
                  alternative="folder containing the file"), "F2"),
        fam(claim("A:File.name", "5204", DROP("f_fname"), "Renewals includes Pricing sheet 2025.xlsx.",
                  alternative="similarly named file"), "F8"),
    ]
    file_query = q(FILES, [f("f_add", "name", "eq", "Discount policy.pdf")])
    return {
        "case_id": "BOX-22", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Add the Discount policy file to the hub Dana Whitfield last updated that already includes the "
                  "Pricing sheet file.",
        "references": [
            ref("BOX-22.r1", "Resolve the destination hub",
                "The hub whose last updater is Dana Whitfield and that lists the file Pricing sheet.xlsx itself; only 5201.",
                "target", hub_query, ["5201"], claims,
                paths=[{"entities": ["box_hubs", "box_users"], "relationships": ["box_hubs.updated_by_id"]},
                       {"entities": ["box_hubs", "box_hub_items", "box_files"], "relationships": ["box_hub_items.hub_id"]}],
                identifying=["box_hubs.updated_by_id", "box_hub_items.item_type", "box_files.name"],
                written=["box_hub_items"], effect={"table": "box_hub_items", "changes": ["insert"], "field": "hub_id"}),
            ref("BOX-22.r2", "Resolve the file to add", "The Discount policy file; only 8012.", "input", file_query,
                ["8012"], [], paths=[{"entities": ["box_files"], "relationships": []}], identifying=["box_files.name"]),
        ],
        "probes": [("GET", "/hubs", None, {"box-version": "2025.0"}),
                   ("GET", "/hub_items", {"hub_id": "5203"}, {"box-version": "2025.0"}),
                   ("GET", "/hub_items", {"hub_id": "5202"}, {"box-version": "2025.0"})],
    }


# ---------------------------------------------------------------------------
def box_23():
    """File description, size and number of comments."""
    s = seed()
    folder(s, "8100", "Contracts")
    specs = [  # id, name, description, size, comments
        ("8101", "Initech MSA.pdf", "Initech renewal terms for 2027", 3_400_000, 3),       # target
        ("8102", "Initech renewal.pdf", "Master terms, signed 2024", 3_100_000, 3),         # the name says it
        ("8103", "Initech SOW.pdf", "Initech renewal statement of work", 1_950_000, 3),     # just under 2 MB
        ("8104", "Initech NDA.pdf", "Initech renewal NDA", 2_600_000, 2),                   # one comment short
        ("8105", "Initech pricing.docx", "Initech renewal pricing", 2_900_000, 3),          # not a PDF
    ]
    for fid, name, desc, size, k in specs:
        file(s, fid, name, "8100", "JL", description=desc, size=size)
        for i in range(k):
            comment(s, f"{fid}{i}", fid, ["PN", "OH", "SR"][i], f"Reviewed section {i + 1}.")
    query = q(FILES, [f("f_ext", "extension", "eq", "pdf", "A:File.extension"),
                      f("f_desc", "description", "contains_ci", "initech renewal", "A:File.description"),
                      f("f_size", "size", "gt", 2_000_000, "A:File.size")], [
        e("e_comments", "id", "file_id", n("box_comments"), "D:File.comment_count", count={"op": "ge", "value": 3})])
    by_name = q(FILES, [f("f_ext", "extension", "eq", "pdf"), f("f_desc", "name", "contains_ci", "initech renewal"),
                        f("f_size", "size", "gt", 2_000_000)], [
        e("e_comments", "id", "file_id", n("box_comments"), count={"op": "ge", "value": 3})])
    claims = [
        fam(claim("A:File.description", "8102", REPLACE(by_name, "description replaced by name"),
                  "The name says Initech renewal; the description does not.", alternative="File.name"), "F1"),
        fam(claim("A:File.size", "8103", DROP("f_size"), "1.95 MB, just under 2 MB.",
                  alternative="nearest size below the threshold"), "F7"),
        fam(claim("D:File.comment_count", "8104", REPLACE(q(FILES, [f("f_ext", "extension", "eq", "pdf"),
                  f("f_desc", "description", "contains_ci", "initech renewal"), f("f_size", "size", "gt", 2_000_000)]),
                  "comment count condition dropped"), "Two comments, one short of three.",
                  alternative="nearest count"), "F7"),
        fam(claim("A:File.extension", "8105", DROP("f_ext"), "A Word document, not a PDF."), "F0"),
    ]
    return {
        "case_id": "BOX-23", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Add the tag renewal to the contract PDF whose description mentions the Initech renewal, that is "
                  "larger than 2 MB and has at least three comments.",
        "references": [ref("BOX-23.r1", "Resolve the contract to tag",
                           "The PDF whose description mentions the Initech renewal, larger than 2 MB, with at least "
                           "three comments; only 8101.", "target", query, ["8101"], claims,
                           paths=[{"entities": ["box_files"], "relationships": []},
                                  {"entities": ["box_files", "box_comments"], "relationships": ["box_comments.file_id"]}],
                           identifying=["box_files.extension", "box_files.description", "box_files.size",
                                        "box_files.comment_count"],
                           written=["box_files.tags"], effect={"table": "box_files", "changes": ["update"]})],
        "probes": [("GET", "/folders/8100/items", None), ("GET", "/files/8103", None),
                   ("GET", "/files/8104/comments", None), ("GET", "/files/8102", None)],
    }


# ---------------------------------------------------------------------------
def box_24():
    """Task creator's login, task creation day and task message."""
    s = seed()
    pat, patk = "30000000009", "30000000010"
    for uid, name, login in [(pat, "Pat Kim", "pat.kim@northwind.example"),
                             (patk, "Pat Kimura", "pat.kimura@northwind.example")]:
        s["box_users"].append({"id": uid, "type": "user", "name": name, "login": login, "status": "active",
                               "role": "user", "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"})
    folder(s, "8200", "Legal")
    file(s, "8201", "Acme MSA.pdf", "8200", "JL")
    file(s, "8202", "Indemnity clause review.pdf", "8200", "JL")
    file(s, "8203", "Globex MSA.pdf", "8200", "JL")

    def task(tid, file_id, creator, created, message):
        s["box_tasks"].append({"id": tid, "type": "task", "item_id": file_id, "item_type": "file", "message": message,
                               "action": "review", "is_completed": False, "completion_rule": "all_assignees",
                               "due_at": "2026-10-05T17:00:00+00:00", "created_by_id": creator, "created_at": created})

    task("8301", "8201", pat, "2026-09-14T16:00:00+00:00", "Please check the indemnity clause")    # target
    task("8302", "8203", patk, "2026-09-14T16:00:00+00:00", "Please check the indemnity clause")   # Pat Kimura
    task("8303", "8203", pat, "2026-09-15T16:00:00+00:00", "Please check the indemnity clause")    # next day
    task("8304", "8202", pat, "2026-09-14T16:00:00+00:00", "Please check the payment terms")       # file name only
    task("8305", "8201", pat, "2026-09-14T16:00:00+00:00", "Please approve the invoice")           # other message
    query = q("box_tasks", [f("f_msg", "message", "contains_ci", "indemnity", "A:Task.message"),
                            f("f_created", "created_at", "contains_ci", "2026-09-14", "A:Task.created_at")], [
        e("e_creator", "created_by_id", "id",
          n("box_users", [f("f_login", "login", "eq", "pat.kim@northwind.example", "A:User.login")]),
          "R:Task.created_by_id")])
    by_file = q("box_tasks", [f("f_created", "created_at", "contains_ci", "2026-09-14")], [
        e("e_creator", "created_by_id", "id", n("box_users", [f("f_login", "login", "eq", "pat.kim@northwind.example")])),
        e("e_file", "item_id", "id", n(FILES, [f("x", "name", "contains_ci", "indemnity")]))])
    claims = [
        fam(claim("A:User.login", "8302", DROP("f_login"), "Created by pat.kimura@, not pat.kim@.",
                  alternative="similar login"), "F8"),
        fam(claim("A:Task.created_at", "8303", DROP("f_created"), "Created on September 15, the next day.",
                  alternative="adjacent day"), "F7"),
        fam(claim("A:Task.message", "8304", REPLACE(by_file, "task message replaced by the file's name"),
                  "The file is the indemnity clause review; the task asks about payment terms.",
                  alternative="File.name of the task's file"), "F1"),
        fam(claim("A:Task.message", "8305", DROP("f_msg"), "Asks to approve the invoice."), "F0"),
    ]
    return {
        "case_id": "BOX-24", "domain": "box", "form": "present", "mode": "single", "acting_user_id": ACTOR, "seed": s,
        "prompt": "Move the due date to October 20, 2026 on the task pat.kim@northwind.example created on "
                  "September 14 asking to check the indemnity clause.",
        "references": [ref("BOX-24.r1", "Resolve the task",
                           "The task created by pat.kim@northwind.example on 2026-09-14 whose message asks to check the "
                           "indemnity clause; only 8301.", "target", query, ["8301"], claims,
                           paths=[{"entities": ["box_tasks", "box_users"], "relationships": ["box_tasks.created_by_id"]}],
                           identifying=["box_tasks.message", "box_tasks.created_at", "box_users.login"],
                           written=["box_tasks.due_at"], effect={"table": "box_tasks", "changes": ["update"]})],
        "probes": [("GET", "/files/8201/tasks", None), ("GET", "/files/8203/tasks", None),
                   ("GET", "/files/8202/tasks", None)],
    }


SCENARIOS = [box_21, box_22, box_23, box_24]
