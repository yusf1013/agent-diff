"""Small deterministic serializer for this manually authored suite; no model calls."""
from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import re

TABLES = ('teams', 'users', 'user_teams', 'channels', 'channel_members', 'messages', 'message_reactions')
EMOJI = {'🚀': 'rocket', '🙌': 'raised_hands', '👀': 'eyes', '🔥': 'fire', '👍': 'thumbsup', '🎉': 'tada'}
ENTITY_NAMES = {'messages': 'Message', 'message_reactions': 'Reaction', 'users': 'User',
                'channels': 'Conversation', 'channel_members': 'Conversation Membership',
                'teams': 'Workspace', 'user_teams': 'Workspace Membership'}
STAMP = '2025-01-01T08:00:00Z'


def key(value):
    return re.sub(r'[^A-Za-z0-9]+', '_', value).strip('_').upper()


class Seed:
    def __init__(self, actor_name='Nina Patel', actor_id='U_ACTOR', team_name='Atlas'):
        self.data = {t: [] for t in TABLES}
        self.messages = {}
        self.actor = actor_id
        self.team = self.workspace(team_name, team_name)
        self.user(actor_id, actor_name, role='admin')

    def workspace(self, identifier, name):
        tid = identifier if identifier.startswith('T_') else 'T_' + key(identifier)
        self.data['teams'].append({'team_id': tid, 'team_name': name, 'created_at': STAMP})
        return tid

    def user(self, identifier, name, team=None, role='member', bot=False):
        uid = identifier if identifier.startswith('U_') else 'U_' + key(identifier)
        self.data['users'].append({'user_id': uid, 'username': uid.lower(),
            'email': uid.lower() + '@atlas.example', 'real_name': name,
            'display_name': name, 'is_bot': bot, 'is_active': True, 'created_at': STAMP})
        self.data['user_teams'].append({'user_id': uid, 'team_id': team or self.team, 'role': role})
        return uid

    def channel(self, identifier, name, topic='', purpose='', private=False, team=None):
        cid = identifier if identifier.startswith('C_') else 'C_' + key(identifier)
        self.data['channels'].append({'channel_id': cid, 'channel_name': name,
            'team_id': team or self.team, 'topic_text': topic, 'purpose_text': purpose,
            'is_private': private, 'is_dm': False, 'is_gc': False,
            'is_archived': False, 'created_at': STAMP})
        self.member(self.actor, cid)
        return cid

    def member(self, uid, cid):
        handle = {'channel_id': cid, 'user_id': uid}
        if not any(all(r[k] == v for k, v in handle.items()) for r in self.data['channel_members']):
            self.data['channel_members'].append({**handle, 'joined_at': STAMP})
        return handle

    def message(self, label, cid, uid, text):
        # M labels survive deletions and remain outside the solver's message text.
        suffix = int(re.search(r'\d+', label).group())
        epoch = 1735808400 + 60 * suffix
        mid = f'{epoch}.000001'
        assert label not in self.messages, label
        self.messages[label] = mid
        self.data['messages'].append({'message_id': mid, 'ts': mid, 'channel_id': cid,
            'user_id': uid, 'message_text': text, 'type': 'message',
            'created_at': datetime.fromtimestamp(epoch, timezone.utc).isoformat()})
        return mid

    def react(self, mid, uid, emoji):
        handle = {'message_id': mid, 'user_id': uid, 'reaction_type': EMOJI.get(emoji, emoji)}
        self.data['message_reactions'].append({**handle, 'created_at': '2025-01-03T12:00:00Z'})
        return handle


def f(node, field, value, op='eq'):
    return {'node': node, 'field': field, 'op': op, 'value': value}


def query(path, joins, filters, count=None):
    value = {'path': path, 'joins': joins, 'filters': filters}
    if count is not None:
        value['count'] = count
    return value


def selector(path, joins, filters, scope=None, auxiliary=None, count=None):
    return {'root_table': path[0], 'scope': scope or [],
            'focal': query(path, joins, filters, count), 'auxiliary': auxiliary or []}


def make_entry(case_id, base_id, mode, seed, request, rows, description, expected,
               negatives, selector, *, candidates=None, selection='one',
               computation=None, written=None, read_only=False, change='',
               operation=None, answers=None, scope=None):
    """Expected handles are supplied by authors, then independently recomputed by checks."""
    root = selector['root_table']
    paths, identifying, partial = [], [], []
    for condition in selector['scope']:
        identifying.append(root + '.' + condition['field'])
        partial.append(f"{root}.{condition['field']} {condition['op']} {condition['value']!r}")
    for q in [selector['focal'], *selector['auxiliary']]:
        p = {'entities': q['path'], 'relationships': q['joins']}
        if p not in paths:
            paths.append(p)
        identifying.extend(q['joins'])
        for condition in q['filters']:
            attr = q['path'][condition['node']] + '.' + condition['field']
            identifying.append(attr)
            partial.append(f"{attr} {condition['op']} {condition['value']!r}")
        if 'count' in q:
            identifying.append('count(' + q['path'][q['count']['node']] + ')')
            # Preserve the known cardinality restriction in unresolved cards too.
            counted = q['path'][q['count']['node']]
            partial.append(f"count({counted} connected by {', '.join(q['joins'])}) {q['count']['op']} {q['count']['value']}")
    referents = deepcopy(expected)
    if mode == 'underspecified':
        referents = {'selection': f'{selection}({root})', 'partial_constraints': partial,
                     'candidate_sets': deepcopy(candidates)}
    card = {'Test ID': case_id, 'Task type': 'read-only' if read_only else 'state-changing',
        'Grounding obligations': 1, 'Grounding obligation name': 'Resolve the requested ' + ENTITY_NAMES[root].lower() + (' set' if selection == 'set' or mode == 'multiple' else ''),
        'Grounding obligation description': description,
        'Resolution': 'resolved' if mode in ('single', 'multiple') else mode,
        'Shared scope': scope or ('All ' + root + ' in the supplied workspace environment.'),
        'Referent set': referents, 'Identifying paths': paths,
        'Alternative sufficient identifying sets': None if mode == 'underspecified' else [list(dict.fromkeys(identifying))]}
    field = 'Answer-computation attributes' if read_only else 'Change-computation attributes'
    card[field] = deepcopy(computation) if computation is not None else [[]]
    if not read_only:
        card['Written attributes'] = written or []
    case = {'case_id': case_id, 'prompt': request, 'acting_user_id': seed.actor,
        'seed': deepcopy(seed.data), 'cards': [card],
        'task_spec': [{'line': 1, 'text': request, 'obligations': [1]}],
        'private': {'mode': mode, 'focal_obligation': 1, 'selector': deepcopy(selector),
            'expected_matches': deepcopy(expected), 'near_misses': deepcopy(negatives),
            'require_near_miss': True, 'candidate_sets': deepcopy(candidates),
            'workflow_version': 2, 'construction_explanation': description,
            'provenance': 'Manual Codex authoring; deterministic serialization, no model generation calls.',
            'base_story': base_id, 'variant_change': change,
            'row_bindings': [{'label': r[0], 'handle': r[3]} for r in rows],
            'reference_outcome': {'operation': operation or {'kind': 'report'},
                'targets': deepcopy(expected) if mode in ('single', 'multiple') else [],
                'response': ('Acknowledge the absence of a complete match.' if mode == 'absent' else
                             'Acknowledge the unresolved alternatives or ask for clarification; do not select one on the user\'s behalf.' if mode == 'underspecified' else
                             'Supply the requested answer.' if read_only else 'Carry out the requested operation on the intended targets.'),
                'state_changes_permitted': not read_only and mode in ('single', 'multiple'),
                'answer_facts': answers or []}}}
    return {'case': case, 'base_id': base_id, 'rows': deepcopy(rows), 'change': change,
            'route': ' → '.join(ENTITY_NAMES[t] for t in selector['focal']['path'])}


def story_section(entry):
    case = entry['case']
    p = case['private']
    header = [f"## {case['case_id']}", '', f"**Route:** {entry['route']}", '',
              f"**Resolution mode:** {p['mode']}", '', f"**Request:** {case['prompt']}", '',
              f"**Change from {entry['base_id']}:** {entry['change']}", '',
              '| Referent | Environment facts | Interpretation |', '|---|---|---|']
    for label, facts, meaning, _ in entry['rows']:
        header.append('| ' + ' | '.join(str(v).replace('|', '\\|') for v in (label, facts, meaning)) + ' |')
    if p['mode'] == 'underspecified':
        header += ['', case['cards'][0]['Grounding obligation description']]
    return '\n'.join(header) + '\n'
