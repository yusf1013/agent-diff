"""Compare generated scenarios with the hand-built ones on design: size, families, and (Arm R) fact by fact.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.compare_design GEN_RUN [...]

For every accepted scenario:
- conditions (counted as fact_coverage_02's request-size note counts them: each filter, and each edge with its
  node's checks);
- facts tested;
- decoys, by family.

For Arm R, next to the exemplar scenario of the same facts (fact_coverage_02/cases_new): the families each side used
per fact. This is the overfitting check: similar choices are expected from the same domain model, identical decoys
would be suspicious.
"""
from __future__ import annotations

import json
import statistics
import sys
from collections import Counter
from pathlib import Path

from grounding.runs.autogen_01.inputs.make_briefs import SLACK_ALIASES
from grounding.runs.fact_coverage_02.followups import _conditions

FC2 = Path(__file__).resolve().parents[2] / "fact_coverage_02" / "cases_new"


def design(case):
    ref = case["references"][0]
    claims = ref["claims"]
    return {"conditions": _conditions(ref["query"]), "facts": len({c["requirement"] for c in claims}),
            "decoys": len(claims),
            "families": Counter(c.get("family") for c in claims),
            "by_fact": {SLACK_ALIASES.get(f, f): sorted(c.get("family") for c in claims if c["requirement"] == f)
                        for f in {c["requirement"] for c in claims}}}


def exemplar(case_id, domain):
    path = FC2 / domain / f"{case_id}.json"
    return json.loads(path.read_text()) if path.exists() else None


def summary(rows):
    out = {}
    for key in ("conditions", "facts", "decoys"):
        vals = [r[key] for r in rows]
        out[key] = {"median": statistics.median(vals), "range": [min(vals), max(vals)]} if vals else None
    fam = Counter()
    for r in rows:
        fam.update(r["families"])
    out["families"] = dict(sorted(fam.items()))
    out["scenarios"] = len(rows)
    return out


def main():
    generated, hand = [], []
    per_fact = []
    for run in sys.argv[1:]:
        for outcome in sorted(Path(run).glob("*/outcome.json")):
            o = json.loads(outcome.read_text())
            if o["status"] != "accepted":
                continue
            case = json.loads((outcome.parent / "case.json").read_text())
            d = design(case)
            generated.append(d)
            ex_id = o["brief"].get("exemplar")
            if ex_id:
                ex = exemplar(ex_id, o["domain"])
                if ex:
                    e = design(ex)
                    hand.append(e)
                    for fact in o["brief"]["facts"]:
                        per_fact.append({"scenario": ex_id, "fact": fact,
                                         "exemplar_families": e["by_fact"].get(fact, []),
                                         "generated_families": d["by_fact"].get(fact, [])})
    result = {"generated": summary(generated), "exemplars_same_facts": summary(hand) if hand else None,
              "per_fact": per_fact}
    same = sum(1 for p in per_fact if set(p["exemplar_families"]) & set(p["generated_families"]))
    result["facts_sharing_a_family"] = f"{same}/{len(per_fact)}"
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
