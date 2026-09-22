"""Manual variants that move consequential ambiguity along W08–W10's routes.

Existing family builders supply unchanged records. Every candidate set below is
authored explicitly, independently of the executable selector.
"""

from copy import deepcopy

from suite_support import Seed, f, make_entry
from suite_w07_w10 import w08, w09, w10, workspace_membership


def seed_from(entry):
    seed = Seed()
    seed.data = deepcopy(entry['case']['seed'])
    seed.actor = entry['case']['acting_user_id']
    seed.team = seed.data['teams'][0]['team_id']
    return seed


def finish(base, case_id, seed, request, rows, description, expected, candidates,
           selection, change, location, choices, *, selector=None,
           operation=None, answers=None):
    """Serialize a manually specified ambiguity without extending the card schema."""
    original = base['case']
    card = original['cards'][0]
    read_only = card['Task type'] == 'read-only'
    computation_key = 'Answer-computation attributes' if read_only else 'Change-computation attributes'
    result = make_entry(
        case_id, base['base_id'], 'underspecified', seed, request, rows,
        description, expected, [row[3] for row in rows if row[3] not in expected],
        deepcopy(selector or original['private']['selector']),
        candidates=candidates, selection=selection,
        computation=card[computation_key], written=card.get('Written attributes', []),
        read_only=read_only, change=change,
        operation=operation or original['private']['reference_outcome']['operation'],
        answers=answers or original['private']['reference_outcome']['answer_facts'],
    )
    result['route'] = base['route']
    result['ambiguity'] = {'location': location, 'explanation': description,
                           'choices': choices}
    result['case']['private']['ambiguity'] = deepcopy(result['ambiguity'])
    return result


def w08_reaction():
    base = w08('single')
    seed = seed_from(base)
    rows = deepcopy(base['rows'])
    fire, eyes = rows[0][3], rows[1][3]
    rows[0] = (rows[0][0], rows[0][1] + ' Nina reacted 🔥 to M1.',
               'Alternative: remove Nina’s 🔥 reaction', fire)
    rows[1] = (rows[1][0], rows[1][1],
               'Alternative: remove Nina’s 👀 reaction', eyes)
    selector = deepcopy(base['case']['private']['selector'])
    selector['focal']['filters'] = [condition for condition in selector['focal']['filters']
                                  if condition['field'] != 'reaction_type']
    return finish(
        base, 'W08-underspecified-reaction', seed,
        'Remove my reaction from the message written by a member of the channel about launch readiness.',
        rows,
        'Kevin, #product-launch, and M1 are established. Nina has two different reactions on M1, 🔥 and 👀; '
        'the singular “my reaction” does not distinguish which reaction record to remove. '
        'The two singleton reaction sets are alternatives, not a request to remove both.',
        [fire, eyes], [[fire], [eyes]], 'one',
        'Keep the original W08 environment and delete only 🔥 from the request. '
        'The unresolved choice is the target reaction, while the message, author and channel stay fixed.',
        'Reaction (target)', {'Nina’s 🔥 on M1': [fire], 'Nina’s 👀 on M1': [eyes]},
        selector=selector, operation={'kind': 'remove_reaction', 'user_id': seed.actor},
    )


def w08_channel():
    base = w08('single')
    seed = seed_from(base)
    for channel in seed.data['channels']:
        if channel['channel_id'] == 'C_DESIGN':
            channel['topic_text'] = 'Launch readiness for visual assets'
    rows = deepcopy(base['rows'])
    first, second = rows[0][3], rows[3][3]
    rows[0] = (rows[0][0], rows[0][1] + ' Nina reacted 🔥 to M1.',
               'Alternative through #product-launch', first)
    rows[3] = (rows[3][0],
               'Priya wrote M2 in #general. She belongs to #general and #design-crew, whose topic is '
               '“Launch readiness for visual assets”; she does not belong to #product-launch. Nina reacted 🔥 to M2.',
               'Alternative through #design-crew', second)
    return finish(
        base, 'W08-underspecified-channel', seed, base['case']['prompt'], rows,
        'Both #product-launch and #design-crew are about launch readiness. Selecting #product-launch '
        'yields Nina’s 🔥 reaction on Kevin’s M1; selecting #design-crew yields Nina’s 🔥 reaction '
        'on Priya’s M2. Each channel interpretation yields exactly one qualifying message and actor-owned 🔥 reaction. '
        'The request does not select a channel or authorize removing both alternatives.',
        [first, second], [[first], [second]], 'one',
        'Keep the request and records; change #design-crew’s topic from visual-design reviews to '
        '“Launch readiness for visual assets”. Its existing Priya-authored M2 becomes the alternative '
        'to Kevin’s M1 through a different qualifying channel.',
        'Conversation (author’s membership channel)',
        {'#product-launch': [first], '#design-crew': [second]},
    )


def w09_channel():
    base = w09('multiple')
    seed = seed_from(base)
    for channel in seed.data['channels']:
        if channel['channel_id'] == 'C_INCIDENT':
            channel['channel_name'] = 'incident-triage'
            channel['topic_text'] = 'Incident response: triage and coordination'
    bridge = seed.channel('INCIDENT_BRIDGE', 'incident-bridge',
                          'Incident response: live coordination and recovery')
    seed.data['channel_members'] = [row for row in seed.data['channel_members']
                                   if not (row['user_id'] == 'U_SIGNAL' and row['channel_id'] == 'C_INCIDENT')]
    seed.member('U_SIGNAL', bridge)
    seed.message('M3', bridge, seed.actor, 'The operational handover starts at 5pm.')
    rows = [
        ('Atlas, through WatcherBot',
         'WatcherBot is a bot whose profile displays its sole Atlas workspace association. '
         'It belongs to #project-launch and #incident-triage, not #incident-bridge. '
         '#incident-triage’s topic is “Incident response: triage and coordination”. '
         'WatcherBot is the only bot in that channel.',
         'Alternative through #incident-triage', 'T_ATLAS'),
        ('Nimbus, through Dana Reyes',
         'Dana is a human user, marked as not a bot. Her profile displays its sole Nimbus workspace '
         'association. She belongs to #incident-triage. Nimbus has no bot users.',
         'Wrong user classification only', 'T_NIMBUS'),
        ('Orion, through SignalBot',
         'SignalBot is a bot whose profile displays its sole Orion workspace association. '
         'It belongs to #incident-bridge, not #incident-triage. '
         '#incident-bridge’s topic is “Incident response: live coordination and recovery”. '
         'SignalBot is the only bot in that channel.',
         'Alternative through #incident-bridge', 'T_ORION'),
    ]
    selector = deepcopy(base['case']['private']['selector'])
    selector['focal']['filters'] = [f(2, 'is_bot', True),
                                    f(4, 'topic_text', 'Incident response:', op='contains_ci')]
    return finish(
        base, 'W09-underspecified-channel', seed,
        'What workspace is shown on the profile of the bot in the incident-response channel?',
        rows,
        'The descriptive incident-response channel reference fits #incident-triage and #incident-bridge. '
        'Each contains exactly one bot; their profiles display different sole workspace associations: '
        'WatcherBot shows Atlas’s ID and SignalBot shows Orion’s ID. The alternatives are the two '
        'singleton workspace sets, not uncertainty about either bot’s profile. Workspace names in '
        'the story are labels; the supported profile answer is the actual workspace ID.',
        ['T_ATLAS', 'T_ORION'], [['T_ATLAS'], ['T_ORION']], 'one',
        'Replace exact #incident-response with the descriptive “the incident-response channel”. '
        'Rename that channel to #incident-triage and add #incident-bridge, with both topics explicitly '
        'about incident response. Keep WatcherBot in the first and place SignalBot only in the second; '
        'every profile retains exactly one workspace association.',
        'Conversation (bot’s membership channel)',
        {'#incident-triage': ['T_ATLAS'], '#incident-bridge': ['T_ORION']}, selector=selector,
    )


def w10_location(location):
    base = w10('multiple')
    seed = seed_from(base)
    roots = {name: workspace_membership('U_' + name, seed.team)
             for name in ('ALICE', 'BEN', 'ELENA')}
    group_a, group_b = [roots['ALICE'], roots['BEN']], [roots['ELENA']]
    rows = deepcopy(base['rows'])
    if location == 'channel':
        seed.member('U_PRIYA', 'C_MARKETING')
        rows[0] = (rows[0][0], rows[0][1] + ' Priya also belongs to #marketing.',
                   'Member of the #launch-prep alternative; answer is admin', rows[0][3])
        rows[1] = (rows[1][0], rows[1][1],
                   'Member of the #launch-prep alternative; answer is neither', rows[1][3])
        rows[4] = (rows[4][0],
                   'Elena reacted 🚀 to launch-checklist message M3 in #marketing. M3 has the same text '
                   'and author, Morgan, as M1 in #launch-prep. The same Priya Shah belongs to both '
                   'channels. Elena’s profile shows admin true, owner true.',
                   'Member of the #marketing alternative; answer is owner (also admin)', roots['ELENA'])
        description = ('Priya Shah is one established person who belongs to both #launch-prep and #marketing. '
                       'Each channel contains exactly one launch-checklist message. The singular channel '
                       'reference leaves the jointly intended reactor set unresolved between Alice/Ben '
                       'in #launch-prep and Elena in #marketing. Their union is not authorized. '
                       'Admin/owner status is answer content, never an identifying restriction.')
        change = ('Keep the original request and all messages/reactions. Add Priya Shah’s membership '
                  'in #marketing. No second Priya is introduced; the choice lies between channels.')
        choices = {'#launch-prep': group_a, '#marketing': group_b}
        label = 'Conversation (between message and Priya’s membership)'
    elif location == 'message':
        m3 = next(row for row in seed.data['messages']
                  if row['channel_id'] == 'C_MARKETING' and row['message_text'].startswith('Launch checklist:'))
        m3['channel_id'] = 'C_LAUNCH'
        seed.member('U_ELENA', 'C_LAUNCH')
        rows[0] = (rows[0][0], rows[0][1],
                   'Member of the M1 alternative; answer is admin', rows[0][3])
        rows[1] = (rows[1][0], rows[1][1],
                   'Member of the M1 alternative; answer is neither', rows[1][3])
        rows[4] = (rows[4][0],
                   'Elena reacted 🚀 to launch-checklist message M3 in #launch-prep. M3 is a separate '
                   'message with the same text and author, Morgan, as M1. Priya Shah belongs only to '
                   '#launch-prep. Elena belongs to #launch-prep and #marketing; her profile shows admin '
                   'true, owner true.',
                   'Member of the M3 alternative; answer is owner (also admin)', roots['ELENA'])
        description = ('Priya Shah and her single channel #launch-prep are established. That channel contains '
                       'two distinct launch-checklist messages, M1 and M3, with the same text and author. '
                       'The singular message reference leaves the jointly intended reactor set unresolved '
                       'between Alice/Ben on M1 and Elena on M3. Their union is not authorized. '
                       'Admin/owner status is answer content, never an identifying restriction.')
        change = ('Keep the original request. Move M3 into #launch-prep, preserving its text, author and '
                  'Elena’s 🚀 reaction, and add Elena to that channel. Priya remains one person with '
                  'only the #launch-prep membership. M1 and M3 lead to different reactor collections.')
        choices = {'M1': group_a, 'M3': group_b}
        label = 'Message (launch-checklist announcement)'
    else:
        raise ValueError(location)
    return finish(
        base, f'W10-underspecified-{location}', seed, base['case']['prompt'], rows,
        description, group_a + group_b, [group_a, group_b], 'set', change, label, choices,
        answers=[{'user_id': 'U_ALICE', 'is_admin': True, 'is_owner': False},
                 {'user_id': 'U_BEN', 'is_admin': False, 'is_owner': False},
                 {'user_id': 'U_ELENA', 'is_admin': True, 'is_owner': True}],
    )


def build_entries():
    return [w08_reaction(), w08_channel(), w09_channel(),
            w10_location('channel'), w10_location('message')]
