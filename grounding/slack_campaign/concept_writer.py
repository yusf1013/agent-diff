"""Seed-free Markdown writer pilot. Planning is local; --run makes paid calls."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path

from .bedrock import Conversation, save

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = Path(__file__).parent / 'prompts/v3'
DEFAULT_FOLDER = ROOT / 'experiments/slack_campaign/writer_pilot_03'

# Fixed before viewing any new writer outputs. Two counts are design choices,
# not a reinterpretation of existing benchmark cards or all possible modes.
PLAN = [
    ('W01', 'R083', 'multiple'),
    ('W02', 'R146', 'single'),
    ('W03', 'R024', 'underspecified'),
    ('W04', 'R089', 'absent'),
    ('W05', 'R009', 'multiple'),
    ('W06', 'R078', 'multiple'),
    ('W07', 'R058', 'underspecified'),
    ('W08', 'R108', 'single'),
    ('W09', 'R154', 'absent'),
    ('W10', 'R212', 'multiple'),
]

# Directional conceptual relationship labels, transcribed from the adopted model.
# No native schema, foreign-key query or seed population is given to the writer.
RELATIONS = {
    ('WORKSPACE', 'WORKSPACE_MEMBERSHIP'): ('has', 'belongs to workspace'),
    ('USER', 'WORKSPACE_MEMBERSHIP'): ('holds', 'is held by'),
    ('WORKSPACE', 'CONVERSATION'): ('contains', 'belongs to workspace'),
    ('CONVERSATION', 'CONVERSATION_MEMBERSHIP'): ('has', 'belongs to conversation'),
    ('USER', 'CONVERSATION_MEMBERSHIP'): ('holds', 'is held by'),
    ('CONVERSATION', 'MESSAGE'): ('contains', 'is located in'),
    ('USER', 'MESSAGE'): ('authors', 'is authored by'),
    ('MESSAGE', 'REACTION'): ('receives', 'is attached to'),
    ('USER', 'REACTION'): ('contributes', 'is contributed by'),
}


def label(entity):
    return entity.replace('_', ' ').title()


def relationship(left, right):
    if (left, right) in RELATIONS:
        return RELATIONS[left, right][0]
    if (right, left) in RELATIONS:
        return RELATIONS[right, left][1]
    raise ValueError(f'Unsupported conceptual edge: {left} -> {right}')


def system_prompt():
    return '\n\n'.join([
        (PROMPTS / 'writer.md').read_text().strip(),
        (PROMPTS / 'slack_capabilities.md').read_text().strip(),
        '# Adopted conceptual domain model\n\n' +
        (ROOT / 'systematic modeling/slack-conceptual-model.md').read_text().strip(),
    ]) + '\n'


def assignments():
    rows = json.loads((ROOT / 'grounding/slack_coverage/route_inclusion_review.json').read_text())['routes']
    routes = {row['route_id']: row for row in rows}
    result = []
    for cid, rid, mode in PLAN:
        route = routes[rid]
        if route['decision'] != 'retain':
            raise ValueError(f'{rid} is not a retained route')
        nodes = route['nodes']
        for left, right in zip(nodes, nodes[1:]):
            relationship(left, right)
        result.append({
            'case_id': cid, 'route_id': rid, 'route_nodes': nodes,
            'referent_entity': nodes[0], 'resolution_mode': mode,
            'match_count': {'single': 1, 'multiple': 2, 'absent': 0, 'underspecified': None}[mode],
            'alternative_count': 2 if mode == 'underspecified' else None,
            'selection_note': 'Fixed conceptual writer pilot; no seed or solver outcome supplied.',
        })
    return result


def user_prompt(assignment):
    nodes = assignment['route_nodes']
    mode = assignment['resolution_mode']
    mode_text = (PROMPTS / 'modes' / f'{mode}.md').read_text().format(
        match_count=assignment['match_count'], alternative_count=assignment['alternative_count'])
    edges = '\n'.join(
        f'- {label(left)} (position {i}) {relationship(left, right)} '
        f'{label(right)} (position {i+1}).'
        for i, (left, right) in enumerate(zip(nodes, nodes[1:]))
    )
    extra = ('\nInclude a distinct conversation-member count as an identifying condition. '
             'Count every member, including the actor if present.\n') if assignment['route_id'] == 'R009' else ''
    return (
        f'# Assignment {assignment["case_id"]}\n\n'
        f'Referent: {label(nodes[0])}\n\n'
        f'Route: {" → ".join(map(label, nodes))}\n\n'
        f'Resolution mode: {mode}\n\n'
        'Relationship meanings (positions identify conceptual roles, not database IDs):\n'
        f'{edges}\n\n'
        'Identify the first entity using this complete chain. Conditions on one '
        'intermediate role must concern that same record. Do not invent equality '
        'between a membership channel and a message location.\n'
        f'{extra}\n# Instructions for this assigned mode\n\n{mode_text.strip()}\n'
    )


def prepare(folder):
    folder.mkdir(parents=True, exist_ok=True)
    system = system_prompt()
    plan = assignments()
    # Fixed copies make authoring inputs inspectable without running a model.
    files = {folder / 'system.md': system}
    for a in plan:
        files[folder / a['case_id'] / 'input.md'] = user_prompt(a)
    for path, content in files.items():
        if path.exists() and path.read_text() != content:
            raise ValueError(f'Existing input differs; use a new experiment folder: {path}')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    save(folder / 'assignments.json', plan)
    save(folder / 'provenance.json', {
        'stage': 'Conceptual writer only; no compiler, solver or model reviewer.',
        'manual_work': 'Instructions, capability brief, assignment selection, and output assessments.',
        'automated_work': 'Separate Sonnet 5 authoring of Markdown sketches.',
        'system_sha256': hashlib.sha256(system.encode()).hexdigest(),
        'seed_supplied': False, 'native_schema_supplied': False,
        'mode_instructions': 'Exactly the assigned fragment is injected; alternatives stay out of the input.',
        'examples': 'Reviewed manual scenarios adapted to supported operations; not measured pilot cases.',
        'output_policy': 'Preserve first outputs without semantic retry or selection.',
        'cache_policy': 'Identical system prefix; five-minute ephemeral cache; verify native hits before parallel expansion.',
        'limits': {'calls': len(plan), 'max_output_tokens_per_call': 6000, 'effort': 'medium'},
    })
    return system, plan


def run_one(folder, system, a):
    case_folder = folder / a['case_id']
    out = case_folder / 'writer/turn-01/output.md'
    if out.exists():
        summary = json.loads((out.parent / 'summary.json').read_text())
        if summary['status'] == 'returned':
            return summary
        raise RuntimeError(f'Incomplete prior response retained: {out.parent}')
    agent = Conversation(case_folder / 'writer', system, output_format='markdown',
                         cache_system=True, max_tokens=6000)
    try:
        agent.ask((case_folder / 'input.md').read_text())
    finally:
        print(a['case_id'], 'recorded', flush=True)
    return json.loads((out.parent / 'summary.json').read_text())


def run(folder, concurrency):
    system, plan = prepare(folder)
    # The first two substantive cases also verify caching; no throwaway probe calls.
    first = run_one(folder, system, plan[0])
    second = run_one(folder, system, plan[1])
    cache_check = {
        'first_usage': first.get('usage'), 'second_usage': second.get('usage'),
        'cache_reuse_observed': (second.get('usage') or {}).get('cache_read_input_tokens', 0) > 0,
    }
    save(folder / 'cache_check.json', cache_check)
    if not cache_check['cache_reuse_observed']:
        raise RuntimeError('No native cache hit on second case; remaining calls not launched.')
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(run_one, folder, system, a): a['case_id'] for a in plan[2:]}
        failures = []
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as exc:
                failures.append({'case_id': futures[future], 'error': str(exc)})
        save(folder / 'run_status.json', {'failures': failures, 'assignments': len(plan)})
    if failures:
        raise RuntimeError(f'{len(failures)} recorded writer failures; no automatic retry')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--folder', type=Path, default=DEFAULT_FOLDER)
    p.add_argument('--run', action='store_true', help='Make ten paid writer calls; otherwise only prepare inputs.')
    p.add_argument('--concurrency', type=int, default=8)
    args = p.parse_args()
    if not 1 <= args.concurrency <= 15:
        p.error('concurrency must be 1..15')
    try:
        if args.run:
            run(args.folder, args.concurrency)
        else:
            prepare(args.folder)
    finally:
        if args.run:
            from .usage import report
            report(args.folder)


if __name__ == '__main__':
    main()
