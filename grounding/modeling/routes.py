"""Exact role-sensitive simple entity-route counts; no depth cutoff.

Input is an audited conceptual graph, not an ORM schema. Graphillion compresses
the set of undirected simple paths. Subdivision preserves parallel relationship
roles, and degree constraints prevent subdivision vertices becoming endpoints.
Each nonempty undirected path has exactly two directed reference routes.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import importlib.metadata
import json
from pathlib import Path
import sys


def count_dfs(edges, incompatible=()):
    adjacency = defaultdict(list)
    for i, edge in enumerate(edges):
        a, b = edge['source'], edge['target']
        if a != b:
            adjacency[a].append((b, edge.get('id', str(i))))
            adjacency[b].append((a, edge.get('id', str(i))))
    counts = Counter()

    def walk(node, visited, used):
        for nxt, role in adjacency[node]:
            selected = used | {role}
            if nxt not in visited and not any(set(pair) <= selected for pair in incompatible):
                depth = len(used)
                counts[depth + 1] += 1
                walk(nxt, visited | {nxt}, selected)

    for root in list(adjacency):
        walk(root, {root}, set())
    return dict(sorted(counts.items()))


def count_zdd(edges, incompatible=()):
    from graphillion import GraphSet
    universe, intermediates, nodes, representatives = [], [], set(), {}
    for i, edge in enumerate(edges):
        a, b = edge['source'], edge['target']
        if a == b:
            continue
        a, b, via = 'node:' + a, 'node:' + b, f'edge:{i}'
        nodes.update([a, b])
        intermediates.append(via)
        universe.extend([(a, via), (via, b)])
        representatives[edge.get('id', str(i))] = (a, via)
    if not universe:
        return {}
    GraphSet.set_universe(universe)
    paths = GraphSet.paths()
    paths = GraphSet.graphs(
        degree_constraints={v: range(0, 3, 2) for v in intermediates},
        graphset=paths,
    )
    for first, second in incompatible:
        if first in representatives and second in representatives:
            paths -= paths.including(representatives[first]).including(representatives[second])
    counts = {n: 2 * paths.graph_size(2 * n).len() for n in range(1, len(nodes))}
    counts = {n: count for n, count in counts.items() if count}
    assert sum(counts.values()) == 2 * paths.len()
    return counts


def summarize(edges, method='zdd', incompatible=()):
    counts = (count_zdd if method == 'zdd' else count_dfs)(edges, incompatible)
    return {'routes': sum(counts.values()), 'by_relationship_edges': counts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('graph', type=Path)
    parser.add_argument('--method', choices=['dfs', 'zdd'], default='zdd')
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    graph = json.loads(args.graph.read_text())
    edges = graph['relationships']
    result = {
        'domain': graph['domain'],
        'model_sha256': hashlib.sha256(args.graph.read_bytes()).hexdigest(),
        'counter': args.method,
        'python': sys.version.split()[0],
        'graphillion': importlib.metadata.version('graphillion') if args.method == 'zdd' else None,
        'rule': 'Both directions; distinct relationship roles; no repeated entity type; nonempty paths.',
        'entities': len(graph['entities']),
        'relationships': len(edges),
        'self_relationships_excluded': [e['id'] for e in edges if e['source'] == e['target']],
        'structural': summarize(edges, args.method),
    }
    if all('read_witnesses' in e for e in edges):
        readable = [e for e in edges if e['read_witnesses']]
        result['direct_read_screen'] = {
            'definition': 'Routes using modeled relationships with a read witness; not an ordinary-use or end-to-end-discovery certification.',
            'relationships': len(readable),
            'excluded_relationships': [e['id'] for e in edges if not e['read_witnesses']],
            **summarize(readable, args.method),
        }
        result['direct_read_and_tag_consistent'] = summarize(readable, args.method, graph.get('incompatible_relationship_pairs', []))
    print(json.dumps(result, indent=2), flush=True)
    if args.out:
        args.out.write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
