"""Carry my rulings into roadmap_01/known_defects.json, which the runner, the policy stage and the scoring read
(openclaw_eval_01/rulings.py; the lead's decision of 2026-09-30: appended on this branch, in a block keyed by this
study's ids, for the lead to merge). No model calls; plain python3 is enough.

    python3 grounding/runs/regen_01/defects.py [--check]

- **Flawed near misses** (eval/review.json, a near miss whose verdict starts with "flawed") go to `near_misses`, by
  their original ids, with the group the verdict names.
- **Invalid policy variants** (eval/variant_review.json, `valid` false) go to `curated` as "leave out".
- **Invalid scenarios** (a scenario verdict starting with "invalid") go to `curated` as "leave out".
The entries this script wrote before (their `source` starts with SOURCE) are replaced, so it can be run again after
each review; nothing else in the file changes. --check prints the entries and writes nothing.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KNOWN = HERE.parent / "roadmap_01" / "known_defects.json"
SOURCE = "regen_01"
WHO = ("my validity review of regen_01 ({path}), under the PI's criteria of 2026-09-28 and the rulings in this file; "
       "for the PI to overrule")


def entries() -> tuple[list[dict], list[dict]]:
    review = json.loads((HERE / "eval" / "review.json").read_text())
    near, curated = [], []
    for sid, r in review.items():
        if sid.startswith("_"):
            continue
        if r["verdict"].startswith("invalid"):
            curated.append({"id": sid, "kind": "scenario: invalid", "note": r["verdict"],
                            "source": f"{SOURCE}: " + WHO.format(path="regen_01/eval/review.json"),
                            "for_new_agents": "leave out", "frozen_suite": "leave out"})
        for witness, verdict in r["decoys"].items():
            if not verdict.startswith("flawed"):
                continue
            group = re.search(r"group ([ABC])", verdict)
            near.append({"scenario": sid, "witness": witness, "ruling": "flawed",
                         "group": group.group(1) if group else None, "why": verdict,
                         "source": f"{SOURCE}: " + WHO.format(path="regen_01/eval/review.json")})
    variants = HERE / "eval" / "variant_review.json"
    if variants.exists():
        for unit, read in json.loads(variants.read_text()).get("dropf", {}).items():
            if not read["valid"]:
                curated.append({"id": unit, "kind": "test: drop-F variant, read as invalid", "note": read["note"],
                                "source": f"{SOURCE}: " + WHO.format(path="regen_01/eval/variant_review.json"),
                                "for_new_agents": "leave out", "frozen_suite": "leave out"})
    return near, curated


def main():
    near, curated = entries()
    if "--check" in sys.argv:
        print(json.dumps({"near_misses": near, "curated": curated}, indent=1, ensure_ascii=False))
        return
    doc = json.loads(KNOWN.read_text())
    mine = lambda e: str(e.get("source", "")).startswith(SOURCE + ":")  # noqa: E731
    doc["near_misses"] = [e for e in doc["near_misses"] if not mine(e)] + near
    doc["curated"] = [e for e in doc["curated"] if not mine(e)] + curated
    KNOWN.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(near)} flawed near misses and {len(curated)} left-out tests of regen_01 in {KNOWN.name}")


if __name__ == "__main__":
    main()
