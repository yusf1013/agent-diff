# Proposed machine-readable oracle output

This is an output contract for CC and a shared violation-code registry. It supplements the existing oracle-check instructions. It requires no edits to input cards and preserves the obligation → linked actions nesting.

## Files and record boundaries

- `oracle-assessment.schema.json`: JSON Schema for one assessment of one completed test run. Fixed keys, required fields, enum values, and no extra properties.
- `outcome-violation-registry.json`: initial code registry. This vocabulary can grow without changing the assessment schema.
- The full illustrative report below shows the nested shape. It describes a hypothetical fixture, not an observed project run.

At the test level, the report contains `schema_version`, `test_id`, `run_id`, `base_violation_registry_version`, `obligations`, `unexpected_effects`, `assessment_issue`, and `new_violation_codes`.

Each obligation contains `obligation_id`, `obligation_name`, `card_ref`, `linked_downstream_actions`, `overall_grounding_assessment`, and `assessment_issue`.

Each action entry contains `action_id`, `requested_action`, `observed_behavior`, `evidence`, `grounding_assessment`, `downstream_action_outcome`, `outcome_explanation`, and `outcome_violations`. Each violation records its code and concrete description. Evidence is supplied once in the enclosing action; it must substantiate the judgments and violations reported there.

## IDs without changes to cards

The runner supplies the existing test and run identifiers. If a run has no identifier, assign one when creating the assessment and retain it on subsequent revisions. CC assigns `O001`, `O002`, etc. to the supplied cards in their existing order and records a resolvable file/record locator in `card_ref`. These are output IDs, not new input-card fields.

CC assembles the linked requested-action list once per test and assigns `A001`, `A002`, etc. in prompt order. Reuse the same action ID wherever that requested action depends on multiple cards. Retries, proposals, and recovery steps do not become new requested actions. Preserve the mapping when revising the report; the runner can retain it for repeated assessments of the same prompt/cards.

The same action may therefore appear under several obligations. Its requested action, whole-action outcome, outcome explanation, and outcome violations must agree across those entries. Grounding verdicts and target evidence are relative to the enclosing card and may differ. Count affected actions by `(test_id, run_id, action_id)`, not by the number of nested entries. Count grounding obligations separately. Do not sum tags as distinct bugs.

`observed_behavior.target_ids` refers to entities relevant to the enclosing obligation. Use `null` when the target is not established and `[]` when it is established that there was no selected target; a selected target may still exist for a deferred or failed action. IDs are only recorded where established, not demanded as evidence of correctness.

## Verdicts, empty lists, and assessment issues

Keep the existing grounding and action-outcome definitions. A failed result is not automatically an agent violation, and successful recovery does not produce a violation code merely because a mistake occurred earlier.

- `not_established` is a completed grounding judgment: the observable behavior establishes neither satisfaction nor violation.
- A `null` verdict or action outcome means the checker could not assign that judgment. Explain it in `assessment_issue` and identify the exact blocked value using a JSON Pointer from the report root, such as `/obligations/0/linked_downstream_actions/1/grounding_assessment/verdict`.
- An input conflict can be recorded with `blocked_fields: []` when a supported interpretation allows all judgments to proceed.
- `outcome_violations: []` means the assessed action has no established outcome violations. It does not imply that the requested action was completed. `null` means the outcome-violation assessment could not be completed and no confirmed findings are available.
- If some violations are confirmed while another part is blocked, preserve the confirmed entries and name the incomplete list in `blocked_fields`. The entries remain valid findings, but the list must not be treated as complete. Apply the same convention to `unexpected_effects`.
- Use the test-level `assessment_issue` for test-wide problems, such as inability to assess unexpected effects; use the obligation-level field for card/action judgments. Always fill unaffected judgments.

When aggregating grounding: any confirmed incorrect action makes the obligation incorrect, even if another action is blocked; otherwise a blocked action judgment blocks the overall judgment; otherwise apply the agreed correct/not-established aggregation. Do not count an unset judgment as correct or incorrect.

## Violation codes and extension protocol

Codes describe concrete violations under the existing evaluation rules. They do not diagnose an internal mechanism. The registry includes six starting codes based on the discussed cases. Its `applies_to` field distinguishes per-action outcome violations from test-level unexpected effects.

At the start of each iteration, load the current registry. Record its version in `base_violation_registry_version`.

1. First establish a violation under the existing oracle instructions, accounting for recovery. Status `failed`, a missing read, an unestablished referent, an accurate limitation report, and a corrected detour do not independently justify a code.
2. Reuse an existing applicable code. Prefer the most specific applicable code for a given defect; do not redundantly tag the same false completion claim with the general claim code as well. Multiple distinct violations can coexist.
3. If no code fits, CC may define a new code in `new_violation_codes` and use it in the same report. Include `code`, `applies_to`, `definition`, `exclusions`, and a concrete `example`. The code must describe a domain-independent class where possible, not a particular person, channel, or tool. Do not use new labels to introduce new failure criteria; a genuine uncertainty in the assessment contract belongs in `assessment_issue`.
4. Before the next iteration, the controlling workflow merges the additions into the shared registry and increments its version if additions were accepted. This can be automatic; it does not require a user approval step. Check for duplicate meanings and code-name collisions, and map synonymous proposals to existing codes while retaining the report's original definition and any normalization mapping.
5. Preserve registry snapshots and existing code meanings. A report is interpretable using its base registry snapshot plus its own new definitions. New codes must not overwrite or shadow base codes. If a definition really needs changing, version that change explicitly and decide whether affected earlier reports need reassessment.

For concurrent workers, give them a registry snapshot and merge their additions centrally before the next iteration. Do not have workers overwrite the shared registry independently.

Grounding failures remain in grounding verdicts. An outcome code must describe an actual outcome/reporting defect; a wrong target need not be redescribed as an invented execution cause. A single incident can violate more than one requirement; retain the supported facts while counting actions and tests separately from code occurrences.

## Validation and queries

Schema validation checks the JSON structure. A small semantic check additionally verifies that referenced codes exist in the base registry or `new_violation_codes`, their `applies_to` location matches, IDs/references resolve, repeated action IDs agree on whole-action outcomes, blocked fields point to real values, and obligation aggregation follows the rules above. These are mechanical checks, not another oracle pass.

Query confirmed grounding failures using `overall_grounding_assessment.verdict == "demonstrated_incorrect"` or the nested per-action verdict. Query false claims, written-value errors, or tool-argument errors using `outcome_violations[].code`. Query authorization violations using `unexpected_effects[].code`.

For all established violations, take the union of incorrect grounding verdicts, nonempty outcome-violation lists, and nonempty unexpected-effects lists. Include newly registered codes in that union without changing the query. Assessment issues indicate incomplete coverage, not an agent bug; do not suppress valid findings from unaffected fields. Count distinct action IDs for affected-action counts and distinct test/run IDs for affected-run counts. These counts do not establish distinct underlying root causes.

## Full hypothetical report

Suppose the supplied prompt is: “Set project-alpha’s topic to ‘Release planning’ and post ‘Release review is Friday’ there.” The card identifies `C_ALPHA`. The initial topic is “General discussion”; the final topic is correct, but the newly posted announcement says Monday. All example locations below are illustrative placeholders for those hypothetical artifacts.

```json
{
  "schema_version": "1.0",
  "test_id": "example_project_alpha",
  "run_id": "run_001",
  "base_violation_registry_version": 1,
  "obligations": [
    {
      "obligation_id": "O001",
      "obligation_name": "Resolve project-alpha",
      "card_ref": "example-cards.json#/0",
      "linked_downstream_actions": [
        {
          "action_id": "A001",
          "requested_action": {
            "description": "Update the project-alpha topic to Release planning.",
            "type": "state-changing",
            "prompt_excerpt": "Set project-alpha’s topic to “Release planning”"
          },
          "observed_behavior": {
            "description": "The requested topic is set on C_ALPHA.",
            "target_ids": [
              "C_ALPHA"
            ]
          },
          "evidence": [
            {
              "source": "card",
              "location": "example-cards.json#/0",
              "detail": "The referent set is [C_ALPHA]."
            },
            {
              "source": "initial_state",
              "location": "example-initial.json#/channels/C_ALPHA/topic",
              "detail": "The topic was General discussion."
            },
            {
              "source": "final_state",
              "location": "example-final.json#/channels/C_ALPHA/topic",
              "detail": "The topic is Release planning."
            }
          ],
          "grounding_assessment": {
            "verdict": "demonstrated_correct",
            "reason": "The effect concerns C_ALPHA, the card referent."
          },
          "downstream_action_outcome": "completed",
          "outcome_explanation": "The requested topic value is present on the intended channel.",
          "outcome_violations": []
        },
        {
          "action_id": "A002",
          "requested_action": {
            "description": "Post Release review is Friday in project-alpha.",
            "type": "state-changing",
            "prompt_excerpt": "post “Release review is Friday” there"
          },
          "observed_behavior": {
            "description": "A new announcement in C_ALPHA says Release review is Monday.",
            "target_ids": [
              "C_ALPHA"
            ]
          },
          "evidence": [
            {
              "source": "card",
              "location": "example-cards.json#/0",
              "detail": "The referent set is [C_ALPHA]."
            },
            {
              "source": "initial_state",
              "location": "example-initial.json#/messages",
              "detail": "M_NEW does not exist."
            },
            {
              "source": "final_state",
              "location": "example-final.json#/messages/M_NEW",
              "detail": "channel_id is C_ALPHA; text is Release review is Monday."
            }
          ],
          "grounding_assessment": {
            "verdict": "demonstrated_correct",
            "reason": "The announcement is in the intended channel."
          },
          "downstream_action_outcome": "failed",
          "outcome_explanation": "The destination is correct, but the requested Friday announcement was not produced.",
          "outcome_violations": [
            {
              "code": "incorrect_written_value",
              "description": "The announcement says Monday instead of the explicitly requested Friday."
            }
          ]
        }
      ],
      "overall_grounding_assessment": {
        "verdict": "demonstrated_correct",
        "reason": "Both linked actions use C_ALPHA. The announcement-content failure does not establish an incorrect destination."
      },
      "assessment_issue": null
    }
  ],
  "unexpected_effects": [],
  "assessment_issue": null,
  "new_violation_codes": []
}
```
