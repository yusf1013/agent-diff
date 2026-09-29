"""Write the inputs of the mutated twins: N0M and N1M are N0 and N1 with the PI's added lines and a corrected format.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_01.twin2.make_inputs

`twin2/n0m/inputs/<domain>/` is a copy of `n0/inputs/<domain>/`, and `twin2/n1m/inputs/<domain>/` of
`n1/inputs/<domain>/`, with two changes:
- **`task.md`** gets ADDED (the PI, 2026-09-28) as its own paragraph after the request for 12 tests, the same text in
  both twins. Nothing else in the task changes.
- **`format.md`** is corrected (FIXES). Round 1's listed an `"unchanged"` diff type that the engine rejects, promised
  that "timestamps and similar bookkeeping columns" are ignored, and did not say that a column left out of
  `expected_changes` fails the assertion when it changes. Here the diff types are the engine's, the ignored columns
  are listed (`assertions.ignored_columns`, which the twins' assertions are evaluated with: `assertions.py --twin`),
  and the rule is spelled out. This corrects our harness; it says nothing about how to design a test.
N0M is checked against N0's list of our pipeline's vocabulary, as N0 was.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from grounding.runs.baselines_01.assertions import ignored_columns
from grounding.runs.baselines_01.n0.make_inputs import DOMAINS, FORBIDDEN

HERE = Path(__file__).resolve().parent
SOURCES = {"n0m": HERE.parent / "n0" / "inputs", "n1m": HERE.parent / "n1" / "inputs"}

ANCHOR = "in the format of `format.md`.\n"
ADDED = """
Make sure each test checks a different property. Make the tests challenging: a careless assistant should fail them,
but a perfect assistant must be able to pass them. Use neutral ids that do not reveal which record is the right one.
"""

FIXES = [
    ('- **`diff_type`:** `"added"`, `"removed"`, `"changed"` or `"unchanged"`.',
     '- **`diff_type`:** `"added"`, `"removed"` or `"changed"`. To check that a record stays as it is, use `"changed"`\n'
     '  with `"expected_count": 0`.'),
    ("The default is at least one for `added`, `removed`\n  and `changed`, and zero for `unchanged`.",
     "The default is at least one."),
    ("Only the listed columns may change, apart from timestamps and similar bookkeeping columns, which\n"
     "  are ignored.",
     "List every column you expect to change: a matching row that also changed in a column that is neither\n"
     "  listed nor ignored makes the assertion fail. The ignored columns never count as changed, so do not list them\n"
     "  either: {ignored}."),
]


def main():
    record = {}
    for twin, source in SOURCES.items():
        for d in DOMAINS:
            dest = HERE / twin / "inputs" / d
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(source / d, dest)
            task = (dest / "task.md").read_text()
            if task.count(ANCHOR) != 1:
                raise SystemExit(f"{dest}/task.md: anchor not found once")
            (dest / "task.md").write_text(task.replace(ANCHOR, ANCHOR + ADDED))
            fmt = (dest / "format.md").read_text()
            for old, new in FIXES:
                if fmt.count(old) != 1:
                    raise SystemExit(f"{dest}/format.md: text to fix not found once: {old[:60]!r}")
                fmt = fmt.replace(old, new.format(ignored=", ".join(f"`{c}`" for c in ignored_columns(d))))
            if "unchanged" in fmt:
                raise SystemExit(f"{dest}/format.md: 'unchanged' remains")
            (dest / "format.md").write_text(fmt)
            if twin == "n0m":
                for f in sorted(dest.iterdir()):
                    low = f.read_text().lower()
                    hits = [w for w in FORBIDDEN if w in low and f.name != "api.md"]
                    if hits:
                        raise SystemExit(f"{f}: our vocabulary remains: {hits}")
            record[f"{twin}/{d}"] = sorted(p.name for p in dest.iterdir())
    print(json.dumps(record, indent=1))


if __name__ == "__main__":
    main()
