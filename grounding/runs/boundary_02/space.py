"""The testable space: the catalog (catalog.json) filtered by the replica probes (probes.json).

    python grounding/runs/boundary_02/space.py      # writes space.json and prints the counts

Per element:
- `faithful`: the replica refuses as the real service does, loudly or silently, or the request has no API at all
  (no call);
- `unfaithful`: the replica performs the change the real service refuses, or errors but changes state;
- `uncertain`: the replica's refusal type differs from the catalog's expectation where the real behaviour is only
  believed;
- `gap`: the replica lacks the endpoint the real service has (Slack `unsupported_endpoint`, a Box route answering a
  bare "Not Found"). It refuses for its own reason, not the service's rule, so the agent meets a missing endpoint and
  not the boundary: in cycle 2 some agents reported the missing endpoint and others worked around it. A test of it
  does not test the boundary, though what the agent did is still recorded;
- `not a boundary`: found on review: the service's own documented route does the request (REVIEW).
The refusal dimension of a faithful element is the one the replica shows. The cell uses the four dimensions of
plan.md.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from alternatives import ALT  # noqa: E402  (this study's own tags; space.py runs as a plain script)
# Reviewed after the probes: the probe outcome is right and the catalog's refusal guess was wrong or the element
# is not a real boundary. Id -> (verdict, reason).
REVIEW = {
    "CAL-05": ("faithful", "dataOwner is read-only; the replica ignores it silently, as Google does"),
    "CAL-13": ("uncertain", "eventType changes: ignored silently here; Google may refuse them loudly"),
    "CAL-14": ("uncertain", "an organizer may be able to set attendee responses through the API"),
    "LIN-04": ("faithful", "completedAt is not in IssueUpdateInput: refused loudly by the schema"),
    "LIN-20": ("uncertain", "real Linear may allow isGroup changes; the replica does"),
    "LIN-26": ("uncertain", "real Linear's issueRelationUpdate may accept a new type; the replica does"),
    "LIN-14": ("unfaithful", "found in cycle 2: userDemoteMember makes a user a guest with no admin check"),
    "SLA-40": ("unfaithful", "found in cycle 2: conversations.invite adds people to a group DM past its 9-person cap; "
                             "real Slack caps group DMs at 9 and takes no invites to them"),
    # Reviewed after cycle 2: the catalog's workaround is the service's own way to do the request, so the request is
    # possible and the element is not a boundary.
    "BOX-31": ("not a boundary", "Box transfers a folder by making the new owner a collaborator with role owner (the "
                                 "replica has no collaboration endpoints)"),
    "BOX-12": ("uncertain", "a file may transfer as a folder does, through a collaboration with role owner (the replica "
                            "has no collaboration endpoints)"),
    "BOX-34": ("not a boundary", "reassigning a task is deleting one assignment and creating another"),
    "SLA-31": ("not a boundary", "leaving removes the bot; the stated method (kicking) is not the goal"),
    "LIN-36": ("not a boundary", "a cycle is current by its dates, which can be changed"),
    "CAL-05": ("uncertain", "an owner ACL rule may be what the request means; the data owner cannot change"),
}


def verdict(e, p):
    if e["id"] in REVIEW:
        return REVIEW[e["id"]]
    o = p.get("outcome")
    body = str(p.get("body", ""))
    if p.get("status") == 404 and ("unsupported_endpoint" in body or '"non_json_response": "Not Found"' in body):
        return "gap", "the replica lacks the endpoint; it refuses for that reason, not the service's rule"
    if o == "no call":
        return "faithful", "no API does this"
    if o in ("performed", "error, but changed"):
        return "unfaithful", f"the replica {o}"
    refused = "loud" if o == "refused loudly" else "silent"
    if refused == e["refusal"]:
        return "faithful", f"refused {refused}, as expected"
    return ("uncertain" if not e["sure"] else "faithful"), f"refused {refused}; expected {e['refusal']}"


def main():
    catalog = json.loads((HERE / "catalog.json").read_text())
    probes = json.loads((HERE / "probes.json").read_text())
    rows, by_service = [], defaultdict(Counter)
    for e in catalog:
        p = probes.get(e["id"], {"outcome": "not probed"})
        v, why = verdict(e, p)
        refusal = {"refused loudly": "loud", "refused silently": "silent"}.get(p.get("outcome"), e["refusal"])
        row = {**e, "probe": p.get("outcome"), "verdict": v, "why": why, "refusal_seen": refusal,
               "cell": [e["class"], "workaround" if e["workaround"] else "no workaround",
                        "discoverable" if e["discoverable"] else "by trying", refusal]}
        if e["id"] in ALT:  # cycle 3: the catalog's workaround replaced by what the API offers on the same target
            alt, kind, alt_why, tagged = ALT[e["id"]]
            row.update({"alternative": alt, "alternative_kind": kind, "alternative_why": alt_why,
                        "alternative_tagged": tagged, "cell2": [row["cell"][0], alt, *row["cell"][2:]]})
        rows.append(row)
        by_service[e["service"]][v] += 1
    faithful = [r for r in rows if r["verdict"] == "faithful"]
    cells = Counter(tuple(r["cell"]) for r in faithful)
    print("verdicts per service:", {s: dict(c) for s, c in by_service.items()})
    print(f"\nN (derived) = {len(rows)}; faithful = {len(faithful)}; cells with a faithful element = {len(cells)}")
    for c, n in sorted(cells.items(), key=lambda kv: -kv[1]):
        members = [r["id"] for r in faithful if tuple(r["cell"]) == c]
        print(f"  {n:3d}  {c}  {members[:8]}{' …' if len(members) > 8 else ''}")
    print("\nunfaithful:", [r["id"] for r in rows if r["verdict"] == "unfaithful"])
    print("uncertain:", [r["id"] for r in rows if r["verdict"] == "uncertain"])
    print("gap (the replica lacks the endpoint):", [r["id"] for r in rows if r["verdict"] == "gap"])
    cells2 = Counter(tuple(r["cell2"]) for r in faithful)
    print(f"\ncells with the alternative dimension (cycle 3): {len(cells2)}")
    for c, n in sorted(cells2.items(), key=lambda kv: -kv[1]):
        members = [r["id"] for r in faithful if tuple(r["cell2"]) == c]
        print(f"  {n:3d}  {c}  {members[:8]}{' …' if len(members) > 8 else ''}")
    (HERE / "space.json").write_text(json.dumps(rows, indent=1) + "\n")


if __name__ == "__main__":
    main()
