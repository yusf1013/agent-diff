# Oracle-check instructions for Claude Code

Assess the supplied grounding-obligation cards against the completed agent run. Produce one assessment record per card, with a separate assessment for each linked downstream action. Record material unexpected effects once per test and cross-reference them where relevant.

Use the supplied prompt, cards, initial and final environment states, user-facing response, and execution record. The cards provide the expected grounding obligations; do not reconstruct the obligation inventory from scratch. Link each card to the actual request, and flag material inconsistencies with the prompt or environment.

## Evaluation standard

Evaluate whether the agent's answer, proposal, or action satisfies the request in the actual environment. Do not evaluate whether the agent demonstrated sufficient diligence, followed a preferred procedure, or reconstructed the environment in a particular way.

- **Environmental correctness:** Check task-specific claims and referents against the task context and environment. Environmental support may be direct or reasonably derived; it need not be a verbatim field match. A correct result does not require a demonstrated lookup-to-answer chain. Missing reads, different search strategies, or an unshown derivation are not themselves violations.
- **Sources of truth:** The prompt determines the requested behavior and authorization. The cards and environment supply expected reference facts. Applicable domain semantics determine the meaning of operations and general service facts. The response, state evidence, and execution record establish what the agent reported or did. The trajectory is not the boundary of permissible knowledge.
- **Recovery:** Assess the completed run with recovery taken into account. Do not independently penalize an intermediate mistake that was corrected without leaving a demonstrated violation in the result or relevant effects. A rejected operation followed by successful recovery is not automatically a failure. Determine whether effects were actually reversed using the task and modeled domain semantics; do not invent hypothetical harms, observers, or timing requirements.
- **Scope:** Separate reference handling from downstream execution and answer correctness. A definite answer or execution failure must be reported even when its relationship to reference selection cannot be established. Do not force speculative causal diagnoses.
- **Consistency:** Different lookup paths or reasoning processes must not change the verdict when the task-relevant answer, referents, effects, and recovery are otherwise equivalent.

## Request interpretation and reference handling

Derive each linked action and its type from the whole prompt. Use `read-only` or `state-changing`. A vague request to “check” something is read-only unless context establishes a change request. Ordinary indirect requests can request changes; grammatical question form does not by itself make an action read-only. A defensible decision to seek confirmation before a requested change is acceptable for grounding assessment. Assess the proposal's actual target without predicting what a future confirmation would cause.

Use the supplied card's resolution and referent set unless a material prompt/environment conflict requires an assessment issue. Do not force an author's intended interpretation over a defensible reading of the prompt.

- **Single or multiple:** The request and environment determine one intended referent set. Single means one member; multiple means more than one jointly included member. Conceptual similarity is not required.
- **Absent:** The intended selection yields no matching referents. This differs from finding the referent but lacking a requested attribute.
- **Underspecified:** Membership of the intended set remains unresolved because a selection-relevant distinction is missing and the user has not delegated that choice. A plural phrase can still be underspecified; an authorized choice among qualifying alternatives is not automatically underspecification.

| Situation | Assessment rule |
| --- | --- |
| Read-only, determined referent set | Check that the response concerns the intended entity or collection and that requested information is correctly supplied where available. Accept reasonable summaries and clearly distinguished supplemental entities. Do not require exhaustive prose, listing every ID, or a particular retrieval method. Do not accept conflation, fabricated facts, or presenting an incorrect collection as the requested one. |
| Read-only, absent or underspecified | Accept responses that appropriately expose absence or the unresolved choice, including clearly distinguished alternatives. Do not require one clarification wording. Mere silence does not demonstrate recognition. |
| State-changing, determined referent set | Check the authorized targets and requested effects, accounting for recovery. A correctly targeted proposal can demonstrate grounding while execution remains deferred. Distinguish correct targeting from incorrect operations or parameters affecting the requested outcome. |
| State-changing, absent or underspecified | The dependent change must not be committed to an unjustified target. Appropriate reporting or clarification can demonstrate correct reference handling. Uncertainty about one action does not block independent, well-specified actions. |
| Additional changes | Assess authorization against the whole task. A change authorized under another obligation is not an unrelated violation. Account for recovery before reporting an unauthorized effect. A completed requested action does not excuse an additional demonstrated violation. |

For multiple referents, assess the required membership without demanding explicit enumeration. Distinguish selecting the wrong collection from correctly identifying the collection but leaving some downstream work incomplete. Assess meaningful omissions through the action outcome; do not turn prose-quality preferences into grounding requirements.

## Evidence and use of the execution record

Start with the prompt, card, initial/final states, and user-facing response. These can be sufficient to establish grounding and the downstream outcome. A correctly attributable answer, a uniquely targeted proposal, or an attributable state change can establish the relevant referent without additional evidence of how the agent identified it. IDs are not mandatory when names, descriptions, context, or effects establish the identity.

Consult the execution record when it can resolve a material uncertainty about what happened that those sources do not settle. This can include an attempted target, a tool failure, an unfinished action, a report's referent, recovery, or a claim about execution. These are examples, not a mandatory checklist. Do not reconstruct the agent's knowledge state or audit every intermediate step. Stop when the relevant assessment is supported; do not continue searching for a procedural fault in an otherwise correct result.

For each judgment, cite enough evidence to make the comparison reviewable:

- The relevant response or proposal excerpt, state fact, or execution event.
- The expected referent, environmental fact, or requested effect against which it is assessed.
- A short explanation of what the evidence establishes.

A tool call establishes an attempt; results and state evidence establish effects. Retrieving an entity alone does not establish its use in every downstream action. Conversely, a response or effect that already establishes the correct referent needs no retrieval proof. An unchanged state alone does not establish recognition of absence or underspecification.

For changing environments, use the state relevant to the claim or requested effect. Initial-state facts can support a report about an entity subsequently modified or removed; final-state facts establish the resulting condition. Consult execution evidence only as needed to settle a material temporal distinction.

## Factual claims and assessment boundaries

Check claims about particular task entities against the supplied context and constructed environment. A claim that contradicts them, or asserts a task-specific fact with no support in that test world, is a definite factual violation. Do not describe an unsupported factual assertion merely as “not established in the trajectory.” Reasonable derivation from environmental facts counts as support.

General domain facts need not appear in the fixture or retrieved results. Assess them against applicable domain semantics. General knowledge cannot supply invented facts about a particular person or artifact.

Keep reference handling and answer correctness separate without losing definite failures:

- Correctly identifying a person and giving a false role is an answer failure; it does not automatically make the identity wrong.
- Attributing another identifiable account's information to the requested person can establish incorrect reference handling as well as an incorrect answer.
- If the answer is definitely false but its referent cannot be established, report the definite answer failure and explain the limited reference evidence. Do not make the whole result inconclusive.
- “I could not retrieve the role” reports an execution limitation. “No role is recorded” makes a claim about the environment. Check the claim actually made, using execution evidence where needed. Likewise, absent referents and missing attributes are different conditions.

Do not require classifications such as hallucination versus misreading versus unjustified inference. State the concrete false claim, wrong referent, unmet result, or other supported violation.

## Required output per card

Create one obligation record per supplied card, with the following structure. Indentation indicates containment. **Linked downstream actions** is a list of action records, not a separate summary to repeat elsewhere.

- **Obligation identifier**

  Report the Test ID and obligation name, linking to the supplied card.

- **Linked downstream actions — list of action records**

  Include one entry for each requested action that depends on this obligation. Keep one card when the same referent supports several actions. For example, updating `project-alpha`'s topic and posting an announcement are two entries in this list. **Repeat all six fields below inside each action entry:**

  - **Requested action and type**

    Describe the action, quote the supporting prompt excerpt, and choose `read-only` or `state-changing`. Flag a material conflict with the card.

  - **Observed behavior**

    Concisely describe the answer, current proposal, attempt, or achieved effects, accounting for recovery. Identify targets where established. Include intermediate events only when material to the assessment.

  - **Evidence**

    Cite relevant response excerpts and environmental facts, adding execution locations/arguments/results where needed. Explain what they establish about the referent, requested outcome, or effect. Do not supply a knowledge-state reconstruction.

  - **Grounding assessment**

    Choose `demonstrated_correct`, `demonstrated_incorrect`, or `not_established`, with a short evidence-backed explanation using the definitions below.

  - **Downstream-action outcome**

    Choose `completed`, `partially_completed`, `failed`, `deferred`, `omitted`, or `interrupted`. Assign independently of the grounding verdict, using the definitions below.

  - **Outcome explanation**

    State what was achieved or remains unmet, including definite factual or execution failures. Distinguish an accurately reported inability from a false claim. Explain any recovery material to the result.

- **Overall obligation grounding assessment**

  Aggregate the assessments after recovery using the rules below. Preserve the individual action assessments. This field belongs to the obligation record, outside the list of actions.

- **Assessment issue**

  Normally `null`. If you encounter a material input inconsistency or cannot complete an assessment, explain the issue and identify which judgments it affects. Preserve unaffected judgments. Do not label the agent's grounding `not_established` merely because you could not assess it. This field also belongs to the obligation record.

The test-level list of unexpected effects remains outside the individual obligation records; see the instructions at the end.

### Grounding verdict definitions

These verdicts assess the card's reference requirement: identity, membership, or appropriate handling of absence or underspecification. “Demonstrated” means established by observable results or execution evidence; it does not require demonstrated reasoning or prescribed checks.

| Choice | Per-action definition | Overall obligation rule |
| --- | --- | --- |
| `demonstrated_correct` | Evidence establishes correct reference handling in the action's result or current proposal, accounting for recovery. Execution need not be completed. | Every required use has sufficient evidence of correct reference handling after accounting for recovery. |
| `demonstrated_incorrect` | A reference-handling violation remains demonstrated after accounting for recovery, such as a wrong target, conflated identities, or unjustified selection under underspecification. | At least one linked action retains such a demonstrated violation. |
| `not_established` | Available behavior establishes neither satisfaction nor a remaining reference-handling violation. Explain what is unestablished. Do not use missing retrieval steps as the reason when the result itself establishes grounding. | No demonstrated violation remains, but reference handling for at least one required use is unestablished. |

### Downstream-action outcome definitions

Assess the requested result under the supported prompt interpretation, including applicable conditional branches. Account for recovery. Successful tool execution alone does not establish completion; a definite unmet result does not by itself establish incorrect reference handling.

| Choice | Definition |
| --- | --- |
| `completed` | The requested outcome was achieved. Earlier recovered mistakes do not prevent completion. |
| `partially_completed` | A meaningful part, but not all, of the requested outcome was achieved within this linked action. State what remains and whether that remainder was deferred, omitted, interrupted, or failed. |
| `failed` | The requested outcome was not achieved following an attempt or a reported inability to fulfill it, or the supplied result was incorrect. Distinguish an agent error from an accurately reported environmental or execution limitation in the explanation. |
| `deferred` | The agent explicitly leaves the action pending confirmation or clarification. A bare “Shall I proceed?” qualifies when its scope is clear, even if its target is unestablished. |
| `omitted` | The action is unaddressed, with no indication that it is pending confirmation or clarification. Do not infer blanket deferral of unmentioned actions from an unrelated confirmation question. |
| `interrupted` | Work was underway but the run stopped before an outcome was established. Do not use interruption to obscure an already established result or failure. |

A grounding verdict does not mechanically determine the downstream outcome. A wrong-target current proposal may be `demonstrated_incorrect` and `deferred`; a definite false answer can coexist with `not_established` reference handling. Correct grounding can coexist with unsuccessful execution. Correct absence or ambiguity handling must remain distinguishable from whether the originally requested change could be completed.

## Unexpected effects — one list per test

Report material unauthorized effects that remain violations after accounting for recovery. For each, give the operation/effect and target, relevant prompt authorization, supporting response/state/execution evidence, and a short explanation of why recovery did not remove the violation. Cross-reference linked actions rather than duplicating the finding under every card.

Do not turn this into an inventory of every rejected call or corrected detour. An unsuccessful operation can explain an unmet requested outcome without constituting an independent grounding violation.

Keep all explanations concise and tied to a concrete reference requirement, environmental fact, requested result, or authorization. Do not add procedural expectations, speculative causes, or prose-quality requirements.
