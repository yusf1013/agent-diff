"""Phase 4 briefs, drawn by rule (plan, Phase 4).

    python3 -m grounding.runs.autogen_02.inputs.make_briefs4

1. **Candidates:** catalog facts (fact_coverage_01/catalog) that no autogen_01 brief used (dev, Arm R, Arm P, v2).
2. **Known replica gaps excluded** (inputs/<domain>/replica.md), because a fact the solver cannot read or filter
   through the replica tests the replica, not the solver:
   - Linear: every `projects` query errors and a project's lead cannot be read, so the Project, ProjectStatus,
     ProjectRelation and InitiativeToProject facts go, and R:Project.leadId; the `parent` filter is ignored
     (H:Issue.parentId, B:Issue.parentId); initiatives, notifications and organization invites exist "with varying
     completeness", so their facts go too;
   - Calendar: listing a calendar's sharing rules needs the owner role (the AclRule facts); a recurring series is
     listed only when the window covers its first start (H:Event.recurring_event_id, D:occurrence).
3. **Grouping:** by entity, in catalog order, three facts per brief (a remainder of one joins the previous brief; a
   remainder of two is its own brief).
4. **Order:** each domain's briefs are shuffled with the seed, then the domains are interleaved (box, calendar,
   linear, slack, box, ...), so a run cut short by time still covers every domain.
"""
from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parents[1]
A1_INPUTS = RUNS / "autogen_01" / "inputs"
SEED = 20260927
DOMAINS = ("box", "calendar", "linear", "slack")
PREFIX = {"box": "G4-BOX", "calendar": "G4-CAL", "linear": "G4-LIN", "slack": "G4-SLK"}
GAP_ENTITIES = {"linear": {"Project", "ProjectStatus", "ProjectRelation", "InitiativeToProject", "Initiative",
                           "InitiativeRelation", "Notification", "OrganizationInvite"},
                "calendar": {"AclRule"}}
GAP_FACTS = {"linear": {"R:Project.leadId", "H:Issue.parentId", "B:Issue.parentId", "R:Document.initiativeId",
                        "H:Initiative.parentInitiativeId"},
             "calendar": {"H:Event.recurring_event_id", "D:occurrence", "R:AclRule.calendar_id"}}


def entity(fact_id: str) -> str:
    return fact_id.split(":", 1)[1].split(".")[0]


def main():
    used = set()
    for name in ("briefs_dev", "briefs_arm_r", "briefs_arm_p", "briefs_arm_p_v2"):
        for b in json.loads((A1_INPUTS / f"{name}.json").read_text()):
            used.update((b["domain"], f) for f in b["facts"])
    per_domain, excluded = {}, {}
    for d in DOMAINS:
        catalog = json.loads((RUNS / "fact_coverage_01" / "catalog" / f"{d}.json").read_text())["requirements"]
        groups = defaultdict(list)
        excluded[d] = []
        for r in catalog:
            fid = r["id"]
            if (d, fid) in used:
                continue
            if entity(fid) in GAP_ENTITIES.get(d, set()) or fid in GAP_FACTS.get(d, set()):
                excluded[d].append(fid)
                continue
            groups[entity(fid)].append(fid)
        briefs = []
        for ent, facts in groups.items():
            chunks = [facts[i:i + 3] for i in range(0, len(facts), 3)]
            if len(chunks) > 1 and len(chunks[-1]) == 1:
                last = chunks.pop()
                chunks[-1] += last
            briefs += chunks
        random.Random(SEED + DOMAINS.index(d)).shuffle(briefs)
        per_domain[d] = briefs
    ordered = []
    counters = defaultdict(int)
    for i in range(max(len(b) for b in per_domain.values())):
        for d in DOMAINS:
            if i < len(per_domain[d]):
                counters[d] += 1
                ordered.append({"scenario_id": f"{PREFIX[d]}-{counters[d]:02}", "domain": d,
                                "facts": per_domain[d][i], "order": len(ordered) + 1})
    (HERE / "briefs_phase4.json").write_text(json.dumps(ordered, indent=1) + "\n")
    (HERE / "briefs_phase4.excluded.json").write_text(json.dumps(excluded, indent=1) + "\n")
    for d in DOMAINS:
        print(d, len(per_domain[d]), "briefs,", sum(len(b) for b in per_domain[d]), "facts; excluded",
              len(excluded[d]))
    print("first 16:", [(b["scenario_id"], b["facts"]) for b in ordered[:16]])


if __name__ == "__main__":
    main()
