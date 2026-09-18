"""Adapt Agent-Diff saved runs and existing annotations into an oracle input bundle."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from grounding.evaluation.adapter import load


def write(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')


def prepare(run_path, analysis_path, tests_path, seed_path, docs_path, out):
    run = load(run_path)
    entry = next(row for row in map(json.loads, Path(tests_path).read_text().splitlines())
                 if row['test_id'] == run['test_id'])
    analysis = next(x for x in load(analysis_path) if x['test_id'] == run['test_id'])
    info = json.loads(entry['info']) if isinstance(entry['info'], str) else entry['info']
    if run.get('question') != entry['question']:
        raise ValueError('Run question differs from supplied test prompt')
    if 'final' in run and not isinstance(run['final'], str):
        raise ValueError('Recorded final is not a string; provide an explicit output mapping')
    if 'final' not in run and run.get('termination') not in ('error', 'timeout', 'turn_limit'):
        raise ValueError('Missing final without a recorded termination explaining incomplete execution')
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    write(out/'task.json', {'test_id': run['test_id'], 'run_id': run['run_id'], 'prompt': entry['question'],
                           'acting_user_id': info['impersonate_user_id'], 'seed_template': info['seed_template'],
                           'termination': run.get('termination'),
                           'final_response_recorded': 'final' in run})
    write(out/'cards.json', [x['card'] for x in analysis['obligations']])
    write(out/'task_spec.json', analysis['task_spec'])
    write(out/'initial_state.json', load(seed_path))
    write(out/'recorded_diff.json', run['evaluation']['diff'])
    write(out/'response.json', {'final': run['final']} if 'final' in run else {})
    steps = []
    for step in run['steps']:
        value = {k: step[k] for k in ('turn', 'action', 'observation') if k in step}
        value['assistant_text'] = [b['text'] for b in step.get('response', {}).get('content', []) if b.get('type') == 'text']
        steps.append(value)
    write(out/'trajectory.json', {'steps': steps, 'termination': run.get('termination')})
    (out/'api_docs').mkdir()
    docs = load(docs_path)
    for i, (name, value) in enumerate(docs.items()):
        # Documentation names are data, not paths supplied to the filesystem.
        filename = name if '/' not in name and '\\' not in name and name not in ('.', '..') else f'document_{i}'
        write(out/'api_docs'/f'{filename}.json', value)
    write(out/'api_docs/index.json', list(docs))
    write(out/'provenance.json', {'run': str(Path(run_path).resolve()), 'annotations': str(Path(analysis_path).resolve()),
                                'test_entries': str(Path(tests_path).resolve()), 'seed': str(Path(seed_path).resolve()),
                                'docs': str(Path(docs_path).resolve()),
                                'omitted': 'Benchmark scores/assertions, solver thinking/signatures/usage. No final snapshot reconstructed.'})


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    for name in ('run', 'analysis', 'tests', 'seed', 'docs', 'out'):
        p.add_argument('--'+name, type=Path, required=True)
    a = p.parse_args()
    prepare(a.run, a.analysis, a.tests, a.seed, a.docs, a.out)
