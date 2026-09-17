# Slack G1–G4 campaign

Updated 2026-09-17T06:30:58.712027+00:00.

This development run has ended; the requested evaluation is not complete. G2 mutation remains a six-source pilot, and G3 authoring and quality checks are under review before further generation. Preserve all attempts, costs and original denominators. Unresolved and unrealized attempts remain outcomes, not successful tests. See the [current work status](../../../grounding/slack_campaign/README.md).

The domain model, baseline cards, baseline ground truth and manual audits are human/Codex work. Writer, compiler, reviewer, solver and evaluator calls use Sonnet 5 on Bedrock. Baseline run labels enter only G4. The earlier `pilot_01` is preserved separately and excluded from these yields. See [methods](methods.md) and [all cases](campaign_results.md).

## G1: baseline design

| Measure | Result |
|---|---:|
| Tasks / tasks with obligations | 59 / 58 |
| Grounding obligations | 198 |
| Native assertions: full / partial / unchecked | 74 / 37 / 87 |
| Complete routes | 12 / 174 |
| Identifying attributes | 13 / 26 |
| Entity–resolution modes | 12 / 28 |
| Representative capability-limit probes | 0 / 25 |

The requested modes are 129 single, 34 jointly intended collections, 11 absent and 20 underspecified. Four optional delegated subsets remain separate. Counts concern the benchmark design, not whether a solver followed a particular trajectory. [Counts](g1.json); [baseline mapping](../../../grounding/slack_coverage/baseline_mapping_review.md); [catalog](../../../grounding/slack_coverage/catalog.md).

## G2: native false passes and mutation

Fresh structured assessments followed by manual source-evidence confirmation found **9 grounding violations in 7 of the 47 native-accepted baseline runs**. This is a confirmed-discovery count, not exhaustive recall. No ground-truth run labels were supplied to that discovery process.

| Native-accepted task | Confirmed obligations |
|---|---|
| slack_67 | O1 |
| slack_74 | O1 |
| slack_95 | O1 |
| slack_97 | O4 |
| slack_101 | O2, O5, O8 |
| slack_107 | O5 |
| slack_110 | O7 |

[Manual confirmations and evidence](g2_native_manual_review.json). Six source assignments were fixed for environment-only mutation, preserving their prompts and intended references. Failed/no-op intermediate patches remain in the attempt history.

| Mutation | Manual final validity / quality | Execution | Original focal judgment → mutant |
|---|---|---|---|
| [M-slack_66](construction/M-slack_66/case.json) | accepted / weak | completed | demonstrated_correct → demonstrated_correct |
| [M-slack_86](construction/M-slack_86/case.json) | accepted / adequate | completed | demonstrated_correct → demonstrated_correct |
| [M-slack_89](construction/M-slack_89/case.json) | semantic_boundary_review_required / weak | access_unresolved | demonstrated_correct → not assessed |
| [M-slack_90](construction/M-slack_90/case.json) | accepted / weak | completed | demonstrated_correct → demonstrated_correct |
| [M-slack_93](construction/M-slack_93/case.json) | accepted / strong | completed | demonstrated_correct → demonstrated_correct |
| [M-slack_105](construction/M-slack_105/case.json) | semantic_boundary_review_required / adequate | completed | demonstrated_correct → demonstrated_correct |

Among the **4 accepted completed mutations**, there are **0 observed correct-to-incorrect focal transitions**. These are focal-obligation comparisons; a source run can contain independent failures. This pilot does not establish that mutation increases failure probability. Several negatives are valid but weak (they differ in more than one condition); the owner-as-nonadmin and root-message-versus-thread-reply boundaries are withheld from definitive mutation claims. [Manual review](manual_review.json).

## G3: generation

The fixed route plan has 174 assignments, including six labeled development/calibration cases. Repairs use native conversation continuations. Prompt and harness changes during development are preserved per invocation; this is not a held-out evaluation of one frozen authoring prompt.

| Stage / result | Cases |
|---|---:|
| Planned complete routes | 174 |
| Construction: error | 5 |
| Construction: review_pass | 125 |
| Construction: unrealized | 44 |
| Execution: access_unresolved | 37 |
| Execution: completed | 90 |
| Execution: evaluation_unresolved | 1 |
| Execution: not_run | 46 |
| Model-accepted current cases manually audited | 125 / 125 |
| Audited cases accepted as valid tasks, including shorter routes | 115 / 125 |
| Accepted valid-task yield over all planned assignments | 115 / 174 |
| Current valid generated cases with confirmed grounding failures | 15 |
| Distinct generated case IDs with confirmed failures across preserved valid versions | 16 |

Stage counts are not a strictly nested funnel: a case can retain an earlier execution after a later construction revision fails. Coverage and current primary discoveries require a version-matched accepted case. 7 recorded current solver episodes ended at the turn limit; an evaluator reporting completed means its assessment completed, not that the solver succeeded. One revised case (G-R094) received earlier solver-answer detail in manual construction feedback. It is outcome-informed and excluded from the primary current failure/coverage counts; the original shorter-route case remains separate. [Provenance exception](provenance_exceptions.json). A valid shorter-route task does not earn its assigned longer route. API eligibility is separate from what the prompt asks. The following counts are conservative, version-matched manual coverage lower bounds; no automatic prefix/subpath credit is used.

| Requirement family | Baseline | Generated requested designs | Generated API-qualified solver executions | Baseline ∪ executed generation |
|---|---:|---:|---:|---:|
| Complete routes | 12/174 | 100/174 | 75/174 | 78/174 |
| Identifying attributes | 13/26 | 15/26 | 15/26 | 18/26 |
| Entity–resolution modes | 12/28 | 28/28 | 26/28 | 26/28 |
| Capability limits | 0/25 | 0/25 | 0/25 | 0/25 |

[Cell-level evidence](coverage_results.json). A solver execution with unresolved evaluator serialization is still an execution, but is not counted as a complete automated assessment. No dedicated capability-probe generation was completed; incidental unavailable asks and manual API investigations receive no automatic capability credit.

The compiled-query diagnostic finds at least one declared negative admitted by relaxing exactly one filter in **104/131 model-accepted cases** (generation and mutation combined). This is evidence of a concrete near-miss distinction, not a semantic-validity or difficulty certificate. Missing-edge negatives can escape this diagnostic. [Negative audit](negative_audit.json).

| Confirmed current generated failure | Requested mode | Evidence |
|---|---|---|
| [G-R013](construction/G-R013/case.json) | absent | [Response](execution/G-R013/assessment/sources/response.json), [assessment](execution/G-R013/assessment/assessment.json) |
| [G-R042](construction/G-R042/case.json) | underspecified | [Response](execution/G-R042/assessment/sources/response.json), [assessment](execution/G-R042/assessment/assessment.json) |
| [G-R090](construction/G-R090/case.json) | underspecified | [Response](execution/G-R090/assessment/sources/response.json), [assessment](execution/G-R090/assessment/assessment.json) |
| [G-R098](construction/G-R098/case.json) | multiple | [Response](execution/G-R098/assessment/sources/response.json), [assessment](execution/G-R098/assessment/assessment.json) |
| [G-R099](construction/G-R099/case.json) | underspecified | [Response](execution/G-R099/assessment/sources/response.json), [assessment](execution/G-R099/assessment/assessment.json) |
| [G-R108](construction/G-R108/case.json) | multiple | [Response](execution/G-R108/assessment/sources/response.json), [assessment](execution/G-R108/assessment/assessment.json) |
| [G-R109](construction/G-R109/case.json) | underspecified | [Response](execution/G-R109/assessment/sources/response.json), [assessment](execution/G-R109/assessment/assessment.json) |
| [G-R133](construction/G-R133/case.json) | underspecified | [Response](execution/G-R133/assessment/sources/response.json), [assessment](execution/G-R133/assessment/assessment.json) |
| [G-R137](construction/G-R137/case.json) | underspecified | [Response](execution/G-R137/assessment/sources/response.json), [assessment](execution/G-R137/assessment/assessment.json) |
| [G-R138](construction/G-R138/case.json) | absent | [Response](execution/G-R138/assessment/sources/response.json), [assessment](execution/G-R138/assessment/assessment.json) |
| [G-R145](construction/G-R145/case.json) | underspecified | [Response](execution/G-R145/assessment/sources/response.json), [assessment](execution/G-R145/assessment/assessment.json) |
| [G-R148](construction/G-R148/case.json) | multiple | [Response](execution/G-R148/assessment/sources/response.json), [assessment](execution/G-R148/assessment/assessment.json) |
| [G-R184](construction/G-R184/case.json) | underspecified | [Response](execution/G-R184/assessment/sources/response.json), [assessment](execution/G-R184/assessment/assessment.json) |
| [G-R199](construction/G-R199/case.json) | underspecified | [Response](execution/G-R199/assessment/sources/response.json), [assessment](execution/G-R199/assessment/assessment.json) |
| [G-R207](construction/G-R207/case.json) | underspecified | [Response](execution/G-R207/assessment/sources/response.json), [assessment](execution/G-R207/assessment/assessment.json) |

Common confirmed failures include false empty-set reports for existing reactions, silently dropping a condition, and choosing between equally matching people using unrequested email/domain preferences. Manual review also rejects evaluator flags: G-R212 explicitly acknowledges the missing channel-membership condition and distinguishes supplemental information, so its flag is not a confirmed failure. G-R059 remains withheld over the wording boundary between a Slack reaction and a textual emoji reply. The earlier G-R062 flag rested on an unjustifiably narrow generated card.

The full [manual audit](manual_review.json) and [preserved findings](campaign_results.json) distinguish current cases, old versions, invalid boundaries and qualified shorter-route discoveries. These flag-focused confirmations do not measure generation-evaluator recall. Read-only status and partial-performance disagreements are not silently promoted into grounding failures.

## G4: evaluator reliability

Ground-truth labels enter only this comparison. All 59 cases have one fresh
assessment and one direct-judge result. Both use Sonnet 5, medium effort, a
16,000-token output limit and the same underlying request/state/diff/response/
trajectory/API evidence. The structured method additionally receives manually
curated cards, task specifications and links. The direct judge receives no cards
or obligation inventory and reports localized failures. This compares the full
approaches, not a component ablation or automatic card extraction.

| Obligation-level structured assessment | Result |
|---|---:|
| Exact three-class accuracy | 187 / 198 (94.4%) |
| Violation-detection accuracy | 191 / 198 (96.5%) |
| True positives / false positives / false negatives | 18 / 7 / 0 |
| Violation precision / recall | 72.0% / 100.0% |
| Violation F1 | 83.7% |
| Mechanically valid final reports | 59 / 59 |

| Failing-run detection | Structured evaluator | Direct judge |
|---|---:|---:|
| True positives / false positives / false negatives | 13 / 3 / 0 | 4 / 2 / 9 |
| Precision | 81.3% | 66.7% |
| Recall | 100.0% | 30.8% |

The direct judge produced nine localized failure reports. Manual matching found
five true-positive reports and four false positives: **55.6% report precision**,
and detection of **5/18 reference violations (27.8% recall)**. A report about the
wrong person in Slack 98 does not automatically receive credit for the separate
wrong-channel obligation. See [matching decisions](g4_direct_matching.json),
[aggregate metrics](g4.json), and [all structured judgments](g4_judgments.json).

The 18 reference violations occur in 13 distinct runs. These are descriptive
results on this Slack suite: some examples/policies were developed using these
cases, and the manually curated cards impose interpretations the direct judge
must infer. This is not a held-out generalization claim. Mechanical repairs are
selected by the fixed validation rule, never by agreement with the reference.
Two direct-judge transport failures were preserved and retried without semantic
feedback; their unknown usage is not assumed free.

## Cost, limitations and reproduction

Recorded invocations: **3,106**. Native usage totals: **111,140,830 input**, **6,502,554 output**, **1,324,755 cache-write**, and **22,154,152 cache-read tokens**. The historical-rate estimate is **$442.57**, not a Bedrock invoice or provider-reported dollar charge. **11** recorded invocations lack returned usage; they are listed rather than treated as free. [Usage totals and rates](usage_summary.json); [every recorded call](usage_ledger.json).

Input/context repetition is substantial: authoring/review conversations repeatedly carry base seed, source API information and cumulative compilation context. Solver caching is recorded; the authoring adapter did not use prompt caching in this campaign. These costs include unsuccessful, repair and transport attempts with returned usage; they exclude the already-existing baseline solver run costs and manual/Codex labor.

The main limitations are incomplete route realization, secondary-workspace discovery limits, semantic annotation errors, and uneven negative-example strength. Some long absent queries can be settled at an early empty join and therefore provide a weaker depth challenge. The shared seed leads to repeated names/topics. Role-report tasks can expose only the distinctions supported by API flags; identity-grounding findings do not certify every reported role attribute. [Runtime qualifications](runtime_qualifications.md).

[Final mechanical/provenance checks](final_validation.json) verify the recorded accepted artifacts, version-matched manual audits and evidence links; they do not certify generation quality or completion of the requested goals. G2 mutation remains incomplete, and G3 requires renewed authoring calibration. The recorded measurements do not establish complete coverage, a mutation-induced failure increase, or held-out oracle generalization. Source cards and oracle policies were developed with some of these baseline cases.

To rebuild this report without model calls, run `python -m grounding.slack_campaign.build_report --final` with the configured project Python environment. [Methods](methods.md) explain the authoring, validation, runtime and provenance boundaries. All native requests/responses and available summarized thinking blocks remain beside their stage artifacts.
