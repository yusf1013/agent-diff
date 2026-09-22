"""Independent checks for the manually authored W01–W10 family.

This module never reads or evaluates private.selector. Its joins, interpretations,
and fixed story invariants were written separately from the case builders. Topic
tests apply to the manually reviewed concrete message texts in this suite, not to
arbitrary natural language. Passing does not establish API accessibility or test
difficulty; native observations and semantic review remain separate evidence.
"""
from __future__ import annotations

import json
import re
from pathlib import Path


ROOTS = {
    'W01': 'messages', 'W02': 'users', 'W03': 'channels', 'W04': 'messages',
    'W05': 'channels', 'W06': 'messages', 'W07': 'channel_members',
    'W08': 'message_reactions', 'W09': 'teams', 'W10': 'user_teams',
}
PK = {
    'messages': ('message_id',), 'users': ('user_id',), 'channels': ('channel_id',),
    'channel_members': ('channel_id', 'user_id'),
    'message_reactions': ('message_id', 'user_id', 'reaction_type'),
    'teams': ('team_id',), 'user_teams': ('user_id', 'team_id'),
}


def freeze(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False)


def handle(table, row):
    fields = PK[table]
    return row[fields[0]] if len(fields) == 1 else {field: row[field] for field in fields}


def normalized(text):
    return re.sub(r'[-–—]', ' ', text).casefold()


def first_name(user, name):
    return user['real_name'].split()[0].casefold() == name.casefold()


def recompute(case):
    """Return independently matched native root handles, without the selector."""
    family = case['private']['base_story']
    seed, prompt = case['seed'], case['prompt']
    users = {row['user_id']: row for row in seed['users']}
    channels = {row['channel_id']: row for row in seed['channels']}
    messages = {row['message_id']: row for row in seed['messages']}
    reactions, memberships = seed['message_reactions'], seed['channel_members']

    def belongs(uid, name=None, topic=None):
        return any(m['user_id'] == uid
                   and (name is None or channels[m['channel_id']]['channel_name'] == name)
                   and (topic is None or topic in normalized(channels[m['channel_id']].get('topic_text', '')))
                   for m in memberships)

    def about(mid, topic):
        return topic in normalized(messages[mid]['message_text'])

    def in_channel(mid, name):
        return channels[messages[mid]['channel_id']]['channel_name'] == name

    if family == 'W01':
        result = {r['message_id'] for r in reactions
                  if r['reaction_type'] == 'raised_hands' and first_name(users[r['user_id']], 'Priya')}
        return sorted(result)
    if family == 'W02':
        return sorted({r['user_id'] for r in reactions if r['reaction_type'] == 'fire'
                       and about(r['message_id'], 'budget freeze') and in_channel(r['message_id'], 'finance')})
    if family == 'W03':
        def named_alex(uid):
            name = users[uid]['real_name']
            return name == 'Alex Rivera' if 'Alex Rivera' in prompt else first_name(users[uid], 'Alex')
        return sorted({messages[r['message_id']]['channel_id'] for r in reactions
                       if r['reaction_type'] == 'tada' and named_alex(r['user_id'])
                       and about(r['message_id'], 'budget approved')})
    if family == 'W04':
        return sorted({r['message_id'] for r in reactions if r['reaction_type'] == 'rocket'
                       and about(r['message_id'], 'rollout checklist') and belongs(r['user_id'], name='beta-testers')})
    if family == 'W05':
        return sorted(c['channel_id'] for c in channels.values()
                      if 'onboarding' in normalized(c.get('topic_text', '') + ' ' + c.get('purpose_text', ''))
                      and sum(m['channel_id'] == c['channel_id'] for m in memberships) == 6)
    if family == 'W06':
        return sorted(m['message_id'] for m in messages.values() if belongs(m['user_id'], name='mentorship-hub'))
    if family == 'W07':
        requested_channel = re.search(r'Remove from #([^ ]+)', prompt).group(1)
        eligible_users = {r['user_id'] for r in reactions if r['reaction_type'] == 'thumbsup'
                          and first_name(users[r['user_id']], 'Jordan')
                          and about(r['message_id'], 'security audit') and in_channel(r['message_id'], 'announcements')}
        # Some variants can identify a full name; keep that supplied restriction.
        specified = [u['user_id'] for u in users.values() if u['real_name'] in prompt]
        if specified:
            eligible_users.intersection_update(specified)
        return [handle('channel_members', m) for m in memberships
                if channels[m['channel_id']]['channel_name'] == requested_channel and m['user_id'] in eligible_users]
    if family == 'W08':
        return [handle('message_reactions', r) for r in reactions
                if r['reaction_type'] == 'fire' and r['user_id'] == case['acting_user_id']
                and belongs(messages[r['message_id']]['user_id'], topic='launch readiness')]
    if family == 'W09':
        eligible_users = {uid for uid, u in users.items() if u.get('is_bot') and belongs(uid, name='incident-response')}
        return sorted({m['team_id'] for m in seed['user_teams'] if m['user_id'] in eligible_users})
    if family == 'W10':
        priya_channels = {m['channel_id'] for m in memberships if first_name(users[m['user_id']], 'Priya')}
        eligible_users = {r['user_id'] for r in reactions if r['reaction_type'] == 'rocket'
                          and about(r['message_id'], 'launch checklist')
                          and messages[r['message_id']]['channel_id'] in priya_channels}
        return [handle('user_teams', m) for m in seed['user_teams'] if m['user_id'] in eligible_users]
    raise ValueError(f'Unknown manual family {family}')


def audit(case) -> list[str]:
    """Check manual intent, fixed source facts, and independently joined roots."""
    errors = []
    family, seed, private = case['private']['base_story'], case['seed'], case['private']
    root = ROOTS[family]
    actual = {freeze(h) for h in recompute(case)}
    expected = {freeze(h) for h in private['expected_matches']}
    if actual != expected:
        errors.append(f'Independent {family} traversal differs: actual={sorted(actual)}, expected={sorted(expected)}')
    roots = {freeze(handle(root, row)) for row in seed[root]}
    bindings = private.get('row_bindings', [])
    seen = set()
    for binding in bindings:
        marker = freeze(binding['handle'])
        if marker not in roots:
            errors.append(f'Story row {binding["label"]} has no existing {root} root')
        if marker in seen:
            errors.append(f'Different story rows share the same root: {binding["label"]}')
        seen.add(marker)
    if not actual <= seen:
        errors.append('Seed introduces a matching root outside the story table')
    for negative in private['near_misses']:
        marker = freeze(negative)
        if marker not in roots or marker in actual:
            errors.append(f'Negative is not an existing nonmatching root: {negative!r}')

    mode = private['mode']
    if mode == 'single' and len(actual) != 1:
        errors.append('Single mode must have one concrete root in this suite')
    if mode == 'absent' and actual:
        errors.append('Absent mode has a complete match')
    if mode == 'underspecified':
        candidates = private['candidate_sets']
        sets = [frozenset(freeze(v) for v in group) for group in candidates]
        if len(sets) < 2 or len(set(sets)) != len(sets) or not all(sets):
            errors.append('Underspecified candidate sets must be nonempty and distinct')
        if set().union(*sets) != actual:
            errors.append('Underspecified alternatives do not cover the eligible roots')
        if family == 'W01':
            # Priya's plural messages form one collection per possible identity.
            users = {u['user_id']: u for u in seed['users']}
            independently_grouped = {
                frozenset(freeze(r['message_id']) for r in seed['message_reactions']
                          if r['user_id'] == uid and r['reaction_type'] == 'raised_hands')
                for uid, u in users.items() if first_name(u, 'Priya')}
            if set(sets) != independently_grouped:
                errors.append('W01 alternatives do not correspond to the two Priya identities')
            if case['cards'][0]['Referent set']['selection'] != 'set(messages)':
                errors.append('W01 ambiguity concerns a message collection, not one(message)')
        if family == 'W10':
            users = {u['user_id']: u for u in seed['users']}
            messages = {m['message_id']: m for m in seed['messages']}
            independently_grouped = set()
            for uid, user in users.items():
                if not first_name(user, 'Priya'):
                    continue
                channels = {m['channel_id'] for m in seed['channel_members'] if m['user_id'] == uid}
                reactors = {r['user_id'] for r in seed['message_reactions']
                            if r['reaction_type'] == 'rocket'
                            and messages[r['message_id']]['channel_id'] in channels
                            and 'launch checklist' in normalized(messages[r['message_id']]['message_text'])}
                independently_grouped.add(frozenset(freeze(handle('user_teams', m))
                                                    for m in seed['user_teams'] if m['user_id'] in reactors))
            if set(sets) != independently_grouped:
                errors.append('W10 alternatives do not preserve the separate Priya-defined collections')
            if case['cards'][0]['Referent set']['selection'] != 'set(user_teams)':
                errors.append('W10 ambiguity concerns a membership collection, not one(membership)')

    users = {u['user_id']: u for u in seed['users']}
    channels = {c['channel_id']: c for c in seed['channels']}
    members = seed['channel_members']

    def member_names(uid):
        return {channels[m['channel_id']]['channel_name'] for m in members if m['user_id'] == uid}

    def named_first(name):
        return [uid for uid, u in users.items() if first_name(u, name)]

    # Every scenario channel is intentionally readable without an access repair.
    for cid in channels:
        if not any(m['user_id'] == case['acting_user_id'] and m['channel_id'] == cid for m in members):
            errors.append(f'Actor lacks story-promised channel access: {cid}')
    if family == 'W06':
        for uid in named_first('Lucia'):
            if member_names(uid):
                errors.append('W06 changed Lucia’s missing membership relationship')
        for name, required in [('Theo', {'general'}), ('Priya', {'general'}), ('Owen', {'general', 'mentors-lounge'})]:
            for uid in named_first(name):
                if member_names(uid) != required:
                    errors.append(f'W06 changed {name}’s fixed current memberships')
    if family == 'W08':
        for uid in named_first('Elena'):
            if member_names(uid) != {'marketing-updates'}:
                errors.append('W08 changed Elena’s fixed current memberships')
        for uid in named_first('Priya'):
            if member_names(uid) != {'general', 'design-crew'}:
                errors.append('W08 changed Priya’s fixed current memberships')
    if family in ('W09', 'W10'):
        for uid in users:
            if sum(row['user_id'] == uid for row in seed['user_teams']) != 1:
                errors.append(f'{family} requires one displayed workspace association per user: {uid}')
        if family == 'W09' and users[case['acting_user_id']].get('is_bot'):
            errors.append('W09 actor must not become an accidental bot match')
        for group in case['cards'][0]['Answer-computation attributes']:
            if 'teams.team_name' in group:
                errors.append('Workspace names are not exposed by the profile API')
    if family == 'W10':
        # Owner status implies admin status in the runtime projection.
        facts = private.get('reference_outcome', {}).get('answer_facts', [])
        for fact in facts:
            if isinstance(fact, dict) and fact.get('is_owner') is True and fact.get('is_admin') is False:
                errors.append('Owner answer incorrectly denies admin status')
            if isinstance(fact, dict) and 'user_id' in fact:
                memberships = [m for m in seed['user_teams'] if m['user_id'] == fact['user_id']]
                if len(memberships) == 1:
                    role = memberships[0]['role']
                    if fact.get('is_admin') != (role in {'admin', 'owner'}) or fact.get('is_owner') != (role == 'owner'):
                        errors.append(f'W10 answer facts disagree with the displayed role for {fact["user_id"]}')
    for message in seed['messages']:
        text = message['message_text'].casefold()
        for giveaway in ('do not reply', "don't reply", 'no action needed', 'negative example', 'decoy', 'test case'):
            if giveaway in text:
                errors.append(f'Message contains a test-role/action giveaway: {message["message_id"]}: {giveaway}')
    return errors


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path, help='One case.json, or a directory containing case.json files')
    args = parser.parse_args()
    paths = [args.path] if args.path.is_file() else sorted(args.path.glob('*.json'))
    results = [{'case': str(path), 'errors': audit(json.loads(path.read_text()))} for path in paths]
    print(json.dumps(results, ensure_ascii=False, indent=2))
    raise SystemExit(any(r['errors'] for r in results) or not results)


if __name__ == '__main__':
    main()
