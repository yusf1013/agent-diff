"""Mechanical role bindings for an assigned route, using real schema foreign keys.

This supplies the writer with relationship identity, not a test prompt, field
values, intended answers, or a manually authored test scenario.
"""
from .selection import SCHEMA

TABLES={'WORKSPACE':'teams','USER':'users','CONVERSATION':'channels','WORKSPACE_MEMBERSHIP':'user_teams',
        'CONVERSATION_MEMBERSHIP':'channel_members','MESSAGE':'messages','REACTION':'message_reactions'}
ROLES={'messages.user_id':'message author','messages.channel_id':'message location',
       'message_reactions.user_id':'reactor','message_reactions.message_id':'reacted-to message',
       'channel_members.user_id':'channel member','channel_members.channel_id':'membership channel',
       'user_teams.user_id':'workspace member','user_teams.team_id':'membership workspace',
       'channels.team_id':'conversation workspace'}

def build(nodes):
    tables=[TABLES.get(n,n) for n in nodes];joins=[]
    for i,(left,right) in enumerate(zip(tables,tables[1:])):
        choices=[]
        for source,target,a,b in [(left,right,i,i+1),(right,left,i+1,i)]:
            for field,column in SCHEMA[source].columns.items():
                if column.foreign_key and column.foreign_key.split('.')[0]==target:
                    key=source+'.'+field
                    choices.append({'left':f'r{a}.{field}','right':f'r{b}.{column.foreign_key.split(".")[1]}',
                                    'foreign_key':key,'relationship_role':ROLES.get(key,key)})
        if len(choices)!=1:raise ValueError(f'Route edge {left} to {right} needs explicit relationship selection: {choices}')
        joins.append(choices[0])
    return {'requested_referent':'r0','records':[{'variable':f'r{i}','table':table} for i,table in enumerate(tables)],
            'joins':joins,'instruction':'Use these exact relationship roles to identify r0. Pick conditions along these bound records. A relation used only to report an extra answer field is not identifying. Different variables remain distinct unless an additional equality is explicitly requested and represented.'}
