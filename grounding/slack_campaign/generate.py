"""Two-stage Sonnet construction with independent review and bounded repairs."""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path
import re

from .bedrock import Conversation, save

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
TABLES = ('teams', 'users', 'channels', 'user_teams', 'channel_members', 'messages', 'message_reactions')
KEYS = {'teams': ['team_id'], 'users': ['user_id'], 'channels': ['channel_id'],
        'user_teams': ['user_id', 'team_id'], 'channel_members': ['channel_id', 'user_id'],
        'messages': ['message_id'], 'message_reactions': ['message_id', 'user_id', 'reaction_type']}


def read(path):
    return json.loads(Path(path).read_text())


def dump(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(',', ':'))


def seed_schema():
    tree = ast.parse((ROOT / 'backend/src/services/slack/database/schema.py').read_text())
    result = {}
    for cls in tree.body:
        if not isinstance(cls, ast.ClassDef):
            continue
        table = next((ast.literal_eval(n.value) for n in cls.body if isinstance(n, ast.Assign)
                      and any(isinstance(t, ast.Name) and t.id == '__tablename__' for t in n.targets)), None)
        if table not in TABLES:
            continue
        fields = {n.target.id: ast.unparse(n.value) for n in cls.body
                  if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name)
                  and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name)
                  and n.value.func.id == 'mapped_column'}
        result[table] = {'primary_key': KEYS[table], 'columns': fields}
    return result


def domain_context():
    model = (ROOT / 'systematic modeling/slack-conceptual-model.md').read_text()
    docs = read(ROOT / 'examples/slack/testsuites/slack_docs/slack_api_full_docs.json')
    protocol = (ROOT / 'grounding/card extraction.md').read_text()
    cards = protocol.split('### 4.2 Locked card schema', 1)[1].split('### 4.3', 1)[0]
    return {'domain_model': model, 'seed_schema': seed_schema(), 'api_docs': docs,
            'locked_card_schema': cards,
            'runtime_qualifications': [
                'Use only these seven exposed tables in the initial pilot.',
                'Native message API ts is message_id; do not substitute stored ts.',
                'Supply explicit deterministic created_at timestamps where time matters.',
                'users.list/search use the actor selected workspace; known-ID histories may span workspaces if actor is a member.',
                'users.info exposes one selected workspace association. For reproducible profile predicates give each queried person one workspace membership. Actor may have all workspaces for access.',
                'No stored workspace-name lookup, profile writes, purpose writes, named roles or hidden-table operations.',
                'No API call beyond the supplied documentation is available to the solver.'
            ]}


def baseline_context(assignment):
    source_id = assignment.get('baseline_test_id') or assignment.get('source_test_id')
    if not source_id:
        return None
    entry = next(x for x in map(json.loads, (ROOT / 'datasets/agent-diff-bench/all_numbered.jsonl').read_text().splitlines())
                 if x['test_id'] == source_id)
    annotation = next(x for x in read(ROOT / 'grounding/slack_analysis/analysis.json') if x['test_id'] == source_id)
    info = json.loads(entry['info']) if isinstance(entry['info'], str) else entry['info']
    # The source seed is the actual referenced benchmark seed, never a ground-truth run label.
    seed = read(ROOT / 'examples/slack/seeds' / (info['seed_template'] + '.json'))
    return {'test_id': source_id, 'prompt': entry['question'], 'acting_user_id': info['impersonate_user_id'],
            'seed': seed, 'cards': [o['card'] for o in annotation['obligations']],
            'task_spec': annotation['task_spec']}


def materialize(output, base_seed=None):
    case = copy.deepcopy(output)
    if case.pop('status', 'compiled') == 'unrealized':
        raise ValueError('Author reported unrealized assignment')
    if base_seed is None:
        if 'seed_edits' in case and case['seed_edits']:
            raise ValueError('Clean generation must return a complete seed, not source edits')
        if not isinstance(case.get('seed'), dict):
            raise ValueError('Clean generation requires seed object')
    else:
        if 'seed' in case:
            raise ValueError('Mutation must return seed_edits, not replace the source seed')
        seed = copy.deepcopy(base_seed)
        for edit in case.get('seed_edits', []):
            table = edit['table']
            if table not in TABLES:
                raise ValueError(f'Unsupported edit table {table}')
            rows = seed.setdefault(table, [])
            op, key, values = edit['op'], edit.get('key', {}), edit.get('values', {})
            if op == 'insert':
                rows.append(copy.deepcopy(values))
                continue
            if set(key) != set(KEYS[table]):
                raise ValueError(f'Edit key must be complete native primary key for {table}')
            found = [r for r in rows if all(r.get(k) == v for k, v in key.items())]
            if len(found) != 1:
                raise ValueError(f'Edit must select exactly one existing {table} row: {key}')
            if op == 'update':
                if any(k in values and values[k] != key[k] for k in key):
                    raise ValueError('Primary-key mutation is not supported; use explicit delete/insert')
                found[0].update(copy.deepcopy(values))
            elif op == 'delete':
                rows.remove(found[0])
            else:
                raise ValueError('Unknown edit operation ' + str(op))
        case['seed'] = seed
    case.pop('seed_edits', None)
    for table in TABLES:
        case['seed'].setdefault(table, [])
    return case


def contract():
    from .selection import SELECTOR_GUIDE
    return '''Return a JSON object with exactly case_id, prompt, acting_user_id, seed OR seed_edits, cards, task_spec, private.
Clean generation: seed maps each of the seven table names to complete concrete rows; seed_edits absent.
Mutation: seed absent; seed_edits is a list of {table,op:"insert|update|delete",key:{actual PK fields},values:{fields}}. For insert values is the entire new row and key may be omitted. For update values is the changed fields only. Use every baseline row unchanged except these declared edits.
cards is an array of RAW fixed-schema cards, no wrapping {card:...}. Their Test ID is case_id and Grounding obligations is len(cards). Referent handles use scalar native IDs or objects containing precisely composite PK fields. All field names in cards refer to real tables/columns. Underspecified sufficient identifying/computation sets are null; its Referent set is the exact selection/partial_constraints/candidate_sets object.
task_spec is [{line:1,text:"ordinary requested action",obligations:[1]}], one-based consecutive lines, direct card indices; preserve indentation for branches.
private is {mode:"single|multiple|absent|underspecified",focal_obligation:1,selector:{...},expected_matches:[native handles],near_misses:[native handles],require_near_miss:true,candidate_sets:null,construction_explanation:"brief evidence for the distinction",mutation_summary:"concrete changes or clean generation"}.
For underspecified, expected_matches is the union of competing possible referents (not an authorized set), and candidate_sets is concrete alternatives matching the focal card. For absent it is []. For initial enrich, require_near_miss=false and near_misses may be []; otherwise true and include at least one plausible root that passes auxiliaries and fails focal. Do not list competing legitimate candidates as negatives.
The selector is a private checkable construction claim, not a solver instruction or card addition.
''' + str(SELECTOR_GUIDE)


def validate_assignment(case, assignment):
    from .validate import validate_case
    result = validate_case(case)
    errors = result.setdefault('errors', [])
    expected_id = assignment.get('case_id') or assignment['assignment_id']
    if case.get('case_id') != expected_id:
        errors.append(f'case_id must equal assigned {expected_id}')
    if case.get('private', {}).get('mode') != assignment.get('mode', assignment.get('resolution_mode')):
        errors.append('Private mode differs from assigned mode')
    route = assignment.get('route') or assignment.get('route_nodes')
    if isinstance(route, dict):
        route = route.get('nodes')
    mapping = {'WORKSPACE': 'teams', 'USER': 'users', 'CONVERSATION': 'channels',
               'WORKSPACE_MEMBERSHIP': 'user_teams', 'CONVERSATION_MEMBERSHIP': 'channel_members',
               'MESSAGE': 'messages', 'REACTION': 'message_reactions'}
    if route:
        expected_path = [mapping.get(n, n) for n in route]
        actual = case.get('private', {}).get('selector', {}).get('focal', {}).get('path')
        if actual != expected_path:
            errors.append(f'Focal path {actual} differs from assigned {expected_path}')
    root = assignment.get('referent_entity')
    if root and case.get('private', {}).get('selector', {}).get('root_table') != mapping.get(root, root):
        errors.append('Selector root differs from assigned referent entity')
    private = case.get('private', {})
    if private.get('require_near_miss') != assignment.get('requires_near_miss', True):
        errors.append('require_near_miss differs from the assigned stage')
    lock = assignment.get('focal_condition', {})
    focal = private.get('selector', {}).get('focal', {})
    if lock.get('kind') == 'field':
        required_field = lock['field'].split('.')[-1]
        if not any(f.get('node') == lock['node_index'] and f.get('field') == required_field for f in focal.get('filters', [])):
            errors.append(f'Focal query must use assigned field {lock["field"]} at node {lock["node_index"]}')
    elif lock.get('kind') == 'relation_count':
        if focal.get('count', {}).get('node') != lock['node_index'] or lock.get('group_by_node_index') != 0:
            errors.append('Focal count must use the assigned distinct entity node, grouped by root')
    if len(private.get('selector', {}).get('auxiliary', [])) > 2:
        errors.append('At most two auxiliary criteria are permitted')
    if assignment.get('construction_type') == 'clean_generation' and private.get('mode') == 'multiple' and len(result.get('computed_matches', [])) < 2:
        errors.append('Clean multiple construction must exercise at least two jointly intended roots')
    if assignment.get('baseline_context'):
        # This gate preserves explicit source literals without trying to grade prose.
        # Semantic action preservation is independently reviewed as well.
        original = assignment['baseline_context']['prompt']
        literals = re.findall(r"(?<![A-Za-z])'([^'\n]+)'(?![A-Za-z])|\"([^\"\n]+)\"", original)
        for choices in literals:
            literal = next(x for x in choices if x)
            if literal not in case.get('prompt', ''):
                errors.append(f'Source action/request literal must remain unchanged: {literal!r}')
        original_card = assignment['baseline_context']['card']
        if original_card['Resolution'] == 'resolved':
            idx = private.get('focal_obligation')
            cards = case.get('cards', [])
            current = cards[idx-1].get('Referent set') if type(idx) is int and isinstance(cards, list) and 1 <= idx <= len(cards) and isinstance(cards[idx-1], dict) else None
            if not isinstance(current, list) or dump(sorted(original_card['Referent set'], key=dump)) != dump(sorted(current, key=dump)):
                errors.append('This mutation stage must preserve the source intended referents')
    if assignment.get('stage') == 'introduce_focal_near_miss':
        source_prompt = assignment.get('locked_prompt') or assignment.get('baseline_context', {}).get('prompt')
        if source_prompt and case.get('prompt') != source_prompt:
            errors.append('Near-miss stage must preserve the supplied source prompt verbatim')
    return result


def repair_construction(folder, issues, *, kind='semantic'):
    """One explicit review repair, preserving both native conversations and old files."""
    folder = Path(folder)
    if kind not in ('semantic', 'runtime', 'annotation'):
        raise ValueError('Unknown repair stage')
    if (folder / f'{kind}_repair.json').exists():
        raise ValueError(f'{kind} repair already attempted for this construction')
    save(folder / f'{kind}_repair.json', {'issues': issues, 'kind': kind})
    packet = read(folder / 'input.json')
    assignment, source = packet['assignment'], packet['source']
    previous = read(folder / 'summary.json')
    save(folder / f'summary-before-{kind}-repair.json', previous)
    save(folder / 'summary.json', {**previous, 'status': 'repair_running', 'repair_kind': kind})
    original_case = read(folder / 'case.json') if kind == 'annotation' else None
    if original_case is not None:
        save(folder / 'case-before-annotation-repair.json', original_case)
    author = Conversation.resume(folder / 'author')
    if kind == 'annotation':
        output = author.ask(
            'Thanks. Review found these annotation defects. Make only the required changes to the cards '
            'and task specification. Return exactly {cards:[...],task_spec:[...]} with both complete arrays; '
            'do not return any other fields. The request, actor, seed, every private field, and assignment '
            'are frozen. Preserve the number and order of grounding obligations and their concrete '
            'referents/candidate sets; correct only the identified annotation defects. Do not introduce '
            'intermediate implementation work as requested actions.\n'
            + dump({'issues': issues, 'current_annotations': {
                'cards': original_case['cards'], 'task_spec': original_case['task_spec']}}))
        case = copy.deepcopy(original_case)
        checked = {'errors': []}
        if not isinstance(output, dict) or set(output) != {'cards', 'task_spec'}:
            checked['errors'].append('Annotation repair must return exactly cards and task_spec; all other case fields are frozen')
        else:
            case.update(copy.deepcopy(output))
            checked = validate_assignment(case, assignment)
            # Compare every protected field, including all private annotations.
            # This remains a gate even if the response contract later changes.
            protected = lambda item: {key: value for key, value in item.items() if key not in ('cards', 'task_spec')}
            if protected(case) != protected(original_case):
                checked['errors'].append('Annotation repair changed protected case fields')
            old_cards, new_cards = original_case.get('cards'), case.get('cards')
            if not isinstance(new_cards, list) or len(new_cards) != len(old_cards):
                checked['errors'].append('Annotation repair must preserve grounding-obligation count and ordering')
            else:
                for index, (old, new) in enumerate(zip(old_cards, new_cards), 1):
                    if not isinstance(new, dict):
                        continue  # Fixed card validation already reports this.
                    for field in ('Resolution', 'Grounding obligation name'):
                        if new.get(field) != old.get(field):
                            checked['errors'].append(f'Annotation repair changed O{index} {field}')
                    old_ref, new_ref = old.get('Referent set'), new.get('Referent set')
                    if old.get('Resolution') == 'underspecified' and isinstance(old_ref, dict) and isinstance(new_ref, dict):
                        # one(entity)/set(entity) is annotation; the alternatives
                        # and established constraints themselves remain frozen.
                        for field in ('candidate_sets', 'partial_constraints'):
                            if new_ref.get(field) != old_ref.get(field):
                                checked['errors'].append(f'Annotation repair changed O{index} {field}')
                    elif new_ref != old_ref:
                        checked['errors'].append(f'Annotation repair changed O{index} Referent set')
    else:
        output = author.ask('Thanks. Review found these construction defects. Make only the required changes, '
                            'preserving the assignment and unrelated content. Return the complete compilation object.\n'
                            + dump(issues) + '\n' + contract())
        case = materialize(output, source['seed'] if source else None)
        checked = validate_assignment(case, assignment)
    save(folder / f'case-after-{kind}-repair.json', case)
    save(folder / f'validation-after-{kind}-repair.json', checked)
    if checked['errors']:
        previous.update(status='invalid_after_annotation_repair' if kind == 'annotation' else 'invalid_after_review_repair', errors=checked['errors'])
    else:
        reviewer = Conversation.resume(folder / 'reviewer')
        review = reviewer.ask('Review this corrected case independently. The prior case and review remain historical. '
                              'Check the actual contents against the supplied source and assignment; verify that every '
                              'identifying attribute alternative is independently sufficient without inserting answer-only IDs. '
                              'Preserve original action arguments, including quoted contents.\n' + dump({'case': case, 'mechanical_findings': checked, 'review_feedback': issues}))
        save(folder / f'review-after-{kind}-repair.json', review)
        expected_checks = {'prompt_path_fidelity','resolution','negatives','realism_and_hints','api_scope','cards_and_spec','mutation_integrity'}
        checks = review.get('checks', [])
        passed = (review.get('decision') == 'pass' and len(checks) == 7
                  and {c.get('name') for c in checks} == expected_checks
                  and all(c.get('status') == 'pass' for c in checks))
        previous.update(status='construction_validated' if passed else 'review_rejected_after_repair',
                        review_decision=review.get('decision'), review_issues=review.get('issues'))
        if passed:
            save(folder / 'case.json', case)
    previous.update({f'{kind}_repairs': 1, 'runtime_validated': False})
    save(folder / 'summary.json', previous)
    return previous


def construct(assignment, out, *, model='us.anthropic.claude-sonnet-5', source_case=None):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    source = source_case or baseline_context(assignment)
    context = domain_context()
    packet = {'assignment': assignment, 'domain': context, 'source': source}
    save(out / 'input.json', packet)
    save(out / 'assignment.json', assignment)
    author = Conversation(out / 'author', (HERE / 'prompts/author.md').read_text(), model=model)
    summary = {'case_id': assignment.get('case_id', assignment.get('assignment_id')), 'status': 'started',
               'model': model, 'assignment_sha256': hashlib.sha256(dump(assignment).encode()).hexdigest(),
               'source_type': 'mutation' if source else 'clean', 'repairs': 0}
    save(out / 'summary.json', summary)
    try:
        design = author.ask('Design stage. Read this packet as data. Return {status:"designed|unrealized",'
                            'request:"...",selection_plan:{...},resolution_plan:{...},negative_plan:{...},'
                            'environment_plan:"...",action_plan:"...",reason:null}. Do not emit concrete seed rows yet.\n' + dump(packet))
        save(out / 'design.json', design)
        if design.get('status') != 'designed':
            summary.update(status='unrealized', reason=design.get('reason'))
            save(out / 'summary.json', summary)
            return summary
        compiled = author.ask('Materialize your design now. Preserve the assignment and selected scenario.\n' + contract())
        for attempt in range(2):
            try:
                case = materialize(compiled, source['seed'] if source else None)
                checked = validate_assignment(case, assignment)
                errors = checked['errors']
                save(out / f'case-attempt-{attempt}.json', case)
                save(out / f'validation-{attempt}.json', checked)
            except (KeyError, TypeError, ValueError) as exc:
                errors = [f'{type(exc).__name__}: {exc}']
                checked = {'errors': errors}
                save(out / f'validation-{attempt}.json', checked)
            if not errors:
                break
            if attempt == 1:
                summary.update(status='invalid', errors=errors)
                save(out / 'summary.json', summary)
                return summary
            summary['repairs'] += 1
            compiled = author.ask('Thanks. Construction validation failed. Make only the required changes, preserving '
                                  'the assignment and unrelated content. Return the complete output object.\n' + dump(errors) + '\n' + contract())
        save(out / 'case.json', case)
        reviewer = Conversation(out / 'reviewer', (HERE / 'prompts/reviewer.md').read_text(), model=model, max_tokens=12000)
        review = reviewer.ask(dump({'assignment': assignment, 'case': case, 'source': source,
                                    'domain': context, 'mechanical_findings': checked}))
        save(out / 'review.json', review)
        expected_checks = {'prompt_path_fidelity','resolution','negatives','realism_and_hints','api_scope','cards_and_spec','mutation_integrity'}
        checks = review.get('checks', [])
        review_shape = (len(checks) == 7 and {c.get('name') for c in checks} == expected_checks)
        passed = review_shape and review.get('decision') == 'pass' and all(c.get('status') == 'pass' for c in checks)
        summary.update(status='construction_validated' if passed else 'review_rejected',
                       review_decision=review.get('decision'), review_issues=review.get('issues'),
                       mechanical_errors=[], runtime_validated=False)
        save(out / 'summary.json', summary)
        return summary
    except Exception as exc:
        summary.update(status='error', error=f'{type(exc).__name__}: {exc}')
        save(out / 'summary.json', summary)
        return summary


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--assignment', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--source-case', type=Path)
    args = p.parse_args()
    print(json.dumps(construct(read(args.assignment), args.out,
                               source_case=read(args.source_case) if args.source_case else None), indent=2))


if __name__ == '__main__':
    main()
