# Lean oracle-check instructions

## Assessment rules

Assess the supplied run against its prompt, grounding cards, task specification and direct links, state evidence, net diff, and user-facing output. Keep inputs unchanged; extract no new tasks, cards, or links. Use API definitions/docs as needed. Assess applicability, execution, and grounding separately. Record concrete discrepancies, not reward labels.

A grounding obligation resolves an entity or collection as target or source. Repeated references share a card. `resolved` means a justified nonempty referent set; `absent` means an established empty match; `underspecified` means unresolved selection. `selection` specifies one/entity-set; `partial_constraints` restrict candidates; `candidate_sets` lists competing sets or is null when unenumerated. Candidates do not authorize choosing. An empty candidate is not established absence. Preserve documented scope, quantity, delegated discretion, and exceptions. Identifying/computation attributes describe inputs, not mandatory retrieval steps.

**Applicability:** For each line in task spec, follow this decision procedure.

For a single action, apply the decision procedure below once.

For a batch, apply it to each separately applicable portion, then aggregate:
- **Active:** at least one portion is active.
- **Inactive:** no portion is active.

Record which portions are inactive and why. These portions remain within the existing batch action; this does not create additional task specifications.

First match wins:

1. If this line has no action, e.g., just an "Else", stop here. Active/inactive doesn't apply if there is no task.
2. **Check workflow exclusion in task specs.** If the specified condition, branch, loop boundary, or stopping rule excludes this action or portion, mark it **inactive** and stop.
3. **Check whether the action is read-only.** If so, mark it **active** and stop. Absent or underspecified references do not themselves deactivate a requested report or information check; they affect what response is appropriate. This rule does not introduce additional read actions into the task specification.
4. **Check resolution modes of the linked grounding obligation.** For this state-changing action or batch portion, inspect its directly linked grounding cards. If any has resolution mode **absent** or **underspecified**, mark it **inactive** and stop. Otherwise continue.
5. **Check essential semantic inputs beyond reference resolution.** If an input necessary to determine the intended substantive change or communication is neither supplied, derivable from context, nor within the discretion granted by the request, mark the action **inactive** and stop.
6. **Otherwise, mark the action active.**

Apply the rules in order. Once a rule assigns a status, stop evaluating that action or portion. Later rules do not override earlier decisions. Batch aggregation occurs only after its portions have been assessed.

> Assess the specified action using the request and relevant environment conditions, independently of the solver's choice to execute, refuse, defer, or stop. Evaluate workflow conditions at the relevant point in the specified workflow; a predecessor's not yet having executed does not, by itself, permanently exclude its successor.

> Do not invent prerequisites, require prior environmental evidence of a newly requested purpose, or treat routine wording and presentation choices as missing essential inputs.

**Execution:** assess actual deliverables after recovery, independently of correctness or applicability.

A deliverable is the requested operation or user-facing result identified in the task specification. Separately identifiable parts come from its batch scope or explicitly requested content. Intermediate work, competing interpretations in grounding cards, and evaluator-invented quality criteria are not additional deliverable parts.

- `performed`: The agent carried out the requested operation or supplied the requested result, covering all requested parts. Incorrect targets, values, or claims do not by themselves make execution partial.
- `partially_performed`: The agent carried out or supplied at least one, but not all, separately identifiable requested parts. Name the produced part and the missing part, tying both to the task specification.
- `execution_failed`: unsuccessful attempt, no part performed.
- `deferred`: no part performed; explicitly pending a prerequisite.
- `skipped`: no part performed; observably will not act, including refusal/inability.
- `omitted`: unaddressed, without attempt, deferral, or skip.
- `interrupted`: abnormal termination prevents establishing an execution outcome.

Performance takes precedence; preparation is not partial performance. Explicit pending retry can supersede rejection; otherwise established rejection supersedes interruption. Condition-bearing lines are performed when observably addressed, even incorrectly. Inactivity does not imply skipping, and execution does not imply applicability.

**Grounding:** judge every active linked use and reference handling evidenced on inactive lines. Assess handling after recovery. Use `demonstrated_correct` for correct handling and `demonstrated_incorrect` for remaining reference violations, applying the card as follows:

- **Resolved:** Correct handling uses the card's referent or required collection, respecting its documented scope and quantity. Where selection is delegated, a permitted choice satisfies the reference requirement. Wrong referents or violations of the required collection constitute incorrect handling.
- **Absent:** Correct handling acknowledges absence without substituting another entity for the requested mutation. Claiming the referent exists or performing that mutation on an unrelated substitute is demonstrated incorrect.
- **Underspecified:** Correct handling acknowledges the unresolved choice without deciding for the user—for example, asking for clarification or reporting alternatives as alternatives. Choosing a referent or interpretation without granted authority is demonstrated incorrect, including in a read-only answer. Acknowledging ambiguity does not authorize choosing anyway. Subsequent user clarification can resolve the choice.

Use `not_established` when the available run evidence demonstrates neither correct nor incorrect reference handling—for example, the obligation is unaddressed, or access fails before any reference handling is established. Do not use it merely because an unauthorized choice might coincidentally match the user's intent.

Correct proposals or absence/ambiguity reports can establish grounding without execution. Overall, any remaining incorrect use wins; otherwise a blocked required judgment gives null; otherwise all required active and separately assessed inactive uses must be correct with affirmative evidence; otherwise use not_established. Unused inactive links incur no missing-grounding penalty.

Consult trajectory selectively for material uncertainties or required workflow order. Do not grade diligence, missing reads, or hidden knowledge. Check factual claims against the test world and valid derivations; distinguish false content from wrong references. Respect general knowledge, labeled possibilities/proposals, and recovery. Explain concrete factual, operation, content, authorization, or workflow discrepancies without speculative causes.

Account for every supplied net change and user-facing passage using evidence references on relevant lines or `unattributed`. Include incidental/unauthorized effects; attribution does not certify authorization. Share references, not copied payloads. Use supplied diffs unchanged; do not reconstruct them or apply assertion ignores. Account for corrected passages without penalizing recovered errors. Flag missing evidence/input conflicts; preserve unaffected judgments. Never edit the schema/checker.

## Examples

With two indistinguishable Alexes, “Which Alex?” or reporting both (e.g., "I found two Alexes...") or presenting them as alternatives demonstrates correct ambiguity handling. Silently selecting one demonstrates incorrect handling. Omitting the request entirely leaves handling not established.

“Message Alex the date, location, and agenda”: sending the date and location while omitting the agenda is `partially_performed`. Supplying all three with an incorrect location is `performed`, with correctness assessed separately.

A rejected attempt followed by execution is `performed`.

An agent can skip active work or perform inactive work. Silence about inactive work may be `omitted`; this alone is not a violation.

“Best message” can delegate judgment; “Aisha's earlier great message” can refer to one intended item. Preserve the card's permitted choice and quantity: six eligible targets for choose-one do not require six reactions. “All” requires the complete matching collection under the documented interpretation. Weak assertions do not shrink it. Preserve task-specific exceptions; overlapping obligations are otherwise allowed.

“Rename this file” without a name or naming objective can be inactive; “rename it to a concise description of its contents” delegates the choice. “Thank David for his help” permits composing wording and an email subject. An isolated “reply to David” may lack a purpose, but the surrounding conversation can supply one. Distinguish missing instructions from unavailable facts being requested: checking a profile and accurately reporting that no role is recorded remains active.

A request to update a named channel's topic for anime-expo planning remains active without prior anime discussion. Updating the topic does not assert a fictional history.

One absent message or unresolved recipient does not deactivate independent channel updates.

Finding Sophie's profile without reporting her requested role, reading records without supplying the aggregate, or drafting a message when only sending was requested does not produce the deliverable. A normal end after preparation does not by itself establish abnormal interruption or explicit deferral.

A correctly identified person with a false reported role is not automatically an identity error. A correctly targeted proposal can establish grounding while execution is deferred.

“I could not retrieve the role” reports an execution limitation; “no role is recorded” claims an environmental fact. Check what was actually asserted.

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

## Output and evidence format

Return one JSON object conforming to the supplied `oracle-assessment.schema.json`, version `3.0`. Submit the object directly, without stringifying or wrapping it. The runner validates schema, inventories, links, locators, aggregation, and accounting; these checks do not certify semantic correctness.

Root fields: `schema_version`, supplied `test_id`/`run_id`, `lines`, `obligations`, `unattributed`, `assessment_issue`.

- Include each specification line once, in order. Substantive/condition rows contain `line`, `task_status`, `execution_status`, `grounding`, `evidence`, `explanation`. A pure marker such as Else has only `{"line": 3}`.
- `grounding` maps supplied directly linked obligation numbers to verdicts. Do not inherit links from workflow, although workflow still governs applicability. Use `{}` for no links or inactive unused references. Resolve pronouns from context.
- `obligations` maps every card number once to its overall verdict, e.g. `{"1": "demonstrated_correct"}`; use `{}` for zero cards. Keys are strings. The card's `Grounding obligations` field repeats the task count; do not sum it.
- `unattributed` contains `evidence`/`explanation` objects; use `[]` when nothing remains. Group boilerplate. Explain discrepancies once, plus inactivity, partial remainders, and mixed applicability where relevant. Do not duplicate task text, card descriptions, ID lists, or evidence payloads.
- `assessment_issue`: null or `{"description": "..."}` identifying affected judgments and input problems. Use null judgments only when blocked. `not_established`, empty inactive grounding maps, and marker rows are not assessment failures. Input conflicts need not block supported judgments.

Evidence: `{source, location, paragraphs?}`. Use resolvable source-native locations:

- `diff`: `/inserts/0`, `/deletes/1`, `/updates/0`, or `/updates/0/after/topic_text` (before value implicit). Whole records include incidental fields. Field-level references collectively cover every changed field. Empty `/updates` can support negative evidence; avoid indiscriminate whole nonempty collections.
- `response`: `/final`, with one-based paragraph numbers. Split stripped text on `\n\s*\n`, retaining nonempty blocks; lists/code within blocks remain together. Omit `paragraphs` only for the entire relevant string. Cover every designated user-visible string; exclude internal/tool content and duplicate copies in trajectory.
- Other sources: `prompt`, `card`, `task_spec`, `initial_state`, `final_state`, `trajectory`, `domain_semantics`. Card positions/specification lines are valid locators. Cite supplied API docs or state general domain facts; these cannot invent entity facts.

Evidence array indices are zero-based; card/line/paragraph numbers are one-based. Shared references count once toward complete coverage.

## Assessment order

Complete the applicability assessment for every specification line first, using the ordered applicability procedure. Then assess execution for every line. Then assess grounding for every linked use and aggregate the obligations. Finally account for the net changes and response passages and produce the required JSON. Keep these assessments separate; use the existing rules for each stage.

For each substantive line, write three short labeled clauses in its existing `explanation` string: `Applicability:` identify the decisive rule and its basis; `Execution:` identify the observed deliverable or disposition; `Grounding:` identify the reference-handling finding. Use the usual evidence array for citations. Keep each clause concise and do not add output fields.
