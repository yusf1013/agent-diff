"""Render the manually reviewed ambiguity-location contrasts, not solver input."""
import json

from suite_support import story_section


CONTRASTS = [
    ('W01', [('User / reactor', 'W01-underspecified'), ('Message / target', 'W01-underspecified-message')]),
    ('W02', [('User / target reactor', 'W02-underspecified-reactor'), ('Message / announcement', 'W02-underspecified-announcement'), ('Conversation / announcement channel', 'W02-underspecified-channel')]),
    ('W03', [('User / reactor', 'W03-base'), ('Message / announcement', 'W03-underspecified-message'), ('Conversation / target', 'W03-underspecified-channel')]),
    ('W04', [('Message / target', 'W04-underspecified'), ('Reaction / intermediate emoji', 'W04-underspecified-reaction'), ('Conversation / reactor membership channel', 'W04-underspecified-channel')]),
    ('W05', [('Conversation / target', 'W05-underspecified')]),
    ('W06', [('Message / target', 'W06-underspecified'), ('User / author', 'W06-underspecified-author'), ('Conversation / author membership channel', 'W06-underspecified-channel')]),
    ('W07', [('User / Jordan', 'W07-base'), ('Message / announcement', 'W07-underspecified-message'), ('Conversation / removal-channel side branch', 'W07-underspecified-removal-channel')]),
    ('W08', [('Reaction / target', 'W08-underspecified-reaction'), ('Message / source', 'W08-underspecified'), ('Conversation / author membership channel', 'W08-underspecified-channel')]),
    ('W09', [('User / bot', 'W09-underspecified'), ('Conversation / bot membership channel', 'W09-underspecified-channel')]),
    ('W10', [('User / terminal channel member Priya', 'W10-underspecified'), ('Conversation / intermediate channel', 'W10-underspecified-channel'), ('Message / checklist', 'W10-underspecified-message')]),
]


def render(entries):
    new_ids = {entry['case']['case_id'] for entry in entries}
    lines = ['# Manual Slack exemplars — ambiguity locations', '',
             'These **15 additional tests** extend the 42 tests in [story.md](story.md) and [story2.md](story2.md) to **57 full tests**. '
             'There are now **26 underspecified cases**, indexed below. Existing cases are retained; the 15 new stories follow the index.', '',
             'Each case has an unresolved choice whose plausible resolutions produce **different final target sets**. '
             'A choice between intermediate records that converges to the same target set would not establish the intended contrast. '
             'Multiple members of a requested collection are not ambiguity by themselves. '
             'The request does not delegate selection between the competing sets.', '',
             'The same private-label and access conventions as the earlier stories apply. All tables, interpretations and alternatives are withheld from the solver. '
             'Only the ordinary request and instantiated environment are solver inputs.', '',
             '## Contrast index', '',
             '| Family | Ambiguity locations and executable tests | Count |', '|---|---|---:|']
    for family, items in CONTRASTS:
        links = []
        for label, cid in items:
            source = 'story3.md' if cid in new_ids else 'story.md' if cid.endswith('-base') else 'story2.md'
            anchor = family.lower() if source == 'story.md' else cid.lower()
            links.append(f'**{label}**: [story]({source}#{anchor}), [test](cases/{cid}.json)')
        lines.append(f'| {family} | ' + ' · '.join(links) + f' | {len(items)} |')
    lines += ['',
              'W01 has two natural locations, W05 one, and W09 two. We do not force a third location by adding unrelated semantics. '
              'W05 counts all memberships; the individual membership rows are not competing selections. '
              'W09 preserves one displayed workspace association per profile.', '',
              '**W03:** “the budget-approved message” leaves a particular announcement unresolved; '
              '“a budget-approved message” accepts any qualifying announcement as evidence, leaving the target channel unresolved. '
              'These variants intentionally differ in that quantifier; they are not two labels for identical wording.', '',
              '**W04:** the middle variant refers to the emoji on one identified release-date announcement. '
              'Its two reaction emojis select different rollout-checklist messages. This adds a small source reference; '
              'simply dropping the emoji and saying “a reaction” would allow any qualifying reaction and would not isolate the intended Reaction ambiguity.', '',
              '**W07:** the new third variant concerns the channel to remove the established Jordan from. '
              'This is the `Conversation Membership → Conversation` side branch, explicitly recorded in the card. '
              'The announcement channel stays fixed. It replaces the proposed second announcement-channel ambiguity.', '',
              'These are controlled semantic contrasts with the changes listed per case, not a claim that every pair differs in exactly one database cell. '
              'Negatives that become legitimate alternatives are relabeled. Candidate-set unions in private selectors enumerate possible targets; they do not authorize acting on that union.', '',
              '## Additional stories', '']
    for entry in entries:
        section = story_section(entry)
        metadata = entry['ambiguity']
        section = section.replace('**Resolution mode:** underspecified\n',
                                  '**Resolution mode:** underspecified\n\n**Ambiguity location:** ' + metadata['location'] + '\n', 1)
        lines.append(section)
        if metadata['explanation'] != entry['case']['cards'][0]['Grounding obligation description']:
            lines += [metadata['explanation'], '']
        lines += ['| Unresolved choice | Resulting target set |', '|---|---|']
        labels = {json.dumps(row[3], sort_keys=True): row[0] for row in entry['rows']}
        for choice, targets in metadata['choices'].items():
            rendered = ', '.join(labels[json.dumps(target, sort_keys=True)] for target in targets)
            lines.append(f'| {choice} | {{{rendered}}} |')
        cid = entry['case']['case_id']
        lines += ['', f'[Full executable test](cases/{cid}.json)', '']
    return '\n'.join(lines) + '\n'
