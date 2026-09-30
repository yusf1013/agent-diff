"""The Sol round's regular score under the PI's rulings and the 10-minute budget, per set and combined. No model calls.

Copies `openclaw_eval_01/adjudicate.py` (`adjudicate`, `totals`) and `openclaw_eval_01/combine.py` (`combine`),
whose paths are hard-wired to that study, with the paths as parameters. The rules are `openclaw_eval_01/rulings.py`,
imported unchanged (known_defects.json, the opaque-id maps, `over_budget` at 600 s). One addition: a provider stall
(OpenClaw's "LLM idle timeout", or a timeout far short of the budget; runtime rule R3 since 2026-09-30 00:55) is an
infrastructure void, never a budget failure. The retry pass re-runs stalls; until it has, a stalled latest attempt is
counted here as void and listed.

The rulings file is roadmap_01/known_defects.json as it now stands: since 2026-09-30 01:14 it holds two near misses
the PI ruled matches in blind_review_01 (G4-BOX-11's "Seaport Archive 2024", G4-BOX-02's copy in a subfolder), found
while labelling this round. `--before-br` scores with the file as it was before that change
(eval/known_defects_before_br.json, from commit 3405221d90^), so the PI sees the difference.

    L="python grounding/runs/fact_coverage_02/launch.py"
    $L grounding.runs.sol_eval_01.kit.score adjudicate SET [--before-br]      # eval/<set>.adjudicated[_before_br].json
    $L grounding.runs.sol_eval_01.kit.score combine [--before-br]              # eval/final_regular[_before_br].json
    $L grounding.runs.sol_eval_01.kit.score combine --regen                    # eval/final_regular_regen.json
    $L grounding.runs.sol_eval_01.kit.score borderline      # eval/regen_full_01.borderline_sensitivity.json
    $L grounding.runs.sol_eval_01.kit.score qwen --before-br   # Qwen's final score with the earlier file (eval/qwen_final_regular_before_br.json)
    $L grounding.runs.sol_eval_01.kit.score regress                                        # the copies on Qwen's records

`regress` runs the copies on the Qwen round's records (full_02, full_03, full_04) and checks that they reproduce
openclaw_eval_01's adjudicated files and final_regular_with_6b.json exactly.

Inputs per set: `eval/<set>.score.json` (autogen_02's `phase4 score`), the verdicts in `eval/judged_<set>/<set>/`,
and the runs in `runs/<set>/`. The regenerated half's regular set (regen_full_01) is scored alone (`combine
--regen`), with regen_01's rulings wrapper loaded through kit/sets.py; `--before-br` applies to the first half only.

The regenerated half's set is adjudicated by regen_01/score.py's `adjudicate`, unchanged: the script that scored
Qwen's regenerated half (openclaw_eval_01's logic plus the exposure filter the lead agreed for regen_01, a fact
counting only through a valid near miss), run on this study's layout through a folder of links. The file also records
this kit's own `adjudicate` on the same set (`without_exposure_filter`), so any difference the filter makes shows, and
the stalled attempts (the stall rule is this kit's; runtime rule R3 already catches stalls in these runs).
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from grounding.runs.openclaw_eval_01 import rulings
from grounding.runs.sol_eval_01.kit import sets  # noqa: F401  (regen_01's rulings wrapper)

STUDY = Path(__file__).resolve().parents[1]
EVAL = STUDY / "eval"
QWEN = STUDY.parent / "openclaw_eval_01"
FAIL = {"incorrect", "presented"}
SETS = ("regular_p4", "regular_6b")
STALL = re.compile(r"LLM idle timeout|no response from model")
BEFORE_BR = EVAL / "known_defects_before_br.json"


def use_rulings_before_br() -> None:
    """Point rulings.py at the rulings file as it was before the two blind-review rulings were added."""
    rulings.KNOWN_DEFECTS = BEFORE_BR
    rulings._doc.cache_clear()


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


def _regen_score(run: str) -> dict:
    """regen_01/score.py's `adjudicate` (as run), unchanged, on this study's layout through a folder of links."""
    import tempfile
    from grounding.runs.regen_01 import score as regen_score
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / f"{run}.score.json").symlink_to(EVAL / f"{run}.score.json")
        (tmp / f"judged_{run}").symlink_to(EVAL / f"judged_{run}")
        (tmp / run).symlink_to((STUDY / "runs" / run).resolve())
        return regen_score.adjudicate(run, tmp)


def borderline_regen(run: str = "regen_full_01") -> dict:
    """regen_01/borderline.py's sensitivity on Sol's run: the score if the PI ruled the near misses regen_01's review
    flagged borderline (valid by the rulings) flawed. The extra rulings exist only in this process, as there."""
    from grounding.runs.regen_01 import borderline
    base, extra, original = _regen_score(run), borderline.borderline(), rulings._doc

    def doc():
        d = dict(original())
        d["near_misses"] = list(d.get("near_misses", [])) + [
            {"scenario": s, "witness": w, "ruling": "flawed", "source": "regen_01 borderline (hypothetical)"}
            for s, w in extra]
        return d

    rulings._doc = doc
    try:
        alt = _regen_score(run)
    finally:
        rulings._doc = original
    q = lambda out: {f"{r['domain']} {f}" for r in out["tests"] for f in r["exposed"]}  # noqa: E731
    return {"_about": f"regen_01/borderline.py's sensitivity on Sol's {run} (kit/score.py borderline; not a ruling).",
            "borderline_near_misses": [f"{s} {w}" for s, w in extra],
            "as_run": base["adjudicated"], "borderline_ruled_flawed": alt["adjudicated"],
            "facts_lost": sorted(q(base) - q(alt)),
            "tests_left_out": sorted(t["case_id"] for t in alt["left_out_tests"]),
            "trials_not_counted": len(alt["trials_not_counted"]) - len(base["trials_not_counted"])}


def adjudicate_regen(run: str) -> dict:
    """regen_01/score.py's `adjudicate` (as run) on a regenerated-half set, with this kit's own `adjudicate` beside it."""
    out = _regen_score(run)
    out["scored_by"] = "regen_01/score.py adjudicate, as run (the script that scored Qwen's regenerated half)"
    raw = json.loads((EVAL / f"{run}.score.json").read_text())
    out["facts_lost"] = sorted({f for t in raw["tests"] for f in t["exposed"]} - set(out["facts"]))
    out["trials_stalled"] = [f"{a.parts[-3]}/{a.parts[-2]}" for a in sorted((STUDY / "runs" / run).glob("t*/*/attempt-*"))
                             if a == sorted(a.parent.glob("attempt-*"))[-1] and stalled(a)]
    mine = adjudicate(run, EVAL / f"{run}.score.json", EVAL / f"judged_{run}" / run, STUDY / "runs" / run)
    out["without_exposure_filter"] = {k: mine[k] for k in ("adjudicated", "by")}
    out["without_exposure_filter"]["facts_detect3"] = sorted({f for r in mine["tests"] for f in r["exposed"]})
    return out


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
        suffix = "_before_br" if "--before-br" in sys.argv else ""
        if suffix:
            use_rulings_before_br()
        if sets.SETS[run]["half"] == "regen":
            if suffix:
                raise SystemExit("--before-br applies to the first half only")
            out = adjudicate_regen(run)
            print("without the exposure filter:", out["without_exposure_filter"]["adjudicated"])
        else:
            out = adjudicate(run, EVAL / f"{run}.score.json", EVAL / f"judged_{run}" / run, STUDY / "runs" / run)
        (EVAL / f"{run}.adjudicated{suffix}.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
        print(json.dumps({k: out[k] for k in ("raw", "adjudicated", "facts_lost")}, indent=1))
        print(f"left out: {len(out['left_out_tests'])} tests; not counted: {len(out['trials_not_counted'])} trials; "
              f"over the budget: {len(out['trials_over_budget'])} trials "
              f"({sum(bool(x['exposed_raw']) for x in out['trials_over_budget'])} had exposed a fact); "
              f"stalled (void, to re-run): {len(out['trials_stalled'])}")
        for x in out["left_out_tests"]:
            print("  LEFT OUT", x["case_id"], x["exposed_raw"], "|", x["why"][:100])
        for x in out["trials_not_counted"]:
            print("  NOT COUNTED", x["trial"], x["acted_on"], x["exposed"], "|", x["why"][:100])
    elif cmd == "borderline":
        out = borderline_regen()
        (EVAL / "regen_full_01.borderline_sensitivity.json").write_text(json.dumps(out, indent=1) + "\n")
        print(json.dumps({k: v for k, v in out.items() if k != "_about"}, indent=1))
    elif cmd == "combine":
        suffix = "_before_br" if "--before-br" in sys.argv else ""
        names, out_name = (("regen_full_01",), "final_regular_regen.json") if "--regen" in sys.argv else \
            (SETS, f"final_regular{suffix}.json")
        parts = [(s, {"box", "calendar", "linear", "slack"}, EVAL / f"{s}.adjudicated{suffix}.json") for s in names
                 if (EVAL / f"{s}.adjudicated{suffix}.json").exists()]
        result = combine(parts)
        (EVAL / out_name).write_text(json.dumps(result, indent=1) + "\n")
        print(json.dumps({k: result[k] for k in ("parts", "final", "by")}, indent=1))
    elif cmd == "qwen":
        suffix = "_before_br" if "--before-br" in sys.argv else ""
        if suffix:
            use_rulings_before_br()
        runs, parts = QWEN / "runs", []
        for run, domains in (("full_02", {"box"}), ("full_03", {"calendar", "linear", "slack"}),
                             ("full_04", {"box", "calendar", "linear", "slack"})):
            adj = adjudicate(run, runs / f"{run}.score.json", runs / f"judged_{run}" / run, runs / run, stalls=False)
            path = EVAL / f"qwen_{run}.adjudicated{suffix}.json"
            path.write_text(json.dumps(adj, indent=1) + "\n")
            parts.append((run, domains, path))
        result = combine(parts)
        (EVAL / f"qwen_final_regular{suffix}.json").write_text(json.dumps(result, indent=1) + "\n")
        print(f"Qwen{suffix}:", result["final"], "| left out:", len(result["left_out_tests"]),
              "| not counted:", len(result["trials_not_counted"]))
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
