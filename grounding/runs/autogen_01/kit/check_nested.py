"""Which GraphQL paths fail with "Cannot return null for non-nullable field" in the Linear trials, per run.

    python3 -m grounding.runs.autogen_01.kit.check_nested

Counts each failing path (for example `issue.attachments.nodes`) once per trial, from the error's `path`, so a replica
field that cannot be resolved shows up however the solver phrased its query.
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

RUNS = Path(__file__).resolve().parents[1] / "runs"
RUN_NAMES = ("solve_arm_r", "solve_control", "solve_arm_p", "solve_arm_p_v2")
ERROR = re.compile(r'"message":\s*"Cannot return null for non-nullable field [^"]*",(?:(?!"message").)*?"path":\s*'
                   r'\[([^\]]*)\]')


def main():
    for run in RUN_NAMES:
        paths = Counter()
        tests = defaultdict(set)
        for solver in RUNS.glob(f"{run}/t*/*/attempt-*/solver/*.json"):
            if "LIN" not in solver.parent.parent.parent.name:
                continue
            try:
                steps = json.loads(solver.read_text()).get("steps", [])
            except (json.JSONDecodeError, OSError):
                continue
            seen = set()
            for s in steps:
                for m in ERROR.finditer(str((s.get("observation") or {}).get("stdout", ""))):
                    path = ".".join(p.strip().strip('"') for p in m.group(1).split(",") if not p.strip().isdigit())
                    seen.add(path)
            for p in seen:
                paths[p] += 1
                tests[p].add(solver.parent.parent.parent.name)
        print(f"== {run}")
        for p, n in paths.most_common():
            print(f"  {p}: {n} trials, e.g. {sorted(tests[p])[:3]}")


if __name__ == "__main__":
    main()
