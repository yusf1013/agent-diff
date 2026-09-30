"""openclaw_eval_01's adjudication, unchanged, for this study's run under this study's rulings (rules.py). No model
calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.qwen_writer_01.adjudicate RUN

Reads runs/RUN.score.json and runs/judged_RUN/RUN/ in this folder; writes runs/RUN.adjudicated.json.
"""
from __future__ import annotations

import json
import sys

from grounding.runs.qwen_writer_01 import rules  # noqa: F401  (before anything reads the rulings)
from grounding.runs.openclaw_eval_01 import adjudicate

adjudicate.HERE = rules.HERE

if __name__ == "__main__":
    run = sys.argv[1]
    out = adjudicate.adjudicate(run)
    (rules.HERE / "runs" / f"{run}.adjudicated.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({k: out[k] for k in ("raw", "adjudicated", "facts_lost")}, indent=1))
    print(f"left out: {len(out['left_out_tests'])} tests; not counted: {len(out['trials_not_counted'])} trials; "
          f"over the solver's budget: {len(out['trials_over_budget'])} trials")
