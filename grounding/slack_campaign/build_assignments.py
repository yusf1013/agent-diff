"""Build the fixed pilot assignment manifest; does not author tests or call a model."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path(__file__).with_name("pilot_assignments.json")
ROUTES = ROOT / "grounding/slack_coverage/route_inclusion_review.json"
ANALYSIS = ROOT / "grounding/slack_analysis/analysis.json"
DATASET = ROOT / "datasets/agent-diff-bench/all_numbered.jsonl"

# These are construction assignments, not generated prompts, seeds or answer labels.
# The direct User attribute assignment deliberately has no relationship-route ID.
# id, root, route, mode, focal field (or relation count), baseline, initial stage
PLAN = [
    ("P01", "USER", None, "single", "users.real_name", "slack_58", "enrich_reference"),
    ("P02", "MESSAGE", "R061", "multiple", "channels.channel_name", "slack_66", "introduce_focal_near_miss"),
    ("P03", "USER", "R145", "absent", "message_reactions.reaction_type", None, "generate"),
    ("P04", "MESSAGE", "R089", "multiple", "channels.channel_name", None, "generate"),
    ("P05", "CONVERSATION", "R009", "multiple", "relation_count", None, "generate"),
    ("P06", "CONVERSATION", "R024", "underspecified", "users.real_name", None, "generate"),
    ("P07", "CONVERSATION_MEMBERSHIP", "R045", "single", "users.real_name", None, "generate"),
    ("P08", "CONVERSATION_MEMBERSHIP", "R031", "absent", "users.real_name", None, "generate"),
    ("P09", "REACTION", "R111", "underspecified", "users.real_name", None, "generate"),
    ("P10", "REACTION", "R108", "multiple", "channels.channel_name", None, "generate"),
    ("P11", "WORKSPACE", "R165", "absent", "channels.channel_name", None, "generate"),
    ("P12", "WORKSPACE", "R179", "single", "users.real_name", None, "generate"),
    ("P13", "WORKSPACE_MEMBERSHIP", "R195", "underspecified", "users.real_name", None, "generate"),
    ("P14", "WORKSPACE_MEMBERSHIP", "R203", "multiple", "messages.message_text", None, "generate"),
]

TABLE_BY_ENTITY = {
    "USER": "users", "MESSAGE": "messages", "CONVERSATION": "channels",
    "CONVERSATION_MEMBERSHIP": "channel_members", "REACTION": "message_reactions",
    "WORKSPACE": "teams", "WORKSPACE_MEMBERSHIP": "user_teams",
}

RISKS = {
    "P01": "Keep the original person-name field focal when adding auxiliary conditions. This direct-attribute assignment does not claim relationship-route coverage.",
    "P02": "The plural request jointly intends the matching MCP deployment questions even though its existing seed contains one match. Preserve that target set and original prompt. A focal negative must match the message-content condition in a different channel.",
    "P03": "Establish absence using the focal emoji restriction while keeping plausible users, readable messages and other reactions. An empty environment is insufficient construction quality.",
    "P04": "The reacting person must be the person who holds the qualifying channel membership. Distinct qualifying paths to one message identify only one referent.",
    "P05": "Count distinct membership identities per conversation, including the acting user when that user is a member. Collection wording must jointly intend all matching conversations.",
    "P06": "Use partial name information on the focal User field to leave competing conversation selections. Two matches alone are insufficient if the request delegates a choice or jointly intends both.",
    "P07": "A conversation-membership referent is a user–conversation pair, not merely the user. Bound the candidate memberships naturally and preserve pair identity in the deliverable.",
    "P08": "Use only the profile-displayed workspace association; do not assume complete workspace-membership discovery. Keep the earlier route population nonempty and establish the missing focal person within the stated roster.",
    "P09": "A reaction is a message–user–emoji identity. The ambiguous user name must leave distinct intended reaction selections rather than merely multiple paths to one reaction.",
    "P10": "The message author, rather than the reactor, must hold the qualifying membership. Multiple qualifying reactions are distinct referents even when on one message.",
    "P11": "Use bounded non-DM channel candidates and actual exposed workspace IDs. Keep plausible channels/workspaces; establish absence through the channel-name restriction.",
    "P12": "Deduplicate by workspace identity, not qualifying reactions or users. More than one qualifying relationship path can still identify one workspace.",
    "P13": "Use only profile-displayed workspace memberships. Ambiguous focal reactor names must induce different candidate sets of user–workspace pairs, with no delegated selection.",
    "P14": "Return user–workspace membership pairs from the profile-displayed scope. The post author must be the membership's user; supplemental text must not replace the focal selection.",
}


def load_json(path: Path):
    return json.loads(path.read_text())


def build() -> dict:
    review = load_json(ROUTES)
    routes = {row["route_id"]: row for row in review["routes"]}
    analyses = {row["test_id"]: row for row in load_json(ANALYSIS)}
    tests = {row["test_id"]: row for row in map(json.loads, DATASET.read_text().splitlines())}
    assignments = []
    for assignment_id, root, route_id, mode, field, baseline_id, stage in PLAN:
        route = routes.get(route_id)
        nodes = route["nodes"] if route else [root]
        if route:
            assert route["decision"] == "retain", route_id
            assert nodes[0] == root, (route_id, root)
        if field == "relation_count":
            focal = {
                "kind": "relation_count", "node_index": 1,
                "identity_fields": ["channel_members.channel_id", "channel_members.user_id"],
                "group_by_node_index": 0,
                "value_policy": "Author chooses a natural explicit count; compute it over complete candidate membership data.",
            }
        else:
            assert field.split(".")[0] == TABLE_BY_ENTITY[nodes[-1]], (assignment_id, field)
            focal = {"kind": "field", "node_index": len(nodes) - 1, "field": field}
        assignment = {
            "assignment_id": assignment_id,
            "construction_type": "mutation" if baseline_id else "clean_generation",
            "referent_entity": root,
            "route_id": route_id,
            "route_nodes": nodes,
            "resolution_mode": mode,
            "focal_condition": focal,
            "stage": stage,
            "requires_near_miss": stage != "enrich_reference",
            "baseline_test_id": baseline_id,
            "baseline_obligation_index": 1 if baseline_id else None,
            "construction_risk": RISKS[assignment_id],
        }
        if route:
            assignment["route_context"] = {
                "status": "Catalog feasibility witness only; not the generated test prompt or its answer.",
                **{key: route[key] for key in ("group_id", "request_fragment", "selector", "scope", "api_evidence")},
            }
        if baseline_id:
            test, analysis = tests[baseline_id], analyses[baseline_id]
            obligation = analysis["obligations"][0]
            assert obligation["referent_entity"] == TABLE_BY_ENTITY[root]
            # Input cards/specs are manually curated task-design artifacts. No run
            # ground-truth judgments, native scores or solver outcomes are loaded.
            assignment["baseline_context"] = {
                "prompt": test["question"],
                "info": json.loads(test["info"]),
                "card": obligation["card"],
                "selection_rule": obligation["selection_rule"],
                "task_spec": analysis["task_spec"],
            }
        assignments.append(assignment)

    entity_counts = dict(sorted(Counter(row["referent_entity"] for row in assignments).items()))
    mode_counts = dict(sorted(Counter(row["resolution_mode"] for row in assignments).items()))
    assert len(assignments) == 14 and set(entity_counts.values()) == {2}
    assert len(entity_counts) == 7
    assert mode_counts == {"absent": 3, "multiple": 5, "single": 3, "underspecified": 3}
    assert len({row["assignment_id"] for row in assignments}) == len(assignments)
    assert sum(row["construction_type"] == "mutation" for row in assignments) == 2
    sources = [ROUTES, ANALYSIS, DATASET, ROOT / "systematic modeling/slack-conceptual-model.md"]
    return {
        "schema_version": "1.0",
        "status": "Pilot construction assignments only; no generated or validated cases and no claimed achieved coverage.",
        "provenance": "Manual campaign planning; prompts, seeds and updated cards must be authored by the separate Sonnet construction agent.",
        "comparison_policy": "Use existing baseline runs where comparable. Do not generate easy controls for newly authored or adapted cases. Report adapted-prompt comparisons as adapted variants, not environment-only causal pairs.",
        "selection_policy": "Fixed purposive feasibility pilot covering seven referent roots, all four modes, relation counts, long routes and workspace scope. No ground-truth run labels or solver outcomes were consulted to choose assignments.",
        "authoring_policy": {
            "locks": ["referent_entity", "route_nodes", "resolution_mode", "focal_condition"],
            "maximum_total_criteria": 3,
            "auxiliary_criteria": "Up to two author-chosen criteria; preserve an existing compound baseline's content restrictions.",
            "underspecified": "Partial information must remain on the focal field/path; competing candidate sets require clarification without delegated choice.",
            "near_miss": "A plausible focal negative satisfies all auxiliary criteria and violates the focal predicate. For ambiguity, competing positive selections are not themselves negatives.",
            "coverage_credit": "Only concrete validated cases earn coverage. Source witnesses and construction claims do not earn credit.",
        },
        "initial_assignment_count": len(assignments),
        "entity_counts": entity_counts,
        "mode_counts": mode_counts,
        "conditional_followups": [{
            "assignment_id": "P01-N1",
            "parent_assignment_id": "P01",
            "stage": "introduce_focal_near_miss",
            "condition": "The enriched P01 case is valid and its solver run has an accepted evaluator assessment with no demonstrated grounding failure. An invalid case or failed evaluation does not satisfy this gate.",
            "requires_near_miss": True,
            "preserve": ["P01 generated prompt", "referent entity", "focal identifying path", "resolution mode", "existing intended matches"],
            "counting": "One additional construction/run beyond the 14 initial assignments, only if the gate is met; not an easy-control run.",
        }],
        "sources": [{"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in sources],
        "assignments": assignments,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check the committed/generated manifest without rewriting it.")
    args = parser.parse_args()
    result = build()
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != rendered:
            raise SystemExit("Pilot manifest is missing or stale; run build_assignments.py.")
    else:
        OUTPUT.write_text(rendered)
    print(json.dumps({
        "initial_assignments": result["initial_assignment_count"],
        "construction_types": dict(Counter(row["construction_type"] for row in result["assignments"])),
        "entities": result["entity_counts"], "modes": result["mode_counts"],
        "conditional_additional_assignments": len(result["conditional_followups"]),
    }, indent=2))


if __name__ == "__main__":
    main()
