"""Qwen's suite: its accepted scenarios (cases.py: one per brief, from runs/gen_02 or runs/gen_04) with opaque ids and
test-side clocks, built exactly as
regen_01/suite.py builds Muse's new scenarios (completion_01's method, itself openclaw_eval_01/opaque_suite.py's). No
model or replica calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.qwen_writer_01.suite

For each accepted scenario (skipped: those this study's rulings leave out, rules.py):
1. **The recorded suite:** the frozen derivation (`derive.suite_with_dropped`) of the accepted case must equal the
   suite the orchestrator wrote (runs/gen_NN/cases/), test by test.
2. **Opaque ids:** one mapping per scenario (`autogen_01/kit/opaque_ids.py`). The derivation from the obfuscated case
   must equal the obfuscated suite, test by test, with the same drops, and every test passes `opaque_ids.check`.
   Box's ids are numbers already and come out unchanged.
3. **The clock** (not Calendar's, whose tests run on June 17, 2018): the moment the accepted version was written
   (the scenario's last writer call), or, when its data has a later event, a day after that event
   (completion_01/suite.py's `clock_for`).

Writes suite/: cases/<domain>/, cases/suite.json (the index), ids/<scenario>.json (old id -> new id), check.json.
Any failure stops before anything is written.
"""
from __future__ import annotations

import json
import re
import shutil

from grounding.runs.qwen_writer_01 import cases, rules  # rules before anything reads the rulings
from grounding.runs.autogen_01.kit import derive, opaque_ids
from grounding.runs.autogen_01.kit.derive import digest
from grounding.runs.completion_01.suite import clock_for, written_at
from grounding.runs.openclaw_eval_01 import materialize, rulings

HERE = rules.HERE
OUT = HERE / "suite"


def main():
    check = {"scenarios": 0, "tests": 0, "dropped": [], "ids_replaced": 0, "clocks": {}, "skipped": {}, "failures": []}
    fail = check["failures"].append
    tests_out, index, mappings = [], [], {}
    for sid, folder in cases.accepted().items():
        GEN = folder.parent
        written = written_at(GEN)
        action = rulings.actions().get(sid, "keep")
        if action.startswith("leave out"):
            check["skipped"][sid] = f"ruling: {action}"
            continue
        case = json.loads((folder / "case.json").read_text())
        check["scenarios"] += 1
        kept, gone = derive.suite_with_dropped(case)
        recorded = {p.stem: p for p in (GEN / "cases" / case["domain"]).glob("*.json")
                    if p.stem == sid or re.sub(r"^(FP|P)-", "", p.stem).startswith(sid + "-")}
        for test, _ in kept:
            path = recorded.get(test["case_id"])
            if path is None or path.read_text() != materialize.text(test):
                fail(f"{test['case_id']}: differs from the recorded suite")
        mapping = opaque_ids.mapping_for(sid, [case] + [t for t, _ in kept])
        mappings[sid] = {"scenario": sid, "domain": case["domain"], "ids": mapping}
        check["ids_replaced"] += len(mapping)
        try:
            opaque_case = opaque_ids.obfuscate(case, sid, mapping)
        except ValueError as exc:
            fail(str(exc))
            continue
        kept_o, gone_o = derive.suite_with_dropped(opaque_case)
        derived = {t["case_id"]: t for t, _ in kept_o}
        if {t["case_id"] for t, _ in gone_o} != {t["case_id"] for t, _ in gone}:
            fail(f"{sid}: the obfuscated case drops different tests")
        check["dropped"] += [t["case_id"] for t, _ in gone]
        clock = clock_for(case, written[sid]) if sid in written else None
        if case["domain"] != "calendar" and clock is None:
            fail(f"{sid}: no writer call recorded for its clock")
        if clock:
            check["clocks"][sid] = clock
        for test, meta in kept:
            check["tests"] += 1
            opaque = opaque_ids.obfuscate(test, sid, mapping)
            problems = opaque_ids.check(test, opaque, mapping)
            if derived.get(test["case_id"]) != opaque:
                problems.append(f"derivation does not commute: {materialize.differences(opaque, derived.get(test['case_id'], {}))[:6]}")
            for p in problems:
                fail(f"{test['case_id']}: {p}")
            if clock:
                opaque = {**opaque, "clock": {"now": clock["now"]}}
                opaque["case_sha256"] = digest({k: v for k, v in opaque.items() if k != "case_sha256"})
            tests_out.append(opaque)
            index.append({"case_id": test["case_id"], "domain": case["domain"], **meta,
                          "source": f"qwen_writer_01/runs/{GEN.name}", "writer": "qwen3.8-27b",
                          "case_sha256": opaque["case_sha256"]})
    print(json.dumps({k: v for k, v in check.items() if k not in ("failures", "clocks")}, indent=1))
    if check["failures"]:
        for f in check["failures"][:60]:
            print("FAIL", f)
        raise SystemExit(f"{len(check['failures'])} failures; nothing written")
    for sub in ("cases", "ids"):
        if (OUT / sub).exists():
            shutil.rmtree(OUT / sub)
    for t in tests_out:
        path = OUT / "cases" / t["domain"] / f"{t['case_id']}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(t, indent=1, ensure_ascii=False) + "\n")
    (OUT / "cases" / "suite.json").write_text(json.dumps(sorted(index, key=lambda m: m["case_id"]), indent=1) + "\n")
    for sid, m in mappings.items():
        path = OUT / "ids" / f"{sid}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(m, indent=1) + "\n")
    (OUT / "check.json").write_text(json.dumps(check, indent=1) + "\n")
    print(f"{len(tests_out)} tests from {check['scenarios']} scenarios -> {OUT.relative_to(HERE.parent)}")


if __name__ == "__main__":
    main()
