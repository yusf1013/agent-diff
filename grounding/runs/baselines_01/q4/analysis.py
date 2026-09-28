"""Question 4: why the naive judges (J0, J1) came out close to judge v2. Existing data only; no model calls.

    python3 grounding/runs/baselines_01/q4/analysis.py      # writes q4/numbers.json and prints it

A. How much of the judging the answer key does before any LLM reads a trial: openclaw_eval_01's full_02 run, the
   mechanical triage (autogen_01's select_run: "clean" = provisional correct or correct_absent) against judge v2.
B. J0's and J1's recall split by how the failure happened (the mechanism in my hand labels): an agent that saw the
   mismatch and accepted it usually says so; one that misread or skipped the check does not.
C. The trials 6c left out: void labels (artifact, not established), which no naive judge read, and what judge v2
   said on them.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
RUNS = REPO / "grounding/runs"
JB = RUNS / "judge_baselines_01"
OC = RUNS / "openclaw_eval_01"
A2 = RUNS / "autogen_02"
MISTAKE = {"incorrect", "presented"}


def triage_vs_judge() -> dict:
    selected = json.loads((OC / "runs/judge_full_02.trials.json").read_text())
    verdicts = {"/".join(p.parts[-3:-1]): json.loads(p.read_text())
                for p in (OC / "runs/judged_full_02").rglob("verdict.json")}
    trials = len(list((OC / "runs/full_02").glob("t*/*/attempt-*/execution_summary.json")))
    non_clean = [i for i in selected if "provisional" in i and not i.get("clean_sample")]
    sampled_clean = [i for i in selected if i.get("clean_sample") or i.get("blind_sample")]
    rows = Counter()
    for i in selected:
        v = verdicts[f"{i['trial']}/{i['case_id']}"]
        group = "blind" if i.get("blind_sample") else "clean_sample" if i.get("clean_sample") else "non_clean"
        rows[(group, i.get("provisional") or v.get("provisional"), v["outcome"])] += 1
    failures = {k: n for k, n in rows.items() if k[2] in MISTAKE}
    flagged = sum(n for k, n in failures.items() if k[1] == "incorrect")
    clean_changed = sum(n for k, n in rows.items() if k[0] != "non_clean" and k[2] not in ("correct", "correct_absent"))
    return {
        "trials": trials,
        "clean": trials - len(non_clean),
        "non_clean": len(non_clean),
        "clean_checked_by_judge": len(sampled_clean),
        "clean_changed_by_judge": clean_changed,
        "failures_after_judge": sum(failures.values()),
        "failures_flagged_incorrect_by_triage": flagged,
        "triage_incorrect_voided_by_judge": rows[("non_clean", "incorrect", "artifact")],
        "triage_uncertain_resolved_correct": sum(n for k, n in rows.items() if k[0] == "non_clean"
                                                 and k[1] in ("presented?", "absent_unclear", "not_established",
                                                              "attempted?") and k[2] in ("correct", "correct_absent")),
        "table": {" | ".join(map(str, k)): n for k, n in sorted(rows.items(), key=str)},
    }


def label_index() -> dict:
    """(label file name, run-relative key) -> label, for every hand label the judge baselines used."""
    files = sorted((A2 / "eval/labels_phase1").glob("*.json")) + \
        sorted(p for p in (A2 / "eval/labels_phase3").glob("*.json") if p.name != "attempts.json") + \
        sorted((A2 / "eval/labels_phase4").glob("*.json")) + \
        sorted(p for p in (OC / "eval").glob("labels_*/*_blind.json") if p.parent.name != "labels_full_01")
    out = {}
    for f in files:
        data = json.loads(f.read_text())
        for key, value in data.items():
            if isinstance(value, dict) and "outcome" in value:
                out[(f.name, key)] = value
    return out


def recall_by_mechanism() -> dict:
    trials = json.loads((JB / "trials.json").read_text())
    verdicts = defaultdict(dict)
    for variant in ("j0", "j1"):
        for p in (JB / "runs" / variant).rglob("verdict.json"):
            v = json.loads(p.read_text())
            verdicts[variant][v["key"]] = v.get("mistake")
    labels = label_index()
    out = {}
    prefix = "openclaw_eval_01/"
    for agent in ("openclaw", "qwen_toy_harness"):
        mine = [t for t in trials if t["truth"] is True and t["key"].startswith(prefix) == (agent == "openclaw")]
        table = defaultdict(lambda: {"failures": 0, "j0_found": 0, "j1_found": 0})
        missing = 0
        for t in mine:
            run_key = t["key"][len(prefix):] if agent == "openclaw" else t["key"]
            label = labels.get((t["label_file"], run_key))
            if label is None:
                missing += 1
                mechanism = "unknown"
            else:
                mechanism = label.get("mechanism") or "unknown"
            row = table[mechanism]
            row["failures"] += 1
            row["j0_found"] += bool(verdicts["j0"].get(t["key"]))
            row["j1_found"] += bool(verdicts["j1"].get(t["key"]))
        out[agent] = {"labels_not_found": missing, "by_mechanism": dict(sorted(table.items()))}
    return out


def void_trials() -> dict:
    trials = json.loads((JB / "trials.json").read_text())
    void = [t for t in trials if t["truth"] is None]
    judged = {v: {json.loads(p.read_text())["key"] for p in (JB / "runs" / v).rglob("verdict.json")}
              for v in ("j0", "j1")}
    return {
        "void": len(void),
        "by_label": dict(Counter(t["label"] for t in void)),
        "read_by_j0": sum(t["key"] in judged["j0"] for t in void),
        "read_by_j1": sum(t["key"] in judged["j1"] for t in void),
        "judge_v2_outcome_on_artifacts": dict(Counter(t["v2"] for t in void if t["label"] == "artifact")),
        "judge_v2_outcome_on_not_established": dict(Counter(t["v2"] for t in void if t["label"] == "not_established")),
    }


def main():
    result = {"A_answer_key_triage_full_02": triage_vs_judge(),
              "B_recall_by_mechanism": recall_by_mechanism(),
              "C_void_trials": void_trials()}
    (Path(__file__).parent / "numbers.json").write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
