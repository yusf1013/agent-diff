"""Seed-reusing writer/compiler/reviewer workflow; model outputs remain claims."""
from __future__ import annotations
import argparse
import copy
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path

from .bedrock import Conversation, save
from .generate import ROOT, HERE, read, dump, domain_context, materialize
from .selection import SELECTOR_GUIDE, evaluate_selector, SCHEMA
from .validate import validate_case

BASE = ROOT / 'examples/slack/seeds/slack_bench_v2.json'
PROMPTS = HERE / 'prompts/v2'
MAPPING = {'WORKSPACE':'teams','USER':'users','CONVERSATION':'channels',
           'WORKSPACE_MEMBERSHIP':'user_teams','CONVERSATION_MEMBERSHIP':'channel_members',
           'MESSAGE':'messages','REACTION':'message_reactions'}

def assignments():
    routes = read(ROOT / 'grounding/slack_coverage/route_inclusion_review.json')['routes']
    modes = ('single','multiple','underspecified','absent')
    counts = {}
    result = []
    for r in routes:
        if r['decision'] != 'retain':
            continue
        root = r['nodes'][0]
        n = counts.get(root, 0)
        counts[root] = n + 1
        result.append({'case_id':'G-'+r['route_id'], 'construction_type':'clean_generation',
                       'route_id':r['route_id'],'route_nodes':r['nodes'],
                       'resolution_mode':modes[n % 4], 'referent_entity':root,
                       'exposure_qualification':r['reason']})
    # Fixed pilot assignments span paths/modes; these are planned before results.
    pilot = {'R083':'multiple','R146':'single','R024':'underspecified',
             'R089':'absent','R073':'multiple','R001':'single'}
    for a in result:
        if a['route_id'] in pilot:
            a['resolution_mode'] = pilot[a['route_id']]
        a['calibration'] = a['route_id'] in pilot
    return result


def source_context():
    context = domain_context()
    context.pop('locked_card_schema')  # writer has a small plan contract, not raw cards
    context['runtime_qualifications'][0] = 'Seven supported referent tables; preserve the supplied base seed.'
    return context


def write_design(folder, assignment):
    folder.mkdir(parents=True, exist_ok=True)
    save(folder/'assignment.json', assignment)
    if (folder/'design.json').exists():
        return read(folder/'design.json')
    agent = Conversation(folder/'writer', (PROMPTS/'writer.md').read_text(), max_tokens=12000)
    packet = {'assignment':assignment, 'domain':source_context(), 'base_seed':read(BASE),
              'acting_user_id':'U01AGENBOT9',
              'instruction':'Write a fresh scenario; do not copy the calibration names or prompts.'}
    if assignment.get('source_context'):
        packet['source_case']=assignment['source_context']
        packet['instruction']='Mutate this existing case by adding plausible path-derived negative examples. Keep the original prompt byte-for-byte, its downstream actions, original intended referents and resolution mode. Use existing cards to preserve source interpretation, including exceptions. Reuse the full base seed; do not add a replacement positive, alter the requested target identity, or reinterpret a condition. Write the same short design contract for the complete mutated case. The primary obligation is the assigned source obligation; preserve other needed references and direct task links.'
    save(folder/'writer_input.json', packet)
    design = agent.ask(dump(packet))
    save(folder/'design.json', design)
    return design


def role_handles(design, bindings, labels):
    output = []
    for label in labels:
        if label not in bindings:
            raise ValueError('Missing role binding '+label)
        output.extend(bindings[label])
    # Two roles can name the same native record; referent sets have no duplicates.
    return list({dump(x):x for x in output}.values())


def assemble(assignment, design, compiled):
    if compiled.get('design_defect'):
        raise ValueError('Design defect: '+compiled['design_defect'])
    case = materialize({'case_id':assignment['case_id'], 'prompt':design['prompt'],
                        'acting_user_id':'U01AGENBOT9','seed_edits':compiled['seed_edits']}, read(BASE))
    cards=[]
    selectors=compiled['selectors']
    if len(selectors)!=len(design['obligations']):
        raise ValueError('One selector required per planned obligation')
    for index, ob in enumerate(design['obligations']):
        selector=selectors[index]
        query=selector['focal']
        refs=role_handles(design,compiled['bindings'],ob['target_roles'])
        mode=ob['mode']
        id_fields=[]
        for q in [query]+selector.get('auxiliary',[]):
            id_fields.extend(q['path'][f['node']]+'.'+f['field'] for f in q.get('filters',[]))
            id_fields.extend(q.get('joins',[]))
            if q.get('count'):
                id_fields.append('count('+q['path'][q['count']['node']]+')')
        card={'Test ID':case['case_id'],'Task type':ob['task_type'],
              'Grounding obligations':len(design['obligations']),
              'Grounding obligation name':ob['name'],
              'Grounding obligation description':ob['description'],
              'Resolution':'resolved' if mode in ('single','multiple') else mode,
              'Shared scope':ob['scope'], 'Referent set':refs,
              'Identifying paths':[{'entities':q['path'],'relationships':q['joins']} for q in [query]+selector.get('auxiliary',[])],
              'Alternative sufficient identifying sets':None if mode=='underspecified' else [list(dict.fromkeys(id_fields))]}
        if mode=='underspecified':
            card['Referent set']={'selection':ob['selection']+'('+ob['table']+')',
                                 'partial_constraints':[q['path'][f['node']]+'.'+f['field']+' '+f['op']+' '+dump(f['value']) for q in [query]+selector.get('auxiliary',[]) for f in q.get('filters',[])],
                                 'candidate_sets':[role_handles(design,compiled['bindings'],s) for s in ob['candidate_role_sets']]}
        if ob['task_type']=='read-only':
            card['Answer-computation attributes']=ob['answer_attributes']
        else:
            card['Change-computation attributes']=ob['change_attributes']
            card['Written attributes']=ob['written_attributes']
        cards.append(card)
    primary=design['obligations'][0]
    main=selectors[0]
    negatives=[r['role'] for r in design['roles'] if r['selection']=='negative' and MAPPING.get(r['entity'],r['entity'])==primary['table']]
    case.update(cards=cards,task_spec=design['task_spec'],private={
        'mode':primary['mode'],'focal_obligation':1,'selector':main,
        'expected_matches':role_handles(design,compiled['bindings'],primary['target_roles']),
        'near_misses':compiled.get('negative_referents',role_handles(design,compiled['bindings'],negatives)),
        'require_near_miss':True,'candidate_sets':cards[0]['Referent set'].get('candidate_sets') if isinstance(cards[0]['Referent set'],dict) else None,
        'construction_explanation':design['binding_note'],
        'mutation_summary':'Base seed plus declared patches; separate writer and compiler',
        'scope_exception':design.get('scope_exception'),'workflow_version':2})
    return case


def check(case, assignment, design, compiled):
    result=validate_case(case)
    errors=result['errors']
    if assignment.get('source_context'):
        source=assignment['source_context']
        if case['prompt'] != source['prompt']:
            errors.append('Environment-only mutation must preserve source prompt byte-for-byte')
        old=source['cards'][assignment.get('source_obligation',1)-1]['Referent set']
        if {dump(x) for x in case['private']['expected_matches']} != {dump(x) for x in old}:
            errors.append('Environment-only mutation must preserve source intended referent set')
    path=[MAPPING[n] for n in assignment['route_nodes']]
    if case['private']['selector']['focal']['path']!=path:
        errors.append('Main identifying path differs from assigned complete route')
    if design['obligations'][0]['mode']!=assignment['resolution_mode']:
        errors.append('Main mode differs from assignment')
    if design['obligations'][0]['table']!=path[0]:
        errors.append('Main referent entity differs from assignment')
    for i,(ob,selector) in enumerate(zip(design['obligations'],compiled['selectors'])):
        if selector['root_table']!=ob['table']:
            errors.append(f'O{i+1}: selector root differs from design')
        try:
            actual=evaluate_selector(case['seed'],selector)['matches']
            expected=role_handles(design,compiled['bindings'],ob['target_roles'])
            if {dump(x) for x in actual}!={dump(x) for x in expected}:
                errors.append(f'O{i+1}: complete selector matches {actual}, but planned bindings are {expected}')
        except Exception as exc:
            errors.append(f'O{i+1}: {exc}')
    return result


def check_design(design, assignment):
    errors=[]
    if design.get('unrealized_reason'):return errors
    roles={r['role']:r for r in design['roles']}
    for i,ob in enumerate(design['obligations'],1):
        for role in ob['target_roles'] + [r for group in (ob.get('candidate_role_sets') or []) for r in group]:
            if role not in roles or MAPPING.get(roles[role]['entity'],roles[role]['entity']) != ob['table']:
                errors.append(f'O{i}: target/candidate role {role} must name only the referent table {ob["table"]}; intermediate records belong in support roles.')
        for field in ob.get('written_attributes',[]):
            parts=field.split('.')
            if len(parts)!=2 or parts[0] not in SCHEMA or parts[1] not in SCHEMA[parts[0]].columns:
                errors.append(f'O{i}: written attribute {field!r} must be a real table.column, with values in prose instead.')
        if 'messages.user_id' in ob.get('written_attributes',[]):
            errors.append(f'O{i}: omit authentication-supplied actor messages.user_id unless the request specifically controls it.')
    if design['obligations'][0]['table'] != MAPPING[assignment['route_nodes'][0]]:
        errors.append('Main obligation referent differs from assignment')
    if design['obligations'][0]['mode'] != assignment['resolution_mode']:
        errors.append('Main obligation mode differs from assignment')
    return errors


def review_design(folder,assignment,design,reviewer):
    for attempt in range(1,4):
        errors=check_design(design,assignment)
        review=reviewer.ask(dump({'stage':'short design review before compilation; concrete rows are not available yet, judge the plan',
            'assignment':assignment,'design':design,'mechanical_design_errors':errors,
            'base_seed':read(BASE) if attempt==1 else 'unchanged',
            'domain':source_context() if attempt==1 else 'unchanged'}))
        save(folder/f'design-review-{attempt}.json',review)
        if not errors and review['validity']=='pass' and not any(i['kind'] in ('validity','access','annotation') for i in review.get('issues',[])):
            save(folder/'design.json',design)
            return design
        if attempt==3:return {'unrealized_reason':{'design_review':review,'errors':errors}}
        writer=Conversation.resume(folder/'writer')
        save(folder/f'design-before-repair-{attempt}.json',design)
        design=writer.ask('Thanks. Review found these defects. Make minimal necessary repairs and return the complete corrected design JSON. Preserve the short prompt unless its selection/route is itself defective. Ensure target_roles and candidate_role_sets contain only referent-entity roles, and represent negative referents in the role table as well as their supporting records.\n'+dump({'errors':errors,'review':review}))
        save(folder/'design.json',design)
    return design


def compile_review(folder, assignment, design):
    if design.get('unrealized_reason'):
        return {'status':'unrealized','reason':design['unrealized_reason']}
    reviewer=Conversation(folder/'reviewer',(PROMPTS/'reviewer.md').read_text(),max_tokens=10000)
    design=review_design(folder,assignment,design,reviewer)
    if design.get('unrealized_reason'):return {'status':'unrealized','reason':design['unrealized_reason']}
    compiler=Conversation(folder/'compiler',(PROMPTS/'compiler.md').read_text(),max_tokens=20000)
    packet={'assignment':assignment,'design':design,'base_seed':read(BASE),
            'domain':source_context(),'selector_syntax':SELECTOR_GUIDE}
    compiled=compiler.ask(dump(packet))
    for attempt in range(1,4):
        save(folder/f'compiled-{attempt}.json',compiled)
        try:
            case=assemble(assignment,design,compiled)
            checks=check(case,assignment,design,compiled)
        except Exception as exc:
            case=None
            checks={'errors':[str(exc)]}
        save(folder/f'checks-{attempt}.json',checks)
        if checks['errors']:
            if attempt<3 and not compiled.get('design_defect'):
                compiled=compiler.ask('Thanks. Validation failed. Make the smallest required fixes, preserving the locked design and prompt. Return the complete corrected compilation JSON.\n'+dump(checks))
                continue
            return {'status':'unrealized','reason':checks['errors']}
        save(folder/f'case-{attempt}.json',case)
        review=reviewer.ask(dump({'assignment':assignment,'design':design,'compiled':compiled,
                                 'case':case,'mechanical_checks':checks,
                                 'api_context':source_context() if attempt==1 else 'unchanged from previous turn'}))
        save(folder/f'review-{attempt}.json',review)
        if review['validity']=='pass' and not any(i['kind'] in ('validity','access','annotation') for i in review.get('issues',[])):
            save(folder/'case.json',case)
            return {'status':'review_pass','quality':review['quality'],'attempts':attempt,
                    'scope_exception':design.get('scope_exception')}
        if attempt<3:
            compiled=compiler.ask('Independent review found these issues. Repair only concrete compilation defects while preserving the locked design. If changing the design is required, return design_defect. Return the complete compilation JSON.\n'+dump(review))
    return {'status':'unrealized','reason':review}


def job(folder,assignment,phase):
    out=folder/'construction'/assignment['case_id']
    try:
        if (out/'summary.json').exists() and read(out/'summary.json').get('status')=='review_pass':
            return read(out/'summary.json')
        design=write_design(out,assignment)
        summary={'status':'design_written'} if phase=='write' else compile_review(out,assignment,design)
    except Exception as exc:
        summary={'status':'error','error':f'{type(exc).__name__}: {exc}'}
    save(out/'summary.json',summary)
    print(assignment['case_id'],summary,flush=True)
    return summary


def main():
    p=argparse.ArgumentParser()
    p.add_argument('phase',choices=['plan','write','construct'])
    p.add_argument('--folder',type=Path,default=ROOT/'experiments/slack_campaign/campaign_02')
    p.add_argument('--ids',nargs='+')
    p.add_argument('--all',action='store_true')
    p.add_argument('--concurrency',type=int,default=6)
    args=p.parse_args()
    if not 1<=args.concurrency<=15:p.error('concurrency must be 1..15')
    planned=assignments()
    save(args.folder/'assignments.json',planned)
    chosen=[a for a in planned if (a['case_id'] in args.ids if args.ids else args.all or a['calibration'])]
    if args.phase=='plan':print(len(planned),'planned;',len(chosen),'selected');return
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures=[pool.submit(job,args.folder,a,args.phase) for a in chosen]
        for future in as_completed(futures):future.result()

if __name__=='__main__':main()
