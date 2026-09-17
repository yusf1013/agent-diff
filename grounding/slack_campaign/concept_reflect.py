"""One native follow-up per saved conceptual writer conversation; no fresh authors."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path

from .bedrock import Conversation, save
from .concept_writer import DEFAULT_FOLDER, PROMPTS
from .usage import RATES, report


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(folder, prompts=PROMPTS):
    """Freeze the common follow-up and originals before any paid continuation."""
    cases = [a['case_id'] for a in read(folder / 'assignments.json')]
    originals = [folder / 'system.md', folder / 'assignments.json']
    for cid in cases:
        writer = folder / cid / 'writer'
        first = writer / 'turn-01'
        if read(first / 'summary.json')['status'] != 'returned':
            raise ValueError(f'{cid}: original response did not return successfully')
        originals.extend([folder / cid / 'input.md', writer / 'instructions.md'])
        originals.extend(p for p in first.iterdir() if p.is_file())
    hashes = {str(p.relative_to(folder)): digest(p) for p in sorted(originals)}
    text = (prompts / 'self_reflection.md').read_text()
    meta = folder / 'reflection'
    meta.mkdir(exist_ok=True)
    manifest = {
        'cases': cases, 'original_sha256': hashes,
        'followup_sha256': hashlib.sha256(text.encode()).hexdigest(),
        'procedure': 'One common user follow-up appended to the original native conversation.',
        'case_specific_feedback_supplied': False,
        'manual_review_supplied': False,
        'model_effort_or_output_budget_changed': False,
        'semantic_retries': 0,
    }
    path = meta / 'manifest.json'
    if path.exists() and read(path) != manifest:
        raise ValueError('Reflection inputs or original records changed; do not overwrite this experiment')
    prompt = meta / 'followup.md'
    if prompt.exists() and prompt.read_text() != text:
        raise ValueError('Recorded reflection follow-up differs')
    save(path, manifest)
    prompt.write_text(text)
    return cases, text


def verify_history(writer, followup):
    first = read(writer / 'turn-01/request.json')
    response = read(writer / 'turn-01/response.json')
    second = read(writer / 'turn-02/request.json')
    expected = [*first['messages'], {'role': 'assistant', 'content': response['content']},
                {'role': 'user', 'content': [{'type': 'text', 'text': followup}]}]
    if second['messages'] != expected:
        raise ValueError(f'Native continuation history mismatch: {writer}')
    if {k: v for k, v in second.items() if k != 'messages'} != {
            k: v for k, v in first.items() if k != 'messages'}:
        raise ValueError(f'System or model request settings changed: {writer}')


def reflect_one(folder, cid, followup):
    writer = folder / cid / 'writer'
    turns = sorted(p.name for p in writer.glob('turn-*') if p.is_dir())
    second = writer / 'turn-02'
    if turns == ['turn-01', 'turn-02']:
        summary = read(second / 'summary.json')
        verify_history(writer, followup)
        if summary['status'] == 'returned' and (second / 'output.md').exists():
            return summary
        raise ValueError(f'{cid}: prior incomplete reflection retained; no automatic retry')
    if turns != ['turn-01']:
        raise ValueError(f'{cid}: expected only the original turn; refusing an additional review')
    conversation = Conversation.resume(writer)
    try:
        conversation.ask(followup)
    finally:
        print(cid, 'reflection recorded', flush=True)
    verify_history(writer, followup)
    return read(second / 'summary.json')


def account(folder):
    report(folder)
    ledger = read(folder / 'usage_ledger.json')
    calls = [r for r in ledger if '/turn-02/' in r['source']]
    tokens = {k: sum((r.get('usage') or {}).get(k, 0) or 0 for r in calls) for k in RATES}
    output = {
        'invocations': len(calls), 'usage_unavailable': [r['source'] for r in calls if r['usage'] is None],
        'tokens': tokens,
        'cache_hit_calls': sum((r.get('usage') or {}).get('cache_read_input_tokens', 0) > 0 for r in calls),
        'estimated_cost_usd': sum(tokens[k] * RATES[k] / 1e6 for k in RATES),
        'historical_rates_usd_per_million': RATES,
        'cost_note': 'Incremental reflection cost, own historical-rate estimate; not a Bedrock invoice.',
    }
    save(folder / 'reflection/usage.json', output)
    return output


def verify_originals(folder):
    manifest = read(folder / 'reflection/manifest.json')
    changed = [rel for rel, sha in manifest['original_sha256'].items() if digest(folder / rel) != sha]
    if changed:
        raise ValueError(f'Original artifacts changed: {changed}')


def run(folder, concurrency, prompts=PROMPTS):
    cases, followup = prepare(folder, prompts)
    first = reflect_one(folder, cases[0], followup)
    second = reflect_one(folder, cases[1], followup)
    check = {'first_usage': first.get('usage'), 'second_usage': second.get('usage'),
             'cache_reuse_observed': (second.get('usage') or {}).get('cache_read_input_tokens', 0) > 0}
    save(folder / 'reflection/cache_check.json', check)
    if not check['cache_reuse_observed']:
        raise RuntimeError('No cache hit in second reflection; remaining calls not launched')
    failures = []
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(reflect_one, folder, cid, followup): cid for cid in cases[2:]}
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as exc:
                failures.append({'case_id': futures[future], 'error': str(exc)})
    verify_originals(folder)
    save(folder / 'reflection/run_status.json', {'cases': cases, 'failures': failures,
                                               'original_hashes_verified': True})
    if failures:
        raise RuntimeError(f'{len(failures)} reflections failed; original attempts retained')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--folder', type=Path, default=DEFAULT_FOLDER)
    parser.add_argument('--prompts', type=Path, default=PROMPTS)
    parser.add_argument('--run', action='store_true', help='Make one paid continuation per original case.')
    parser.add_argument('--concurrency', type=int, default=8)
    args = parser.parse_args()
    if not 1 <= args.concurrency <= 15:
        parser.error('concurrency must be 1..15')
    try:
        if args.run:
            run(args.folder, args.concurrency, args.prompts)
        else:
            prepare(args.folder, args.prompts)
    finally:
        if args.run:
            account(args.folder)


if __name__ == '__main__':
    main()
