"""Rerun selected manual Slack cases on the currently served Qwen, via the unchanged Purdue comparison runner.

    python -m grounding.runs.fact_coverage_01.pilot.slack_bridge --out <new dir> --cases W08-base ...

Only the model name differs from grounding/runs/purdue_comparison_01 (qwen3.6:27b is no longer served).
"""
from __future__ import annotations

import sys

from grounding.solver.slack import compare_purdue

compare_purdue.MODELS["qwen36"]["model"] = "qwen3.8:27b"

if __name__ == "__main__":
    compare_purdue.main()
