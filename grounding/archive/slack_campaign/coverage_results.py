"""Conservative linear coverage projection from version-matched manual case audits.

No prefix/subpath credit, no join-only identifying-attribute credit, no baseline
run labels. Requested-design and API-qualified execution are separate measures.
"""
import json
from grounding.archive.slack_campaign.generate import ROOT,read
from grounding.common.bedrock import save
from grounding.archive.slack_campaign.campaign_metrics import collect,BASE

VALID={'accepted','accepted_shorter_route','accepted_different_route','accepted_as_shorter_route','accepted_as_different_route','accepted_reference_design'}
def build():
    data=collect();cat=read(ROOT/'grounding/domains/slack/coverage/catalog.json');g1=read(BASE/'g1.json')
    attrset={a['table']+'.'+a['field'] for a in cat['attributes']}
    routebase={'R009','R010','R017','R061','R068','R072','R093','R127','R128','R134','R139','R140'}
    results={}
    for stage in ['requested_design','api_qualified_executed']:
        routes={};attrs={};modes={};cases=[]
        for row in data['cases']:
            if row['construction_type']!='clean_generation' or row['construction_status']!='review_pass' or row.get('outcome_informed_revision'):continue
            audit=row['manual_review'] or {}
            if audit.get('validity') not in VALID:continue
            cid=row['case_id'];folder=BASE/'execution'/cid
            if stage=='api_qualified_executed' and (row['execution_status'] not in ('completed','evaluation_unresolved') or not (folder/'accepted_access.json').exists()):continue
            case=read(BASE/'construction'/cid/'case.json');cases.append(cid)
            if audit.get('assigned_route_realized') is True:routes.setdefault(row['assigned_route'],[]).append(cid)
            # Mode refers to the task's primary referent, including valid shorter routes.
            selector=case['private']['selector'];mode=selector['root_table']+':'+case['private']['mode'];modes.setdefault(mode,[]).append(cid)
            for q in [selector['focal']]+selector.get('auxiliary',[]):
                filters=[(q['path'][f['node']],f) for f in q.get('filters',[])]
                if q is selector['focal']:filters += [(selector['root_table'],f) for f in selector.get('scope',[])]
                for table,f in filters:
                    field=table+'.'+f['field']
                    if field not in attrset:continue
                    if f['field'] in ('user_id','team_id','channel_id','message_id'):
                        values=f['value'] if isinstance(f['value'],list) else [f['value']]
                        if not any(isinstance(v,str) and v in case['prompt'] for v in values):continue
                    attrs.setdefault(field,[]).append(cid)
        result={'eligible_cases':cases,'routes':routes,'attributes':attrs,'modes':modes,
                'coverage':{'routes':len(routes),'attributes':len(attrs),'modes':len(modes),'capability_limitations':0},
                'with_baseline':{'routes':len(routebase|set(routes)), 'attributes':len(set(g1['attribute_coverage']['fields'])|set(attrs)), 'modes':len(set(g1['mode_coverage']['cells'])|set(modes)), 'capability_limitations':0}}
        results[stage]=result
    results['denominators']={'routes':len(cat['routes']),'attributes':len(cat['attributes']),'modes':len(cat['resolution_modes']),'capability_limitations':len(cat['limitations'])}
    results['notes']=['Coverage is a conservative manually audited lower bound. A valid task on a shorter route does not earn its originally assigned longer route.', 'Only the primary query is projected for generated attributes/modes. Literal internal IDs earn no direct-identity credit unless present in the prompt.', 'Requested design and API-qualified completed solver execution are distinct. An unresolved evaluator serialization still has an executed solver, but is not a complete automated assessment.', 'No dedicated unavailable-capability generation was completed; incidental unsupported asks and manual API probes receive no automatic capability credit.', 'No Cartesian products or prefix route credit are introduced. Baseline run ground-truth labels are not read.']
    save(BASE/'coverage_results.json',results)
    print(json.dumps({k:v.get('coverage',v) if isinstance(v,dict) else v for k,v in results.items() if k!='notes'},indent=2))
    return results
if __name__=='__main__':build()
