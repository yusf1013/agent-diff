"""Reproduce remaining_routes_audit.md structural counts; no semantic labels."""
from collections import Counter, defaultdict
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
MODEL = ROOT / 'systematic modeling/slack-conceptual-model.md'
HIDDEN = {'NAMED_ROLE', 'ROLE_ASSIGNMENT', 'FILE', 'FILE_ATTACHMENT', 'USER_MENTION', 'MESSAGE_EDIT_RECORD'}
ASSOCIATIONS = {'WORKSPACE_MEMBERSHIP', 'CONVERSATION_MEMBERSHIP', 'REACTION'}
diagram = MODEL.read_text().split('```mermaid\nerDiagram\n')[1].split('```')[0]
adj = defaultdict(list)
for line in diagram.splitlines():
    match = re.fullmatch(r'\s*(\w+)\s+([^ ]+)\s+(\w+)\s*:\s*(.*)', line)
    if not match:
        continue
    source, cardinality, target, label = match.groups()
    if source == target or source in HIDDEN or target in HIDDEN or label == '"default in settings"':
        continue
    assert cardinality.endswith('o{'), cardinality
    adj[source].append((target, 'many'))
    adj[target].append((source, 'optional' if cardinality.startswith('|o') else 'one'))

paths = []
def walk(nodes, steps):
    for target, cardinality in adj[nodes[-1]]:
        if target in nodes:
            continue
        expanded = (nodes + [target], steps + [cardinality])
        paths.append(expanded)
        walk(*expanded)

for root in sorted(adj):
    walk([root], [])

ordinary = [(nodes, steps) for nodes, steps in paths if nodes[0] not in ASSOCIATIONS and nodes[-1] not in ASSOCIATIONS]
print(json.dumps({
    'source': str(MODEL.relative_to(ROOT)),
    'routes': len(paths),
    'endpoint_types': dict(Counter(('association' if nodes[0] in ASSOCIATIONS else 'ordinary') + '_to_' + ('association' if nodes[-1] in ASSOCIATIONS else 'ordinary') for nodes, _ in paths)),
    'fanout_counts': dict(sorted(Counter(steps.count('many') for _, steps in paths).items())),
    'ordinary_endpoint_routes': len(ordinary),
    'ordinary_endpoint_display_depth_after_internal_association_contraction': dict(sorted(Counter(1 + sum(node not in ASSOCIATIONS for node in nodes[1:-1]) for nodes, _ in ordinary).items())),
    'all_routes': [{'nodes': nodes, 'directions': steps} for nodes, steps in paths],
}, indent=2))
