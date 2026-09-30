"""The generation half: Qwen's writer (the attempt that counts per brief, cases.py: runs/gen_02 or runs/gen_03) against
Muse's (autogen_02/runs/phase4_gen) on the drawn briefs.
No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.qwen_writer_01.compare_gen

Per brief and writer:
- **the pipeline's record:** status; scenario versions; check rounds (mechanical and replica findings answered) and
  reader rounds; the stage each rejected version stopped at; the writer's calls, wall time and tokens; the readers'
  calls and cost (Muse list and billed);
- **the scenario:** its near misses (decoys) by fact and family (F0 plain; F1-F8 substitutes, which the method
  prefers);
- **validity:** each near miss's verdict. Muse's are Phase 4's manual review (autogen_02/eval/phase4_review.json)
  under the PI's rulings (roadmap_01/known_defects.json: a near miss ruled flawed is flawed; a scenario ruled weak
  but valid is kept). Qwen's are my review (eval/review.json), under the same criteria. A fact is covered validly when
  the scenario is kept and at least one of its near misses on that fact is valid.

Writes eval/generation.json and prints the tables for the README.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from grounding.runs.qwen_writer_01 import cases

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
MUSE_GEN = RUNS / "autogen_02" / "runs" / "phase4_gen"
STOPPED = [HERE / "runs" / "gen_01_xhigh", HERE / "runs" / "gen_02"]  # runs stopped with briefs in progress
BRIEFS = RUNS / "autogen_02" / "inputs" / "briefs_phase4.json"
MUSE_REVIEW = RUNS / "autogen_02" / "eval" / "phase4_review.json"
QWEN_REVIEW = HERE / "eval" / "review.json"
KNOWN_DEFECTS = RUNS / "roadmap_01" / "known_defects.json"


def calls(gen: Path) -> list[dict]:
    log = gen / "calls.jsonl"
    return [json.loads(line) for line in log.read_text().splitlines() if line.strip()] if log.exists() else []


def muse_verdicts(sid: str, case: dict) -> tuple[str, dict]:
    """(scenario verdict, near miss -> verdict) under the rulings: the review's verdicts, with the PI's rulings
    replacing them where they exist."""
    review = json.loads(MUSE_REVIEW.read_text())[sid]
    doc = json.loads(KNOWN_DEFECTS.read_text())
    action = next((e["frozen_suite"] for e in doc["curated"] if e["id"] == sid), "keep")
    if action.startswith(("leave out", "dropped")):
        scenario = "left out"
    elif review["verdict"] == "flawed":  # the review's "flawed but usable": kept only by a ruling that says keep
        scenario = "weak but valid" if action.startswith("keep") and sid in {e["id"] for e in doc["curated"]} else \
            "flawed (no ruling)"
    else:
        scenario = review["verdict"]
    ruled = {n["witness"]: n["ruling"] for n in doc["near_misses"] if n["scenario"] == sid}
    decoys = {}
    for claim in case["references"][0]["claims"]:
        w = str(claim["witness"])
        v = ruled.get(w) or review["decoys"].get(w, "unreviewed")
        decoys[w] = "valid" if v.startswith("valid") else v
    return scenario, decoys


def qwen_verdicts(sid: str) -> tuple[str, dict] | None:
    if not QWEN_REVIEW.exists():
        return None
    review = json.loads(QWEN_REVIEW.read_text()).get(sid)
    if not review:
        return None
    return review["verdict"], {w: ("valid" if v["verdict"].startswith("valid") else v["verdict"])
                               for w, v in review["near_misses"].items()}


def side(gen: Path, sid: str, facts: list[str], verdicts) -> dict:
    outcome_path = gen / sid / "outcome.json"
    rows = [c for c in calls(gen) if c.get("label") == sid]
    writer = [c for c in rows if c["role"] == "writer"]
    readers = [c for c in rows if c["role"] == "reader"]
    out = {"status": "error" if (gen / sid / "error.txt").exists() else "missing"}
    if outcome_path.exists():
        o = json.loads(outcome_path.read_text())
        stages = Counter(h["stage"] for h in o["history"] if h["problems"])
        out = {"status": o["status"], "versions": o["versions"], "check_rounds": o["check_rounds"],
               "reader_rounds": o["reader_rounds"], "rejected_versions_by_stage": dict(stages),
               "seconds": o["seconds"]}
    out.update({
        "writer_calls": sum(1 for c in writer if not c.get("failed")),
        "writer_calls_failed": sum(1 for c in writer if c.get("failed")),
        "writer_seconds": round(sum(c.get("seconds") or 0 for c in writer), 1),
        "writer_output_tokens": sum(c.get("output_tokens") or 0 for c in writer),
        "writer_input_tokens": sum((c.get("input_tokens") or 0) + (c.get("cache_read_input_tokens") or 0)
                                   + (c.get("cache_creation_input_tokens") or 0) for c in writer),
        "writer_cost_usd_list": round(sum(c.get("cost_usd_list_price") or 0 for c in writer), 4),
        "reader_calls": len(readers),
        "reader_cost_usd_list": round(sum(c.get("cost_usd_list_price") or 0 for c in readers), 4),
        "reader_cost_usd_billed": round(sum(c.get("cost_usd_billed") or 0 for c in readers), 4)})
    case_path = gen / sid / "case.json"
    if out["status"] != "accepted" or not case_path.exists():
        out.update(facts_covered_validly=[], near_misses=[])
        return out
    case = json.loads(case_path.read_text())
    out["request"] = case["prompt"]
    claims = case["references"][0]["claims"]
    judged = verdicts(sid, case) if verdicts else None
    scenario_verdict, decoy_verdicts = judged if judged else ("unreviewed", {})
    out["scenario_verdict"] = scenario_verdict
    out["near_misses"] = [{"witness": str(c["witness"]), "fact": c["requirement"], "family": c.get("family"),
                           "verdict": decoy_verdicts.get(str(c["witness"]), "unreviewed"),
                           "contestable": c.get("contestable")} for c in claims]
    kept = scenario_verdict in ("valid", "weak but valid")
    out["families"] = dict(Counter(n["family"] for n in out["near_misses"]))
    out["facts_with_substitute"] = sorted({n["fact"] for n in out["near_misses"] if n["family"] not in ("F0", None)})
    out["facts_covered_validly"] = sorted({n["fact"] for n in out["near_misses"] if kept and n["verdict"] == "valid"}
                                          & set(facts))
    return out


def stopped_attempts(sid: str, counted: Path | None) -> list[dict]:
    """The brief's writer attempts in the stopped runs, other than the one that counts: writer time and output."""
    out = []
    for gen in STOPPED:
        folder = gen / sid
        if not folder.exists() or folder == counted:
            continue
        rows = [c for c in calls(gen) if c.get("label") == sid and c["role"] == "writer"]
        live = folder / "writer" / "live-transcript-at-stop.jsonl"
        steps, out_tokens = set(), 0
        if live.exists():
            for line in live.read_text().splitlines():
                e = json.loads(line)
                if e.get("type") == "assistant" and e["message"].get("id") not in steps:
                    steps.add(e["message"].get("id"))
                    out_tokens += (e["message"].get("usage") or {}).get("output_tokens") or 0
        out.append({"run": gen.name, "writer_calls_done": len(rows),
                    "writer_seconds_done": round(sum(c.get("seconds") or 0 for c in rows), 1),
                    "stopped_call_output_tokens": out_tokens if live.exists() else None})
    return out


def md(header, rows):
    return "\n".join(["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
                     + ["| " + " | ".join(str(x) for x in r) + " |" for r in rows])


def main():
    plan = json.loads((HERE / "plan.json").read_text())
    drawn = [sid for d in sorted(plan["drawn"]) for sid in plan["drawn"][d]]
    briefs = {b["scenario_id"]: b for b in json.loads(BRIEFS.read_text())}
    result = {"briefs": {}}
    for sid in drawn:
        facts = briefs[sid]["facts"]
        folder = cases.attempt(sid)
        qwen = side(folder.parent, sid, facts, lambda s, c: qwen_verdicts(s)) if folder else {"status": "not run"}
        qwen["run"] = folder.parent.name if folder else None
        qwen["stopped_attempts"] = stopped_attempts(sid, folder)
        result["briefs"][sid] = {"facts": facts, "muse": side(MUSE_GEN, sid, facts, muse_verdicts), "qwen": qwen}
    totals = {}
    for who in ("muse", "qwen"):
        sides = [b[who] for b in result["briefs"].values()]
        nm = [n for s in sides for n in s.get("near_misses", [])]
        totals[who] = {
            "briefs": len(sides), "accepted": sum(s["status"] == "accepted" for s in sides),
            "kept_after_review": sum(s.get("scenario_verdict") in ("valid", "weak but valid") for s in sides),
            "facts": sum(len(b["facts"]) for b in result["briefs"].values()),
            "facts_covered_validly": sum(len(s["facts_covered_validly"]) for s in sides),
            "versions": sum(s.get("versions", 0) for s in sides),
            "check_rounds": sum(s.get("check_rounds", 0) for s in sides),
            "reader_rounds": sum(s.get("reader_rounds", 0) for s in sides),
            "rejected_versions_by_stage": dict(sum((Counter(s.get("rejected_versions_by_stage", {})) for s in sides),
                                                   Counter())),
            "near_misses": len(nm), "near_misses_valid": sum(n["verdict"] == "valid" for n in nm),
            "families": dict(sorted(Counter(n["family"] for n in nm).items())),
            "plain_share": round(sum(n["family"] == "F0" for n in nm) / len(nm), 2) if nm else None,
            "writer_seconds": round(sum(s["writer_seconds"] for s in sides)),
            "writer_calls": sum(s["writer_calls"] for s in sides),
            "writer_calls_failed": sum(s["writer_calls_failed"] for s in sides),
            "writer_output_tokens": sum(s["writer_output_tokens"] for s in sides),
            "writer_cost_usd_list": round(sum(s["writer_cost_usd_list"] for s in sides), 2),
            "reader_calls": sum(s["reader_calls"] for s in sides),
            "reader_cost_usd_list": round(sum(s["reader_cost_usd_list"] for s in sides), 3),
            "reader_cost_usd_billed": round(sum(s["reader_cost_usd_billed"] for s in sides), 3)}
    result["totals"] = totals
    (HERE / "eval").mkdir(exist_ok=True)
    (HERE / "eval" / "generation.json").write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n")
    rows = []
    for sid, b in result["briefs"].items():
        for who in ("muse", "qwen"):
            s = b[who]
            rows.append([sid if who == "muse" else "", who, s["status"], s.get("versions", "-"),
                         s.get("check_rounds", "-"), s.get("reader_rounds", "-"),
                         ", ".join(f"{k} {v}" for k, v in sorted(s.get("rejected_versions_by_stage", {}).items())) or "-",
                         f"{s['writer_seconds'] / 60:.1f}", s.get("scenario_verdict", "-"),
                         " ".join(n["family"] or "?" for n in s.get("near_misses", [])) or "-",
                         f"{len(s['facts_covered_validly'])}/{len(b['facts'])}"])
    print(md(["Brief", "Writer", "Status", "Versions", "Check rounds", "Reader rounds", "Rejected at",
              "Writer min", "Review", "Near-miss families", "Facts valid"], rows))
    print(json.dumps(totals, indent=1))


if __name__ == "__main__":
    main()
