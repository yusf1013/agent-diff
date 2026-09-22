"""Independent seed traversals for the 15 added ambiguity-location cases.

Does not import builders or read private.selector/expected_matches/candidate_sets.
Predicates interpret only the concrete, manually reviewed stories in this suite.
"""
from __future__ import annotations

import re


def alternatives(case):
    """Return independently derived alternative target sets, or None for old cases."""
    cid = case['case_id']
    known = {
        'W01-underspecified-message', 'W02-underspecified-channel',
        'W03-underspecified-message', 'W03-underspecified-channel',
        'W04-underspecified-channel', 'W04-underspecified-reaction',
        'W06-underspecified-author', 'W06-underspecified-channel',
        'W07-underspecified-message', 'W07-underspecified-removal-channel',
        'W08-underspecified-reaction', 'W08-underspecified-channel',
        'W09-underspecified-channel', 'W10-underspecified-channel', 'W10-underspecified-message',
    }
    if cid not in known:
        return None
    data = case['seed']
    users = {u['user_id']: u for u in data['users']}
    channels = {c['channel_id']: c for c in data['channels']}
    messages = {m['message_id']: m for m in data['messages']}
    members, reactions = data['channel_members'], data['message_reactions']

    def norm(text):
        return re.sub(r'[-–—]', ' ', text).casefold()

    def named(uid, first):
        return users[uid]['real_name'].split()[0] == first

    def channel_named(name):
        found = [c['channel_id'] for c in channels.values() if c['channel_name'] == name]
        assert len(found) == 1, f'Expected unique #{name}: {found}'
        return found[0]

    def in_channel(uid, channel):
        return any(m['user_id'] == uid and m['channel_id'] == channel for m in members)

    def topic_channels(topic):
        return [c['channel_id'] for c in channels.values() if topic in norm(c['topic_text'])]

    def about(mid, topic):
        return topic in norm(messages[mid]['message_text'])

    def reaction_handle(r):
        return {k: r[k] for k in ('message_id', 'user_id', 'reaction_type')}

    def membership_handles(uids, channel):
        return [{'channel_id': m['channel_id'], 'user_id': m['user_id']} for m in members
                if m['user_id'] in uids and m['channel_id'] == channel]

    def workspace_handles(uids):
        return [{'user_id': m['user_id'], 'team_id': m['team_id']} for m in data['user_teams']
                if m['user_id'] in uids]

    def reactors(mid, emoji, first=None):
        return {r['user_id'] for r in reactions if r['message_id'] == mid and r['reaction_type'] == emoji
                and (first is None or named(r['user_id'], first))}

    if cid.startswith('W01-'):
        priyas = [uid for uid in users if named(uid, 'Priya')]
        assert len(priyas) == 1
        mids = {r['message_id'] for r in reactions if r['user_id'] == priyas[0] and r['reaction_type'] == 'raised_hands'}
        return [[mid] for mid in sorted(mids)]
    if cid.startswith('W02-'):
        groups = []
        for channel in topic_channels('financial planning'):
            mids = [mid for mid, m in messages.items() if m['channel_id'] == channel and about(mid, 'budget freeze')]
            assert len(mids) == 1
            group = sorted(reactors(mids[0], 'fire'))
            assert len(group) == 1
            groups.append(group)
        return groups
    if cid.startswith('W03-'):
        alex = [uid for uid, u in users.items() if u['real_name'] == 'Alex Rivera']
        assert len(alex) == 1
        mids = {r['message_id'] for r in reactions if r['reaction_type'] == 'tada'
                and r['user_id'] == alex[0] and about(r['message_id'], 'budget approved')}
        if cid.endswith('-message'):
            return [[messages[mid]['channel_id']] for mid in sorted(mids)]
        return [[channel] for channel in sorted({messages[mid]['channel_id'] for mid in mids})]
    if cid.startswith('W04-'):
        if cid.endswith('-channel'):
            pairs = [(c, 'rocket') for c in topic_channels('beta testing')]
        else:
            anchors = [mid for mid in messages if about(mid, 'release date announcement:')]
            assert len(anchors) == 1, 'Reaction ambiguity must have one established source announcement'
            emojis = {r['reaction_type'] for r in reactions if r['message_id'] == anchors[0]}
            assert len(emojis) == 2
            pairs = [(channel_named('beta-testers'), emoji) for emoji in sorted(emojis)]
        groups = []
        for channel, emoji in pairs:
            mids = {r['message_id'] for r in reactions if r['reaction_type'] == emoji
                    and about(r['message_id'], 'rollout checklist') and in_channel(r['user_id'], channel)}
            assert len(mids) == 1, 'Fixing the channel/emoji must establish one rollout-checklist target'
            groups.append(sorted(mids))
        return groups
    if cid == 'W06-underspecified-author':
        channel = channel_named('mentorship-hub')
        authors = [uid for uid in users if named(uid, 'Dana') and in_channel(uid, channel)]
        return [[mid for mid, m in messages.items() if m['user_id'] == uid] for uid in authors]
    if cid == 'W06-underspecified-channel':
        return [[mid for mid, m in messages.items() if in_channel(m['user_id'], channel)]
                for channel in topic_channels('mentorship')]
    if cid.startswith('W07-'):
        announcement_channel = channel_named('announcements')
        mids = [mid for mid, m in messages.items() if m['channel_id'] == announcement_channel and about(mid, 'security audit')]
        if cid.endswith('-message'):
            return [membership_handles(reactors(mid, 'thumbsup', 'Jordan'), channel_named('team-hub')) for mid in mids]
        assert len(mids) == 1
        groups = [membership_handles(reactors(mids[0], 'thumbsup', 'Jordan'), c) for c in topic_channels('team coordination')]
        assert len({m['user_id'] for group in groups for m in group}) == 1, 'Removal-channel choice must keep Jordan fixed'
        return groups
    if cid.startswith('W08-'):
        def targets(channel, emoji=None):
            return [reaction_handle(r) for r in reactions if r['user_id'] == case['acting_user_id']
                    and (emoji is None or r['reaction_type'] == emoji)
                    and in_channel(messages[r['message_id']]['user_id'], channel)]
        channels_about_launch = topic_channels('launch readiness')
        if cid.endswith('-reaction'):
            assert len(channels_about_launch) == 1
            matches = targets(channels_about_launch[0])
            assert len({r['message_id'] for r in matches}) == 1
            return [[r] for r in matches]
        groups = [targets(c, 'fire') for c in channels_about_launch]
        assert all(len(g) == 1 for g in groups)
        return groups
    if cid.startswith('W09-'):
        groups = []
        for channel in topic_channels('incident response'):
            bots = [uid for uid, user in users.items() if user['is_bot'] and in_channel(uid, channel)]
            assert len(bots) == 1
            groups.append(sorted({m['team_id'] for m in data['user_teams'] if m['user_id'] == bots[0]}))
        return groups
    if cid.startswith('W10-'):
        priyas = [uid for uid in users if named(uid, 'Priya')]
        assert len(priyas) == 1
        cs = {m['channel_id'] for m in members if m['user_id'] == priyas[0]}
        mids = [mid for mid, m in messages.items() if m['channel_id'] in cs and about(mid, 'launch checklist')]
        if cid.endswith('-message'):
            assert len(cs) == 1
            return [workspace_handles(reactors(mid, 'rocket')) for mid in mids]
        groups = []
        for channel in sorted(cs):
            local = [mid for mid in mids if messages[mid]['channel_id'] == channel]
            assert len(local) == 1
            groups.append(workspace_handles(reactors(local[0], 'rocket')))
        return groups
    raise AssertionError(cid)
