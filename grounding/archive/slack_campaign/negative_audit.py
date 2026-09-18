"""Audit one-condition near misses in the compiled finite queries.

This is diagnostic only: semantic fidelity and API visibility are separate, and
failure to find this kind of witness does not invalidate missing-edge negatives.
"""
import copy,json
from grounding.archive.slack_campaign.generate import read
from grounding.common.bedrock import save
from grounding.generation.selection import evaluate_selector,handle_key
from grounding.archive.slack_campaign.campaign_metrics import BASE,collect

def audit():
    rows=[]
    for row in collect()['cases']:
        if row['construction_status']!='review_pass':continue
        cid=row['case_id'];case=read(BASE/'construction'/cid/'case.json');s=case['private']['selector'];table=s['root_table']
        expected={handle_key(table,x) for x in case['private']['expected_matches']}
        negatives={handle_key(table,x) for x in case['private']['near_misses']};results=[]
        queries=[('scope',s.get('scope',[])),('focal',s['focal'].get('filters',[]))]+[(f'auxiliary/{i}',q.get('filters',[])) for i,q in enumerate(s.get('auxiliary',[]))]
        for location,filters in queries:
            for index,f in enumerate(filters):
                relaxed=copy.deepcopy(s)
                if location=='scope':del relaxed['scope'][index]
                elif location=='focal':del relaxed['focal']['filters'][index]
                else:del relaxed['auxiliary'][int(location.split('/')[1])]['filters'][index]
                try:matches=evaluate_selector(case['seed'],relaxed)['matches']
                except Exception as exc:results.append({'location':location,'filter':f,'error':str(exc)});continue
                admitted=[x for x in matches if handle_key(table,x) not in expected]
                declared=[x for x in admitted if handle_key(table,x) in negatives]
                if admitted:results.append({'location':location,'filter':f,'new_matches':admitted,'declared_negative_matches':declared})
        rows.append({'case_id':cid,'construction_type':row['construction_type'],'one_filter_negative':any(r.get('declared_negative_matches') for r in results),'conditions_with_witnesses':results})
    out={'note':'Lower-bound diagnostic on compiled queries, not a natural-language validity or difficulty certificate. Removing one filter keeps every remaining path/join/filter fixed. Same-condition alternatives, missing-edge negatives and semantic equivalent predicates can escape this diagnostic. No solver labels or outcomes influence it.','summary':{'cases':len(rows),'with_declared_one_filter_negative':sum(x['one_filter_negative'] for x in rows)},'cases':rows}
    save(BASE/'negative_audit.json',out);print(json.dumps(out['summary']))
    return out
if __name__=='__main__':audit()
