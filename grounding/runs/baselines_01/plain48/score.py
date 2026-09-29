"""Score the random plain twins from the hand labels (labels.json), against the prediction in README.md.

    python3 grounding/runs/baselines_01/plain48/score.py      # writes score.json and prints it

Per pair (a probe and its plain twin, 3 trials each): whether each version fails at least once (a mistake:
incorrect or presented), the failing trials, and the facts exposed. A pair is discordant when exactly one version
fails. The sign test is exact and two-sided on the discordant pairs. Timeouts are failures of the agent that expose
no fact (the PI's rule): counted apart, not as mistakes.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
MISTAKE = {"incorrect", "presented"}


def sign_test(a: int, b: int) -> float:
    n = a + b
    if n == 0:
        return 1.0
    k = min(a, b)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n)


def main():
    labels = {k: v for k, v in json.loads((HERE / "labels.json").read_text()).items() if not k.startswith("_")}
    pick = json.loads((HERE / "pick.json").read_text())
    family = {}
    for path in (HERE / "suite").glob("*/*.json"):
        case = json.loads(path.read_text())
        if not case["case_id"].endswith("-PL"):
            family[case["case_id"]] = [c["family"] for r in case["references"] for c in r["claims"]][0]
    arms = {"original": {}, "plain": {}}
    for key, label in labels.items():
        _, trial, case = key.split("/")
        arm, probe = ("plain", case[:-3]) if case.endswith("-PL") else ("original", case)
        arms[arm].setdefault(probe, []).append(label)
    probes = sorted(c for ids in pick["pick"].values() for c in ids)
    rows, by_family = [], defaultdict(Counter)
    for probe in probes:
        row = {"probe": probe, "family": family[probe]}
        for arm in ("original", "plain"):
            ls = arms[arm][probe]
            row[f"{arm}_failing_trials"] = sum(1 for l in ls if l["outcome"] in MISTAKE)
            row[f"{arm}_timeouts"] = sum(1 for l in ls if l.get("timeout"))
            row[f"{arm}_exposed"] = sorted({f for l in ls if l["outcome"] in MISTAKE for f in l.get("exposed", [])})
        row["original_fails"] = row["original_failing_trials"] > 0
        row["plain_fails"] = row["plain_failing_trials"] > 0
        rows.append(row)
        by_family[row["family"]]["pairs"] += 1
        by_family[row["family"]]["original_fails"] += row["original_fails"]
        by_family[row["family"]]["plain_fails"] += row["plain_fails"]
    only_original = sum(1 for r in rows if r["original_fails"] and not r["plain_fails"])
    only_plain = sum(1 for r in rows if r["plain_fails"] and not r["original_fails"])
    out = {
        "pairs": len(rows),
        "original_fails": sum(r["original_fails"] for r in rows),
        "plain_fails": sum(r["plain_fails"] for r in rows),
        "both_fail": sum(1 for r in rows if r["original_fails"] and r["plain_fails"]),
        "neither_fails": sum(1 for r in rows if not r["original_fails"] and not r["plain_fails"]),
        "only_original": only_original, "only_plain": only_plain,
        "sign_test_p_two_sided": round(sign_test(only_original, only_plain), 4),
        "failing_trials": {"original": sum(r["original_failing_trials"] for r in rows),
                           "plain": sum(r["plain_failing_trials"] for r in rows), "of": 3 * len(rows)},
        "timeouts": {"original": sum(r["original_timeouts"] for r in rows),
                     "plain": sum(r["plain_timeouts"] for r in rows)},
        "facts_exposed": {"original": sorted({f for r in rows for f in r["original_exposed"]}),
                          "plain": sorted({f for r in rows for f in r["plain_exposed"]})},
        "by_family": {k: dict(v) for k, v in sorted(by_family.items())},
        "by_service": {d: {"original_fails": sum(r["original_fails"] for r in rows if r["probe"] in ids),
                           "plain_fails": sum(r["plain_fails"] for r in rows if r["probe"] in ids)}
                       for d, ids in pick["pick"].items()},
        "cycle2_overlap": {r["probe"]: [r["original_failing_trials"], r["plain_failing_trials"]]
                           for r in rows if r["probe"] in pick["cycle2_overlap"]},
        "rows": rows,
    }
    (HERE / "score.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}, indent=1))
    for r in rows:
        if r["original_fails"] or r["plain_fails"]:
            print(f"  {r['probe']:22} {r['family']}  original {r['original_failing_trials']}/3  plain "
                  f"{r['plain_failing_trials']}/3")


if __name__ == "__main__":
    main()
