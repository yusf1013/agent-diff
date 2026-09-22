"""Native load/read checks for the manual suite; no model or solver calls.

backend/.venv/bin/python grounding/runs/manual_exemplars_01/check_reads.py
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import tempfile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2]))
from grounding.integrations.agentdiff.native_compile_check import check


def run(database_url, case_ids=None):
    manifest = json.loads((HERE / 'manifest.json').read_text())
    results = []
    current = {item['case_id']: item for item in manifest['cases']}
    if case_ids:
        unknown = set(case_ids) - current.keys()
        if unknown:
            raise ValueError(f'Unknown case IDs: {sorted(unknown)}')
        saved = HERE / 'read_checks.json'
        if saved.exists():
            results = [r for r in json.loads(saved.read_text())['results']
                       if r['case_id'] not in case_ids and r['case_id'] in current
                       and r.get('case_sha256') == current[r['case_id']]['sha256']]
    for item in manifest['cases']:
        if case_ids and item['case_id'] not in case_ids:
            continue
        path = HERE / item['path']
        case = json.loads(path.read_text())
        with tempfile.TemporaryDirectory(prefix='manual-slack-read-') as tmp:
            out = Path(tmp) / 'check'
            try:
                summary = check(case, out, database_url)
            except Exception as exc:
                summary = {'status': 'error', 'error': f'{type(exc).__name__}: {exc}'}
            result = {'case_id': case['case_id'], 'case_sha256': hashlib.sha256(path.read_bytes()).hexdigest(), **summary}
            if (out / 'visibility_check.json').exists():
                result['visibility'] = json.loads((out / 'visibility_check.json').read_text())
            if (out / 'visibility.json').exists():
                probes = json.loads((out / 'visibility.json').read_text())['probes']
                result['required_answer_probes'] = [
                    {'method': p['probe']['method'], 'params': p['probe'].get('params', {}),
                     'checks': p['probe']['checks'], 'errors': p['errors']}
                    for p in probes if p['probe'].get('checks')]
            results.append(result)
        print(case['case_id'], result['status'], 'visible=' + str(result.get('mechanical_visibility_established')), flush=True)
    results.sort(key=lambda r: r['case_id'])
    passed = sum(r['status'] == 'passed' and r.get('mechanical_visibility_established') for r in results)
    report = {'total': len(results), 'passed': passed, 'model_calls': 0,
              'scope': 'Actual isolated PostgreSQL loading and native Slack read/visibility checks. Includes required profile answer-field checks for W09/W10. No solver or platform HTTP authentication.',
              'results': results}
    (HERE / 'read_checks.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(f'Passed: {passed}/{len(results)}', flush=True)
    return passed == len(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database-url', default='postgresql://postgres@127.0.0.1:15432/agentdiff_campaign')
    parser.add_argument('--cases', nargs='+', help='Check these fixtures, retaining hash-matching saved results for others.')
    args = parser.parse_args()
    raise SystemExit(0 if run(args.database_url, args.cases) else 1)
