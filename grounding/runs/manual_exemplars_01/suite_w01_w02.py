"""Manual W01/W02 originals and agreed variants."""
from suite_support import Seed, f, selector, make_entry


def w01(variant):
    mode = {'base': 'multiple', 'single': 'single', 'absent-authorship': 'absent',
            'absent-text-emoji': 'absent', 'underspecified': 'underspecified'}[variant]
    s = Seed()
    priya = s.user('PRIYA_SHAH', 'Priya Shah')
    diego = s.user('DIEGO', 'Diego Alvarez')
    author = s.user('MORGAN', 'Morgan Chen')
    rao = s.user('PRIYA_RAO', 'Priya Rao') if variant == 'underspecified' else None
    channel = s.channel('GENERAL', 'general', topic='Company updates and discussion')
    for u in s.data['users']:
        s.member(u['user_id'], channel)
    texts = ['The supplier estimates arrived this morning.', 'The draft schedule is ready for review.',
             'The updated supplier estimates arrived this afternoon.', 'The revised schedule is ready for review.',
             'The room booking is confirmed for Thursday.', 'The room booking is confirmed for Friday.']
    absent = mode == 'absent'
    for n, text in enumerate(texts, 1):
        if variant == 'single' and n == 1:
            continue
        if variant == 'absent-text-emoji' and n in (1, 2):
            text += ' 🙌'
        s.message('M' + str(n), channel, priya if absent and n in (1, 2) else author, text)
    m = s.messages
    if not absent:
        if 'M1' in m:
            s.react(m['M1'], priya, '🙌')
        s.react(m['M2'], rao or priya, '🙌')
    s.react(m['M2'], diego, '👀')
    s.react(m['M3'], priya, '👀')
    s.react(m['M4'], diego, '🙌')
    s.react(m['M6'], priya, '👀')
    s.react(m['M6'], diego, '🙌')
    rows = []
    if 'M1' in m:
        facts = ('Authored by Priya; no reactions.' if absent else 'Priya Shah reacted 🙌.' if rao else 'Priya reacted 🙌.')
        if variant == 'absent-text-emoji':
            facts = 'Authored by Priya; 🙌 appears in the message text; no reactions.'
        rows.append(('M1', facts, 'Authorship/text is not a reaction' if absent else 'Alternative through Priya Shah' if rao else 'Match', m['M1']))
    facts = ('Authored by Priya; Diego reacted 👀; no other reactions.' if absent else
             'Priya Rao reacted 🙌; Diego also reacted 👀.' if rao else 'Priya reacted 🙌; Diego also reacted 👀.')
    if variant == 'absent-text-emoji':
        facts = 'Authored by Priya; 🙌 appears in the message text; Diego reacted 👀; no other reactions.'
    rows.append(('M2', facts, 'Authorship/text is not a reaction' if absent else 'Alternative through Priya Rao' if rao else 'Match with unrelated activity', m['M2']))
    pname = 'Priya Shah' if rao else 'Priya'
    rows += [('M3', f'{pname} reacted 👀, with no other reactions.', 'Wrong emoji only', m['M3']),
             ('M4', 'Diego reacted 🙌, with no other reactions.', 'Wrong person only', m['M4']),
             ('M5', 'The message has no reactions.', 'Missing reaction relationship', m['M5']),
             ('M6', f'{pname} reacted 👀 and Diego reacted 🙌. These are the only reactions.', 'Person and emoji occur on different reactions', m['M6'])]
    expected = [] if absent else [m[x] for x in ('M1', 'M2') if x in m]
    negatives = [m[x] for x in m if m[x] not in expected]
    candidates = [[m['M1']], [m['M2']]] if rao else None
    q = selector(['messages', 'message_reactions', 'users'],
                 ['message_reactions.message_id', 'message_reactions.user_id'],
                 [f(1, 'reaction_type', 'raised_hands'),
                  f(2, 'real_name', 'Priya ', 'contains_ci') if rao else f(2, 'real_name', 'Priya Shah')])
    description = 'Resolve messages with a raised_hands reaction by Priya on that same reaction record, then add rocket to those messages.'
    if rao:
        description += ' Priya Shah and Priya Rao are distinct users. The intended message collection is {M1} for Shah or {M2} for Rao; the request does not identify which Priya. The alternatives are not a combined target set.'
    change = {'base': 'Original story, concretely instantiated.', 'single': 'Remove M1 only; retain the plural request and every other row.',
              'absent-authorship': 'Replace Priya’s 🙌 reactions on M1/M2 with Priya’s authorship. Preserve Diego’s 👀 on M2.',
              'absent-text-emoji': 'As in absent-authorship, and include 🙌 in both authored message bodies, not as Priya’s reaction.',
              'underspecified': 'Keep Priya Shah on M1/M3/M6; add Priya Rao and make her the 🙌 reactor on M2.'}[variant]
    return make_entry('W01-' + variant, 'W01', mode, s,
        'Add 🚀 to the messages Priya reacted to with 🙌.', rows, description, expected, negatives, q,
        candidates=candidates, selection='set', computation=[['messages.message_id']],
        written=['message_reactions.message_id', 'message_reactions.reaction_type'],
        change=change, operation={'kind': 'react', 'emoji': 'rocket'})


def w02(variant):
    mode = {'base': 'single', 'multiple': 'multiple', 'absent': 'absent',
            'underspecified-reactor': 'underspecified', 'underspecified-announcement': 'underspecified'}[variant]
    s = Seed()
    names = {'DANA': 'Dana Reyes', 'WES': 'Wes Carter', 'NORA': 'Nora Ellis',
             'IMANI': 'Imani Brooks', 'PRIYA': 'Priya Shah', 'OMAR': 'Omar Haddad'}
    users = {k: s.user(k, name) for k, name in names.items()}
    extra = variant in ('multiple', 'underspecified-reactor', 'underspecified-announcement')
    if extra:
        users['MORGAN'] = s.user('MORGAN', 'Morgan Chen')
    finance = s.channel('FINANCE', 'finance', topic='Financial planning')
    ops = s.channel('OPERATIONS', 'operations', topic='Operations coordination')
    for uid in users.values():
        s.member(uid, finance)
        s.member(uid, ops)
    budget = 'Budget freeze: spending limits are now in effect for the coming quarter.'
    m1 = s.message('M1', finance, users['PRIYA'], budget)
    m2 = s.message('M2', finance, users['PRIYA'], 'Office relocation: assigned rooms are on the floor plan; moving day is Tuesday.')
    m3 = s.message('M3', ops, users['PRIYA'], budget)
    if mode != 'absent':
        s.react(m1, users['DANA'], '🔥')
    s.react(m1, users['WES'], '👍')
    s.react(m2, users['NORA'], '🔥')
    s.react(m3, users['IMANI'], '🔥')
    s.react(m1, users['OMAR'], '👍')
    s.react(m2, users['OMAR'], '🔥')
    if extra:
        target = s.message('M4', finance, users['PRIYA'],
                           'Budget freeze: the revised spending limits take effect on the first day of next month.') if variant == 'underspecified-announcement' else m1
        s.react(target, users['MORGAN'], '🔥')
    alternatives = mode == 'underspecified'
    rows = [('Dana', 'Has no reactions.' if mode == 'absent' else 'Reacted 🔥 to budget-freeze announcement M1 in #finance.',
             'Missing reaction relationship' if mode == 'absent' else 'Alternative recipient' if alternatives else 'Match', users['DANA']),
            ('Wes', 'Reacted 👍 to M1; no 🔥 on it.', 'Wrong emoji only', users['WES']),
            ('Nora', 'Reacted 🔥 to office-relocation announcement M2 in #finance, not to M1. M2 concerns rooms and moving dates only.', 'Wrong message topic only', users['NORA']),
            ('Imani', 'Reacted 🔥 to budget-freeze announcement M3 in #operations, not to M1.', 'Wrong message channel only', users['IMANI']),
            ('Priya', 'Authored M1 but has no reactions.', 'Author is not a reactor', users['PRIYA']),
            ('Omar', 'Reacted 👍 to M1 and 🔥 to M2; no other reactions.', 'Emoji and announcement occur on different reactions', users['OMAR'])]
    if extra:
        facts = ('Reacted 🔥 to a different budget-freeze announcement M4 in #finance; did not react to M1.'
                 if variant == 'underspecified-announcement' else 'Reacted 🔥 to the same M1 as Dana.')
        rows.append(('Morgan', facts, 'Alternative recipient' if alternatives else 'Match', users['MORGAN']))
    expected = [] if mode == 'absent' else [users['DANA']] + ([users['MORGAN']] if extra else [])
    negatives = [uid for uid in users.values() if uid not in expected]
    candidates = [[users['DANA']], [users['MORGAN']]] if alternatives else None
    q = selector(['users', 'message_reactions', 'messages', 'channels'],
                 ['message_reactions.user_id', 'message_reactions.message_id', 'messages.channel_id'],
                 [f(1, 'reaction_type', 'fire'), f(2, 'message_text', 'Budget freeze:', 'contains_ci'),
                  f(3, 'channel_name', 'finance')])
    description = 'Resolve the person who has a fire reaction on a budget-freeze announcement in #finance; emoji, message topic, and location must hold on the same reaction/message path. Send the requested DM.'
    if variant == 'multiple':
        description = description.replace('the person who has', 'the people who have')
    if alternatives:
        description += (' Dana and Morgan both reacted to the one announcement, but the singular request does not distinguish the intended person.'
                        if variant == 'underspecified-reactor' else
                        ' Two separate budget-freeze announcements in #finance lead to Dana and Morgan respectively; the request selects neither announcement. Recency is not a supplied selection rule.')
    recipient = 'people' if mode == 'multiple' else 'person'
    request = f'DM the {recipient} who reacted with 🔥 to the budget-freeze announcement in #finance: “The follow-up meeting is Thursday at 2pm.”'
    change = {'base': 'Original story, concretely instantiated.', 'multiple': 'Add Morgan’s 🔥 to M1; change person to people.',
              'absent': 'Remove Dana’s 🔥 reaction; keep every other row.',
              'underspecified-reactor': 'Add Morgan’s 🔥 to M1; preserve the singular person request.',
              'underspecified-announcement': 'Add a second budget-freeze announcement M4 in #finance and Morgan’s 🔥 on it; preserve the singular request.'}[variant]
    return make_entry('W02-' + variant, 'W02', mode, s, request, rows, description,
        expected, negatives, q, candidates=candidates, selection='set' if mode == 'multiple' else 'one',
        computation=[['users.user_id']], written=['channel_members.user_id', 'messages.channel_id', 'messages.message_text'],
        change=change, operation={'kind': 'dm', 'text': 'The follow-up meeting is Thursday at 2pm.'})


def build_entries():
    return [w01(v) for v in ('base', 'single', 'absent-authorship', 'absent-text-emoji', 'underspecified')] + [
        w02(v) for v in ('base', 'multiple', 'absent', 'underspecified-reactor', 'underspecified-announcement')]
