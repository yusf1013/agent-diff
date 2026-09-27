"""Remove byte-for-byte or semantically duplicate evidence from finished attempts (nothing unique is deleted).

    python3 -m grounding.runs.openclaw_transfer_01.compact runs/<run> [--apply]

- solver/openclaw_turn*.stdout.txt when it holds exactly the JSON envelope saved as openclaw_turn*.json;
- environment/preflight/initial_state.json when it equals environment/initial_state.json, excluding the tables
  the backend writes on read (the runner already refused to run if they differed); prepared.json keeps its sha256.
Each removal is recorded in the attempt's execution_summary.json under "compacted".
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

VOLATILE = {"calendar": {"calendar_sync_tokens"}}


def same_envelope(stdout: Path, envelope: Path) -> bool:
    text = stdout.read_text(errors="replace")
    start = text.find("{")
    if start < 0 or text[:start].strip():
        return False
    try:
        parsed, end = json.JSONDecoder().raw_decode(text[start:])
    except json.JSONDecodeError:
        return False
    return not text[start + end:].strip() and parsed == json.loads(envelope.read_text())


def digest(state: dict, domain: str) -> str:
    kept = {k: v for k, v in state.items() if k not in VOLATILE.get(domain, set())}
    return hashlib.sha256(json.dumps(kept, sort_keys=True).encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    saved, removed = 0, 0
    for attempt in sorted(args.run.glob("*/attempt-*")):
        summary_path = attempt / "execution_summary.json"
        summary = json.loads(summary_path.read_text())
        if summary.get("status") not in ("completed", "infrastructure_error"):
            continue
        domain = summary.get("domain", "")
        victims = []
        for stdout in sorted((attempt / "solver").glob("openclaw_turn*.stdout.txt")):
            envelope = stdout.with_name(stdout.name.replace(".stdout.txt", ".json"))
            if envelope.exists() and same_envelope(stdout, envelope):
                victims.append(stdout)
        pre, run_state = attempt / "environment/preflight/initial_state.json", attempt / "environment/initial_state.json"
        if pre.exists() and run_state.exists():
            if digest(json.loads(pre.read_text()), domain) == digest(json.loads(run_state.read_text()), domain):
                victims.append(pre)
        for path in victims:
            saved += path.stat().st_size
            removed += 1
            if args.apply:
                path.unlink()
        if args.apply and victims:
            summary.setdefault("compacted", []).extend(str(p.relative_to(attempt)) for p in victims)
            summary_path.write_text(json.dumps(summary, indent=1))
    print(f"{'removed' if args.apply else 'would remove'} {removed} duplicate files, {saved / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
