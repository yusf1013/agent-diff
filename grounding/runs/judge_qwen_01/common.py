"""Shared paths and helpers: the final executions, Muse's saved verdicts and prompts, and the reference labels.

No model calls. Reference labels are read only by `labels()`, which the replay never calls.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
OC = RUNS / "openclaw_eval_01" / "runs"
CONCISE = RUNS / "report_01" / "numbers" / "concise.json"
SEP = "\n\n---\n\n"
ASK = "\n\nGive your verdict for this trial."
FAIL = {"incorrect", "presented"}
NONFAIL = {"correct", "correct_absent", "false_absence", "incomplete"}
VOID = {"artifact", "not_established"}


def load(path: Path):
    return json.loads(Path(path).read_text())


def cls(outcome: str | None) -> str | None:
    """blind_review_01's three groups: failure, nonfailure (no established grounding failure), void."""
    if outcome in FAIL:
        return "fail"
    if outcome in NONFAIL:
        return "nonfail"
    if outcome in VOID:
        return "void"
    return None


def kind_of(key: str) -> str:
    run = key.split("/")[0]
    if run.startswith("full_"):
        return "regular"
    return "absence" if "absence" in run else "underspecified"


def run_dir(key: str) -> Path:
    run = key.split("/")[0]
    return OC / run if run.startswith("full_") else OC / "policy" / run


def muse_dir(key: str) -> Path:
    """Where judge v2 on Muse left this execution's verdict and call evidence (report_01's concise.py convention)."""
    run = key.split("/")[0]
    if run.startswith("full_"):
        return OC / f"judged_{run}" / key
    return OC / "policy" / run.replace("solve_", "judged_", 1) / key


def final_keys() -> list[str]:
    return load(CONCISE)["final_execution_keys"]


def judged_keys() -> list[str]:
    """The final executions with a saved LLM verdict (2,139)."""
    return [k for k in final_keys() if (muse_dir(k) / "verdict.json").exists()]


def muse_verdict(key: str) -> dict:
    return load(muse_dir(key) / "verdict.json")


def attempt_path(key: str) -> Path:
    """The attempt folder Muse judged, in this checkout."""
    run, trial, case_id = key.split("/")
    return run_dir(key) / trial / case_id / Path(muse_verdict(key)["attempt"]).name


def muse_prompt(key: str) -> tuple[str, str]:
    """(system, user) exactly as Muse received them: Muse has no system-prompt flag, so agent._run_muse sent
    system + SEP + user as one message; judge.system.md holds the system part."""
    d = muse_dir(key)
    result = sorted(d.glob("*-judge.result.json"))[-1]
    saved = (d / result.name.replace(".result.json", ".prompt.md")).read_text()
    system = (d / "judge.system.md").read_text()
    if not saved.startswith(system + SEP):
        raise ValueError(f"{key}: the saved prompt does not start with judge.system.md")
    return system, saved[len(system) + len(SEP):]


def labels() -> dict:
    """Reference labels on final executions: the lead's 310 retained blind labels and blind_review_01's effective
    labels (all 200; `has_llm` marks the 133 with a saved LLM verdict). Value: outcome, exposed, mechanism, source."""
    final = set(final_keys())
    out = {}
    for f in sorted((RUNS / "openclaw_eval_01" / "eval").glob("labels_*/*_blind.json")):
        for key, v in load(f).items():
            if key in final and isinstance(v, dict):
                assert key not in out
                out[key] = {"outcome": v["outcome"], "exposed": sorted(v.get("exposed", [])),
                            "mechanism": v.get("mechanism"), "source": "lead", "file": str(f.relative_to(RUNS))}
    br = RUNS / "blind_review_01"
    effective = {x["blind_id"]: x for x in load(br / "effective_labels.json")}
    for row in csv.DictReader((br / "samples.csv").open()):
        e = effective[row["blind_id"]]
        assert row["key"] in final and row["key"] not in out
        out[row["key"]] = {"outcome": e["outcome"], "exposed": sorted(e.get("exposed") or []),
                           "mechanism": e.get("mechanism"), "source": "blind_review_01", "blind_id": row["blind_id"],
                           "review_status": e.get("review_status"), "has_llm": row["source"] == "LLM"}
    return out
