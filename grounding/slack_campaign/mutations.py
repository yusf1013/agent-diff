"""Fixed compound-reference mutation assignments, without ground-truth labels."""
from concurrent.futures import ThreadPoolExecutor
from .generate import ROOT,read,baseline_context
from .workflow import job
from .bedrock import save

def plan():
    mapping=read(ROOT/'grounding/slack_coverage/baseline_mapping.json')['obligations']
    inverse={'teams':'WORKSPACE','users':'USER','channels':'CONVERSATION','messages':'MESSAGE',
             'user_teams':'WORKSPACE_MEMBERSHIP','channel_members':'CONVERSATION_MEMBERSHIP','message_reactions':'REACTION'}
    output=[]
    for cid in ('slack_66','slack_86','slack_89','slack_90','slack_93','slack_105'):
        ob=next(x for x in mapping if x['test_id']==cid and x['obligation']==1)
        path=max(ob['identifying_paths'],key=lambda p:len(p['entities']))
        a={'case_id':'M-'+cid,'construction_type':'mutation','baseline_test_id':cid,'source_obligation':1,
           'referent_entity':inverse[ob['referent_entity']], 'route_nodes':[inverse[n] for n in path['entities']],
           'resolution_mode':ob['requested_resolution_mode'], 'stage':'path_negative_environment_only',
           'selection_note':'Fixed purposive compound-reference examples; chosen without ground-truth labels. Original incorrect runs remain in attempted accounting but cannot establish correct-to-incorrect transitions.'}
        a['source_context']=baseline_context(a)
        output.append(a)
    return output

if __name__=='__main__':
    folder=ROOT/'experiments/slack_campaign/campaign_02';items=plan()
    save(folder/'mutation_assignments.json',items)
    with ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(lambda a:job(folder,a,'construct'),items))
