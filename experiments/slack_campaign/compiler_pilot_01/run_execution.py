"""Run the reviewed W01 compilation once with the existing solver and evaluator.

From the repository root:
  python -m experiments.slack_campaign.compiler_pilot_01.run_execution
Requires the local backend on :18000 and its existing local campaign database.
No author/reviewer calls, access-review model, prompt changes or semantic retries.
"""
import asyncio
from pathlib import Path
import sys

from grounding.slack_campaign import runtime
from grounding.slack_campaign.bedrock import save
from grounding.slack_campaign.generate import ROOT, read
from grounding.slack_campaign.usage import report
from grounding.slack_campaign.validate import validate_case

HERE = Path(__file__).resolve().parent
DATABASE = 'postgresql://postgres@127.0.0.1:15432/agentdiff_campaign'


def validate_installed(case, state):
    checks = validate_case({**case, 'seed': state})
    if checks['errors']:
        raise ValueError(str(checks['errors']))


async def main():
    case = read(HERE / 'W01/case.json')
    out = HERE / 'execution/W01'
    out.mkdir(parents=True, exist_ok=False)
    prepared = None
    status = {'case_id': case['case_id'], 'status': 'preflight',
              'source_case': str(HERE / 'W01/case.json'),
              'case_sha256': runtime.digest(case),
              'construction_review': str(HERE / 'review.md')}
    save(out / 'summary.json', status)
    try:
        checks = validate_case(case)
        save(out / 'source_validation.json', checks)
        if checks['errors']:
            raise ValueError(str(checks['errors']))
        prepared = await asyncio.to_thread(runtime.prepare, case, out / 'preflight', DATABASE)
        access = read(prepared['visibility_certification_path'])
        if not access['certified']:
            raise ValueError('Native visibility check failed: ' + str(access))
        status['status'] = 'solver_running'
        save(out / 'summary.json', status)
        print('Running unchanged baseline solver', flush=True)
        record = await runtime.run_prepared(case, prepared, out / 'solver', DATABASE,
                                            validate_installed=validate_installed)
        prepared = None
        status.update(solver_termination=record.get('termination'), solver_error=record.get('error'))
        if 'evaluation' not in record:
            raise ValueError('Solver produced no recorded diff')
        status['status'] = 'evaluator_running'
        save(out / 'summary.json', status)
        print('Running existing ordered evaluator with one mechanical repair allowed', flush=True)
        args = [sys.executable, str(ROOT / 'grounding/oracle_bedrock/run.py'),
                '--inputs', str(out / 'solver/oracle_input'),
                '--instructions', str(ROOT / 'grounding/oracle_bedrock/prompts/ordered.md'),
                '--schema', str(ROOT / 'docs/for eval/oracle-assessment.schema.json'),
                '--instruction-placement', 'after-evidence',
                '--repair-on-validation-failure', '--out', str(out / 'assessment')]
        save(out / 'evaluator_command.json', args)
        with (out / 'evaluator.log').open('w') as log:
            process = await asyncio.create_subprocess_exec(*args, stdout=log, stderr=asyncio.subprocess.STDOUT)
            code = await process.wait()
        chosen = out / ('assessment-repair-1' if (out / 'assessment-repair-1/summary.json').exists() else 'assessment')
        result = read(chosen / 'summary.json')
        status.update(status='completed' if code == 0 else 'evaluation_unresolved',
                      evaluator_output=str(chosen), validation_errors=result.get('validation_errors', []))
        if (chosen / 'assessment.json').exists():
            status['obligations'] = read(chosen / 'assessment.json')['obligations']
    except Exception as exc:
        status.update(status='error', error=f'{type(exc).__name__}: {exc}')
        raise
    finally:
        if prepared:
            await asyncio.to_thread(runtime.cleanup, prepared, DATABASE)
        save(out / 'summary.json', status)
        report(HERE)
        print(status, flush=True)


if __name__ == '__main__':
    asyncio.run(main())
