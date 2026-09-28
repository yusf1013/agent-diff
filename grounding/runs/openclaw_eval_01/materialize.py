"""The frozen generated suite for the final evaluation (roadmap step 6a), written with the frozen kit (tag
grounding-freeze-01). No model or replica calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.materialize

For each of the 78 accepted generated scenarios (autogen_01's arms R, P and P v2; autogen_02's Phase 4):
- **The case** is the recorded `case.json`, as accepted. It carries the reader's contestable flags, which the
  orchestrator adds after the build.
- **G4-CAL-06** is the exception. Step 3's time-zone fix changes its seed, so it is rebuilt from its last scenario
  version with the frozen kit, and the recorded case's reader flags are applied again, by decoy witness.
- **Its suite** comes from the frozen derivation (`derive.suite_with_dropped`), written as the orchestrator writes
  it.

Checks (written to suite/check.json; any failure stops before the suite is written):
1. **Recorded suite:** every test of the other 77 scenarios is byte-identical to the recorded suite file. The tests
   no longer there are exactly the ones the derivation drops.
2. **Qwen's runs:** every test Qwen ran (autogen_01's solve runs, Phase 4's two batches) that is still in the suite
   has the case_sha256 recorded in that run's plan.
3. **G4-CAL-06:** the rebuilt case differs from the recorded one only in its events' start and end (zone and
   offset) and in its digest.
"""
from __future__ import annotations

import copy
import json
import re
import shutil
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, scenario

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
SUITE = HERE / "suite"
SOURCES = {  # generation run -> the solve runs that ran its tests on Qwen
    "autogen_01/runs/gen_arm_r": ["autogen_01/runs/solve_arm_r"],
    "autogen_01/runs/gen_arm_p": ["autogen_01/runs/solve_arm_p"],
    "autogen_01/runs/gen_arm_p_v2": ["autogen_01/runs/solve_arm_p_v2"],
    "autogen_02/runs/phase4_gen": ["autogen_02/runs/phase4/solve_phase4_batch1", "autogen_02/runs/phase4/solve_phase4_batch2"],
}
REBUILT = {"G4-CAL-06"}  # scenarios whose case step 3 changes


def text(test: dict) -> str:
    return json.dumps(test, indent=1, ensure_ascii=False) + "\n"


def latest_version(folder: Path) -> Path:
    versions = sorted(folder.glob("scenario-v*.json"), key=lambda p: int(re.search(r"v(\d+)", p.name).group(1)))
    return versions[-1]


def rebuild(folder: Path, recorded: dict) -> dict:
    """The scenario rebuilt with the frozen kit, with the recorded reader flags applied by witness."""
    s = json.loads(latest_version(folder).read_text())
    brief = {"scenario_id": s["scenario_id"], "domain": s["domain"],
             "facts": sorted({d["fact"] for d in s["reference"]["decoys"]})}
    case, problems = scenario.build(s, brief)
    if case is None or problems:
        raise SystemExit(f"{folder.name}: the frozen kit does not build it: {problems}")
    flags = {str(c["witness"]): c["contestable"] for c in recorded["references"][0]["claims"] if c.get("contestable")}
    for claim in case["references"][0]["claims"]:
        if str(claim["witness"]) in flags:
            claim["contestable"] = flags[str(claim["witness"])]
    return case


def differences(a, b, path="") -> list[str]:
    """JSON paths where a and b differ."""
    if isinstance(a, dict) and isinstance(b, dict):
        return [d for k in sorted(set(a) | set(b)) for d in differences(a.get(k), b.get(k), f"{path}.{k}")]
    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        return [d for i, (x, y) in enumerate(zip(a, b)) for d in differences(x, y, f"{path}[{i}]")]
    return [] if a == b else [path]


def ran_on_qwen() -> dict[str, set[str]]:
    """case id -> the case_sha256 values Qwen's runs recorded for it."""
    out: dict[str, set[str]] = {}
    for solves in SOURCES.values():
        for run in solves:
            for plan in sorted((RUNS / run).glob("t*/plan.json")):
                for case_id, sha in json.loads(plan.read_text())["cases"].items():
                    out.setdefault(case_id, set()).add(sha)
    return out


def main():
    qwen = ran_on_qwen()
    tests, dropped, check = [], [], {"scenarios": 0, "tests": 0, "identical_to_recorded": 0, "ran_on_qwen": 0,
                                     "rebuilt": {}, "failures": []}
    fail = check["failures"].append
    for source in SOURCES:
        gen = RUNS / source
        for case_path in sorted(gen.glob("*/case.json")):
            folder = case_path.parent
            recorded = json.loads(case_path.read_text())
            sid = recorded["case_id"]
            check["scenarios"] += 1
            if sid in REBUILT:
                case = rebuild(folder, recorded)
                diff = differences(recorded, case)
                allowed = [d for d in diff if d == ".case_sha256" or
                           re.fullmatch(r"\.seed\.calendar_events\[\d+\]\.(start|end)\.(dateTime|timeZone)", d)]
                if len(allowed) != len(diff) or not allowed:
                    fail(f"{sid}: rebuilt case differs outside the events' zones: {sorted(set(diff) - set(allowed))}")
                check["rebuilt"][sid] = diff
            else:
                case = copy.deepcopy(recorded)
            kept, gone = derive.suite_with_dropped(case)
            recorded_files = {p.stem: p for p in (gen / "cases" / recorded["domain"]).glob("*.json")
                              if p.stem == sid or re.sub(r"^(FP|P)-", "", p.stem).startswith(sid + "-")}
            for test, meta in kept:
                cid = test["case_id"]
                check["tests"] += 1
                if sid not in REBUILT:
                    path = recorded_files.get(cid)
                    if path is None:
                        fail(f"{cid}: not in the recorded suite")
                    elif path.read_text() != text(test):
                        fail(f"{cid}: differs from the recorded suite file")
                    else:
                        check["identical_to_recorded"] += 1
                if cid in qwen:
                    check["ran_on_qwen"] += 1
                    if sid not in REBUILT and qwen[cid] != {test["case_sha256"]}:
                        fail(f"{cid}: Qwen's runs recorded {sorted(qwen[cid])}, the suite has {test['case_sha256']}")
                tests.append((test, {"case_id": cid, "domain": case["domain"], **meta, "source": source,
                                     "ran_on_qwen": cid in qwen}))
            dropped += [{"case_id": t["case_id"], "domain": case["domain"], **m, "source": source} for t, m in gone]
            missing = set(recorded_files) - {t["case_id"] for t, _ in kept} - {t["case_id"] for t, _ in gone}
            if missing:
                fail(f"{sid}: recorded tests the derivation no longer produces: {sorted(missing)}")
    check["dropped"] = sorted(d["case_id"] for d in dropped)
    print(json.dumps({k: v for k, v in check.items() if k != "rebuilt"}, indent=1))
    if check["failures"]:
        raise SystemExit("checks failed; nothing written")
    if SUITE.exists():
        shutil.rmtree(SUITE)
    for test, _ in tests:
        path = SUITE / "cases" / test["domain"] / f"{test['case_id']}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text(test))
    index = sorted((m for _, m in tests), key=lambda m: m["case_id"])
    (SUITE / "suite.json").write_text(json.dumps(index, indent=1) + "\n")
    (SUITE / "suite_dropped.json").write_text(json.dumps(sorted(dropped, key=lambda d: d["case_id"]), indent=1) + "\n")
    (SUITE / "check.json").write_text(json.dumps(check, indent=1) + "\n")
    print(f"{len(tests)} tests from {check['scenarios']} scenarios -> {SUITE.relative_to(RUNS.parents[1])}")


if __name__ == "__main__":
    main()
