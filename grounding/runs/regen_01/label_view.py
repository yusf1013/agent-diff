"""Print a blind-sample trial for my label, before any verdict on it: the evidence judge v2 reads (autogen_01's
bundle: request, candidates, every step, the final answer, the state diff), without the mechanical attribution, so
the label is independent of the triage as well as of the judge. Only I read this; it never reaches an agent.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.label_view RUN/TRIAL/CASE [...]
    python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.label_view --list RUN   # unlabelled keys
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import bundle
from grounding.runs.autogen_01.kit import judge as v1
from grounding.runs.autogen_02.kit.judge2 import form_of, triage

HERE = Path(__file__).resolve().parent


def show(key: str) -> str:
    run, trial, case_id = key.split("/")
    run_dir = HERE / "runs" / run
    attempt = v1.latest(run_dir, trial, case_id)
    case, summary, tri = triage(run, trial, attempt)
    targets = len(case["references"][0]["expected"])
    form = form_of(case_id) or ("cover (target and all decoys)" if targets else "no-target test")
    text = bundle.build(case, attempt, form, tri, summary)
    text = text.split("## Mechanical attribution")[0].rstrip()
    return f"{'=' * 100}\nKEY {key}  (attempt {attempt.name})\n{text}\n"


def main():
    args = sys.argv[1:]
    if args and args[0] == "--list":
        run = args[1]
        blind = json.loads((HERE / "eval" / f"blind_{run}.json").read_text())["keys"]
        labels_path = HERE / "eval" / f"labels_{run}.json"
        labelled = set(json.loads(labels_path.read_text())) if labels_path.exists() else set()
        print("\n".join(k for k in blind if k not in labelled))
        return
    for key in args:
        print(show(key))


if __name__ == "__main__":
    main()
