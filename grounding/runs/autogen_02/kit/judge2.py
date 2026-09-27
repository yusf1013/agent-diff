"""Judge v2 (autogen_02): autogen_01's judge with explicit rules for the policy tests, run on Muse (decision N13).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.judge2 select --runs RUN_DIR ... > trials.json
    AUTOGEN_BACKEND=muse python ... judge2 run --trials trials.json --out DIR [--concurrency 4]
    python ... judge2 select-panel > panel.json    # fact_coverage_02's 24 labelled P1/P3 trials
    python ... judge2 compare --out DIR --labels LABELS.json [LABELS.json ...]

What changes from v1 (kit/prompts/judge_v2.md; v1 stays frozen in autogen_01):
- the prompt's "Policy tests" section: the absence test (per-fact twin, or fact_coverage_02's panel P1) and the
  underspecified test (drop-F, clone, or the panel's P3), with correct and failing behaviour for each;
- the test form is named for the new variants (by case-id prefix: `AT-` absence twin, `U-`/`UC-` underspecified), and
  the bundle lists every full match as TARGET (the variant's expected set);
- the replica notes are autogen_02's (`inputs/<domain>/replica.md`), which add the gaps autogen_01 found.

Labels are read only by `compare`. Verdicts are cached per attempt, as in v1.
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from grounding.runs.autogen_01.kit import agent, bundle
from grounding.runs.autogen_01.kit import judge as v1

KIT = Path(__file__).resolve().parent
STUDY = KIT.parent
PROMPT = KIT / "prompts" / "judge_v2.md"
INPUTS = STUDY / "inputs"
WORKSPACES = Path("/tmp/autogen-02/ws/judge")
FORMS = {"AT-": "absence twin (no target; the request presupposes one, with no escape clause)",
         "UC-": "underspecified (several records fully meet the singular request; each is listed as TARGET)",
         "U-": "underspecified (several records fully meet the singular request; each is listed as TARGET)"}


GENERATED = ("AR-", "AP-", "AP2-", "G4-")


def generated(case_id: str) -> bool:
    """A test derived from a generated scenario (autogen_01's arms, or Phase 4), whatever its variant prefix."""
    stem = case_id
    for prefix in ("AT-", "UC-", "U-", "FP-", "P-"):
        if stem.startswith(prefix):
            stem = stem[len(prefix):]
            break
    return stem.startswith(GENERATED)


def triage(run_name: str, trial: str, attempt: Path) -> tuple[dict, dict, dict]:
    """v1's triage, with effects keyed by each table's real key for every generated scenario. v1 does this only
    for tests under autogen_01's folder; Phases 3 and 4 run generated tests from this study's folder."""
    import json as _json
    from grounding.runs.autogen_01.kit.derive import normalize_effects
    from grounding.runs.fact_coverage_01.pilot import analyze as pilot
    from grounding.runs.fact_coverage_02 import score
    from grounding.runs.fact_coverage_02.analyze import current
    summary = _json.loads((attempt / "execution_summary.json").read_text())
    case = current(_json.loads((attempt / "case.json").read_text()))
    if generated(case["case_id"]) or v1.STUDY in attempt.resolve().parents:
        normalize_effects(case)
    row = {"run": run_name, "trial": trial, "case_id": summary["case_id"], "status": summary.get("status")}
    if summary.get("status") == "completed":
        row.update(pilot.attribute(case, attempt))
    result = score.classify(row, case, {}, attempt)
    return case, summary, {"references": row.get("references", []), "outcome": result["outcome"],
                           "exposed": result["exposed"]}


def form_of(case_id: str) -> str | None:
    for prefix, form in FORMS.items():
        if case_id.startswith(prefix):
            return form
    return None


def kind(form: str | None, targets: int) -> str:
    """absence, underspecified, or regular."""
    f = form or ""
    if f.startswith("absence") or (f == "policy panel" and targets == 0):
        return "absence"
    if f.startswith("underspecified") or (f == "policy panel" and targets > 1):
        return "underspecified"
    return "regular"


def select(run_dirs: list[Path]) -> list[dict]:
    items = []
    for run_dir in run_dirs:
        for summary in sorted(run_dir.glob("t*/*/attempt-*/execution_summary.json")):
            attempt = summary.parent
            trial, case_id = attempt.parts[-3], attempt.parts[-2]
            if attempt != v1.latest(run_dir, trial, case_id):
                continue
            items.append({"run_dir": str(run_dir), "run": run_dir.name, "trial": trial, "case_id": case_id})
    return items


FC2_RUNS = STUDY.parent / "fact_coverage_02" / "runs"
PANEL = {"method_pilot_panel": ["BOX-01-A", "CAL-06-A", "LIN-01-A"], "method_new_slk21": ["SLK-21-A"],
         "method_pilot": ["BOX-01-TWIN", "CAL-09-TWIN", "LIN-15-TWIN"], "method_new": ["SLK-23-TWIN"]}


def select_panel() -> list[dict]:
    """fact_coverage_02's P1 and P3 policy-panel trials with manual labels (24), judged as form "policy panel"."""
    items = []
    for run, cases in PANEL.items():
        for case_id in cases:
            for trial in ("t1", "t2", "t3"):
                items.append({"run_dir": str(FC2_RUNS / run), "run": run, "trial": trial, "case_id": case_id,
                              "form": "policy panel"})
    return items


def judge_one(item: dict, out: Path, calls_log: Path) -> dict:
    run_dir = Path(item["run_dir"])
    attempt = v1.latest(run_dir, item["trial"], item["case_id"])
    dest = out / item["run"] / item["trial"] / item["case_id"]
    verdict_path = dest / "verdict.json"
    if verdict_path.exists():
        old = json.loads(verdict_path.read_text())
        if old.get("attempt") == str(attempt):
            return old
        verdict_path.rename(dest / f"verdict-{Path(old.get('attempt', 'unknown')).name}.json")
    case, summary, tri = triage(item["run"], item["trial"], attempt)
    # The policy concerns the record the request acts on (the first reference); another reference, such as the
    # workflow state an issue moves to, may also have a target.
    targets = len(case["references"][0]["expected"])
    form = item.get("form") or form_of(case["case_id"]) or (
        "cover (target and all decoys)" if targets else "no-target test with all of the scenario's decoys")
    text = bundle.build(case, attempt, form, tri, summary)
    system = PROMPT.read_text() + "\n\n# Replica notes for this domain\n\n" + \
        (INPUTS / case["domain"] / "replica.md").read_text()
    result = agent.run(agent.Call(
        role="judge", workspace=WORKSPACES / out.name / f"{item['run']}-{item['trial']}-{item['case_id']}",
        prompt=text + "\n\nGive your verdict for this trial.", log_dir=dest, calls_log=calls_log, tools=[],
        schema=v1.SCHEMA, system_append=system, label=f"{item['run']}/{item['trial']}/{item['case_id']}"))
    verdict = agent.structured(result) or {}
    verdict.update(key=f"{item['run']}/{item['trial']}/{item['case_id']}", attempt=str(attempt),
                   provisional=tri["outcome"], provisional_exposed=tri["exposed"], form=form, targets=targets,
                   kind=kind(form, targets), judge="v2", backend=result.get("backend", "claude"))
    dest.mkdir(parents=True, exist_ok=True)
    verdict_path.write_text(json.dumps(verdict, indent=1, ensure_ascii=False) + "\n")
    return verdict


def run(trials: list[dict], out: Path, concurrency: int):
    out.mkdir(parents=True, exist_ok=True)
    prompt = PROMPT.read_text()
    frozen = out / "judge_prompt.md"
    if frozen.exists() and frozen.read_text() != prompt:
        raise SystemExit(f"{out} was judged with another prompt version; use a new --out")
    frozen.write_text(prompt)
    calls_log = out / "calls.jsonl"
    done = 0
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(judge_one, t, out, calls_log): t for t in trials}
        for fut in as_completed(futures):
            t = futures[fut]
            done += 1
            try:
                v = fut.result()
                print(f"[{done}/{len(trials)}] {v['key']}: {v.get('outcome')} {v.get('exposed')}", flush=True)
            except Exception as exc:
                print(f"[{done}/{len(trials)}] {t['run']}/{t['trial']}/{t['case_id']}: FAILED {exc}", flush=True)


def compare(out: Path, label_files: list[Path]) -> dict:
    labels = {}
    for f in label_files:
        labels.update({k: v for k, v in json.loads(f.read_text()).items() if not k.startswith("_")})
    rows = []
    for path in sorted(out.glob("*/*/*/verdict.json")):
        v = json.loads(path.read_text())
        ref = labels.get(v["key"])
        if not ref:
            continue
        rows.append({"key": v["key"], "kind": v.get("kind"), "ref": ref["outcome"], "judge": v.get("outcome"),
                     "ref_exposed": sorted(ref.get("exposed", [])), "judge_exposed": sorted(v.get("exposed", [])),
                     "note": v.get("note", "")[:300], "ref_note": ref.get("note", "")[:300]})
    collapsed = [r for r in rows if v1.COLLAPSE.get(r["ref"], r["ref"]) == v1.COLLAPSE.get(r["judge"], r["judge"])]
    by_kind = {}
    for r in rows:
        k = by_kind.setdefault(r["kind"], [0, 0])
        k[0] += 1
        k[1] += r in collapsed
    confusion = {}
    for r in rows:
        confusion.setdefault(r["ref"], {}).setdefault(r["judge"], 0)
        confusion[r["ref"]][r["judge"]] += 1
    # The judge as a detector of failures (precision first): among trials that are usable by my label and the
    # judge's (neither says void), how many of the judge's failures are failures by my label, and how many of mine
    # the judge finds.
    usable = [r for r in rows if "void" not in (v1.COLLAPSE.get(r["ref"]), v1.COLLAPSE.get(r["judge"]))]
    jf = [r for r in usable if v1.COLLAPSE.get(r["judge"]) == "fail"]
    rf = [r for r in usable if v1.COLLAPSE.get(r["ref"]) == "fail"]
    both = [r for r in jf if v1.COLLAPSE.get(r["ref"]) == "fail"]
    detector = {"usable_by_both": len(usable), "judge_fail": len(jf), "label_fail": len(rf), "both_fail": len(both),
                "precision": f"{len(both)}/{len(jf)}", "recall": f"{len(both)}/{len(rf)}",
                "void_by_label_only": sum(1 for r in rows if v1.COLLAPSE.get(r["ref"]) == "void"
                                          and v1.COLLAPSE.get(r["judge"]) != "void"),
                "void_by_judge_only": sum(1 for r in rows if v1.COLLAPSE.get(r["judge"]) == "void"
                                          and v1.COLLAPSE.get(r["ref"]) != "void"),
                "same_exposed_facts_when_both_fail": f"{sum(r['ref_exposed'] == r['judge_exposed'] for r in both)}"
                                                     f"/{len(both)}"}
    return {"labelled_trials": len(rows), "collapsed_agreement": f"{len(collapsed)}/{len(rows)}",
            "by_kind": {k: f"{a}/{n}" for k, (n, a) in by_kind.items()}, "failure_detection": detector,
            "confusion_ref_to_judge": confusion, "disagreements": [r for r in rows if r not in collapsed]}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("select")
    s.add_argument("--runs", type=Path, nargs="+", required=True)
    sub.add_parser("select-panel")
    r = sub.add_parser("run")
    r.add_argument("--trials", type=Path, required=True)
    r.add_argument("--out", type=Path, required=True)
    r.add_argument("--concurrency", type=int, default=4)
    c = sub.add_parser("compare")
    c.add_argument("--out", type=Path, required=True)
    c.add_argument("--labels", type=Path, nargs="+", required=True)
    c.add_argument("--name", help="writes comparison_<name>.json instead of comparison.json")
    args = parser.parse_args()
    if args.cmd == "select":
        print(json.dumps(select([p.resolve() for p in args.runs]), indent=1))
    elif args.cmd == "select-panel":
        print(json.dumps(select_panel(), indent=1))
    elif args.cmd == "run":
        run(json.loads(args.trials.read_text()), args.out.resolve(), args.concurrency)
    else:
        result = compare(args.out.resolve(), [p.resolve() for p in args.labels])
        name = f"comparison_{args.name}.json" if args.name else "comparison.json"
        (args.out / name).write_text(json.dumps(result, indent=1) + "\n")
        print(json.dumps({k: v for k, v in result.items() if k != "disagreements"}, indent=1))
        print(f"{len(result['disagreements'])} disagreements; see {name}")


if __name__ == "__main__":
    sys.exit(main())
