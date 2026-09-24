"""Shared case assembly for the FDC pilot (manual research cases).

A case holds the solver-visible request and seed, plus private references:
each reference has a reference query, its expected referent set, and credit
claims (requirement, near-miss witness, mutation). Cards and task specifications
are derived in the existing grounding-card schema for evaluator bundles.
"""
from __future__ import annotations

import copy

from grounding.runs.fact_coverage_01 import fdc


def f(key, field, op, value=None, fact=None):
    out = {"key": key, "field": field, "op": op}
    if value is not None or op not in {"is_null", "not_null"}:
        out["value"] = value
    if fact:
        out["fact"] = fact
    return out


def e(key, parent, child, node, fact=None, op="eq", closure=None, count=None, negate=False):
    edge = {"key": key, "join": {"parent": parent, "child": child, "op": op}, "node": node}
    if fact:
        edge["fact"] = fact
    if closure:
        edge["closure"] = closure
    if count:
        edge["count"] = count
    if negate:
        edge["negate"] = True
    return edge


def n(table, filters=(), edges=(), key=None):
    node = {"table": table, "filters": list(filters), "edges": list(edges)}
    if key:
        node["key"] = key
    return node


def q(table, filters=(), edges=(), key=("id",), **extra):
    query = n(table, filters, edges)
    query["key"] = list(key)
    query.update(extra)
    return query


def claim(requirement, witness, mutation, explanation, alternative=None):
    out = {"requirement": requirement, "witness": witness, "mutation": mutation, "explanation": explanation}
    if alternative:
        out["alternative"] = alternative
    return out


def DROP(target):
    return {"type": "DROP", "target": target}


def SUB(target, replacement):
    return {"type": "SUB", "target": target, "replacement": replacement}


def SPLIT(target, *groups):
    return {"type": "SPLIT", "target": target, "groups": [list(g) for g in groups]}


def REPLACE(query, note):
    return {"type": "REPLACE", "query": query, "note": note}


def ref(rid, name, description, use, query, expected, claims, *, paths, identifying, written=None,
        answer=None, resolution=None, scope="All records in the supplied environment visible to the actor.",
        effect=None, labels=None):
    out = {"id": rid, "name": name, "description": description, "use": use, "query": query,
           "expected": expected, "claims": claims, "resolution": resolution or ("resolved" if expected else "absent"),
           "scope": scope, "paths": paths, "identifying": identifying, "written": written or [],
           "answer": answer or []}
    if effect:
        out["effect"] = effect   # {"table", "changes", "field"}: where acting on a candidate shows in the diff
    if labels:
        out["labels"] = labels   # candidate handle -> distinctive text, for read-only answers
    return out


def cards_for(case):
    cards = []
    total = len(case["references"])
    for r in case["references"]:
        card = {
            "Test ID": case["case_id"],
            "Task type": "read-only" if r["use"] == "evidence" else "state-changing",
            "Grounding obligations": total,
            "Grounding obligation name": r["name"],
            "Grounding obligation description": r["description"],
            "Resolution": r["resolution"],
            "Shared scope": r["scope"],
            "Referent set": r["expected"],
            "Identifying paths": r["paths"],
            "Alternative sufficient identifying sets": [r["identifying"]],
        }
        if r["use"] == "evidence":
            card["Answer-computation attributes"] = [r["answer"]]
        else:
            card["Change-computation attributes"] = [r["answer"]] if r["answer"] else [[]]
            card["Written attributes"] = r["written"]
        cards.append(card)
    return cards


def finish(case):
    """Attach cards/specs and check every reference mechanically."""
    case = copy.deepcopy(case)
    case["cards"] = cards_for(case)
    case["task_spec"] = case.get("task_spec") or [
        {"line": 1, "text": case["prompt"], "obligations": list(range(1, len(case["references"]) + 1))}]
    check_seed = copy.deepcopy(case["seed"])
    for table, rows in case.get("derived_rows", {}).items():
        check_seed[table] = rows
    results, errors = [], []
    for r in case["references"]:
        result, errs = fdc.check_reference(check_seed, r)
        results.append(result)
        errors += errs
    return case, results, errors
