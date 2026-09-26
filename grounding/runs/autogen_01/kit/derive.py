"""The suite for one accepted scenario (decisions D6 and D7), built with fact_coverage_02's functions.

- **Cover:** the scenario as written (target and all decoys). It is the one target-present test; hidden-target
  layouts are not generated in this version.
- **Probe:** one per decoy. The decoy alone, no target, and "If there isn't one, just tell me." (plural: "If there
  aren't any, …"). A decoy's `keep` rows stay, as in the pilot.
- **Fact probe:** one per fact with two or more decoys, holding all of them, no target, and the escape clause.
"""
from __future__ import annotations

import copy
import hashlib
import json
from collections import defaultdict

from grounding.runs.fact_coverage_01.pilot.common import finish
from grounding.runs.fact_coverage_01.pilot.variants import isolate
from grounding.runs.fact_coverage_02.suite_pilot import keep_claims, rename, told

PRIVATE = ("write_check", "conditions")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def _foreign_keys(domain):
    """(table, column, referenced table, referenced column) from the replica's own schema."""
    from grounding.runs.autogen_01.kit.seedops import _metadata
    out = []
    for table in _metadata(domain).tables.values():
        for fk in table.foreign_keys:
            out.append((table.name, fk.parent.name, fk.column.table.name, fk.column.name))
    return out


def prune_orphans(case):
    """Remove rows whose foreign keys point at removed rows, until none do. Target removal must take whatever
    points to the target with it (method.md, "anchors must survive"); the shared cascade does not know every
    replica foreign key (for example Slack's memberships of a removed user)."""
    seed = case["seed"]
    # Self-references (a sub-issue's parent, a reply's root) are left to the shared cascade, which already
    # decides them for the hand-built suites.
    fks = [fk for fk in _foreign_keys(case["domain"]) if fk[0] in seed and fk[0] != fk[2]]
    while True:
        removed = 0
        for table, col, ref_table, ref_col in fks:
            present = {r.get(ref_col) for r in seed.get(ref_table, [])}
            keep = [r for r in seed[table] if r.get(col) is None or r.get(col) in present]
            removed += len(seed[table]) - len(keep)
            seed[table] = keep
        if not removed:
            return case


def effect_key(domain, table) -> list[str]:
    """The primary-key columns of a table, from the replica's own schema."""
    from grounding.runs.autogen_01.kit.seedops import _metadata
    return [c.name for c in _metadata(domain).tables[table].primary_key.columns]


def normalize_effects(case):
    """Give every effect locator its table's real key. The diff attribution keys rows by it, and a writer who
    leaves it out gets `id`, which association tables (reactions, memberships, label links) do not have."""
    for ref in case["references"]:
        effect = ref.get("effect")
        if effect and effect.get("table"):
            effect["key"] = effect_key(case["domain"], effect["table"])
    return case


def dangling(case) -> list[str]:
    """Foreign keys (self-references included) that point at no row: the test's seed would not install."""
    seed = case["seed"]
    out = []
    for table, col, ref_table, ref_col in _foreign_keys(case["domain"]):
        if table not in seed:
            continue
        present = {r.get(ref_col) for r in seed.get(ref_table, [])}
        for r in seed[table]:
            if r.get(col) is not None and r.get(col) not in present:
                out.append(f"{table}.{col}={r.get(col)!r} has no {ref_table} row")
    return sorted(set(out))


def _finish(case):
    prune_orphans(case)
    case, _results, errors = finish(case)
    case["coverage_claims"] = sorted({c["requirement"] for r in case["references"] for c in r["claims"]})
    case["case_sha256"] = digest({k: v for k, v in case.items() if k != "case_sha256"})
    return case, errors


def suite(case: dict):
    """[(test case, meta)] for a built scenario case; meta has form, scenario, fact, family."""
    sid = case["case_id"]
    plural = bool(case.get("plural"))
    base = {k: v for k, v in copy.deepcopy(case).items() if k not in PRIVATE}
    out = []
    cover, _ = _finish(copy.deepcopy(base))
    out.append((cover, {"form": "cover", "scenario": sid, "fact": None, "family": None}))
    ref = base["references"][0]
    by_fact = defaultdict(list)
    for ci, claim in enumerate(ref["claims"]):
        key = f"I1{ci + 1}"
        probe = told(rename(isolate(base, 0, ci, claim.get("keep", ())), f"P-{sid}-{key}"), plural)
        probe, _ = _finish(probe)
        out.append((probe, {"form": "probe", "scenario": sid, "fact": claim["requirement"],
                            "family": claim.get("family"), "contestable": bool(claim.get("contestable"))}))
        by_fact[claim["requirement"]].append((ci, key))
    for fact, items in by_fact.items():
        if len(items) < 2:
            continue
        keys = [k for _, k in items]
        fp = told(rename(keep_claims(base, 0, {ci for ci, _ in items}), f"FP-{sid}-{'-'.join(keys)}"), plural)
        fp, _ = _finish(fp)
        out.append((fp, {"form": "fact probe", "scenario": sid, "fact": fact,
                         "family": "+".join(sorted({ref["claims"][ci].get("family", "") for ci, _ in items}))}))
    return out
