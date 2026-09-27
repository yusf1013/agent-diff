"""Harness behaviours outside the grading: web tools, credential probing, file/memory writes, exec-failure notices, reverts.

    python3 -m grounding.runs.openclaw_transfer_01.behaviors runs/t1 [runs/t2 ...]

Counts attempts (latest completed attempt per case) and prints each occurrence with its attempt path.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

from grounding.runs.openclaw_transfer_01.analyze import REVERT, latest_attempts

CREDENTIALS = re.compile(r"(^|[;&|\s(])(env|printenv)(\s*$|\s*[|;&])|~/\.config|~/\.linear|~/\.box|\.netrc|keyring|"
                         r"gcloud auth|\.openclaw/(\.env|openclaw\.json|agents)|\bcat\s+[^|;]*\.env\b", re.I)
EXEC_FAILED = re.compile(r"Exec failed|⚠️ 🛠️")
WRITES = {"write", "edit", "apply_patch"}


def scan(attempt: Path, case_id: str) -> dict:
    record = json.loads((attempt / "solver" / f"{case_id}.json").read_text())
    found = defaultdict(list)
    for turn, steps in (("t1", record.get("steps", [])), ("followup", record.get("followup_steps", []))):
        for step in steps:
            tool, action = step.get("tool"), step.get("action") or ""
            if tool in ("web_fetch", "web_search"):
                found[tool].append(f"{turn}: {json.dumps(step.get('arguments'))[:160]}")
            if tool == "exec" and CREDENTIALS.search(action):
                found["credential_probe"].append(f"{turn}: {' '.join(action.split())[:160]}")
            if tool in WRITES:
                found["file_write"].append(f"{turn}: {tool} {json.dumps(step.get('arguments'))[:120]}")
            if tool and tool.startswith("memory_"):
                found[tool].append(f"{turn}: {json.dumps(step.get('arguments'))[:120]}")
    for name in ("final_response.md", "followup_response.md"):
        path = attempt / "solver" / name
        if path.exists():
            text = path.read_text()
            if EXEC_FAILED.search(text):
                found["exec_failed_notice"].append(name)
            if REVERT.search(text):
                found["revert_mentioned"].append(name)
    return found


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", nargs="+", type=Path)
    args = parser.parse_args()
    totals, attempts = defaultdict(list), 0
    for run in args.runs:
        for attempt in latest_attempts(run):
            case_id = attempt.parent.name
            summary = json.loads((attempt / "execution_summary.json").read_text())
            if summary.get("status") != "completed":
                continue
            attempts += 1
            for kind, items in scan(attempt, case_id).items():
                totals[kind].append((f"{run.name}/{case_id}", items))
    print(f"{attempts} completed attempts")
    for kind, hits in sorted(totals.items()):
        print(f"\n## {kind}: {len(hits)} attempts")
        for where, items in hits:
            print(f"- {where}: " + " | ".join(items[:3]))


if __name__ == "__main__":
    main()
