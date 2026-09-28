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
from grounding.runs.openclaw_eval_01 import run as runner
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


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    lk = sub.add_parser("look")
    lk.add_argument("mode", choices=["absence", "underspecified"])
    lk.add_argument("n", type=int, choices=[1, 2, 3, 4])
    lk.add_argument("--cells", nargs="+")
    lk.add_argument("--read", nargs="*", default=[])
    dc = sub.add_parser("decide")
    dc.add_argument("mode", choices=["absence", "underspecified"])
    dc.add_argument("--verdicts", type=Path, nargs="+", required=True)
    args = parser.parse_args()
    if args.cmd == "look":
        look(args.mode, args.n, args.cells, set(args.read))
    else:
        result = decide(args.mode, [p.resolve() for p in args.verdicts])
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"decisions_{args.mode}.json").write_text(json.dumps(result, indent=1) + "\n")
        print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
