"""The regeneration briefs: autogen_01's Sonnet briefs (arms R, P and P v2), mapped to the frozen pipeline's format,
plus the related-issue brief. No model calls.

    python3 grounding/runs/regen_01/inputs/make_briefs.py

The facts are copied, never rewritten. autogen_01's brief files already have the frozen format (`scenario_id`,
`domain`, `facts`); their extra fields (`exemplar`, `v1`) never reached a writer (the orchestrator shows it only the
id, the domain and the facts), and are kept here only as provenance.

- **One brief per distinct fact set.** Arm P and arm P v2 are the same 16 fact sets, written under two method
  versions. Under one frozen pipeline the second is a replicate, so each fact set gets one brief here. Arm P's
  AP-LIN-03 (rejected) and AP2-LIN-03 (accepted) are one of them.
- **Ids** continue Phase 4's numbering (G4-BOX-16, G4-CAL-11, G4-LIN-22, G4-SLK-10 onwards), as completion_01 did for
  its new briefs. The frozen code recognizes generated scenarios by their prefix (`judge2.generated`,
  `run.scenario_of`), and new ids must not reuse the Sonnet scenarios' ids, which the rulings key on.
- **The related-issue brief** (new): `R:IssueRelation.relatedIssueId` alone. Muse's G4-LIN-17 credited it only
  through a plain near miss (F0); the catalog's designated substitute is the reversed direction.

Writes briefs_regen.json.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUTOGEN_01 = HERE.parents[1] / "autogen_01" / "inputs"
ARMS = (("briefs_arm_r.json", "Sonnet arm R"), ("briefs_arm_p.json", "Sonnet arm P"),
        ("briefs_arm_p_v2.json", "Sonnet arm P v2"))
PREFIX = {"box": "BOX", "calendar": "CAL", "linear": "LIN", "slack": "SLK"}
FIRST = {"box": 16, "calendar": 11, "linear": 22, "slack": 10}  # after Phase 4's and completion_01's ids
DOMAINS = ("box", "calendar", "linear", "slack")
NEW = [{"domain": "linear", "facts": ["R:IssueRelation.relatedIssueId"],
        "source": "new: R:IssueRelation.relatedIssueId with its designated near miss (the reversed direction); "
                  "Muse's G4-LIN-17 credited it only through a plain near miss"}]


def main():
    sets = {}  # (domain, facts) -> the Sonnet briefs that carry it, in arm order
    for name, arm in ARMS:
        for b in json.loads((AUTOGEN_01 / name).read_text()):
            key = (b["domain"], tuple(b["facts"]))
            sets.setdefault(key, []).append(b["scenario_id"])
    briefs, n = [], dict(FIRST)
    for domain in DOMAINS:
        for (d, facts), sources in sets.items():
            if d != domain:
                continue
            sid = f"G4-{PREFIX[d]}-{n[d]:02}"
            n[d] += 1
            briefs.append({"scenario_id": sid, "domain": d, "facts": list(facts), "sonnet": sources,
                           "source": "autogen_01 brief " + " = ".join(sources)})
        for extra in NEW:
            if extra["domain"] == domain:
                sid = f"G4-{PREFIX[domain]}-{n[domain]:02}"
                n[domain] += 1
                briefs.append({"scenario_id": sid, **extra, "sonnet": []})
    (HERE / "briefs_regen.json").write_text(json.dumps(briefs, indent=1) + "\n")
    facts = {(b["domain"], f) for b in briefs for f in b["facts"]}
    print(f"{len(briefs)} briefs, {len(facts)} distinct facts, from {sum(len(s) for s in sets.values())} Sonnet briefs")


if __name__ == "__main__":
    main()
