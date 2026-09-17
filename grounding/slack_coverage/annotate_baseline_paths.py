"""Project manually reviewed identifying-path annotations; not an extractor.

Every exceptional path/quantity below was reviewed against the fixed cards and
requests. Defaults cover direct names/content and unresolved root populations.
No trajectory, evaluator judgment, or ground-truth run label is consumed.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ANALYSIS = HERE.parent / "slack_analysis/analysis.json"
ROOT = HERE.parents[1]

ENTITY = {
    "channels": "CONVERSATION", "messages": "MESSAGE", "users": "USER",
    "channel_members": "CONVERSATION_MEMBERSHIP", "user_teams": "WORKSPACE_MEMBERSHIP",
    "teams": "WORKSPACE", "message_reactions": "REACTION",
}
FK = {
    frozenset(("channels", "teams")): "channels.team_id",
    frozenset(("users", "user_teams")): "user_teams.user_id",
    frozenset(("teams", "user_teams")): "user_teams.team_id",
    frozenset(("channels", "channel_members")): "channel_members.channel_id",
    frozenset(("users", "channel_members")): "channel_members.user_id",
    frozenset(("messages", "channels")): "messages.channel_id",
    frozenset(("messages", "users")): "messages.user_id",
    frozenset(("messages", "message_reactions")): "message_reactions.message_id",
    frozenset(("users", "message_reactions")): "message_reactions.user_id",
    frozenset(("messages",)): "messages.parent_id",
}

def path(*entities):
    return {"entities": list(entities), "relationships": [
        FK[frozenset((a, b))] for a, b in zip(entities, entities[1:])
    ]}

PATHS = {}
def assign(keys, *paths):
    for key in keys.split():
        assert key not in PATHS, key
        PATHS[key] = list(paths)

# Root-local predicates are projected separately below. These are the actual
# relational identification routes, not routes implied by downstream writes.
assign("65.1 66.1 67.1 67.2 68.1 73.1 74.1 75.1 77.2 92.1 93.1 100.7 103.4 105.3 107.6 108.6 108.7 110.7 112.3 113.5", path("messages", "channels"))
assign("86.1", path("users", "messages", "channels"))
assign("87.1 108.2", path("users", "messages"))
assign("89.1", path("users", "user_teams", "teams"))
assign("90.1", path("users", "user_teams"))
assign("94.7 95.6 96.4 97.1 104.2 106.4 106.7 109.9", path("users", "channel_members", "channels"))
assign("95.10 98.6 99.5 107.4", path("messages", "users"))
assign("97.4 98.4 101.2 109.6", path("channels", "messages"))
assign("105.1", path("messages", "channels"), path("messages", "users"))
assign("105.2", path("messages", "channels", "channel_members", "users"), path("messages", "users"))
assign("106.1 115.1", path("channels", "channel_members"))
assign("106.5 109.7 114.2", path("message_reactions", "messages", "channels"))
assign("107.5", path("messages", "users"), path("messages", "messages", "channels"))
assign("110.4", path("users", "messages", "channels"))
assign("113.4", path("messages", "messages", "channels"))
assign("113.6", path("users", "messages", "channels"))
assign("114.1", path("channels", "channel_members", "users"))
assign("115.2", path("users", "channel_members", "channels"))

# Determined collections are requested as collections even when this seed has
# only one member. Named individuals remain separate single obligations.
MULTIPLE = set("66.1 67.1 74.1 75.1 76.1 77.1 87.1 89.1 92.1 94.7 95.3 95.6 96.1 96.4 97.1 97.2 97.4 101.2 103.3 104.2 106.1 106.4 106.7 108.1 108.2 109.6 110.6 112.1 113.1 113.2 113.4 114.1 115.1 115.2".split())
OPTIONAL = set("100.7 107.4 107.5 108.8".split())
CHOOSE_ONE = {"112.3"}

# Predicate fields only: ordinary joins/returned identifiers are not attribute
# coverage. Structural relation predicates are recorded by routes. Actor IDs
# are genuine direct field conditions but do not require a users-table join.
FIELDS = {}
def fields(keys, *names):
    for key in keys.split():
        assert key not in FIELDS, key
        FIELDS[key] = list(names)

fields("65.1 68.1", "channels.channel_name", "messages.message_id")
fields("66.1 67.1 67.2 74.1 75.1 93.1 108.6 108.7 110.7 113.5", "channels.channel_name", "messages.message_text")
fields("73.1 77.2 103.4", "channels.channel_name", "messages.message_text", "messages.user_id")
fields("76.1 77.1 87.1 94.8 97.4 101.2 102.3 102.4 102.11 108.1 108.2 108.8 109.6 110.6", "messages.message_text")
fields("78.1", "messages.message_text", "messages.user_id", "messages.parent_id")
fields("86.1", "channels.channel_name", "messages.message_text")
fields("89.1", "user_teams.role", "teams.team_name")
fields("90.1", "users.real_name", "user_teams.role")
fields("92.1 100.7 112.3", "channels.channel_name")
fields("94.1 95.1 95.9 96.2 96.3 98.7 98.8 101.5 101.8 102.6 103.1")
fields("94.5", "messages.user_id", "messages.message_text")
fields("94.7 95.6 96.4 97.1 104.2", "channels.channel_name")
fields("95.3 96.1 97.2 103.3 113.2")
fields("95.8 99.3 100.6 102.10 103.5", "messages.user_id", "messages.message_text")
fields("95.10 99.5 107.4", "users.real_name", "messages.message_text")
fields("97.10 97.11 99.4", "messages.user_id")
fields("98.4", "messages.message_text")
fields("98.6", "users.real_name")
fields("105.1", "channels.channel_name", "messages.message_text", "users.real_name")
fields("105.2", "users.real_name", "channels.is_dm", "channel_members.user_id", "messages.message_text")
fields("105.3", "channels.channel_name", "messages.message_text")
fields("106.1 115.1", "channel_members.user_id", "channels.is_dm")
fields("106.4 106.7", "channels.channel_name", "users.timezone")
fields("106.5 109.7 114.2", "channels.channel_name", "messages.message_text", "message_reactions.user_id", "message_reactions.reaction_type")
fields("107.5", "users.real_name", "messages.message_text", "channels.channel_name")
fields("107.6", "channels.channel_name", "messages.message_text", "messages.message_id")
fields("109.9", "channels.channel_name", "users.display_name")
fields("110.4", "users.real_name", "channels.channel_name")
fields("112.1 113.1", "channels.is_dm", "channels.is_private")
fields("113.4", "channels.channel_name", "messages.message_text")
fields("113.6", "channels.channel_name", "messages.message_text", "messages.parent_id")
fields("114.1", "users.real_name")
fields("115.2", "users.real_name", "users.user_id", "channels.is_dm", "channel_members.user_id")

NOTES = {
    "66.1": "The original request and task specification say MCP deployment questions (plural), so requested collection mode is retained although only one qualifying message exists. This mode annotation does not change the existing singleton referent set.",
    "78.1": "Reply status uses parent_id on the target itself; no parent record is identified, so no parent traversal is credited.",
    "89.1": "The original request explicitly names Test Workspace, so the full membership-to-workspace path is retained despite that workspace already fixing the shared scope. API exposure of its name is a separate limitation, not inferred from this annotation.",
    "92.1": "The existing permissive card deliberately selects the containing history, not an exact Gemini-message subset. Credit the channel-name path; do not manufacture a content predicate from summary output words.",
    "97.4": "The request seeks conversations (plural); the single containing channel in this seed does not turn the requested collection into single mode.",
    "98.4": "Both competing topic interpretations identify channels by their discussions. The path is stable although the intended topic and resulting set are unresolved; stored candidate channel IDs are outcomes, not prompt-given identifying attributes.",
    "101.2": "Plural source conversations form a collection even though only one containing channel resolves in the seed.",
    "105.1": "Robert is a named author in the original request. The existing sufficient field list relies on unique question content; the added path preserves that explicit author qualifier without changing the referent.",
    "105.2": "Sophie qualifies both the DM membership and message authorship. These are separate conjunctive paths, bound to the same Sophie; the actor's DM membership is an internal path condition.",
    "107.4": "The requested inaugural post can draw relevant material from the eligible GPU discussion population; it is not an exhaustive recap. Optional subset recorded separately from determined-collection mode.",
    "107.5": "Eligibility permits explicit circuit-tracer mention OR membership in its reply thread, with the named-author restriction. These paths are not all conjunctive; the prose/card selection rule retains that Boolean meaning. Parent traversal repeats messages and is outside the no-repeated-type route catalog.",
    "109.6": "The card resolves the five broad source conversations collectively; it imposes no exact message selection or ranking within those histories. This remains collection identification rather than optional message selection.",
    "112.3": "Explicitly delegated choose-one; six eligible IDs do not mean six requested actions or multiple mode.",
    "113.4": "The referent is the reply collection, selected through its parent root and that root's named channel. Reply count is an answer computation, not an identifying predicate. Repeated message type is preserved outside the catalog.",
    "113.6": "The requested subject is the original author's user. parent_id identifies root-versus-reply on the qualifying message; no second message record is traversed.",
    "115.2": "Select the first six eligible users by name after excluding the actor and existing DM counterparts. Exclusion is a real membership/conversation condition, not an assumed positive join. Record selected collection and retain negative relation semantics in the existing selection rule.",
}

def main():
    analysis = json.loads(ANALYSIS.read_text())
    catalog = json.loads((HERE / "route_inclusion_review.json").read_text())
    routes = {tuple(r["nodes"]): r for r in catalog["routes"]}
    rows = []
    seen = set()
    for test in analysis:
        for i, obligation in enumerate(test["obligations"], 1):
            key = f"{test['test_id'].split('_')[1]}.{i}"
            seen.add(key)
            card = obligation["card"]
            entity = obligation["referent_entity"]
            identifying_fields = FIELDS.get(key)
            if identifying_fields is None:
                identifying_fields = sorted({f for alt in card["Alternative sufficient identifying sets"] or [] for f in alt})
                # Remaining defaults are direct fields only, reviewed names,
                # archived flags, or literal message content.
                assert all(f.startswith(entity + ".") for f in identifying_fields), key
            paths = list(PATHS.get(key, []))
            if not paths or any(f.startswith(entity + ".") for f in identifying_fields):
                paths.insert(0, path(entity))
            assert all(p["entities"][0] == entity for p in paths)
            # Insert the one authorized card addition next to identifying sets.
            updated = {}
            for field, value in card.items():
                if field == "Identifying paths":
                    continue
                updated[field] = value
                if field == "Alternative sufficient identifying sets":
                    updated["Identifying paths"] = paths
            obligation["card"] = updated
            resolution = card["Resolution"]
            if resolution != "resolved":
                mode, policy = resolution, "unresolved_selection" if resolution == "underspecified" else "empty_match"
            elif key in OPTIONAL:
                mode, policy = None, "delegated_optional_subset"
            elif key in CHOOSE_ONE:
                mode, policy = "single", "delegated_choose_one"
            elif key in MULTIPLE:
                mode, policy = "multiple", "determined_collection"
            else:
                mode, policy = "single", "determined_single"
            route_ids, excluded, outside = [], [], []
            for p in paths:
                nodes = tuple(ENTITY[e] for e in p["entities"])
                r = routes.get(nodes)
                if r is not None:
                    (route_ids if r["decision"] == "retain" else excluded).append(r["route_id"])
                elif len(nodes) > 1:
                    outside.append(p)
            reason = NOTES.get(key)
            if not reason:
                if resolution == "underspecified" and not identifying_fields:
                    reason = "The existing card leaves selection unresolved without a supported field predicate. A root-only path does not invent an unavailable role/status field or award a speculative relationship route."
                elif key in OPTIONAL:
                    reason = "The request delegates selection from an eligible population without a fixed cardinality; retained outside the four requested-resolution-mode cells."
                elif mode == "multiple":
                    reason = "The request identifies a collection; cardinality is determined from the request and selection rule, not merely the number of seeded IDs."
                else:
                    reason = "Paths follow the existing referent's identifying conditions; answer/change computations and newly written destinations do not add paths."
            rows.append({
                "test_id": test["test_id"], "obligation": i,
                "referent_entity": entity, "requested_resolution_mode": mode,
                "selection_policy": policy, "identifying_paths": paths,
                "identifying_attributes": identifying_fields,
                "retained_complete_route_ids": sorted(set(route_ids)),
                "excluded_complete_route_ids": sorted(set(excluded)),
                "paths_outside_catalog": outside,
                "annotation_note": reason,
                "evidence": {"selection_rule": obligation["selection_rule"],
                    "task_spec_lines": [l["line"] for l in test["task_spec"] if i in l["obligations"]]},
            })
    assert set(PATHS) | set(FIELDS) | MULTIPLE | OPTIONAL | CHOOSE_ONE <= seen
    ANALYSIS.write_text(json.dumps(analysis, ensure_ascii=False, indent=2) + "\n")
    result = {
        "provenance": "Manual Codex annotation of all baseline Slack prompts/cards; mechanical projection only. No solver results or ground-truth run labels consulted.",
        "sources": ["grounding/slack_analysis/analysis.json", "datasets/agent-diff-bench/all_numbered.jsonl", "examples/slack/seeds/slack_bench_v2.json", "grounding/slack_coverage/route_inclusion_review.json"],
        "analysis_sha256": hashlib.sha256(ANALYSIS.read_bytes()).hexdigest(),
        "method": "Count only complete annotated ordered routes. No subroute/edge completion credit. Root-only identification is separate from the 174 nonempty relationship routes. Structural paths retain Boolean and shared-binding meaning from each existing selection rule; they are not executable query syntax. Predicate attributes exclude mere join handles. Shared workspace scope alone adds no workspace route; an explicitly named workspace does. Optional subsets remain outside the four-mode cells.",
        "summary": {"tests": len(analysis), "obligations": len(rows),
            "requested_resolution_modes": dict(Counter(r["requested_resolution_mode"] or "optional_subset" for r in rows)),
            "retained_complete_route_ids": sorted({rid for r in rows for rid in r["retained_complete_route_ids"]}),
            "identifying_attributes": sorted({f for r in rows for f in r["identifying_attributes"]})},
        "obligations": rows,
    }
    (HERE / "baseline_mapping.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result["summary"], indent=2))

if __name__ == "__main__":
    main()
