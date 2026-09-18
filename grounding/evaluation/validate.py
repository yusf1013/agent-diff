"""Mechanical checks only. Do not certify or repair the model's semantic judgments."""
from __future__ import annotations
from jsonschema import Draft202012Validator
from grounding.evaluation.adapter import entries, paragraphs, pointer


def validate(report, schema, sources):
    errors = [f'schema: {e.json_path}: {e.message}' for e in Draft202012Validator(schema).iter_errors(report)]
    if errors:
        return {'errors': errors}
    spec, cards, task = sources['task_spec'], sources['card'], sources['prompt']
    def check(ok, message):
        if not ok:
            errors.append(message)
    check(report['test_id'] == task['test_id'] and report['run_id'] == task['run_id'], 'Test/run ID mismatch')
    check([x['line'] for x in report['lines']] == [x['line'] for x in spec], 'Line inventory/order mismatch')
    check(set(report['obligations']) == {str(i) for i in range(1, len(cards)+1)}, 'Card inventory mismatch')
    spec_by_line = {x['line']: x for x in spec}
    for row in report['lines']:
        if row['line'] not in spec_by_line:
            continue
        text = spec_by_line[row['line']]['text'].strip().rstrip(':,.').casefold()
        if 'grounding' not in row:
            # Only bare syntax markers may use the schema's short row. Conditions/actions may not.
            check(text in {'else', 'otherwise', 'end', 'endif', 'end if', 'endfor', 'end for'},
                  f'L{row["line"]}: marker-only output for a substantive specification line')
        allowed = set(map(str, spec_by_line[row['line']]['obligations']))
        got = set(row.get('grounding', {}))
        check(got <= allowed, f'L{row["line"]}: invented direct grounding link')
        if row.get('task_status') == 'active':
            check(got == allowed, f'L{row["line"]}: missing active grounding use')
        if 'grounding' in row and (row['task_status'] is None or row['execution_status'] is None or None in row['grounding'].values()):
            check(report['assessment_issue'] is not None, 'Blocked judgment without assessment issue')
    for key, overall in report['obligations'].items():
        uses = [r['grounding'][key] for r in report['lines'] if key in r.get('grounding', {})]
        if 'demonstrated_incorrect' in uses:
            check(overall == 'demonstrated_incorrect', f'O{key}: incorrect-use aggregation mismatch')
        elif None in uses:
            check(overall is None, f'O{key}: blocked-use aggregation mismatch')
        elif 'not_established' in uses or not uses:
            check(overall == 'not_established', f'O{key}: unsupported overall verdict')
        # All-correct aggregation still needs semantic evidence; leave that to review.
    required, covered = set(), set()
    diff = sources['diff']
    for kind in ('inserts', 'deletes'):
        required.update(f'{kind}/{i}' for i in range(len(diff[kind])))
    for i, update in enumerate(diff['updates']):
        before, after = update['before'], update['after']
        for key in before.keys() | after.keys():
            if key not in before or key not in after or before[key] != after[key]:
                required.add(f'updates/{i}/{key}')
    response_counts = {loc: len(paragraphs(text)) for loc, text in entries(sources['response'])}
    required.update(f'response:{loc}:{i}' for loc, n in response_counts.items() for i in range(1, n+1))
    for row in report['lines'] + report['unattributed']:
        for ref in row.get('evidence', []):
            source, loc = ref['source'], ref['location']
            try:
                if source in ('card', 'task_spec') and loc[:1] in ('O', 'L') and loc[1:].isdigit():
                    pointer(sources[source], '/' + str(int(loc[1:])-1))
                elif source != 'domain_semantics':
                    pointer(sources[source], loc)
            except (KeyError, ValueError, TypeError, IndexError) as exc:
                errors.append(f'Invalid evidence {source}:{loc}: {exc}')
            if source == 'response':
                nums = ref.get('paragraphs', list(range(1, response_counts.get(loc, 0)+1)))
                check(loc in response_counts and all(1 <= n <= response_counts[loc] for n in nums), f'Invalid response paragraphs: {ref}')
                covered.update(f'response:{loc}:{n}' for n in nums)
            elif source == 'diff':
                parts = loc.strip('/').split('/')
                if len(parts) == 2 and parts[0] in ('inserts', 'deletes'):
                    covered.add('/'.join(parts))
                elif len(parts) >= 2 and parts[0] == 'updates':
                    prefix = '/'.join(parts[:2]) + '/'
                    if len(parts) == 2:
                        covered.update(x for x in required if x.startswith(prefix))
                    elif len(parts) >= 4 and parts[2] == 'after':
                        covered.add(prefix + parts[3].replace('~1', '/').replace('~0', '~'))
    missing = sorted(required-covered)
    check(not missing, f'Unaccounted changes/response paragraphs: {missing}')
    return {'errors': errors, 'required_accounting_items': len(required), 'covered_accounting_items': len(required & covered),
            'missing_accounting_items': missing, 'semantic_correctness_checked': False}
