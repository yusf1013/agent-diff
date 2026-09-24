"""Controlled variants of built cases: isolate one near-miss (no target, no other near-misses).

isolate(case, ref_index, claim_index, keep=()) removes the reference's expected
targets and every other claimed witness from the seed, cascading through foreign
keys (and the domain's interpreted references), while keeping `keep` rows that
give the retained witness its meaning. The request text is unchanged, so the only
candidate that resembles the request is the single near-miss.
"""
from __future__ import annotations

import copy
import json

from grounding.paths import REPO_ROOT

INTERPRETED = {  # interpreted references not declared as database foreign keys
    "box": [("box_comments", "item_id", "box_comments", "id"), ("box_hub_items", "item_id", "box_files", "id"),
            ("box_hub_items", "item_id", "box_folders", "id"), ("box_task_assignments", "item_id", "box_files", "id")],
    "calendar": [("calendar_events", "recurring_event_id", "calendar_events", "id")],
    "linear": [("issue_label_issue_association", "issue_id", "issues", "id"),
               ("issue_subscriber_user_association", "issue_id", "issues", "id")],
}


def foreign_keys(domain):
    if domain == "slack":
        return []
    inv = json.loads((REPO_ROOT / f"grounding/domains/{domain}/source_inventory.json").read_text())
    out = []
    for t in inv["tables"]:
        for c in t["columns"]:
            for fk in c["foreign_keys"]:
                target = fk if isinstance(fk, str) else fk.get("target", "")
                if "." in target:
                    ref_table, ref_col = target.split(".")[-2:]
                    out.append((t["table"], c["name"], ref_table, ref_col))
    return out + INTERPRETED.get(domain, [])


def cascade_remove(seed, domain, table, ids):
    """Remove rows of `table` with ids in `ids` and, transitively, rows referencing them."""
    fks = foreign_keys(domain)
    pending = [(table, set(map(str, ids)))]
    while pending:
        tbl, gone = pending.pop()
        if tbl not in seed:
            continue
        seed[tbl] = [r for r in seed[tbl] if str(r.get("id")) not in gone]
        for child, col, parent, pcol in fks:
            if parent != tbl or child not in seed:
                continue
            dead = [r for r in seed[child] if str(r.get(col)) in gone]
            if dead:
                if "id" in dead[0]:
                    pending.append((child, {str(r["id"]) for r in dead}))
                else:
                    seed[child] = [r for r in seed[child] if str(r.get(col)) not in gone]
    return seed


def isolate(case, ref_index, claim_index, keep=()):
    case = copy.deepcopy(case)
    ref = case["references"][ref_index]
    kept = ref["claims"][claim_index]
    table = ref["query"]["table"]
    drop = [str(x) for x in ref["expected"]] + [str(c["witness"]) for i, c in enumerate(ref["claims"]) if i != claim_index]
    drop = [d for d in drop if d not in set(map(str, keep))]
    if table in case["seed"]:
        cascade_remove(case["seed"], case["domain"], table, drop)
    derived = case.get("derived_rows", {}).get(table)
    if derived is not None:
        case["derived_rows"][table] = [r for r in derived if str(r["id"]) not in drop]
    gone = set(drop)
    case["probes"] = [p for p in case.get("probes", []) if not any(g in json.dumps(p) for g in gone)]
    suffix = f"-I{ref_index + 1}{claim_index + 1}"
    case["variant_of"] = case["case_id"]
    case["case_id"] += suffix
    case["form"], case["mode"] = "absent", "absent"
    case["isolated_requirement"] = kept["requirement"]
    for i, r in enumerate(case["references"]):
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
        if i == ref_index:
            r["expected"], r["resolution"] = [], "absent"
            r["claims"] = [kept]
            r["description"] += f" [Isolated: only the {kept['requirement']} near-miss remains; no target.]"
    return case


def absent_of(case, ref_index=0):
    """Remove one reference's targets (with dependents): the same request over a no-match environment."""
    case = copy.deepcopy(case)
    ref = case["references"][ref_index]
    table = ref["query"]["table"]
    gone = [str(x) for x in ref["expected"]]
    if table in case["seed"]:
        cascade_remove(case["seed"], case["domain"], table, gone)
    derived = case.get("derived_rows", {}).get(table)
    if derived is not None:
        case["derived_rows"][table] = [r for r in derived if str(r["id"]) not in gone]
    case["probes"] = [p for p in case.get("probes", []) if not any(g in json.dumps(p) for g in gone)]
    case["variant_of"] = case["case_id"]
    case["case_id"] += "-A"
    case["form"], case["mode"] = "absent", "absent"
    for i, r in enumerate(case["references"]):
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
        if i == ref_index:
            r["expected"], r["resolution"] = [], "absent"
            r["description"] += " [Target removed: no match.]"
    return case


def present_of(case, table, rows, expected, ref_index=0):
    """Add target rows to an absent-form case (same request)."""
    case = copy.deepcopy(case)
    for t, row in rows:
        case["seed"].setdefault(t, []).append(row)
    case["variant_of"] = case["case_id"]
    case["case_id"] += "-P"
    case["form"], case["mode"] = "present", "single"
    for i, r in enumerate(case["references"]):
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
        if i == ref_index:
            r["expected"], r["resolution"] = expected, "resolved"
            r["description"] += " [Target added.]"
    return case
