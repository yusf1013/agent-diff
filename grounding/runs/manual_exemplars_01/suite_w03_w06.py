"""Manually authored W03–W06 bases and resolution variants; no model calls."""
from suite_support import Seed, f, make_entry, selector


def w03(mode):
    s = Seed()
    rivera = s.user('alex_rivera', 'Alex Rivera')
    kim = s.user('alex_kim', 'Alex Kim')
    morgan = s.user('morgan', 'Morgan Ellis')
    channels = [
        ('finance', 'finance-updates', 'Finance updates'),
        ('planning', 'planning-sync', 'Planning updates'),
        ('vendor', 'vendor-updates', 'Vendor updates'),
        ('office', 'office-updates', 'Office logistics'),
        ('procurement', 'procurement-updates', 'Procurement updates'),
        ('delivery', 'delivery-updates', 'Delivery updates'),
        ('purchasing', 'purchasing-updates', 'Purchasing updates'),
    ]
    cs = [s.channel(key, name, topic=topic) for key, name, topic in channels]
    for cid in cs:
        for uid in (rivera, kim, morgan):
            s.member(uid, cid)
    texts = [
        'Budget approved for the autumn customer research program. The travel allocation is ready.',
        'Budget approved for the website localization project. Procurement can book the translation work.',
        'Budget approved for the annual vendor workshop. The catering allocation is included.',
        'The office relocation is scheduled for October 12. Room assignments and moving dates are on the facilities board.',
        'Budget approved for the accessibility research program. The participant funding is ready.',
        'Budget approved for the regional training workshop. The venue allocation is included.',
        'Budget approved for the documentation refresh. The copyediting allocation is ready.',
    ]
    mids = [s.message(f'M{i+1}', cid, rivera if i == 6 else morgan, text)
            for i, (cid, text) in enumerate(zip(cs, texts))]
    # The full-name variants retain an isolated topic negative by using Rivera on M4.
    name = 'Alex' if mode == 'underspecified' else 'Alex Rivera'
    second = rivera if mode == 'multiple' else kim
    office = kim if mode == 'underspecified' else rivera
    s.react(mids[0], rivera, '👍' if mode == 'absent' else '🎉')
    s.react(mids[1], second, '🎉')
    s.react(mids[2], rivera, '👍')
    s.react(mids[3], office, '🎉')
    s.react(mids[4], morgan, '🎉')
    s.react(mids[5], rivera, '👍')
    s.react(mids[5], morgan, '🎉')
    s.react(mids[6], morgan, '🎉')
    text = 'Please send feedback by Friday.'
    target = 'channels with the budget-approved messages' if mode == 'multiple' else 'channel with the budget-approved message'
    request = f'Post “{text}” in the {target} {name} reacted to with 🎉.'
    first_i = 'Alternative through Alex Rivera' if mode == 'underspecified' else 'Wrong emoji only' if mode == 'absent' else 'Match'
    second_i = 'Alternative through Alex Kim' if mode == 'underspecified' else 'Match' if mode == 'multiple' else 'Wrong reactor identity only; Alex Kim is not Alex Rivera'
    second_name = 'Alex Rivera' if second == rivera else 'Alex Kim'
    office_name = 'Alex Rivera' if office == rivera else 'Alex Kim'
    rows = [
        ('#finance-updates', f'Contains budget-approved message M1, which Alex Rivera reacted to with {"👍" if mode == "absent" else "🎉"}.', first_i, cs[0]),
        ('#planning-sync', f'Contains a different budget-approved message M2, which {second_name} reacted to with 🎉.', second_i, cs[1]),
        ('#vendor-updates', 'Contains budget-approved message M3. Alex Rivera reacted 👍, with no other reactions.', 'Wrong emoji only', cs[2]),
        ('#office-updates', f'Contains office-relocation message M4, which {office_name} reacted to with 🎉. M4 does not discuss budgets.', 'Wrong message topic only', cs[3]),
        ('#procurement-updates', 'Contains budget-approved message M5, which Morgan reacted to with 🎉. Neither Alex reacted to it.', 'Wrong reactor name only', cs[4]),
        ('#delivery-updates', 'Contains budget-approved message M6. Alex Rivera reacted 👍 and Morgan reacted 🎉; these are its only reactions.', 'Requested person and 🎉 occur on different reactions', cs[5]),
        ('#purchasing-updates', 'Contains budget-approved message M7, authored by Alex Rivera. Its only reaction is Morgan’s 🎉; neither Alex reacted to it.', 'Alex is the author, not the reactor', cs[6]),
    ]
    expected = cs[:2] if mode in ('multiple', 'underspecified') else cs[:1] if mode == 'single' else []
    filters = [f(1, 'message_text', 'budget approved', 'contains_ci'), f(2, 'reaction_type', 'tada'),
               f(3, 'real_name', 'Alex ', 'contains_ci') if mode == 'underspecified' else f(3, 'real_name', 'Alex Rivera')]
    q = selector(['channels', 'messages', 'message_reactions', 'users'],
                 ['messages.channel_id', 'message_reactions.message_id', 'message_reactions.user_id'], filters)
    changes = {
        'underspecified': 'Base case: Alex Rivera and Alex Kim identify different channels; no authority to choose.',
        'single': 'Name Alex Rivera explicitly. M4’s reactor is also Alex Rivera, preserving its isolated topic mismatch. Other records remain unchanged.',
        'multiple': 'Name Alex Rivera explicitly, use plural channels/messages, and change M2’s and M4’s reactor from Alex Kim to Alex Rivera. The two channels are jointly intended.',
        'absent': 'Name Alex Rivera explicitly; change his M1 reaction to 👍. M4’s reactor becomes Alex Rivera so the office message remains an isolated topic negative.',
    }
    return make_entry('W03-base' if mode == 'underspecified' else f'W03-{mode}', 'W03', mode, s, request, rows,
                      f'Channels containing a budget-approved message with a 🎉 reaction whose reactor is {name}. The same reaction must bind the emoji and reactor. '
                      + ('The two Alex identities remain competing alternatives.' if mode == 'underspecified' else 'Only the named full identity is intended.'),
                      expected, [c for c in cs if c not in expected], q,
                      candidates=[[c] for c in expected] if mode == 'underspecified' else None,
                      computation=[['channels.channel_id']], written=['messages.channel_id', 'messages.message_text'],
                      change=changes[mode], operation={'kind': 'post', 'text': text})


def w04(mode):
    s = Seed()
    ethan = s.user('ethan', 'Ethan Brooks')
    farah = s.user('farah', 'Farah Ali')
    grace = s.user('grace', 'Grace Chen')
    harold = s.user('harold', 'Harold Davis')
    morgan = s.user('morgan', 'Morgan Ellis')
    release = s.channel('release', 'release-updates', topic='Product release coordination')
    beta = s.channel('beta', 'beta-testers', topic='Beta testing')
    care = s.channel('care', 'customer-care', topic='Customer support')
    west = s.channel('west', 'beta-testers-west', topic='Western region beta testing')
    for uid in (ethan, farah, grace, harold, morgan):
        s.member(uid, release)
    for uid, cid in ((ethan, care), (farah, beta), (grace, beta), (harold, west)):
        s.member(uid, cid)
    mids = [
        s.message('M1', release, morgan, 'The rollout checklist for the account dashboard is ready. The staging smoke tests are complete.'),
        s.message('M2', release, morgan, 'The rollout checklist for the search update is ready. The regional schedule is in the release notes.'),
        s.message('M3', release, morgan, 'The office relocation is scheduled for October 12. Room assignments and moving dates are on the facilities board.'),
        s.message('M4', release, morgan, 'The rollout checklist for the billing update is ready. The support handover is scheduled for Tuesday.'),
        s.message('M5', release, morgan, 'The rollout checklist for the reporting update is ready. The training session is on Wednesday.'),
        s.message('M6', release, morgan, 'The rollout checklist for the export update is ready. The documentation draft is linked in the release notes.'),
        s.message('M7', release, farah, 'The rollout checklist for the notification update is ready. The delivery monitoring panel is configured.'),
    ]
    for idx, uid, emoji in [(0, ethan, '🚀'), (1, farah, '👍'), (2, grace, '🚀'), (3, farah, '👀'),
                            (3, ethan, '🚀'), (5, harold, '🚀'), (6, ethan, '🚀')]:
        s.react(mids[idx], uid, emoji)
    rows = [
        ('M1', 'A rollout-checklist message. Its only reaction is Ethan’s 🚀. Ethan belongs to #customer-care, not #beta-testers.', 'Wrong reactor membership only', mids[0]),
        ('M2', 'A distinct rollout-checklist message. Its only reaction is Farah’s 👍. Farah belongs to #beta-testers.', 'Wrong emoji only', mids[1]),
        ('M3', 'An office-relocation announcement about room assignments and moving dates. Its only reaction is Grace’s 🚀. Grace belongs to #beta-testers. It does not discuss a product rollout or checklist.', 'Wrong message topic only', mids[2]),
        ('M4', 'A rollout-checklist message. Farah reacted 👀 and Ethan reacted 🚀; these are its only reactions.', '🚀 and #beta-testers membership belong to different reactors', mids[3]),
        ('M5', 'A rollout-checklist message with no reactions.', 'Missing reaction relationship', mids[4]),
        ('M6', 'A rollout-checklist message. Its only reaction is Harold’s 🚀. Harold belongs to #beta-testers-west, not #beta-testers.', 'Wrong membership channel only; the similarly named channel is distinct', mids[5]),
        ('M7', 'A rollout-checklist message authored by Farah, who belongs to #beta-testers. Its only reaction is Ethan’s 🚀; Ethan does not belong to #beta-testers.', 'The author has the required membership, but the reactor does not', mids[6]),
    ]
    expected = []
    positive_rows = []
    if mode != 'absent':
        m8 = s.message('M8', release, morgan, 'The rollout checklist for the permissions update is ready. The deployment window is booked for Thursday.')
        s.react(m8, farah, '🚀')
        expected.append(m8)
        positive_rows.append(('M8', 'A rollout-checklist message. Its only reaction is Farah’s 🚀; Farah belongs to #beta-testers.', 'Alternative through M8' if mode == 'underspecified' else 'Match', m8))
    if mode in ('multiple', 'underspecified'):
        m9 = s.message('M9', release, morgan, 'The rollout checklist for the search index migration is ready. The deployment window is booked for Monday.')
        s.react(m9, grace, '🚀')
        s.react(m9, ethan, '👀')
        expected.append(m9)
        positive_rows.append(('M9', 'A different rollout-checklist message. Grace reacted 🚀 and Ethan reacted 👀. Grace belongs to #beta-testers; Ethan does not.', 'Alternative through M9' if mode == 'underspecified' else 'Match with unrelated activity', m9))
    rows = positive_rows + rows
    text = 'Please confirm the final go-ahead timing.'
    noun = 'messages' if mode == 'multiple' else 'message'
    request = f'Reply to the rollout-checklist {noun} that got a 🚀 reaction from a member of #beta-testers: “{text}”'
    q = selector(['messages', 'message_reactions', 'users', 'channel_members', 'channels'],
                 ['message_reactions.message_id', 'message_reactions.user_id', 'channel_members.user_id', 'channel_members.channel_id'],
                 [f(0, 'message_text', 'rollout checklist', 'contains_ci'), f(1, 'reaction_type', 'rocket'), f(4, 'channel_name', 'beta-testers')])
    changes = {
        'absent': 'Base case: seven negatives and no full match.',
        'single': 'Keep all seven negatives and add one qualifying message, M8. The request is unchanged.',
        'multiple': 'Keep all seven negatives and add M8 and M9. Pluralize message to messages so both are jointly intended.',
        'underspecified': 'Use the same two qualifying messages as the multiple variant, with the original singular request. No condition distinguishes the intended message.',
    }
    return make_entry('W04-base' if mode == 'absent' else f'W04-{mode}', 'W04', mode, s, request, rows,
                      'Rollout-checklist messages with a 🚀 reaction whose reactor currently belongs to #beta-testers. '
                      'The emoji and membership must bind the same reactor. '
                      + ('One message is intended, but M8 and M9 remain competing alternatives.' if mode == 'underspecified' else ''),
                      expected, mids, q, candidates=[[m] for m in expected] if mode == 'underspecified' else None,
                      computation=[['messages.channel_id', 'messages.message_id']],
                      written=['messages.channel_id', 'messages.parent_id', 'messages.message_text'],
                      change=changes[mode], operation={'kind': 'reply', 'text': text})


def w05(mode):
    s = Seed()
    roster = [s.user(key, name) for key, name in [('jules', 'Jules Morgan'), ('ravi', 'Ravi Singh'),
              ('sofia', 'Sofia Gomez'), ('kate', 'Kate Jensen'), ('noah', 'Noah Clarke'), ('amal', 'Amal Hassan')]]
    unrelated = s.channel('general', 'general', topic='Company discussion')
    s.member(roster[0], unrelated)
    definitions = [
        ('fall', 'onboarding-fall', 5 if mode == 'absent' else 6, False),
        ('spring', 'onboarding-spring', 7 if mode == 'absent' else 6, True),
        ('winter', 'onboarding-winter', 5, False),
        ('summer', 'onboarding-summer', 7, False),
        ('office', 'office-move', 6, False),
    ]
    if mode == 'single':
        definitions = [d for d in definitions if d[0] != 'fall']
    rows, expected, negatives = [], [], []
    for key, name, count, private in definitions:
        purpose = 'Office relocation logistics' if key == 'office' else 'New-hire onboarding'
        cid = s.channel(key, name, topic=purpose, purpose=purpose, private=private)
        for uid in roster[:count-1]:
            s.member(uid, cid)
        content = ('The movers will arrive at 8am on Saturday. The seating chart is on the facilities board.' if key == 'office'
                   else 'The new-hire onboarding schedule is ready. Orientation starts at 9am and the benefits session follows lunch.')
        s.message('M' + str({'fall': 1, 'spring': 2, 'winter': 3, 'summer': 4, 'office': 5}[key]), cid, roster[0], content)
        is_match = key != 'office' and count == 6
        if is_match:
            expected.append(cid)
            interpretation = ('Alternative through #' + name) if mode == 'underspecified' else 'Match; privacy and unrelated memberships do not exclude it' if private else 'Match'
        else:
            negatives.append(cid)
            interpretation = 'Wrong channel purpose/topic only' if key == 'office' else f'Wrong member count only — {"below" if count < 6 else "above"} six'
        facts = (f'{"Private" if private else "Public"} channel for {"office-relocation logistics" if key == "office" else "new-hire onboarding"}; exactly {count} current members, including the actor.'
                 + (' One member also belongs to unrelated channels.' if private else '')
                 + (' Its content does not concern onboarding.' if key == 'office' else ''))
        rows.append(('#' + name, facts, interpretation, cid))
    text = 'Please complete the compliance training module by Friday.'
    noun = 'channel' if mode == 'underspecified' else 'channels'
    request = f'Post “{text}” to the onboarding {noun} with exactly six members.'
    q = selector(['channels', 'channel_members'], ['channel_members.channel_id'], [],
                 scope=[{'field': 'topic_text', 'op': 'contains_ci', 'value': 'onboarding'}],
                 count={'node': 1, 'op': 'eq', 'value': 6})
    changes = {
        'multiple': 'Base case: both six-member onboarding channels are intended, including the private channel.',
        'single': 'Remove #onboarding-fall. The private #onboarding-spring is the sole match; retain the original plural request.',
        'absent': 'Change #onboarding-fall to five members and #onboarding-spring to seven. The request and all other channel facts remain unchanged.',
        'underspecified': 'Keep the original environment and change channels to channel. Both six-member onboarding channels remain alternatives; no choice is delegated.',
    }
    return make_entry('W05-base' if mode == 'multiple' else f'W05-{mode}', 'W05', mode, s, request, rows,
                      'Onboarding channels with exactly six current members, including the actor. Public/private status does not change eligibility. '
                      + ('The singular request does not distinguish the two qualifying channels.' if mode == 'underspecified' else ''),
                      expected, negatives, q, candidates=[[c] for c in expected] if mode == 'underspecified' else None,
                      computation=[['channels.channel_id']], written=['messages.channel_id', 'messages.message_text'],
                      change=changes[mode], operation={'kind': 'post', 'text': text})


def w06(mode):
    s = Seed()
    dana = s.user('dana', 'Dana Park')
    farid = s.user('farid', 'Farid Hasan')
    priya = s.user('priya', 'Priya Shah')
    owen = s.user('owen', 'Owen Miller')
    lucia = s.user('lucia', 'Lucia Torres')
    theo = s.user('theo', 'Theo Bennett')
    general = s.channel('general', 'general', topic='Company updates')
    random = s.channel('random', 'random', topic='Informal conversation')
    hub = s.channel('hub', 'mentorship-hub', topic='Mentoring coordination')
    lounge = s.channel('lounge', 'mentors-lounge', topic='Mentor discussion')
    for uid, cid in [(dana, general), (farid, random), (priya, general), (owen, general), (owen, lounge), (theo, general)]:
        s.member(uid, cid)
    if mode != 'absent':
        s.member(dana, hub)
        s.member(farid, hub)
    # Actor belongs to all scenario channels but authors no seeded messages.
    # Lucia deliberately has no channel membership; authoring history adds none.
    mids = {}
    if mode != 'single':
        mids['M1'] = s.message('M1', general, dana, 'The meeting room booking calendar has been updated for October.')
    mids['M2'] = s.message('M2', random, farid, 'The food truck is coming to the courtyard on Friday.')
    s.react(mids['M2'], priya, '👍')
    mids['M3'] = s.message('M3', general, priya, 'The new printer is installed beside the reception desk.')
    mids['M4'] = s.message('M4', general, owen, 'The bike storage entrance will reopen on Monday.')
    mids['M5'] = s.message('M5', general, lucia, 'The book exchange shelf has moved to the third-floor lounge.')
    mids['M6'] = s.message('M6', hub, theo, 'The visitor badges are available from reception.')
    member_suffix = 'currently belongs only to #general; she does not belong to #mentorship-hub' if mode == 'absent' else 'currently belongs to #general and #mentorship-hub'
    farid_suffix = 'currently belongs only to #random; he does not belong to #mentorship-hub' if mode == 'absent' else 'currently belongs to #random and #mentorship-hub'
    rows = []
    if mode != 'single':
        rows.append(('M1', f'Dana authored this message in #general. Dana {member_suffix}.',
                     'Wrong author membership channel only' if mode == 'absent' else 'Alternative through Dana’s message' if mode == 'underspecified' else 'Match', mids['M1']))
    rows += [
        ('M2', f'Farid authored this message in #random. Farid {farid_suffix}. Priya also reacted 👍 to M2.',
         'Wrong author membership channel only' if mode == 'absent' else 'Alternative through Farid’s message' if mode == 'underspecified' else 'Match with unrelated activity', mids['M2']),
        ('M3', 'Priya authored this message in #general. Priya currently belongs only to #general.', 'Wrong author membership channel only', mids['M3']),
        ('M4', 'Owen authored this message in #general. Owen currently belongs to #general and #mentors-lounge, not #mentorship-hub.', 'Wrong author membership channel only; the similarly named channel is distinct', mids['M4']),
        ('M5', 'Lucia authored this message in #general before leaving her channels. Lucia retains workspace membership but currently has no channel memberships.', 'Missing author-to-channel membership relationship', mids['M5']),
        ('M6', 'Theo authored this message in #mentorship-hub before leaving that channel. Theo currently belongs only to #general.', 'Message location does not establish the author’s current membership', mids['M6']),
    ]
    request = ('Add 👀 to the message from a person who is a member of #mentorship-hub.' if mode == 'underspecified'
               else 'Add 👀 to the messages from people who are members of #mentorship-hub.')
    expected = [] if mode == 'absent' else [mids['M2']] if mode == 'single' else [mids['M1'], mids['M2']]
    q = selector(['messages', 'users', 'channel_members', 'channels'],
                 ['messages.user_id', 'channel_members.user_id', 'channel_members.channel_id'],
                 [f(3, 'channel_name', 'mentorship-hub')])
    changes = {
        'multiple': 'Base case: Dana’s and Farid’s messages are jointly intended.',
        'single': 'Remove M1, leaving M2 as the sole qualifying message. Preserve the original plural request and all membership facts.',
        'absent': 'Remove Dana’s and Farid’s #mentorship-hub memberships; retain their #general/#random memberships and every message. The actor has channel access but authors no messages.',
        'underspecified': 'Keep the original environment and ask for the message from a person who is a member. Dana’s and Farid’s messages remain alternatives without a selection rule.',
    }
    return make_entry('W06-base' if mode == 'multiple' else f'W06-{mode}', 'W06', mode, s, request, rows,
                      'Messages whose author currently belongs to #mentorship-hub. Message location and other people’s reactions do not establish the author’s membership. '
                      + ('The singular request does not distinguish Dana’s and Farid’s qualifying messages.' if mode == 'underspecified' else ''),
                      expected, [mid for mid in mids.values() if mid not in expected], q,
                      candidates=[[m] for m in expected] if mode == 'underspecified' else None,
                      computation=[['messages.message_id']], written=['message_reactions.message_id', 'message_reactions.reaction_type'],
                      change=changes[mode], operation={'kind': 'react', 'emoji': 'eyes'})


def build_entries():
    return [w03(m) for m in ('underspecified', 'single', 'multiple', 'absent')] + [
        w04(m) for m in ('absent', 'single', 'multiple', 'underspecified')] + [
        w05(m) for m in ('multiple', 'single', 'absent', 'underspecified')] + [
        w06(m) for m in ('multiple', 'single', 'absent', 'underspecified')]
