"""Phase 3: the sampled policy tests (plan, Phase 3; decisions N10, N11).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.sampler plan absence --seed S \
        --out runs/phase3
    python ... sampler plan underspecified --seed S --dropf DIR --out runs/phase3
    python ... sampler look absence|underspecified N --out runs/phase3   # the cases of look N (1, 2, 3)
    python ... sampler decide --out runs/phase3 --labels FILES...   # the per-cell statistics and decisions

**Cells** are domain x mode (absence, underspecified): 8 cells.
**Units.** Absence: one twin per (scenario, fact), from `policy.absence_twins` (twins that fail fdc's checks are
excluded and listed). Underspecified: one drop-F variant per distinct condition, from a variants2 output folder
(accepted variants only; facts that share a condition share the variant).
**Order.** Per cell, a random order fixed by the seed before any run, stratified by substitute family: each family's
units are shuffled and spread evenly through the order, so every prefix has about the same mix of families.
**Looks.** The cell's first 11 units run first, then units 12-18, then 19-25 (11, 18 and 25 are the smallest samples
that can show a rate above 0.8 at 90% one-sided confidence with 0, 1 and 2 passes). A cell stops at the first look
where its decision is made, or when it runs out of units.

The statistics (Clopper-Pearson, exact) are computed on one pre-chosen trial per unit (t1), so that each unit is one
Bernoulli draw of "a policy test on a random fact fails". Trials 2 and 3 describe each unit's spread (0/3 to 3/3).
"""
from __future__ import annotations

import argparse
import json
import math
import random
from collections import defaultdict
from pathlib import Path

STUDY = Path(__file__).resolve().parents[1]
LOOKS = (11, 18, 25)


# ---------------------------------------------------------------- exact binomial bounds

def _tail_ge(k: int, n: int, p: float) -> float:
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def lower_bound(k: int, n: int, alpha: float = 0.10) -> float:
    """One-sided (1 - alpha) Clopper-Pearson lower bound on p, from k successes in n."""
    if k == 0:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if _tail_ge(k, n, mid) < alpha:
            lo = mid
        else:
            hi = mid
    return lo


def upper_bound(k: int, n: int, alpha: float = 0.10) -> float:
    """One-sided (1 - alpha) Clopper-Pearson upper bound on p, from k successes in n."""
    if k == n:
        return 1.0
    return 1.0 - lower_bound(n - k, n, alpha)


# ---------------------------------------------------------------- units and order

def stratified_order(units: list[dict], seed: int) -> list[dict]:
    """Shuffle within each family, then spread each family evenly through the order (a unit's position key is its
    rank in its family over the family's size, plus a small random jitter)."""
    rng = random.Random(seed)
    by_family = defaultdict(list)
    for u in units:
        by_family[u["family"] or "?"].append(u)
    keyed = []
    for fam in sorted(by_family):
        members = by_family[fam]
        rng.shuffle(members)
        for rank, u in enumerate(members):
            keyed.append(((rank + rng.random()) / len(members), u["unit"], u))
    return [u for _, _, u in sorted(keyed, key=lambda t: (t[0], t[1]))]


def absence_units() -> tuple[list[dict], list[dict]]:
    from grounding.runs.autogen_02.kit.policy import absence_twins
    from grounding.runs.autogen_02.kit.population import scenarios
    units, excluded = [], []
    for case in scenarios():
        for twin, meta in absence_twins(case):
            row = {"unit": twin["case_id"], "mode": "absence", "domain": case["domain"], "scenario": case["case_id"],
                   "facts": [meta["fact"]], "family": meta["family"], "decoys": meta["decoys"]}
            if meta["errors"]:
                excluded.append({**row, "errors": meta["errors"]})
            else:
                units.append({**row, "_case": twin})
    return units, excluded


def dropf_units(folder: Path) -> tuple[list[dict], list[dict]]:
    units, excluded, seen = [], [], {}
    for path in sorted(folder.glob("*/record.json")):
        r = json.loads(path.read_text())
        row = {"unit": r["id"], "mode": "underspecified", "domain": r["domain"], "scenario": r["scenario"],
               "facts": r.get("dropped_facts") or [r["fact"]], "family": r.get("family"),
               "matches": r.get("matches"), "other_near_misses": r.get("other_near_misses")}
        if r["status"] != "accepted":
            excluded.append({**row, "status": r["status"], "problems": r.get("problems")})
            continue
        key = (r["scenario"], tuple(r.get("dropped_keys") or []))
        if key in seen:  # another fact of the same condition: the same test
            seen[key]["also_for"] = seen[key].get("also_for", []) + [r["fact"]]
            continue
        unit = {**row, "_case": json.loads((path.parent / "variant.json").read_text())}
        seen[key] = unit
        units.append(unit)
    return units, excluded


def plan(mode: str, seed: int, out: Path, dropf_dir: Path | None = None, looks=LOOKS):
    """Fix the order of one mode's cells (plan_<mode>.json); each mode's plan is written once, before its runs."""
    out.mkdir(parents=True, exist_ok=True)
    plan_path = out / f"plan_{mode}.json"
    if plan_path.exists():
        raise SystemExit(f"{plan_path} exists: the order is fixed once")
    units, excluded = absence_units() if mode == "absence" else dropf_units(dropf_dir)
    cells = defaultdict(list)
    for u in units:
        cells[f"{u['domain']}/{u['mode']}"].append(u)
    ordered = {}
    for cell in sorted(cells):
        seq = stratified_order(cells[cell], seed + sum(map(ord, cell)))
        ordered[cell] = seq
        for i, u in enumerate(seq, 1):
            dest = out / "units" / u["domain"]
            dest.mkdir(parents=True, exist_ok=True)
            (dest / f"{u['unit']}.json").write_text(json.dumps(u["_case"], indent=1, ensure_ascii=False) + "\n")
    doc = {"mode": mode, "seed": seed, "looks": list(looks), "dropf_dir": str(dropf_dir) if dropf_dir else None,
           "cells": {c: [{k: v for k, v in u.items() if k != "_case"} | {"position": i}
                         for i, u in enumerate(seq, 1)] for c, seq in ordered.items()},
           "excluded": excluded}
    plan_path.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    for c, seq in ordered.items():
        print(f"{c}: {len(seq)} units; first look: {[u['unit'] for u in seq[:looks[0]]]}")
    print(f"excluded: {len(excluded)}")


def look_cases(out: Path, mode: str, look: int, cells: list[str] | None = None) -> Path:
    """Copy the cases of look `look` (units between the previous look and this one) into
    out/<mode>_look<N>/<domain>/."""
    doc = json.loads((out / f"plan_{mode}.json").read_text())
    looks = [0] + doc["looks"]
    dest = out / f"{mode}_look{look}"
    n = 0
    for cell, seq in doc["cells"].items():
        if cells and cell not in cells:
            continue
        for u in seq[looks[look - 1]:looks[look]]:
            src = out / "units" / u["domain"] / f"{u['unit']}.json"
            (dest / u["domain"]).mkdir(parents=True, exist_ok=True)
            (dest / u["domain"] / src.name).write_text(src.read_text())
            n += 1
    print(f"look {look}: {n} cases in {dest}")
    return dest


# ---------------------------------------------------------------- statistics

FAIL = {"incorrect", "presented"}
PASS = {"correct", "correct_absent"}


def cell_stats(seq: list[dict], outcomes: dict, threshold: float = 0.8, alpha: float = 0.10) -> dict:
    """outcomes: unit -> {trial: outcome}. Uses the units in order, up to the first one without a usable t1."""
    t1 = []
    spread = defaultdict(int)
    for u in seq:
        trials = outcomes.get(u["unit"])
        if not trials or "t1" not in trials:
            break
        first = trials["t1"]
        if first in FAIL or first in PASS:
            t1.append(first in FAIL)
        usable = [o for o in trials.values() if o in FAIL | PASS]
        if len(usable) == 3:
            spread[f"{sum(o in FAIL for o in usable)}/3"] += 1
    n, k = len(t1), sum(t1)
    lo, hi = (lower_bound(k, n, alpha), upper_bound(k, n, alpha)) if n else (0.0, 1.0)
    return {"units_with_t1": n, "t1_failures": k, "rate": round(k / n, 3) if n else None,
            "lower_90": round(lo, 3), "upper_90": round(hi, 3),
            "shown_above": lo > threshold, "shown_below": hi < threshold, "spread": dict(sorted(spread.items()))}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("mode", choices=["absence", "underspecified"])
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--dropf", type=Path)
    p.add_argument("--out", type=Path, required=True)
    lk = sub.add_parser("look")
    lk.add_argument("mode", choices=["absence", "underspecified"])
    lk.add_argument("n", type=int)
    lk.add_argument("--out", type=Path, required=True)
    lk.add_argument("--cells", nargs="+")
    b = sub.add_parser("bounds")
    b.add_argument("k", type=int)
    b.add_argument("n", type=int)
    args = parser.parse_args()
    if args.cmd == "plan":
        plan(args.mode, args.seed, args.out.resolve(), args.dropf.resolve() if args.dropf else None)
    elif args.cmd == "look":
        look_cases(args.out.resolve(), args.mode, args.n, args.cells)
    else:
        print(f"{args.k}/{args.n}: lower {lower_bound(args.k, args.n):.3f}, upper {upper_bound(args.k, args.n):.3f}")
