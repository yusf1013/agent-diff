"""RQ1 and RQ2: the coverage space and the coverage the generated suites achieve.

A catalog fact is **covered** when some valid regular test holds a near miss for it (credit rule, criterion.md):
a claim whose witness the reference check kills in that test's own world, in a fact-sensitive form (a cover with the
target present, or a probe or fact probe with the escape clause). Tests the PI's rulings leave out and near misses
they rule flawed give no credit. The derivation already dropped the probes whose near miss lost its trap once the
target was removed; their claims still count in the cover, where the check passes (checked here again).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.coverage

Writes numbers/coverage.json.
"""
from __future__ import annotations

import copy
from collections import Counter, defaultdict

from grounding.runs.autogen_01.kit import derive
from grounding.runs.report_01.kit.common import (DOMAINS, RUNS, WRITER_ORDER, WRITERS, catalog, fact_id, load,
                                                 replica_gaps, suite_tests, valid_claims, write)


def main():
    cat = catalog()
    gaps = replica_gaps()
    covered = defaultdict(lambda: defaultdict(set))    # writer -> domain -> facts with valid credit
    claimed = defaultdict(lambda: defaultdict(set))    # writer -> domain -> facts claimed, before the rulings
    forms = defaultdict(lambda: defaultdict(set))      # (domain, fact) -> form -> scenarios giving valid credit
    families = defaultdict(set)                        # (domain, fact) -> families of its valid claims
    cover_errors = []
    for m, case in suite_tests():
        w = WRITERS[m["source"]]
        d = case["domain"]
        for ref in case["references"]:
            for c in ref.get("claims", []):
                claimed[w][d].add(fact_id(d, c["requirement"]))
        for f, _, fam in valid_claims(case):
            covered[w][d].add(f)
            forms[(d, f)][m["form"]].add(m["scenario"])
            families[(d, f)].add(fam)
        if m["form"] == "cover":
            _, errors = derive._finish(copy.deepcopy(case))
            if errors:
                cover_errors.append({"case_id": case["case_id"], "errors": errors})

    space = {}
    achieved = {}
    for d in DOMAINS:
        facts = set(cat[d])
        servable = facts - set(gaps[d])
        per = {w: sorted(covered[w][d] & facts) for w in WRITER_ORDER}
        union = set().union(*map(set, per.values()))
        before = set().union(*(claimed[w][d] for w in WRITER_ORDER)) & facts
        kinds = Counter(f.split(":")[0] for f in facts)
        space[d] = {"facts": len(facts), "by_kind": {k: kinds[k] for k in "ARHBD"}, "replica_gaps": len(gaps[d]),
                    "servable": len(servable),
                    # as catalog/build.py counts it for counts.md
                    "with_designated_alternative": sum(1 for f in facts if cat[d][f]["kind"] in "HBD"
                                                       or cat[d][f].get("alternatives")
                                                       or cat[d][f].get("sibling_alternatives"))}
        before_6b = set().union(*(set(v) for w, v in per.items() if w != "Muse 6b"))
        achieved[d] = {"per_writer": {w: len(v) for w, v in per.items()},
                       "covered_before_6b": len(before_6b),
                       "covered": len(union), "covered_servable": len(union & servable),
                       "claimed_before_rulings": len(before),
                       "uncovered_servable": sorted(servable - union),
                       "lost_to_rulings": sorted(before - union),
                       "covered_facts": sorted(union)}

    by_kind = {}
    for k in "ARHBD":
        n = sum(1 for d in DOMAINS for f in cat[d] if f.startswith(k + ":"))
        g = sum(1 for d in DOMAINS for f in gaps[d] if f.startswith(k + ":"))
        c = sum(1 for d in DOMAINS for f in achieved[d]["covered_facts"] if f.startswith(k + ":"))
        by_kind[k] = {"facts": n, "replica_gaps": g, "servable": n - g, "covered": c}

    # How each covered fact is credited: through a cover only, or also through a probe or fact probe; through a
    # designated substitute (F1-F8) or only through plain near misses (F0).
    cover_only = sorted(f"{d} {f}" for (d, f), v in forms.items() if set(v) == {"cover"})
    plain_only = defaultdict(list)
    for (d, f), fams in families.items():
        if fams and all(x.split("+")[0] == "F0" for x in fams):
            plain_only[d].append(f)
    by_family = Counter(x for fams in families.values() for x in fams)
    by_form = Counter()
    for v in forms.values():
        for form in v:
            by_form[form] += 1

    # 6b's targets: the uncovered servable facts its briefs were drawn for.
    briefs = load(RUNS / "completion_01/inputs/briefs_6b.json")
    target = {(b["domain"], fact_id(b["domain"], f if isinstance(f, str) else f.get("id")))
              for b in (briefs if isinstance(briefs, list) else briefs.get("briefs", [])) for f in b.get("facts", [])}
    sixb = {"target_facts": len(target),
            "covered_after_6b": sum(1 for d, f in target if f in achieved[d]["covered_facts"])}

    out = {"space": space, "achieved": achieved, "by_kind": by_kind, "facts_credited_through_form": dict(by_form),
           "credited_through_a_cover_only": cover_only, "cover_check_errors": cover_errors, "sixb": sixb,
           "credited_only_through_plain_near_misses": {d: sorted(v) for d, v in sorted(plain_only.items())},
           "facts_per_family": dict(sorted(by_family.items())),
           "totals": {"facts": sum(s["facts"] for s in space.values()),
                      "servable": sum(s["servable"] for s in space.values()),
                      "covered_before_6b": sum(a["covered_before_6b"] for a in achieved.values()),
                      "covered": sum(a["covered"] for a in achieved.values()),
                      "covered_servable": sum(a["covered_servable"] for a in achieved.values()),
                      "claimed_before_rulings": sum(a["claimed_before_rulings"] for a in achieved.values())}}
    print(write("coverage", out))
    for d in DOMAINS:
        print(d, space[d], {k: v for k, v in achieved[d].items() if k != "covered_facts"})
    print(out["totals"], by_kind, sixb, "cover only:", cover_only, "cover check errors:", len(cover_errors))
    print("plain only:", {d: len(v) for d, v in plain_only.items()}, dict(plain_only), "families:", dict(by_family))


if __name__ == "__main__":
    main()
