"""Smoke test: OpenHands (software-agent-sdk) with the self-hosted Qwen, one trivial terminal task.

    OPENHANDS_SUPPRESS_BANNER=1 ~/.agentdiff-harness/openhands/bin/python grounding/integrations/openhands/smoke.py

Checks the install, the self-host's tool calling through OpenHands's own loop (TerminalTool), and what the event log
records. Free: the self-hosted Qwen. Writes nothing outside a temporary workspace and its persistence folder.
"""
from __future__ import annotations

import json
import os
import tempfile
import time
from pathlib import Path

from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.terminal import TerminalTool

KEY = (Path.home() / "qwen-selfhost/secrets/api_key").read_text().strip()


def main():
    work = Path(tempfile.mkdtemp(prefix="oh-smoke-"))
    llm = LLM(model="openai/qwen3.8-27b", base_url="http://127.0.0.1:18000/v1", api_key=KEY,
              native_tool_calling=True, reasoning_effort="medium", usage_id="smoke")
    agent = Agent(llm=llm, tools=[Tool(name=TerminalTool.name)])
    events = []
    conv = Conversation(agent=agent, workspace=str(work), persistence_dir=str(work / ".oh"),
                        callbacks=[lambda e: events.append(e)])
    t0 = time.time()
    conv.send_message("Run the shell command `echo openhands-smoke-ok` and tell me exactly what it printed.")
    conv.run()
    kinds = {}
    for e in events:
        kinds[type(e).__name__] = kinds.get(type(e).__name__, 0) + 1
    final = [e for e in events if type(e).__name__ == "MessageEvent"]
    print(json.dumps({"seconds": round(time.time() - t0, 1), "event_kinds": kinds,
                      "last_message": str(getattr(final[-1], "llm_message", final[-1]))[:600] if final else None,
                      "metrics": str(llm.metrics.get_snapshot() if hasattr(llm, "metrics") else "")[:300],
                      "workspace": str(work)}, indent=1))


if __name__ == "__main__":
    main()
