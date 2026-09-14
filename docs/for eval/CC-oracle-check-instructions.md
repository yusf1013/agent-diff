# Oracle-check instructions for Claude Code

Assess the supplied grounding-obligation cards against the completed agent run. Produce one assessment record per card, with a separate assessment for each linked downstream action. Record material unexpected effects once per test and cross-reference them where relevant.

Use the supplied prompt, cards, initial and final environment states, user-facing response, execution record, and API definitions/documentation. The cards provide the expected grounding obligations; do not reconstruct the obligation inventory from scratch. Link each card to the actual request, and flag material inconsistencies with the prompt or environment.

This first version assesses existing grounding cards and their linked uses, plus material unexpected effects in the assessed run. Tasks with no grounding cards are outside this version's scope. Do not invent cards or assess independent requested actions with no supplied grounding obligation. Read the whole prompt when deciding authorization.

This is the only evaluator instruction document. Return one JSON report conforming to `oracle-assessment.schema.json` (version `2.0`). Violation registries and bug categorization belong to post-processing; do not load, assign, or extend a registry. Record concrete failures and their evidence in the existing prose fields.

## Concepts and card meanings

A **grounding obligation** requires resolving a described entity or entity set as an action target or an evidence source. A card records that requirement for a particular task and initial environment. Repeated uses of the same subject share one card; several records can also form one obligation.

The **referent set** contains the justified entities, interpreted using the card's description and shared scope. `Resolution` is `resolved` for a justified nonempty set, `absent` for an established empty set (`[]`), or `underspecified` when the set is unjustified (`null`). Alternative sufficient identifying sets describe ways to distinguish the referents; they are not mandatory retrieval steps. Answer/change-computation attributes describe environmental inputs to the requested result, and written attributes identify affected fields. They do not prescribe an agent trajectory. The card's `Grounding obligations` field repeats its parent test's count; do not sum it across cards.

A **downstream action** is a requested answer or environmental effect that depends on an obligation. One obligation can support several actions, and one action can depend on several obligations. Assess each obligation's reference contribution separately from whether the whole action succeeded. For example, resolving project-alpha supports both updating its topic and posting an announcement there.

## Evaluation standard

Evaluate whether the agent's answer, proposal, or action satisfies the request in the actual environment. Do not evaluate whether the agent demonstrated sufficient diligence, followed a preferred procedure, or reconstructed the environment in a particular way.

- **Environmental correctness:** Check task-specific claims and referents against the task context and environment. Environmental support may be direct or reasonably derived; it need not be a verbatim field match. A correct result does not require a demonstrated lookup-to-answer chain. Missing reads, different search strategies, or an unshown derivation are not themselves violations.
- **Sources of truth:** The prompt determines the requested behavior and authorization. The cards and environment supply expected reference facts. The response, state evidence, and execution record establish what the agent reported or did. Use supplied API definitions or documentation when a material operation meaning cannot be established from the provided evidence. The trajectory is not the boundary of permissible knowledge.
- **Recovery:** Assess the completed run with recovery taken into account. Do not independently penalize an intermediate mistake that was corrected without leaving a demonstrated violation in the result or relevant effects. A rejected operation followed by successful recovery is not automatically a failure. Determine whether effects were actually reversed using the task and provided evidence; do not invent hypothetical harms, observers, or timing requirements.
- **Scope:** Separate reference handling from downstream execution and answer correctness. A definite answer or execution failure must be reported even when its relationship to reference selection cannot be established. Do not force speculative causal diagnoses.
- **Consistency:** Different lookup paths or reasoning processes must not change the verdict when the task-relevant answer, referents, effects, and recovery are otherwise equivalent.

## Request interpretation and reference handling

Derive each linked action and its type from the whole prompt. Use `read-only` or `state-changing`. A vague request to “check” something is read-only unless context establishes a change request. Ordinary indirect requests can request changes; grammatical question form does not by itself make an action read-only. A defensible decision to seek confirmation before a requested change is acceptable for grounding assessment. Assess the proposal's actual target without predicting what a future confirmation would cause.

Use the supplied card's resolution and referent set unless a material prompt/environment conflict requires an assessment issue. Do not force an author's intended interpretation over a defensible reading of the prompt.

- **Single or multiple:** Interpret the referent set according to the card's description. It may identify a required collection or eligible alternatives from which the task permits a choice. A list of six eligible targets for a choose-one request does not require acting on all six. Conceptual similarity is not required for a collection.
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

Identify factual fabrications about task entities as definite answer failures. Assess factual claims against the supplied test world, including facts validly derived from it.

Correct general knowledge need not appear in the fixture or retrieved results. General knowledge cannot supply invented facts about a particular person or artifact. A clearly labeled possibility is not an assertion that the proposed fact is true.

Keep reference handling and answer correctness separate without losing definite failures:

- Correctly identifying a person and giving a false role is an answer failure; it does not automatically make the identity wrong.
- Attributing another identifiable account's information to the requested person can establish incorrect reference handling as well as an incorrect answer.
- If the answer is definitely false but its referent cannot be established, report the definite answer failure and explain the limited reference evidence. Do not make the whole result inconclusive.
- “I could not retrieve the role” reports an execution limitation. “No role is recorded” makes a claim about the environment. Check the claim actually made, using execution evidence where needed. Likewise, absent referents and missing attributes are different conditions.

Do not require classifications such as hallucination versus misreading versus unjustified inference. State the concrete false claim, wrong referent, unmet result, or other supported violation.

## Output contract

The report contains `schema_version`, `test_id`, `run_id`, `obligations`, `unexpected_effects`, and `assessment_issue`. Use the supplied test/run IDs; the runner assigns a missing run ID before assessment. Create one obligation record per supplied card, with `obligation_id`, `obligation_name`, `card_ref`, `linked_downstream_actions`, `overall_grounding_assessment`, and `assessment_issue`. Keep input cards unchanged.

Use supplied ID mappings where available. Otherwise label cards `O001`, `O002`, etc. in input order, and linked requested actions `A001`, `A002`, etc. in prompt order. Record a resolvable file/record locator in `card_ref`. Reuse the same action ID wherever that action depends on several cards, and preserve mappings across report revisions. Retries, proposals, and recovery steps do not become new requested actions.

Within each obligation, include one record per linked requested action:

| Field | Required content |
| --- | --- |
| `action_id` | The requested action's stable ID. |
| `requested_action` | Description, supporting `prompt_excerpt`, and `type`: `read-only` or `state-changing`. Flag material card conflicts. |
| `observed_behavior` | Concise description of the answer, proposal, attempt, or achieved effects after recovery. `target_ids` contains established entities relevant to this obligation; use `null` when unestablished and `[]` when no target was selected. A deferred or failed action can still have an established target. |
| `evidence` | Relevant excerpts/facts and their source locations. Explain what they establish about the reference, outcome, or effect. |
| `grounding_assessment` | A verdict and evidence-backed reason under the definitions below. |
| `downstream_action_outcome` | An outcome under the definitions below, assigned independently of grounding. |
| `outcome_explanation` | What was achieved or remains unmet, including definite factual or execution failures. Distinguish an accurately reported inability from a false claim. Explain material recovery. |

The same action's requested action, whole-action outcome, and outcome explanation must agree wherever repeated. Grounding verdicts, relevant targets, and supporting evidence are relative to the enclosing obligation and may differ. The overall grounding assessment belongs to the obligation, outside its action list. Unexpected effects are recorded once at test level.

Evidence entries contain `source`, `location`, and `detail`. Use the schema's source labels; `domain_semantics` covers a cited supplied API definition/documentation passage or an explicitly stated general fact. A general fact cannot establish a particular entity's invented attribute.

### Assessment issues and incomplete judgments

An `assessment_issue` is normally `null`. For a material input inconsistency or an assessment that cannot be completed, provide a description and `blocked_fields`: JSON Pointers from the report root to the affected fields. Preserve all unaffected judgments.

- `not_established` is a completed reference judgment: available behavior establishes neither satisfaction nor a remaining violation. It does not mean the evaluator could not assess the evidence.
- A `null` verdict, action type, or outcome means the evaluator could not assign it. Identify the blocked field in an assessment issue.
- An input conflict can have `blocked_fields: []` when a supported interpretation permits all judgments.
- Use the obligation-level issue for its card/actions and the test-level issue for test-wide problems.
- `unexpected_effects: []` means no material unauthorized effects were established. Use `null` when this assessment could not be completed and no findings are confirmed. If some findings are confirmed but assessment remains incomplete, retain them and name `/unexpected_effects` in `blocked_fields`.

For overall grounding, a confirmed incorrect action makes the obligation incorrect even if another action is blocked. Otherwise a blocked action judgment blocks the overall judgment; otherwise apply the correct/not-established aggregation below. Do not treat missing linked-action information as vacuous evidence of correct grounding; record the assessment issue.

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

## Worked example

Suppose the prompt says: “Set project-alpha's topic to Release planning and post Release review is Friday there.” One card identifies channel `C_ALPHA`; it supports two actions. The final topic is correct, but the announcement says Monday.

| Linked action | Grounding | Outcome | Explanation |
| --- | --- | --- | --- |
| A001: set the topic | `demonstrated_correct` | `completed` | The requested topic is present on C_ALPHA. |
| A002: post the announcement | `demonstrated_correct` | `failed` | The new message is in C_ALPHA but says Monday instead of Friday. |

Overall grounding is `demonstrated_correct`: both actions use the intended channel. The wrong announcement content remains a definite answer/action failure in A002's explanation. Cite the card, prompt, and relevant initial/final facts in the actual report; this hypothetical example supplies no real evidence locations.

## Runner validation and later queries

The runner validates the JSON schema, card coverage, IDs and references, agreement of repeated action outcomes, assessment-issue pointers, and grounding aggregation. These are mechanical checks outside the evaluator's substantive assessment. The evaluator does not modify the schema or validation rules.

Count grounding obligations separately from actions. Deduplicate repeated actions by `(test_id, run_id, action_id)`. `failed` alone does not establish an agent violation: retain its explanation and evidence. Post-processing can classify concrete findings and distinguish acknowledged limitations, fabricated answers, false completion claims, and other failures. Assessment issues indicate incomplete assessment, not agent bugs; preserve confirmed findings in unaffected fields.
