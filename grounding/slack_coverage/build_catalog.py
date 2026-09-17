"""Freeze four linear inventories from the adopted model and exposure audit."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent

ATTRIBUTES={
 'teams':['team_id'],
 'users':['user_id','username','email','real_name','display_name','timezone','title','created_at','is_active','is_bot'],
 'channels':['channel_id','channel_name','topic_text','purpose_text','is_private','is_dm','is_gc','is_archived','created_at'],
 'user_teams':['role'],
 'messages':['message_id','message_text','blocks','created_at'],
 'message_reactions':['reaction_type'],
 'channel_members':[]}
LIMITS=[
 ('workspace_settings','read','Read the stored default conversation'),('workspace_settings','write','Change the stored default conversation'),
 ('user_settings','read','Read notification preference'),('user_settings','write','Change notification preference'),
 ('named_role','read','List defined named roles'),('named_role','write','Create a named role'),
 ('role_assignment','read','Find holders of a named role'),('role_assignment','write','Assign a named role'),
 ('file','read','Read stored file metadata'),('file','write','Rename a stored file'),
 ('file_attachment','read','Read stored file attachments'),('file_attachment','write','Attach an existing stored file; accept a permitted sharing alternative'),
 ('stored_mention','read','Read a stored mention time, when ordinary context distinguishes it from message time'),
 ('edit_history','read','Read prior message content'),('edit_history','write','Remove edit history while preserving the current message'),
 ('workspace_metadata','read','Read stored workspace name'),('workspace_metadata','write','Rename workspace'),
 ('user_login','read','Read last login'),('conversation_membership_time','read','Read join time'),('reaction_time','read','Read reaction time'),
 ('workspace_membership_role','read','Distinguish guest from regular member'),('workspace_membership_role','write','Change workspace admin status'),
 ('user_profile','write','Change a profile attribute'),('conversation_purpose','write','Change conversation purpose'),
 ('conversation_privacy','write','Convert an existing conversation privacy setting')]

def build():
    review=json.loads((HERE/'route_inclusion_review.json').read_text())
    attrs=[{'id':'A:'+t+'.'+f,'table':t,'field':f,
            'qualification': ('Owner/admin predicates only; guest/member differences belong to limitations.' if t=='user_teams' else
              'Message ID is the API ts identity; stored messages.ts is not a second cell.' if (t,f)==('messages','message_id') else
              'Stored creation time is usable through query filters/order; not necessarily a returned field.' if (t,f)==('messages','created_at') else
              'Structured content is one attribute family; nested types do not multiply cells.' if f=='blocks' else
              'Direct supplied identity counts only when requested, not for internal joins.' if f.endswith('_id') else
              'Use the documented observable value; nullable/default representations do not create extra cells.')}
           for t,fs in ATTRIBUTES.items() for f in fs]
    return {'version':'1.0','status':'Operational linear catalog; counts are requirements, not claims of realized tests.',
       'sources':['systematic modeling/slack-conceptual-model.md','systematic modeling/slack-coverage-ledger.md',
                  'grounding/slack_coverage/route_inclusion_review.json','grounding/slack_coverage/capability_limits_audit.md'],
       'discipline':'Take modeled entity attributes/identities exposed by the API once, normalize representation aliases, put unavailable observations/effects in capability limitations, and preserve the reviewed complete-route inventory. Do not multiply dimensions or count join-only foreign keys as independent scalar attributes.',
       'routes':[{'id':r['route_id'],'entities':r['nodes'],'group':r['group_id']} for r in review['routes'] if r['decision']=='retain'],
       'excluded_routes':[r['route_id'] for r in review['routes'] if r['decision']!='retain'],
       'attributes':attrs,
       'resolution_modes':[{'id':'M:'+t+':'+m,'table':t,'mode':m} for t in ATTRIBUTES for m in ('single','multiple','underspecified','absent')],
       'limitations':[{'id':'L:'+g+':'+a,'family':g,'operation':a,'representative':label,'status':'requires faithful realization; never assume empty referents from unavailable access'} for g,a,label in LIMITS],
       'outside_scope':['Repeated-entity routes, including parent/reply and co-member paths, are retained in baseline annotations but outside the adopted 174-route denominator.',
                       'Stored message type and separate timestamp representation are not ordinary exposed distinguishing attributes.',
                       'Stored mention writes are not a limitation test: ordinary textual mentioning is supported.',
                       'Derived collection counts/existence are conditions on relationship routes, not new scalar field cells.',
                       'Optional delegated subsets are recorded separately, not silently mapped to a determined multiple mode.'],
       'counting':'Report each dimension separately. A valid test can cover several requirements, but only actual identifying use earns credit. Assignment, emitted selectors and reviewer acceptance alone are construction claims; final validation and coverage review establish realization.'}

if __name__=='__main__':
    x=build();(HERE/'catalog.json').write_text(json.dumps(x,indent=2)+'\n')
    print({k:len(x[k]) for k in ('routes','attributes','resolution_modes','limitations')})
