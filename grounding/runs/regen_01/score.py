"""This study's regular score, as openclaw_eval_01/adjudicate.py computes a run's (the rulings, the solver's budget,
trials acting only on flawed near misses not counted), with two additions. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.score RUN [--runs-dir DIR] [--quiet-host]

- **The exposure filter** (the lead agreed, 2026-09-30): a failing trial exposes a fact only through a near miss the
  rulings keep valid. When the verdict names acted-on records, a fact counts if one of them is a valid near miss on
  it; when it names none (the agent presented a near miss without acting), a fact counts if the test holds a valid
  near miss on it. adjudicate.py drops a trial only when every acted-on record is flawed, so a cover trial that acts on
  the target and a flawed near miss would otherwise credit the flawed near miss's fact.
- **Timeouts under host load** (the lead, 2026-09-30: "a trial that times out with fewer than 10 requests at over
  30 s each"): a trial that OpenClaw's turn limit ended after fewer than 10 completed model requests whose median
  took over 30 s timed out because the shared self-host was overloaded, not because of the agent. (Read literally,
  "each over 30 s" misses such trials whenever one early, short-context request was quick; `literal` records whether
  every completed request took over 30 s.) They are listed apart, with their request counts and times; the numbers
  count them as the budget rule does (the solver's failure, exposing no fact) until they are re-run on a quiet host.
  Request times come from the attempt's solver/requests.tar.xz (the proxy's records, archived when the attempt ends).

Reads RUNS_DIR/<RUN>.score.json (autogen_02's `phase4 score`) and RUNS_DIR/judged_<RUN>/<RUN>/ (judge v2); writes
RUNS_DIR/<RUN>.adjudicated.json. RUNS_DIR is this study's runs/ unless --runs-dir names another (for checking this
script against openclaw_eval_01's own adjudicated runs). --quiet-host gives the other reading (the lead: "report both
readings"): each timeout under host load is replaced by its re-run on the quiet host (runs/<RUN>_load, rerun_load.py,
judged into runs/judged_<RUN>_load), and writes RUNS_DIR/<RUN>.adjudicated_quiet_host.json. A re-run's verdict is
matched to its attempt by the path from grounding/runs/ on (`same_attempt`), so this reading works in any checkout
(2026-09-30, session sol_score).
"""
from __future__ import annotations

import json
import statistics
import sys
import tarfile
from collections import defaultdict
from pathlib import Path

from grounding.runs.regen_01 import rules

rulings = rules.rulings
HERE = Path(__file__).resolve().parent
FAIL = {"incorrect", "presented"}
LOAD_REQUESTS, LOAD_SECONDS = 10, 30


def totals(tests: list[dict], key: str, key_t1: str) -> dict:
    return {"tests": len(tests), "tests_exposing": sum(1 for t in tests if t[key]),
            "facts_detect3": len({f for t in tests for f in t[key]}),
            "facts_detect1": len({f for t in tests for f in t[key_t1]})}


def request_times(attempt: Path) -> list[dict]:
    """Each model request's time and ending, from the archived proxy records (or the live folder)."""
    out = []
    archive = attempt / "solver" / "requests.tar.xz"
    if archive.exists():
        with tarfile.open(archive) as tar:
            for name in sorted(n for n in tar.getnames() if n.endswith(".meta.json")):
                out.append(json.load(tar.extractfile(name)))
    else:
        out = [json.loads(p.read_text()) for p in sorted((attempt / "solver" / "requests").glob("*.meta.json"))]
    return out


def under_load(attempt: Path) -> dict | None:
    """The trial's request times, if OpenClaw's turn limit ended it under host load (the lead's criterion, read as
    the median; see the module's docstring)."""
    summary = json.loads((attempt / "execution_summary.json").read_text())
    if summary.get("termination") != "timeout":
        return None
    done = [m.get("duration_s") or 0 for m in request_times(attempt) if m.get("finish_reason")]
    if done and len(done) < LOAD_REQUESTS and statistics.median(done) > LOAD_SECONDS:
        return {"completed_requests": len(done), "median_s": round(statistics.median(done), 1),
                "min_s": round(min(done), 1), "max_s": round(max(done), 1), "model_time_s": round(sum(done)),
                "literal": all(d > LOAD_SECONDS for d in done)}
    return None


def valid_facts(case: dict, verdict: dict) -> set[str]:
    """The verdict's exposed facts that a valid near miss of the ran case carries (the exposure filter)."""
    scenario = rulings.scenario_of(case["case_id"])
    bad = rulings.flawed(scenario)
    claims = [c for r in case["references"] for c in r.get("claims", [])]
    valid = defaultdict(set)
    for c in claims:
        if str(c["witness"]) not in bad:
            valid[c["requirement"]].add(str(c["witness"]))
    acted = {str(a) for a in verdict.get("acted_on") or []}
    exposed = set(verdict.get("exposed") or [])
    if acted:
        return {f for f in exposed if valid.get(f, set()) & acted}
    return {f for f in exposed if valid.get(f)}


def same_attempt(recorded: str, attempt: Path) -> bool:
    """A verdict's recorded attempt is this attempt: the same path from grounding/runs/ on, whichever checkout it was
    recorded in. (2026-09-30, session sol_score, with the lead's leave: a plain string comparison matched only in the
    regen session's own worktree, so the quiet-host reading failed in any other checkout.)"""
    marker = "/grounding/runs/"
    return marker in recorded and recorded.split(marker, 1)[1] == str(attempt).split(marker, 1)[-1]


def reruns(run: str, runs_dir: Path) -> dict:
    """(trial, case id) -> (the re-run's latest attempt, judge v2's verdict on it), from runs/<RUN>_load (rerun_load.py)
    and runs/judged_<RUN>_load, for the quiet-host reading."""
    out = {}
    for verdict_path in sorted((runs_dir / f"judged_{run}_load" / f"{run}_load").glob("t*/*/verdict.json")):
        trial, case_id = verdict_path.parent.parent.name, verdict_path.parent.name
        attempts = sorted((runs_dir / f"{run}_load" / trial / case_id).glob("attempt-*"))
        verdict = json.loads(verdict_path.read_text())
        if attempts and same_attempt(verdict.get("attempt") or "", attempts[-1]):
            out[(trial, case_id)] = (attempts[-1], verdict)
    return out


def adjudicate(run: str, runs_dir: Path, quiet: bool = False) -> dict:
    """quiet: the quiet-host reading, each timeout under host load replaced by its re-run (judged by judge v2); a
    re-run over the budget again is a failure exposing no fact, as any trial over the budget."""
    score = json.loads((runs_dir / f"{run}.score.json").read_text())
    judged = runs_dir / f"judged_{run}" / run
    rerun = reruns(run, runs_dir) if quiet else {}
    left_out, not_counted, over_budget, filtered, load, rows, replaced = [], [], [], [], [], [], []
    for t in score["tests"]:
        attempts0 = sorted((runs_dir / run).glob(f"t*/{t['case_id']}/attempt-*/case.json"))
        case = json.loads(attempts0[0].read_text())
        why = rulings.test_exclusion(case)
        if why:
            left_out.append({"case_id": t["case_id"], "exposed_raw": t["exposed"], "why": why})
            continue
        exposed, exposed_t1, exposed_nl, exposed_t1_nl = set(), set(), set(), set()
        for trial, r in t["trials"].items():
            attempts = sorted((runs_dir / run / trial / t["case_id"]).glob("attempt-*"))
            verdict = None
            if quiet and attempts and under_load(attempts[-1]):
                if (trial, t["case_id"]) not in rerun:
                    raise SystemExit(f"no judged re-run for {trial}/{t['case_id']}")
                attempt, verdict = rerun[(trial, t["case_id"])]
                attempts = [attempt]
                r = {"outcome": verdict.get("outcome"), "exposed": sorted(verdict.get("exposed") or [])}
                replaced.append({"trial": f"{trial}/{t['case_id']}", "rerun": str(attempt.relative_to(runs_dir)),
                                 "outcome": r["outcome"], "exposed": r["exposed"],
                                 "over_budget": rulings.over_budget(attempt)})
            if attempts and rulings.over_budget(attempts[-1]):
                heavy = under_load(attempts[-1])
                over_budget.append({"trial": f"{trial}/{t['case_id']}", "judged": r["outcome"],
                                    "exposed_raw": r["exposed"] if r["outcome"] in FAIL else [],
                                    "under_host_load": heavy})
                if heavy:
                    load.append({"trial": f"{trial}/{t['case_id']}", **heavy})
                continue
            if r["outcome"] not in FAIL:
                continue
            verdict = verdict or json.loads((judged / trial / t["case_id"] / "verdict.json").read_text())
            reason = rulings.trial_not_counted(t["scenario"], verdict.get("acted_on"))
            if reason:
                not_counted.append({"trial": f"{trial}/{t['case_id']}", "acted_on": verdict.get("acted_on"),
                                    "exposed": r["exposed"], "why": reason})
                continue
            kept = valid_facts(json.loads((attempts[-1] / "case.json").read_text()), {**verdict, "exposed": r["exposed"]})
            if set(r["exposed"]) - kept:
                filtered.append({"trial": f"{trial}/{t['case_id']}", "exposed": r["exposed"], "kept": sorted(kept),
                                 "acted_on": verdict.get("acted_on")})
            exposed |= kept
            if trial == "t1":
                exposed_t1 |= kept
        rows.append({"case_id": t["case_id"], "domain": t["domain"], "form": t["form"], "scenario": t["scenario"],
                     "exposed_raw": t["exposed"], "exposed_t1_raw": t["exposed_t1"], "exposed": sorted(exposed),
                     "exposed_t1": sorted(exposed_t1)})
    everything = [{"exposed": t["exposed"], "exposed_t1": t["exposed_t1"], "domain": t["domain"], "form": t["form"]}
                  for t in score["tests"]]
    groups = defaultdict(list)
    for r in rows:
        groups[f"domain:{r['domain']}"].append(r)
        groups[f"form:{r['form']}"].append(r)
    return {"run": run, "reading": "quiet host" if quiet else "as run", "rulings": str(rulings.KNOWN_DEFECTS),
            "budget_s": rulings.BUDGET_S,
            "raw": totals(everything, "exposed", "exposed_t1"), "adjudicated": totals(rows, "exposed", "exposed_t1"),
            "by": {g: totals(rs, "exposed", "exposed_t1") for g, rs in sorted(groups.items())},
            "facts": sorted({f for r in rows for f in r["exposed"]}),
            "facts_t1": sorted({f for r in rows for f in r["exposed_t1"]}),
            "left_out_tests": left_out, "trials_not_counted": not_counted, "trials_over_budget": over_budget,
            "timeouts_under_host_load": load, "replaced_by_reruns": replaced, "exposures_filtered": filtered,
            "tests": rows}


def main():
    args = sys.argv[1:]
    run = args[0]
    runs_dir = Path(args[args.index("--runs-dir") + 1]).resolve() if "--runs-dir" in args else HERE / "runs"
    quiet = "--quiet-host" in args
    out = adjudicate(run, runs_dir, quiet)
    if "--runs-dir" not in args:
        name = f"{run}.adjudicated_quiet_host.json" if quiet else f"{run}.adjudicated.json"
        (runs_dir / name).write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({k: out[k] for k in ("reading", "raw", "adjudicated")}, indent=1))
    print(f"left out {len(out['left_out_tests'])} tests; not counted {len(out['trials_not_counted'])} trials; over "
          f"budget {len(out['trials_over_budget'])} ({len(out['timeouts_under_host_load'])} under host load); "
          f"replaced by re-runs {len(out['replaced_by_reruns'])}; "
          f"exposures filtered in {len(out['exposures_filtered'])} trials")


if __name__ == "__main__":
    main()
