"""Project campaign artifacts without turning author/reviewer claims into truth.

No reference run labels are read here. Manual confirmations are matched to the
exact reviewed case bytes; revised cases require a new confirmation.
"""
from collections import Counter
import hashlib
from .generate import ROOT,read
from .bedrock import save

BASE=ROOT/'experiments/slack_campaign/campaign_02'

def collect(base=BASE):
    plans=read(base/'assignments.json')+read(base/'mutation_assignments.json')
    manual=read(base/'manual_review.json')['cases']
    rows=[]
    for a in plans:
        cid=a['case_id'];folder=base/'construction'/cid
        source=read(folder/'summary.json') if (folder/'summary.json').exists() else {'status':'pending'}
        case=read(folder/'case.json') if (folder/'case.json').exists() else None
        execution=read(base/'execution'/cid/'summary.json') if (base/'execution'/cid/'summary.json').exists() else {'status':'not_run'}
        audit=manual.get(cid)
        stale=bool(audit and case and audit.get('case_sha256')!=hashlib.sha256((folder/'case.json').read_bytes()).hexdigest())
        if stale:audit=None
        row={'case_id':cid,'construction_type':a['construction_type'],'development_calibration':a.get('calibration',False),
             'assigned_route':a.get('route_id'),'assigned_mode':a['resolution_mode'],
             'construction_status':source['status'],'model_review_quality':source.get('quality'),
             'execution_status':execution['status'],'solver_termination':execution.get('solver_termination'),
             'model_grounding_flags':execution.get('automated_flags',[]),
             'manual_review':audit,'stale_manual_review':stale,
             'prompt':case['prompt'] if case else None,
             'scope_exception':case.get('private',{}).get('scope_exception') if case else None}
        if a.get('source_context'):
            sid=a['source_context']['test_id'];ob=str(a.get('source_obligation',1))
            root=base/'baseline/assessments'/f'{sid}-ordered-1'
            chosen=root.with_name(root.name+'-repair-1') if root.with_name(root.name+'-repair-1').exists() else root
            prior=read(chosen/'assessment.json') if (chosen/'assessment.json').exists() else {}
            row['source_test_id']=sid;row['source_obligation']=ob
            row['original_focal_judgment']=prior.get('obligations',{}).get(ob)
            row['mutant_focal_judgment']=execution.get('obligations',{}).get('1')
            row['candidate_focal_transition']=row['original_focal_judgment']=='demonstrated_correct' and row['mutant_focal_judgment']=='demonstrated_incorrect'
        rows.append(row)
    summaries={}
    for kind in ['clean_generation','mutation']:
        group=[r for r in rows if (r['construction_type']=='clean_generation')==(kind=='clean_generation')]
        summaries[kind]={'planned':len(group),'construction_status':dict(Counter(r['construction_status'] for r in group)),
                        'execution_status':dict(Counter(r['execution_status'] for r in group)),
                        'model_quality':dict(Counter(r['model_review_quality'] for r in group if r['construction_status']=='review_pass')),
                        'model_flagged_runs':[r['case_id'] for r in group if r['model_grounding_flags']],
                        'manual_confirmed_violations':sum(v=='confirmed' for r in group for v in (r['manual_review'] or {}).get('grounding_flags',{}).values()),
                        'manual_confirmed_failing_runs':[r['case_id'] for r in group if 'confirmed' in (r['manual_review'] or {}).get('grounding_flags',{}).values()],
                        'manually_confirmed_assigned_routes':sorted({r['assigned_route'] for r in group if (r['manual_review'] or {}).get('assigned_route_realized') is True}),
                        'manual_rejected_assigned_routes':[r['case_id'] for r in group if (r['manual_review'] or {}).get('assigned_route_realized') is False]}
    output={'note':'Model review/flags are claims; manual confirmations and route credit are separately recorded. Ground-truth baseline labels are not read. Denominators include unsuccessful attempts.','summary':summaries,'cases':rows}
    save(base/'campaign_results.json',output)
    lines=['# Live generation and mutation inventory','',output['note'],'', '| Case | Route | Mode | Construction | Execution | Model flags | Manual route |','|---|---|---|---|---|---|---|']
    for r in rows:
        audit=r['manual_review'] or {};route=audit.get('assigned_route_realized','unreviewed')
        lines.append(f"| [{r['case_id']}](construction/{r['case_id']}) | {r['assigned_route']} | {r['assigned_mode']} | {r['construction_status']} | {r['execution_status']} | {', '.join(r['model_grounding_flags'])} | {route} |")
    (base/'campaign_results.md').write_text('\n'.join(lines)+'\n')
    return output

if __name__=='__main__':
    import json
    print(json.dumps(collect()['summary'],indent=2))
