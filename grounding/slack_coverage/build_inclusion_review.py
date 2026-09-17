"""Validate and render the manual review of the fixed 212-route inventory.

No model calls and no automatic inclusion judgments. Semantic decisions live in
route_inclusion_review.json; this script checks bookkeeping and projects them.
"""

from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
INPUT = HERE / "route_inclusion_review.json"
CATALOG = HERE / "remaining_route_probe.json"
DECISIONS = {"retain", "pending_group", "limitation", "duplicate", "exclude", "unresolved"}
SHORT = {
    "WORKSPACE": "W", "USER": "U", "CONVERSATION": "C", "MESSAGE": "M",
    "WORKSPACE_MEMBERSHIP": "WM", "CONVERSATION_MEMBERSHIP": "CM", "REACTION": "R",
}


def prose(value):
    return "; ".join(str(item) for item in value) if isinstance(value, list) else str(value)


def cell(value):
    return prose(value).replace("|", "\\|").replace("\n", " ")


def classify_group(nodes):
    """Reproduce the discussion groups; this does not decide inclusion."""
    workspace, membership = "WORKSPACE" in nodes, "WORKSPACE_MEMBERSHIP" in nodes
    if not workspace:
        return "S2" if membership else "S1"
    if not membership:
        return "S3"
    index = nodes.index("WORKSPACE")
    if index in {0, len(nodes) - 1}:
        return "S4"
    arms = [list(reversed(nodes[:index])), nodes[index + 1:]]
    affiliation = next(arm for arm in arms if arm[0] == "WORKSPACE_MEMBERSHIP")
    conversation = next(arm for arm in arms if arm[0] == "CONVERSATION")
    if "USER" in conversation and conversation[-1] != "USER":
        return "D"
    if len(affiliation) > 2:
        return "B" if affiliation[2] == "CONVERSATION_MEMBERSHIP" else "C"
    return "A"


def main():
    review = json.loads(INPUT.read_text())
    candidates = json.loads(CATALOG.read_text())["all_routes"]
    expected = {f"R{i:03d}": row["nodes"] for i, row in enumerate(candidates, 1)}
    rows = review["routes"]
    ids = [row["route_id"] for row in rows]
    assert len(ids) == len(set(ids)) == len(expected) == 212, "Missing/duplicate rows"
    assert set(ids) == set(expected), "Review differs from fixed route inventory"
    assert review["catalog_sha256"] == hashlib.sha256(CATALOG.read_bytes()).hexdigest()
    group_by_id = {group["group_id"]: group for group in review["groups"]}
    grouped_ids = [rid for group in review["groups"] for rid in group["route_ids"]]
    assert len(group_by_id) == len(review["groups"]), "Duplicate group IDs"
    assert len(grouped_ids) == len(set(grouped_ids)) == 212, "Groups must partition the inventory"
    assert set(grouped_ids) == set(expected)
    for source in review["sources"]:
        path = ROOT / source["path"]
        assert path.is_file(), source["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source["sha256"], source["path"]
    for row in rows:
        rid = row["route_id"]
        assert row["nodes"] == expected[rid], rid
        assert row["decision"] in DECISIONS, rid
        group = group_by_id[row["group_id"]]
        assert rid in group["route_ids"] and row["decision"] == group["decision"], rid
        assert row["group_id"] == classify_group(row["nodes"]), rid
        for field in ("request_fragment", "selector", "scope", "api_evidence", "reason"):
            assert row.get(field), (rid, field)
        if row["decision"] == "duplicate":
            assert row["duplicate_of"] in expected and row["duplicate_of"] != rid, rid
        else:
            assert row.get("duplicate_of") is None, rid

    counts = Counter(row["decision"] for row in rows)
    roots = defaultdict(Counter)
    for row in rows:
        roots[row["nodes"][0]][row["decision"]] += 1

    output = [
        "# Slack route inclusion review", "", review["status"], "",
        review["scope_note"], "", "## Decisions", "",
        "| Decision | Routes |", "|---|---:|",
        *[f"| {decision} | {counts[decision]} |" for decision in sorted(DECISIONS)],
        f"| **Total** | **{len(rows)}** |", "",
        "## Groups for the inclusion decision", "",
        "Inverse routes remain separate requirements. Grouping related directions "
        "allows one consistent inclusion decision; it does not declare their referent selections equivalent.", "",
        "| Group | Routes | Decision | Relationship pattern |",
        "|---|---:|---|---|",
        *[f"| [{g['group_id']}](#{g['group_id'].lower()}) | {len(g['route_ids'])} | "
          f"{g['decision']} | {cell(g['title'])} |" for g in review["groups"]], "",
        "## Review standard", "", *[f"- {rule}" for rule in review["review_rules"]], "",
        "## By referent entity", "",
        "| Referent entity | Retain | Pending group decision | Limitation | Duplicate | Exclude | Unresolved |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for root, values in sorted(roots.items()):
        output.append("| " + root + " | " + " | ".join(str(values[d]) for d in
                      ("retain", "pending_group", "limitation", "duplicate", "exclude", "unresolved")) + " |")
    output.extend(["", "## Group details", ""])
    for group in review["groups"]:
        output.extend([
            f"### {group['group_id']}", "", f"**{group['title']}**", "",
            group["pattern"], "", group["reason"], "",
            "**Examples:** " + ", ".join(f"[{rid}](#{rid.lower()})" for rid in group["example_ids"]), "",
            "**All routes:** " + ", ".join(f"[{rid}](#{rid.lower()})" for rid in group["route_ids"]), "",
        ])
    output.extend([
        "", "## Reading the rows", "",
        "W = Workspace; U = User; C = Conversation; M = Message; WM = Workspace membership; "
        "CM = Conversation membership; R = Reaction. Route IDs preserve the original inventory order.",
        "", "Request fragments are manual inclusion witnesses, not generated benchmark cases. "
        "Each needs a concrete seed, complete task/card specification, and runtime validation before use. "
        "Scope restrictions are part of the retained witness, not claims about arbitrary environments.",
        "", "## Index", "",
        "| ID | Complete route | Group | Decision | Ordinary request fragment |",
        "|---|---|---|---|---|",
    ])
    for row in sorted(rows, key=lambda x: x["route_id"]):
        rid = row["route_id"]
        route = " → ".join(SHORT[node] for node in row["nodes"])
        output.append(f"| [{rid}](#{rid.lower()}) | {route} | [{row['group_id']}](#{row['group_id'].lower()}) | {row['decision']} | {cell(row['request_fragment'])} |")
    output.extend(["", "## Individual reviews", ""])
    for row in sorted(rows, key=lambda x: x["route_id"]):
        rid = row["route_id"]
        output.extend([
            f"### {rid}", "",
            "**Route:** " + " → ".join(row["nodes"]), "",
            f"**Decision:** {row['decision']}", "",
            f"**Group:** [{row['group_id']}](#{row['group_id'].lower()})", "",
            f"**Request:** {prose(row['request_fragment'])}", "",
            f"**Selection:** {prose(row['selector'])}", "",
            f"**Scope:** {prose(row['scope'])}", "",
            f"**API evidence:** {prose(row['api_evidence'])}", "",
            f"**Reason:** {prose(row['reason'])}", "",
        ])
        if row.get("duplicate_of"):
            output.extend([f"**Equivalent retained route:** [{row['duplicate_of']}](#{row['duplicate_of'].lower()})", ""])
    output.extend(["## Source snapshot", ""])
    for source in review["sources"]:
        relative = "../../" + source["path"].replace(" ", "%20")
        output.append(f"- [{source['path']}]({relative}) — SHA-256 `{source['sha256']}`")
    output.extend(["", "The builder verifies row completeness, route identity, source hashes, and required evidence fields. "
                   "It does not certify the semantic judgments or execute the proposed tasks.", ""])
    (HERE / "route_inclusion_review.md").write_text("\n".join(output))
    print(json.dumps({"reviewed": len(rows), "decisions": dict(sorted(counts.items()))}, indent=2))


if __name__ == "__main__":
    main()
