"""Print a generated baseline test set compactly for the hand review: request, seed, expected and assertions.

    python3 grounding/runs/baselines_01/show_tests.py GEN_DIR DOMAIN     # e.g. twin2/n0m/runs/gen_01 box

Reads the tests as the coding agent saved them (the last workspace snapshot's `tests.json`).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def compact(value) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def main():
    gen, domain = Path(sys.argv[1]), sys.argv[2]
    snaps = sorted((gen / domain / "workspace").glob("round*/tests.json"))
    data = json.loads(snaps[-1].read_text())
    print(f"# {gen} {domain} ({snaps[-1].parent.name}), {len(data['tests'])} tests")
    for t in data["tests"]:
        print(f"\n## {t['id']}\nrequest: {t['request']}\nexpected: {t['expected']}")
        for op, args in t["seed"]:
            print(f"  seed {op} {compact(args)}")
        for a in t["assertions"]:
            print(f"  assert {compact(a)}")


if __name__ == "__main__":
    main()
