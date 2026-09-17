"""Resumable construction/execution stages for the bounded Slack pilot."""
from __future__ import annotations

import argparse
import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed
import copy
import json
import os
from pathlib import Path
import subprocess
import sys

from .bedrock import save
from .generate import construct, read, repair_construction, validate_assignment

ROOT = Path(__file__).resolve().parents[2]
RATES = {'input_tokens': 3.0, 'output_tokens': 15.0,
         'cache_creation_input_tokens': 3.75, 'cache_read_input_tokens': 0.30}


def assignments(folder, ids=None):
    paths = sorted((folder / 'assignments').glob('*.json'))
    return [read(p) for p in paths if not ids or p.stem in ids]


def construct_all(folder, selected, concurrency):
    def one(a):
        path = folder / 'construction' / a['case_id']
        if path.exists():
            return read(path / 'summary.json')
        source = read(a['source_case_path']) if a.get('source_case_path') else None
        summary = construct(a, path, source_case=source)
        if summary['status'] == 'review_rejected':
            try:
                summary = repair_construction(path, summary.get('review_issues') or ['Independent review did not pass; consult its concrete failed checks.'])
            except Exception as exc:
                summary.update(status='review_repair_error', error=f'{type(exc).__name__}: {exc}')
                save(path / 'summary.json', summary)
        return summary
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = [pool.submit(one, a) for a in selected]
        for future in as_completed(futures):
            print(json.dumps(future.result()), flush=True)


async def execute_all(folder, selected, concurrency, database_url):
    from . import runtime
    semaphore = asyncio.Semaphore(concurrency)

    async def one(a):
        async with semaphore:
            case_id = a['case_id']
            source = folder / 'construction' / case_id
            execution = folder / 'execution' / case_id
            if execution.exists():
                if (execution / 'summary.json').exists():
                    return read(execution / 'summary.json')
                return {'case_id': case_id, 'status': 'existing_incomplete_execution_requires_inspection'}
            if not (source / 'summary.json').exists() or read(source / 'summary.json')['status'] != 'construction_validated':
                return {'case_id': case_id, 'status': 'not_construction_validated'}
            execution.mkdir(parents=True)
            summary = {'case_id': case_id, 'status': 'preflight'}
            save(execution / 'summary.json', summary)
            prepared = None
            try:
                case = read(source / 'case.json')
                checked = validate_assignment(case, a)
                save(execution / 'source_validation.json', checked)
                if checked['errors']:
                    raise ValueError('Construction failed current validation: ' + str(checked['errors']))
                prepared = await asyncio.to_thread(runtime.prepare, case, execution / 'preflight', database_url)
                state = read(prepared['initial_state_path'])
                installed_case = {**case, 'seed': state}
                installed_check = validate_assignment(installed_case, a)
                save(execution / 'installed_validation.json', installed_check)
                if installed_check['errors']:
                    raise ValueError('Installed selector/card validation: ' + str(installed_check['errors']))
                visibility = runtime.certify_visibility(case, state, read(prepared['visibility_path']))
                save(execution / 'visibility_certificate.json', visibility)
                if not visibility.get('certified'):
                    summary.update(status='visibility_unresolved', visibility=visibility)
                    save(execution / 'summary.json', summary)
                    return summary

                def callback(original, actual):
                    errors = validate_assignment({**original, 'seed': actual}, a)['errors']
                    if errors:
                        raise ValueError('Installed validation before solver: ' + str(errors))

                summary.update(status='solver_running')
                save(execution / 'summary.json', summary)
                run = await runtime.run_prepared(case, prepared, execution / 'solver', database_url,
                                                validate_installed=callback)
                prepared = None  # Runtime cleaned the owned template.
                summary.update(solver_termination=run.get('termination'), solver_error=run.get('error'))
                if 'evaluation' not in run:
                    raise ValueError('Solver yielded no recorded native diff')
                summary['status'] = 'evaluator_running'
                save(execution / 'summary.json', summary)
                out = execution / 'assessment'
                cmd = [sys.executable, str(ROOT / 'grounding/oracle_bedrock/run.py'),
                       '--inputs', str(execution / 'solver/oracle_input'),
                       '--instructions', str(ROOT / 'grounding/oracle_bedrock/prompts/ordered.md'),
                       '--schema', str(ROOT / 'docs/for eval/oracle-assessment.schema.json'),
                       '--instruction-placement', 'after-evidence', '--repair-on-validation-failure',
                       '--out', str(out)]
                with (execution / 'evaluator.log').open('w') as log:
                    process = await asyncio.create_subprocess_exec(*cmd, stdout=log, stderr=asyncio.subprocess.STDOUT)
                    code = await process.wait()
                repaired = out.with_name(out.name + '-repair-1')
                final = repaired if (repaired / 'summary.json').exists() else out
                evaluation = read(final / 'summary.json')
                summary.update(evaluator_output=str(final), evaluator_exit=code,
                               evaluator_validation_errors=evaluation.get('validation_errors', []))
                if code or evaluation.get('status') != 'returned' or evaluation.get('validation_errors'):
                    summary['status'] = 'evaluation_unresolved'
                else:
                    assessment = read(final / 'assessment.json')
                    summary.update(status='completed', obligations=assessment['obligations'],
                                   assessment_issue=assessment.get('assessment_issue'),
                                   automated_flags=[k for k, v in assessment['obligations'].items() if v == 'demonstrated_incorrect'])
                save(execution / 'summary.json', summary)
            except Exception as exc:
                summary.update(status='error', error=f'{type(exc).__name__}: {exc}')
                save(execution / 'summary.json', summary)
            finally:
                if prepared:
                    try:
                        await asyncio.to_thread(runtime.cleanup, prepared, database_url)
                    except Exception as exc:
                        summary['cleanup_error'] = str(exc)
                        save(execution / 'summary.json', summary)
            print(json.dumps(summary), flush=True)
            return summary

    return await asyncio.gather(*(one(a) for a in selected))


def report(folder):
    invocations = []
    for phase in ('author', 'reviewer'):
        for path in sorted((folder / 'construction').glob(f'*/{phase}/turn-*/summary.json')):
            row = read(path)
            invocations.append({'stage': phase, 'path': str(path), 'status': row['status'], 'usage': row.get('usage')})
    for path in sorted((folder / 'execution').glob('*/assessment*/summary.json')):
        row = read(path)
        invocations.append({'stage': 'evaluator', 'path': str(path), 'status': row['status'], 'usage': row.get('usage')})
    for path in sorted((folder / 'execution').glob('*/solver/*.json')):
        if path.stem != path.parent.parent.name:
            continue
        row = read(path)
        for step in row.get('steps', []):
            invocations.append({'stage': 'solver', 'path': str(path), 'turn': step['turn'],
                                'status': 'returned', 'usage': step.get('usage')})
        if row.get('error'):
            invocations.append({'stage': 'solver', 'path': str(path), 'status': 'episode_error',
                                'usage': None, 'note': 'Potential unreturned attempt; not assumed free.'})
    totals = {key: 0 for key in RATES}
    by_stage = {}
    unknown = 0
    for row in invocations:
        usage = row.get('usage')
        if usage is None:
            unknown += 1
            continue
        bucket = by_stage.setdefault(row['stage'], {key: 0 for key in RATES})
        for key in RATES:
            amount = usage.get(key, 0)
            totals[key] += amount
            bucket[key] += amount
    rows = []
    for a in assignments(folder):
        cid = a['case_id']
        construction = folder / 'construction' / cid / 'summary.json'
        execution = folder / 'execution' / cid / 'summary.json'
        rows.append({'case_id': cid, 'assignment': a,
                     'construction': read(construction) if construction.exists() else None,
                     'execution': read(execution) if execution.exists() else None})
    summary = {'cases': rows, 'recorded_invocations': len(invocations), 'unknown_usage_records': unknown,
               'tokens': totals, 'tokens_by_stage': by_stage,
               'estimated_cost_usd': sum(totals[k]*RATES[k]/1e6 for k in RATES),
               'estimate_rates_usd_per_million': RATES,
               'cost_note': 'Our estimate using the historical baseline rates, not a native billed dollar figure. Unknown usage excluded, not zero.',
               'claims': 'Pilot generation/evaluation observations; automated flags require confirmation. No G4 labels used.'}
    save(folder / 'usage_ledger.json', invocations)
    save(folder / 'report.json', summary)
    print(json.dumps({'cases': len(rows), 'recorded_invocations': len(invocations), 'tokens': totals,
                      'estimated_cost_usd': summary['estimated_cost_usd']}, indent=2))
    return summary


def main():
    p = argparse.ArgumentParser()
    p.add_argument('phase', choices=['construct', 'execute', 'report'])
    p.add_argument('--folder', type=Path, required=True)
    p.add_argument('--ids', nargs='+')
    p.add_argument('--concurrency', type=int, default=15)
    p.add_argument('--database-url', default=os.environ.get('DATABASE_URL'))
    a = p.parse_args()
    if not 1 <= a.concurrency <= 15:
        p.error('concurrency must be 1..15')
    selected = assignments(a.folder, a.ids)
    if a.phase == 'construct':
        construct_all(a.folder, selected, a.concurrency)
    elif a.phase == 'execute':
        asyncio.run(execute_all(a.folder, selected, a.concurrency, a.database_url))
    report(a.folder)


if __name__ == '__main__':
    main()
