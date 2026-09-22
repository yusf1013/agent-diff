"""Cross-check compressed exact counting against independent exhaustive DFS."""
import json
import random
import re

from grounding.modeling.routes import count_dfs, count_zdd
from grounding.paths import REPO_ROOT


def main():
    text = (REPO_ROOT / 'grounding/domains/slack/model.md').read_text().split('```mermaid\nerDiagram\n')[1].split('```')[0]
    edges = []
    for line in text.splitlines():
        match = re.fullmatch(r'\s*(\w+)\s+[^ ]+\s+(\w+)\s*:\s*(.*)', line)
        if match:
            edges.append(dict(id=str(len(edges)), source=match[1], target=match[2], role=match[3]))
    unavailable = {'NAMED_ROLE', 'ROLE_ASSIGNMENT', 'FILE', 'FILE_ATTACHMENT', 'USER_MENTION', 'MESSAGE_EDIT_RECORD'}
    screened = [e for e in edges if not unavailable & {e['source'], e['target']} and e['role'] != '"default in settings"']
    for graph, expected in [(edges, 2870), (screened, 212)]:
        dfs, compressed = count_dfs(graph), count_zdd(graph)
        assert dfs == compressed and sum(dfs.values()) == expected
    rng = random.Random(418)
    for _ in range(30):
        graph = [dict(id=str(i), source=str(rng.randrange(6)), target=str(rng.randrange(6))) for i in range(10)]
        for incompatible in [[], [['0', '1']]]:
            assert count_dfs(graph, incompatible) == count_zdd(graph, incompatible)
    for domain in ['box', 'calendar']:
        graph = json.loads((REPO_ROOT / f'grounding/domains/{domain}/model.json').read_text())
        for edges in [graph['relationships'], [e for e in graph['relationships'] if e['read_witnesses']]]:
            for incompatible in [[], graph['incompatible_relationship_pairs']]:
                assert count_dfs(edges, incompatible) == count_zdd(edges, incompatible)
    print('PASS: Slack 2870/212; 30 random multigraphs with/without exclusions; Box/Calendar full and screened length histograms.')


if __name__ == '__main__':
    main()
