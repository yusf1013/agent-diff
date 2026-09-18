# Slack generation: reviewed design sketches

Recorded 2026-09-17 from the user's review of five manually authored sketches.
These are design-calibration examples, not automatically generated tests or
measured campaign outcomes. This note records discussion; it does not authorize
implementation or model runs. Earlier prototype code and prompts have not been
updated to implement these agreements.

## Agreed direction

- Focus on clean generation first, reusing the existing Slack seed and adding to
  it as needed. Sketches below describe distinguishing records, not replacement
  environments containing only those records.
- Mechanically choose the identifying route and resolution requirement. A small
  identifying-path addition to cards is allowed; its exact serialization remains
  to be settled. Existing cards will be updated separately when needed.
- Construct identifying conditions from attributes and relationships along the
  path. Multiple conditions can occur on one path. Remove the former arbitrary
  three-condition ceiling and the restriction that negatives violate only one
  designated focal attribute.
- Negatives may challenge different conditions, missing relationships, or wrong
  bindings. Conditions that concern the same reaction/person/message must hold
  on the same connected records. Do not require an exhaustive combination set or
  unlimited negatives.
- Coverage requirements remain separate: complete routes, identifying attributes,
  resolution modes per referent entity, and representative capability limitations.
  A case can satisfy multiple requirements. Additional negatives do not themselves
  create new coverage cells.
- Use a writer, compiler and reviewer. Repairs and further attempts continue the
  relevant existing conversation, retaining prior responses.
- User requests should be short, natural and open-ended. Do not manufacture a
  short list of candidate IDs/channels for the solver to choose from merely to
  simplify construction or validation.

## 1. Messages selected through reactions — multiple

Route: `Message → Reaction → User`

Original reviewed request:

> Find messages Tom reacted to with a thumbs up.

| Message | Reactions | Interpretation |
|---|---|---|
| A | Tom 👍 | Match |
| B | Tom 👍 and Maya 👀 | Match |
| C | Tom 👀 | Wrong emoji |
| D | Tim 👍 | Wrong person |
| E | None | Missing reaction |
| F | Tom 👀 and Tim 👍 | Conditions occur on different reactions |

Tom and Tim are distinct, clearly identifiable people. The messages have ordinary
content and do not disclose their construction roles.

**User feedback:** Valid and generally good; especially useful negative patterns.
Improve task quality with a consequential operation, such as adding a star
reaction to the selected messages. For a read-only alternative, ask a concrete
question, such as which places the selected messages mention. Give the matching
messages distinct substantive answers (A mentions places A/B; B mentions C/D), so
the delivered answer helps identify which sources were used. These are ordinary
content differences, not inserted test labels. Bare "find messages" is a quality
weakness, not a validity failure.

## 2. Messages selected through reactor membership — multiple

Route: `Message → Reaction → User → Channel membership → Channel`

Original reviewed request:

> Find messages that received a thumbs up from someone in #security.

| Message | Environment facts | Interpretation |
|---|---|---|
| A | Maya belongs to #security and reacted 👍 | Match |
| B | Omar belongs to #security and reacted 👍 | Match |
| C | Author belongs to #security; the only reactor does not | Wrong relationship role |
| D | A #security member reacted 👀; a nonmember reacted 👍 | Conditions bind to different people |
| E | The 👍 reactor belongs to #security-planning, not #security | Wrong channel membership |

**User feedback:** Valid, with especially useful relationship negatives. The same
downstream-task quality improvement as example 1 applies. E is valid because
`#security` explicitly names the channel. If the request only said "someone in
security," the intended organizational meaning might reasonably include someone
in security-planning. That would be a validity concern. Do not treat a hidden
exact-field predicate as authority over the ordinary wording.

## 3. A person selected for a downstream action — single

Route: `User → Reaction → Message`

Reviewed request:

> DM the person who reacted with ✅ to the deployment announcement: “Ready for the review?”

| Person | Environment facts | Interpretation |
|---|---|---|
| Maya | Reacted ✅ to the deployment announcement | Intended recipient |
| Omar | Reacted 👍 to that announcement | Wrong emoji |
| Lara | Reacted ✅ to an office-move announcement | Wrong message |
| Tim | Authored the deployment announcement without reacting | Wrong relationship role |

**User feedback:** Correct and very good; the consequential action is appropriate.
Compilation must preserve the semantic separation: Lara's office-move message
must not also discuss deployment in a way that makes it a legitimate match.

Do not rely on superficial negation to create a semantic negative. The user's
earlier example was a "meeting confirmation" request with a supposedly negative
message saying the meeting was canceled. Cancellation remains relevant to the
same meeting-status/confirmation discussion; it is not a reliably separate topic
just because it negates the event. Use clearly excluded content under the actual
request, rather than a debatable linguistic distinction or keyword absence.

## 4. A channel selected through an ambiguous person — underspecified

Route: `Channel → Message → Reaction → User`

Reviewed request:

> Which channel has the deployment announcement Alex reacted to with 👍?

| Channel | Environment facts | Interpretation |
|---|---|---|
| #release-updates | Alex Chen reacted 👍 to a deployment announcement | One possible answer |
| #platform-news | Alex Patel reacted 👍 to a different deployment announcement | Another possible answer |
| #engineering | Alex Chen authored an announcement; only Maya reacted 👍 | Wrong relationship role |

The request does not distinguish the two Alexes. Reporting the person–channel
alternatives or asking which Alex is intended handles the ambiguity. Competing
legitimate alternatives are not negatives.

**User feedback:** Valid and good quality, including its open-ended read-only
question. Additional negatives are welcome but not mandatory: for example,
Alex reacting to another announcement, or using a different emoji on a deployment
announcement. Do not reject the design merely because more negatives are possible.

## 5. A person selected through an absent reaction

Route: `User → Reaction → Message`

Reviewed request:

> Who reacted with 🎉 to the budget approval announcement?

| Environment fact | Why it does not match |
|---|---|
| Maya reacted 👍 to the budget approval announcement | Wrong emoji |
| Omar reacted 🎉 to an office-move announcement | Wrong message |
| Lara authored the budget approval announcement but did not react | Wrong relationship role |

There is no qualifying person, despite plausible related activity.

**User feedback:** Valid and good quality. This open-ended read-only question is
acceptable. The user particularly favors deriving negatives from the query path.

## Requirements learned from the review

**Validity:** The ordinary request must justify excluding each negative. Preserve
relationship bindings, distinguish ambiguity alternatives from negatives, avoid
accidental topic overlap, and do not use semantic negation as an automatic
non-match. Validate the concrete compiled text as well as the abstract role plan.

**Quality:** Prefer consequential supported actions or meaningful open-ended
questions. Concrete answers derived from distinct sources can make read-only
grounding easier to assess. A valid bare retrieval request can still be improved;
do not conflate that preference with invalidity. More negatives can help, but
quantity alone is not an acceptance requirement.

**Prompt preservation:** The short, natural wording in these examples is the
desired style. Once the writer's request meets the requirements and is accepted,
preserve it through compilation. Do not expand it with explanations, candidate
lists, search guidance or repeated constraints. If compilation reveals a real
design defect, return it for an explicit writer revision rather than silently
rewriting the request in the compiler.

## Proposed next step — not yet executed or authorized

Calibrate the writer alone before rebuilding the complete generation pipeline.
Its concise visible deliverable should resemble the examples above: route,
resolution mode, exact user request, and a small table of intended roles,
environment facts and selection consequences. Include a short note only for
material bindings or ambiguity. Concrete database IDs and full serialized seed
rows belong to the compiler stage.

Use a small batch of fresh designs to check whether the instructions reproduce
these qualities beyond the reviewed examples. A reviewer checks the same stated
requirements, separating validity defects from quality suggestions. Repairs
continue the writer conversation. Inspect the resulting designs with the user
before compilation or solver execution.

These manual examples guide prompt development and comparison; do not count them
as automated generation outcomes. Carry general lessons into the instructions
rather than handing the generator the finished designs for its evaluation cases.
