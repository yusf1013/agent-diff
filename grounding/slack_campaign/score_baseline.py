"""G1 summaries and G4 reference comparison; GT is read only in score_g4."""
from collections import Counter
import hashlib
from pathlib import Path
from .generate import ROOT,read
from .bedrock import save

BASE=ROOT/'experiments/slack_campaign/campaign_02/baseline'

def g1():
    cases=read(ROOT/'grounding/slack_analysis/analysis.json')
    obs=[o for c in cases for o in c['obligations']]
    coverage=Counter(o['assertion_coverage'] for o in obs)
    resolution=Counter(o['card']['Resolution'] for o in obs)
    mapping=read(ROOT/'grounding/slack_coverage/baseline_mapping.json')
    modecells=sorted({o['referent_entity']+':'+o['requested_resolution_mode'] for o in mapping['obligations'] if o['requested_resolution_mode']})
    result={'tasks':len(cases),'tasks_with_obligations':sum(bool(c['obligations']) for c in cases),
            'obligations':len(obs),'native_assertion_coverage':dict(coverage),'card_resolutions':dict(resolution),
            'route_coverage':{'covered':len(mapping['summary']['retained_complete_route_ids']),'total':174},
            'mode_coverage':{'covered':len(modecells),'total':28,'cells':modecells},
            'mode_distribution':mapping['summary']['requested_resolution_modes'],
            'provenance':'Manual source/card annotations; counts mechanically aggregated. No solver labels used.'}
    catalog=read(ROOT/'grounding/slack_coverage/catalog.json')
    fields={x['table']+'.'+x['field'] for x in catalog['attributes']}
    observed=set(mapping['summary']['identifying_attributes'])
    result['attribute_coverage']={'covered':len(fields & observed),'total':len(fields),
                                  'fields':sorted(fields & observed),'outside_scalar_inventory':sorted(observed-fields)}
    result['capability_coverage']={'covered':0,'total':len(catalog['limitations']),
       'qualification':'No baseline task was annotated as an isolated representative unavailable-capability probe. Incidental unavailable fields (e.g. workspace name in an admin query) are recorded but receive no automatic boundary-test credit.'}
    save(BASE.parent/'g1.json',result)
    return result

def final_assessment(cid):
    original=BASE/'assessments'/(cid+'-ordered-1')
    repair=original.with_name(original.name+'-repair-1')
    chosen=repair if (repair/'summary.json').exists() else original
    if not (chosen/'assessment.json').exists():return chosen,None
    return chosen,read(chosen/'assessment.json')

def detection(truth,prediction):
    tp=sum(a and b for a,b in zip(truth,prediction));fp=sum(not a and b for a,b in zip(truth,prediction))
    fn=sum(a and not b for a,b in zip(truth,prediction));tn=sum(not a and not b for a,b in zip(truth,prediction))
    ratio=lambda a,b:a/b if b else None
    return {'n':len(truth),'tp':tp,'fp':fp,'fn':fn,'tn':tn,
            'accuracy':ratio(tp+tn,len(truth)),'precision':ratio(tp,tp+fp),'recall':ratio(tp,tp+fn),'f1':ratio(2*tp,2*tp+fp+fn)}

def score_g4():
    judgments=[];mechanical=[];missing=[];run_truth=[];run_pred=[];direct_truth=[];direct_pred=[];direct_rows=[]
    for item in read(ROOT/'grounding/slack_ground_truth/manifest.json')['cases']:
        cid=item['test_id'];gt=read(ROOT/'grounding/slack_ground_truth'/item['report'])
        chosen,pred=final_assessment(cid)
        if pred is None:missing.append(cid);continue
        if pred['run_id']!=gt['run_id']:raise ValueError('Run mismatch '+cid)
        old=read(ROOT/'grounding/slack_ground_truth/inputs'/cid/'cards.json')
        cur=read(BASE/'inputs'/cid/'cards.json')
        for a,b in zip(old,cur):
            a.pop('Identifying paths',None);b.pop('Identifying paths',None)
        if old!=cur:raise ValueError('Card semantic mismatch '+cid)
        if len(gt['obligations'])!=len(pred['obligations']):raise ValueError('Obligation inventory mismatch '+cid)
        meta=read(chosen/'summary.json');mechanical.append(not meta.get('validation_errors') and meta.get('status')=='returned')
        for k,v in gt['obligations'].items():
            judgments.append({'test_id':cid,'obligation':k,'truth':v,'prediction':pred['obligations'][k],
                              'prediction_file':str(chosen.relative_to(ROOT)/'assessment.json')})
        any_truth='demonstrated_incorrect' in gt['obligations'].values();run_truth.append(any_truth)
        run_pred.append('demonstrated_incorrect' in pred['obligations'].values())
        direct=BASE/'direct'/cid/'result.json'
        if direct.exists():
            d=read(direct)
            if d['run_id']!=gt['run_id']:raise ValueError('Direct judge run mismatch')
            direct_truth.append(any_truth);direct_pred.append(bool(d['violations']))
            direct_rows.append({'test_id':cid,'truth_failing_run':any_truth,'predicted_failing_run':bool(d['violations']),
                                'reported_violations':len(d['violations']),'unresolved':len(d['unresolved'])})
    result={'comparison':'One fresh assessment per all baseline cases; no semantic retries. Ground truth used here only.',
            'reports':len(mechanical),'missing':missing,'mechanically_valid':sum(mechanical),
            'obligation_detection':detection([x['truth']=='demonstrated_incorrect' for x in judgments],[x['prediction']=='demonstrated_incorrect' for x in judgments]),
            'exact_three_way_accuracy':sum(x['truth']==x['prediction'] for x in judgments)/len(judgments),
            'three_way_confusion':dict(Counter(str(x['truth'])+' -> '+str(x['prediction']) for x in judgments)),
            'evaluator_run_detection':detection(run_truth,run_pred),
            'direct_judge_run_detection':detection(direct_truth,direct_pred),
            'direct_judge_note':'Run-level detection does not establish localized failure precision; independent manual matching is reported separately.',
            'unresolved_obligation_predictions':sum(x['prediction'] in (None,'not_established') for x in judgments)}
    save(BASE.parent/'g4.json',result);save(BASE.parent/'g4_judgments.json',judgments);save(BASE.parent/'g4_direct_runs.json',direct_rows)
    return result

if __name__=='__main__':
    import json
    print(json.dumps({'G1':g1(),'G4':score_g4()},indent=2))
