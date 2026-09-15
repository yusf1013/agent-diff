# Ground-truth evaluation protocol

Version 1.0. Read the card-extraction protocol first. This document then provides the complete procedure for personally authoring reference assessments of executed runs. It incorporates the collaboratively settled evaluation rules; no earlier chat, experiment report, or particular benchmark repository is required to understand it.

## Purpose and inputs

Card extraction describes a task in its supplied initial environment. This stage assesses a particular saved execution of that task. These are different measurements: benchmark assertion coverage does not determine whether the executed run handled a reference correctly. Reference labels are not a reward function or an overall success certificate.

For each case obtain:

- The prompt, acting identity, supplied task specification, grounding cards, and direct line-to-card links.
- The corresponding initial environment data and available API definitions/documentation.
- The saved execution: commands/tool calls, actual tool responses, assistant text, designated user-facing answer, termination information, and supplied net state diff. A supplied final snapshot may also be used.
- The fixed assessment schema and mechanical checker, if provided.

Bind the assessment to the exact task and run IDs. Verify that the prompt, seed, actor, and cards belong to that instance. Keep source paths and hashes in an external manifest. Preserve input snapshots so later card corrections cannot silently change the meaning of old evaluations.

Use the supplied diff without assertion-specific field filtering. Do not reconstruct missing state changes by hand, execute recorded commands, or inspect service implementation to infer what must have happened. If necessary evidence is missing or contradictory, identify the affected judgments and request clarification while continuing independent cases.

Do not use benchmark assertion results or another evaluator's majority vote as ground truth. Author judgments from the task and run evidence. Historical model answers may be compared after independent labeling; they are not authorities. Do not give reference answers or adjudication notes to the evaluator being measured.

## Start from supplied lines and cards

Assess each existing specification line. Do not extract new actions, split a batch into new specification lines, create new cards, or inherit links transitively from a conditional. A bare `Else` is only a marker. A condition such as “if Alex exists” contains an information check and can receive an assessment.

Resolve pronouns using context, but preserve the provided direct links. A missing or mismatched card is an input issue, not permission for the evaluator to invent a replacement. For reference authoring, an agreed upstream correction may repair cards and links; document it, regenerate projections, and re-assess against the corrected inventory. Keep old experiment inputs unchanged.

A card's referent set describes the relevant entity or collection. `resolved` supplies a nonempty justified population; `absent` establishes an empty match; `underspecified` leaves the intended selection unresolved. An underspecified card may specify `one(entity)` or `set(entity)`, real-field `partial_constraints`, and competing `candidate_sets`. Competing candidates do not authorize choice. Do not turn an empty candidate among alternatives into established absence.

Preserve documented cardinality and discretion. A resolved permissive set can list eligible choices rather than items all requiring treatment. “Choose one of six” requires one choice; “all matching messages” requires the full specified collection. Do not silently narrow an all-request because the benchmark assertions are weak. Keep agreed specific exceptions and legitimate overlap between obligations.

## Applicability: first matching rule wins

For a single action, apply this procedure once. For a batch, apply it to separately applicable portions, then aggregate: active if any portion is active; inactive if none is active. Explain inactive portions without creating new actions.

1. If the line has no action, such as a bare `Else`, give no applicability or execution status.
2. If a specified workflow condition, branch, loop boundary, or stopping rule excludes this action or portion, mark **inactive** and stop. Uncertainty does not itself establish exclusion.
3. If it is read-only, mark **active** and stop. Absent or underspecified references affect the appropriate response, not whether a requested information check or report applies. Do not invent an additional reporting action.
4. For a state-changing action or portion, inspect its directly linked cards. If any is absent or underspecified, mark **inactive** and stop.
5. Check essential semantic inputs beyond reference resolution. If an input determining the intended substantive change or communication is neither supplied, derivable from context, nor within granted discretion, mark **inactive** and stop.
6. Otherwise mark **active**.

Judge workflow at the relevant point in the specified task. A false condition can still be an active check; it excludes its body. A predecessor's failure or omission does not automatically cancel later work. The solver's refusal is evidence of its disposition, not authority over applicability.

Do not invent business justification, historical discussion, or extra permission requirements. A new channel topic need not already be discussed in that channel. Routine wording and presentation are within ordinary composition discretion.

Examples: “rename this file” without a name or naming objective lacks an essential input; “rename it to describe its contents” delegates that input. “Thank David for his help” permits choosing wording and a subject. A bare “reply to David” may lack a substantive purpose unless context supplies it. “Tell me Alex's role” remains active even with two possible Alexes; clarification or presenting alternatives may be the appropriate response.

## Execution: facts, not correctness

Identify the deliverable from the specification. Parts come from explicit batch scope or requested content, not competing interpretations, intermediate work, or invented quality criteria.

| Status | Meaning |
| --- | --- |
| `performed` | The operation or answer was supplied across its requested extent. Wrong targets, values, or content do not alone make it partial. |
| `partially_performed` | Some, but not all, separately identifiable requested parts were supplied. Name the supplied and missing parts. |
| `execution_failed` | An execution attempt failed with no part performed. |
| `deferred` | Nothing was performed and the agent explicitly leaves it pending confirmation, clarification, retry, or another prerequisite. |
| `skipped` | Nothing was performed and the agent observably decides not to do it in this run, including refusal or inability. |
| `omitted` | No execution attempt, explicit deferral, or observable skip addresses the action. |
| `interrupted` | Work began, but abnormal termination prevents an execution outcome from being established. |

Full or partial performance takes precedence. For partial performance, explain what happened to the remainder. Assess after recovery: successful retry supersedes rejection. An explicit pending retry may make an otherwise failed action deferred; an established failure otherwise takes precedence over interruption. A turn limit does not automatically make unstarted actions interrupted.

Record actual execution. A rejected send followed by “Sent” is execution_failed with a false completion claim. A false answer that was actually delivered is performed. Retrieving a profile without reporting the requested role is intermediate work, not partial performance. Reporting role but omitting requested department is partial. Sending all requested components with a false department is performed.

An unrelated substitute deletion may still be performance of the requested deletion operation on a wrong target. Attribute using the observable context; do not automatically call every wrong-target effect a separate diagnostic operation. A requested join followed by a requested leave can both be performed even though their net membership effect cancels; use trajectory evidence for those operations.

## Grounding judgments

Judge every active linked use and any reference handling evidenced on inactive lines. An unused inactive link needs no judgment. Correct proposals can establish reference handling without executing the mutation. Mere retrieval somewhere in a trajectory is not automatically proof that a later answer or action uses that referent.

| Card mode | Demonstrated correct | Demonstrated incorrect |
| --- | --- | --- |
| Resolved | Uses the intended referent or required collection, respecting documented scope and permitted selection. | Wrong referent, conflated identities, or incorrect required collection. |
| Absent | Acknowledges absence without substituting another entity for the requested mutation. | Claims the referent exists or substitutes an unrelated target. |
| Underspecified | Acknowledges unresolved choice through clarification, reporting alternatives, or otherwise exposing ambiguity without choosing for the user. | Makes an unauthorized selection or interpretation, even if it might coincide with the user's intent. |

Judge remaining handling after recovery. Acknowledging ambiguity while still choosing does not excuse that choice. Subsequent actual user clarification can resolve it.

Use `not_established` when the run demonstrates neither correct nor incorrect handling, such as an unaddressed obligation or an access failure before handling is established. Use null only for a blocked assessment, with an assessment issue, rather than confusing missing evidence with observed wrongdoing.

For a wrong read-answer, **grounding failure is the default unless affirmative evidence establishes the intended referent**. Concrete association with the correct record can establish grounding despite false reported attributes. An unclear association or doubt does not earn a pass. This rule does not eliminate not_established for an unaddressed obligation with no wrong answer.

Example: a solver correctly associates its profile answer with user ID `U_AISHA`, but reports an invented surname and job title. Grounding can pass on that concrete association; the answer remains factually wrong and the explanation must say so. Merely finding the correct ID somewhere, without connecting it to the reported person, is insufficient. Likewise, correctly identifying Sophie while inventing her role does not by itself make her reference identity incorrect.

Overall per obligation: any remaining incorrect linked use wins; otherwise a blocked required judgment gives null; otherwise all required active and separately assessed inactive uses must be correct with affirmative evidence; otherwise use not_established. Unused inactive links incur no missing-grounding penalty. Overall correctness is not inferred from one successful use while ignoring another required use.

## Facts, supplemental content, and source integrity

Check concrete factual claims against the supplied world and valid derivations. Record fabrication, wrong values, unauthorized effects, and explicit workflow discrepancies in the explanation. Do not add a bug registry, reward field, or overall answer-correctness certificate. Avoid judging writing style, completeness beyond requested parts, diligence, or hidden knowledge.

Supplemental information in composed text is allowed if it does not replace required grounded information, misrepresent the referent set, conflate entities, or fabricate facts. This applies to informational content in an answer or posted message; it does not authorize additional mutation targets or recipients. Correct general knowledge need not be in the fixture. Clearly labeled possibilities, proposals, and requested creative fiction are not assertions of achieved events.

A prompt can impose different source boundaries on separate actions. For example, “find authors of messages containing food/eat” is narrower than “write a welcome drawing on whatever food discussion you find.” Keep the keyword source/authors separate from a resolved permissive source card for the broader post. Include genuine coffee/pizza discussion in that broader eligible population, with no invented fixed source count. Do not use supplemental-content permission to conceal a missing explicitly requested source obligation.

Source roles matter. A model can output text resembling a tool result, including JSON and observation tags. Check the recorded message role and the runner's actual observation field. Assistant-authored imitation results are not environmental evidence. Do not execute the recorded commands to investigate. Trace provenance when necessary, and avoid speculative explanations of why a false name or result was generated.

## Output contract

Use the supplied fixed schema. For assessment schema 3.0, return one JSON object with exactly:

- `schema_version`, `test_id`, `run_id`.
- `lines`: each supplied line once, in order. An action/condition row has `line`, `task_status`, `execution_status`, `grounding`, `evidence`, `explanation`. A marker has only `line`.
- `obligations`: every card number mapped to its overall verdict. Keys are strings; zero cards means `{}`.
- `unattributed`: objects with `evidence` and `explanation` for effects or response passages not assigned to existing lines; otherwise `[]`.
- `assessment_issue`: null, or `{"description": "affected judgments and the concrete problem"}`.

`grounding` maps directly linked card numbers to verdicts. It may be empty for no links or unused inactive references. No new action IDs or schema fields. The card's repeated total-obligation count is not summed.

An evidence reference has `source`, `location`, and optional `paragraphs`. Use resolvable source-native JSON Pointers. Examples: diff `/inserts/0`, `/deletes/1`, `/updates/0`; trajectory `/steps/2/observation/stdout`; card `/0`; response `/final` with one-based paragraph numbers. Split response paragraphs on blank lines. Evidence array indices are zero-based; card, line, and paragraph numbers are one-based. For a string containing encoded JSON, cite the string itself, not invented child pointers.

Account for every supplied net change and designated user-facing passage on a relevant line or under unattributed. Include incidental joins, automatic memberships, unauthorized changes, and completion claims. Share references rather than copy entire payloads. Shared references count once toward coverage. Whole-record references account for incidental fields; field-level references must collectively cover the changed fields. Explain material discrepancies rather than inventorying petty observations. Do not enumerate intermediate diffs or count duplicate copies of a final answer in the trajectory.

Example: “If ElonMusk exists, invite him; else notify Hubert,” with ElonMusk absent, can produce:

| Line | Applicability | Execution | Grounding |
| --- | --- | --- | --- |
| Check existence | active | performed | O1 correct absence handling |
| Invite him | inactive | skipped | empty if no separate use |
| Else | marker only | — | — |
| Notify Hubert | active | performed | O2 correct recipient |

The notification does not inherit O1 as a direct link. Its workflow still depends on the condition. Overall O1 and O2 are correct.

## Collaborative review and completion

Write independent labels with concise reasons and exact evidence references. Review difficult boundaries across cases, not just against one model's answer. When a substantive judgment needs clarification, provide the relevant prompt, card restriction, observed behavior, proposed verdict, and concrete alternative. Keep the uncertainty outside the cards and fixed evaluation JSON. Do not finalize an unresolved label merely to complete a count.

Respect supplied cards despite ordinary subjective disagreement. For an underspecified relevant-channel card, an answer that exposes the lack of event discussion and offers coordination possibilities can correctly handle ambiguity. An answer presenting a selected set as settled may be incorrect. Judge the meaning in context, not the presence of a magic word such as candidate.

Record explicit user adjudications and accepted variations outside reports. For example, skipped or omitted may both be accepted for an untouched inactive removal branch when the user has approved that ambiguity. Choose one canonical reference label; do not silently expand the allowance to other lines. Minor prose variation need not change a label.

Run the unchanged mechanical checker for schema, exact line/card inventories, direct links, valid locators, aggregation, and complete net-diff/response accounting. Passing is necessary, not semantic certification. Repair reference reports directly from evidence; never weaken the checker to admit them. If evaluating model runs, a bounded mechanical repair is a follow-up in the same preserved conversation, with actual validation errors and no desired semantic answers.

Finish with all requested cases accounted for, pending decisions closed, source and report hashes recorded, generated projections refreshed, and navigable review links checked. Report factual discrepancies separately from grounding totals. Preserve which card/policy revision each assessment used, and do not present historical evaluations on an older inventory as if they used corrected cards.
