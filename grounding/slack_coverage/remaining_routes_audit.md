# Remaining Slack route audit

Read-only analysis of the adopted model and `grounding/slack_coverage/route_probe.py`.
No solver/model calls. These are structural route counts, not feasibility judgments.

**Follow-up:** [Individual inclusion review](route_inclusion_review.md) now
accounts for all 212 routes; [group decisions](inclusion_groups.md) summarize
174 retained routes and 38 excluded for now by the user's whole-group decision.

[remaining_route_probe.py](remaining_route_probe.py) reproduces the statistics
and lists all 212 candidates in [remaining_route_probe.json](remaining_route_probe.json).

## Reproduced counts

After removing routes touching the six no-direct-API entity flags and the default-conversation setting edge, the historical simple-entity-type enumeration has **212 directed routes** over Workspace, User, Conversation, Message, Workspace membership, Conversation membership, and Reaction. It still excludes the Message self-parent relation and useful repeated-type co-membership patterns.

| Endpoint types | Directed routes |
|---|---:|
| Both ordinary entity endpoints (Workspace/User/Conversation/Message) | 54 |
| Ordinary entity to association endpoint | 59 |
| Association endpoint to ordinary entity | 59 |
| Both association endpoints | 40 |

“Association” here is only a diagnostic grouping of Workspace membership, Conversation membership, and Reaction; it does not amend the adopted ER model. **99** routes therefore begin at an association entity. Those 99 are not semantically redundant merely because their referents are associations.

Of the 54 ordinary-to-ordinary routes, contracting internal degree-two association nodes for display yields 12 one-relation, 22 two-relation, and 20 three-relation routes. Contraction changes displayed depth, not the 54 distinct candidate meanings.

Traversing an edge from its one side to its many side is a potential fan-out:

| Number of potential fan-outs in complete route | Routes |
|---|---:|
| 0 | 14 |
| 1 | 74 |
| 2 | 76 |
| 3 | 39 |
| 4 | 9 |

The 14 zero-fan-out routes are ordinary projections such as Message → author User, Reaction → Message → Conversation, and Conversation membership → Conversation → Workspace. They can still select multiple root records through a shared attribute. Fan-out count is not a resolution mode.

## Ordinary long fragments remain distinct

| Route | Ordinary identifying fragment |
|---|---|
| Message → User → Conversation membership → Conversation | Messages written by members of #security |
| Message → Reaction → User → Conversation membership → Conversation | Messages reacted to by members of #security |
| Conversation → Message → Reaction → User | Channels containing messages Tom reacted to |
| Reaction → Message → User | Reactions to messages Tom wrote |
| Conversation membership → Conversation → Message → User | Memberships in channels where Tom posted |

The last fragment can occur in a report about memberships or a batch operation over memberships. It should not be ruled meaningless merely because it is less common than identifying messages. A mutation task would also need an actor/user qualifier where the request's intended scope requires one.

The desired reaction/member long path has **two** potential fan-outs. Thus “at most one fan-out” would exclude an explicitly desired ordinary case. Larger fan-out counts can indicate nested population expansion, but do not establish meaninglessness.

## What can actually be normalized

1. Foreign-key identity checks and referenced-entity ID checks describe the same endpoint constraint. Identifiers are already mapped to relationships rather than repeated ordinary attributes in model lines 35–38.
2. Search-match wrappers and profile wrappers do not add independent identities or relationship paths (model 128–140).
3. API member count and count of Conversation membership rows are the same derived quantity. Since the pair key is unique, count of distinct users **within one fixed conversation** agrees as well. This equivalence need not survive moving aggregation outside the conversation grouping.
4. A Reaction summary's count for one fixed message and emoji agrees with count of matching Reaction rows. Triple-key identity supplies distinct-user agreement within that grouping.
5. If an association is specified entirely by its endpoint identities (and emoji for Reaction), its independent ID lookup is not another lookup mechanism. But changing the referent from association to endpoint changes the output and must not silently merge root coverage.
6. A total mandatory to-one relationship used only to assert endpoint existence imposes no further selection. Likewise, a relation branch with a predicate already entailed by stated scope can be removed **for that scope**. An attribute of that endpoint is generally not redundant.

Most of these normalize attributes, endpoint identities, or derived views. They do not identify large equivalence classes among the 212 already canonical simple paths.

## Unsafe proposed reductions

- **Reverse paths are not duplicate reference selections.** User → authored Message and Message → author User can expose the same relation tuples, but select different kinds of entities. Their one/many behavior also differs.
- **Same root and endpoint are insufficient.** Message → User and Message → Reaction → User distinguish author from reactor.
- **Association contraction is not elimination.** Membership and Reaction have pair/triple identities, attributes, and legitimate direct requested operations. Preserve qualifiers and aggregation scope when writing them as semantic relationships.
- **The same set of fields read is not selection equivalence.** Direction, projection, role, quantifiers, and same-witness binding affect outputs.
- **Predicate agreement in the seed is not a domain equivalence.** Two routes may agree accidentally; all absent selections are empty. Candidate sets for ambiguity must also be preserved, not just their union.
- **Repeated types are not necessarily redundant.** Co-members and parent/reply references can require them. The historical no-repeated-type rule is not itself a completeness argument.
- **No direct API access is not a proved read/write failure.** Indirect observations and authorized alternate effects must be considered. Fields on otherwise exposed entities may also be inaccessible.

Model qualifications at 96–115 specifically prohibit assuming workspace-membership consistency, equivalence of roles, fixed participant counts, or uploader meaning. Structured-value caveats at 119–126 prohibit equating embedded identifiers with stored mentions or attachments.

## A different way to avoid the Cartesian product

A coverage report can require **each complete eligible route** to occur in a test, plus coverage of identifying attributes and resolution modes, without demanding every route × terminal attribute × mode combination. This preserves complete long-route evaluation and is **not local-segment coverage**.

For example, one route test can exercise Messages → Reaction → User → Conversation membership → Conversation.name in multiple mode. Other tests may exercise Conversation.topic and absent handling. This does not cover that long route using topic, nor that long route in absent mode; those untested interactions must not be claimed.

Two defensible granularities are:

- Separate complete-route, attribute, and mode coverage, with their observed combinations reported descriptively.
- Complete-route × mode coverage, while attribute coverage is tracked independently. For 212 candidate routes this is an upper raw product of 848 route-mode cells before feasibility and hidden-field qualification, rather than multiplying again by every terminal attribute.

This is a declared interaction-coverage choice, **not semantic redundancy**. It is potentially a practical answer to the tens-of-thousands concern, but it changes the original entity/path/attribute/mode denominator and needs explicit agreement. It must not be sold as exhaustive coverage of all identifying combinations.

## Conclusion

The API-limitation partition may remove substantial combinatorial duplication of capability failures, subject to proof. Within the remaining graph, exact semantic equivalence is a much smaller reduction. The model intentionally preserves independent relations, so many ordinary complete paths are distinguishable in valid environments. Do not force a small number by calling them equivalent.

The promising options are (a) semantic alias normalization and field-level feasibility, (b) separately defined capability-limitation families, and (c) avoiding the terminal-attribute Cartesian product while retaining complete-route coverage. None requires truncating useful long paths or claiming that local subpaths certify them.
