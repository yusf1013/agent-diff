"""Build inputs/<domain>/facts.json: each catalog fact with the substitute families the domain model suggests.

    python -m grounding.runs.autogen_01.inputs.make_facts

A manual domain input, derived by rule from the fact catalog (fact_coverage_01/catalog):
- the catalog's designated substitutes (`alternatives` for relationship, hierarchy, binding and derived facts;
  `sibling_alternatives` for attributes) are copied as they are;
- the suggested families follow method.md's family table, by fact kind and attribute subkind:
  - identity attributes: F8 partial identity, F1 sibling attribute, F0;
  - text: F1 (the text in a sibling field), F2 (on a related record), F0;
  - time: F7 nearest value, F6 representation, F1 sibling time field, F0;
  - quantity: F7, F0;
  - state: F7 neighbouring state, F1, F0;
  - relationship roles: F1 sibling role, F2 indirection, F8 a person with a similar name, F0 (and F3 when the
    catalog marks a direction);
  - hierarchy: F4 level, F2; binding: F5 split; derived: F6, F7, F0.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG = HERE.parents[1] / "fact_coverage_01" / "catalog"
BY_SUBKIND = {"identity": ["F8", "F1", "F0"], "text": ["F1", "F2", "F0"], "time": ["F7", "F6", "F1", "F0"],
              "quantity": ["F7", "F0"], "state": ["F7", "F1", "F0"]}
BY_KIND = {"R": ["F1", "F2", "F8", "F0"], "H": ["F4", "F2"], "B": ["F5"], "D": ["F6", "F7", "F0"]}


def families(r):
    if r["kind"] == "A":
        fam = list(BY_SUBKIND.get(r.get("subkind"), ["F0"]))
    else:
        fam = list(BY_KIND.get(r["kind"], ["F0"]))
    text = json.dumps(r).lower()
    if r["kind"] == "R" and ("direction" in text or "reverse" in text or "related" in r["id"].lower()):
        fam.insert(1, "F3")
    return fam


def main():
    for path in sorted(CATALOG.glob("*.json")):
        data = json.loads(path.read_text())
        facts = []
        for r in data["requirements"]:
            entry = {"id": r["id"], "kind": r["kind"]}
            for key in ("subkind", "entity", "table", "field", "roles", "meaning", "parent", "child", "evidence",
                        "mutation"):
                if r.get(key):
                    entry[key] = r[key]
            subs = (r.get("alternatives") or []) + (r.get("sibling_alternatives") or [])
            entry["designated_substitutes"] = subs
            entry["suggested_families"] = families(r)
            facts.append(entry)
        out = HERE / data["domain"] / "facts.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({"domain": data["domain"], "entities": data.get("entities"),
                                   "facts": facts}, indent=1, ensure_ascii=False) + "\n")
        print(data["domain"], len(facts))


if __name__ == "__main__":
    main()
