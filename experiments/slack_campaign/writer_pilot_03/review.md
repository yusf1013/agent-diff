# Conceptual writer pilot: first-pass review

Ten fresh Sonnet 5 sketches were produced. **Three meet the observed conceptual
construction requirements; one more is coherent but misses a required negative.
Six need repair or clarification.** This is not a runnable-test validity rate:
the sketches have not been compiled into the existing seed or checked through the
API. Challenge assessments below describe opportunities for mistakes, not measured
solver failures. These manual judgments are Codex development work, not automated
review results.

Read [all ten original outputs together](outputs.md). None were repaired, replaced
or selected from retries. The older campaign remains preserved separately.

## Inputs and procedure

- [Frozen shared input](system.md): procedural writer instructions, concise Slack
  capabilities and the adopted conceptual domain model. No seed or physical schema.
- [Assignments](assignments.json): ten retained routes, all seven root entities,
  all four resolution modes and paths from one to five relationships. Counts are
  assigned mechanically: one, two, zero, or two alternative singleton sets.
- [Common instructions](../../../grounding/slack_campaign/prompts/v3/writer.md)
  and mode fragments for
  [single](../../../grounding/slack_campaign/prompts/v3/modes/single.md),
  [multiple](../../../grounding/slack_campaign/prompts/v3/modes/multiple.md),
  [absent](../../../grounding/slack_campaign/prompts/v3/modes/absent.md), and
  [underspecified](../../../grounding/slack_campaign/prompts/v3/modes/underspecified.md).
  Each case receives only its assigned fragment and example. Its exact input is
  linked beside the output below.
- [Runner](../../../grounding/slack_campaign/concept_writer.py): the first two
  substantive cases establish cache reuse; the remaining eight run in parallel.
  There is no compiler, model reviewer, solver or semantic repair in this pilot.
- [Provenance](provenance.json): manual versus automated work, limits and input hash.

The route procedure translates backward into an expression, then checks the chain
forward. It explicitly distinguishes author/reactor/member roles, preserves shared
intermediate records, avoids equating unrelated locations and counts distinct root
referents rather than their witnesses. Negative construction includes value,
missing-relationship and binding failures. Tom👀 plus Tim👍 is one failed binding,
not two independently changed query requirements.

The successful short-route outputs W01–W03 resemble their mode examples closely.
They demonstrate reproduction of those construction patterns, not independent
evidence of broad generalization. W06 provides a useful additional relationship
pattern. The longer-route failures matter more than a polished overall format.

## Per-case assessment

| Case and evidence | Route / mode | Conceptual validity | Challenge assessment |
|---|---|---|---|
| **W01** — [input](W01/input.md), [output](W01/writer/turn-01/output.md), [thinking](W01/writer/turn-01/thinking.txt) | Message → Reaction → User / multiple | Coherent; two matches, including unrelated activity, and five useful negatives. | Strong match to the agreed example: emoji, person, absent edge, split reaction binding and channel location each matter. Consequential reaction-add. |
| **W02** — [input](W02/input.md), [output](W02/writer/turn-01/output.md), [thinking](W02/writer/turn-01/thinking.txt) | User → Reaction → Message / single | Coherent single recipient. Missing a negative that changes only the explicit #launch-prep location condition. | Good recipient, emoji, message and author/reactor distinctions; incomplete coverage of its own conditions. |
| **W03** — [input](W03/input.md), [output](W03/writer/turn-01/output.md), [thinking](W03/writer/turn-01/thinking.txt) | Conversation → Message → Reaction → User / underspecified | Coherent two-Sam ambiguity and mutually distinct channel alternatives. Mode heading omitted, but interpretation is clear. | Good: unsupported choice would change a channel topic. Extra negatives distinguish topic, emoji, reactor and same-message binding. |
| **W04** — [input](W04/input.md), [output](W04/writer/turn-01/output.md), [thinking](W04/writer/turn-01/thinking.txt) | Message → Reaction → User → Conversation Membership → Conversation / absent | Invalid as absent: the marketing message is a full match. Also contains a draft correction and conflicting apparent message rows. | Useful ingredients, but incorrect selection labels prevent this from being a valid challenge. Requires scenario repair. |
| **W05** — [input](W05/input.md), [output](W05/writer/turn-01/output.md), [thinking](W05/writer/turn-01/thinking.txt) | Conversation → Conversation Membership / multiple | Five rows are coherent; #support contradicts itself about current memberships. Local repair needed. | Moderate: counts 4/5/6 and workspace-versus-channel membership are useful distinctions. A one-edge count route need not invent complex binding failures. |
| **W06** — [input](W06/input.md), [output](W06/writer/turn-01/output.md), [thinking](W06/writer/turn-01/thinking.txt) | Message → User → Conversation Membership → Conversation / multiple | Coherent two-message selection through each author's membership. | Good: channel location is deliberately separated from author membership; similar channel name and missing membership add plausible competitors. Consequential reaction-add. |
| **W07** — [input](W07/input.md), [output](W07/writer/turn-01/output.md), [thinking](W07/writer/turn-01/thinking.txt) | Conversation Membership → User → Reaction → Message → Conversation / underspecified | Invalid as a single environment: purported negative rows reuse already-qualifying membership roots. Another row has no membership root. | Promising ambiguity/binding idea, but both alternatives answer yes, weakening answer discrimination. Read-only chosen although membership removal is supported. |
| **W08** — [input](W08/input.md), [output](W08/writer/turn-01/output.md), [thinking](W08/writer/turn-01/thinking.txt) | Reaction → Message → User → Conversation Membership → Conversation / single | Invalid as a single environment: the same reaction/Nina are repeated with incompatible membership facts. | Weak: every reaction's person is Priya, so selecting a wrong reaction can still give the same answer. Own-reaction removal was available when designing the story. |
| **W09** — [input](W09/input.md), [output](W09/writer/turn-01/output.md), [thinking](W09/writer/turn-01/thinking.txt) | Workspace → Workspace Membership → User → Conversation Membership → Conversation / absent | Absence plausible but not fully established by the table; root rows and accessible workspace scope need clarification. | Promising complementary near matches. It avoids the old G-R154 empty-channel shortcut, but cannot yet be counted as a finished valid design. |
| **W10** — [input](W10/input.md), [output](W10/writer/turn-01/output.md), [thinking](W10/writer/turn-01/thinking.txt) | Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership / multiple | Coherent selection, but requests role distinctions beyond supplied capabilities. Read-answer and membership scope need repair. | Good basic five-edge selection challenge; emoji, channel membership and absent reaction matter. Last negative repeats an emoji failure rather than adding a binding test. |

## Material defects and strengths

**W04 tests a condition its prompt never requested.** Marco reacts 🚀 to a
marketing message and belongs to #eng-rollout. That satisfies “the message that
someone from #eng-rollout reacted to with 🚀.” The requested reply concerns a
rollout, but that purpose does not restrict the selected message's content. Calling
this row “Wrong message only” is incorrect. The Wendy row also leaves an inline
“actually satisfies…adjust” correction in the final table instead of resolving it.

**W07 and W08 confuse competing referents with counterfactual versions of one
referent.** Adding Alex Rivera's wrong-emoji reaction cannot make his membership
a negative when his qualifying reaction remains elsewhere in the same table.
Nina cannot simultaneously have and lack the membership used by the identical
Priya/message/🚀 reaction. The instructions already require distinct roots and
checking all rows together; this is a failure to apply that procedure. Giving a
compiler these tables would force it to redesign selection rather than instantiate
a settled story.

**W05 needs a local factual correction.** #support has “exactly 5 conversation
memberships” and then no current membership rows. A historical mention can be a
useful non-match, but it cannot also be presented as five current relationships.
The other count rows have meaningful, ordinary interpretations.

**W09 is an improvement over the earlier R154 design, with unresolved details.**
There are channel members without the required workspace association and workspace
members without the required channel association. That is the desired complementary
construction. However, Priya's row is a supporting person, not a workspace referent;
Sam's workspace association is unspecified; and discovery across the proposed
workspaces has not been established. Workspace-name lookup is unavailable, but
that alone does not invalidate an absent case: the correct absence response would
not need to return a workspace name. The issue is establishing the complete absence
within an accessible, specified population.

**W10 overstates observable role information.** The capability brief allows
administrator/owner flags but does not establish full member-versus-guest roles.
The request asks for workspace roles and supplies `member` as an answer. A supported
read answer is needed. Resolving terminal-member Priya also adds a user reference;
it must survive compilation rather than being lost because the assigned route
stops at a membership. That extension does not itself erase the assigned route.

Six outputs use writes; four use reads. W09/W10 have roots without supported
writes. W07/W08's read choices were avoidable. In W08 the writer first chooses
another person's reaction, then cites that choice as its reason to avoid removing
the actor's own reaction. This is a story-design choice, not an unavoidable limit.

## Accounting and checks

| Item | Result |
|---|---:|
| Author calls / returned sketches | 10 / 10 |
| Semantic repairs, replacements or resamples | 0 |
| Unknown-usage calls | 0 |
| Native cache-hit calls | 9 / 10 |
| Cache creation tokens | 6,794 |
| Cache read tokens | 61,146 |
| Uncached input tokens | 6,417 |
| Output tokens, including thinking | 15,496 |
| Estimated cost using recorded historical rates | $0.2955123 |
| Unit checks | 47 passed |

Cost is our rate conversion of native Bedrock usage, not an invoice amount. See
[usage summary](usage_summary.json), [all-call ledger](usage_ledger.json),
[cache check](cache_check.json) and [run status](run_status.json). Every call retains
its request, native response, metadata and exposed thinking beside the Markdown.
The test suite covers adapter caching/text output, conversation preservation,
mode-specific input assembly and existing campaign compatibility; it does not
certify the semantic quality of these sketches.

## Assessment before further work

The new interface produces the requested short, reviewable tables and materially
reduces author input. Caching works. Quality is not yet reliable enough to connect
this writer to broad compilation. The strongest examples reach the agreed manual
style, but the batch does not consistently reach its validity standard, especially
on longer paths.

The next focused improvement should make the existing whole-table check concrete:
hold each shared person's/message's facts fixed, create distinct competing roots,
and re-evaluate those roots against only the conditions actually written in the
request. Capability checking should also happen before committing to the downstream
answer. These are development recommendations, not changes already applied or
additional paid runs. Preserve this first-pass result as the comparison point.
