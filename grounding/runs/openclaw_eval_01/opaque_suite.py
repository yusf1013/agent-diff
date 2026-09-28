"""The suite with opaque ids and test-side clocks (the discussion after 6a, 2026-09-28): the frozen suite and every
policy unit, each scenario's made-up ids replaced by `autogen_01/kit/opaque_ids.py`. No model or replica calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.opaque_suite

For each of the 78 scenarios:
1. **One mapping** over its accepted case, its suite tests and its policy units (the units in autogen_02's plans;
   G4-CAL-06's are first rebuilt, as `policy.rebuilt_unit` does).
2. **Commutation:** the suite the frozen derivation (`derive.suite_with_dropped`) builds from the obfuscated case
   equals the obfuscated suite, test by test, and drops the same tests. The derivation and its witness check see
   the same scenario under either ids.
3. **Each test and unit** passes `opaque_ids.check`: the request unchanged, only ids changed, none left, and the
   reference check selecting and crediting the same records under their new ids.
4. **Clocks** (known_defects.json, `clocks`): the scenario's tests and units get `clock` (the instant the agent's
   clock starts at) and a new digest.

Writes suite_opaque/: cases/<domain>/ (with suite.json, the suite's index), units/<domain>/, ids/<scenario>.json
(old id -> new id) and check.json. Box's ids are numbers already, so its tests come out unchanged. Any failure stops
before anything is written.
"""
from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, opaque_ids
from grounding.runs.autogen_01.kit.derive import digest
from grounding.runs.openclaw_eval_01 import materialize, policy, run as runner

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
SUITE = HERE / "suite"
OUT = HERE / "suite_opaque"
PHASE3 = RUNS / "autogen_02" / "runs" / "phase3"


def accepted_cases() -> dict[str, dict]:
    """scenario -> its accepted case, as materialize.py takes it (G4-CAL-06 rebuilt)."""
    out = {}
    for source in materialize.SOURCES:
        for case_path in sorted((RUNS / source).glob("*/case.json")):
            recorded = json.loads(case_path.read_text())
            sid = recorded["case_id"]
            out[sid] = materialize.rebuild(case_path.parent, recorded) if sid in materialize.REBUILT else recorded
    return out


def plan_units() -> dict[str, list[tuple[dict, dict]]]:
    """scenario -> [(plan entry, unit case)] for every unit in the two plans."""
    out: dict[str, list] = {}
    for mode in ("absence", "underspecified"):
        for seq in policy.plan(mode)["cells"].values():
            for u in seq:
                recorded = json.loads((PHASE3 / "units" / u["domain"] / f"{u['unit']}.json").read_text())
                case = policy.rebuilt_unit(u, recorded) if u["scenario"] in policy.REBUILT else recorded
                out.setdefault(u["scenario"], []).append((u, case))
    return out


def clocks() -> dict[str, dict]:
    doc = json.loads(runner.KNOWN_DEFECTS.read_text())
    return {c["scenario"]: {"now": c["now"], "why": c["why"]} for c in doc.get("clocks", [])}


def with_clock(case: dict, clock: dict | None) -> dict:
    if not clock:
        return case
    case = {**case, "clock": {"now": clock["now"]}}
    case["case_sha256"] = digest({k: v for k, v in case.items() if k != "case_sha256"})
    return case


def main():
    index = json.loads((SUITE / "suite.json").read_text())
    tests_by_scenario: dict[str, list[dict]] = {}
    for meta in index:
        test = json.loads((SUITE / "cases" / meta["domain"] / f"{meta['case_id']}.json").read_text())
        tests_by_scenario.setdefault(meta["scenario"], []).append(test)
    dropped_recorded = {d["case_id"] for d in json.loads((SUITE / "suite_dropped.json").read_text())}
    cases, units, times = accepted_cases(), plan_units(), clocks()
    check = {"scenarios": 0, "tests": 0, "units": 0, "unchanged_tests": 0, "ids_replaced": 0, "clocks": {},
             "failures": []}
    fail = check["failures"].append
    written_tests, written_units, mappings = [], [], {}
    for sid, case in sorted(cases.items()):
        check["scenarios"] += 1
        tests = tests_by_scenario.get(sid, [])
        scenario_units = units.get(sid, [])
        mapping = opaque_ids.mapping_for(sid, [case] + tests + [c for _, c in scenario_units])
        mappings[sid] = {"scenario": sid, "domain": case["domain"], "ids": mapping}
        check["ids_replaced"] += len(mapping)
        try:
            opaque_case = opaque_ids.obfuscate(case, sid, mapping)
        except ValueError as exc:
            fail(str(exc))
            continue
        kept, gone = derive.suite_with_dropped(opaque_case)
        derived = {t["case_id"]: t for t, _ in kept}
        if {t["case_id"] for t, _ in gone} != {d for d in dropped_recorded if d.startswith(("P-" + sid + "-", "FP-" + sid + "-"))}:
            fail(f"{sid}: the obfuscated case drops {sorted(t['case_id'] for t, _ in gone)}")
        if set(derived) != {t["case_id"] for t in tests}:
            fail(f"{sid}: derived tests {sorted(set(derived) ^ {t['case_id'] for t in tests})} differ")
        for test in tests:
            check["tests"] += 1
            opaque = opaque_ids.obfuscate(test, sid, mapping)
            problems = opaque_ids.check(test, opaque, mapping)
            if derived.get(test["case_id"]) != opaque:
                diff = materialize.differences(opaque, derived.get(test["case_id"], {}))
                problems.append(f"derivation does not commute: {diff[:6]}")
            for p in problems:
                fail(f"{test['case_id']}: {p}")
            check["unchanged_tests"] += opaque == test
            written_tests.append(with_clock(opaque, times.get(sid)))
        for u, unit in scenario_units:
            check["units"] += 1
            opaque = opaque_ids.obfuscate(unit, sid, mapping)
            for p in opaque_ids.check(unit, opaque, mapping):
                fail(f"{u['unit']}: {p}")
            written_units.append(with_clock(opaque, times.get(sid)))
        if sid in times:
            check["clocks"][sid] = times[sid]
    missing = set(times) - set(cases)
    if missing:
        fail(f"clocks for unknown scenarios: {sorted(missing)}")
    print(json.dumps({k: v for k, v in check.items() if k != "failures"}, indent=1))
    if check["failures"]:
        for f in check["failures"][:60]:
            print("FAIL", f)
        raise SystemExit(f"{len(check['failures'])} failures; nothing written")
    if OUT.exists():
        shutil.rmtree(OUT)
    for folder, cases_out in (("cases", written_tests), ("units", written_units)):
        for c in cases_out:
            path = OUT / folder / c["domain"] / f"{c['case_id']}.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(c, indent=1, ensure_ascii=False) + "\n")
    shas = {c["case_id"]: c["case_sha256"] for c in written_tests}
    (OUT / "cases" / "suite.json").write_text(json.dumps(
        [{**m, "case_sha256": shas[m["case_id"]]} for m in index], indent=1) + "\n")
    for sid, m in mappings.items():
        path = OUT / "ids" / f"{sid}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(m, indent=1) + "\n")
    (OUT / "check.json").write_text(json.dumps(check, indent=1) + "\n")
    print(f"{len(written_tests)} tests and {len(written_units)} units -> {OUT.relative_to(RUNS.parents[1])}")


if __name__ == "__main__":
    main()
