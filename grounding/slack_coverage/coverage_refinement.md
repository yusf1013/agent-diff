# Slack coverage refinement

Date: 2026-09-16. Research findings and proposals; no generator, evaluator,
cards, or coverage denominator changed. No external model/service calls were made.

**Follow-up:** The [212-route inclusion review](inclusion_groups.md) is now
complete: 174 retained and 38 excluded for now by the user's whole-group decision. This note
records the preceding rationale; use the linked review for current dispositions.

## Decision carried forward

The user approved moving unsupported capabilities out of exhaustive
route × attribute × resolution-mode coverage. Cover distinct limitations with
simple representative read/write tasks instead. Do not examine or instantiate
all 2,658 affected routes individually.

The mechanical partition remains 2,564 routes touching six entities without
direct API access, 94 additional routes using the unexposed default-channel
setting, and 212 routes avoiding both. The earlier “about 3,000” was rounding
2,870, not a different enumeration. These are structural routes, not test counts.

The other reductions below are proposals, not adopted policy.

## Limitations: a small separate inventory

[Capability audit](capability_limits_audit.md) checks the complete dispatch and
the adopted model's exposure qualifications. Eight initial groups cover named
roles, role assignments, files, stored attachments, stored mentions, edit history,
workspace settings, and user settings. At most one representative read and write
probe per group gives 16 initial slots. A small extension for unavailable fields
and writes on otherwise exposed entities brings the illustrative plan to about
25 probes. This is grouped capability coverage, not exhaustive CRUD coverage.

Required discipline:

1. Identify the unavailable information or requested effect, and check the full
   relevant API surface, including filters and derived responses.
2. Use an ordinary request that actually needs that capability. If supported
   text, blocks, links, or another permitted operation meets the request, allow
   it. Do not invent storage-specific requests merely to fill an inventory slot.
3. For a read probe, place a positive fact in the hidden state without supplying
   its answer in visible context. Lack of access must not masquerade as absence.
4. For a write probe, supply enough target and intent information to isolate the
   missing operation. Check authorized alternatives; message deletion, for
   example, can also delete edit history.
5. Keep read and write coverage separate. Do not multiply either by hidden paths,
   fields, or four resolution modes. Record what each representative actually
   tests; add another only for a distinct limitation or permitted alternative.

These probes can reveal fabricated references or substitutions, but an inability
to perform an unsupported write is not itself a grounding violation. This does
not change the current evaluator's primary grounding-only metric.

## Multiple workspaces are allowed

[Workspace audit](workspace_scope_audit.md) establishes that the schema, seed
loader, and environment cloning permit multiple workspaces. The platform chooses
an actor and template, not a single Slack workspace. The baseline's one-workspace
seed is not a general invariant.

API workspace support is incomplete: actor-wide list/search/create operations
use one membership selected without ordering and ignore documented `team_id`
inputs. Some ID-addressed channel operations can reach a different workspace.
General workspace enumeration and stored workspace-name lookup are unavailable.

Consequently, workspace-dependent routes cannot be removed globally. A fixed
workspace can make a condition constant only within an explicitly declared
candidate scope. General cross-workspace discovery belongs in limitation
coverage where the interface cannot support it; known-ID cross-workspace work is
not automatically impossible.

## What the 212-route review establishes

[Remaining-route audit](remaining_routes_audit.md) reproduces these partitions:

| Endpoint grouping | Routes |
|---|---:|
| Both endpoints Workspace, User, Conversation, or Message | 54 |
| One endpoint an association, the other one of those four | 118 |
| Both endpoints associations | 40 |
| Total | 212 |

Here “association” groups workspace membership, conversation membership, and
reaction for analysis. All remain entities in the adopted model. Their direct
selection can be meaningful, so these categories are not exclusions.

Some terminal attributes remain unavailable: membership join time, reaction
time, last-login time, and stored workspace metadata are examples. They should
receive limitation coverage once, not a hidden-field test for every incoming
route. Conversation membership has no exposed independent scalar identifying
attribute beyond its endpoint identity; existence and counts can be useful but
must not be confused with its unavailable join time.

Exact normalizations include member-count views versus the matching membership
count, and grouped reaction counts versus the corresponding reaction records.
Most such representation aliases were already absent from the diagram. The
review found no large exact-equivalence collapse among the 212 simple routes.

Complete long references such as “messages reacted to by members of #security”
remain meaningful. Contracting association nodes makes the display shorter but
does not remove their selection meaning. Inverse paths, shared endpoints, and
the same fields do not establish equivalence.

The historical enumeration also omits repeated entity types, including message
parent/reply and co-member references. Therefore 212 is a review inventory, not
a certified complete or meaningful coverage denominator.

## Proposed way to avoid the remaining product

Retain complete eligible routes as one coverage dimension. Track identifying
attributes and resolution modes as separate dimensions, rather than requiring
every route × attribute × mode combination.

For example, a test can exercise the complete route from messages through
reactors and memberships to a channel name. Another can exercise channel topic
identification, and another absent handling. This covers those individual
requirements; it does not claim the long route has been tested with topic or in
absent mode. Record observed combinations so those limits remain visible.

This differs from rejected local-composition coverage: a long route receives
credit only from a test using that entire reference, not from separate tests of
its component edges. It also differs from semantic deduplication: distinct
combinations remain distinct, but exhaustive interaction coverage is not the
requirement.

Two possible strengths to discuss:

- Complete-route coverage, separate attribute coverage, and resolution coverage
  per referent entity. Assign modes and attributes across route tests to meet
  multiple requirements naturally. The historical inventory supplies 212 route
  requirements before feasibility review, with additional field/mode requirements;
  this is not a certified bound on cases.
- Complete-route × mode coverage, with attributes tracked separately. The raw
  212-route inventory gives 848 combinations before checking feasibility, without
  multiplying again by all terminal attributes.

The first is the recommended practical option if the campaign must stay around
a few hundred cases. It requires explicit agreement because the coverage claim
is narrower than exhaustive route/attribute/mode interaction coverage. Neither
option authorizes truncating long paths, discarding inconvenient baseline gaps,
or claiming all 212 candidates have already been validated as ordinary requests.
