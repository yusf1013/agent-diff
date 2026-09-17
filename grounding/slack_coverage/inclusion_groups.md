# Slack: decisions after reviewing all 212 routes

All 212 routes have an individual request fragment, selection rule, scope,
API evidence, and inclusion disposition in the [complete review](route_inclusion_review.md).
The [JSON](route_inclusion_review.json) is the canonical manual annotation;
`python grounding/slack_coverage/build_inclusion_review.py` validates and renders it.

**174 routes are retained. The user chose to exclude the other 38 for now.**
The excluded groups have interpretable, API-supported scoped witnesses, preserved
for possible reconsideration. This campaign-scope decision does not label them
impossible, universally meaningless, or equivalent to shorter paths.

## Retained groups

| Group | Routes | Coverage meaning |
|---|---:|---|
| S1 | 64 | Channel, user, message, reaction and channel-membership connections without workspace concepts |
| S2 | 26 | Profile-displayed workspace membership/role, without a Workspace node |
| S3 | 28 | Workspace as channel context, without workspace membership |
| S4 | 34 | Workspace is the requested or identifying endpoint, with workspace membership on the route |
| A | 22 | Direct connection between workspace affiliation and a channel, its contained records, or their directly identified participant |
| **Retained** | **174** | |

Retained examples include “messages reacted to by members of #security”
([R089](route_inclusion_review.md#r089)), “channels containing posts Tom reacted
to” ([R024](route_inclusion_review.md#r024)), and “channels in the workspace
shown on Tom's profile” ([R003](route_inclusion_review.md#r003)). Long references
remain included when their relationship meaning is justified.

## Groups excluded from the current campaign

An internal Workspace connects its two neighboring relationships:
**workspace membership — workspace — channel**. The three excluded groups add
participation or activity on one side of that connection. Grouping uses these
roles, not a path-length threshold.

### B — Affiliated person's channel participation: 6 routes

Connect someone's channel memberships with channels or content in the workspace
shown on that person's profile.

- “Which channels are in the profile-listed workspaces of people who belong to
  three of these review channels?” ([R004](route_inclusion_review.md#r004))
- “List channel memberships for people whose profile-listed workspace contains
  a message with a thumbs-up.” ([R050](route_inclusion_review.md#r050))

The connection through workspace affiliation is defined, but the present
examples need a convincing reason to use that connection instead of requesting
the person's channel participation directly. This is an ordinary-use question,
not a claim that the two queries select the same entities.

### C — Affiliated person's message/reaction activity: 18 routes

Connect someone's posting or reacting activity with channels or content in the
workspace shown on their profile.

- “Which channels are in the profile-listed workspaces of people who posted
  about the launch?” ([R005](route_inclusion_review.md#r005))
- “Find posts by people whose profile-listed workspace has a channel with three
  members.” ([R076](route_inclusion_review.md#r076))

This group contains the example raised in the clarification. Posting/reacting
and workspace affiliation are distinct relationships; the query combines them
without requiring the activity to occur in that workspace's selected channel.
The question is whether to include this whole class of organizational analysis.

### D — Channel participant's additional activity: 14 routes

Starting from a workspace association, reach a channel member, message author,
or reactor, then qualify that participant using another membership or activity.

- “List people and their profile-listed workspaces where a channel member has
  posted about the launch in these histories.”
  ([R186](route_inclusion_review.md#r186))
- “Find posts reacted to by people who belong to channels in a workspace shown
  on an owner's profile in this roster.”
  ([R091](route_inclusion_review.md#r091))

In retained group A, identifying that channel participant finishes that side of
the reference. In D, the participant connects onward to another condition. The
question is whether this additional connection has a sufficiently ordinary use.

## Effect of the decision

The current campaign includes **174 routes**. The scenarios below record the
effect of reconsidering a group later; none is included in the current count.

| Excluded groups reconsidered and accepted | Retained routes |
|---|---:|
| None | 174 |
| B only | 180 |
| C only | 192 |
| D only | 188 |
| All three | 212 |

Groups are additive, so any combination can be chosen. Their complete ID lists
and paired route patterns are in [workspace_bridge_groups.json](workspace_bridge_groups.json).
An inverse direction remains a separate route requirement: grouping it with its
counterpart does not equate the selected referents or grant shared coverage.

## Access qualifications that apply regardless of the decision

- A workspace-membership witness concerns the workspace and owner/admin status
  displayed on the relevant profile. It does not assume the API can enumerate
  every workspace membership or that the returned workspace is primary.
- Cross-workspace examples use an ordinary bounded list of candidate channels
  or contacts with supplied/discoverable handles. The list supplies a candidate
  population, not the selected answer. The identifying condition must still
  distinguish candidates.
- Hidden attribute variants, such as channel-join time or stored workspace name,
  stay in the small limitation suite. A supported route does not expose every
  attribute of its terminal entity.
- Different relationship roles may refer to the same actual record. “Additional
  activity” does not impose an inequality unless the request explicitly does.

This is a manual inclusion review with static API/source checks. It does not
claim that the illustrative requests have already been compiled into valid
benchmark seeds or run against the service. It closes the review of these 212
candidates, not the separate inventory gaps for parent/reply, repeated-type,
direct-attribute, or nested-content references.
