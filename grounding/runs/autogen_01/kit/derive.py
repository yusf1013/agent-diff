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


def _finish(case):
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
                            "family": claim.get("family")}))
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
