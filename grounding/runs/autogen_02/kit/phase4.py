"""Phase 4: select the trials to judge and score a generated suite's run, with autogen_01's rules and this study's
triage (effects keyed by the real table key for tests outside autogen_01's folder).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.phase4 select RUN_DIR SUITE [--blind BLIND.json] > trials.json
    python ... phase4 score RUN_DIR SUITE JUDGED [--json OUT]
    python ... phase4 cases SUITE SCENARIO_ID ... > ids.txt     # the case ids of some scenarios, for `solve --cases`
    python ... phase4 policy-cases DEST DROPF_DIR CLONE_DIR PHASE3_DIR SCENARIO_ID ...   # their policy variants

select: every trial that is not mechanically clean, plus 20% of the clean ones (seed 7), as autogen_01.
score: a trial's outcome is judge v2's verdict when judged, else the provisional label (autogen_01's score_run).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import judge as v1
from grounding.runs.autogen_01.kit import score_run
from grounding.runs.autogen_02.kit.judge2 import triage

v1.triage = triage          # select_run looks it up in judge's module
score_run.triage = triage   # trial_outcomes imported it by name


def policy_cases(scenario_ids: set[str], dest: Path, dropf_dir: Path, clone_dir: Path, phase3: Path) -> dict:
    """The policy variants of some Phase 4 scenarios, as one cases folder (amendment 5): every absence twin, every
    accepted drop-F unit (one per distinct condition) and the accepted clone. Units ruled out by the review rule
    (C.9) and units a Phase 3 look already holds are left out."""
    from grounding.runs.autogen_02.kit.population import phase4_scenarios
    from grounding.runs.autogen_02.kit.sampler import absence_units, already_cased, dropf_units, review_exclusion
    ran = already_cased(phase3, "absence") | already_cased(phase3, "underspecified")
    if dest.exists():
        raise SystemExit(f"{dest} exists")
    report = {"absence": [], "underspecified": [], "clone": [], "left_out": {}}

    def put(domain: str, name: str, case: dict, kind: str):
        (dest / domain).mkdir(parents=True, exist_ok=True)
        (dest / domain / f"{name}.json").write_text(json.dumps(case, indent=1, ensure_ascii=False) + "\n")
        report[kind].append(name)

    twins, _ = absence_units([c for c in phase4_scenarios() if c["case_id"] in scenario_ids])
    dunits, _ = dropf_units(dropf_dir)
    for kind, units in (("absence", twins), ("underspecified", [u for u in dunits if u["scenario"] in scenario_ids])):
        for u in units:
            why = review_exclusion(u) or ("already run in a Phase 3 look" if u["unit"] in ran else None)
            if why:
                report["left_out"][u["unit"]] = why
            else:
                put(u["domain"], u["unit"], u["_case"], kind)
    for rec in sorted(clone_dir.glob("UC-*/record.json")):
        r = json.loads(rec.read_text())
        if r.get("scenario") in scenario_ids and r.get("status") == "accepted":
            put(r["domain"], r["id"], json.loads((rec.parent / "variant.json").read_text()), "clone")
    (dest.parent / f"{dest.name}.json").write_text(json.dumps(report, indent=1) + "\n")
    return report


def main():
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "policy-cases":  # policy-cases DEST DROPF_DIR CLONE_DIR PHASE3_DIR SCENARIO_ID ...
        dest, dropf_dir, clone_dir, phase3 = (Path(a).resolve() for a in args[:4])
        rep = policy_cases(set(args[4:]), dest, dropf_dir, clone_dir, phase3)
        print({k: len(v) for k, v in rep.items()})
        return
    if cmd == "select":
        run_dir = Path(args[0]).resolve()
        items = v1.select_run(run_dir, Path(args[1]).resolve())
        if "--blind" in args:  # every trial of the blind sample is judged too, clean or not
            have = {f"{i['run']}/{i['trial']}/{i['case_id']}" for i in items}
            for key in json.loads(Path(args[args.index("--blind") + 1]).read_text())["keys"]:
                run, trial, case_id = key.split("/")
                if key not in have and (run_dir / trial / case_id).exists():
                    items.append({"run_dir": str(run_dir), "run": run, "trial": trial, "case_id": case_id,
                                  "blind_sample": True})
        print(json.dumps(items, indent=1))
    elif cmd == "score":
        result = score_run.score(Path(args[0]).resolve(), Path(args[1]).resolve(), Path(args[2]).resolve())
        if "--json" in args:
            Path(args[args.index("--json") + 1]).write_text(json.dumps(result, indent=1) + "\n")
        print(json.dumps(result.get("all", result), indent=1)[:3000])
    elif cmd == "cases":
        wanted = set(args[1:])
        for t in json.loads(Path(args[0]).read_text()):
            if t.get("scenario") in wanted:
                print(t["case_id"])


if __name__ == "__main__":
    main()
