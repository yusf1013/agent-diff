"""Exact small cover diagnostic over the fixed manual suite (no new grading).

This intentionally simple occurrence criterion is a comparator, not the proposed
final requirement catalog. Grounding verdicts are used ONLY to show the observed
range among equally small complete covers, not to author a new suite or claim
out-of-sample performance.
"""
from collections import defaultdict
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
GROUNDING = HERE.parents[1]
CASES = GROUNDING / "runs/manual_comparison_01/dataset/cases"


def main():
    cases = {p.stem: json.loads(p.read_text()) for p in sorted(CASES.glob("*.json"))}
    relation_fields = set()
    for case in cases.values():
        selector = case["private"]["selector"]
        for branch in [selector["focal"], *selector["auxiliary"]]:
            relation_fields.update(branch["joins"])
    coverage = {}
    root_groups = defaultdict(list)
    for cid, case in cases.items():
        selector = case["private"]["selector"]
        root = selector["root_table"]
        root_groups[root].append(cid)
        credits = {f"target:{root}", f"mode:{case['private']['mode']}"}
        filters = [(f"{root}.{f['field']}") for f in selector["scope"]]
        for branch in [selector["focal"], *selector["auxiliary"]]:
            credits.update(f"role:{j}" for j in branch["joins"])
            filters.extend(f"{branch['path'][f['node']]}.{f['field']}" for f in branch["filters"])
            if "count" in branch:
                credits.add(f"derived:count({branch['path'][branch['count']['node']]})")
        for field in filters:
            # A reference column does not become a second scalar model fact.
            credits.add(f"role:{field}" if field in relation_fields else f"identifying_attribute:{field}")
        coverage[cid] = credits
    requirements = sorted(set.union(*coverage.values()))
    bit = {r: 1 << i for i, r in enumerate(requirements)}
    masks = {cid: sum(bit[r] for r in credits) for cid, credits in coverage.items()}
    full = (1 << len(requirements)) - 1
    labels = json.loads((HERE / "manual_episode_analysis.json").read_text())
    errors = {cid: sum(r["grounding"] == "incorrect" for r in labels if r["case_id"] == cid) for cid in cases}

    # Each case has exactly one target entity. Thus seven target requirements
    # give a seven-case lower bound. Any complete cover found by choosing exactly
    # one case per target group meets that bound and is globally minimal in this
    # fixed 57-case pool for THIS criterion.
    def optimize(maximize):
        states = {0: (0, [])}
        for root, options in sorted(root_groups.items()):
            following = {}
            for existing_mask, (score, selected) in states.items():
                for cid in options:
                    mask = existing_mask | masks[cid]
                    candidate = score + errors[cid], selected + [cid]
                    old = following.get(mask)
                    better = old is None or (candidate[0] > old[0] if maximize else candidate[0] < old[0])
                    if better or (old is not None and candidate[0] == old[0] and candidate[1] < old[1]):
                        following[mask] = candidate
            states = following
        score, selected = states[full]
        assert len(selected) == len(root_groups)
        assert set.union(*(coverage[c] for c in selected)) == set(requirements)
        return {"cases": selected, "case_count": len(selected), "model_episodes": 3 * len(selected), "observed_incorrect_grounding_episodes": score}

    result = {
        "status": "Retrospective comparator; not a recommended final coverage catalog or a prospectively selected suite.",
        "denominator": "Facts and modes expressed by these 57 supplied cases, NOT the complete Slack model.",
        "criterion": "Target entity, named relationship role used in selection, ordinary identifying field, derived membership count, resolution mode. Roles counted once independent of traversal direction; reference columns not duplicated as scalar fields.",
        "requirements": requirements,
        "requirement_count": len(requirements),
        "candidate_pool_size": len(cases),
        "minimum_case_count": len(root_groups),
        "minimum_proof": "Seven distinct target types, one target type per case, plus exhibited complete seven-case covers.",
        "least_observed_error_minimum_cover": optimize(False),
        "most_observed_error_minimum_cover": optimize(True),
        "case_to_requirements": {cid: sorted(credits) for cid, credits in coverage.items()},
    }
    (HERE / "manual_cover_probe.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("case_to_requirements", "requirements")}, indent=2))


if __name__ == "__main__":
    main()
