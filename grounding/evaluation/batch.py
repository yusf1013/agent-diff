"""Repeat prepared cases with fixed prompts and bounded concurrency."""
import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
from grounding.paths import PROMPTS, configured_path
import random
import subprocess
import sys
import time


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', type=Path, required=True, help='Directory containing prepared case directories')
    parser.add_argument('--cases', nargs='+', required=True)
    parser.add_argument('--variants', nargs='+', choices=['lean', 'ordered', 'separated'], default=['ordered', 'separated'])
    parser.add_argument('--repeats', type=int, default=5)
    parser.add_argument('--concurrency', type=int, default=15)
    parser.add_argument('--shuffle-seed', type=int, default=20260915)
    parser.add_argument('--out', type=Path, required=True, help='New output directory; never overwrite a previous experiment')
    parser.add_argument('--prepare-only', action='store_true', help='Assemble requests without invoking the model')
    args = parser.parse_args()
    if min(args.repeats, args.concurrency) < 1:
        parser.error('repeats and concurrency must be positive')
    if len(set(args.cases)) != len(args.cases) or len(set(args.variants)) != len(args.variants):
        parser.error('case and variant lists must not contain duplicates')
    for case in args.cases:
        if Path(case).name != case or case in ('.', '..'):
            parser.error('cases must be directory names, not paths')
        if not (args.inputs / case / 'task.json').is_file():
            parser.error(f'Missing prepared case: {case}')
    args.out.mkdir(parents=True, exist_ok=False)
    jobs = [(case, variant, n) for case in args.cases for variant in args.variants for n in range(1, args.repeats + 1)]
    random.Random(args.shuffle_seed).shuffle(jobs)
    prompts = {v: PROMPTS / 'evaluator' / (v + '.md') for v in args.variants}
    manifest = {
        'jobs': jobs, 'concurrency': args.concurrency, 'shuffle_seed': args.shuffle_seed,
        'prepare_only': args.prepare_only, 'inputs': str(args.inputs.resolve()),
        'prompt_sha256': {v: hashlib.sha256(p.read_bytes()).hexdigest() for v, p in prompts.items()},
        'repair_policy': 'At most one same-conversation mechanical repair; no semantic feedback or API retries.',
    }
    (args.out / 'launch-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')

    def run(job):
        case, variant, number = job
        name = f'{case}-{variant}-{number}'
        command = [sys.executable, '-m', 'grounding.evaluation.run', '--inputs', str((args.inputs / case).resolve()),
                   '--instructions', str(prompts[variant]), '--schema', str(configured_path('evaluator_schema')),
                   '--instruction-placement', 'after-evidence', '--effort', 'medium',
                   '--out', str((args.out / name).resolve())]
        command.append('--prepare-only' if args.prepare_only else '--repair-on-validation-failure')
        started = time.monotonic()
        with (args.out / (name + '.log')).open('w') as log:
            code = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT).returncode
        return {'name': name, 'exit_code': code, 'wall_seconds': round(time.monotonic() - started, 3)}

    failed = False
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures = [pool.submit(run, job) for job in jobs]
        for n, future in enumerate(concurrent.futures.as_completed(futures), 1):
            result = future.result()
            failed |= result['exit_code'] != 0
            with (args.out / 'completion.jsonl').open('a') as out:
                out.write(json.dumps(result) + '\n')
            print(f'{n}/{len(jobs)} {json.dumps(result)}', flush=True)
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
