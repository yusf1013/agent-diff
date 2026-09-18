"""Reproduce structural route diagnostics; this does not define coverage cells.

No API calls, model calls, task judgments, or mutations. The historical diagnostic
expands relationships in both directions and disallows repeated entity types.
Consequently it excludes useful parent-message and co-member paths as well.
"""

from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re


from grounding.paths import REPO_ROOT as ROOT
MODEL = ROOT / "grounding/domains/slack/model.md"

# Model section 3 and ledger D06/D08/D10/D12/D14/D15 say no direct API access.
# These are topological flags, not a complete proof of read/write impossibility.
NO_DIRECT_API_ENTITIES = {
    "NAMED_ROLE", "ROLE_ASSIGNMENT", "FILE", "FILE_ATTACHMENT",
    "USER_MENTION", "MESSAGE_EDIT_RECORD",
}


def summarize(paths):
    return {
        "routes": len(paths),
        "by_relationship_edges": dict(sorted(Counter(len(es) for _, es in paths).items())),
    }


def main():
    raw = MODEL.read_bytes()
    diagram = raw.decode().split("```mermaid\nerDiagram\n", 1)[1].split("```", 1)[0]
    edges = []
    adjacency = defaultdict(list)
    nodes = set()
    for line in diagram.splitlines():
        match = re.fullmatch(r"\s*(\w+)\s+[^ ]+\s+(\w+)\s*:\s*(.*)", line)
        if not match:
            if line.strip():
                raise ValueError(f"Unparsed diagram line: {line}")
            continue
        source, target, label = match.groups()
        index = len(edges)
        edges.append((source, target, label))
        nodes.update((source, target))
        if source != target:
            adjacency[source].append((target, index))
            adjacency[target].append((source, index))

    paths = []

    def extend(visited, edge_ids):
        for target, edge_id in adjacency[visited[-1]]:
            if target in visited:
                continue
            next_path = (visited + (target,), edge_ids + (edge_id,))
            paths.append(next_path)
            extend(*next_path)

    for root in sorted(nodes):
        extend((root,), ())

    default_edges = {i for i, (_, _, label) in enumerate(edges) if label == '"default in settings"'}
    if len(default_edges) != 1:
        raise ValueError("Expected the model's one default-conversation relationship")
    touches_unexposed = [p for p in paths if NO_DIRECT_API_ENTITIES.intersection(p[0])]
    avoids_unexposed = [p for p in paths if not NO_DIRECT_API_ENTITIES.intersection(p[0])]
    settings_only = [p for p in avoids_unexposed if default_edges.intersection(p[1])]
    remainder = [p for p in avoids_unexposed if not default_edges.intersection(p[1])]
    result = {
        "source": str(MODEL.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "interpretation": "Structural routes, not cells, meaningfulness labels, or executable-test counts.",
        "enumeration": "Both traversal directions; preserve parallel relationship identities; no repeated entity type.",
        "excludes": ["direct attributes", "terminal attributes", "resolution modes", "derived views", "structured content paths", "all repeated-entity-type paths"],
        "entity_nodes": len(nodes),
        "diagram_relationships": len(edges),
        "excluded_self_relationships": [e for e in edges if e[0] == e[1]],
        "no_direct_api_entity_flag": sorted(NO_DIRECT_API_ENTITIES),
        "all": summarize(paths),
        "partition": {
            "touches_flagged_entity": summarize(touches_unexposed),
            "avoids_flagged_entities_but_uses_default_setting": summarize(settings_only),
            "avoids_both": summarize(remainder),
        },
        "workspace_diagnostics": {
            "all_routes_touching_workspace": summarize([p for p in paths if "WORKSPACE" in p[0]]),
            "remainder_workspace_interior": summarize([p for p in remainder if "WORKSPACE" in p[0][1:-1]]),
            "remainder_workspace_endpoint": summarize([p for p in remainder if p[0][0] == "WORKSPACE" or p[0][-1] == "WORKSPACE"]),
            "remainder_without_workspace": summarize([p for p in remainder if "WORKSPACE" not in p[0]]),
        },
        "remainder_by_root": {root: summarize([p for p in remainder if p[0][0] == root]) for root in sorted(nodes)},
        "limitations": [
            "An unexposed entity is a flag for capability analysis, not a reason to delete inability tests.",
            "The remainder is not certified observable: attributes on these entities can also be hidden.",
            "Workspace traversal is not automatically redundant; scope and predicate decide.",
            "Association contraction changes apparent depth, not necessarily distinct selection meanings.",
        ],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
