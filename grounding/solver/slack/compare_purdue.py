"""Run the fixed manual suite on Purdue GenAI Studio models through the same episode interface.

Mirrors grounding/solver/slack/compare_manual.py: one scored trial per case/model,
same official prompt bytes, same 40-turn/480s episode loop, same sandbox bridge,
same environment prepare/diff/cleanup, same evidence layout. Only the model client
differs (OpenAI-compatible Purdue API instead of Bedrock), with provider defaults
and no caching. No evaluator calls are made here; manual judgments are a later pass.
"""
from __future__ import annotations

import argparse
import asyncio
from copy import deepcopy
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess

from grounding.integrations.agentdiff import runtime
from grounding.generation.validate import validate_case
from grounding.paths import REPO_ROOT
from grounding.solver.slack.purdue_client import PurdueClient

MODELS = {
    'qwen36': {'model': 'qwen3.6:27b', 'max_output_tokens': 16384,
               'thinking_budget': None,
               'rates': {'input_tokens': 0.0, 'output_tokens': 0.0,
                         'cache_creation_input_tokens': 0.0, 'cache_read_input_tokens': 0.0}},
}

COST_SOURCE = ('Purdue GenAI Studio has no per-token charge to this account; '
               'tokens are provider-reported, cost is recorded as 0 (not an invoice)')

_orig_load_baseline = runtime.load_baseline


def _purdue_save_model_request(llm, messages, prompt, options, path):
    """Save the logical OpenAI-style request actually sent to Purdue."""
    body = {"model": llm.model_id,
            "messages": llm._openai_messages(messages, prompt),
            "max_tokens": min(options["max_tokens"], llm.max_output_tokens or options["max_tokens"]),
            "stream": False}
    request = deepcopy(body)
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as handle:
        json.dump(request, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def _patched_load_baseline():
    module = _orig_load_baseline()
    module.BedrockClaudeClient = PurdueClient
    module.save_model_request = _purdue_save_model_request
    return module


runtime.load_baseline = _patched_load_baseline


def read(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def summarize(folder):
    records = []
    for p in sorted((folder / 'runs').glob('*/*/attempt-*/execution_summary.json')):
        s = read(p)
        record_path = p.parent / 'solver' / (s['case_id'] + '.json')
        if record_path.exists():
            r = read(record_path)
            s.update(usage=r.get('usage', {}), cost_usd=r.get('cost_usd', 0),
                     turns=len(r.get('steps', [])), termination=r.get('termination'))
            s['thinking_tokens'] = None
            s['thinking_tokens_note'] = 'unavailable: provider does not report thinking-token counts'
        s['evidence'] = str(p.parent.relative_to(folder))
        records.append(s)
    models = {}
    for alias, config in MODELS.items():
        rows = [r for r in records if r['model_alias'] == alias]
        tokens = {k: sum(r.get('usage', {}).get(k, 0) for r in rows) for k in config['rates']}
        models[alias] = {'attempts': len(rows), 'completed': sum(r['status'] == 'completed' for r in rows),
                         'tokens': tokens, 'thinking_tokens': None,
                         'thinking_tokens_note': 'unavailable: provider does not report thinking-token counts',
                         'estimated_cost_usd': 0.0,
                         'cost_source': COST_SOURCE}
    runtime.write(folder / 'usage_summary.json', {'models': models, 'attempts': records})
    return models


def check_installed(case, state):
    errors = validate_case({**case, 'seed': state})['errors']
    if errors:
        raise ValueError(str(errors))


async def execute(args, alias, item, slot):
    cid = item['case_id']
    root = args.out / 'runs' / alias / cid
    previous = sorted(root.glob('attempt-*/execution_summary.json'))
    if previous:
        latest = read(previous[-1])
        if not args.retry_infrastructure or latest['status'] != 'infrastructure_error':
            return latest
    attempt = len(previous) + 1
    out = root / f'attempt-{attempt:02}'
    out.mkdir(parents=True, exist_ok=False)
    state = {'case_id': cid, 'model_alias': alias, 'attempt': attempt, 'status': 'preflight',
             'started_utc': datetime.now(timezone.utc).isoformat()}
    runtime.write(out / 'execution_summary.json', state)
    case = read(args.out / 'dataset' / item['path'])
    prepared = None
    async with slot:
        try:
            check = validate_case(case)
            runtime.write(out / 'source_validation.json', check)
            if check['errors']:
                raise ValueError(str(check['errors']))
            prepared = await asyncio.to_thread(runtime.prepare, case, out / 'environment/preflight',
                                               args.database_url, args.base_url)
            state['status'] = 'solver_running'
            runtime.write(out / 'execution_summary.json', state)
            config = MODELS[alias]
            record = await runtime.run_prepared(
                case, prepared, out / 'solver', args.database_url, model=config['model'],
                validate_installed=check_installed, environment_out=out / 'environment',
                evaluation_inputs=out / 'evidence', max_output_tokens=config['max_output_tokens'],
                thinking_budget=config['thinking_budget'], rates=config['rates'], record_requests=True,
                prompt_caching_label='none_purdue', cost_source_label=COST_SOURCE)
            prepared = None
            if 'final' in record:
                (out / 'solver/final_response.md').write_text(record['final'] + '\n')
            state.update(termination=record.get('termination'), error=record.get('error'),
                         usage=record.get('usage'), cost_usd=record.get('cost_usd'),
                         status='infrastructure_error' if record.get('termination') in ('error', 'setup_error')
                         or 'evaluation' not in record else 'completed')
        except Exception as exc:
            state.update(status='infrastructure_error', error=f'{type(exc).__name__}: {exc}')
        finally:
            if prepared:
                await asyncio.to_thread(runtime.cleanup, prepared, args.database_url)
            state['ended_utc'] = datetime.now(timezone.utc).isoformat()
            runtime.write(out / 'execution_summary.json', state)
            summarize(args.out)
            print(json.dumps({k: state.get(k) for k in ('model_alias', 'case_id', 'attempt', 'status', 'termination', 'cost_usd', 'error')}), flush=True)
    return state


async def run(args):
    if not os.getenv('GENAI_API_KEY'):
        raise ValueError('GENAI_API_KEY must be set for Purdue runs')
    args.out.mkdir(parents=True, exist_ok=True)
    source_manifest = args.source / 'manifest.json'
    manifest = read(source_manifest)
    plan_file = args.out / 'plan.json'
    if not plan_file.exists():
        dataset = args.out / 'dataset'
        (dataset / 'cases').mkdir(parents=True)
        (dataset / 'manifest.json').write_bytes(source_manifest.read_bytes())
        for item in manifest['cases']:
            original = args.source / item['path']
            if sha(original) != item['sha256']:
                raise ValueError('Source hash mismatch: ' + item['case_id'])
            (dataset / item['path']).write_bytes(original.read_bytes())
        for name in ('story.md', 'story2.md', 'story3.md'):
            (dataset / name).write_bytes((args.source / name).read_bytes())
        prompt = runtime.load_baseline().official_prompt()
        (args.out / 'system_prompt.txt').write_text(prompt)
        runtime.write(plan_file, {'started_utc': datetime.now(timezone.utc).isoformat(),
            'source': str(args.source), 'manifest_sha256': sha(source_manifest),
            'git_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
            'models': MODELS, 'cases_per_model': manifest['total'], 'scored_trials_per_case': 1,
            'turn_limit': 40, 'episode_timeout_seconds': 480, 'concurrency': args.concurrency,
            'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest(),
            'prompt_caching': 'none on Purdue GenAI Studio; same prompt bytes, no cache markers',
            'warmup': 'first pending real case per model completes before remaining cases of that model launch',
            'qwen_settings': 'Provider defaults; no thinking/temperature overrides; 16384 max output tokens per call within 65536 deployed context',
            'retries': 'up to 6 attempts per call with exponential backoff (longer waits for rate-limit/transient-server 400s); shared cross-process rate limiter (60/min) acquired before every HTTP attempt including retries; episode infrastructure retries explicit and separately retained; no correctness retries',
            'manual_evaluation': 'Review all trajectories, final responses and unfiltered net diffs; no paid oracle or assertion scores',
            'solver_context_excludes': ['cards', 'selectors', 'private reference outcomes', 'story tables', 'manual judgments'],
            'fairness': 'Same official_prompt bytes, same XML action/done parsing (first action block per turn), same sandbox image, same environment lifecycle as manual_comparison_01; only model endpoint differs'})
    else:
        plan = read(plan_file)
        if plan['manifest_sha256'] != sha(source_manifest) or plan['models'] != MODELS:
            raise ValueError('Resume source/model configuration differs from recorded plan')
    selected = [v for v in manifest['cases'] if not args.cases or v['case_id'] in args.cases]
    if args.cases and {v['case_id'] for v in selected} != set(args.cases):
        raise ValueError('Unknown requested case')
    slot = asyncio.Semaphore(args.concurrency)

    async def model_batch(alias):
        pending = []
        for item in selected:
            prior = sorted((args.out / 'runs' / alias / item['case_id']).glob('attempt-*/execution_summary.json'))
            if not prior or (args.retry_infrastructure and read(prior[-1])['status'] == 'infrastructure_error'):
                pending.append(item)
        if not pending:
            return
        first = await execute(args, alias, pending[0], slot)
        if first['status'] != 'completed':
            print(f'{alias}: first case stopped; inspect setup before scaling', flush=True)
            return
        await asyncio.gather(*(execute(args, alias, item, slot) for item in pending[1:]))

    await asyncio.gather(*(model_batch(alias) for alias in args.models))
    print(json.dumps(summarize(args.out), indent=2), flush=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source', type=Path, default=REPO_ROOT / 'grounding/runs/manual_exemplars_01')
    p.add_argument('--out', type=Path, default=REPO_ROOT / 'grounding/runs/purdue_comparison_01')
    p.add_argument('--models', nargs='+', choices=MODELS, default=list(MODELS))
    p.add_argument('--cases', nargs='+')
    p.add_argument('--concurrency', type=int, default=10)
    p.add_argument('--retry-infrastructure', action='store_true')
    p.add_argument('--database-url', default='postgresql://postgres@127.0.0.1:15432/agentdiff_campaign')
    p.add_argument('--base-url', default='http://127.0.0.1:18001')
    args = p.parse_args()
    if not 1 <= args.concurrency <= 15:
        p.error('concurrency must be 1..15')
    asyncio.run(run(args))


if __name__ == '__main__':
    main()
