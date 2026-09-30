"""Generate the drawn briefs with the frozen Phase 4 pipeline, the writer on the self-hosted Qwen (backend.py), the cold
reader on Muse.

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py grounding.runs.qwen_writer_01.generate \
        --run grounding/runs/qwen_writer_01/runs/gen_NN [--concurrency 4] [--only ID ...]

Without `--only`, the twelve briefs drawn in plan.json. Everything else is autogen_02's Phase 4 entry point
(`autogen_02/kit/generate.py`: its replica notes and its robustness fix) over autogen_01's orchestrator, unchanged.
Workspaces go under /tmp/qwen-writer-01/ws (Phase 4's were under /tmp/autogen-02/ws/gen).
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

os.environ.setdefault("AUTOGEN_WORK", "/tmp/qwen-writer-01/ws")
if os.environ.get("AUTOGEN_BACKEND") != "muse":
    raise SystemExit("set AUTOGEN_BACKEND=muse: the cold reader stays on Muse")

from grounding.runs.qwen_writer_01 import backend  # noqa: E402
from grounding.runs.autogen_02.kit import generate as phase4  # noqa: E402

HERE = Path(__file__).resolve().parent


def main():
    args = sys.argv[1:]
    run = Path(args[args.index("--run") + 1]).resolve()
    run.mkdir(parents=True, exist_ok=True)
    backend.install(clamp_log=run / "clamps.jsonl")  # the window relay logs each lowered max_tokens there
    if "--only" not in args:
        drawn = json.loads((HERE / "plan.json").read_text())["drawn"]
        args += ["--only", *[sid for domain in sorted(drawn) for sid in drawn[domain]]]
    sys.argv = ["generate", *args]
    phase4.main()


if __name__ == "__main__":
    main()
