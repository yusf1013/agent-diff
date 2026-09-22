"""Manual changes of ambiguity location for W01–W04; no model calls."""
from copy import deepcopy

from suite_support import Seed, f, make_entry, selector
from suite_w01_w02 import w01, w02
from suite_w03_w06 import w03, w04


def copied_seed(entry):
    """Recover the authoring container without adding any seed records."""
    seed = Seed.__new__(Seed)
    seed.data = deepcopy(entry['case']['seed'])
    seed.actor = entry['case']['acting_user_id']
    seed.team = seed.data['teams'][0]['team_id']
    seed.messages = {row[0]: row[3] for row in entry['rows']
                     if row[0].startswith('M') and row[0][1:].isdigit()}
    return seed


def remake(base, case_id, seed, request, rows, description, expected, negatives,
           selection, change, location, choices, *, query=None):
    card = base['case']['cards'][0]
    entry = make_entry(
        case_id, base['base_id'], 'underspecified', seed, request, rows,
        description, expected, negatives, query or base['case']['private']['selector'],
        candidates=[choice['targets'] for choice in choices], selection=selection,
        computation=card['Change-computation attributes'],
        written=card['Written attributes'], change=change,
        operation=base['case']['private']['reference_outcome']['operation'])
    entry['ambiguity'] = {'location': location, 'explanation': description,
                          'choices': {choice['choice']: choice['targets'] for choice in choices}}
    return entry


def w01_message():
    base = w01('base')
    seed = copied_seed(base)
    mids = seed.messages
    rows = [(label, facts, 'Alternative intended message' if label in ('M1', 'M2') else meaning, handle)
            for label, facts, meaning, handle in base['rows']]
    return remake(
        base, 'W01-underspecified-message', seed,
        'Add 🚀 to the message Priya reacted to with 🙌.', rows,
        'Priya is uniquely Priya Shah. She reacted 🙌 to M1 and M2. The singular request '
        'does not distinguish the intended message and delegates no choice. Resolving the '
        'message reference to M1 or M2 yields different action targets; Diego’s additional '
        '👀 on M2 does not disqualify it.', [mids['M1'], mids['M2']],
        base['case']['private']['near_misses'], 'one',
        'Keep the original multiple environment and change messages to message; Priya remains a unique person.',
        'Message (target)', [{'choice': 'M1', 'targets': [mids['M1']]},
                             {'choice': 'M2', 'targets': [mids['M2']]}])


def w02_channel():
    base = w02('base')
    seed = copied_seed(base)
    for channel in seed.data['channels']:
        if channel['channel_id'] == 'C_OPERATIONS':
            channel['channel_name'] = 'finance-planning'
            channel['topic_text'] = 'Financial planning'
    rows = []
    for label, facts, meaning, handle in base['rows']:
        if label == 'Dana':
            meaning = 'Alternative recipient through #finance'
        elif label == 'Imani':
            facts = 'Reacted 🔥 to budget-freeze announcement M3 in #finance-planning, not to M1. Both #finance and #finance-planning have the topic Financial planning.'
            meaning = 'Alternative recipient through #finance-planning'
        rows.append((label, facts, meaning, handle))
    query = selector(['users', 'message_reactions', 'messages', 'channels'],
                     ['message_reactions.user_id', 'message_reactions.message_id', 'messages.channel_id'],
                     [f(1, 'reaction_type', 'fire'), f(2, 'message_text', 'Budget freeze:', 'contains_ci'),
                      f(3, 'topic_text', 'Financial planning', 'contains_ci')])
    expected = ['U_DANA', 'U_IMANI']
    return remake(
        base, 'W02-underspecified-channel', seed,
        'DM the person who reacted with 🔥 to the budget-freeze announcement in the finance channel: “The follow-up meeting is Thursday at 2pm.”',
        rows,
        'The descriptive finance channel reference fits #finance and #finance-planning, '
        'both with the topic Financial planning. Each has one budget-freeze announcement '
        'with one 🔥 reactor: Dana through M1 in #finance, or Imani through M3 in '
        '#finance-planning. The request names neither channel and delegates no choice. '
        'The message and recipient are unique once the channel is selected.',
        expected, [row[3] for row in rows if row[3] not in expected], 'one',
        'Change #operations to #finance-planning with the same finance topic as #finance; replace the exact #finance reference with the descriptive finance channel reference. Preserve both announcement/reaction paths.',
        'Conversation (source channel)',
        [{'choice': '#finance', 'targets': ['U_DANA']},
         {'choice': '#finance-planning', 'targets': ['U_IMANI']}], query=query)


def w03_location(location):
    base = w03('multiple')
    seed = copied_seed(base)
    rows = [(label, facts, 'Alternative target channel' if handle in ('C_FINANCE', 'C_PLANNING') else meaning, handle)
            for label, facts, meaning, handle in base['rows']]
    if location == 'message':
        request = 'Post “Please send feedback by Friday.” in the channel with the budget-approved message Alex Rivera reacted to with 🎉.'
        description = ('Alex Rivera is a unique person, but the definite budget-approved message '
                       'reference fits M1 in #finance-updates and M2 in #planning-sync. Each '
                       'message belongs to one channel. Choosing M1 or M2 therefore yields '
                       'different posting targets; the request does not distinguish the '
                       'intended message or authorize choosing one.')
        choices = [{'choice': 'M1', 'targets': ['C_FINANCE']},
                   {'choice': 'M2', 'targets': ['C_PLANNING']}]
        origin = 'Message (intermediate)'
        change = 'Use unique Alex Rivera, with his 🎉 on both M1 and M2. Ask for the channel containing the budget-approved message, leaving that message unresolved.'
    else:
        request = 'Post “Please send feedback by Friday.” in the channel with a budget-approved message Alex Rivera reacted to with 🎉.'
        description = ('Alex Rivera is a unique person. A budget-approved message is an '
                       'existential condition: #finance-updates qualifies through M1 and '
                       '#planning-sync through M2. No particular message must first be '
                       'selected. The singular target channel remains unresolved between '
                       'the two qualifying channels; listing them does not grant authority '
                       'to choose or post to both.')
        choices = [{'choice': '#finance-updates', 'targets': ['C_FINANCE']},
                   {'choice': '#planning-sync', 'targets': ['C_PLANNING']}]
        origin = 'Conversation (target)'
        change = 'Keep the intermediate-message variant environment and change the budget-approved message to a budget-approved message, leaving the target channel as the unresolved choice.'
    return remake(base, 'W03-underspecified-' + location, seed, request, rows,
                  description, ['C_FINANCE', 'C_PLANNING'],
                  base['case']['private']['near_misses'], 'one', change, origin, choices)


def w04_channel():
    base = w04('single')
    seed = copied_seed(base)
    mids = seed.messages
    expected = [mids['M8'], mids['M6']]
    rows = []
    for label, facts, meaning, handle in base['rows']:
        if label == 'M8':
            meaning = 'Alternative through #beta-testers'
        elif label == 'M6':
            meaning = 'Alternative through #beta-testers-west'
        rows.append((label, facts, meaning, handle))
    query = selector(['messages', 'message_reactions', 'users', 'channel_members', 'channels'],
                     ['message_reactions.message_id', 'message_reactions.user_id',
                      'channel_members.user_id', 'channel_members.channel_id'],
                     [f(0, 'message_text', 'rollout checklist', 'contains_ci'),
                      f(1, 'reaction_type', 'rocket'), f(4, 'topic_text', 'beta testing', 'contains_ci')])
    return remake(
        base, 'W04-underspecified-channel', seed,
        'Reply to the rollout-checklist message that got a 🚀 reaction from a member of the channel for beta testing: “Please confirm the final go-ahead timing.”',
        rows,
        'The channel for beta testing can mean #beta-testers or #beta-testers-west: '
        'their topics explicitly describe Beta testing and Western region beta testing. '
        'Farah’s 🚀 on M8 qualifies through the former; Harold’s 🚀 on M6 qualifies '
        'through the latter. Each channel interpretation yields one different message. '
        'The prompt does not identify the intended channel or delegate a choice. M9 is absent.',
        expected, [row[3] for row in rows if row[3] not in expected], 'one',
        'Keep the single variant environment, including M8 but not M9; replace #beta-testers with the channel for beta testing. M6 is now a legitimate alternative, not a negative.',
        'Conversation (membership channel at far end)',
        [{'choice': '#beta-testers', 'targets': [mids['M8']]},
         {'choice': '#beta-testers-west', 'targets': [mids['M6']]}], query=query)


def w04_reaction():
    base = w04('single')
    seed = copied_seed(base)
    mids = seed.messages
    for reaction in seed.data['message_reactions']:
        if reaction['message_id'] == mids['M2']:
            assert reaction['user_id'] == 'U_FARAH' and reaction['reaction_type'] == 'thumbsup'
            reaction['reaction_type'] = 'tada'
    anchor = seed.message('M10', 'C_RELEASE', 'U_MORGAN',
                          'Release date announcement: the next release will be available on November 14.')
    seed.react(anchor, 'U_FARAH', '🚀')
    seed.react(anchor, 'U_FARAH', '🎉')
    rows = []
    for label, facts, meaning, handle in base['rows']:
        if label == 'M8':
            meaning = 'Alternative target if the intended anchor emoji is 🚀'
        elif label == 'M2':
            facts = 'A rollout-checklist message. Its only reaction is Farah’s 🎉. Farah belongs to #beta-testers.'
            meaning = 'Alternative target if the intended anchor emoji is 🎉'
        elif label == 'M4':
            meaning = 'Farah’s 👀 is not on the anchor announcement; Ethan’s 🚀 lacks the membership'
        rows.append((label, facts, meaning, handle))
    rows.append(('M10', 'The one release-date announcement: the release is available on November 14. Farah reacted both 🚀 and 🎉. It is about the release date, not a rollout checklist.',
                 'Source of the unresolved emoji choice; not a target message', anchor))
    query = selector(['messages', 'message_reactions', 'users', 'channel_members', 'channels'],
                     ['message_reactions.message_id', 'message_reactions.user_id',
                      'channel_members.user_id', 'channel_members.channel_id'],
                     [f(0, 'message_text', 'rollout checklist', 'contains_ci'),
                      f(1, 'reaction_type', ['rocket', 'tada'], 'in'),
                      f(4, 'channel_name', 'beta-testers')])
    description = (
        'Identify a rollout-checklist message with a reaction from a current member of '
        '#beta-testers, using the emoji referred to on the unique release-date announcement '
        'M10. That announcement has Farah’s 🚀 and 🎉 reactions, with no wording selecting '
        'one or delegating a choice. The ambiguity is the referenced reaction emoji: 🚀 '
        'selects only M8, whereas 🎉 selects only M2. Farah and #beta-testers are unambiguous, '
        'and each emoji interpretation yields one different target message. M10 supplies '
        'identifying information; its date-only content does not make it a rollout-checklist '
        'target. The mechanical selector uses the seed-specific union {rocket, tada}; '
        'the independent audit checks that these are exactly the emoji values on M10 '
        'and recomputes the target set separately for each value.')
    expected = [mids['M8'], mids['M2']]
    entry = remake(
        base, 'W04-underspecified-reaction', seed,
        'Reply to the rollout-checklist message that a member of #beta-testers reacted to with the emoji used on the release-date announcement: “Please confirm the final go-ahead timing.”',
        rows, description, expected, [row[3] for row in rows if row[3] not in expected], 'one',
        'Keep the single variant and M8; change M2’s Farah reaction from 👍 to 🎉. Add the unique release-date announcement M10 with 🚀 and 🎉. Replace the fixed 🚀 criterion with a reference to its unresolved reaction emoji. No M9 is added.',
        'Reaction (intermediate emoji choice)',
        [{'choice': '🚀 on M10', 'targets': [mids['M8']]},
         {'choice': '🎉 on M10', 'targets': [mids['M2']]}], query=query)
    card = entry['case']['cards'][0]
    card['Identifying paths'].append({'entities': ['messages', 'message_reactions'],
                                     'relationships': ['message_reactions.message_id']})
    # Real source fields and an explicit set operation preserve the source-derived
    # meaning. The finite selector's constants alone do not document that meaning.
    constraints = card['Referent set']['partial_constraints']
    constraints.remove("message_reactions.reaction_type in ['rocket', 'tada']")
    constraints.append(
        "message_reactions.reaction_type in {r.reaction_type for r in message_reactions "
        "for m in messages if r.message_id == m.message_id and "
        "'release date announcement:' in m.message_text.lower()}")
    entry['case']['private']['materialized_selection_inputs'] = {
        'source_message': anchor,
        'source_message_condition': {'field': 'message_text', 'op': 'contains_ci',
                                     'value': 'release date announcement:'},
        'source_relation': 'message_reactions.message_id',
        'source_attribute': 'message_reactions.reaction_type',
        'values': ['rocket', 'tada'],
        'note': 'Seed-specific values; independently derive them from the unique source announcement before validating the per-emoji target sets.'}
    return entry


def build_entries():
    return [w01_message(), w02_channel(), w03_location('message'),
            w03_location('channel'), w04_channel(), w04_reaction()]
