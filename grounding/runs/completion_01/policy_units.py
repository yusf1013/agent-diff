"""Roadmap 6b's policy units, built as 6a's were: the absence twins of the accepted scenarios (autogen_02's
mechanical derivation, `sampler.absence_units`) and, with --dropf DIR [DIR ...], the accepted drop-F variants of
derivation runs on Muse (`sampler.dropf_units`, one unit per dropped condition; a condition an earlier run already
derived is the same test). Every accepted variant must have my read in eval/variant_review.json, and one I read as
invalid must be left out by the rulings. Each unit gets its scenario's opaque ids (the mapping in suite/ids/,
extended by any id only the unit holds) and clock, and must pass `opaque_ids.check`. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.completion_01.policy_units [--dropf DIR ...]

Writes suite/units/<domain>/<unit>.json and suite/units.json: every unit with its mode, scenario and facts, the ones
the derivation excluded and why, and the ones the rulings leave out (`openclaw_eval_01/rulings.py`).
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from grounding.runs.autogen_01.kit import opaque_ids
from grounding.runs.autogen_01.kit.derive import digest, normalize_effects
from grounding.runs.autogen_02.kit import sampler
from grounding.runs.openclaw_eval_01 import rulings

HERE = Path(__file__).resolve().parent
GEN = HERE / "runs" / "gen_01"
SUITE = HERE / "suite"
REVIEW = HERE / "eval" / "variant_review.json"


def accepted_cases() -> list[dict]:
    out = []
    for outcome in sorted(q for gen in sorted((HERE / "runs").glob("gen_*")) for q in gen.glob("*/outcome.json")):
        if json.loads(outcome.read_text()).get("status") != "accepted":
            continue
        case = json.loads((outcome.parent / "case.json").read_text())
        case["_arm"] = "completion_01"
        out.append(normalize_effects(case))
    return out


def dropf_units(dirs: list[Path]) -> tuple[list[dict], list[dict]]:
    """`sampler.dropf_units` over several derivation runs, in order (dropf_02 derived again the jobs whose variant a
    colliding job overwrote in dropf_01). A condition an earlier run already derived is the same test."""
    units, excluded, seen = [], [], {}
    for folder in dirs:
        more, more_excluded = sampler.dropf_units(folder)
        for u in more:
            record = json.loads((folder / u["unit"] / "record.json").read_text())
            key = (u["scenario"], tuple(record.get("dropped_keys") or []))
            if key in seen:
                seen[key]["also_for"] = seen[key].get("also_for", []) + [record["fact"]]
                continue
            seen[key] = u
            units.append(u)
        excluded += more_excluded
    return units, excluded


def unread(units: list[dict]) -> list[str]:
    """The drop-F units without my read, or read as invalid and not left out by the rulings."""
    reads = json.loads(REVIEW.read_text())["dropf"] if REVIEW.exists() else {}
    out = []
    for u in units:
        read = reads.get(u["unit"])
        if read is None:
            out.append(f"{u['unit']}: not read")
        elif not read["valid"] and not rulings.test_exclusion(u["_case"]):
            out.append(f"{u['unit']}: read as invalid but the rulings keep it (add it to known_defects)")
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dropf", type=Path, nargs="+", default=[])
    args = parser.parse_args()
    check = json.loads((SUITE / "check.json").read_text())
    units, excluded = sampler.absence_units(accepted_cases())
    if args.dropf:
        more, more_excluded = dropf_units([d.resolve() for d in args.dropf])
        problems = unread(more)
        if problems:
            raise SystemExit("drop-F variants not cleared by my read:\n" + "\n".join(problems))
        units, excluded = units + more, excluded + more_excluded
    failures, written, left_out = [], [], {}
    for u in units:
        sid = u["scenario"]
        path = SUITE / "ids" / f"{sid}.json"
        doc = json.loads(path.read_text())
        mapping = dict(doc["ids"])
        extra = {k: v for k, v in opaque_ids.mapping_for(sid, [u["_case"]]).items() if k not in mapping}
        if extra:
            mapping.update(extra)
            doc["ids"] = dict(sorted(mapping.items()))
            path.write_text(json.dumps(doc, indent=1) + "\n")
        opaque = opaque_ids.obfuscate(u["_case"], sid, mapping)
        failures += [f"{u['unit']}: {p}" for p in opaque_ids.check(u["_case"], opaque, mapping)]
        clock = check["clocks"].get(sid)
        if clock:
            opaque = {**opaque, "clock": {"now": clock["now"]}}
            opaque["case_sha256"] = digest({k: v for k, v in opaque.items() if k != "case_sha256"})
        why = rulings.test_exclusion(opaque)
        if why:
            left_out[u["unit"]] = why
        written.append((u, opaque))
    if failures:
        for f in failures[:40]:
            print("FAIL", f)
        raise SystemExit(f"{len(failures)} failures; nothing written")
    out = SUITE / "units"
    if out.exists():
        shutil.rmtree(out)
    for u, case in written:
        p = out / u["domain"] / f"{u['unit']}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(case, indent=1, ensure_ascii=False) + "\n")
    (SUITE / "units.json").write_text(json.dumps({
        "units": [{k: v for k, v in u.items() if k != "_case"} for u, _ in written],
        "excluded_by_derivation": [{k: v for k, v in e.items() if k != "_case"} for e in excluded],
        "left_out_by_rulings": left_out}, indent=1) + "\n")
    print(f"{len(written)} units ({sum(u['mode'] == 'absence' for u, _ in written)} absence, "
          f"{sum(u['mode'] == 'underspecified' for u, _ in written)} underspecified); {len(excluded)} excluded by "
          f"the derivation; {len(left_out)} left out by the rulings")


if __name__ == "__main__":
    main()
