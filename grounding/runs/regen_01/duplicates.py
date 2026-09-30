"""Duplicate policy units (the PI, 2026-09-29: a pair whose request, actor and seed are identical is one test, and the
second unit's trials count as further trials of the first; `rulings.DUPLICATE_UNITS`). Finds them among the accepted
drop-F variants of this study's derivation runs, by the variant's request, actor and seed (the reference differs by the
dropped condition, which the agent never sees). No model calls; plain python3 is enough.

    python3 grounding/runs/regen_01/duplicates.py DROPF_DIR [DROPF_DIR ...]

Prints the pairs as `duplicate -> kept` (the first in id order is kept), for rules.DUPLICATES.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


def key(variant: dict) -> str:
    body = {"prompt": variant["prompt"], "actor": variant.get("acting_user_id"), "seed": variant["seed"]}
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()


def main():
    seen: dict[str, str] = {}
    pairs = {}
    for folder in map(Path, sys.argv[1:]):
        for rec_path in sorted(folder.glob("U-*/record.json")):
            rec = json.loads(rec_path.read_text())
            if rec["status"] != "accepted":
                continue
            k = key(json.loads((rec_path.parent / "variant.json").read_text()))
            if k in seen:
                pairs[rec["id"]] = seen[k]
            else:
                seen[k] = rec["id"]
    print(json.dumps(pairs, indent=1))
    print(f"{len(pairs)} duplicate units among {len(seen) + len(pairs)} accepted variants", file=sys.stderr)


if __name__ == "__main__":
    main()
