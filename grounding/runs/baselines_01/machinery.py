"""What our pipeline's machinery catches before any agent run: the problems its checks and reader sent back to the
writer, per brief, from the recorded generation runs (no model calls).

    python3 grounding/runs/baselines_01/machinery.py        # writes machinery.json and prints the summary

Sources: autogen_02's Phase 4 (Muse writer, the same agent as N0) and autogen_01's arms (Sonnet). Each record's
`history` lists every version with the stage that stopped it (code checks, the replica pre-checks, or the cold
reader) and the problems sent back. A first draft is "clean" when its history has no problem at all.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
SOURCES = {"phase4_muse": RUNS / "autogen_02/runs/phase4_gen",
           "arm_r_sonnet": RUNS / "autogen_01/runs/gen_arm_r",
           "arm_p_sonnet": RUNS / "autogen_01/runs/gen_arm_p",
           "arm_p_v2_sonnet": RUNS / "autogen_01/runs/gen_arm_p_v2"}
FORMAT = "format or seed syntax (writer output did not parse or build)"


def category(stage: str, problem: str) -> str:
    """A problem's kind, from the stage that raised it and its text."""
    low = problem.lower()
    if stage == "missing" or "jsondecodeerror" in low or "could not be built" in low or "cannot be evaluated" in low \
            or low.startswith("seed:"):
        return FORMAT
    if stage == "replica":
        return "the replica rejects the seed or the write does not land"
    if stage == "reader":
        return "the cold reader found other matches, none, or two readings"
    if "not killed" in low:
        return "a near miss fails another condition or none (witness check)"
    if "but query selects" in low and "target removed" not in low:
        return "the request selects other records than the target"
    if "anchor" in low:
        return "an entity the request names disappears with the target"
    if "target removed" in low:
        return "a probe loses its trap when the target is removed"
    if "relative" in low or "today" in low:
        return "the request depends on today's date"
    return "other"


def main():
    out = {}
    for name, folder in SOURCES.items():
        briefs = [p for p in sorted(folder.glob("*/outcome.json"))]
        stats = Counter()
        cats = Counter()
        stages = Counter()
        for path in briefs:
            o = json.loads(path.read_text())
            stats["briefs"] += 1
            stats[o.get("status", "unknown")] += 1
            first = o.get("history", [{}])[0] if o.get("history") else {}
            problems_first = first.get("problems", [])
            clean = not problems_first and o.get("versions", 1) == 1 and o.get("status") == "accepted"
            if clean:
                stats["first_draft_clean"] += 1
            brief_kinds = set()
            for h in o.get("history", []):
                if h.get("problems"):
                    stages[h.get("stage")] += 1
                    kinds = {category(h.get("stage"), p if isinstance(p, str) else json.dumps(p))
                             for p in h["problems"]}
                    brief_kinds |= kinds
                    for k in kinds:  # rounds sent back for each kind of problem
                        cats[k] += 1
            if not clean:  # a brief sent back only for format, or at least once for substance
                stats["sent_back_format_only" if brief_kinds <= {FORMAT} else "sent_back_substantive"] += 1
            stats["versions"] += o.get("versions", 0)
        out[name] = {"counts": dict(stats), "rounds_sent_back_by_stage": dict(stages),
                     "rounds_sent_back_by_problem": dict(cats.most_common())}
    (HERE / "machinery.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
