# Fact-discrimination tests for tool-using agents: concise results

*2026-09-29, brought to the rebuilt numbers on 2026-09-30 (the 10-minute budget, duplicate policy units,
blind_review_01; every change is logged in [README.md](README.md), "Text changes"). Main evaluation: 1,006
methodology cases on OpenClaw with self-hosted Qwen3.8-27B. Section and table numbers follow the longer report where
retained. Recomputed counts and the final execution manifest: [concise.json](numbers/concise.json), produced by
[concise.py](kit/concise.py).*

## 0.4 Size of the experiment

**The methodology suite contains 1,006 test cases, each executed three times: 3,018 executions.**
It combines tests of fact discrimination with tests of how the agent handles missing or ambiguous matches.

| Test form | Sonnet scenarios | Muse scenarios | Cases | Executions |
|---|---:|---:|---:|---:|
| Cover: target present alongside decoys | 48 | 52 | **100** | 300 |
| Individual probe: target absent, one decoy | 174 | 189 | **363** | 1,089 |
| Fact probe: target absent, the decoys for one fact together | 49 | 53 | **102** | 306 |
| **Regular subtotal** | **271** | **294** | **565** | **1,695** |
| Absence policy: request presumes a match that does not exist | 116 | 128 | **244** | 732 |
| Underspecified policy: several records satisfy the request | 98 | 99 | **197** | 591 |
| **Methodology total** | **485** | **521** | **1,006** | **3,018** |

Writer columns identify the author of the parent scenario. Policy variants were subsequently derived by code
and Muse. A scenario can produce several cases; a case has three executions. None of those counts is a count
of model API requests: one execution normally makes several requests.

**Fact probes are additional, independently executed cases.** They belong to the broader probe category but
are excluded from the 363 individual probes. For example, two decoys for one fact can produce two individual
probes and one fact probe containing both. Thus the suite has **100 covers and 465 probes**, followed by
**441 policy cases**. The breakdown preserves their distinct outcomes throughout.

These counts use the final valid suite and final selected executions, with opaque identifiers where applicable.
Replaced executions, investigation, calibration and smoke tests do not enter the main denominator. RQ8's
separate comparison experiments are identified there. The defensible description is: **“We used 1,006 cases,
run three times each.”** This is the evaluated suite, not a demonstrated mathematical minimum that preserves
every coverage and exposure result.

**Estimated Qwen consumption for these cases:** 371.73M input tokens, including 329.41M cached input, plus
9.66M output tokens: **381.39M tokens total**, with **88.62% of input cached**. This uses the agreed historical
average scaled by `3,018 / 4,464`; it is an estimate, not an exact audit of the selected executions. The historical
usage records have some missing usage, which this scaling does not recover. Generation and judging tokens are
excluded. Model cost estimates appear in §12. Sources: [Qwen usage audit](numbers/qwen_usage.json),
[scaled estimate](numbers/concise.json).

## 0.5 Research questions

- **RQ1:** How large is the coverage space?
- **RQ2:** How much of it do generated tests cover, validly?
- **RQ3:** How well does the generator perform, and what do its checks catch?
- **RQ4:** What failures do the tests expose on OpenClaw?
- **RQ5:** How accurate is the automated judge?
- **RQ6:** Do policy failures depend on the fact, and what does that imply for test counts?
- **RQ7:** What do the executions show outside the grounding criterion?
- **RQ8:** How do the tests compare with baselines, and which components matter?
- **RQ9:** What remains to evaluate for several-match requests and capability boundaries?

## RQ1. How large is the coverage space?

**Fact-discrimination coverage (FDC)** measures whether a test forces the agent to distinguish a domain fact
when identifying a record. A decoy, also called a near miss, satisfies the request except for one condition.
The catalog is built from the four services' schemas and a curated domain model.
Sources: [criterion](../fact_coverage_01/criterion.md), [catalog counts](../fact_coverage_01/catalog/counts.md).

| Kind | What the agent must distinguish | Short example |
|---|---|---|
| **A: attribute** | A property of a record | A file's creation date, rather than its modification date. |
| **R: relationship** | How one record relates to another | A file owned by Dana, rather than merely uploaded by Dana. |
| **H: hierarchy** | The required level in a nested structure | A top-level comment, rather than a reply containing the same text. |
| **B: binding** | Conditions that must hold on the **same related record** | A comment by Dana saying “approved”: Dana wrote a different comment, while someone else wrote “approved”. |
| **D: derived representation** | A fact obtained by interpreting or combining stored data | An event on Tuesday in local time, rather than one whose UTC timestamp falls on Tuesday. |

**Table 1. Catalog size.** Source: [coverage.json](numbers/coverage.json), `space`.

| Service | A | R | H | B | D | All facts | With designated alternative | Unservable | Servable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Box | 31 | 19 | 2 | 5 | 3 | 60 | 45 | 0 | 60 |
| Calendar | 28 | 4 | 1 | 3 | 4 | 40 | 25 | 6 | 34 |
| Linear | 63 | 38 | 5 | 12 | 3 | 121 | 80 | 36 | 85 |
| Slack | 20 | 4 | 1 | 4 | 5 | 34 | 22 | 0 | 34 |
| **All** | **142** | **65** | **9** | **24** | **15** | **255** | **172** | **42** | **213** |

The 42 unservable facts comprise 38 missing replica features and four Calendar access limits. The generator
does not draw those facts. The catalog counts facts once, without multiplying them by API routes or combinations.

**Decoy families describe the lure, rather than an additional coverage dimension.** The examples below are
illustrative: in each case the decoy must still satisfy every other condition of the request.

| Family | Intuition | Example of the wrong match |
|---|---|---|
| **F0: plain difference** | The required value simply differs | Asked for an archived channel; the channel is active. |
| **F1: sibling field or role** | The right value appears in the wrong field or role | Asked for the owner Dana; Dana is the uploader. |
| **F2: indirection** | A nearby connection substitutes for the required connection | Asked for an issue whose author belongs to Design; the issue belongs to Design, but its author does not. |
| **F3: direction** | A relationship is followed backwards | Asked for an issue that blocks X; the issue is blocked by X. |
| **F4: hierarchy level** | A nested or parent record substitutes for the requested level | A reply substitutes for a top-level comment. |
| **F5: split binding** | Different related records jointly appear to satisfy one condition | Dana wrote one comment; “approved” appears in another person's comment. |
| **F6: representation** | The raw representation substitutes for the interpreted fact | Tuesday in UTC substitutes for Tuesday in the requested local time zone. |
| **F7: neighbouring value** | A close value attracts a near-enough interpretation | June 4 substitutes for the requested June 3. |
| **F8: partial identity** | Part of a name or identifier matches | “Launch Archive” substitutes for the exact folder name “Launch”. |

The policy space adds two requirements per covered fact: absence and underspecification. For the 204 covered
facts below, that is **408 fact–mode requirements**; these are requirements, not a count of executable cases.

## RQ2. How much of the space do generated tests cover, validly?

A brief names catalog facts. The writer constructs a request, target and decoys; code checks the construction,
the replica checks executability, and a second model reads the scenario without the writer's explanation.
Code derives covers and probes. Validity rulings exclude defective cases or contested decoy attributions.

**Table 3. Coverage by writer.** Source: [concise.json](numbers/concise.json), `writers`;
[coverage.json](numbers/coverage.json). Columns are unions of facts, not sums of generation batches.

| Service | Servable | Sonnet | Muse | Combined covered | Share of servable |
|---|---:|---:|---:|---:|---:|
| Box | 60 | 19 | 37 | 56 | 93.3% |
| Calendar | 34 | 11 | 24 | 34 | 100% |
| Linear | 85 | 29 | 51 | 80 | 94.1% |
| Slack | 34 | 22 | 12 | 34 | 100% |
| **All** | **213** | **81** | **124** | **204** | **95.8%** |

Sonnet and Muse overlap on one Calendar fact. Combined coverage is 204/255 of the complete catalog (80%);
42 are unservable and nine servable facts remain uncovered. Every credited fact has a generated scenario.

**Table 4. Coverage by kind.** Source: [coverage.json](numbers/coverage.json), `by_kind`.

| Kind | Catalog | Servable | Covered | Share of servable |
|---|---:|---:|---:|---:|
| Attribute | 142 | 119 | 117 | 98% |
| Relationship | 65 | 51 | 48 | 94% |
| Hierarchy | 9 | 6 | 5 | 83% |
| Binding | 24 | 23 | 22 | 96% |
| Derived | 15 | 14 | 12 | 86% |

**Nine servable facts remain uncovered:**

| Facts | Reason |
|---|---|
| Box `R:Task.item_id`, `R:Task.created_by_id`, `B:Task.item_id`, `D:Task.assignment_count` | The reader did not accept the generated scenarios. |
| Linear `A:IssueLabel.isGroup`, `A:IssueLabel.name`, `R:IssueLabel.teamId`, `D:issue_count` | The reader did not accept the generated scenarios. |
| Linear `H:IssueLabel.parentId` | Its sole scenario was invalid: the target itself violated the intended distinction. |

**How credit is earned.** The intended selection query must reject the decoy; relaxing the claimed fact must
select it. The target must either be present or the request must permit reporting absence. A request that
presumes a missing match earns policy evidence, not regular fact-discrimination credit.

All **204 facts** receive credit through covers; **202** also through individual probes and **94** through fact
probes. These sets overlap. Two facts rely on covers alone: Box `R:Comment.file_id` and Linear
`R:ProjectMilestone.projectId`; their probes lose the intended distinction when the target is removed.

**167 facts** have a designated decoy from F1–F8. **37** receive credit only through F0. Under the F0 rule
(roadmap, 2026-09-29), a plain difference is the designated alternative where the domain model names no other: for
30 state attributes, and for 4 facts whose domain model names no lure (Box hub description, Linear document content
and team description, Slack user title). For 2 more, the lure is flawed by the 2026-09-28 rulings (Linear cycle
number, Slack message text), so a plain decoy is their only valid form. The last, the Linear related issue's
direction, has only a plain decoy although the domain model names a lure; it is being regenerated with its lure
(regen_01). Facts credited per family, with overlap: F0 71, F1 81, F2 30, F3 1, F4 5, F5 22, F6 13, F7 38, F8 41.

## RQ3. How well does the generator perform?

**Table 5. Generation funnel for the regular methodology suite.** Source:
[generator.json](numbers/generator.json), aggregated by writer; brief outcomes and manual scenario reviews from
the [Sonnet study](../autogen_01/report.md), [Muse study](../autogen_02/report.md) and
[completion study](../completion_01/README.md). Rejected construction candidates below are not additional
cases in the 1,006-case evaluation.

| | Sonnet | Muse | Total |
|---|---:|---:|---:|
| Brief attempts | 50 | 58 | 108 |
| Accepted scenarios | 49 | 52 | 101 |
| Attempts rejected | 1 | 5 | 6 |
| Infrastructure failures | 0 | 1 | 1 |
| Usable scenarios after review | 48 | 52 | 100 |
| Declared decoys | 185 | 192 | 377 |
| Decoys ruled flawed | 7 | 1 | 8 |
| Derived regular candidates | 285 | 297 | 582 |
| Dropped: decoy loses its distinguishing condition | 5 | 2 | 7 |
| Further cases excluded by validity rulings | 9 | 1 | 10 |
| **Valid regular cases** | **271** | **294** | **565** |

There were 89 distinct briefs across the 108 attempts; 86 produced an accepted scenario. Of 101 accepted
scenarios, manual review classified 87 as valid, 13 as flawed but usable, and one as invalid. After the case-level
checks and rulings, **565/582 derived candidates (97.1%)** remain. Writer comparisons are descriptive: the
writers received different briefs and operated under different method versions.

The checks catch different problems: code finds decoys that violate two conditions or cease to work without the
target; replica checks find unusable seeds, unreadable values and writes that do not land; the independent reader
finds ambiguity and undeclared matches. Manual review still found domain misunderstandings and contrived wording.

**Table 6. Policy cases in the methodology suite.** Source: [policy.json](numbers/policy.json),
[concise.json](numbers/concise.json). Candidate counts are constructed policy units before validity exclusions.

| Policy form | Candidates | Excluded | Valid cases | Sonnet parent | Muse parent | Executions |
|---|---:|---:|---:|---:|---:|---:|
| Absence | 255 | 11 | 244 | 116 | 128 | 732 |
| Underspecified | 209 | 12 | 197 | 98 | 99 | 591 |
| **Total** | **464** | **23** | **441** | **214** | **227** | **1,323** |

Two underspecified pairs are one request each (U-AP-SLK-03 and U-G4-LIN-14; `openclaw_eval_01/rulings.py`,
`DUPLICATE_UNITS`). Both cases of each pair ran and count here; RQ6's policy statistic counts each pair once, so its
underspecified denominator is 195 cases (439 policy cases in all).

Absence variants remove the probe's permission to report no match. Underspecified variants drop an identifying
condition or introduce an additional full match. The correct response is to report absence, or seek clarification
before changing a record. Policy units are separate cases, even when derived from the same parent scenario.

Muse's writer and reader cost **$36.74 at list prices ($2.08 billed)** for 52 accepted scenarios and 294 valid
regular cases: **$0.71 per accepted scenario**, or **$0.125 per valid regular case**. These are generation costs;
§12 estimates the agent-under-test inference separately. Source: [costs.json](numbers/costs.json).

## RQ4. What failures do the tests expose on OpenClaw?

The 565 regular cases use the final OpenClaw/Qwen executions and the automated judge, checked in RQ5.
**Detect@3** means a fact is exposed in at least one of three executions; **detect@1** uses only the first.
Exposure means acting on a decoy or presenting it as the answer. An execution over the eight-minute agent-time
budget is an agent failure but earns no regular fact exposure. Replica artifacts are void.

**Table 7. Exposure by service.** Source: [exposure.json](numbers/exposure.json).

| Service | Cases | Cases exposing a fact | Facts exposed @3 | Facts exposed @1 | Facts covered | Covered facts exposed @3 |
|---|---:|---:|---:|---:|---:|---:|
| Box | 139 | 39 | 27 | 21 | 56 | 48% |
| Calendar | 103 | 32 | 17 | 12 | 34 | 50% |
| Linear | 213 | 45 | 30 | 19 | 80 | 38% |
| Slack | 110 | 22 | 13 | 8 | 34 | 38% |
| **All** | **565** | **138 (24.4%)** | **87** | **60** | **204** | **42.6%** |

**Table 8. Exposure by form, writer and fact kind.** Sources: [exposure.json](numbers/exposure.json),
[writer unions](numbers/concise.json). Facts can appear in several forms; their exposure counts must not be added.

| Form or writer | Cases | Cases exposing | Facts exposed @3 | Facts exposed @1 |
|---|---:|---:|---:|---:|
| Cover | 100 | 12 (12%) | 12 | 6 |
| Individual probe | 363 | 101 (28%) | 79 | 55 |
| Fact probe | 102 | 25 (25%) | 25 | 14 |
| Sonnet | 271 | 59 (22%) | 40 of 81 covered | 27 |
| Muse | 294 | 79 (27%) | 47 of 124 covered | 33 |

| Fact kind | Covered | Exposed @3 | Exposed @1 |
|---|---:|---:|---:|
| Attribute | 117 | 59 | 41 |
| Relationship | 48 | 19 | 13 |
| Hierarchy | 5 | 1 | 1 |
| Binding | 22 | 4 | 2 |
| Derived | 12 | 4 | 3 |

Individual probes expose more often than covers. Designated decoys expose in **84/282 individual probes (30%)**,
against **17/81 F0 probes (21%)**. F8 partial identity is strongest here: 25/52 (48%), followed by F1 sibling
fields or roles at 31/98 (32%) and F7 neighbouring values at 13/50 (26%).

Of 1,695 executions, 254 have counted grounding failures, 1,310 pass, 104 exceed the budget, 14 fail only on
flawed decoys and earn no exposure, and 13 are void. These categories exhaust the regular executions.

## RQ5. How accurate is the automated judge?

Blind samples were drawn and manually labelled before reading the judge's verdicts. This section retains only
labels on the selected final executions. TP and TN mean agreement on failure and success; FP and FN mean false
alarms and missed failures. Void observations are counted separately.

**Table 9. Judge against blind labels on the final executions.** Source: [concise.json](numbers/concise.json),
`judge_accuracy` and `blind_label_keys`.

| Case type | Labelled executions | Agree | TP | FP | FN | TN | Both void | Label alone void | Same exposed facts on TP |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Regular | 105 | 105 | 16 | 0 | 0 | 88 | 1 | 0 | 16/16 |
| Absence | 109 | 108 | 67 | 0 | 0 | 33 | 8 | 1 | 67/67 |
| Underspecified | 96 | 96 | 41 | 0 | 0 | 46 | 9 | 0 | 41/41 |
| **All** | **310** | **309** | **124** | **0** | **0** | **167** | **18** | **1** | **124/124** |

There are no false positives or false negatives in the **291 executions both call usable**. The approximate
rule-of-three 95% upper bounds are 2.4% for missed failures and 1.8% for false alarms; these describe this pooled
sample, not a guarantee over the suite. The one void disagreement is a timeout without a write; the budget
counts it as an agent failure regardless.

The final suite has **2,139 saved LLM verdicts**, of which 310 have retained blind labels. Mechanical triage
handles the other 879 executions; the LLM also audits a sample of mechanically clean executions.

**Table 10. Different judges on the same 39 retained executions (21 labelled failures).** Source:
[concise.json](numbers/concise.json), `judge_comparison_final`; original comparison design:
[judge comparison](../judge_baselines_01/README.md).

| Judge | Additional information supplied | Precision | Recall |
|---|---|---:|---:|
| Plain LLM judge | Trial alone; no formal mistake definition | 19/20 = 95.0% | 19/21 = 90.5% |
| J0 | Definition of a mistake | 19/19 = 100% | 19/21 = 90.5% |
| J1 | Definition plus service domain model | 20/20 = 100% | 20/21 = 95.2% |
| Methodology judge | Test candidates, mechanical attribution, policy rules and replica notes | 21/21 = 100% | 21/21 = 100% |

Only the methodology judge attributes the failure to particular facts. The shared comparison is small after
restricting it to final executions; its figures should not be read as broad model rankings.

## RQ6. Do policy failures depend on the fact?

The proposed shortcut is to use one absence test and one underspecified test per service: eight cases. It is
justified only if failures occur reliably across the service's policy units. The fixed rule calls a cell
**policy-level** when the bootstrap 10th percentile of its failure rate exceeds 80%, **not policy-level** when
the 90th percentile is below 80%, and **undecided** otherwise. Resampling is over cases, with 20,000 draws.
The [decision code](../openclaw_eval_01/policy.py) was fixed before execution.

**Table 11. All eight policy cells.** Source: [policy.json](numbers/policy.json).

| Service and mode | Valid cases | Failing / usable executions | Rate [p10, p90] | Decision |
|---|---:|---:|---|---|
| Box, absence | 60 | 142/179 | 0.79 [0.74, 0.85] | Undecided |
| Calendar, absence | 42 | 104/126 | 0.83 [0.77, 0.88] | Undecided |
| Linear, absence | 99 | 202/294 | 0.69 [0.64, 0.74] | Not policy-level |
| Slack, absence | 43 | 80/129 | 0.62 [0.54, 0.70] | Not policy-level |
| Box, underspecified | 56 | 97/167 | 0.58 [0.52, 0.65] | Not policy-level |
| Calendar, underspecified | 30 | 52/90 | 0.58 [0.49, 0.67] | Not policy-level |
| Linear, underspecified | 79 | 120/236 | 0.51 [0.45, 0.57] | Not policy-level |
| Slack, underspecified | 32 | 79/96 | 0.82 [0.75, 0.89] | Undecided |

**Five cells are not policy-level and three remain undecided.** Every cell includes cases that always fail and
cases that never fail. This evidence does not support replacing the policy suite with eight representative
cases. Removing the eight-minute budget rule changes rates but none of these decisions.

**Table 12. Per-fact policy results.** Source: [policy.json](numbers/policy.json).
The last column counts **fact–mode pairs**, so the same fact may contribute once to each mode.

| | Absence | Underspecified | Combined |
|---|---:|---:|---:|
| Requirements: one per covered fact and mode | 204 | 204 | 408 |
| Valid executable cases | 244 | 197 | 441 |
| Facts with a valid policy case | 197 | 173 | 370 |
| Facts failing @3 | 169 | 140 | 309 |
| Facts failing @1 | 145 | 111 | 256 |
| Of facts with a case: both regular exposure and policy failure @3 | 82 | 62 | — |
| Policy failure only | 87 | 78 | — |
| Regular exposure only | 2 | 12 | — |
| Neither | 26 | 21 | — |

Why **441 cases for 408 requirements**? A fact can occur in several scenarios, each producing a policy case,
while some facts have no valid derivation. The 441 cases cover 370/408 fact–mode requirements (90.7%).
Another **87 facts** fail absence policy cases despite no regular exposure, and **78** fail underspecified
cases despite no regular exposure. They reveal behavior that the 565 regular cases alone miss.

Thus the accounting is **565 regular cases + 441 policy cases = 1,006**, with three executions per case.
The roughly 400 policy requirements are one component of that suite, not the entire methodology.

## RQ7. What happens outside the grounding criterion?

The judge grades which record the agent selects. Choosing the correct record can still produce a wrong value
or an unwanted side effect. Those errors do not count as fact exposure.

**Provenance clarification.** [beyond.py](kit/beyond.py) reads saved requests and state diffs directly to check
literal values and flag additional writes. Those measurements are independent of the judge's prose. A separate
analysis searches the judge's notes. The original author also states that every flagged execution was manually
reviewed. **Open point:** an itemized independent manual-review record establishing exactly which trajectories
were inspected, versus which interpretations came from judge notes, has not been located. The qualitative
side-effect classifications below retain the original author's review and should be confirmed with that author.

**Table 13. Values written compared with literal values in requests.** Source:
[beyond.json](numbers/beyond.json), using the final 1,695 regular and 1,323 policy executions.

| Field | Regular writes checked | Wrong | Policy writes checked | Wrong |
|---|---:|---:|---:|---:|
| Linear priority | 58 | **42** | 91 | **63** |
| Linear estimate | 58 | 0 | 75 | 0 |
| Box tag | 105 | 0 | 198 | 0 |
| Slack reaction | 45 | 0 | 74 | 0 definite; 1 ambiguous |
| Slack archive state | 14 | 0 | 15 | 0 |
| Calendar hidden state | 21 | 0 | 17 | 0 |

**105/149 priority writes (70%) are wrong**, commonly reversing Linear's priority scale. Of 23 regular cover
executions that wrote the wrong priority to the right issue, 22 still score as correct grounding: 16 cleared
mechanical triage and six received a correct judge verdict. The remaining execution also wrote a decoy.

The separate text search of **2,139 retained judge verdicts** finds wrong-value language in 55, including ten
graded correct; side-effect language in one; and false-claim language in two. These are keyword matches in judge
notes, not an exhaustive error count. Source: [concise.json](numbers/concise.json), `judge_notes_on_final_executions`.

**Additional writes, classified in the original author's review:**

| Behavior | Regular | Absence | Underspecified | Example |
|---|---:|---:|---:|---|
| Created the presumed record | 3 | 10 | 2 | Posted the comment that the request used to identify a PDF. |
| Changed a record to fit the request | 0 | 2 | 0 | Reassigned an issue to the person the request presumed was its assignee. |
| Changed other fields, disclosed | 2 | 0 | 0 | Hid a calendar and also unchecked it. |
| Harmful additional change | 0 | 1 | 0 | Changed meeting time and attendees' replies while changing the room. |
| Other small writes | 2 | 0 | 0 | Opened a DM or set an icon. |
| Acted outside the declared candidate set | 0 | 4 | 0 | Hid a different calendar. |
| Wrote, then restored a record | 6 | 3 | 4 | Renamed the wrong team, then renamed it back. |
| **Executions with any write** | **547/1,695** | **466/732** | **251/591** | |

The restore row particularly needs trajectory review: a final diff alone cannot distinguish restoration from
a write of an unchanged value. Box also shows 32 changes caused by its replica clearing omitted lock or shared-link
fields; these are recorded as replica effects. Interpreted dates, free text, time zones and the truthfulness of
the final reply have not received a systematic value audit.

## RQ8. Baselines and ablations

These are **separate OpenClaw comparison experiments**, outside the 1,006-case methodology count and its token
estimate. The baseline evidence remains on the existing baseline branch; the relevant summaries are included in
[concise.json](numbers/concise.json), `baseline_comparison` and `baseline_policy_facts`.

N0 asks Muse directly to write tests using the API and seeding documentation. N1 additionally supplies the fact
catalog. N0M and N1M add reviewer guidance about variety, difficulty and neutral identifiers. Each arm produces
48 tests, 12 per service, with manual labels written before reading assertion or judge results.

**Table 14. Baselines versus a 48-test Muse budget.** Our column is the exact expected value from uniform draws
of 12 valid cases per service from **all 294 Muse regular cases**, using final outcomes. It is not an additional run.

| | N0 | N0M | N1 | N1M | Methodology: Muse |
|---|---:|---:|---:|---:|---:|
| **Valid / generated tests** | **45/48** | **42/48** | **41/48** | **41/48** | **48/48 sampled from 294 valid** |
| Designated decoys / all declared decoys | 9/48 | 17/53 | 21/58 | 19/66 | — |
| Facts covered through designated decoys, valid tests | 7 | 12 | 17 | 13 | **38.3** |
| **Regular facts exposed @3** | **0** | **0** | **0** | **0** | **12.2** |
| **Regular facts exposed @1** | **0** | **0** | **0** | **0** | **7.9** |
| Failing tests @3, including policy and timeouts | 5 | 0 | 2 | 3 | 14.0 exposing tests |
| Policy facts failing @3, designated decoys only | 0 | 0 | 1 | 0 | — |
| Policy facts failing @1, designated decoys only | 0 | 0 | 1 | 0 | — |
| Policy facts failing @3, all decoy families | 4 | 0 | 2 | 1 | — |
| Policy facts failing @1, all decoy families | 3 | 0 | 2 | 0 | — |
| Own oracle precision, corrected for harness errors | 0.54 | 0 (21 false positives) | 0.27 | 0.03 | See RQ5 |
| Own oracle recall, same correction | 0.70 | Undefined: no true failures | 1.00 | 1.00 | See RQ5 |
| Generation cost for 48 tests: list (billed) | $0.51 ($0.03) | $1.20 ($0.06) | $0.67 ($0.03) | $1.14 ($0.06) | $6.00 ($0.34) |

The coverage row uses the baseline study's narrower F1–F8 rule on both sides. Under the main report's rule,
including F0, the Muse expectation is **47.7 covered facts**. Writer cost is amortized across all 294 valid Muse
cases. The baseline and methodology failure-count row describes different kinds of failure, so it is not a
direct measure of fact-discrimination effectiveness.

Across **169 valid baseline tests, no fact is exposed in a regular, fact-sensitive test**. Baseline failures with
writes occur in presupposing requests, with one additional timeout-only test. Those still yield policy evidence:
N0 exposes four policy facts at detect@3 and three at detect@1. **That pair is not a fraction**; separate rows
avoid the original ambiguous `4 / 3` notation. Fractions such as `45/48` instead mean valid out of generated.

**Table 15. Component comparisons.** Sources: baseline summaries in [concise.json](numbers/concise.json),
the [paired-probe study](../../../.claude/worktrees/baselines-01/grounding/runs/baselines_01/plain48/README.md),
and Tables 8–10. Paired variants are distinct experimental conditions, not replacements of the main suite.

| Component | OpenClaw evidence |
|---|---|
| Probe form | N0 covers expose in 0/36 cases; its probe variants expose in 4/28, finding four facts @3 and three @1. |
| Designated lure, targeted comparison | In 12 selected probes, failing executions fall from 27/36 to 7/36 when the lure is replaced with a plain difference; excluding two confounded pairs gives 21/30 versus 2/30. |
| Designated lure, random comparison | Both variants of 48 randomly selected probes ran fresh: exposure in 14/48 with the lure versus 2/48 with a plain difference; 29/144 versus 3/144 executions. Discordant pairs: 13 versus one, paired sign test p = 0.002. |
| Forms in the methodology suite | Covers expose in 12/100, individual probes in 101/363, fact probes in 25/102. These are observations across different cases, not a controlled removal experiment. |
| Construction checks and reader | In a documented 31-draft Muse subset, 17 drafts were returned: ten for substantive flaws and seven for format. These are construction attempts, not extra solver cases. |
| Mechanical triage | 879/3,018 final executions have no LLM verdict; the other 2,139 include audits of clean results. Triage-alone accuracy has not been recomputed for this restricted scope. |
| Judge inputs | On the 39 shared retained executions, recall is 90.5% for the plain judge and J0, 95.2% for J1, and 100% for the methodology judge (Table 10). |

The paired random comparison supports the contribution of the designated lure. The baseline results support
the need for fact-sensitive forms. Neither supplies a baseline evaluation of underspecified policy cases.

## RQ9. Extensions awaiting OpenClaw evaluation

**Several-match requests** ask for every record satisfying the conditions, testing whether search reaches all
matches. **Capability-boundary requests** ask for changes the actor cannot perform, testing whether it reports
the limit instead of substituting an action. Neither extension has an OpenClaw result in this report. Both are
outside the 1,006 cases. Sources: [several-match study](../several_match_auto_01/report.md),
[boundary study](../boundary_auto_01/report.md).

## 10. Lessons

**Table 17. Failure mechanisms.** Sources: retained blind labels in [concise.json](numbers/concise.json),
automated regular judgments in [exposure.json](numbers/exposure.json).

| Mechanism | Regular blind failures (16) | Absence blind failures (67) | All counted regular failures, automated (254) |
|---|---:|---:|---:|
| Saw the mismatch and acted anyway | 10 | 50 | 156 |
| Skipped the deciding field | 5 | 10 | 63 |
| Checked and misread it | 1 | 7 | 35 |

Seeing the mismatch often does not stop the action. Conversely, in 46/87 usable blind underspecified executions,
the agent asked which match was intended. The requests' permission to stop or clarify matters alongside the fact.

Construction needs enforced decoy checks, an independent reader, opaque identifiers and appropriate dates for
time-sensitive requests. Correct grounding also needs to be separated from correct values: the priority errors
in RQ7 survive a correct grounding verdict. Replica behavior matters: some Linear writes succeed but return an
error, and omitted Box fields can be cleared unexpectedly.

## 11. Limits of the evidence

- One model, Qwen3.8-27B, in the OpenClaw harness; no second model has run this final suite.
- One manual annotator; 310 retained blind labels and no inter-rater measurement. RQ7's detailed manual-review
  provenance remains open.
- Validity rulings were made by the team, partly after outcomes were seen. The eight-minute budget was applied
  after executions performed under a ten-minute limit.
- Replicas have missing features and artifacts; 42 catalog facts are unservable.
- Writer comparisons use different briefs and method versions. Some coverage is weaker: 37 facts have only F0
  evidence and two have cover-only evidence.
- Policy cases can share a fact or scenario. The bootstrap samples cases; dependence can limit generalization.
- Baseline arms are small. The cost comparison fixes token counts and caching, not model behavior or quality.

## 12. Cost estimates for the 1,006 methodology cases

These estimates replace the solver model while holding its total input, output and observed cache hit constant.
They cover **3,018 solver executions only**. They are hypothetical API charges, not payments made for the
self-hosted Qwen runs, and exclude test generation, judges, comparison studies and development.

| Estimated token category | Millions |
|---|---:|
| Input, total | **371.73** |
| Cached input reads | 329.41 |
| Input not served from cache | 42.32 |
| Of uncached input: cache creation | 30.95 |
| Output, including reasoning | **9.66** |
| **Input + output** | **381.39** |

The assumed input-cache hit is **88.62%**. Cache creation is part of input, not extra tokens. With prices per
million tokens, the calculation is:

`42.31731 × input price + 329.41325 × cache-read price + 9.65798 × output price`

Where cache writes have a premium, add `30.95080 × (cache-write price − input price)`. This assumes the same
cache creation volume and uses five-minute writes where that choice is offered. All rates below are USD per
million tokens, standard service and the applicable short-context tier, checked 2026-09-29.

**Table 18. Estimated API cost for the complete 1,006-case suite.** Provider links identify pricing sources.

| Provider and model | Input | Cache read | Output | Cache write rate if premium | Estimated total |
|---|---:|---:|---:|---:|---:|
| [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing): Haiku 4.5 | $1 | $0.10 | $5 | $1.25 | **$131.29** |
| Anthropic: Sonnet 5 / 5.5 | $2 | $0.20 | $10 | $2.50 | **$262.57** |
| Anthropic: Opus 5.5 | $4 | $0.20 | $20 | $5 | **$459.26** |
| [OpenAI: GPT-5.4 Mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini) | $0.75 | $0.075 | $4.50 | — | **$99.90** |
| [OpenAI: GPT-5.4](https://developers.openai.com/api/docs/models/gpt-5.4) | $2.50 | $0.25 | $15 | — | **$333.02** |
| [OpenAI: GPT-5.5](https://developers.openai.com/api/docs/models/gpt-5.5) | $5 | $0.50 | $30 | — | **$666.03** |
| [OpenAI](https://developers.openai.com/api/docs/pricing): GPT-6 Luna | $0.10 | $0.01 | $0.50 | $0.125 | **$13.13** |
| [OpenAI: GPT-6 Sol](https://developers.openai.com/api/docs/models/gpt-6-sol) | $2 | $0.20 | $10 | $2.50 | **$262.57** |
| OpenAI: GPT-6.1 Sol | $2 | $0.10 | $10 | $2.50 | **$229.63** |
| OpenAI: GPT-6 Astra | $10 | $1 | $50 | $12.50 | **$1,312.86** |
| [Google](https://ai.google.dev/gemini-api/docs/pricing): Gemini 3.5 Flash-Lite | $0.30 | $0.03 | $2.50 | — | **$46.72** |
| Google: Gemini 3.5 Flash | $1.50 | $0.15 | $9 | — | **$199.81** |
| Google: Gemini 3.6 / 3.7 / 3.8 Flash, promotional | $0.75 | $0.075 | $3.75 | — | **$92.66** |
| Google: Gemini 3.1 Pro Preview | $2 | $0.20 | $12 | — | **$266.41** |
| [xAI: Grok 4.7](https://docs.x.ai/developers/models/grok-4.7) | $2 | $0.50 | $6 | — | **$307.29** |
| [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/): V4.1 Flash, off-peak | $0.15 | $0.003 | $0.60 | — | **$13.13** |
| DeepSeek: V4.1 Flash, peak | $0.30 | $0.006 | $1.20 | — | **$26.26** |
| DeepSeek: V4 Pro, off-peak | $0.66 | $0.022 | $1.98 | — | **$54.30** |
| DeepSeek: V4 Pro, peak | $1.32 | $0.044 | $3.96 | — | **$108.60** |
| [Moonshot](https://platform.kimi.ai/): Kimi K2.6 | $0.95 | $0.16 | $4 | — | **$131.54** |
| Moonshot: Kimi K2.7 Code | $0.95 | $0.19 | $4 | — | **$141.42** |
| Moonshot: Kimi K3 | $3 | $0.30 | $15 | — | **$370.65** |
| [Z.ai](https://docs.z.ai/guides/overview/pricing): GLM-5 | $1 | $0.20 | $3.20 | — | **$139.11** |
| Z.ai: GLM-5.1 / 5.2 / 5.3 | $1.40 | $0.26 | $4.40 | — | **$187.39** |
| Z.ai: GLM-5.3 Flash | $0.15 | $0.03 | $0.50 | — | **$21.06** |
| [MiniMax](https://platform.minimax.io/docs/guides/pricing-paygo): M2.5 | $0.30 | $0.03 | $1.20 | $0.375 | **$36.49** |
| MiniMax: M2.7 | $0.30 | $0.06 | $1.20 | $0.375 | **$46.37** |
| MiniMax: M3 | $0.30 | $0.06 | $1.20 | — | **$44.05** |
| [Alibaba](https://www.alibabacloud.com/help/en/model-studio/model-pricing): hosted Qwen3.8-27B, International | $0.50 | $0.10 | $3 | — | **$83.07** |

Google's Flash promotion runs through 2026-12-31; its estimates assume implicit caching, with no explicit-cache
storage charge. The Qwen cache rate assumes [implicit caching at 20% of input price](https://www.alibabacloud.com/help/en/model-studio/context-cache).
Kimi K3 lists cache writes at its ordinary input rate, so there is no write premium in this calculation. Batch,
regional premiums, taxes, paid provider tools and any separate cache-storage costs are excluded. Actual models
may tokenize differently, make different numbers of calls and achieve different cache hits.

**Actual self-hosted Qwen dollar cost remains unmeasured:** there is no per-token API bill, but GPU operation is
not free. A dollar total requires the allocated GPU time and hardware or rental cost. The hosted-Qwen row is only
an API-equivalent estimate. Generation and judge totals across all historical development runs cannot be treated
as exact costs of the final 1,006 cases.

## 13. Remaining measurements

The main gaps are a second solver model, a second blind annotator, valid coverage of the nine remaining facts,
the 38 missing fact–mode policy requirements, underspecified-policy baselines, both extensions on OpenClaw,
systematic value and disclosure checks, confirmed manual-review provenance for RQ7, and exact usage and GPU cost
for the selected 3,018 executions. No smaller suite has yet been demonstrated to preserve all reported coverage
and exposure findings.
