"""How many tests does it take to defeat every lazy strategy in a service? (plan.md, question 3)

    python grounding/runs/several_match_02/numbers.py      # reads matrix.json; writes numbers.json

For every probe or test in matrix.json, the lazy strategies it defeats: those that miss at least one match, where the
probe's thorough strategy finds them all. Two ways to count:
- **Among the built tests (SM2-*):** the smallest set of tests that together defeat every lazy strategy the service's
  tests were run against. This is an exact search; the sets are small.
- **With the probes as candidate tests:** the same over every valid probe, for the placements not built as tests yet.
Strategies that no valid placement defeats are listed: no test in this space can catch them.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Invalid although a thorough strategy retrieves every match: the runner counts retrieval, and on these seeds the
# condition's field is not in what the thorough route returns (cycle 5).
INVALID = {
    "SM2-BOX-02": "the Box replica's folder listing leaves out modified_by whatever `fields` asks for",
    "SM2-SLK-03": "the Slack replica's history leaves out reactions",
}


def defeats(r: dict) -> set[str] | None:
    """The lazy strategies this probe defeats, or None if it is invalid (no thorough strategy finds every match)."""
    if r["probe"] in INVALID:
        return None
    s = r["strategies"]
    if not any(v.get("thorough") and not v.get("missed") and "error" not in v for v in s.values()):
        return None
    return {name for name, v in s.items() if not v.get("thorough") and "error" not in v and v.get("missed")}


def cover(cands: dict[str, set[str]], universe: set[str]):
    for k in range(1, len(cands) + 1):
        for combo in itertools.combinations(sorted(cands), k):
            if set().union(*(cands[c] for c in combo)) >= universe:
                return list(combo)
    return None


def main():
    matrix = json.loads((HERE / "matrix.json").read_text())
    by_service: dict[str, dict[str, set[str]]] = {}
    lazy: dict[str, set[str]] = {}
    for pid, r in matrix.items():
        d = defeats(r)
        key = r["domain"]
        lazy.setdefault(key, set()).update(n for n, v in r["strategies"].items() if not v.get("thorough"))
        if d is not None:
            by_service.setdefault(key, {})[pid] = d
    out = {}
    for svc, cands in sorted(by_service.items()):
        reachable = set().union(*cands.values())
        never = sorted(lazy[svc] - reachable)
        tests = {k: v for k, v in cands.items() if k.startswith("SM2-")}
        best_tests = cover(tests, set().union(*tests.values())) if tests else None
        best_all = cover(cands, reachable)
        out[svc] = {"lazy strategies": sorted(lazy[svc]), "defeated by some valid placement": sorted(reachable),
                    "defeated by none": never, "smallest set among built tests": best_tests,
                    "smallest set over all valid probes": best_all}
        print(f"\n== {svc}: {len(lazy[svc])} lazy strategies; {len(reachable)} defeated by some valid placement")
        print(f"   smallest set of built tests: {best_tests}")
        print(f"   smallest set over all valid probes: {best_all}")
        if never:
            print(f"   defeated by no valid placement: {never}")
    (HERE / "numbers.json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
