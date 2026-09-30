"""Which of a plural request's targets Agent-Diff's own assertions would notice missing: a review by hand.

    python -m grounding.runs.related_work_01.s1.omissions

The question, per target: a trial does everything the test asks, except that it leaves this one target out (does not
act on it, report it or count it) and puts nothing in its place. Does an assertion fail? The engine's rules
(backend/src/platform/evaluationEngine/assertion.py, `_check_count`): an integer `expected_count` is exact, `{"min": n}`
a lower bound, and no count means at least one match.

A target is pinned when an assertion fails without it. Three ways, read from each test's assertions:
- by id or identifier (`eq` on the target's key or identifier, with a count);
- by text unique to the target (`contains` or `regex` on a fragment only that target's content carries);
- by count (an exact or minimum count on the obligation's rows equal to the number of targets). A count notices an
  omission only when nothing is put in its place: a trial that substitutes a non-target passes.

The first run's mechanical rule (ids in `eq`/`in`, and exact counts) was wrong both ways: it missed text, regex,
identifier and minimum-count pins, and counted ids that belong to other obligations. Replaced by this table.
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.related_work_01.s1.probes import PROBES, SAME_AS

REPO = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent

# (test, obligation) -> (pins: {target: how}, or "count: ..." for every target, note). Unlisted targets are unnoticed.
EVERY = "every target"
HAND = {
    ("slack_67", 1): ({"1699572000.000789": "A0: a thumbsup on its id", "1706052665.000000": "A1: a thumbsup on its id"},
                      "the pizza-quantity and garlic-knots questions are unchecked"),
    ("slack_74", 1): ({"1700210000.000001": "A0: 'Gemini' reposted to #general",
                       "1700210180.000004": "A1: 'preview' reposted", "1706052160.000000": "A2: 'garlic knots' reposted",
                       "1706052665.000000": "A3: 'shared lunch' reposted"},
                      "each keyword is in that target only; the other four questions are unchecked"),
    ("slack_75", 1): ({EVERY: "A3-A6: each target's fragment ('500 errors', 'invalid_grant', 'login rate limit', "
                              "'login endpoint') in the DM"}, "each fragment is in one target only"),
    ("slack_76", 1): ({EVERY: "A2-A7: each target's fragment in the DM"}, "each fragment is in one target only"),
    ("slack_77", 1): ({EVERY: "A0-A5: each target's fragment in the edited message"}, "each fragment is in one target only"),
    ("slack_106", 1): ({"C01ABCD1234": "A0: a message containing 'general'"},
                       "the other eight channels of the requested list are unchecked"),
    ("slack_108", 1): ({}, "read-only: the authors found are an answer, and Agent-Diff checks no answer"),
    ("slack_110", 6): ({EVERY: "count: A2's regex needs '2' after 'supercomputer' on the manifesto line"},
                       "an omission makes the count 1; a stray standalone '2' later on that line would pass"),
    ("slack_112", 1): ({}, "read-only: the survey ('how many cells, which are alive') is an answer, unchecked"),
    ("slack_113", 1): ({c: "A1: its line in the Field Report regex" for c in
                        ["C_INFRA", "C03IJKL9012", "C_FRONTEND", "C01ABCD1234", "C04MNOP3456", "C_MODEL", "C05ALPHA",
                         "C06ALPHADEV", "C02EFGH5678"]},
                       "the regex lists nine channels; product-growth and the archived old-project-q3 are unchecked"),
    ("box_127", 2): ({}, "A0 needs any non-empty description: a count missing files passes"),
    ("box_129", 1): ({}, "A1 needs at least one fomc file moved, with no count"),
    ("box_139", 1): ({EVERY: "A0-A4: each file's new name, by id"}, ""),
    ("box_141", 1): ({EVERY: "count: A1 needs at least 8 file hub items"}, "any eight files pass"),
    ("box_143", 2): ({}, "no assertion on the moved files; A3 checks only that six subfolders are trashed"),
    ("box_150", 1): ({EVERY: "count: A1 needs at least 4 hub items named fomc"}, ""),
    ("box_151", 1): ({}, "A0 needs at least one PDF tagged, with no count"),
    ("box_152", 1): ({}, "A0 needs at least one fomc file's description, with no count"),
    ("box_155", 1): ({}, "A1 needs at least 2 Domain_ folders; the three CSVs have three domains, so two remain"),
    ("box_158", 1): ({}, "read-only: the search's result is not checked; the later steps name each file by its role"),
    ("linear_32", 1): ({"87c1d2f3-66c4-4dd0-bc93-1b99d04dc374": "A0: ENG-3 reassigned, by identifier"},
                       "PROD-2, also John's and urgent, is unchecked"),
    ("linear_41", 1): ({EVERY: "count: A1 needs exactly 4 label associations"}, "any four issues pass"),
    ("linear_41", 3): ({}, "the rate is computed from them, but A5 checks only the comments' 'GERMINATION_AUDIT:' "
                           "prefix; leaving one packet out changes the rate (1/2 or 0/2) but not the branch"),
    ("linear_41", 5): ({"bc234567-3456-789a-bcde-f01234567890": "A3: SEED-7 moved, by identifier",
                        "cd345678-4567-89ab-cdef-012345678901": "A4: SEED-8 moved, by identifier"}, ""),
    ("linear_56", 2): ({}, "read-only: the in-flight birds found are not reported or checked"),
    ("box_163", 2): ({}, "no assertion on the hub's items"),
}


def main():
    rows = []
    pairs = [(tid, oi) for tid, oi, _k, _p in PROBES] + list(SAME_AS)
    for tid, oi in pairs:
        service = tid.split("_")[0]
        ob = next(t for t in json.loads((REPO / f"grounding/domains/{service}/analysis/analysis.json").read_text())
                  if t["test_id"] == tid)["obligations"][oi - 1]
        targets = [str(t) for t in ob["card"]["Referent set"]]
        pins, note = HAND[(tid, oi)]
        pinned = {t: pins[EVERY] for t in targets} if EVERY in pins else {t: h for t, h in pins.items()}
        assert set(pinned) <= set(targets), (tid, set(pinned) - set(targets))
        by_count = sum(h.startswith("count:") for h in pinned.values())
        rows.append({"test": tid, "obligation": oi, "targets": len(targets), "pinned": len(pinned),
                     "pinned_by_count_only": by_count, "unnoticed_if_omitted": len(targets) - len(pinned),
                     "unnoticed": [t for t in targets if t not in pinned], "how": pinned, "note": note,
                     "cards_assertion_coverage": ob.get("assertion_coverage")})
    (HERE / "omissions.json").write_text(json.dumps(rows, indent=1) + "\n")
    for r in rows:
        print(f"{r['test']:<10} O{r['obligation']} targets={r['targets']:<3} pinned={r['pinned']:<3} "
              f"(by count only {r['pinned_by_count_only']}) unnoticed={r['unnoticed_if_omitted']:<3} "
              f"cards={r['cards_assertion_coverage']}")
    tot = sum(r["targets"] for r in rows)
    un = sum(r["unnoticed_if_omitted"] for r in rows)
    cnt = sum(r["pinned_by_count_only"] for r in rows)
    blind = sum(r["unnoticed_if_omitted"] > 0 for r in rows)
    print(f"{len(rows)} obligations, {tot} targets: {un} unnoticed if omitted, {cnt} noticed by a count only "
          f"(a substitute passes), {tot - un - cnt} pinned by id or unique text; {blind} obligations with at least "
          f"one unnoticed target")
    for svc in ("slack", "box", "linear"):
        rs = [r for r in rows if r["test"].startswith(svc)]
        print(f"  {svc}: {len(rs)} obligations, {sum(r['targets'] for r in rs)} targets, "
              f"{sum(r['unnoticed_if_omitted'] for r in rs)} unnoticed")


if __name__ == "__main__":
    main()
