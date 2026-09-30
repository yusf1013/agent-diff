"""What else the Sol round's runs show (the brief's question 4), beside Qwen's runs of the same tests: statuses and
infrastructure errors, attempts, timings, tool calls, tokens (input, cached, output, reasoning), compactions, visible
text, and awareness remarks. Reads the run records only, never a verdict or a mechanical triage. No model calls.

Awareness copies openclaw_eval_01/test_awareness.py's pattern and scan (`AWARE`, `texts`). Sol's steps carry no
thinking: its visible words are its final answer and occasional reasoning summaries. So Qwen's rate is given twice
on the same tests, over all its words (as the Qwen round counted it) and over its final answers only, the one
source both agents share.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.observe   # eval/observations.json

Qwen's records of the same tests: 6a's Box tests from full_02 (ids unchanged), its Calendar, Linear and Slack tests
from full_03, 6b's from full_04; policy units from the population runs (Box's first-pass units from the looks).
"""
from __future__ import annotations

import json
import statistics
from collections import Counter
from pathlib import Path

from grounding.runs.autogen_01.kit import bundle
from grounding.runs.autogen_01.kit.judge import latest
from grounding.runs.openclaw_eval_01 import rulings
from grounding.runs.openclaw_eval_01.test_awareness import AWARE, texts
from grounding.runs.sol_eval_01.kit.score import stalled

STUDY = Path(__file__).resolve().parents[1]
RUNS = STUDY / "runs"
QRUNS = STUDY.parent / "openclaw_eval_01" / "runs"
SETS = ("regular_p4", "regular_6b", "policy_absence", "policy_underspecified")


def sol_attempts(name: str):
    """(trial, case_id, latest attempt, all attempts) for a Sol set."""
    run = RUNS / name
    seen = {}
    for summary in sorted(run.glob("t*/*/attempt-*/execution_summary.json")):
        trial, case_id = summary.parent.parts[-3], summary.parent.parts[-2]
        seen.setdefault((trial, case_id), []).append(summary.parent)
    for (trial, case_id), attempts in sorted(seen.items()):
        yield trial, case_id, attempts[-1], attempts


def qwen_attempt(case_id: str, trial: str, domain: str, sixb: bool, mode: str | None) -> Path | None:
    """Qwen's latest attempt of the same test in the runs its final numbers used."""
    if mode:
        folders = [QRUNS / "policy" / f"solve_population_{'6b_' if sixb else ''}{mode}"] + \
                  sorted((QRUNS / "policy").glob(f"solve_{mode}_look*"))
    elif sixb:
        folders = [QRUNS / "full_04"]
    else:
        folders = [QRUNS / ("full_02" if domain == "box" else "full_03")]
    for f in folders:
        if (f / trial / case_id).exists():
            return latest(f, trial, case_id)
    return None


def usage_row(attempt: Path) -> dict:
    s = json.loads((attempt / "execution_summary.json").read_text())
    u, flags = s.get("usage") or {}, s.get("flags") or {}
    return {"status": s.get("status"), "termination": s.get("termination"), "error": s.get("error"),
            "seconds": (s.get("turn_durations_s") or [None])[0], "tool_calls": s.get("turns"),
            "requests": u.get("requests"), "input": u.get("input_tokens"), "cached": u.get("cached_input_tokens"),
            "output": u.get("output_tokens"), "reasoning": u.get("reasoning_tokens"),
            "compactions": flags.get("compactions"), "stall": stalled(attempt),
            "over_budget": rulings.over_budget(attempt) and not stalled(attempt),
            "reclassified": bool(s.get("reclassified_from"))}


def aware(attempt: Path) -> dict:
    record = bundle.solver_record(attempt)
    final_path = attempt / "solver" / "final_response.md"
    final = final_path.read_text() if final_path.exists() else ""
    hits_all, hits_final, visible_steps = [], [], 0
    for where, text in texts(record, final):
        if where != "final" and text.strip():
            visible_steps += 1
        for m in AWARE.finditer(text):
            hit = {"where": where, "match": m.group(0), "context": text[max(0, m.start() - 160):m.end() + 160]}
            hits_all.append(hit)
            if where == "final":
                hits_final.append(hit)
    return {"all": hits_all, "final": hits_final, "visible_steps": visible_steps,
            "steps": len(record.get("steps", []))}


def dist(values: list) -> dict:
    v = sorted(x for x in values if x is not None)
    if not v:
        return {"n": 0}
    return {"n": len(v), "sum": round(sum(v), 1), "median": round(statistics.median(v), 1),
            "p90": round(v[int(0.9 * (len(v) - 1))], 1), "max": round(v[-1], 1)}


def summarize(rows: list[dict]) -> dict:
    done = [r for r in rows if r["status"] == "completed"]
    return {"trials": len(rows), "status": dict(Counter(r["status"] for r in rows)),
            "termination": dict(Counter(str(r["termination"]) for r in done)),
            "stalls": sum(r["stall"] for r in rows), "reclassified": sum(r["reclassified"] for r in rows),
            "over_budget": sum(r["over_budget"] for r in rows),
            "attempts": dict(Counter(r.get("attempts", 1) for r in rows)),
            **{k: dist([r[k] for r in done]) for k in ("seconds", "tool_calls", "requests", "input", "cached",
                                                        "output", "reasoning", "compactions")},
            "trials_with_reasoning_tokens": sum(1 for r in done if (r["reasoning"] or 0) > 0),
            "cached_share_of_input": round(sum(r["cached"] or 0 for r in done) / max(1, sum(r["input"] or 0
                                                                                              for r in done)), 3)}


def main():
    suites = {s: {m["case_id"]: m for m in json.loads((STUDY / "cases" / s / "suite.json").read_text())}
              for s in ("regular_p4", "regular_6b")}
    out = {"_about": __doc__.split("\n\n")[0], "sets": {}}
    for name in SETS:
        mode = name.split("_", 1)[1] if name.startswith("policy") else None
        if not (RUNS / name).exists():
            continue
        sol_rows, qwen_rows, aw = [], [], {"sol": [], "qwen_all": [], "qwen_final": [], "pairs": 0}
        sol_visible, sol_steps = 0, 0
        for trial, case_id, attempt, attempts in sol_attempts(name):
            row = {**usage_row(attempt), "attempts": len(attempts), "trial": f"{trial}/{case_id}"}
            sol_rows.append(row)
            case = json.loads((attempt / "case.json").read_text())
            sixb = case_id in suites["regular_6b"] if not mode else \
                (STUDY.parent / "completion_01" / "suite" / "units" / case["domain"] / f"{case_id}.json").exists()
            q = qwen_attempt(case_id, trial, case["domain"], sixb, mode)
            if q is not None:
                qwen_rows.append({**usage_row(q), "trial": f"{trial}/{case_id}"})
            if row["status"] != "completed":
                continue
            a = aware(attempt)
            sol_visible += a["visible_steps"]
            sol_steps += a["steps"]
            if a["all"]:
                aw["sol"].append({"trial": f"{trial}/{case_id}", "hits": a["all"]})
            if q is not None and json.loads((q / "execution_summary.json").read_text()).get("status") == "completed":
                aw["pairs"] += 1
                qa = aware(q)
                if qa["all"]:
                    aw["qwen_all"].append({"trial": f"{trial}/{case_id}", "hits": qa["all"]})
                if qa["final"]:
                    aw["qwen_final"].append({"trial": f"{trial}/{case_id}", "hits": qa["final"]})
        done = sum(1 for r in sol_rows if r["status"] == "completed")
        out["sets"][name] = {
            "sol": summarize(sol_rows), "qwen_same_tests": summarize(qwen_rows),
            "infrastructure_errors": [{"trial": r["trial"], "error": r["error"], "attempts": r["attempts"]}
                                      for r in sol_rows if r["status"] != "completed"],
            "sol_steps_with_visible_text": f"{sol_visible}/{sol_steps}",
            "awareness": {"sol_trials_remarking": f"{len(aw['sol'])}/{done}",
                          "sol_words": dict(Counter(h["match"].lower() for r in aw["sol"] for h in r["hits"])),
                          "qwen_trials_remarking_any_text": f"{len(aw['qwen_all'])}/{aw['pairs']}",
                          "qwen_trials_remarking_final_answer": f"{len(aw['qwen_final'])}/{aw['pairs']}",
                          "sol_hits": aw["sol"]}}
        s = out["sets"][name]
        print(name, "sol", {k: s["sol"][k] for k in ("trials", "status", "stalls", "over_budget")},
              "| seconds", s["sol"]["seconds"], "| awareness", {k: v for k, v in s["awareness"].items()
                                                               if k.startswith(("sol_trials", "qwen"))})
    (STUDY / "eval" / "observations.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
