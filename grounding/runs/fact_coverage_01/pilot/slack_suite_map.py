"""Occurrence-level map of the 57-case manual Slack suite onto the Slack FDC catalog (no model or service calls).

    python3 -m grounding.runs.fact_coverage_01.pilot.slack_suite_map

A case "mentions" a fact when its fixed selector filters on the attribute, joins through the relationship role, or
(W05) counts members. Bindings and the workspace link are not mapped, and near-misses are not re-checked under FDC,
so this measures what the suite expresses, not FDC credit.
"""
import json
from itertools import combinations
from pathlib import Path

SUITE = Path(__file__).resolve().parents[2] / "manual_exemplars_01" / "cases"
ENTITY = {"users": "User", "channels": "Conversation", "messages": "Message", "message_reactions": "Reaction"}
JOIN = {"message_reactions": "R:message_reactions", "channel_members": "R:channel_members",
        "messages.channel_id": "R:messages.channel_id", "messages.user_id": "R:messages.user_id"}
FIELD = {"reaction_type": "reaction_type", "real_name": "real_name", "message_text": "message_text",
         "channel_name": "channel_name", "topic_text": "topic_text", "is_bot": "is_bot"}


def facts(case):
    selector = case["private"]["selector"]
    found = set()
    for part in [selector["focal"], *selector.get("auxiliary", [])]:
        for join in part["joins"]:
            fact = JOIN.get(join) or JOIN.get(join.split(".")[0])
            if fact:
                found.add(fact)
        for flt in part["filters"]:
            table = part["path"][flt["node"]]
            if table in ENTITY and flt["field"] in FIELD:
                found.add(f"A:{ENTITY[table]}.{FIELD[flt['field']]}")
    for flt in selector.get("scope", []):
        found.add(f"A:{ENTITY[selector['root_table']]}.{FIELD[flt['field']]}")
    if case["case_id"].startswith("W05-"):
        found.add("D:member_count")
    return found


def main():
    cases = {c["case_id"]: c for c in (json.loads(p.read_text()) for p in sorted(SUITE.glob("*.json")))}
    mentioned = {cid: facts(c) for cid, c in cases.items()}
    present = [cid for cid, c in cases.items() if c["private"]["mode"] in ("single", "multiple")]
    everything = set().union(*mentioned.values())
    from_present = set().union(*(mentioned[cid] for cid in present))
    print(f"cases {len(cases)}, target-present {len(present)}")
    print(f"facts mentioned by any case: {len(everything)}; by target-present cases: {len(from_present)}")
    print("  " + "; ".join(sorted(everything)))
    for size in range(1, len(present) + 1):
        covers = [combo for combo in combinations(present, size)
                  if set().union(*(mentioned[cid] for cid in combo)) == from_present]
        if covers:
            print(f"exact minimum cover over target-present cases: {size} (e.g. {', '.join(covers[0])}; "
                  f"{len(covers)} such covers)")
            break


if __name__ == "__main__":
    main()
