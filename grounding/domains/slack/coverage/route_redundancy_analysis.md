# Complete identifying routes: redundancy investigation

Date: 2026-09-16. **Research notes for discussion, not an adopted coverage rule.** The source is the adopted [Slack conceptual model](../model.md) and its [ledger](../model_source_ledger.md). No changes to that model, cards, evaluator, or generation policy are proposed as completed work here. The earlier provisional entity inventory and local-composition coverage proposal are superseded as directions for defining the denominator.

## 1. What was investigated

Re-enumerated every route under the previous diagnostic's rule: start at each diagram node; traverse each relationship in either direction; preserve distinct relationship roles; do not repeat an entity type. This produces 2,870 routes from 13 nodes and 20 relationships. The self-parent Message relationship is excluded by that rule. These are neither cells nor validated request families. Attributes, modes, derived Thread paths, nested content, and useful repeated-type paths are not included.

[route_probe.py](route_probe.py) reproduces the counts in [route_probe.json](route_probe.json). The traversal is mechanical; interpretation of its partitions and the examples below is manual analysis.

| Structural partition | Routes |
|---|---:|
| Touches Named role, Role assignment, File, File attachment, User mention, or Message edit record | 2,564 |
| Avoids those six but traverses the default-conversation settings relationship | 94 |
| Avoids both groups | 212 |
| Total | 2,870 |

The six entities are explicitly documented as having no direct API access (D06, D08, D10, D12, D14, D15). The default-conversation setting is likewise unexposed (D09). This is a topological partition, not proof that each corresponding task is impossible or that the remaining 212 routes are fully observable. For example, an attribute on a visible entity can still be unavailable. Write effects and permissible alternatives require their own check.

Separately, 2,188 routes touch Workspace. Of the 212-route remainder, 60 have Workspace internally, 62 have it as an endpoint, and 90 avoid it. These are not automatic exclusion categories.

## 2. The closest analogue to equivalent read/write workflows

For reference selection, normalize the query's **referent, scope, relationship roles, predicates, quantifiers, witness bindings, and permitted selections**. Two formulations are genuinely redundant when they permit the same referent selections for every environment admitted by that scope, with the same parameters and selection authority.

Do not compare only the answers in the present seed: otherwise every absent reference becomes equivalent to every other empty query. Nor is a shared set of fields sufficient. Authorship and reaction paths can both use User.real_name yet select different messages.

Preserve collection/choice distinctions: selecting both Alexes as a determined collection differs from an unresolved choice between two singleton candidate sets, even though their unions coincide. Preserve counts of association records versus distinct endpoints, and whether multiple conditions must hold on the same related record.

### Genuine normalizations supported by this model

| Apparent alternatives | Normalization and qualification |
|---|---|
| Message author foreign key versus joined author's ID | Same identity condition under the foreign-key relationship. |
| Search-result Message versus the underlying Message | Same referent and relationships; generated result IDs and wrappers add no family. |
| API message `ts` versus `message_id` | Same source identity. The separate stored `Message.ts` is not an alias. |
| Conversation member-count view versus counting its memberships | Same derived quantity; the membership pair key also makes this the distinct-user count. |
| Reaction summary count versus counting reactions for one message and emoji | Same grouped quantity under the triple key. |
| Thread reply count versus counting the documented direct replies | Same anchor, conversation boundary, and exclusion of the root are required. |

Evidence: model section 3; ledger D04/D05/D07, H01/H02, A08/A22/A26/A27. Many such aliases are already absent from the ER diagram. They do not explain away thousands of its simple routes.

## 3. Association records inflate length, not necessarily the number of meanings

`Message → Reaction → User → Conversation membership → Conversation.name` has four diagram edges. Its faithful ordinary fragment is simply **messages reacted to by members of #security**.

When the intermediate associations are not themselves the referent, a display can abbreviate this as `Message —reacted to by→ User —member of→ Conversation.name`. Preserve association attributes, identity, multiplicity, and access qualifications. When reaction emoji, membership join time, or the association record itself matters, it must remain represented.

This explains why edge depth is a poor proxy for request complexity. It is not a proof that the longer path and another unrelated path have equivalent selection meanings, nor a sufficient denominator reduction by itself.

## 4. Fixed-context conditions are frequently repeated as target paths

Consider the actual route:

`Message → Conversation → Workspace → Named role → Role assignment → User.real_name`

Its faithful fragment is **messages in a workspace where Tom holds a named role**. It does not mean messages authored by Tom, messages to Tom, or messages carrying Tom's role.

For messages scoped to one fixed workspace W, let G(W) say that Tom holds a named role there. Selection is then `all messages in the scope if G(W), otherwise none`. The suffix does not distinguish one scoped message from another; repeating it beneath different descendant entity types repeats the shared context test.

A possible reduction is to represent the scope condition once, with its dependent population selections retained as composition/provenance, rather than credit every inherited occurrence as a new discriminating path. This is **factorization under an explicit fixed scope**, not global query equivalence. The condition can matter, including producing an empty set; it must not simply be deleted. Across multiple workspaces, the original path can discriminate.

Other traps:

- `Message → Conversation → Workspace → Workspace membership → User.name` means messages in a workspace Tom belongs to, not Tom's messages.
- `Role assignment → Named role → Workspace → Workspace membership → User.name` means role assignments in Tom's workspace, not assignments to Tom. The two User roles are different variables.

An ordinary-language fragment must preserve these role distinctions. A short predicate with named variables makes accidental conflation visible.

## 5. Hidden continuations can repeat the same capability limitation

Keep the user's requested read/write limitation tests. Do not turn lack of API exposure into absence or drop the modeled concepts.

For the fixed request **find messages with budget.pdf attached**, two environments can share all visible messages, blocks, users, and conversations while differing in hidden File/File attachment records. Their correct referent sets differ, but the solver's read interface does not expose the distinguishing facts. The model explicitly says file descriptors in blocks and transient chat attachments do not establish these stored records.

Changing the hidden file criterion to type or size changes the reference query, but can exercise the same missing read capability. A candidate limitation requirement is therefore: identify the visible anchor, the unavailable information, its requested use, and the allowed response/alternatives; map hidden path variants to it and test representative cases.

This is a **declared grouping by missing capability**, not a claim of equivalent reference queries or exhaustive testing of every hidden path. The prompts themselves differ. The indistinguishability argument compares environments for one fixed prompt.

Necessary qualifications:

- Establish that information is unavailable through all applicable observations, including prompt-supplied facts and indirect interface projections. Absence of a dedicated endpoint alone is insufficient.
- Keep read limitations separate from write limitations. A supplied handle can permit an operation even when enumeration is unavailable.
- Preserve requested effects and authorized alternatives. Deleting a message can cascade to edit records, but deleting only its history cannot be replaced by deleting the message.
- Preserve independent work and visible grounding requirements. A missing attachment lookup does not disable a separately requested channel update.
- Do not infer observability of all fields from observability of their owning entity.

Evidence: model sections 3–4; ledger D09–D15 and H05. The numerical partition suggests where to investigate this grouping; it does not itself prove the grouping or count its final families.

## 6. Distinct ordinary long references must survive

| Path | Faithful ordinary fragment | Why the link matters |
|---|---|---|
| Message → User → Conversation membership → Conversation.name | Messages written by members of #engineering | The membership belongs to that message's author. |
| Conversation → Message → Reaction → User.name | Channels containing messages Tom reacted to | Tom's reaction is linked to a message in that particular channel. |
| Message → Reaction → User → Conversation membership → Conversation.name | Messages reacted to by members of #security | The member and the reactor must be the same user. |
| File → User → Conversation membership → Conversation.name | Files associated with members of #design | The model establishes associated user, not uploader/owner. Access remains a limitation question. |
| User → Role assignment → Named role.name | Users assigned the role Reviewer | Named role is independent of workspace admin/member flags. Access remains a limitation question. |

The first three do not need arbitrary depth exceptions: their ordinary identifying meanings and witness relationships justify retaining the full paths. The last two retain valid structural meaning while acknowledging capability limitations.

A concrete counterexample to merging author and reactor paths: message M1 is authored by Tom and reacted to by Lee; message M2 is authored by Lee and reacted to by Tom. The two name-based descriptions select different messages. Equal endpoints or information footprints do not establish redundancy.

## 7. Candidate inclusion procedure to discuss

1. Start with the entire adopted model; preserve entities and relationship identities.
2. Write the complete selection meaning and a faithful ordinary request fragment. Do not silently invent uploader, channel-admin, co-membership, or same-person semantics.
3. Canonicalize proven identity/view aliases and equivalent query representations.
4. Identify fixed context. Factor conditions that depend only on that context; keep their effect explicit.
5. Identify observation and operation limitations. Consider grouping hidden continuations by the actual missing capability, with alternatives and requested effects preserved.
6. For remaining discriminating reference families, demonstrate how the focal evidence can change candidate eligibility while auxiliary criteria remain equal. A target/decoy construction is useful evidence; absent and underspecified realizations still require their own semantics. This is not a rule that every legitimate context/existence check must distinguish two simultaneous candidates.
7. Retain meaningful long paths. Give distinct but contrived compositions an explicit inclusion decision rather than falsely labeling them equivalent to shorter paths.

This procedure has not been adopted, run exhaustively, or assigned final coverage counts. Exact equivalence alone probably will not make the remaining space small: the model explicitly lacks several cross-relationship invariants, and nested ordinary references can remain distinct. The strongest measured opportunity is separating repeated capability limitations and fixed-scope qualifications from independent referent discrimination.

## 8. Unsafe reductions to avoid

- Channel members are not interchangeable with message authors or workspace members.
- Role assignments do not establish workspace membership.
- Default conversation and containing workspace relationships are independent here.
- Three attachment records need not mean three distinct files; repeated attachment pairs are permitted.
- Text/block mentions are not the stored User mention relationship.
- A message's parent is not guaranteed to be a root.
- A long path using the same fields as a shorter one is not automatically equivalent.
- A shared empty result in the current seed is not evidence of duplicate path families.
- Lack of direct API access is not automatic lack of all permissible effects.

These restrictions follow the adopted model; they are not proposed elaborations of it.
