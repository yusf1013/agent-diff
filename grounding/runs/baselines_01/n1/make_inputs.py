"""Write the inputs of N1: N0's inputs plus the domain model's facts to test, without the substitute menus (the
roadmap's G1).

    python3 grounding/runs/baselines_01/n1/make_inputs.py

The facts are those our accepted Phase 4 briefs asked for in each domain (autogen_02/inputs/briefs_phase4.json), so
N1 and our Phase 4 tests aim at the same facts. Each fact is given by its catalog id, its kind and the field it
rests on, with the catalog's definition of the kinds (fact_coverage_01/criterion.md). Left out: the designated
substitutes, the suggested families, and any gloss that would name a substitute.
"""
from __future__ import annotations

import json
import shutil
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parents[1]
N0_INPUTS = HERE.parent / "n0" / "inputs"
OUT = HERE / "inputs"
KIND = {"A": "attribute", "R": "relationship", "H": "hierarchy", "B": "binding", "D": "derived value"}

FACTS_HEAD = """# Facts to test

Together, your tests must check the assistant on each fact below: for every fact, at least one test in which that
fact decides which record is the right one.

The kinds of fact:
- **attribute:** an identifying attribute of a record (identity, text, time, quantity, state);
- **relationship:** a record's related person or record in a given role (a foreign-key role, an association);
- **hierarchy:** a level of a hierarchy or a self-relationship (a parent, a reply's parent);
- **binding:** several conditions that must hold on the same related record, across a to-many relationship;
- **derived value:** a value computed from records (a count, the latest one, a local date, the primary calendar).

| Fact | Kind | Rests on |
|---|---|---|
"""

TASK_ADD = """
The facts in `facts.md` are the ones we care about most. Together, the 12 tests must cover every one of them.
"""


def main():
    idx = json.loads((RUNS / "openclaw_eval_01/suite/suite.json").read_text())
    accepted = {t["scenario"] for t in idx if t["source"].endswith("phase4_gen")}
    per = defaultdict(set)
    for b in json.loads((RUNS / "autogen_02/inputs/briefs_phase4.json").read_text()):
        if b["scenario_id"] in accepted:
            per[b["domain"]].update(b["facts"])
    for domain, facts in sorted(per.items()):
        dest = OUT / domain
        dest.mkdir(parents=True, exist_ok=True)
        for f in (N0_INPUTS / domain).iterdir():
            shutil.copy(f, dest / f.name)
        catalog = {f["id"]: f for f in json.loads((RUNS / f"autogen_01/inputs/{domain}/facts.json").read_text())["facts"]}
        rows = []
        for fid in sorted(facts):
            f = catalog[fid]
            rests = f"`{f['table']}.{f['field']}`" if f.get("field") else f"`{fid.split(':', 1)[1]}`"
            rows.append(f"| `{fid}` | {KIND[f['kind']]} | {rests} |")
        (dest / "facts.md").write_text(FACTS_HEAD + "\n".join(rows) + "\n")
        (dest / "task.md").write_text((dest / "task.md").read_text().replace(
            "Scope: only whether", TASK_ADD.lstrip() + "\nScope: only whether"))
        print(domain, len(facts))


if __name__ == "__main__":
    main()
