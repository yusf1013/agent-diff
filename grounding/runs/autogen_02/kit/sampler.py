"""Phase 3: the sampled policy tests (plan, Phase 3; decisions N10, N11).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.sampler plan absence --seed S \
        --out runs/phase3
    python ... sampler plan underspecified --seed S --dropf DIR --out runs/phase3
    python ... sampler look absence|underspecified N --out runs/phase3 [--cells C ...] [--dest NAME]
        # the cases of look N (1, 2, 3); with --dest, only the units no earlier look folder holds
    python ... sampler extend absence|underspecified --seed S [--dropf DIR] --out runs/phase3
        # amendment 5: append Phase 4's units after each cell's fixed order (once, before any Phase 3 verdict)
    python ... sampler decide absence|underspecified --out runs/phase3 --verdicts DIRS...
        # the per-cell statistics and decisions

**Cells** are domain x mode (absence, underspecified): 8 cells.
**Units.** Absence: one twin per (scenario, fact), from `policy.absence_twins` (twins that fail fdc's checks are
excluded and listed). Underspecified: one drop-F variant per distinct condition, from a variants2 output folder
(accepted variants only; facts that share a condition share the variant).
**Order.** Per cell, a random order fixed by the seed before any run, stratified by substitute family: each family's
units are shuffled and spread evenly through the order, so every prefix has about the same mix of families.
**Looks.** The cell's first 11 units run first, then units 12-18, then 19-25 (11, 18 and 25 are the smallest samples
that can show a rate above 0.8 at 90% one-sided confidence with 0, 1 and 2 passes). A cell stops at the first look
where its decision is made, or when it runs out of units.

The statistics (Clopper-Pearson, exact) are computed on one pre-chosen trial per unit (t1; if t1 is void, the first
usable of t2 and t3), so that each unit is one Bernoulli draw of "a policy test on a random unit fails". All three
trials describe each unit's spread (0/3 to 3/3). Decisions are taken only at a look: the statistic uses the first
11, 18 or 25 valid units, or all of them when fewer remain.
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


def absence_units(cases: list[dict] | None = None) -> tuple[list[dict], list[dict]]:
    from grounding.runs.autogen_02.kit.policy import absence_twins
    from grounding.runs.autogen_02.kit.population import scenarios
    units, excluded = [], []
    for case in cases or scenarios():
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


def extend(mode: str, seed: int, out: Path, dropf_dir: Path | None = None):
    """Append Phase 4's units to each cell's fixed order (amendment 5): the cell's Phase 3 order is unchanged, and
    Phase 4's units follow it in their own stratified order (seed recorded), so they are drawn only where Phase 3's
    units run out. The plan before the extension is kept as plan_<mode>.v1.json. Done once, before any Phase 3
    verdict."""
    import datetime
    import shutil
    from grounding.runs.autogen_02.kit.population import phase4_scenarios
    plan_path = out / f"plan_{mode}.json"
    doc = json.loads(plan_path.read_text())
    if doc.get("extension"):
        raise SystemExit(f"{plan_path} is already extended: the order is fixed once")
    v1 = out / f"plan_{mode}.v1.json"
    if not v1.exists():
        shutil.copy(plan_path, v1)
    units, excluded = absence_units(phase4_scenarios()) if mode == "absence" else dropf_units(dropf_dir)
    cells = defaultdict(list)
    for u in units:
        cells[f"{u['domain']}/{u['mode']}"].append(u)
    added = {}
    for cell in sorted(cells):
        seq = doc["cells"].setdefault(cell, [])
        start = len(seq)
        for i, u in enumerate(stratified_order(cells[cell], seed + sum(map(ord, cell))), start + 1):
            dest = out / "units" / u["domain"]
            dest.mkdir(parents=True, exist_ok=True)
            (dest / f"{u['unit']}.json").write_text(json.dumps(u["_case"], indent=1, ensure_ascii=False) + "\n")
            seq.append({k: v for k, v in u.items() if k != "_case"} | {"position": i, "source": "phase4"})
        added[cell] = len(seq) - start
    doc["extension"] = {"source": "phase4", "seed": seed, "at": datetime.datetime.now().isoformat(timespec="seconds"),
                        "dropf_dir": str(dropf_dir) if dropf_dir else None, "added": added, "excluded": excluded}
    plan_path.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    for cell, n in added.items():
        valid = valid_sequence(doc["cells"][cell])
        print(f"{cell}: {n} Phase 4 units appended; valid units now {len(valid)} "
              f"({sum(u.get('source') == 'phase4' for u in valid)} from Phase 4)")
    print(f"excluded: {len(excluded)}")


VALIDITY = STUDY.parent / "autogen_01" / "eval" / "validity.json"
VALIDITY4 = STUDY / "eval" / "phase4_review.json"


def review_exclusion(unit: dict) -> str | None:
    """Why the manual validity review rules this unit out, or None (amendment 2, C.9): autogen_01's review for its
    scenarios, mine (eval/phase4_review.json) for Phase 4's. An absence unit goes when any of its near misses is
    invalid or contestable (under presupposition, acting on a contestable near miss may be the reasonable reading);
    an underspecified unit goes when any near miss left in its seed is invalid (a record that in fact fits), or when
    the scenario is invalid."""
    source = VALIDITY4 if unit["scenario"].startswith("G4-") else VALIDITY
    review = json.loads(source.read_text()).get(unit["scenario"], {})
    if review.get("verdict") == "invalid":
        return f"scenario {unit['scenario']} invalid in {'my Phase 4' if source == VALIDITY4 else 'autogen_01'}'s review"
    case = json.loads((STUDY / "runs" / "phase3" / "units" / unit["domain"] / f"{unit['unit']}.json").read_text())
    witnesses = {str(c["witness"]) for c in case["references"][0]["claims"]}
    for w, verdict in review.get("decoys", {}).items():
        if w not in witnesses:
            continue
        if verdict.startswith("invalid") or (unit["mode"] == "absence" and verdict.startswith("contestable")):
            return f"near miss {w}: {verdict[:160]}"
    return None


def valid_sequence(seq: list[dict]) -> list[dict]:
    return [u for u in seq if not review_exclusion(u)]


def already_cased(out: Path, mode: str) -> set[str]:
    """Units already copied into an earlier look folder of this mode, or into a Phase 4 policy run (amendment 5), run
    or queued: a look takes their verdicts from that run instead of running them again."""
    return {p.stem for p in out.glob(f"{mode}_look*/*/*.json")} | \
        {p.stem for p in (STUDY / "runs" / "phase4").glob("*policy_cases/*/*.json")}


def look_cases(out: Path, mode: str, look: int, cells: list[str] | None = None, dest_name: str | None = None,
               positions: tuple[int, int] | None = None) -> Path:
    """Copy the cases of look `look` (the cell's valid units between the previous look and this one, in the fixed
    order) into out/<mode>_look<N>/<domain>/, or into out/<dest_name>/ (a look completed after the order was
    extended, amendment 5). Units already cased by an earlier look or a Phase 4 policy run are left out: their
    verdicts come from that run (pass its judge folder to `decide`)."""
    doc = json.loads((out / f"plan_{mode}.json").read_text())
    looks = [0] + doc["looks"]
    dest = out / (dest_name or f"{mode}_look{look}")
    if dest.exists():
        raise SystemExit(f"{dest} exists")
    have = already_cased(out, mode)
    n = 0
    for cell, seq in doc["cells"].items():
        if cells and cell not in cells:
            continue
        lo, hi = (positions[0] - 1, positions[1]) if positions else (looks[look - 1], looks[look])
        for u in valid_sequence(seq)[lo:hi]:
            if u["unit"] in have:
                continue
            src = out / "units" / u["domain"] / f"{u['unit']}.json"
            (dest / u["domain"]).mkdir(parents=True, exist_ok=True)
            (dest / u["domain"] / src.name).write_text(src.read_text())
            n += 1
    print(f"look {look}: {n} cases in {dest}")
    return dest


# ---------------------------------------------------------------- statistics

FAIL = {"incorrect", "presented"}
PASS = {"correct", "correct_absent", "false_absence", "incomplete"}  # every usable outcome that is not a fail
# (amendment 2, C.5); `not_established` and `artifact` are void and drop out of n


def draw(trials: dict) -> bool | None:
    """The unit's one draw: its first trial with a usable outcome, in the fixed order t1, t2, t3 (t1 unless t1 is
    void). True = fails; None = no usable trial."""
    for t in ("t1", "t2", "t3"):
        o = trials.get(t)
        if o in FAIL or o in PASS:
            return o in FAIL
    return None


def cell_stats(seq: list[dict], outcomes: dict, threshold: float = 0.8, alpha: float = 0.10) -> dict:
    """outcomes: unit -> {trial: outcome}. Uses the units in order up to the first one not run yet (no outcomes)."""
    draws, run = [], 0
    spread = defaultdict(int)
    for u in seq:
        trials = outcomes.get(u["unit"])
        if not trials:
            break
        run += 1
        d = draw(trials)
        if d is not None:
            draws.append(d)
        usable = [o for o in trials.values() if o in FAIL | PASS]
        if len(usable) == 3:
            spread[f"{sum(o in FAIL for o in usable)}/3"] += 1
    n, k = len(draws), sum(draws)
    lo, hi = (lower_bound(k, n, alpha), upper_bound(k, n, alpha)) if n else (0.0, 1.0)
    return {"units_run": run, "draws": n, "failures": k, "rate": round(k / n, 3) if n else None,
            "lower_90": round(lo, 3), "upper_90": round(hi, 3),
            "shown_above": lo > threshold, "shown_below": hi < threshold, "spread": dict(sorted(spread.items()))}


def verdict_outcomes(verdict_dirs: list[Path]) -> dict:
    """unit -> {trial: outcome} from judge v2's verdicts (DIR/<run>/<trial>/<unit>/verdict.json)."""
    out = defaultdict(dict)
    for d in verdict_dirs:
        for path in d.glob("*/*/*/verdict.json"):
            v = json.loads(path.read_text())
            unit, trial = path.parent.name, path.parent.parent.name
            out[unit][trial] = v.get("outcome")
    return out


def decide(out: Path, mode: str, verdict_dirs: list[Path], threshold: float = 0.8) -> dict:
    """Per cell, the statistic over the units run so far (in the fixed valid order) and the decision at the last
    completed look (amendment 2, C.5 and C.6)."""
    doc = json.loads((out / f"plan_{mode}.json").read_text())
    outcomes = verdict_outcomes(verdict_dirs)
    result = {}
    for cell, seq in doc["cells"].items():
        valid = valid_sequence(seq)
        run = cell_stats(valid, outcomes, threshold)["units_run"]
        boundaries = [k for k in doc["looks"] if k <= len(valid)] + ([len(valid)] if len(valid) not in doc["looks"]
                                                                       else [])
        reached = max([k for k in boundaries if k <= run] or [0])
        stats = cell_stats(valid[:reached], outcomes, threshold) if reached else cell_stats([], outcomes, threshold)
        if not reached:
            decision = "first look not complete"
        elif stats["shown_above"]:
            decision = "policy-level"
        elif stats["shown_below"]:
            decision = "not policy-level"
        elif reached >= len(valid):
            decision = "undecided (units exhausted)"
        else:
            decision = "continue to the next look"
        result[cell] = {**stats, "valid_units": len(valid), "look_reached": reached, "decision": decision}
        if any(u.get("source") == "phase4" for u in valid[:reached]):  # amendment 5: the two writers' units apart
            for name, keep in (("phase3_only", lambda u: u.get("source") != "phase4"),
                               ("phase4_only", lambda u: u.get("source") == "phase4")):
                part = cell_stats([u for u in valid[:reached] if keep(u)], outcomes, threshold)
                result[cell][name] = {k: part[k] for k in ("draws", "failures", "rate", "lower_90", "upper_90")}
    return result


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
    lk.add_argument("--dest", help="a new folder name: only units no earlier look folder holds (amendment 5)")
    lk.add_argument("--positions", type=int, nargs=2, metavar=("FIRST", "LAST"),
                    help="valid positions FIRST..LAST (1-based) instead of the look's (a declared robustness check)")
    xt = sub.add_parser("extend")
    xt.add_argument("mode", choices=["absence", "underspecified"])
    xt.add_argument("--seed", type=int, required=True)
    xt.add_argument("--dropf", type=Path)
    xt.add_argument("--out", type=Path, required=True)
    dc = sub.add_parser("decide")
    dc.add_argument("mode", choices=["absence", "underspecified"])
    dc.add_argument("--out", type=Path, required=True)
    dc.add_argument("--verdicts", type=Path, nargs="+", required=True)
    ex = sub.add_parser("exclusions")
    ex.add_argument("mode", choices=["absence", "underspecified"])
    ex.add_argument("--out", type=Path, required=True)
    b = sub.add_parser("bounds")
    b.add_argument("k", type=int)
    b.add_argument("n", type=int)
    args = parser.parse_args()
    if args.cmd == "plan":
        plan(args.mode, args.seed, args.out.resolve(), args.dropf.resolve() if args.dropf else None)
    elif args.cmd == "look":
        look_cases(args.out.resolve(), args.mode, args.n, args.cells, args.dest,
                   tuple(args.positions) if args.positions else None)
    elif args.cmd == "extend":
        extend(args.mode, args.seed, args.out.resolve(), args.dropf.resolve() if args.dropf else None)
    elif args.cmd == "decide":
        res = decide(args.out.resolve(), args.mode, [p.resolve() for p in args.verdicts])
        (args.out.resolve() / f"decisions_{args.mode}.json").write_text(json.dumps(res, indent=1) + "\n")
        print(json.dumps(res, indent=1))
    elif args.cmd == "exclusions":
        doc = json.loads((args.out.resolve() / f"plan_{args.mode}.json").read_text())
        for cell, seq in doc["cells"].items():
            for u in seq:
                why = review_exclusion(u)
                if why:
                    print(f"{cell} #{u['position']} {u['unit']}: {why}")
    else:
        print(f"{args.k}/{args.n}: lower {lower_bound(args.k, args.n):.3f}, upper {upper_bound(args.k, args.n):.3f}")
