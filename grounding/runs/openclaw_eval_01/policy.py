"""The policy stage on OpenClaw (roadmap step 6a): autogen_02's sequential looks, in its fixed per-cell orders, run on
this study's agent. No unit is drawn again and no order changes.

    L="python grounding/runs/fact_coverage_02/launch.py"
    $L grounding.runs.openclaw_eval_01.policy look absence|underspecified N [--cells C ...] [--read UNIT ...]
    $L grounding.runs.openclaw_eval_01.policy decide absence|underspecified --verdicts DIR ...

- **Plans and units** are autogen_02's: runs/phase3/plan_<mode>.json (fixed per cell before any run, extended once
  with Phase 4's units) and runs/phase3/units/. Clones play no part in the looks and do not run.
- **Validity:** a unit is skipped when autogen_02's manual review rules it out (`sampler.review_exclusion`), or when
  known_defects.json leaves it out ("flawed is flawed": found flawed after Qwen's runs, it is left out before this
  agent's). The next valid unit takes its place. A unit to "read before it runs" stops the look until it is read
  (--read). A unit valid only up to a date (G4-LIN-02's) is left out from the start, since the looks span days and
  dropping it midway would shift the order.
- **G4-CAL-06's units** take the rebuilt case's event times (roadmap step 3), by event id. They are re-finished with
  the derivation's own `_finish`, which re-runs the reference check. A check requires that nothing else changed, and
  its absence twins must equal the ones `policy.absence_twins` derives from the rebuilt case.
- **A look** writes its cases to runs/policy/<mode>_look<N>/<domain>/: the cell's valid units between the previous
  look and this one (11, 18, 25; look 4 is the rest of the cell's valid units). Run them with run.py (3 trials),
  judge them with judge v2, then `decide`.
- **decide** gives each cell's statistic and decision by autogen_02's rules (`sampler.cell_stats` on one pre-chosen
  trial per unit, looks after 11, 18 and 25 valid units), from this study's verdicts only. As in autogen_02's
  `sampler.decide`, a cell still undecided at 25 goes on to its last valid unit, and once Phase 4's units are in, each
  writer's units are also reported apart (amendment 5).

`look` and `decide` are the first pass's (2026-09-28) and stay as they ran. After the discussion of 6a (roadmap,
2026-09-28) every valid policy test runs, with opaque ids and test-side clocks:

    $L grounding.runs.openclaw_eval_01.policy population absence|underspecified
    $L grounding.runs.openclaw_eval_01.policy decide-population absence|underspecified --verdicts DIR ... \
        --first-pass DIR ...

- **population** writes runs/policy/population_<mode>/<domain>/: every valid unit of the plans (suite_opaque/units;
  validity by `rulings.test_exclusion`), except Box units the first pass already ran. Box's ids are numbers, so its
  units are unchanged and their first-pass verdicts stand.
- **decide-population** applies the working rule, fixed here before the runs (`pooled_decision`): all runs of every
  valid unit count, and units, not runs, are the independent draws. A trial whose solver ran out its 8-minute budget
  (limiter waits excluded) is a failure, not a void (the PI, 2026-09-28, before any population verdict). Verdicts come from --verdicts, and for Box units
  from --first-pass. It also writes the other readings the step-5 investigation compares (`readings`).
"""
from __future__ import annotations

import argparse
import copy
import json
import re
from datetime import date
from pathlib import Path

from grounding.runs.autogen_01.kit.derive import _finish
from grounding.runs.autogen_02.kit import sampler
from grounding.runs.openclaw_eval_01 import rulings, run as runner
from grounding.runs.openclaw_eval_01.materialize import differences

HERE = Path(__file__).resolve().parent
PHASE3 = HERE.parent / "autogen_02" / "runs" / "phase3"
OUT = HERE / "runs" / "policy"
SUITE = HERE / "suite" / "cases"
REBUILT = {"G4-CAL-06"}
EVENT_TIMES = re.compile(r"\.seed\.calendar_events\[\d+\]\.(start|end)\.(dateTime|timeZone)")


def plan(mode: str) -> dict:
    return json.loads((PHASE3 / f"plan_{mode}.json").read_text())


def valid_units(seq: list[dict], actions: dict[str, str]) -> tuple[list[dict], dict[str, str]]:
    """The cell's valid units in the fixed order, and the ones left out with the reason. Nothing here depends on
    the date or on any outcome, so every look and `decide` see the same sequence."""
    kept, left_out = [], {}
    for u in seq:
        why = sampler.review_exclusion(u)
        action = runner.action_for(u["unit"], actions)
        if why:
            left_out[u["unit"]] = f"manual review: {why}"
        elif action.startswith(("leave out", "dropped")):
            left_out[u["unit"]] = f"known defect: {action}"
        elif runner.date_limit(action):
            left_out[u["unit"]] = f"known defect: {action} (the looks span days)"
        else:
            kept.append(u)
    return kept, left_out


def rebuilt_unit(u: dict, recorded: dict) -> dict:
    """A unit of a rebuilt scenario, with the rebuilt case's event times; checked."""
    scenario = json.loads((SUITE / u["domain"] / f"{u['scenario']}.json").read_text())
    times = {e["id"]: e for e in scenario["seed"]["calendar_events"]}
    case = copy.deepcopy(recorded)
    for event in case["seed"]["calendar_events"]:
        event["start"], event["end"] = copy.deepcopy(times[event["id"]]["start"]), copy.deepcopy(times[event["id"]]["end"])
    case, errors = _finish(case)
    diff = differences(recorded, case)
    other = [d for d in diff if d != ".case_sha256" and not EVENT_TIMES.fullmatch(d)]
    if errors or other:
        raise SystemExit(f"{u['unit']}: re-finished with problems {errors} or other changes {other}")
    if u["mode"] == "absence":  # unit files also carry `_arm`, which enters their digest
        from grounding.runs.autogen_02.kit.policy import absence_twins
        derived = {t["case_id"]: t for t, _ in absence_twins(scenario)}.get(u["unit"], {})
        strip = lambda c: {k: v for k, v in c.items() if k not in ("_arm", "case_sha256")}  # noqa: E731
        if strip(derived) != strip(case):
            raise SystemExit(f"{u['unit']}: differs from the twin derived from the rebuilt case: "
                             f"{differences(strip(derived), strip(case))[:10]}")
    return case


def look(mode: str, n: int, cells: list[str] | None, read: set[str]) -> Path:
    """Look n's units per cell: positions 1-11, 12-18 and 19-25; look 4 is the rest of a cell's valid units, the
    sampler's last boundary for a cell still undecided at 25."""
    doc = plan(mode)
    bounds = [0] + doc["looks"] + [None]
    dest = OUT / f"{mode}_look{n}"
    if dest.exists():
        raise SystemExit(f"{dest} exists")
    actions = runner.defect_actions()
    written, unread, left, positions = [], [], {}, {}
    for cell, seq in doc["cells"].items():
        if cells and cell not in cells:
            continue
        kept, left_out = valid_units(seq, actions)
        left.update(left_out)
        chosen = kept[bounds[n - 1]:bounds[n]]
        positions[cell] = [bounds[n - 1] + 1, bounds[n - 1] + len(chosen)]
        for u in chosen:
            if runner.action_for(u["unit"], actions).startswith("read before") and u["unit"] not in read:
                unread.append(u["unit"])
            written.append(u)
    if unread:
        raise SystemExit(f"read these units first, then pass them with --read: {unread}")
    for u in written:
        recorded = json.loads((PHASE3 / "units" / u["domain"] / f"{u['unit']}.json").read_text())
        case = rebuilt_unit(u, recorded) if u["scenario"] in REBUILT else recorded
        path = dest / u["domain"] / f"{u['unit']}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(case, indent=1, ensure_ascii=False) + "\n")
    (dest / "look.json").write_text(json.dumps({
        "mode": mode, "look": n, "positions": positions, "cells": cells or sorted(doc["cells"]),
        "units": [u["unit"] for u in written], "left_out_in_order": left, "read": sorted(read),
        "rebuilt": [u["unit"] for u in written if u["scenario"] in REBUILT], "date": date.today().isoformat()},
        indent=1) + "\n")
    print(f"{mode} look {n}: {len(written)} units -> {dest}")
    return dest


def decide(mode: str, verdict_dirs: list[Path]) -> dict:
    doc = plan(mode)
    outcomes = sampler.verdict_outcomes(verdict_dirs)
    actions = runner.defect_actions()
    result = {}
    for cell, seq in doc["cells"].items():
        valid, _ = valid_units(seq, actions)
        run = sampler.cell_stats(valid, outcomes)["units_run"]
        boundaries = [k for k in doc["looks"] if k <= len(valid)] + ([len(valid)] if len(valid) not in doc["looks"]
                                                                       else [])
        reached = max([k for k in boundaries if k <= run] or [0])
        stats = sampler.cell_stats(valid[:reached], outcomes)
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
                part = sampler.cell_stats([u for u in valid[:reached] if keep(u)], outcomes)
                result[cell][name] = {k: part[k] for k in ("draws", "failures", "rate", "lower_90", "upper_90")}
    return result


# ------------------------------------------------------------------ the full population (after 2026-09-28)

OPAQUE_UNITS = HERE / "suite_opaque" / "units"
SIXB_UNITS = HERE.parent / "completion_01" / "suite" / "units"
EXTENSION = OUT / "plan_extension.json"
EXTENSION_SEED = 2026092803
THRESHOLD, ALPHA, RESAMPLES, SEED = 0.8, 0.10, 20_000, 20260928


def local_attempt(recorded: str) -> Path:
    """A verdict's recorded attempt path, or, when it does not exist here (recorded in another checkout, such as a
    session's worktree since removed), the same attempt in this repository: everything up to and including
    "/grounding/runs/" is replaced by this repository's grounding/runs/ (2026-09-30, the lead's rule)."""
    path = Path(recorded)
    if path.exists() or "/grounding/runs/" not in recorded:
        return path
    return HERE.parent / recorded.split("/grounding/runs/", 1)[1]


def population_outcomes(verdict_dirs: list[Path]) -> dict:
    """unit -> {trial: outcome} from judge v2's verdicts, with every trial over the solver's budget
    (`rulings.over_budget`) counted as a failure ("incorrect"): judge v2 calls a timeout not_established, which
    would void it. The attempt is read where its verdict records it, or re-rooted here (`local_attempt`)."""
    out = sampler.verdict_outcomes(verdict_dirs)
    for d in verdict_dirs:
        for path in d.glob("*/*/*/verdict.json"):
            v = json.loads(path.read_text())
            attempt = local_attempt(v.get("attempt", ""))
            if attempt.exists() and rulings.over_budget(attempt):
                out[path.parent.name][path.parent.parent.name] = "incorrect"
    return out


def unit_case(u: dict) -> dict:
    folder = SIXB_UNITS if u.get("source") == "completion_01" else OPAQUE_UNITS
    return json.loads((folder / u["domain"] / f"{u['unit']}.json").read_text())


def population_plan(mode: str) -> dict:
    """autogen_02's plan with roadmap 6b's units (completion_01) appended to each cell (plan_extension.json)."""
    doc = plan(mode)
    ext = json.loads(EXTENSION.read_text()) if EXTENSION.exists() else {}
    for cell, seq in ext.get("cells", {}).items():
        if cell.endswith("/" + mode):
            doc["cells"].setdefault(cell, []).extend(seq)
    return doc


def extend(mode: str) -> None:
    """Append 6b's units of one mode to each cell's order, as amendment 5 appended Phase 4's: after the existing
    order, in their own stratified order (seed recorded). Done once per mode, before any of their verdicts."""
    ext = json.loads(EXTENSION.read_text()) if EXTENSION.exists() else {"cells": {}, "done": {}}
    if mode in ext["done"]:
        raise SystemExit(f"{mode} is already extended: the order is fixed once")
    listed = json.loads((SIXB_UNITS.parent / "units.json").read_text())["units"]
    cells: dict[str, list] = {}
    for u in listed:
        if u["mode"] == mode:
            cells.setdefault(f"{u['domain']}/{mode}", []).append(u)
    base = plan(mode)["cells"]
    added = {}
    for cell in sorted(cells):
        start = len(base.get(cell, []))
        order = sampler.stratified_order(cells[cell], EXTENSION_SEED + sum(map(ord, cell)))
        ext["cells"][cell] = [{**u, "position": start + i, "source": "completion_01"} for i, u in enumerate(order, 1)]
        added[cell] = len(order)
    ext["done"][mode] = {"seed": EXTENSION_SEED, "at": date.today().isoformat(), "added": added}
    EXTENSION.write_text(json.dumps(ext, indent=1) + "\n")
    print(f"{mode}: appended {added}")


def population_units(seq: list[dict]) -> tuple[list[dict], dict[str, str]]:
    """The cell's valid units in the fixed order, by the PI's rulings, and the ones left out with the reason."""
    kept, left_out = [], {}
    for u in seq:
        why = rulings.test_exclusion(unit_case(u))
        if why:
            left_out[u["unit"]] = why
        elif rulings.actions().get(u["unit"], "").startswith("read before"):
            kept.append({**u, "read_before": True})
        else:
            kept.append(u)
    return kept, left_out


def first_pass_units(mode: str) -> set[str]:
    return {unit for p in OUT.glob(f"{mode}_look*/look.json") for unit in json.loads(p.read_text())["units"]}


def population(mode: str) -> Path:
    dest = OUT / f"population_{mode}"
    if dest.exists():
        raise SystemExit(f"{dest} exists")
    ran = first_pass_units(mode)
    record = {"mode": mode, "cells": {}, "left_out": {}, "box_from_first_pass": [], "read_before": []}
    for cell, seq in plan(mode)["cells"].items():
        kept, left_out = population_units(seq)
        record["left_out"].update(left_out)
        record["cells"][cell] = [u["unit"] for u in kept]
        for u in kept:
            if u["domain"] == "box" and u["unit"] in ran:
                record["box_from_first_pass"].append(u["unit"])
                continue
            if u.get("read_before"):
                record["read_before"].append(u["unit"])
            path = dest / u["domain"] / f"{u['unit']}.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(unit_case(u), indent=1, ensure_ascii=False) + "\n")
    record["to_run"] = sorted(p.stem for p in dest.glob("*/*.json"))
    (dest / "population.json").write_text(json.dumps(record, indent=1) + "\n")
    print(f"{mode}: {len(record['to_run'])} units to run, {len(record['box_from_first_pass'])} Box units from the "
          f"first pass, {len(record['left_out'])} left out -> {dest}")
    return dest


def pooled_decision(per_unit: list[tuple[int, int]]) -> dict:
    """The working rule (roadmap, 2026-09-28; fixed before the population runs). `per_unit` holds (failing trials,
    usable trials) for each valid unit with a usable trial. The rate is all failing trials over all usable trials.
    Its one-sided 90% bounds come from a cluster bootstrap: units drawn with replacement, each with all its trials,
    20,000 times, seed 20260928. Policy-level if the 10th percentile is above 0.8; not policy-level if the 90th is
    below 0.8; undecided otherwise."""
    import random
    n = len(per_unit)
    if not n:
        return {"units": 0, "decision": "no usable units"}
    fails, trials = sum(f for f, _ in per_unit), sum(t for _, t in per_unit)
    rng, rates = random.Random(SEED), []
    for _ in range(RESAMPLES):
        f = t = 0
        for _ in range(n):
            a, b = per_unit[rng.randrange(n)]
            f, t = f + a, t + b
        rates.append(f / t)
    rates.sort()
    lo, hi = rates[int(ALPHA * RESAMPLES)], rates[int((1 - ALPHA) * RESAMPLES) - 1]
    decision = ("policy-level" if lo > THRESHOLD else "not policy-level" if hi < THRESHOLD else "undecided")
    return {"units": n, "failing_trials": fails, "usable_trials": trials, "rate": round(fails / trials, 3),
            "p10": round(lo, 3), "p90": round(hi, 3), "decision": decision}


def readings(valid: list[dict], outcomes: dict, looks: list[int]) -> dict:
    """The other ways to read the same verdicts, for the step-5 investigation: the pre-registered sequential rule
    (one pre-chosen trial per unit, looks after 11, 18, 25 and all units, Clopper-Pearson bounds) replayed in the
    fixed order; a unit failing in any of its runs, or in all of them (bounds over units); and every trial as its own
    draw, which overstates the evidence when a unit's runs agree."""
    FAIL, PASS = sampler.FAIL, sampler.PASS
    boundaries = [k for k in looks if k < len(valid)] + [len(valid)]
    sequential = {"decision": "undecided (units exhausted)"}
    for k in boundaries:
        s = sampler.cell_stats(valid[:k], outcomes)
        if s["shown_above"] or s["shown_below"]:
            sequential = {"decision": "policy-level" if s["shown_above"] else "not policy-level", "at_units": k,
                          **{x: s[x] for x in ("draws", "failures", "lower_90", "upper_90")}}
            break
    else:
        s = sampler.cell_stats(valid, outcomes)
        sequential.update({x: s[x] for x in ("draws", "failures", "lower_90", "upper_90")})

    def over_units(rule):
        units = [[o for o in outcomes.get(u["unit"], {}).values() if o in FAIL | PASS] for u in valid]
        draws = [rule(us) for us in units if us]
        k, n = sum(draws), len(draws)
        lo, hi = sampler.lower_bound(k, n, ALPHA), sampler.upper_bound(k, n, ALPHA)
        return {"units": n, "failing": k, "rate": round(k / n, 3) if n else None, "lower_90": round(lo, 3),
                "upper_90": round(hi, 3), "decision": "policy-level" if lo > THRESHOLD else
                "not policy-level" if hi < THRESHOLD else "undecided"}

    trials = [o for u in valid for o in outcomes.get(u["unit"], {}).values() if o in FAIL | PASS]
    k, n = sum(o in FAIL for o in trials), len(trials)
    naive = {"trials": n, "failing": k, "lower_90": round(sampler.lower_bound(k, n, ALPHA), 3) if n else None,
             "upper_90": round(sampler.upper_bound(k, n, ALPHA), 3) if n else None}
    return {"sequential_first_run": sequential, "any_of_runs": over_units(lambda us: any(o in FAIL for o in us)),
            "all_runs": over_units(lambda us: all(o in FAIL for o in us)), "trials_as_draws": naive,
            "spread": sampler.cell_stats(valid, outcomes)["spread"]}


def population_6b(mode: str) -> Path:
    """Roadmap 6b's valid units of one mode (appended by `extend`) as their own cases folder, to run after the
    6a population."""
    dest = OUT / f"population_6b_{mode}"
    if dest.exists():
        raise SystemExit(f"{dest} exists")
    ext = json.loads(EXTENSION.read_text())
    record = {"mode": mode, "units": [], "left_out": {}}
    for cell, seq in ext["cells"].items():
        if not cell.endswith("/" + mode):
            continue
        kept, left_out = population_units(seq)
        record["left_out"].update(left_out)
        for u in kept:
            path = dest / u["domain"] / f"{u['unit']}.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(unit_case(u), indent=1, ensure_ascii=False) + "\n")
            record["units"].append(u["unit"])
    (dest / "population.json").write_text(json.dumps(record, indent=1) + "\n")
    print(f"{mode}: {len(record['units'])} 6b units to run, {len(record['left_out'])} left out -> {dest}")
    return dest


def decide_population(mode: str, verdict_dirs: list[Path], first_pass_dirs: list[Path]) -> dict:
    doc = population_plan(mode)
    outcomes = population_outcomes(verdict_dirs)
    earlier = population_outcomes(first_pass_dirs)
    ran = first_pass_units(mode)
    result = {}
    for cell, seq in doc["cells"].items():
        valid, _ = population_units(seq)
        for u in valid:  # Box units the first pass ran keep its verdicts; nothing else does
            if u["domain"] == "box" and u["unit"] in ran and u["unit"] not in outcomes:
                outcomes[u["unit"]] = earlier.get(u["unit"], {})
        valid = rulings.merge_duplicate_units(valid, outcomes)  # the PI, 2026-09-29: a duplicate pair counts once
        missing = [u["unit"] for u in valid if not outcomes.get(u["unit"])]
        per_unit = []
        for u in valid:
            usable = [o for o in outcomes.get(u["unit"], {}).values() if o in sampler.FAIL | sampler.PASS]
            if usable:
                per_unit.append((sum(o in sampler.FAIL for o in usable), len(usable)))
        decision = pooled_decision(per_unit)
        if missing:
            decision["decision"] = f"incomplete: {len(missing)} valid units without verdicts"
        result[cell] = {"valid_units": len(valid), "missing": missing, **decision,
                        "readings": readings(valid, outcomes, doc["looks"])}
        if any(u.get("source") == "phase4" for u in valid):  # amendment 5: each writer's units apart (and 6b's)
            for name, keep in (("phase3_only", lambda u: u.get("source") not in ("phase4", "completion_01")),
                               ("phase4_only", lambda u: u.get("source") == "phase4"),
                               ("6b_only", lambda u: u.get("source") == "completion_01")):
                part = [u for u in valid if keep(u)]
                pu = [(sum(o in sampler.FAIL for o in us), len(us)) for us in
                      ([o for o in outcomes.get(u["unit"], {}).values() if o in sampler.FAIL | sampler.PASS]
                       for u in part) if us]
                result[cell][name] = {k: v for k, v in pooled_decision(pu).items() if k != "decision"}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    pp = sub.add_parser("population")
    pp.add_argument("mode", choices=["absence", "underspecified"])
    ex = sub.add_parser("extend")
    ex.add_argument("mode", choices=["absence", "underspecified"])
    p6 = sub.add_parser("population-6b")
    p6.add_argument("mode", choices=["absence", "underspecified"])
    dp = sub.add_parser("decide-population")
    dp.add_argument("mode", choices=["absence", "underspecified"])
    dp.add_argument("--verdicts", type=Path, nargs="+", required=True)
    dp.add_argument("--first-pass", type=Path, nargs="*", default=[])
    lk = sub.add_parser("look")
    lk.add_argument("mode", choices=["absence", "underspecified"])
    lk.add_argument("n", type=int, choices=[1, 2, 3, 4])
    lk.add_argument("--cells", nargs="+")
    lk.add_argument("--read", nargs="*", default=[])
    dc = sub.add_parser("decide")
    dc.add_argument("mode", choices=["absence", "underspecified"])
    dc.add_argument("--verdicts", type=Path, nargs="+", required=True)
    args = parser.parse_args()
    if args.cmd == "population":
        population(args.mode)
    elif args.cmd == "extend":
        extend(args.mode)
    elif args.cmd == "population-6b":
        population_6b(args.mode)
    elif args.cmd == "decide-population":
        result = decide_population(args.mode, [p.resolve() for p in args.verdicts],
                                   [p.resolve() for p in args.first_pass])
        (OUT / f"decisions_population_{args.mode}.json").write_text(json.dumps(result, indent=1) + "\n")
        print(json.dumps({c: {k: r[k] for k in ("valid_units", "rate", "p10", "p90", "decision") if k in r}
                          for c, r in result.items()}, indent=1))
    elif args.cmd == "look":
        look(args.mode, args.n, args.cells, set(args.read))
    else:
        result = decide(args.mode, [p.resolve() for p in args.verdicts])
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"decisions_{args.mode}.json").write_text(json.dumps(result, indent=1) + "\n")
        print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
