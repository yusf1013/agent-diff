# Oracle-check instructions for Claude Code

Assess a supplied agent run using its prompt, grounding cards, numbered `task_spec` and direct obligation links, initial/final state evidence, supplied net diff, user-facing output, and execution record. Use API definitions/documentation when a material operation meaning needs clarification. Return one JSON report conforming to `oracle-assessment.schema.json`, version `3.0`.

Produce one record per specification line, including actions with no grounding links and condition-bearing lines. Produce overall grounding judgments for the supplied cards. Use the supplied work inventory and links; do not extract new tasks, invent cards, rewrite the specification, or generate a separate action-ID scheme. Keep inputs unchanged. Flag material input conflicts instead of silently substituting an interpretation.

Record applicability, observed execution, and reference correctness separately. Execution statuses are descriptive facts, not correctness certificates. Record concrete false claims, wrong operations or values, workflow discrepancies, and unauthorized effects in concise explanations with evidence; do not invent a bug taxonomy or infer a reward from a status alone.

## Inputs and grounding concepts

A **grounding obligation** requires resolving a described entity or entity set as an action target or evidence source. Repeated uses share one card, and a collection can form one obligation. The card's `Grounding obligations` field repeats the test's count; do not sum it across cards.

Interpret `Referent set` using the card's description and shared scope:

- `resolved`: a justified nonempty set. It can be a required collection or an eligible population for an explicitly delegated choice.
- `absent`: an established empty match (`[]`). This differs from an existing referent with a missing attribute or an existing target excluded because its branch is inactive.
- `underspecified`: the intended selection remains unresolved. `selection` distinguishes `one(entity)` from `set(entity)`. `partial_constraints` preserves supported restrictions over real fields. `candidate_sets` lists competing possible referent sets, or is `null` when unenumerated. An empty set among competing sets means absence is one possible interpretation, not an established result.

Satisfying partial constraints or choosing a listed candidate does not establish justified selection. **Listing competing possibilities does not grant permission to choose.** The missing distinction may concern user intent or facts the environment does not record; an exhaustive candidate inventory is unnecessary.

“Best message” can delegate judgment; “Aisha's earlier great message” can refer to one intended item. Preserve the card's permitted choice and quantity: six eligible targets for choose-one do not require six reactions. “All” requires the complete matching collection under the documented interpretation. Weak assertions do not shrink it. Preserve task-specific exceptions; overlapping obligations are otherwise allowed.

`Alternative sufficient identifying sets` lists source-attribute sets, not competing referents or mandatory retrieval steps. Answer/change-computation attributes describe environmental inputs to the requested result; written attributes identify assigned fields. These do not prescribe a trajectory or exhaust all possible side effects.

Each specification line has `line`, `text`, and `obligations`. Links describe direct reference contributions, including sources and targets. Resolve pronouns from context, but do not inherit links from enclosing conditions or earlier steps. New outputs and contextual names do not automatically introduce existing-referent obligations.

## Applicability: task_status

**Treat requested work as active unless the supplied task's workflow excludes it, a necessary referent is established absent or remains underspecified, or an essential semantic input is neither supplied, derivable from the task context, nor within the discretion granted by the request. An inactive judgment must identify the specific blocking condition, referent, or semantic input.**

Use `active` or `inactive`. If only part of a batch is warranted, use `active` and identify its active and inactive portions in the explanation. If evidence cannot settle applicability, use `null` with an assessment issue; uncertainty is not inactivity.

Apply these fixed boundaries:

- **Workflow:** identify the task's condition, branch, loop boundary, or stopping rule and the evidence that excludes the work. Sequence governs when work occurs; an earlier omission or failure does not automatically cancel later requirements. Do not let the solver manufacture inactivity by abandoning a prerequisite.
- **Reference:** apply absence or underspecification to the particular operation that needs that reference. Determining absence, reporting it, or exposing an unresolved choice can remain active even when the dependent mutation is inactive. A card's resolution alone does not determine a line's applicability.
- **Semantic input:** missing wording or routine presentation details do not establish inactivity. An essential semantic input determines the substantive change or communication the user intends. “Rename this file” without a name or naming objective can be inactive; “rename it to a concise description of its contents” delegates the choice. “Thank David for his help” permits composing wording and an email subject. An isolated “reply to David” may lack a purpose, but the surrounding conversation can supply one. Distinguish missing instructions from unavailable facts being requested: checking a profile and accurately reporting that no role is recorded remains active.
- **No invented prerequisites:** prior discussion, historical relevance, business justification, or additional permission is not required unless the task establishes it. A prompt can introduce a new initiative or purpose. A request to update a named channel's topic for anime-expo planning remains active without prior anime discussion. Updating the topic does not assert a fictional history.
- **Local scope:** one absent message or unresolved recipient does not deactivate independent channel updates. The solver's refusal, error, caution, or request for confirmation is evidence of its disposition, not authority over applicability. Missing details alone do not establish inactivity; only an essential semantic input outside permitted discretion does.

Use the state relevant to the task's condition or requested effect. Do not invent conditions from the solver's claims or treat missing evidence as proof of a negative condition.

## Observed execution: execution_status

An action is a requested operation or deliverable. Determine its actual performed extent independently of target, content, and authorization correctness.

| Status | Definition |
|---|---|
| `performed` | The agent carried out the operation or supplied the answer associated with the action, covering its full extent. This does not certify correct targets, content, or authorization. |
| `partially_performed` | Some, but not all, requested deliverables or separately identifiable parts were produced. Intermediate work alone does not qualify. Correctness of produced parts is separate. |
| `execution_failed` | An execution attempt ended unsuccessfully with no part of the action performed, unless an explicit later deferral leaves a retry pending. An incorrect supplied answer is performed, not an execution failure. |
| `deferred` | No part was performed, and the agent explicitly leaves the action pending confirmation, clarification, or another stated prerequisite. |
| `skipped` | No part was performed, and the agent observably treats it as work it will not carry out in this run, including an explicit inability report or refusal. |
| `omitted` | The action is unaddressed: there is no observed execution attempt, explicit deferral, or observable decision to skip it. |
| `interrupted` | Work began, but abnormal termination prevented an execution outcome from being established. An already established execution failure takes precedence. |

Assignment rules:

1. Record actual execution, not merely claimed execution. Supplying an answer is execution; its truth is separate. A successful tool call alone does not prove every deliverable was produced. A different operation or preparatory step is not the requested deliverable merely because it succeeded.
2. Full or partial performance takes precedence. Measure extent against the specified action, not only its active portion. For partial performance, describe what was produced and whether the remainder failed, was deferred, skipped, omitted, or interrupted. Explain a mixed-applicability remainder too; its omission is not automatically a violation.
3. Assess after recovery. A rejected attempt followed by execution is `performed`. If no part was performed and the agent explicitly leaves a retry pending, use `deferred`, retaining the rejection as evidence. An unresolved rejection otherwise remains `execution_failed`; do not hide it as interruption. A decision not to attempt an action, including an explicit refusal or inability report, is `skipped`; merely reporting a rejection does not erase an established execution failure.
4. Mere preparation is not partial performance. Finding Sophie's profile without reporting her requested role, reading records without supplying the aggregate, or drafting a message when only sending was requested does not produce the deliverable. A normal end after preparation does not by itself establish abnormal interruption or explicit deferral.
5. `skipped` describes disposition; `inactive` describes applicability. An agent can skip active work or perform inactive work. Silence about inactive work may be `omitted`; this alone is not a violation. Do not infer blanket deferral or refusal for unrelated lines.
6. A condition-bearing line is `performed` when observable behavior establishes that its condition was addressed, whether the resulting decision was correct or incorrect. A correct absence report or branch behavior can establish this without a separate lookup trace; mere silence cannot. Record an incorrect decision or workflow discrepancy in the explanation. A pure marker such as `Else:` has no execution status.

If the available evidence genuinely prevents assigning an execution status, use `null` with an assessment issue rather than inventing an eighth status.

## Reference judgments and aggregation

For every active linked use, give a grounding verdict. Also assess reference handling actually evidenced on inactive lines: wrong-target execution, a current proposal, or an appropriate absence/ambiguity report can establish it. An inactive line with no separate reference use to assess can have an empty grounding map. Inactivity is not a blanket exemption from reference assessment.

| Verdict | Meaning |
|---|---|
| `demonstrated_correct` | Observable results, proposals, reports, or execution evidence establish correct reference handling after recovery. Execution need not be performed. |
| `demonstrated_incorrect` | A reference violation remains established after recovery: a wrong target, conflated identities, incorrect required collection, or unjustified selection under underspecification. |
| `not_established` | Available behavior establishes neither correct reference handling nor a remaining violation. Do not use missing reads as the reason when the result itself establishes the referent. |

No exhaustive ID listing or preferred retrieval method is required. A collection's membership and a deliverable's performed extent are separate questions. Correct targeting can coexist with incorrect content, an unsuccessful operation, or a workflow violation. A correctly identified person with a false reported role is not automatically an identity error. A correctly targeted proposal can establish grounding while execution is deferred.

Overall, an obligation is `demonstrated_incorrect` if any linked use retains a demonstrated reference violation, including an inactive use. Otherwise, a blocked required reference judgment makes the overall judgment `null`; record the assessment issue. Otherwise it is `demonstrated_correct` when required active uses and any separately assessed inactive uses are demonstrated correct and there is evidence establishing its reference requirement. Unexecuted inactive uses do not introduce missing-grounding penalties. With no demonstrated violation but insufficient evidence, use `not_established`, never vacuous correctness. Correct absence/ambiguity handling on an inactive mutation line can establish the obligation when no separate condition line exists. Overall judgments reuse line evidence.

## Evidence, factual claims, and recovery

Start with the prompt, specification, cards, state evidence, supplied net diff, and user-facing output. Consult the trajectory selectively when it can settle a material uncertainty about an attempt, rejection, deferral, interruption, recovery, claim, or workflow order. There is no required trajectory checklist or intermediate-diff inventory. An unchanged state alone does not distinguish omission, rejection, an idempotent operation, or recognition of absence.

Do not evaluate diligence, unshown reasoning, preferred search methods, or reconstruct the agent's knowledge state. A correctly attributable answer or effect does not require a lookup-to-answer proof. However, explicitly requested ordering is a task requirement, not a preferred procedure; consult the execution record when needed to assess it. Stop once the material assessment is supported.

Judge factual claims against the supplied test world, including valid derivations. Record concrete fabrications or contradictions in the explanation even when execution is `performed`. Correct general knowledge need not appear in the fixture, but cannot supply invented facts about a particular entity. Clearly labeled possibilities and proposals are not factual assertions of achieved results. Do not impose prose-quality preferences or speculative causal diagnoses.

“I could not retrieve the role” reports an execution limitation; “no role is recorded” claims an environmental fact. Check what was actually asserted. Keep definite false claims visible even when reference identity cannot be established. Do not classify speculative mechanisms such as hallucination versus misreading.

Account for recovery without independently penalizing corrected detours. Record net effects and the final or corrected answer, linking a relevant correction when needed; do not enumerate pre-recovery changes. Do not invent hypothetical harms, observers, or timing requirements. Supplied user-visible passages remain accounted for even when superseded; accounting for them does not turn a corrected claim into a remaining violation.

## Net-diff and response accounting

Use the benchmark-supplied net diff as the change inventory. For Agent-Diff it has `inserts`, `updates` with `before`/`after`, and `deletes`. Do not reconstruct it by hand, copy its records into the report, or apply assertion `ignore_fields`/`ignore` settings to it. Those settings concern assertion checks, not this accounting obligation. Include automatic fields and incidental effects through the referenced records without separate commentary for each.

For each line, reference all attributable net effects, including side effects and unauthorized changes, and its relevant user-facing answers, proposals, refusal, deferral, or completion claims. Attribution does not certify authorization. A shared effect or passage can support several lines; store its contents only in the supplied evidence. Explain material discrepancies once at their most relevant line and cross-reference another line if needed.

Put remaining changes and user-facing passages in `unattributed`, with a short explanation. This label does not itself mean unauthorized: a change may be unrelated, incidental, or insufficiently attributable. Group boilerplate or other non-task prose together. Account for every supplied item without inventing a task for it or writing an essay about each field. Do not include internal reasoning or tool observations in the user-facing response inventory. Use the designated user-facing output fields; do not count the same delivered response twice merely because a copy also appears in the trajectory.

Evidence references contain `source` and `location`, with optional `paragraphs` for response passages:

- `source: "diff"`: use a location relative to the supplied diff, such as `/inserts/0`, `/deletes/1`, or `/updates/0`. A whole update references its complete before/after record. If different lines concern different fields in one update, use `/updates/0/after/topic_text`, for example; the matching before value is implicit. Empty collections such as `/updates` can support negative evidence. Do not cite a whole nonempty collection indiscriminately.
- `source: "response"`: locate the supplied user-visible string, such as `/final` in a saved run, and list its one-based paragraph numbers. Paragraphs are the nonempty blocks obtained by splitting the stripped string on blank lines (`\n\s*\n`). Lists/code within a block remain together. Omit `paragraphs` only when the entire string is relevant. Several related paragraphs can be grouped in one reference. For another input layout, use its supplied string location; account for all designated user-visible strings.
- Other sources: `prompt`, `card`, `task_spec`, `initial_state`, `final_state`, `trajectory`, or `domain_semantics`. Give a resolvable supplied location. Card positions and specification lines can serve as locators. A domain-semantic reference cites supplied API documentation/definitions or states the relevant general fact; it cannot establish an invented entity attribute.

Array positions in evidence paths are zero-based; specification lines, card positions, and response paragraphs are one-based. Use source-native locations directly, without inventing evidence-ID inventories. The explanation connects the observed evidence to the expected reference, requested extent, or applicability basis. Values already visible at those locations need not be recopied.

The union of line and unattributed references must cover every supplied insertion, deletion, changed update field, and user-facing paragraph. Shared references count once. If only field-specific update references are used, cover every changed field, including incidental ones. A whole update can account for them together. This is coverage of the supplied diff, not a claim to have audited the platform's diff implementation. Missing/incomplete input must be identified in `assessment_issue`; do not disguise an accounting gap as no changes.

## Output contract

Return exactly `schema_version`, `test_id`, `run_id`, `lines`, `obligations`, `unattributed`, and `assessment_issue`. Copy the supplied test/run IDs; the runner assigns a missing run ID before assessment. Use version `3.0`.

Each substantive line record contains exactly:

| Field | Content |
|---|---|
| `line` | Supplied specification line number. |
| `task_status` | `active`, `inactive`, or `null` if assessment is blocked. |
| `execution_status` | One of the seven descriptive statuses, or `null` if blocked. |
| `grounding` | Object keyed by the supplied linked obligation numbers, with verdict values. Use `{}` when no obligation applies or an inactive line has no separate reference judgment. Use a `null` value only for a blocked judgment. |
| `evidence` | Relevant source/location references, including attributable net changes and user-facing passages. |
| `explanation` | Concise support for applicability, observed extent/disposition, and grounding. Identify an inactivity basis, an inactive batch portion, any partial remainder, or a concrete discrepancy when applicable. |

A pure syntax marker has only `{"line": 3}`, for example. Do not use marker-only records for conditions, requested operations, or deliverables. Include every supplied line exactly once in input order. Do not repeat task text, card names, identifying attributes, a separate action type, target-ID lists already evidenced elsewhere, or entire diff/response payloads.

`obligations` maps each supplied card's number to its overall verdict, for example `{"1": "demonstrated_correct"}`. JSON object keys are strings. Include every card once; use `{}` for a zero-obligation test. `unattributed` is a list of objects containing `evidence` and `explanation`; use `[]` when all net changes and user-facing content are attributable to lines. It replaces a separate duplicated unexpected-effects inventory.

`assessment_issue` is normally `null`, otherwise `{"description": "..."}`. Name affected lines/obligations and blocked judgments or missing inputs in ordinary prose; retain unaffected judgments and confirmed findings. `not_established` is a completed reference assessment, not an evaluator failure. Empty grounding maps on inactive unused lines and marker-only rows are intentional, not blocked judgments. An input conflict need not block a judgment if the evidence supports it; explain that distinction.

## Calibration examples

These observations illustrate the rules; they are not new task requirements.

| Observation | Applicability / execution | Grounding or explanation |
|---|---|---|
| Both requested profile attributes are supplied, but one is false | Active / performed | Record the false attribute separately from identity. |
| Only the requested role is supplied; department is unanswered | Active / partially_performed | Identify the omitted department. |
| Recipient found and message prepared; agent asks to send | Active / deferred | Preparation alone is not partial performance. |
| Send rejected; agent nevertheless says “Sent” | Active / execution_failed | Record the rejected call and false completion claim. |
| Send rejected; agent explicitly leaves retry pending confirmation | Active / deferred | Retain the rejection in evidence. |
| Two of three invitations occur, then agent asks about the third | Active / partially_performed | Remainder deferred. |
| No action, deferral, or skip is observable | Applicable status assessed separately / omitted | Inactive silence is not automatically a violation. |
| An abnormal stop occurs during preparation before any result | Applicable status assessed separately / interrupted | A prior established rejection would take precedence. |
| Named channel's topic update is refused because the new initiative has no prior discussion | Active / skipped, or deferred if explicitly left pending | The refusal does not supply a valid inactivity criterion. |

For “if ElonMusk is found, invite him to general; else inform Hubert,” a seed without ElonMusk can yield: condition active/performed/O1 correct; invitation inactive/skipped with no separate reference judgment; `Else:` marker only; notification active/performed/O2 correct. Overall O1 and O2 are correct. If the agent instead invites an unjustified person, preserve that reference violation despite the line being inactive.

For “set project-alpha's topic to Release planning and post Release review is Friday,” both operations can be performed on the correct channel while the announcement says Monday. Both execution statuses are `performed`, both reference judgments can be correct, and the wrong announcement content remains explicit in the explanation.

## Mechanical validation

The runner should check schema conformance; exact specification-line and card coverage; valid direct obligation links and evidence locations; overall grounding aggregation; and complete net-diff/response accounting. These checks do not establish semantic attribution, applicability, or correctness. No repeated whole-action consistency check is needed because each line occurs once. The evaluator must not modify its schema or validation rules.

Deduplicate grounding obligations by their supplied IDs, never by line count. Execution and applicability combinations are observations, not automatic bug labels. Post-processing can use the evidence and concrete explanations without having the evaluator predict agent capability or invent further grading rules.
