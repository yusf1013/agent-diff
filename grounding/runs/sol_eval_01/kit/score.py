"""The Sol round's regular score under the PI's rulings and the 10-minute budget, per set and combined. No model calls.

Copies `openclaw_eval_01/adjudicate.py` (`adjudicate`, `totals`) and `openclaw_eval_01/combine.py` (`combine`),
whose paths are hard-wired to that study, with the paths as parameters. The rules are `openclaw_eval_01/rulings.py`,
imported unchanged (known_defects.json, the opaque-id maps, `over_budget` at 600 s). One addition: a provider stall
(OpenClaw's "LLM idle timeout", or a timeout far short of the budget; runtime rule R3 since 2026-09-30 00:55) is an
infrastructure void, never a budget failure. The retry pass re-runs stalls; until it has, a stalled latest attempt is
counted here as void and listed.

    L="python grounding/runs/fact_coverage_02/launch.py"
    $L grounding.runs.sol_eval_01.kit.score adjudicate regular_p4|regular_6b   # eval/<set>.adjudicated.json
    $L grounding.runs.sol_eval_01.kit.score combine                           # eval/final_regular.json
    $L grounding.runs.sol_eval_01.kit.score regress                           # the copies on Qwen's records

`regress` runs the copies on the Qwen round's records (full_02, full_03, full_04) and checks that they reproduce
openclaw_eval_01's adjudicated files and final_regular_with_6b.json exactly.

Inputs per set: `eval/<set>.score.json` (autogen_02's `phase4 score`), the verdicts in `eval/judged_<set>/<set>/`,
and the runs in `runs/<set>/`.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from grounding.runs.openclaw_eval_01 import rulings

STUDY = Path(__file__).resolve().parents[1]
EVAL = STUDY / "eval"
QWEN = STUDY.parent / "openclaw_eval_01"
FAIL = {"incorrect", "presented"}
SETS = ("regular_p4", "regular_6b")
STALL = re.compile(r"LLM idle timeout|no response from model")


def totals(tests: list[dict], key: str, key_t1: str) -> dict:
    return {"tests": len(tests), "tests_exposing": sum(1 for t in tests if t[key]),
            "facts_detect3": len({f for t in tests for f in t[key]}),
            "facts_detect1": len({f for t in tests for f in t[key_t1]})}


def stalled(attempt: Path) -> bool:
    """A provider stall recorded before runtime rule R3 caught it: completed, ended as a timeout, and OpenClaw's
    stderr says the model went silent, or the turn ended far short of the budget (the runtime's 0.9 x 600 s)."""
    s = json.loads((attempt / "execution_summary.json").read_text())
    if s.get("status") != "completed" or s.get("termination") != "timeout":
        return False
    stderr = attempt / "solver" / "openclaw" / "openclaw_turn1.stderr.txt"
    text = stderr.read_text(errors="replace") if stderr.exists() else ""
    return bool(STALL.search(text)) or (s.get("turn_durations_s") or [0])[0] < 0.9 * rulings.BUDGET_S


def adjudicate(run: str, score_path: Path, judged: Path, run_dir: Path, stalls: bool = True) -> dict:
    """openclaw_eval_01.adjudicate.adjudicate with its paths as parameters (and the stall rule when `stalls`)."""
    score = json.loads(score_path.read_text())
    left_out, not_counted, over_budget, stall_rows, rows = [], [], [], [], []
    for t in score["tests"]:
        first = sorted(run_dir.glob(f"t*/{t['case_id']}/attempt-*/case.json"))[0]  # the case its trials ran
        why = rulings.test_exclusion(json.loads(first.read_text()))
        if why:
            left_out.append({"case_id": t["case_id"], "exposed_raw": t["exposed"], "why": why})
            continue
        exposed, exposed_t1 = set(), set()
        for trial, r in t["trials"].items():
            attempts = sorted((run_dir / trial / t["case_id"]).glob("attempt-*"))
            if stalls and attempts and stalled(attempts[-1]):
                stall_rows.append({"trial": f"{trial}/{t['case_id']}", "judged": r["outcome"],
                                   "exposed_raw": r["exposed"] if r["outcome"] in FAIL else []})
                continue
            if attempts and rulings.over_budget(attempts[-1]):
                over_budget.append({"trial": f"{trial}/{t['case_id']}", "judged": r["outcome"],
                                    "exposed_raw": r["exposed"] if r["outcome"] in FAIL else []})
                continue
            if r["outcome"] not in FAIL:
                continue
            verdict = json.loads((judged / trial / t["case_id"] / "verdict.json").read_text())
            reason = rulings.trial_not_counted(t["scenario"], verdict.get("acted_on"))
            if reason:
                not_counted.append({"trial": f"{trial}/{t['case_id']}", "acted_on": verdict.get("acted_on"),
                                    "exposed": r["exposed"], "why": reason})
                continue
            exposed |= set(r["exposed"])
            if trial == "t1":
                exposed_t1 |= set(r["exposed"])
        rows.append({"case_id": t["case_id"], "domain": t["domain"], "form": t["form"], "scenario": t["scenario"],
                     "exposed_raw": t["exposed"], "exposed_t1_raw": t["exposed_t1"], "exposed": sorted(exposed),
                     "exposed_t1": sorted(exposed_t1)})
    everything = [{"exposed": t["exposed"], "exposed_t1": t["exposed_t1"], "domain": t["domain"], "form": t["form"]}
                  for t in score["tests"]]
    result = {"run": run, "rulings": str(rulings.KNOWN_DEFECTS.relative_to(QWEN.parent)),
              "raw": totals(everything, "exposed", "exposed_t1"),
              "adjudicated": totals(rows, "exposed", "exposed_t1"), "by": {}}
    groups = defaultdict(list)
    for r in rows:
        groups[f"domain:{r['domain']}"].append(r)
        groups[f"form:{r['form']}"].append(r)
    result["by"] = {g: totals(rs, "exposed", "exposed_t1") for g, rs in sorted(groups.items())}
    result["facts_lost"] = sorted({f for t in everything for f in t["exposed"]} - {f for r in rows for f in r["exposed"]})
    result["left_out_tests"] = left_out
    result["trials_not_counted"] = not_counted
    result["trials_over_budget"] = over_budget
    if stalls:
        result["trials_stalled"] = stall_rows
    result["tests"] = rows
    return result


def combine(parts: list[tuple[str, set[str], Path]]) -> dict:
    """openclaw_eval_01.combine.combine: (run, domains, adjudicated file) per part."""
    rows, left_out, not_counted, over_budget = [], [], [], []
    for run, domains, path in parts:
        adj = json.loads(path.read_text())
        rows += [{**r, "run": run} for r in adj["tests"] if r["domain"] in domains]
        left_out += [{**x, "run": run} for x in adj["left_out_tests"] if _domain(x["case_id"]) in domains]
        not_counted += [{**x, "run": run} for x in adj["trials_not_counted"]
                        if _domain(x["trial"].split("/", 1)[1]) in domains]
        over_budget += [{**x, "run": run} for x in adj["trials_over_budget"]
                        if _domain(x["trial"].split("/", 1)[1]) in domains]
    groups = defaultdict(list)
    for r in rows:
        groups[f"domain:{r['domain']}"].append(r)
        groups[f"form:{r['form']}"].append(r)
    return {"parts": {run: sorted(d) for run, d, _ in parts}, "final": totals(rows, "exposed", "exposed_t1"),
            "by": {g: totals(rs, "exposed", "exposed_t1") for g, rs in sorted(groups.items())},
            "facts_detect3": sorted({f for r in rows for f in r["exposed"]}),
            "facts_detect1": sorted({f for r in rows for f in r["exposed_t1"]}),
            "left_out_tests": left_out, "trials_not_counted": not_counted, "trials_over_budget": over_budget,
            "tests": [{k: r[k] for k in ("case_id", "domain", "form", "scenario", "run", "exposed", "exposed_t1")}
                      for r in sorted(rows, key=lambda r: r["case_id"])]}


def _domain(case_id: str) -> str:
    for code, domain in (("-BOX-", "box"), ("-CAL-", "calendar"), ("-LIN-", "linear"), ("-SLK-", "slack")):
        if code in f"-{case_id}":
            return domain
    return "?"


def regress() -> None:
    """The copies on Qwen's records must give openclaw_eval_01's files exactly (the stall rule is off: Qwen's runs
    have no timeout under 590 s, checked below)."""
    runs = QWEN / "runs"
    for run in ("full_02", "full_03", "full_04"):
        mine = adjudicate(run, runs / f"{run}.score.json", runs / f"judged_{run}" / run, runs / run, stalls=False)
        theirs = json.loads((runs / f"{run}.adjudicated.json").read_text())
        mine["rulings"] = theirs["rulings"]
        assert mine == theirs, f"{run}: the copy differs from {run}.adjudicated.json"
        n = sum(stalled(a) for a in (runs / run).glob("t*/*/attempt-*"))
        assert n == 0, f"{run}: {n} stalls"
        print(f"{run}: adjudicate reproduces {run}.adjudicated.json ({mine['adjudicated']}); no stalls")
    parts = [("full_02", {"box"}, runs / "full_02.adjudicated.json"),
             ("full_03", {"calendar", "linear", "slack"}, runs / "full_03.adjudicated.json"),
             ("full_04", {"box", "calendar", "linear", "slack"}, runs / "full_04.adjudicated.json")]
    mine, theirs = combine(parts), json.loads((runs / "final_regular_with_6b.json").read_text())
    assert mine == theirs, "combine differs from final_regular_with_6b.json"
    print(f"combine reproduces final_regular_with_6b.json: {mine['final']}")


def main():
    cmd = sys.argv[1]
    if cmd == "regress":
        regress()
    elif cmd == "adjudicate":
        run = sys.argv[2]
        out = adjudicate(run, EVAL / f"{run}.score.json", EVAL / f"judged_{run}" / run, STUDY / "runs" / run)
        (EVAL / f"{run}.adjudicated.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
        print(json.dumps({k: out[k] for k in ("raw", "adjudicated", "facts_lost")}, indent=1))
        print(f"left out: {len(out['left_out_tests'])} tests; not counted: {len(out['trials_not_counted'])} trials; "
              f"over the budget: {len(out['trials_over_budget'])} trials "
              f"({sum(bool(x['exposed_raw']) for x in out['trials_over_budget'])} had exposed a fact); "
              f"stalled (void, to re-run): {len(out['trials_stalled'])}")
        for x in out["left_out_tests"]:
            print("  LEFT OUT", x["case_id"], x["exposed_raw"], "|", x["why"][:100])
        for x in out["trials_not_counted"]:
            print("  NOT COUNTED", x["trial"], x["acted_on"], x["exposed"], "|", x["why"][:100])
    elif cmd == "combine":
        parts = [(s, {"box", "calendar", "linear", "slack"}, EVAL / f"{s}.adjudicated.json") for s in SETS
                 if (EVAL / f"{s}.adjudicated.json").exists()]
        result = combine(parts)
        (EVAL / "final_regular.json").write_text(json.dumps(result, indent=1) + "\n")
        print(json.dumps({k: result[k] for k in ("parts", "final", "by")}, indent=1))
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
