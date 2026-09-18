"""Fresh-world compilation of a saved Markdown sketch; fixed checks, bounded repairs."""
from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import re

from .bedrock import Conversation, save
from .generate import ROOT, TABLES, read, dump
from .route_contract import build as route_contract
from .selection import SCHEMA, SELECTOR_GUIDE, canonical_handle, handle_key, evaluate_selector
from .validate import validate_case
from .usage import report

PROMPTS = Path(__file__).parent / 'prompts/v4'
ACTOR = 'U01AGENBOT9'
MAX_OUTPUT_TOKENS = 24_000  # Compiler and construction reviewer, including thinking.


def parse_sketch(text):
    """Extract final prose without using the author's self-audit as evidence."""
    headings = list(re.finditer(r'(?im)^.*\bfinal sketch\b.*$', text))
    final = text[headings[-1].end():].strip() if headings else text.strip()
    def field(label):
        match = re.search(r'(?im)^\*{0,2}' + label + r':\*{0,2}\s*(.+)$', final)
        if not match:
            raise ValueError('Missing final-sketch field: ' + label)
        value = match[1].strip()
        if len(value) > 1 and (value[0], value[-1]) in [('"', '"'), ('“', '”')]:
            value = value[1:-1]
        return value
    rows = []
    for line in final.splitlines():
        if not line.strip().startswith('|'):
            continue
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if len(cells) != 3:
            raise ValueError('Expected exactly three story-table columns')
        if cells[0].lower() == 'referent' or all(re.fullmatch(r'[:\- ]+', c) for c in cells):
            continue
        interpretation = cells[2]
        role = ('match' if interpretation.lower().startswith('match') else
                'alternative' if interpretation.lower().startswith('alternative') else 'negative')
        rows.append({'row': len(rows)+1, 'referent': cells[0], 'facts': cells[1],
                     'interpretation': interpretation, 'role': role})
    if not rows:
        raise ValueError('No final story rows')
    return {'request': field(r'(?:Exact user request|Request)'),
            'selection_conditions': field('Selection conditions'), 'rows': rows, 'final_sketch': final}


def system_prompt(review=False):
    schema = {table: {'primary_key': list(SCHEMA[table].primary_key),
                      'columns': {k: asdict(v) for k, v in SCHEMA[table].columns.items()}}
              for table in TABLES}
    docs = read(ROOT / 'examples/slack/testsuites/slack_docs/slack_api_full_docs.json')
    # Native API signatures, without repeated curl examples; no API implementation.
    signatures = {name: {k: v for k, v in doc.items() if k != 'example_request'}
                  for name, doc in docs.items()}
    return '\n\n'.join([(PROMPTS / ('compiler_review.md' if review else 'compiler.md')).read_text(),
                         (PROMPTS / 'compiler_domain.md').read_text(),
                         '# Native schema\n' + dump(schema),
                         '# Documented API definitions\n' + dump(signatures),
                         '# Restricted selector syntax\n' + SELECTOR_GUIDE])


def mode_instructions(assignment):
    """Dispatch on fixed metadata, outside the shared cached system prefix."""
    mode = assignment['resolution_mode']
    if mode not in ('single', 'multiple', 'absent', 'underspecified'):
        raise ValueError('Unknown assigned resolution mode: ' + str(mode))
    return (PROMPTS/'compiler_modes'/f'{mode}.md').read_text().format_map(assignment).strip()


def compiler_message(packet):
    return mode_instructions(packet['assignment']) + '\n\n' + dump(packet)


def reviewer_message(packet, compiled, case, checks):
    return mode_instructions(packet['assignment']) + '\n\n' + dump(
        {'source':packet,'compilation':compiled,'case':case,'mechanical_checks':checks})


def packet_for(source, case_id):
    assignment = next(a for a in read(source/'assignments.json') if a['case_id'] == case_id)
    path = source/case_id/'writer/turn-02/output.md'
    text = path.read_text()
    sketch = parse_sketch(text)
    roles = [row['role'] for row in sketch['rows']]
    count = assignment['match_count']
    if count is not None and roles.count('match') != count:
        raise ValueError('Story match rows disagree with assigned count')
    if assignment['resolution_mode'] == 'underspecified' and roles.count('alternative') != assignment['alternative_count']:
        raise ValueError('Pilot expects one row per singleton alternative')
    return {'assignment': assignment, 'sketch': sketch, 'acting_user_id': ACTOR,
            'native_route': route_contract(assignment['route_nodes']),
            'operation_menu': read(PROMPTS/'root_operations.json')[assignment['referent_entity']],
            'source': str(path.relative_to(ROOT)), 'source_sha256': hashlib.sha256(text.encode()).hexdigest()}


def check_compilation(packet, compiled, locked_selector=None):
    """Checks do not trust model-supplied match labels or execute generated code."""
    errors = []
    try:
        if not isinstance(compiled, dict):
            raise ValueError('Compilation must be an object')
        if 'design_defect' in compiled:
            return None, {'errors': ['Design conflict: '+str(compiled['design_defect'])], 'design_defect': True}
        if set(compiled) != {'seed','row_bindings','selector','annotation'}:
            raise ValueError('Expected exactly seed, row_bindings, selector, annotation')
        seed, selector, annotation = compiled['seed'], compiled['selector'], compiled['annotation']
        if set(seed) != set(TABLES):
            raise ValueError('Fresh seed must contain exactly the seven domain tables')
        if locked_selector is not None and selector != locked_selector:
            raise ValueError('Selector changed after it was locked; report a conflict instead')
        expected_path = [r['table'] for r in packet['native_route']['records']]
        expected_joins = [r['foreign_key'] for r in packet['native_route']['joins']]
        if (selector['root_table'] != expected_path[0]
            or selector['focal']['path'][:len(expected_path)] != expected_path
            or selector['focal']['joins'][:len(expected_joins)] != expected_joins):
            raise ValueError('Selector must preserve the assigned full route and relationships')
        table = selector['root_table']
        all_handles = {t: {handle_key(t,canonical_handle(t,r)) for r in rows} for t,rows in seed.items()}
        bindings = compiled['row_bindings']
        if [b['row'] for b in bindings] != [r['row'] for r in packet['sketch']['rows']]:
            raise ValueError('Bind every story row exactly once, in order')
        targets, negatives, alternatives, seen = [], [], [], set()
        for binding, story in zip(bindings, packet['sketch']['rows']):
            if set(binding) != {'row','referent','support'}:
                raise ValueError('A binding requires exactly row, referent, support')
            handle = binding['referent']
            if handle is None:
                if story['role'] != 'negative' or not binding['support']:
                    raise ValueError('Null roots require a negative missing-root chain with concrete support')
                if any(s.get('table') == table for s in binding['support']):
                    raise ValueError(f'Row {story["row"]}: null referent contradicts a root listed in support')
            else:
                key = handle_key(table, handle)
                if key not in all_handles[table]:
                    raise ValueError(f'Row {story["row"]}: referent is not a seeded root')
                if key in seen:
                    raise ValueError('Different story root rows cannot bind the same root')
                seen.add(key)
                if story['role'] in ('match','alternative'):
                    targets.append(handle)
                    if story['role'] == 'alternative': alternatives.append([handle])
                else: negatives.append(handle)
            for support in binding['support']:
                if set(support) != {'table','handle'} or support['table'] not in all_handles:
                    raise ValueError('Support requires a real table and native handle')
                if handle_key(support['table'],support['handle']) not in all_handles[support['table']]:
                    raise ValueError('Support record does not exist')
        if set(annotation) != {'name','scope','task_type','computation_attributes','written_attributes'}:
            raise ValueError('Annotation fields differ from the compiler contract')
        if annotation['task_type'] == 'read-only' and annotation['written_attributes']:
            raise ValueError('Read-only annotation cannot declare writes')
        # No free-form expressions in this small native annotation interface.
        for group in annotation['computation_attributes']:
            for attribute in group:
                t,c = attribute.split('.')
                if c not in SCHEMA[t].columns: raise ValueError('Unknown computation field '+attribute)
        for attribute in annotation['written_attributes']:
            t,c = attribute.split('.')
            if c not in SCHEMA[t].columns: raise ValueError('Unknown written field '+attribute)
        assignment = packet['assignment']; mode = assignment['resolution_mode']
        queries = [selector['focal'], *selector['auxiliary']]
        identifying = [table+'.'+f['field'] for f in selector['scope']]
        paths = []
        for query in queries:
            identifying += [query['path'][f['node']]+'.'+f['field'] for f in query['filters']]
            identifying += query['joins']
            if query.get('count'): identifying.append('count('+query['path'][query['count']['node']]+')')
            path = {'entities':query['path'], 'relationships':query['joins']}
            if path not in paths: paths.append(path)
        card = {'Test ID':assignment['case_id'], 'Task type':annotation['task_type'],
                'Grounding obligations':1,'Grounding obligation name':annotation['name'],
                'Grounding obligation description':packet['sketch']['selection_conditions'],
                'Resolution':'resolved' if mode in ('single','multiple') else mode,
                'Shared scope':annotation['scope'], 'Referent set':targets,
                'Identifying paths':paths, 'Alternative sufficient identifying sets':[list(dict.fromkeys(identifying))]}
        if mode == 'underspecified':
            card['Referent set']={'selection':f'one({table})','candidate_sets':alternatives,
                'partial_constraints':[q['path'][f['node']]+'.'+f['field']+' '+f['op']+' '+dump(f['value']) for q in queries for f in q['filters']]}
            card['Alternative sufficient identifying sets']=None
        attr = 'Answer-computation attributes' if annotation['task_type']=='read-only' else 'Change-computation attributes'
        card[attr] = annotation['computation_attributes']
        if annotation['task_type']=='state-changing': card['Written attributes']=annotation['written_attributes']
        case={'case_id':assignment['case_id'], 'prompt':packet['sketch']['request'],
              'acting_user_id':packet['acting_user_id'],'seed':seed, 'cards':[card],
              'task_spec':[{'line':1,'text':packet['sketch']['request'],'obligations':[1]}],
              'private':{'mode':mode,'focal_obligation':1,'selector':selector,'expected_matches':targets,
                         'near_misses':negatives,'require_near_miss':True,'candidate_sets':alternatives or None,
                         'workflow_version':2,'construction_explanation':packet['sketch']['selection_conditions'],
                         'mutation_summary':'Fresh environment; Markdown story compiled without inherited seed.'}}
        checks=validate_case(case)
        count=assignment['match_count']
        if count is not None and len(checks['computed_matches']) != count:
            checks['errors'].append(f'Assigned count is {count}; actual count is {len(checks["computed_matches"])}')
        return case, checks
    except (ValueError, TypeError, KeyError, IndexError, AttributeError) as exc:
        errors.append(str(exc))
        return None, {'errors':errors}


def selector_is_valid(selector, seed):
    # Syntax/real-field validity only, not agreement with expected referents.
    # Empty populations still cause query validation before evaluation.
    try:
        evaluate_selector({table:[] for table in TABLES}, selector)
        return True
    except (ValueError, TypeError, KeyError, IndexError):
        return False


def run(source, case_id, out, *, max_attempts=3):
    out.mkdir(parents=True, exist_ok=False)
    packet=packet_for(source,case_id); save(out/'input.json',packet)
    (out/'story.md').write_text(packet['sketch']['final_sketch']+'\n')
    compiler=Conversation(out/'compiler', system_prompt(), cache_system=True, max_tokens=MAX_OUTPUT_TOKENS)
    message=compiler_message(packet); locked=None; reviewers=0
    result={'status':'running'}
    try:
        for attempt in range(1,max_attempts+1):
            try:
                compiled=compiler.ask(message)
            except RuntimeError:
                summary=read(out/'compiler'/f'turn-{attempt:02d}'/'summary.json')
                if not summary.get('parse_error') or attempt==max_attempts: raise
                message='Thanks. Validation failed: return one complete JSON object in the required format. Preserve the original story and conditions.'
                continue
            save(out/f'compiled-{attempt}.json',compiled)
            if isinstance(compiled,dict) and locked is None and selector_is_valid(compiled.get('selector'),compiled.get('seed')):
                locked=compiled['selector']; save(out/'locked_selector.json',locked)
            case,checks=check_compilation(packet,compiled,locked)
            save(out/f'checks-{attempt}.json',checks)
            if checks.get('design_defect'):
                result={'status':'design_conflict','attempts':attempt,'errors':checks['errors']}; return result
            if checks['errors']:
                result={'status':'mechanical_failure','attempts':attempt,'errors':checks['errors']}
                message='Thanks. Validation failed: '+dump(checks['errors'])+'. Please fix only the concrete compilation errors. Preserve the story and locked selector; otherwise report design_defect. Return the complete JSON.'
                continue
            save(out/f'case-{attempt}.json',case)
            reviewer=Conversation(out/'reviews'/f'attempt-{attempt}'/'reviewer',system_prompt(True),cache_system=True,max_tokens=MAX_OUTPUT_TOKENS)
            reviewers+=1
            review=reviewer.ask(reviewer_message(packet,compiled,case,checks))
            save(out/f'review-{attempt}.json',review)
            valid=(isinstance(review,dict) and review.get('validity') in ('pass','fail','unresolved')
                   and review.get('quality') in ('strong','adequate','weak') and isinstance(review.get('issues'),list)
                   and all(isinstance(i,dict) and i.get('kind') in ('validity','quality') and i.get('origin') in ('design','compilation','selector') for i in review['issues']))
            if not valid:
                result={'status':'review_unresolved','attempts':attempt,'reason':'Malformed review; no acceptance inferred'}; return result
            issues=[i for i in review['issues'] if i['kind']=='validity']
            if review['validity']=='pass' and not issues:
                save(out/'case.json',case)
                result={'status':'review_pass','attempts':attempt,'quality':review['quality'],
                        'computed_matches':checks['computed_matches'],'reviewer_calls':reviewers}; return result
            result={'status':'review_unresolved','attempts':attempt,'review':review}
            if not issues or any(i['origin']!='compilation' for i in issues): return result
            message='Thanks. Review identified concrete instantiation errors: '+dump(issues)+'. Make minimal repairs, preserving all story facts and the locked selector. Return the complete JSON or design_defect.'
        return result
    except Exception as exc:
        result={'status':'error','error':f'{type(exc).__name__}: {exc}'}
        raise
    finally:
        save(out/'summary.json',result)
        report(out)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,default=ROOT/'experiments/slack_campaign/writer_pilot_04')
    parser.add_argument('--case',required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--run',action='store_true')
    args=parser.parse_args()
    if args.run:
        result=run(args.source,args.case,args.out)
        print(dump(result))
        raise SystemExit(result['status']!='review_pass')
    packet=packet_for(args.source,args.case)
    args.out.mkdir(parents=True,exist_ok=False)
    save(args.out/'input.json',packet)
    (args.out/'compiler_instructions.md').write_text(system_prompt())
    (args.out/'compiler_input.md').write_text(compiler_message(packet)+'\n')


if __name__=='__main__':main()
