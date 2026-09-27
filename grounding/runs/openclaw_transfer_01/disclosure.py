"""Wrong actions in fact-sensitive forms: did the reply disclose the mismatch, or did only the reasoning notice it?

    python3 -m grounding.runs.openclaw_transfer_01.disclosure rows.json [--harness toy|openclaw] > listing.txt

Prints one compact entry per wrong action (reply, and reasoning lines that mention a mismatch) for manual
classification; labels go to disclosure_labels.json as {"<harness>/<run>/<case>": "disclosed" | "noticed_silent" |
"unnoticed"}.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from grounding.runs.openclaw_transfer_01.analyze import primary, toy_rows

HERE = Path(__file__).resolve().parent
TOY_RUNS = HERE.parent / "fact_coverage_01" / "pilot" / "runs"
SENSITIVE = ("present", "told-packed", "contrast-alt", "contrast-plain", "alt-sweep", "wording")
MISMATCH = re.compile(r"\b(not|isn't|wasn't|doesn't|didn't|rather than|instead|however|although|but|mismatch|"
                      r"discrepanc|trap|nuance|note|flag|mention|closest|actually)\b", re.I)


def toy_texts(row: dict) -> tuple[str, str]:
    attempts = sorted((TOY_RUNS / row["run"] / row["case_id"]).glob("attempt-*"))
    for attempt in reversed(attempts):
        summary = json.loads((attempt / "execution_summary.json").read_text())
        if summary.get("status") == "completed":
            record = json.loads((attempt / "solver" / f"{row['case_id']}.json").read_text())
            reasoning = []
            for step in record.get("steps", []):
                for block in step.get("response", {}).get("content", []):
                    text = block.get("text") or ""
                    if block.get("type") == "thinking":
                        reasoning.append(text)
                    reasoning += re.findall(r"<thinking>(.*?)</thinking>", text, re.S)
            return record.get("final") or "", "\n".join(reasoning)
    return "", ""


def openclaw_texts(row: dict) -> tuple[str, str]:
    attempt = Path(row["attempt"])
    record = json.loads((attempt / "solver" / f"{row['case_id']}.json").read_text())
    reasoning = [(s.get("thinking") or "") + "\n" + (s.get("text") or "") for s in record.get("steps", [])]
    return (attempt / "solver/final_response.md").read_text(), "\n".join(reasoning)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("rows", type=Path, help="analyze.py --json output (OpenClaw rows)")
    parser.add_argument("--harness", choices=["toy", "openclaw"], default="openclaw")
    args = parser.parse_args()
    if args.harness == "toy":
        rows = primary(toy_rows())
    else:
        rows = primary([r for r in json.loads(args.rows.read_text()) if r.get("status") == "completed"])
    for row in rows:
        if row.get("condition") not in SENSITIVE or row.get("outcome") != "incorrect":
            continue
        reply, reasoning = (toy_texts if args.harness == "toy" else openclaw_texts)(row)
        hits = [s.strip() for s in re.split(r"(?<=[.!?])\s+", reasoning) if MISMATCH.search(s)][-4:]
        print(f"### {args.harness}/{row['run']}/{row['case_id']}  exposed={row.get('exposed')}")
        print("REPLY:", " ".join(reply.split())[:500])
        for h in hits:
            print("  ~", " ".join(h.split())[:220])
        print()


if __name__ == "__main__":
    main()
