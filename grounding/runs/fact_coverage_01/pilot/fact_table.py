"""Per-fact sensitivity across designs: which facts Qwen fails, and in which forms.

    python -m grounding.runs.fact_coverage_01.pilot.fact_table <run dirs...> [--md out.md]

Forms: fact-sensitive = target present, absence permitted (told/contrast/ALT sweep);
presupposing = no-target request that presupposes a match (packed absent, isolated, plain, far).
A fact 'fails' in a run when the (manually corrected) outcome is incorrect and the fact is among the exposed ones.
Runs where the fact's near-miss was present but not acted on count as 'held'.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

SENSITIVE = {"present", "absent-told"}


def form(row):
    cid = row["case_id"]
    if row["design"] in SENSITIVE or cid.startswith(("CON-", "ALT-")):
        if cid.startswith("CON-") and cid.endswith("-plain"):
            return "sensitive-plain"
        return "sensitive"
    return "presupposing"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", nargs="+")
    parser.add_argument("--md")
    args = parser.parse_args()
    out = Path("/tmp/fact_rows.json")
    subprocess.run([sys.executable, "-m", "grounding.runs.fact_coverage_01.pilot.results", *args.runs, "--json", str(out)],
                   check=True, capture_output=True)
    rows = [r for r in json.loads(out.read_text()) if r.get("status") == "completed" and r["outcome"] != "invalid_env"]
    stats = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    for r in rows:
        f = form(r)
        present = set(r.get("claims", []))
        if r.get("isolated"):
            present = {r["isolated"]}
        for req in present | set(r["exposed"]):
            stats[req][f][1] += 1
            stats[req][f][0] += req in r["exposed"] and r["outcome"] in ("incorrect", "recovered")
    lines = ["| Fact | Fact-sensitive: failed / runs | Plain near-miss (sensitive) | Presupposing: failed / runs |",
             "|---|---|---|---|"]
    order = sorted(stats, key=lambda k: (-stats[k]["sensitive"][0], -stats[k]["presupposing"][0], k))
    for req in order:
        d = stats[req]
        cell = lambda k: f"{d[k][0]}/{d[k][1]}" if d[k][1] else "-"
        lines.append(f"| {req} | {cell('sensitive')} | {cell('sensitive-plain')} | {cell('presupposing')} |")
    sens = [k for k in stats if stats[k]["sensitive"][1]]
    failing = [k for k in sens if stats[k]["sensitive"][0]]
    summary = (f"\nFacts tested in a fact-sensitive form: {len(sens)}; failed at least once: {len(failing)}. "
               f"Facts tested only in presupposing forms: {len([k for k in stats if not stats[k]['sensitive'][1]])}.")
    text = "\n".join(lines) + "\n" + summary + "\n"
    print(text)
    if args.md:
        Path(args.md).write_text(text)


if __name__ == "__main__":
    main()
