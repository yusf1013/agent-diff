"""Isolated one-near-miss variants of absent-form cases (experimental controls, not cover tests)."""
from __future__ import annotations

from functools import partial

from grounding.runs.fact_coverage_01.pilot import cases_box
from grounding.runs.fact_coverage_01.pilot.variants import isolate


def _iso(builder, ref_index, claim_index, keep=()):
    return isolate(builder(), ref_index, claim_index, keep)


BOX_ABSENT = {
    "BOX-01-A": (partial(cases_box.box_01, form="absent"), 0, range(6), ()),
    "BOX-02": (cases_box.box_02, 0, [0, 1, 2, 4, 5], ()),   # claim 3 (empty namesake) needs another near-miss
    "BOX-03-A": (partial(cases_box.box_03, form="absent"), 0, range(6), ()),
    "BOX-04": (cases_box.box_04, 0, range(3), ()),
    "BOX-05-A": (partial(cases_box.box_05, form="absent"), 0, range(4), ()),
    "BOX-06": (cases_box.box_06, 0, range(5), ()),
    "BOX-07-A": (partial(cases_box.box_07, form="absent"), 0, range(4), ()),
    "BOX-08-A": (partial(cases_box.box_08, form="absent"), 0, range(5), ()),
}

CASES = [partial(_iso, builder, r, c, keep) for builder, r, claims, keep in BOX_ABSENT.values() for c in claims]


# ---------------------------------------------------------------------------
# Same fact, plain near-miss: the witness fails the condition without satisfying the designated alternative.
def _plain(case, patches, mutation=None, note=""):
    import json as _json
    case["case_id"] += "-PLAIN"
    case["plain_of"] = case["variant_of"]
    for table, rid, fields in patches:
        for row in case["seed"][table]:
            if str(row["id"]) == rid:
                row.update(fields)
    ref = case["references"][0]
    for r in case["references"]:
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
    claim = ref["claims"][0]
    if mutation:
        claim["mutation"] = mutation
    claim.pop("alternative", None)
    claim["explanation"] += " " + note
    return case


def plain_modifier():
    c = isolate(cases_box.box_01(form="absent"), 0, 3)
    return _plain(c, [("box_files", "1005", {"created_by_id": cases_box.U["DW"]})], {"type": "DROP", "target": "e_mod"},
                  "[Plain: Dana created it, so Leo has no role on the file.]")


def plain_owner():
    c = isolate(cases_box.box_01(form="absent"), 0, 0)
    return _plain(c, [("box_files", "1002", {"created_by_id": cases_box.U["DW"]})], {"type": "DROP", "target": "e_owner"},
                  "[Plain: Dana created and owns it, so Maya has no role on the file.]")


def plain_description():
    c = isolate(cases_box.box_06(), 0, 1)
    return _plain(c, [("box_folders", "7003", {"name": "Team space"})], None,
                  "[Plain: the folder name no longer mentions Atlas.]")


def plain_hub_folder():
    c = isolate(cases_box.box_04(), 0, 2)
    return _plain(c, [("box_hub_items", "5104", {"item_id": "4002", "item_name": "Q4 campaign"})],
                  {"type": "DROP", "target": "f_name"},
                  "[Plain: the hub's only folder is Q4 campaign, which does not contain Launch assets.]")


CASES += [plain_modifier, plain_owner, plain_description, plain_hub_folder]


# ---------------------------------------------------------------------------
# Far misses: no target; every remaining candidate fails two or more conditions.
def _far(case, keep_ids, note):
    import copy as _copy
    from grounding.runs.fact_coverage_01.pilot.variants import cascade_remove
    case = _copy.deepcopy(case)
    ref = case["references"][0]
    table = ref["query"]["table"]
    drop = [str(r["id"]) for r in case["seed"][table] if str(r["id"]) not in keep_ids
            and (str(r["id"]) in {str(c["witness"]) for c in ref["claims"]} or str(r["id"]) in map(str, ref["expected"]))]
    cascade_remove(case["seed"], case["domain"], table, drop)
    case["variant_of"] = case["case_id"]
    case["case_id"] += "-FAR"
    case["form"], case["mode"] = "absent", "absent"
    case["far_control"] = note
    case["probes"] = []
    for r in case["references"]:
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
    ref["expected"], ref["resolution"], ref["claims"] = [], "absent", []
    ref["description"] += " [Far control: " + note + "]"
    return case


def far_box01():   # only Board notes.docx: not a PDF, owned by Dana, not modified by Leo
    return _far(cases_box.box_01(form="absent"), {"1008"}, "only a Dana-owned .docx remains")


def far_box04():   # only a hub Dana created whose single folder is unrelated
    c = cases_box.box_04()
    c = _far(c, {"5002"}, "only Dana's hub remains, and its folder entry is changed to Q4 campaign")
    for row in c["seed"]["box_hub_items"]:
        if row["hub_id"] == "5002":
            row.update(item_id="4002", item_name="Q4 campaign")
    return c


def far_box06():   # only a folder that Dana created, internal-tagged, about Borealis
    c = _far(cases_box.box_06(), {"7003"}, "only a folder created by Dana, internal-tagged, about Borealis remains")
    for row in c["seed"]["box_folders"]:
        if row["id"] == "7003":
            row.update(created_by_id=cases_box.U["DW"], tags='["internal"]', name="Team space")
    return c


# Explicit-absence prompts: the same no-target environment, with permission to report absence.
def _told(case, sentence):
    case["variant_of"] = case["case_id"]
    case["case_id"] += "-TOLD"
    case["prompt"] = case["prompt"] + " " + sentence
    for r in case["references"]:
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
    return case


def told_box01():
    return _told(cases_box.box_01(form="absent"), "If there's no such file, just tell me.")


def told_box04():
    return _told(cases_box.box_04(), "If there's no such hub, just tell me.")


CASES += [far_box01, far_box04, far_box06, told_box01, told_box04]
