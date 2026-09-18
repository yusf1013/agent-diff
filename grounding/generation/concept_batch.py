"""Compile fixed writer sketches, then run the existing solver and evaluator.

One bounded workflow per case. Source/review conflicts stop that case. There are
no writer calls, semantic retries of the solver/evaluator, or access-review calls.
"""
from __future__ import annotations

import argparse
import asyncio
from datetime import datetime, timezone
from pathlib import Path
import sys

from grounding.integrations.agentdiff import runtime
from grounding.common.bedrock import save
from grounding.generation.concept_compile import packet_for, run as compile_case
from grounding.common.io import ROOT, read
from grounding.common.usage import report
from grounding.generation.validate import validate_case
from grounding.common.layout import case_root
from grounding.paths import configured_path


def check_installed(case, state):
    result = validate_case({**case, 'seed': state})
    if result['errors']:
        raise ValueError(str(result['errors']))


async def execute(case_path, out, database_url, base_url, update):
    case = read(case_path)
    out.mkdir(parents=True, exist_ok=True)
    if (out/"execution_summary.json").exists() or (out/"solver").exists():
        raise ValueError("Execution already recorded; use a new run directory")
    state = {'case_id': case['case_id'], 'status': 'preflight',
             'source_case': str(case_path), 'case_sha256': runtime.digest(case)}
    prepared = None
    try:
        checks = validate_case(case)
        save(out/'generation/validation/source_validation.json', checks)
        if checks['errors']:
            raise ValueError(str(checks['errors']))
        prepared = await asyncio.to_thread(runtime.prepare, case, out/'environment/preflight', database_url, base_url)
        visibility = read(prepared['visibility_certification_path'])
        if not visibility['certified']:
            state.update(status='access_unresolved', access=visibility)
            return state
        state['status'] = 'solver_running'; save(out/'execution_summary.json', state); update(state)
        # run_prepared owns cleanup after it starts; outer cleanup also covers
        # pre-solver exceptions, and is safe when the exact template is gone.
        record = await runtime.run_prepared(case, prepared, out/'solver', database_url,
                                            validate_installed=check_installed,
                                            environment_out=out/'environment',
                                            evaluation_inputs=out/'evaluation/inputs')
        prepared = None
        state.update(solver_termination=record.get('termination'), solver_error=record.get('error'))
        if 'evaluation' not in record:
            raise ValueError('No recorded solver diff')
        if 'final' in record:
            (out/'solver/final_response.md').write_text(record['final']+'\n')
        state['status'] = 'evaluator_running'; save(out/'execution_summary.json', state); update(state)
        command = [sys.executable, '-m', 'grounding.evaluation.run',
                   '--inputs', str(out/'evaluation/inputs'),
                   '--instructions', str(configured_path('evaluator_prompt')),
                   '--schema', str(configured_path('evaluator_schema')),
                   '--instruction-placement', 'after-evidence', '--repair-on-validation-failure',
                   '--out', str(out/'evaluation/assessment')]
        save(out/'evaluation/command.json', command)
        with (out/'evaluation/run.log').open('w') as log:
            proc = await asyncio.create_subprocess_exec(*command, stdout=log, stderr=asyncio.subprocess.STDOUT, cwd=ROOT)
            code = await proc.wait()
        chosen = out/'evaluation'/('assessment-repair-1' if (out/'evaluation/assessment-repair-1/summary.json').exists() else 'assessment')
        summary = read(chosen/'summary.json')
        state.update(status='completed' if code == 0 else 'evaluation_unresolved',
                     evaluator_output=str(chosen), validation_errors=summary.get('validation_errors', []))
        if (chosen/'assessment.json').exists():
            state['obligations'] = read(chosen/'assessment.json')['obligations']
        return state
    except Exception as exc:
        state.update(status='error', error=f'{type(exc).__name__}: {exc}')
        return state
    finally:
        if prepared:
            await asyncio.to_thread(runtime.cleanup, prepared, database_url)
        save(out/'execution_summary.json', state)


async def run(args):
    if not 1 <= args.concurrency <= 15 or len(set(args.cases)) != len(args.cases):
        raise ValueError('Require distinct case IDs and concurrency between 1 and 15')
    packets = [packet_for(args.source, cid) for cid in args.cases]
    args.folder.mkdir(parents=True, exist_ok=False)
    save(args.folder/'plan.json', {
        'started_utc': datetime.now(timezone.utc).isoformat(), 'cases': args.cases,
        'source': str(args.source), 'source_sha256': {p['assignment']['case_id']: p['source_sha256'] for p in packets},
        'concurrency': args.concurrency, 'first_case_warms_compiler_cache': True,
        'max_compiler_turns': 3, 'evaluator_max_validation_repairs': 1,
        'writer_changes_allowed': False, 'manual_judgments_sent_to_models': False,
        'execution_requires': ['mechanical_validation', 'semantic_review_pass', 'native_preflight'],
        'quality_issues_reported_separately': True,
    })
    for packet in packets:
        cid = packet['assignment']['case_id']
        save(case_root(args.folder, cid)/'assignment.json', packet['assignment'])
    states = {cid: {'case_id': cid, 'status': 'pending'} for cid in args.cases}
    def update(value):
        states[value['case_id']] = dict(value)
        save(args.folder/'batch_summary.json', states)
        print(value['case_id'], value['status'], value.get('error', ''), flush=True)
    save(args.folder/'batch_summary.json', states)
    if not args.run:
        return
    slots = asyncio.Semaphore(args.concurrency)
    warmed = asyncio.Event()

    async def one(cid, first=False):
        if not first:
            await warmed.wait()
        async with slots:
            try:
                update({'case_id': cid, 'status': 'compiling'})
                source = case_root(args.folder, cid)/'generation'
                try:
                    result = await asyncio.to_thread(compile_case, args.source, cid, source)
                finally:
                    if first:
                        warmed.set()
                if result['status'] != 'review_pass':
                    update({'case_id': cid, 'status': 'construction_stopped', 'construction': result})
                    return
                update({'case_id': cid, 'status': 'preflight', 'construction': result})
                result = await execute(source/'case.json', case_root(args.folder, cid),
                                       args.database_url, args.base_url, update)
                update(result)
            except Exception as exc:
                update({'case_id': cid, 'status': 'error', 'error': f'{type(exc).__name__}: {exc}'})
            finally:
                # Only the event-loop thread updates the shared ledger. Individual
                # compilers have independent folders/ledgers and atomic records.
                report(args.folder)

    await asyncio.gather(*(one(cid, first=i == 0) for i, cid in enumerate(args.cases)))
    report(args.folder)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT/'grounding/runs/slack_campaign/writer_pilot_04')
    parser.add_argument('--folder', type=Path, required=True)
    parser.add_argument('--cases', nargs='+', default=[f'W{i:02}' for i in range(2, 11)])
    parser.add_argument('--concurrency', type=int, default=9)
    parser.add_argument('--base-url', default='http://127.0.0.1:18000')
    parser.add_argument('--database-url', default='postgresql://postgres@127.0.0.1:15432/agentdiff_campaign')
    parser.add_argument('--run', action='store_true')
    args = parser.parse_args()
    args.source = args.source.resolve(); args.folder = args.folder.resolve()
    asyncio.run(run(args))


if __name__ == '__main__':
    main()
