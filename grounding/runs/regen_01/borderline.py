"""Sensitivity of the regular score to the 8 near misses my review flagged borderline (valid by the rulings, flagged
for the PI): the score (score.py, as run) if the PI ruled them flawed. No model calls; nothing is written to the
rulings file (the extra rulings exist only in this process).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.borderline

Writes eval/borderline_sensitivity.json: the as-run score, the score with the borderline near misses ruled flawed,
the facts and tests that depend on them, and the near misses themselves.
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.regen_01 import rules, score

HERE = Path(__file__).resolve().parent
R = rules.rulings


def borderline() -> list[tuple[str, str]]:
    review = {k: v for k, v in json.loads((HERE / "eval" / "review.json").read_text()).items() if not k.startswith("_")}
    return [(sid, w) for sid, r in review.items() for w, v in r["decoys"].items()
            if "borderline" in v and not v.startswith("flawed")]


def main():
    base = score.adjudicate("full_01", HERE / "runs")
    extra = borderline()
    original = R._doc

    def doc():
        d = dict(original())
        d["near_misses"] = list(d.get("near_misses", [])) + [
            {"scenario": s, "witness": w, "ruling": "flawed", "source": "regen_01 borderline (hypothetical)"}
            for s, w in extra]
        return d

    R._doc = doc
    try:
        alt = score.adjudicate("full_01", HERE / "runs")
    finally:
        R._doc = original
    q = lambda out: {f"{r['domain']} {f}" for r in out["tests"] for f in r["exposed"]}  # noqa: E731
    result = {
        "_about": __doc__.split("\n\n")[0],
        "borderline_near_misses": [f"{s} {w}" for s, w in extra],
        "as_run": base["adjudicated"], "borderline_ruled_flawed": alt["adjudicated"],
        "facts_lost": sorted(q(base) - q(alt)),
        "tests_left_out": sorted(t["case_id"] for t in alt["left_out_tests"]),
        "trials_not_counted": len(alt["trials_not_counted"]) - len(base["trials_not_counted"]),
    }
    (HERE / "eval" / "borderline_sensitivity.json").write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "_about"}, indent=1))


if __name__ == "__main__":
    main()
