"""Which facts the regenerated scenarios cover with a valid near miss, against the briefs' facts and against the facts
report_01 credits to the Sonnet half. No model calls; plain python3 is enough.

    python3 grounding/runs/regen_01/coverage.py [--json]

A fact is covered when an accepted scenario (cases.py's choice) declares a near miss on it that my review
(eval/review.json) does not rule flawed. Every near miss is held by its scenario's cover, which the derivation always
keeps (report_01 credits two facts through covers alone), so a probe the witness check drops does not remove the
fact. "Designated" means a family F1 to F8; F0 is a plain different value (report_01's F0 counting rule is open
with the PI).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from grounding.runs.regen_01.cases import accepted  # noqa: E402  (one rule for which attempt a brief uses)

HERE = Path(__file__).resolve().parent
REPORT = HERE.parent / "report_01" / "numbers" / "concise.json"


def main():
    briefs = json.loads((HERE / "inputs" / "briefs_regen.json").read_text())
    review = json.loads((HERE / "eval" / "review.json").read_text())
    sonnet = {(d, f) for d, fs in json.loads(REPORT.read_text())["writers"]["Sonnet"]["coverage"].items() for f in fs}
    brief_facts = {(b["domain"], f) for b in briefs for f in b["facts"]}
    status = {b["scenario_id"]: "not accepted" for b in briefs}
    covered: dict[tuple[str, str], set[str]] = {}
    flawed_only: dict[tuple[str, str], list[str]] = {}
    for sid, folder in accepted().items():
        status[sid] = "accepted"
        case = json.loads((folder / "case.json").read_text())
        verdicts = review.get(sid, {}).get("decoys", {})
        for claim in case["references"][0]["claims"]:
            key, w = (case["domain"], claim["requirement"]), str(claim["witness"])
            verdict = verdicts.get(w, "unreviewed")
            if verdict.startswith("flawed"):
                flawed_only.setdefault(key, []).append(f"{sid}:{w}")
                continue
            covered.setdefault(key, set()).add(claim.get("family") or "?")
    for key in covered:
        flawed_only.pop(key, None)
    designated = {k for k, fam in covered.items() if any(f != "F0" for f in fam)}
    result = {
        "briefs": len(briefs), "accepted": sorted(s for s, v in status.items() if v == "accepted"),
        "not_accepted": sorted(s for s, v in status.items() if v != "accepted"),
        "covered": len(covered), "covered_designated": len(designated),
        "covered_f0_only": sorted(f"{d} {f}" for d, f in covered if (d, f) not in designated),
        "brief_facts": len(brief_facts), "brief_facts_covered": len(brief_facts & set(covered)),
        "brief_facts_uncovered": sorted(f"{d} {f}" for d, f in brief_facts - set(covered)),
        "sonnet_credited": len(sonnet), "sonnet_credited_covered": len(sonnet & set(covered)),
        "sonnet_credited_uncovered": sorted(f"{d} {f}" for d, f in sonnet - set(covered)),
        "beyond_briefs": sorted(f"{d} {f}" for d, f in set(covered) - brief_facts),
        "only_flawed_near_misses": {f"{d} {f}": v for (d, f), v in sorted(flawed_only.items())},
    }
    if "--json" in sys.argv:
        print(json.dumps(result, indent=1))
        return
    for k, v in result.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
