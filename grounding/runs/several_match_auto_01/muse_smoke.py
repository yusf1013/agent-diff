"""One Muse writer call with a trivial schema: confirms the binary, the sandbox and the account before the pipeline.

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.muse_smoke
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.autogen_01.kit import agent

HERE = Path(__file__).resolve().parent
SCHEMA = {"type": "object", "properties": {"plural": {"type": "string"}, "ok": {"type": "boolean"}},
          "required": ["plural", "ok"]}


def main():
    out = HERE / "runs" / "muse_smoke"
    result = agent.run(agent.Call(
        role="writer", workspace=Path("/tmp/sm-auto-01/ws-smoke"), log_dir=out, calls_log=out / "calls.jsonl",
        prompt='Rewrite this request so that it asks for every matching record, keeping every condition: "Delete '
               'Friday\'s architecture review that Kenji Sato attends as an optional guest." Answer with JSON: '
               '{"plural": <the rewritten request>, "ok": true}.',
        schema=SCHEMA, label="smoke", timeout=600))
    print(json.dumps({"answer": agent.structured(result), "billed": result["cost_usd_billed"],
                      "list": result["total_cost_usd"], "usage": result["usage"]}, indent=1))


if __name__ == "__main__":
    main()
