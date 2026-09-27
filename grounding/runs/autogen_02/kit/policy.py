"""Per-fact policy variants of a built scenario case (decisions N10 and D4 in ../decisions.md, and fact_coverage_02).

- **Absence twin.** One per fact: the fact's probe (its single near miss) or fact probe (all its near misses), with no
  target and *without* "If there isn't one, just tell me". The request presupposes a match that does not exist.
- **Underspecified per fact (drop-F).** The request without the condition that carries the fact. The seed is the
  cover's (target and every near miss), so the target and every near miss that fails only that condition fully match.
  The rewording is supplied (by hand in Phase 1, by the Muse writer later); this module checks the match set.
- **Underspecified clone.** One per scenario: a copy of the target that differs only in fields the request never uses
  (its name or title), with copies of the rows that point at it (fact_coverage_02's P3 twin, generalized to any
  table key and to child rows).

Every variant is finished with fdc (the expected set is recomputed and every claim checked), and dangling foreign keys
are reported. Nothing here calls a model.
"""
from __future__ import annotations

import copy
import re
from collections import defaultdict

from grounding.runs.autogen_01.kit.derive import PRIVATE, _finish, _foreign_keys, dangling, effect_key
from grounding.runs.fact_coverage_01 import fdc
from grounding.runs.fact_coverage_01.pilot.variants import isolate
from grounding.runs.fact_coverage_02.followups import _conditions
from grounding.runs.fact_coverage_02.suite_pilot import keep_claims, rename

PLURAL_WORDS = re.compile(r"\b(all|every|each|any|both)\b", re.I)


def _base(case: dict) -> dict:
    return {k: v for k, v in copy.deepcopy(case).items() if k not in PRIVATE}


def _check_seed(case: dict) -> dict:
    seed = copy.deepcopy(case["seed"])
    for table, rows in case.get("derived_rows", {}).items():
        seed[table] = rows
    return seed


def facts_of(case: dict) -> dict:
    """fact -> indices of its claims in the first reference, in the order they appear."""
    out = defaultdict(list)
    for ci, claim in enumerate(case["references"][0]["claims"]):
        out[claim["requirement"]].append(ci)
    return dict(out)


def _family(claims, idx):
    return "+".join(sorted({claims[ci].get("family") or "" for ci in idx}))


def absence_twins(case: dict) -> list:
    """[(twin case, meta)], one per fact."""
    base = _base(case)
    sid, ref = base["case_id"], base["references"][0]
    out = []
    for fact, idx in facts_of(base).items():
        keys = [f"I1{ci + 1}" for ci in idx]
        if len(idx) >= 2:
            twin = keep_claims(base, 0, set(idx))
        else:
            twin = isolate(base, 0, idx[0], ref["claims"][idx[0]].get("keep", ()))
        twin = rename(twin, f"AT-{sid}-{'-'.join(keys)}")
        twin["form"], twin["mode"], twin["variant_of"] = "absent", "absent", sid
        twin, errors = _finish(twin)
        errors = list(errors) + dangling(twin)
        out.append((twin, {"form": "absence twin", "scenario": sid, "fact": fact, "family": _family(ref["claims"], idx),
                           "keys": keys, "decoys": len(idx), "errors": errors}))
    return out


def _nodes(query):
    yield query
    for e in query.get("edges", []):
        yield from _nodes(e["node"])


def condition_keys(query: dict, claims: list, fact: str) -> set:
    """Filter and edge keys that carry the fact: those labelled with it, and the DROP/SUB targets of its claims."""
    keys = set()
    for node in _nodes(query):
        for f in node.get("filters", []):
            if f.get("fact") == fact:
                keys.add(f["key"])
        for e in node.get("edges", []):
            if e.get("fact") == fact:
                keys.add(e["key"])
    for c in claims:
        if c["requirement"] == fact and c["mutation"].get("type") in ("DROP", "SUB") and c["mutation"].get("target"):
            keys.add(c["mutation"]["target"])
    return keys


def relaxed_query(query: dict, keys: set) -> dict:
    out = copy.deepcopy(query)
    present = set(fdc.keys(out))
    for key in sorted(keys):
        if key in present:
            out = fdc.mutate(out, {"type": "DROP", "target": key})
            present = set(fdc.keys(out))
    return out


def _same(a, b):
    return fdc._same(a, b)


def drop_f(case: dict, fact: str, prompt: str | None, variant_id: str | None = None) -> tuple:
    """The underspecified variant on `fact`. Returns (variant, meta); meta['problems'] lists every failed check."""
    base = _base(case)
    sid, ref = base["case_id"], base["references"][0]
    claims = ref["claims"]
    keys = condition_keys(ref["query"], claims, fact)
    relaxed = relaxed_query(ref["query"], keys)
    seed = _check_seed(base)
    full = fdc.evaluate(seed, ref["query"])
    selected = fdc.evaluate(seed, relaxed)
    dropped_facts = sorted({c["requirement"] for c in claims if condition_keys(ref["query"], claims, c["requirement"]) & keys})
    freed = [c["witness"] for c in claims if c["requirement"] in dropped_facts]
    expected_matches = list(full) + [w for w in freed if not any(_same(w, f) for f in full)]
    problems = []
    if not keys:
        problems.append(f"no query condition carries {fact}")
    if sorted(map(str, selected)) != sorted(map(str, expected_matches)):
        problems.append(f"the relaxed query selects {selected}, not the target plus the freed near misses "
                        f"{expected_matches}")
    if len(selected) < 2:
        problems.append("fewer than two full matches")
    remaining = _conditions(relaxed)
    if remaining < 2:
        problems.append(f"scope (D2): {remaining} identifying condition(s) remain")
    if prompt and PLURAL_WORDS.search(prompt):
        problems.append("the reworded request has a plural or universal word")
    variant = copy.deepcopy(base)
    if prompt:
        variant["prompt"] = prompt
    vref = variant["references"][0]
    vref["query"] = relaxed
    vref["expected"] = selected
    vref["resolution"] = "underspecified"
    vref["claims"] = [c for c in claims if c["requirement"] not in dropped_facts]
    kept_decoys = sum(1 for c in vref["claims"])
    variant["form"], variant["mode"], variant["variant_of"] = "present", "underspecified", sid
    variant = rename(variant, variant_id or f"U-{sid}-{fact.split(':')[-1].replace('.', '_')}")
    variant, errors = _finish(variant)
    problems += list(errors) + dangling(variant)
    return variant, {"form": "underspecified", "scenario": sid, "fact": fact, "dropped_facts": dropped_facts,
                     "dropped_keys": sorted(keys), "matches": len(selected), "other_near_misses": kept_decoys,
                     "conditions_left": remaining, "problems": problems,
                     "family": _family(claims, [i for i, c in enumerate(claims) if c["requirement"] in dropped_facts])}


def clone(case: dict, changes: dict, new_key: str, variant_id: str | None = None) -> tuple:
    """The underspecified clone: the target copied with `changes` (fields the request does not use), and a copy of
    every row that points at it. Returns (variant, meta)."""
    base = _base(case)
    sid, ref = base["case_id"], base["references"][0]
    table = ref["query"]["table"]
    pk = effect_key(base["domain"], table)
    col = pk[0] if len(pk) == 1 else None
    problems = []
    if col is None:
        problems.append(f"{table} has a composite key {pk}; clone not supported")
        return None, {"form": "underspecified clone", "scenario": sid, "problems": problems}
    target_id = str(ref["expected"][0])
    rows = [r for r in base["seed"][table] if str(r.get(col)) == target_id]
    if len(rows) != 1:
        problems.append(f"found {len(rows)} {table} rows for the target {target_id}")
        return None, {"form": "underspecified clone", "scenario": sid, "problems": problems}
    new_row = copy.deepcopy(rows[0])
    new_row.update({col: new_key, **changes})
    base["seed"][table].append(new_row)
    copied = 0
    for child, fk_col, ref_table, ref_col in _foreign_keys(base["domain"]):
        if ref_table != table or ref_col != col or child not in base["seed"] or child == table:
            continue
        child_pk = effect_key(base["domain"], child)
        for r in [r for r in base["seed"][child] if str(r.get(fk_col)) == target_id]:
            c = copy.deepcopy(r)
            c[fk_col] = new_key
            if len(child_pk) == 1 and child_pk[0] != fk_col and c.get(child_pk[0]) is not None:
                c[child_pk[0]] = f"{c[child_pk[0]]}_clone" if isinstance(c[child_pk[0]], str) else c[child_pk[0]] + 100000
            base["seed"][child].append(c)
            copied += 1
    seed = _check_seed(base)
    selected = fdc.evaluate(seed, ref["query"])
    want = [ref["expected"][0], new_key]
    if sorted(map(str, selected)) != sorted(map(str, want)):
        problems.append(f"the query selects {selected}, not the target and its clone {want}")
    ref["expected"] = selected
    ref["resolution"] = "underspecified"
    base["form"], base["mode"], base["variant_of"] = "present", "underspecified", sid
    base = rename(base, variant_id or f"UC-{sid}")
    base, errors = _finish(base)
    problems += list(errors) + dangling(base)
    return base, {"form": "underspecified clone", "scenario": sid, "fact": None, "changes": changes,
                  "child_rows_copied": copied, "matches": len(selected), "problems": problems}
