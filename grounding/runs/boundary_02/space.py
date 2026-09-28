"""The testable space: the catalog (catalog.json) filtered by the replica probes (probes.json).

    python grounding/runs/boundary_02/space.py      # writes space.json and prints the counts

Per element:
- `faithful`: the replica refuses as the real service does, loudly or silently, or the request has no API at all
  (no call);
- `unfaithful`: the replica performs the change the real service refuses, or errors but changes state;
- `uncertain`: the replica's refusal type differs from the catalog's expectation where the real behaviour is only
  believed.
The refusal dimension of a faithful element is the one the replica shows. The cell uses the four dimensions of
plan.md.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Reviewed after the probes: the probe outcome is right and the catalog's refusal guess was wrong or the element
# is not a real boundary. Id -> (verdict, reason).
REVIEW = {
    "CAL-05": ("faithful", "dataOwner is read-only; the replica ignores it silently, as Google does"),
    "CAL-13": ("uncertain", "eventType changes: ignored silently here; Google may refuse them loudly"),
    "CAL-14": ("uncertain", "an organizer may be able to set attendee responses through the API"),
    "LIN-04": ("faithful", "completedAt is not in IssueUpdateInput: refused loudly by the schema"),
    "LIN-20": ("uncertain", "real Linear may allow isGroup changes; the replica does"),
    "LIN-26": ("uncertain", "real Linear's issueRelationUpdate may accept a new type; the replica does"),
}


def verdict(e, p):
    if e["id"] in REVIEW:
        return REVIEW[e["id"]]
    o = p.get("outcome")
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
    (HERE / "space.json").write_text(json.dumps(rows, indent=1) + "\n")


if __name__ == "__main__":
    main()
