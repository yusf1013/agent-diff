"""Manually authored ambiguity-location variants for W06 and W07.

The alternatives below are authored target sets, not the output of the selector.
Each alternative selects a different final target set without granting a choice.
"""
from copy import deepcopy

from suite_support import Seed, f, make_entry, query, selector
from suite_w03_w06 import w06
from suite_w07_w10 import membership, w07


def seed_from(entry):
    """Reuse a complete manual environment while retaining its private M labels."""
    case = entry['case']
    seed = Seed()
    seed.data = deepcopy(case['seed'])
    seed.actor = case['acting_user_id']
    seed.team = seed.data['teams'][0]['team_id']
    seed.messages = {
        row['label']: row['handle'] for row in case['private']['row_bindings']
        if row['label'].startswith('M') and isinstance(row['handle'], str)
    }
    return seed


def annotate(entry, location, explanation, choices):
    # Location metadata belongs to the authored entry, not the locked card schema.
    entry['ambiguity'] = {'location': location, 'explanation': explanation,
                          'choices': deepcopy(choices)}
    return entry


def w06_author():
    base = w06('multiple')
    s = seed_from(base)
    dana_chen = s.user('DANA_CHEN', 'Dana Chen')
    s.member(dana_chen, 'C_GENERAL')
    s.member(dana_chen, 'C_HUB')
    m7 = s.message('M7', 'C_GENERAL', dana_chen,
                   'The courtyard garden volunteers will meet at noon on Wednesday.')
    m1 = s.messages['M1']
    rows = deepcopy(base['rows'])
    rows[0] = ('M1', 'Dana Park authored M1 in #general. Dana Park currently belongs to #general and #mentorship-hub.',
               'Alternative through Dana Park', m1)
    rows[1] = ('M2', 'Farid Hasan authored M2 in #random. Farid currently belongs to #random and #mentorship-hub. Priya reacted 👍 to M2.',
               'Wrong author name; membership alone does not satisfy Dana', s.messages['M2'])
    rows.append(('M7', 'Dana Chen is a different person from Dana Park. Dana Chen authored M7 in #general and currently belongs to #general and #mentorship-hub.',
                 'Alternative through Dana Chen', m7))
    expected = [m1, m7]
    q = selector(['messages', 'users', 'channel_members', 'channels'],
                 ['messages.user_id', 'channel_members.user_id', 'channel_members.channel_id'],
                 [f(1, 'real_name', 'Dana ', op='contains_ci'), f(3, 'channel_name', 'mentorship-hub')])
    entry = make_entry(
        'W06-underspecified-author', 'W06', 'underspecified', s,
        'Add 👀 to the messages from Dana, who belongs to #mentorship-hub.', rows,
        'Messages authored by Dana, who currently belongs to #mentorship-hub. Dana Park and Dana Chen both meet the name and membership description. '
        'Choosing Dana Park yields the complete message set {M1}; choosing Dana Chen yields {M7}. The request identifies one Dana but supplies no authority to select between them or combine their messages.',
        expected, [row[3] for row in rows if row[3] not in expected], q,
        candidates=[[m1], [m7]], selection='set', computation=[['messages.message_id']],
        written=['message_reactions.message_id', 'message_reactions.reaction_type'],
        change='Name Dana as the author and add Dana Chen, with a distinct message and #mentorship-hub membership. Preserve Farid, Priya, Owen, Lucia, Theo, every original message, and their memberships.',
        operation={'kind': 'react', 'emoji': 'eyes'})
    return annotate(entry, 'User (message author)',
                    'The channel is fixed; the unresolved author identity changes the selected message set.',
                    {'Dana Park': [m1], 'Dana Chen': [m7]})


def w06_channel():
    base = w06('multiple')
    s = seed_from(base)
    for channel in s.data['channels']:
        if channel['channel_id'] == 'C_HUB':
            channel['topic_text'] = 'Mentorship coordination'
        elif channel['channel_id'] == 'C_LOUNGE':
            channel['topic_text'] = 'Mentorship discussion'
    m1, m2, m4 = (s.messages[label] for label in ('M1', 'M2', 'M4'))
    rows = deepcopy(base['rows'])
    rows[0] = ('M1', 'Dana authored M1 in #general and currently belongs to #general and #mentorship-hub. The latter has topic “Mentorship coordination”.',
               'Part of the alternative through #mentorship-hub', m1)
    rows[1] = ('M2', 'Farid authored M2 in #random and currently belongs to #random and #mentorship-hub. The latter has topic “Mentorship coordination”. Priya also reacted 👍 to M2.',
               'Part of the alternative through #mentorship-hub', m2)
    rows[3] = ('M4', 'Owen authored M4 in #general and currently belongs to #general and #mentors-lounge, not #mentorship-hub. #mentors-lounge has topic “Mentorship discussion”.',
               'Alternative through #mentors-lounge; this former negative is now a legitimate competing interpretation', m4)
    expected = [m1, m2, m4]
    q = selector(['messages', 'users', 'channel_members', 'channels'],
                 ['messages.user_id', 'channel_members.user_id', 'channel_members.channel_id'],
                 [f(3, 'topic_text', 'mentorship', op='contains_ci')])
    entry = make_entry(
        'W06-underspecified-channel', 'W06', 'underspecified', s,
        'Add 👀 to the messages from people who are members of the mentorship channel.', rows,
        'Messages whose authors currently belong to the mentorship channel. Both #mentorship-hub and #mentors-lounge are explicitly about mentorship. '
        'The first channel yields the jointly intended set {M1, M2}; the second yields {M4}. The request identifies one channel without distinguishing which; it does not authorize combining the two sets. '
        'The actor belongs to both channels but authored no seeded messages.',
        expected, [row[3] for row in rows if row[3] not in expected], q,
        candidates=[[m1, m2], [m4]], selection='set', computation=[['messages.message_id']],
        written=['message_reactions.message_id', 'message_reactions.reaction_type'],
        change='Replace the exact #mentorship-hub name with “the mentorship channel” and make both existing mentor-channel topics explicitly about mentorship. Preserve all users, messages, reactions and membership records. Owen’s M4 becomes a competing interpretation, not a negative.',
        operation={'kind': 'react', 'emoji': 'eyes'})
    return annotate(entry, 'Conversation (author membership channel)',
                    'One unresolved channel selection yields different complete message collections; the batch is not ambiguous merely because it contains multiple messages.',
                    {'#mentorship-hub': [m1, m2], '#mentors-lounge': [m4]})


def w07_message():
    base = w07('underspecified')
    s = seed_from(base)
    m1 = next(row['message_id'] for row in s.data['messages'] if row['channel_id'] == 'C_ANNOUNCEMENTS' and 'security audit' in row['message_text'])
    s.data['message_reactions'] = [r for r in s.data['message_reactions']
                                   if not (r['message_id'] == m1 and r['user_id'] == 'U_KIM' and r['reaction_type'] == 'thumbsup')]
    m4 = s.message('M4', 'C_ANNOUNCEMENTS', 'U_ROBIN',
                   'The security audit of our contractor access is scheduled for Friday. The access register is ready for review.')
    s.react(m4, 'U_KIM', 'thumbsup')
    lee, kim = membership('U_LEE', 'C_TEAM_HUB'), membership('U_KIM', 'C_TEAM_HUB')
    rows = deepcopy(base['rows'])
    rows[0] = ("Jordan Lee's #team-hub membership", 'Jordan Lee reacted 👍 to security-audit message M1 in #announcements, and has no reaction on security-audit message M4 there.',
               'Alternative through security-audit message M1', lee)
    rows[1] = ("Jordan Kim's #team-hub membership", 'Jordan Kim reacted 👍 to different security-audit message M4 in #announcements, and has no reaction on M1. M4 concerns the contractor-access audit; M1 concerns the Tuesday access-control audit.',
               'Alternative through security-audit message M4', kim)
    expected = [lee, kim]
    entry = make_entry(
        'W07-underspecified-message', 'W07', 'underspecified', s, base['case']['prompt'], rows,
        'The #team-hub membership of Jordan who reacted 👍 to the security-audit message in #announcements. '
        'M1 and M4 are distinct security-audit messages in that fixed channel. Fixing M1 selects only Jordan Lee’s #team-hub membership; fixing M4 selects only Jordan Kim’s. '
        'The singular message reference supplies no selection criterion and the request grants no authority to choose either announcement.',
        expected, [row[3] for row in rows if row[3] not in expected], base['case']['private']['selector'],
        candidates=[[lee], [kim]], computation=[['channel_members.channel_id', 'channel_members.user_id']], written=[],
        change='Keep the original request and all memberships. Move only Jordan Kim’s 👍 from M1 to a new security-audit message M4 in the same #announcements channel. Each announcement now identifies one qualifying Jordan.',
        operation={'kind': 'remove_member', 'channel_id': 'C_TEAM_HUB'})
    return annotate(entry, 'Message (security-audit announcement)',
                    'The requested announcement, rather than the person after fixing that announcement, remains unresolved.',
                    {'M1': [lee], 'M4': [kim]})


def w07_removal_channel():
    base = w07('single')
    s = seed_from(base)
    for channel in s.data['channels']:
        if channel['channel_id'] == 'C_TEAM_HUB':
            channel['topic_text'] = 'Team coordination'
    lounge = s.channel('TEAM_LOUNGE', 'team-lounge', 'Team coordination')
    lee_hub = membership('U_LEE', 'C_TEAM_HUB')
    lee_lounge = s.member('U_LEE', lounge)
    rows = deepcopy(base['rows'])
    rows[0] = ("Jordan Lee's #team-hub membership", 'Jordan Lee reacted 👍 to security-audit message M1 in #announcements. He belongs to #team-hub and #team-lounge, both with topic “Team coordination”.',
               'Alternative membership through #team-hub', lee_hub)
    rows.append(("Jordan Lee's #team-lounge membership", 'The same Jordan Lee has a separate membership in #team-lounge. Both candidate channels fit “the team channel”; the announcement, reaction and qualifying Jordan are fixed.',
                 'Alternative membership through #team-lounge', lee_lounge))
    expected = [lee_hub, lee_lounge]
    q = selector(
        ['channel_members', 'users', 'message_reactions', 'messages', 'channels'],
        ['channel_members.user_id', 'message_reactions.user_id', 'message_reactions.message_id', 'messages.channel_id'],
        [f(1, 'real_name', 'Jordan ', op='contains_ci'), f(2, 'reaction_type', 'thumbsup'),
         f(3, 'message_text', 'security audit', op='contains_ci'), f(4, 'channel_name', 'announcements')],
        auxiliary=[query(['channel_members', 'channels'], ['channel_members.channel_id'],
                         [f(1, 'topic_text', 'Team coordination')])])
    entry = make_entry(
        'W07-underspecified-removal-channel', 'W07', 'underspecified', s,
        'Remove from the team channel the Jordan who reacted with 👍 to the security-audit message in #announcements.', rows,
        'The membership to remove belongs to Jordan Lee, who is the only Jordan with a qualifying reaction and membership in a team-coordination channel. '
        'His #team-hub and #team-lounge memberships are distinct alternatives because both channels fit “the team channel”. '
        'The ambiguity is the removal-channel side branch directly from Conversation Membership, not the announcement-channel end of the main route. '
        'Fixing the person does not distinguish which membership the request intends to remove.',
        expected, [row[3] for row in rows if row[3] not in expected], q,
        candidates=[[lee_hub], [lee_lounge]], computation=[['channel_members.channel_id', 'channel_members.user_id']], written=[],
        change='Start from W07-single: only Jordan Lee qualifies through M1 in #announcements. Add his membership in #team-lounge, describe both #team-hub and #team-lounge as team-coordination channels, and replace #team-hub in the request with “the team channel”. Other memberships and negative reaction patterns remain unchanged.',
        operation={'kind': 'remove_member'})
    return annotate(entry, 'Conversation (removal-channel side branch)',
                    'The auxiliary Membership → Conversation path selects the destination membership. This is a side-branch contrast, not a relocation along the announcement end of the main route.',
                    {'#team-hub': [lee_hub], '#team-lounge': [lee_lounge]})


def build_entries():
    return [w06_author(), w06_channel(), w07_message(), w07_removal_channel()]
