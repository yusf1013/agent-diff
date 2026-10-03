"""The tests behind grounding/denominator_tables.md, with the case file each one ran from and its trials on record.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.dates_02.kit.population

- Tables 1-3: the 742 tests and units that fill the 948 items (86 covers, 195 packed probes, 131 single-decoy probes
  counted apart from a packed one, 187 absence units, 143 underspecified units; denominator_01's `retained.json`,
  kinds "denominator: ..."), and the 90 boundary tests (boundary_auto_01: round 1's 89 valid requests and round 2's
  LIN-24).
- Table 4: the 105 by-product tests and units (retained.json's origins, four kinds).

Each test's case file is the run suite's (opaque ids; the clock it ran under). Its trials are the attempts recorded
in denominator_01's run folders (OpenClaw only: Qwen and Sol), counted here and listed in affected.json. Writes
numbers/population.json.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import grounding.runs.regen_01.rules  # noqa: F401
from grounding.runs.denominator_01.kit.outcomes import QWEN_RUNS, SOL_RUNS
from grounding.runs.openclaw_eval_01 import rulings
from grounding.runs.report_01.kit.common import RUNS, load

HERE = Path(__file__).resolve().parents[1]
RETAINED = RUNS / "denominator_01/numbers/retained.json"
CASE_FOLDERS = [RUNS / "openclaw_eval_01/suite_opaque/cases", RUNS / "completion_01/suite/cases", RUNS / "regen_01/suite/cases"]
UNIT_FOLDERS = [RUNS / "openclaw_eval_01/suite_opaque/units", RUNS / "completion_01/suite/units", RUNS / "regen_01/suite/units"]
BOUNDARY = RUNS / "boundary_auto_01"
BOUNDARY_INVALID_ROUND1 = ("SLA-34", "CAL-18", "BOX-06", "LIN-24")   # the cold reader's four (summary.json)
BYPRODUCT_ORIGINS = ("the writer's extra decoys on its own facts", "a decoy on a condition outside the brief",
                     "a fact in two briefs by the brief set's design",
                     "the variant builder: one variant per fact of a shared condition")
KIND = {"denominator: cover": "cover", "denominator: packed probe": "packed probe",
        "denominator: single-decoy probe (counted)": "single-decoy probe", "denominator: absence test": "absence",
        "denominator: underspecified test": "underspecified"}


def find(test_id: str, folders) -> Path | None:
    hits = [p for f in folders for p in f.glob(f"*/{test_id}.json")]
    if len(hits) > 1:
        raise SystemExit(f"{test_id}: in more than one suite: {hits}")
    return hits[0] if hits else None


def trials() -> dict[str, list[dict]]:
    """test id -> its recorded attempts on OpenClaw (both agents), with the clock each ran under and the real day."""
    out = defaultdict(list)
    # Qwen's first-round Box tests count from full_02 (Box ids are numbers, so Box kept its run there; the tables'
    # score files read it the same way); its other tests in full_02 were run again with opaque ids in full_03.
    qwen = [(f, None) for f in QWEN_RUNS] + [(RUNS / "openclaw_eval_01/runs/full_02", "box")]
    for agent, folders in (("qwen", qwen), ("sol", [(f, None) for f in SOL_RUNS])):
        for folder, only in folders:
            for s in sorted(folder.glob("*/*/attempt-*/execution_summary.json")):
                x = json.loads(s.read_text())
                if only and x.get("domain") != only:
                    continue
                cfg = s.parent / "solver/config.json"
                clock = (json.loads(cfg.read_text()).get("fake_clock") or {}).get("start") if cfg.exists() else None
                out[x["case_id"]].append({
                    "agent": agent, "run": folder.name, "trial": s.parent.parent.parent.name, "attempt": s.parent.name,
                    "status": x.get("status"), "termination": x.get("termination"), "started": x.get("started_utc"),
                    "clock": clock, "clock_suspects": [k["kind"] for k in (x.get("flags") or {}).get("clock_suspects") or []],
                    "path": str(s.parent.relative_to(RUNS))})
    return out


def population() -> list[dict]:
    R = load(RETAINED)
    rows = []
    for test_id, v in R["qwen"]["tests"].items():
        if v["kind"] in KIND:
            rows.append({"test": test_id, "group": "tables 1-3", "kind": KIND[v["kind"]], "domain": v["domain"],
                         "facts": v["facts"], "path": find(test_id, CASE_FOLDERS)})
    for unit_id, v in R["qwen"]["units"].items():
        if v["kind"] in KIND:
            rows.append({"test": unit_id, "group": "tables 1-3", "kind": KIND[v["kind"]], "domain": v["domain"],
                         "facts": v["facts"], "path": find(unit_id, UNIT_FOLDERS)})
    for test_id, origin in R["origin_of_excluded_muse_tests"].items():
        if origin in BYPRODUCT_ORIGINS:
            v = R["qwen"]["tests"][test_id]
            rows.append({"test": test_id, "group": "table 4", "kind": "by-product test", "origin": origin,
                         "domain": v["domain"], "facts": v["facts"], "path": find(test_id, CASE_FOLDERS)})
    for unit_id, origin in R["origin_of_excluded_muse_units"].items():
        if origin in BYPRODUCT_ORIGINS:
            v = R["qwen"]["units"][unit_id]
            rows.append({"test": unit_id, "group": "table 4", "kind": "by-product unit", "origin": origin,
                         "domain": v["domain"], "facts": v["facts"], "path": find(unit_id, UNIT_FOLDERS)})
    for p in sorted((BOUNDARY / "cases").glob("*/BDA-*.json")):
        element = p.stem.removeprefix("BDA-")
        if element in BOUNDARY_INVALID_ROUND1:
            continue
        rows.append({"test": p.stem, "group": "tables 1-3", "kind": "boundary", "domain": p.parent.name, "facts": [],
                     "path": p})
    rows.append({"test": "BDA-LIN-24-W2", "group": "tables 1-3", "kind": "boundary", "domain": "linear", "facts": [],
                 "path": BOUNDARY / "cases_w2/linear/BDA-LIN-24-W2.json"})
    missing = [r["test"] for r in rows if r["path"] is None or not Path(r["path"]).exists()]
    if missing:
        raise SystemExit(f"no case file for {missing}")
    for r in rows:
        r["scenario"] = rulings.scenario_of(r["test"]) if r["kind"] != "boundary" else r["test"]
        r["path"] = str(Path(r["path"]).relative_to(RUNS))
    return rows


def main():
    rows = population()
    tr = trials()
    for r in rows:
        r["trials"] = len(tr.get(r["test"], []))      # the trials themselves are in affected.json
    counts = Counter((r["group"], r["kind"]) for r in rows)
    print(json.dumps({f"{g}: {k}": n for (g, k), n in sorted(counts.items())}, indent=1))
    print("tests:", len(rows), " scenarios:", len({r["scenario"] for r in rows if r["kind"] != "boundary"}),
          " trials:", sum(r["trials"] for r in rows))
    (HERE / "numbers/population.json").write_text(json.dumps(rows, indent=1) + "\n")


if __name__ == "__main__":
    main()
