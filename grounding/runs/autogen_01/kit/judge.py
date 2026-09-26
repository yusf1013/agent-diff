"""Judge recorded trials with a headless Claude Code Sonnet agent, and compare its verdicts with reference labels.

    python -m grounding.runs.autogen_01.kit.judge select --split dev|test [--clean N] > trials.json
    python -m grounding.runs.autogen_01.kit.judge run --trials trials.json --out DIR [--concurrency 4]
    python -m grounding.runs.autogen_01.kit.judge compare --out DIR [--labels LABELS.json]

`run` triages each trial with fact_coverage_02's scorer (diff and write commands), builds the judge's bundle from
the attempt folder, and asks the judge for one verdict (JSON schema). Reference labels are read only by `select`
(to pick trials) and `compare`, never by `run`. Every call's prompt, result, transcript and usage are kept.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from grounding.runs.autogen_01.kit import agent, bundle
from grounding.runs.fact_coverage_01.pilot import analyze as pilot
from grounding.runs.fact_coverage_02 import score
from grounding.runs.fact_coverage_02.analyze import current

KIT = Path(__file__).resolve().parent
STUDY = KIT.parent
FC2 = STUDY.parent / "fact_coverage_02"
WORKSPACES = Path("/tmp/autogen-5840209d/ws/judge")
OUTCOMES = ["incorrect", "presented", "correct", "correct_absent", "false_absence", "incomplete", "not_established",
            "artifact"]
SCHEMA = {
    "type": "object",
    "properties": {
        "outcome": {"type": "string", "enum": OUTCOMES},
        "acted_on": {"type": "array", "items": {"type": "string"},
                     "description": "ids of records the solver acted on or presented as the match"},
        "exposed": {"type": "array", "items": {"type": "string"}, "description": "facts exposed (decoys' facts)"},
        "mechanism": {"type": "string", "enum": ["skipped-check", "saw-mismatch-accepted", "misread", "none"]},
        "artifact_reason": {"type": "string", "description": "for artifact: the replica behaviour or test defect"},
        "note": {"type": "string", "description": "1-3 sentences citing the decisive steps"},
    },
    "required": ["outcome", "acted_on", "exposed", "mechanism", "artifact_reason", "note"],
}
DEV_RUNS = {"b1", "method_pilot", "method_pilot_panel"}
TEST_RUNS = {"method_new", "method_new_lin25", "method_new_slk21", "factprobe", "factprobe_extra", "wording_check",
             "hidden_pilot"}
COLLAPSE = {"incorrect": "fail", "presented": "fail", "correct": "pass", "correct_absent": "pass",
            "false_absence": "false_absence", "incomplete": "incomplete", "not_established": "void", "artifact": "void"}


def scored_exposed(verdict: dict) -> list[str]:
    """The method's scoring rule for policy-panel tests is applied in code, not left to the judge: a failure on a
    no-target panel test exposes `policy:presupposed`, one on a two-target test `policy:underspecified`."""
    if verdict.get("form") == "policy panel" and COLLAPSE.get(verdict.get("outcome")) == "fail":
        return ["policy:underspecified"] if verdict.get("targets", 0) > 1 else ["policy:presupposed"]
    return sorted(verdict.get("exposed", []))


def latest(run_dir: Path, trial: str, case_id: str) -> Path:
    return sorted((run_dir / trial / case_id).glob("attempt-*"))[-1]


def triage(run_name: str, trial: str, attempt: Path) -> tuple[dict, dict, dict]:
    """The scorer's provisional label (no manual labels), with the case refreshed as the scorer does."""
    summary = json.loads((attempt / "execution_summary.json").read_text())
    case = current(json.loads((attempt / "case.json").read_text()))
    row = {"run": run_name, "trial": trial, "case_id": summary["case_id"], "status": summary.get("status")}
    if summary.get("status") == "completed":
        row.update(pilot.attribute(case, attempt))
    result = score.classify(row, case, {}, attempt)
    return case, summary, {"references": row.get("references", []), "outcome": result["outcome"],
                           "exposed": result["exposed"]}


def select(split: str, clean: int, seed: int = 7) -> list[dict]:
    """Trials to judge: every labelled trial of the split's runs, plus `clean` sampled unlabelled clean trials."""
    labels = json.loads((FC2 / "manual_labels.json").read_text())
    runs = DEV_RUNS if split == "dev" else TEST_RUNS
    chosen = [{"run_dir": str(FC2 / "runs" / k.split("/")[0]), "run": k.split("/")[0], "trial": k.split("/")[1],
               "case_id": k.split("/")[2], "labelled": True} for k in labels if k.split("/")[0] in runs]
    pool = []
    for run in sorted(runs):
        for summary in sorted((FC2 / "runs" / run).glob("t*/*/attempt-*/execution_summary.json")):
            attempt = summary.parent
            trial, case_id = attempt.parts[-3], attempt.parts[-2]
            key = f"{run}/{trial}/{case_id}"
            if key in labels or attempt != latest(FC2 / "runs" / run, trial, case_id):
                continue
            try:
                _, _, tri = triage(run, trial, attempt)
            except Exception:
                continue
            if tri["outcome"] in ("correct", "correct_absent"):
                pool.append({"run_dir": str(FC2 / "runs" / run), "run": run, "trial": trial, "case_id": case_id,
                             "labelled": False, "clean_outcome": tri["outcome"]})
    random.Random(seed).shuffle(pool)
    return chosen + pool[:clean]


def select_run(run_dir: Path, suite: Path, clean_share: float = 0.2, seed: int = 7) -> list[dict]:
    """Trials of a generated suite's solver run: every trial that is not mechanically clean, plus a random share of
    the clean ones (their provisional label stands unless the judge is asked)."""
    meta = {t["case_id"]: t for t in json.loads(suite.read_text())}
    chosen, clean = [], []
    for summary in sorted(run_dir.glob("t*/*/attempt-*/execution_summary.json")):
        attempt = summary.parent
        trial, case_id = attempt.parts[-3], attempt.parts[-2]
        if attempt != latest(run_dir, trial, case_id):
            continue
        _, _, tri = triage(run_dir.name, trial, attempt)
        item = {"run_dir": str(run_dir), "run": run_dir.name, "trial": trial, "case_id": case_id,
                "form": meta.get(case_id, {}).get("form"), "provisional": tri["outcome"]}
        (clean if tri["outcome"] in ("correct", "correct_absent") else chosen).append(item)
    random.Random(seed).shuffle(clean)
    k = round(len(clean) * clean_share)
    for item in clean[:k]:
        item["clean_sample"] = True
    return chosen + clean[:k]


def forms() -> dict:
    return {k: v.get("form") for k, v in score.suites().items()}


def judge_one(item: dict, out: Path, form_of: dict, calls_log: Path) -> dict:
    run_dir = Path(item["run_dir"])
    attempt = latest(run_dir, item["trial"], item["case_id"])
    dest = out / item["run"] / item["trial"] / item["case_id"]
    verdict_path = dest / "verdict.json"
    if verdict_path.exists():
        old = json.loads(verdict_path.read_text())
        if old.get("attempt") == str(attempt):
            return old
        # A newer attempt of this trial exists (a retry): keep the old verdict as evidence and judge again.
        verdict_path.rename(dest / f"verdict-{Path(old.get('attempt', 'unknown')).name}.json")
    case, summary, tri = triage(item["run"], item["trial"], attempt)
    present = any(r["use"] == "target" and r["expected"] for r in case["references"])
    form = item.get("form") or form_of.get(case["case_id"]) or (
        "cover (target and all decoys)" if present else "no-target test with all of the scenario's decoys")
    text = bundle.build(case, attempt, form, tri, summary)
    system = (KIT / "prompts" / "judge.md").read_text() + "\n\n# Replica notes for this domain\n\n" + \
        (STUDY / "inputs" / case["domain"] / "replica.md").read_text()
    result = agent.run(agent.Call(
        role="judge", workspace=WORKSPACES / out.name / f"{item['run']}-{item['trial']}-{item['case_id']}",
        prompt=text + "\n\nGive your verdict for this trial.", log_dir=dest, calls_log=calls_log, tools=[],
        schema=SCHEMA, system_append=system, label=f"{item['run']}/{item['trial']}/{item['case_id']}"))
    verdict = agent.structured(result) or {}
    verdict.update(key=f"{item['run']}/{item['trial']}/{item['case_id']}", attempt=str(attempt),
                   provisional=tri["outcome"], provisional_exposed=tri["exposed"], form=form,
                   targets=sum(len(r["expected"]) for r in case["references"] if r["use"] == "target"))
    verdict_path.write_text(json.dumps(verdict, indent=1, ensure_ascii=False) + "\n")
    return verdict


def run(trials: list[dict], out: Path, concurrency: int):
    out.mkdir(parents=True, exist_ok=True)
    prompt = (KIT / "prompts" / "judge.md").read_text()
    frozen = out / "judge_prompt.md"
    if frozen.exists() and frozen.read_text() != prompt:
        raise SystemExit(f"{out} was judged with another prompt version; use a new --out")
    frozen.write_text(prompt)
    calls_log = out / "calls.jsonl"
    form_of = forms()
    done = 0
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(judge_one, t, out, form_of, calls_log): t for t in trials}
        for fut in as_completed(futures):
            t = futures[fut]
            done += 1
            try:
                v = fut.result()
                print(f"[{done}/{len(trials)}] {v['key']}: {v.get('outcome')} {v.get('exposed')}", flush=True)
            except Exception as exc:  # recorded; the trial stays unjudged
                print(f"[{done}/{len(trials)}] {t['run']}/{t['trial']}/{t['case_id']}: FAILED {exc}", flush=True)


def compare(out: Path, trials: list[dict] | None = None) -> dict:
    labels = json.loads((FC2 / "manual_labels.json").read_text())
    rows = []
    for path in sorted(out.glob("*/*/*/verdict.json")):
        v = json.loads(path.read_text())
        key = v["key"]
        if key in labels:
            ref = labels[key]
            ref_outcome, ref_exposed = ref["outcome"], sorted(ref.get("exposed", []))
            if ref_outcome in ("incorrect", "presented") and "exposed" not in ref:
                ref_exposed = sorted(v.get("provisional_exposed", []))
        else:
            ref, ref_outcome, ref_exposed = {}, v["provisional"], []
        if "targets" not in v:  # verdicts from before the field was recorded
            attempt = Path(v["attempt"])
            case = current(json.loads((attempt / "case.json").read_text()))
            v["targets"] = sum(len(r["expected"]) for r in case["references"] if r["use"] == "target")
        rows.append({"key": key, "labelled": key in labels, "ref": ref_outcome, "judge": v.get("outcome"),
                     "ref_exposed": ref_exposed, "judge_exposed": scored_exposed(v),
                     "ref_mechanism": ref.get("mechanism"), "judge_mechanism": v.get("mechanism"),
                     "contestable": bool(ref.get("contestable"))})
    n = len(rows)
    exact = sum(r["ref"] == r["judge"] for r in rows)
    collapsed = sum(COLLAPSE.get(r["ref"], r["ref"]) == COLLAPSE.get(r["judge"], r["judge"]) for r in rows)
    fails = [r for r in rows if COLLAPSE.get(r["ref"]) == "fail" and COLLAPSE.get(r["judge"]) == "fail"]
    exposed_ok = sum(r["ref_exposed"] == r["judge_exposed"] for r in fails)
    art_ref = [r for r in rows if r["ref"] == "artifact"]
    art_judge = [r for r in rows if r["judge"] == "artifact"]
    mech = [r for r in rows if r["ref_mechanism"]]
    confusion = {}
    for r in rows:
        confusion.setdefault(r["ref"], {}).setdefault(r["judge"], 0)
        confusion[r["ref"]][r["judge"]] += 1

    def facts(which):
        out_ = {}
        for r in rows:
            run = r["key"].split("/")[0]
            outcome = r["ref"] if which == "ref" else r["judge"]
            if COLLAPSE.get(outcome) == "fail" and not (which == "ref" and r["contestable"]):
                out_.setdefault(run, set()).update(r[f"{which}_exposed"])
        return {k: sorted(v) for k, v in out_.items()}

    ref_facts, judge_facts = facts("ref"), facts("judge")
    summary = {
        "trials": n, "labelled": sum(r["labelled"] for r in rows), "clean_sampled": sum(not r["labelled"] for r in rows),
        "exact_agreement": f"{exact}/{n}", "collapsed_agreement": f"{collapsed}/{n}",
        "exposed_agreement_on_shared_fails": f"{exposed_ok}/{len(fails)}",
        "artifact_recall": f"{sum(r['judge'] == 'artifact' for r in art_ref)}/{len(art_ref)}",
        "artifact_precision": f"{sum(r['ref'] == 'artifact' for r in art_judge)}/{len(art_judge)}",
        "mechanism_agreement": f"{sum(r['ref_mechanism'] == r['judge_mechanism'] for r in mech)}/{len(mech)}",
        "confusion_ref_to_judge": confusion,
        "distinct_facts": {run: {"reference": ref_facts.get(run, []), "judge": judge_facts.get(run, []),
                                 "missed_by_judge": sorted(set(ref_facts.get(run, [])) - set(judge_facts.get(run, []))),
                                 "extra_by_judge": sorted(set(judge_facts.get(run, [])) - set(ref_facts.get(run, [])))}
                           for run in sorted(set(ref_facts) | set(judge_facts))},
        "disagreements": [r for r in rows if COLLAPSE.get(r["ref"], r["ref"]) != COLLAPSE.get(r["judge"], r["judge"])
                          or (r in fails and r["ref_exposed"] != r["judge_exposed"])],
    }
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("select")
    s.add_argument("--split", choices=["dev", "test"], required=True)
    s.add_argument("--clean", type=int, default=0)
    sr = sub.add_parser("select-run", help="trials of a generated suite's solver run")
    sr.add_argument("--run-dir", type=Path, required=True)
    sr.add_argument("--suite", type=Path, required=True)
    sr.add_argument("--clean-share", type=float, default=0.2)
    r = sub.add_parser("run")
    r.add_argument("--trials", type=Path, required=True)
    r.add_argument("--out", type=Path, required=True)
    r.add_argument("--concurrency", type=int, default=4)
    r.add_argument("--limit", type=int)
    c = sub.add_parser("compare")
    c.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.cmd == "select":
        print(json.dumps(select(args.split, args.clean), indent=1))
    elif args.cmd == "select-run":
        print(json.dumps(select_run(args.run_dir.resolve(), args.suite.resolve(), args.clean_share), indent=1))
    elif args.cmd == "run":
        trials = json.loads(args.trials.read_text())
        run(trials[:args.limit] if args.limit else trials, args.out.resolve(), args.concurrency)
    else:
        result = compare(args.out.resolve())
        (args.out / "comparison.json").write_text(json.dumps(result, indent=1) + "\n")
        print(json.dumps({k: v for k, v in result.items() if k not in ("disagreements", "distinct_facts")}, indent=1))
        print(f"{len(result['disagreements'])} disagreements; see comparison.json")


if __name__ == "__main__":
    sys.exit(main())
