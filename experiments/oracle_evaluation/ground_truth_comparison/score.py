"""Rescore saved Bedrock reports; no API calls or historical file mutations."""
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
BATCH = HERE.parent / 'ten_case_comparison'
TRUTH = REPO / 'grounding/slack_ground_truth'
LABELS = ['demonstrated_correct', 'demonstrated_incorrect', 'not_established']
POSITIVE = 'demonstrated_incorrect'


def read(p):
    return json.loads(p.read_text())


def fraction(a, b):
    return a / b if b else None


def normalized(card):
    return {k: v for k, v in card.items() if k != 'Grounding obligations'}


def metrics(pairs):
    confusion = Counter((x['expected'], x['observed']) for x in pairs)
    tp = confusion[POSITIVE, POSITIVE]
    fp = sum(n for (gold, pred), n in confusion.items() if gold != POSITIVE and pred == POSITIVE)
    fn = sum(n for (gold, pred), n in confusion.items() if gold == POSITIVE and pred != POSITIVE)
    tn = len(pairs) - tp - fp - fn
    correct = sum(x['expected'] == x['observed'] for x in pairs)
    per_class = {}
    for label in LABELS:
        support = sum(n for (g, p), n in confusion.items() if g == label)
        predicted = sum(n for (g, p), n in confusion.items() if p == label)
        hits = confusion[label, label]
        per_class[label] = {'support': support, 'predicted': predicted,
                            'precision': fraction(hits, predicted), 'recall': fraction(hits, support),
                            'f1': fraction(2 * hits, support + predicted)}
    return {'count': len(pairs), 'exact_matches': correct, 'accuracy': fraction(correct, len(pairs)),
            'violation_detection': {'positive_class': POSITIVE, 'tp': tp, 'fp': fp, 'fn': fn, 'tn': tn,
                                   'accuracy': fraction(tp + tn, len(pairs)), 'precision': fraction(tp, tp + fp),
                                   'recall': fraction(tp, tp + fn), 'f1': fraction(2 * tp, 2 * tp + fp + fn)},
            'per_class': per_class,
            'confusion': {g: {p: confusion[g, p] for p in LABELS + ['MISSING', 'NULL']} for g in LABELS}}


def main():
    cases = sorted([p.name for p in (BATCH / 'inputs').iterdir() if p.is_dir()], key=lambda x: int(x.split('_')[1]))
    observations = []
    summaries = []
    exclusions = []
    hashes = {}
    for tid in cases:
        gold_path = TRUTH / 'reports' / f'{tid}.json'
        gold = read(gold_path)
        old_cards = read(BATCH / 'inputs' / tid / 'cards.json')
        new_cards = read(TRUTH / 'inputs' / tid / 'cards.json')
        comparable = [str(i + 1) for i, card in enumerate(new_cards)
                      if i < len(old_cards) and normalized(card) == normalized(old_cards[i])]
        excluded = [str(i + 1) for i in range(len(new_cards)) if str(i + 1) not in comparable]
        old_spec = read(BATCH / 'inputs' / tid / 'task_spec.json')
        new_spec = read(TRUTH / 'inputs' / tid / 'task_spec.json')
        full_comparable = not excluded and old_spec == new_spec and len(old_cards) == len(new_cards)
        if excluded:
            exclusions.append({'test_id': tid, 'overall_obligations': excluded,
                               'reason': 'Card changed or was added after these evaluations. No historical prediction is remapped to a new obligation.',
                               'status_scoring': 'Entire case excluded from status/all-field comparison because its card/specification inventory changed.'})
        hashes[str(gold_path.relative_to(REPO))] = hashlib.sha256(gold_path.read_bytes()).hexdigest()
        for variant in ('ordered', 'separated'):
            for repeat in range(1, 6):
                folder = BATCH / 'runs' / f'{tid}-{variant}-{repeat}'
                repair = folder.with_name(folder.name + '-repair-1')
                if repair.exists():
                    folder = repair
                report_path = folder / 'assessment.json'
                report = read(report_path)
                summary = read(folder / 'summary.json')
                assert report['run_id'] == gold['run_id'], (tid, variant, repeat)
                assert report['test_id'] == tid
                assert summary['status'] == 'returned' and summary['stop_reason'] == 'end_turn'
                hashes[str(report_path.relative_to(REPO))] = hashlib.sha256(report_path.read_bytes()).hexdigest()
                checks = []

                def add(category, field, expected, observed, accepted=None):
                    observed = 'NULL' if observed is None else observed
                    obj = {'test_id': tid, 'variant': variant, 'repeat': repeat, 'category': category,
                           'field': field, 'expected': expected, 'observed': observed,
                           'strict_match': observed == expected,
                           'accepted_match': observed in (accepted or [expected]),
                           'report': str(report_path.relative_to(REPO))}
                    checks.append(obj)
                    observations.append(obj)

                for key in comparable:
                    add('overall_grounding', f'O{key}', gold['obligations'][key], report['obligations'].get(key, 'MISSING'))
                if full_comparable:
                    got_lines = {row['line']: row for row in report['lines']}
                    for row in gold['lines']:
                        n = row['line']
                        got = got_lines.get(n, {})
                        if 'task_status' not in row:
                            add('marker', f'L{n}', 'marker_only', 'marker_only' if got == {'line': n} else 'other')
                            continue
                        for field in ('task_status', 'execution_status'):
                            allowed = None
                            if tid == 'slack_115' and n == 5 and field == 'execution_status':
                                allowed = ['omitted', 'skipped']  # Explicit user adjudication.
                            add(field, f'L{n}', row[field], got.get(field, 'MISSING'), allowed)
                        for key, verdict in row['grounding'].items():
                            add('linked_grounding', f'L{n}.O{key}', verdict, got.get('grounding', {}).get(key, 'MISSING'))
                overall = [x for x in checks if x['category'] == 'overall_grounding']
                summaries.append({'test_id': tid, 'variant': variant, 'repeat': repeat,
                                  'report': str(report_path.relative_to(REPO)),
                                  'mechanical_pass': summary['validation_errors'] == [],
                                  'full_inventory_comparable': full_comparable,
                                  'all_comparable_overall_match': all(x['strict_match'] for x in overall),
                                  'all_fields_strict_match': all(x['strict_match'] for x in checks) if full_comparable else None,
                                  'all_fields_accepted_match': all(x['accepted_match'] for x in checks) if full_comparable else None})
    variants = {}
    for variant in ('ordered', 'separated'):
        obs = [x for x in observations if x['variant'] == variant]
        runs = [x for x in summaries if x['variant'] == variant]
        status = {}
        for field in ('task_status', 'execution_status', 'linked_grounding'):
            rows = [x for x in obs if x['category'] == field]
            status[field] = {'count': len(rows), 'strict_matches': sum(x['strict_match'] for x in rows),
                             'accepted_matches': sum(x['accepted_match'] for x in rows),
                             'strict_accuracy': fraction(sum(x['strict_match'] for x in rows), len(rows)),
                             'accepted_accuracy': fraction(sum(x['accepted_match'] for x in rows), len(rows))}
        variants[variant] = {
            'overall_grounding': metrics([x for x in obs if x['category'] == 'overall_grounding']),
            'unchanged_nine_case_overall_grounding': metrics([x for x in obs if x['category'] == 'overall_grounding' and x['test_id'] != 'slack_108']),
            'statuses': status, 'mechanical_pass': sum(x['mechanical_pass'] for x in runs), 'reports': len(runs),
            'all_comparable_overall_match': sum(x['all_comparable_overall_match'] for x in runs),
            'fully_comparable_reports': sum(x['full_inventory_comparable'] for x in runs),
            'all_fields_strict_match': sum(x['all_fields_strict_match'] is True for x in runs),
            'all_fields_accepted_match': sum(x['all_fields_accepted_match'] is True for x in runs)}
    per_case = []
    for tid in cases:
        for variant in ('ordered', 'separated'):
            obs = [x for x in observations if x['test_id'] == tid and x['variant'] == variant and x['category'] == 'overall_grounding']
            per_case.append({'test_id': tid, 'variant': variant, **metrics(obs)})
    output = {'scope': 'Saved ten-case Bedrock batch, five repeats per variant, latest repair when present. No new API calls.',
              'primary_unit': 'Overall grounding obligation per repeated evaluator report; three-class exact accuracy, incorrect as positive for precision/recall.',
              'exclusions': exclusions, 'variants': variants, 'per_case': per_case, 'runs': summaries,
              'mismatches': [x for x in observations if not x['strict_match']], 'file_sha256': hashes}
    (HERE / 'metrics.json').write_text(json.dumps(output, indent=2) + '\n')
    (HERE / 'judgments.jsonl').write_text(''.join(json.dumps(x) + '\n' for x in observations))
    print(json.dumps(variants, indent=2))


if __name__ == '__main__':
    main()
