# Fact-discrimination tests for tool-using agents: concise results

*2026-09-29, brought to the rebuilt numbers on 2026-09-30 (the 10-minute budget, two PI rulings, duplicate policy
units, blind_review_01; every change is logged in [README.md](README.md), "Text changes"; numbers as of commit
a8c046c891, with the same day's follow-up for RQ7's policy side). Main evaluation: 998 methodology cases on OpenClaw
with self-hosted Qwen3.8-27B. Section and table numbers follow the longer report where retained. Recomputed counts
and the final execution manifest: [concise.json](numbers/concise.json), produced by [concise.py](kit/concise.py). The
second agent, GPT-6.1 Sol (the section after RQ6), was added on 2026-09-30 from the files of
[sol_eval_01](../sol_eval_01/README.md) at commit fca57dd6de.*

## 0.4 Size of the experiment

**The methodology suite contains 998 test cases, each executed three times: 2,994 executions.**
It combines tests of fact discrimination with tests of how the agent handles missing or ambiguous matches.
A second agent, GPT-6.1 Sol, ran 496 of the 513 Muse cases in the same harness. Its **1,488 executions** are
counted apart from the 2,994 and reported after RQ6.

| Test form | Sonnet scenarios | Muse scenarios | Cases | Executions |
|---|---:|---:|---:|---:|
| Cover: target present alongside decoys | 48 | 52 | **100** | 300 |
| Individual probe: target absent, one decoy | 174 | 187 | **361** | 1,083 |
| Fact probe: target absent, the decoys for one fact together | 49 | 53 | **102** | 306 |
| **Regular subtotal** | **271** | **292** | **563** | **1,689** |
| Absence policy: request presumes a match that does not exist | 116 | 126 | **242** | 726 |
| Underspecified policy: several records satisfy the request | 98 | 95 | **193** | 579 |
| **Methodology total** | **485** | **513** | **998** | **2,994** |

Writer columns identify the author of the parent scenario. Policy variants were subsequently derived by code
and Muse. A scenario can produce several cases; a case has three executions. None of those counts is a count
of model API requests: one execution normally makes several requests.

**Fact probes are additional, independently executed cases.** They belong to the broader probe category but
are excluded from the 361 individual probes. For example, two decoys for one fact can produce two individual
probes and one fact probe containing both. Thus the suite has **100 covers and 463 probes**, followed by
**435 policy cases**. The breakdown preserves their distinct outcomes throughout.

These counts use the final valid suite and final selected executions, with opaque identifiers where applicable.
Replaced executions, investigation, calibration and smoke tests do not enter the main denominator. RQ8's
separate comparison experiments are identified there. The defensible description is: **“We used 998 cases,
run three times each.”** This is the evaluated suite, not a demonstrated mathematical minimum that preserves
every coverage and exposure result.

**Two rulings of 2026-09-30.** Two of the PI's blind-review rulings, applied on 2026-09-30, made two Box near
misses flawed. They removed 2 probes and 6 policy units (2 absence, 4 underspecified): 6 regular and 18 policy
executions left the manifest, which went from 1,006 cases and 3,018 executions to 998 and 2,994. blind_review_01,
judge_qwen_01 and values_01 used the earlier 3,018-execution manifest and keep their own populations.

**Estimated Qwen consumption for these cases:** 368.77M input tokens, including 326.79M cached input, plus
9.58M output tokens: **378.36M tokens total**, with **88.62% of input cached**. This uses the agreed historical
average scaled by `2,994 / 4,464`; it is an estimate, not an exact audit of the selected executions. The historical
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
(regen_01). Facts credited per family, with overlap: F0 71, F1 81, F2 30, F3 1, F4 5, F5 22, F6 13, F7 38, F8 40.

## RQ3. How well does the generator perform?

**Table 5. Generation funnel for the regular methodology suite.** Source:
[generator.json](numbers/generator.json), aggregated by writer; brief outcomes and manual scenario reviews from
the [Sonnet study](../autogen_01/report.md), [Muse study](../autogen_02/report.md) and
[completion study](../completion_01/README.md). Rejected construction candidates below are not additional
cases in the 998-case evaluation.

| | Sonnet | Muse | Total |
|---|---:|---:|---:|
| Brief attempts | 50 | 58 | 108 |
| Accepted scenarios | 49 | 52 | 101 |
| Attempts rejected | 1 | 5 | 6 |
| Infrastructure failures | 0 | 1 | 1 |
| Usable scenarios after review | 48 | 52 | 100 |
| Declared decoys | 185 | 192 | 377 |
| Decoys ruled flawed | 7 | 3 | 10 |
| Derived regular candidates | 285 | 297 | 582 |
| Dropped: decoy loses its distinguishing condition | 5 | 2 | 7 |
| Further cases excluded by validity rulings | 9 | 3 | 12 |
| **Valid regular cases** | **271** | **292** | **563** |

There were 89 distinct briefs across the 108 attempts; 86 produced an accepted scenario. Of 101 accepted
scenarios, manual review classified 87 as valid, 13 as flawed but usable, and one as invalid. After the case-level
checks and rulings, **563/582 derived candidates (96.7%)** remain. Writer comparisons are descriptive: the
writers received different briefs and operated under different method versions.

The checks catch different problems: code finds decoys that violate two conditions or cease to work without the
target; replica checks find unusable seeds, unreadable values and writes that do not land; the independent reader
finds ambiguity and undeclared matches. Manual review still found domain misunderstandings and contrived wording.

**Table 6. Policy cases in the methodology suite.** Source: [policy.json](numbers/policy.json),
[concise.json](numbers/concise.json). Candidate counts are constructed policy units before validity exclusions.

| Policy form | Candidates | Excluded | Valid cases | Sonnet parent | Muse parent | Executions |
|---|---:|---:|---:|---:|---:|---:|
| Absence | 255 | 13 | 242 | 116 | 126 | 726 |
| Underspecified | 209 | 16 | 193 | 98 | 95 | 579 |
| **Total** | **464** | **29** | **435** | **214** | **221** | **1,305** |

Two underspecified pairs are one request each (U-AP-SLK-03 and U-G4-LIN-14; `openclaw_eval_01/rulings.py`,
`DUPLICATE_UNITS`). Both cases of each pair ran and count here; RQ6's policy statistic counts each pair once, so its
underspecified denominator is 191 cases (433 policy cases in all).

Absence variants remove the probe's permission to report no match. Underspecified variants drop an identifying
condition or introduce an additional full match. The correct response is to report absence, or seek clarification
before changing a record. Policy units are separate cases, even when derived from the same parent scenario.

Muse's writer and reader cost **$36.74 at list prices ($2.08 billed)** for 52 accepted scenarios and 292 valid
regular cases: **$0.71 per accepted scenario**, or **$0.126 per valid regular case**. These are generation costs;
§12 estimates the agent-under-test inference separately. Source: [costs.json](numbers/costs.json).

## RQ4. What failures do the tests expose on OpenClaw?

The 563 regular cases use the final OpenClaw/Qwen executions and the automated judge, checked in RQ5.
**Detect@3** means a fact is exposed in at least one of three executions; **detect@1** uses only the first.
Exposure means acting on a decoy or presenting it as the answer. An execution ended by the ten-minute budget
(OpenClaw's own turn limit) is an agent failure but earns no regular fact exposure. Replica artifacts are void.

**Table 7. Exposure by service.** Source: [exposure.json](numbers/exposure.json).

| Service | Cases | Cases exposing a fact | Facts exposed @3 | Facts exposed @1 | Facts covered | Covered facts exposed @3 |
|---|---:|---:|---:|---:|---:|---:|
| Box | 137 | 35 | 26 | 20 | 56 | 46% |
| Calendar | 103 | 34 | 17 | 13 | 34 | 50% |
| Linear | 213 | 47 | 31 | 19 | 80 | 39% |
| Slack | 110 | 23 | 13 | 8 | 34 | 38% |
| **All** | **563** | **139 (24.7%)** | **87** | **60** | **204** | **42.6%** |

**Table 8. Exposure by form, writer and fact kind.** Sources: [exposure.json](numbers/exposure.json),
[writer unions](numbers/concise.json). Facts can appear in several forms; their exposure counts must not be added.

| Form or writer | Cases | Cases exposing | Facts exposed @3 | Facts exposed @1 |
|---|---:|---:|---:|---:|
| Cover | 100 | 12 (12%) | 12 | 6 |
| Individual probe | 361 | 103 (29%) | 79 | 55 |
| Fact probe | 102 | 24 (24%) | 24 | 12 |
| Sonnet | 271 | 61 (23%) | 40 of 81 covered | 27 |
| Muse | 292 | 78 (27%) | 47 of 124 covered | 33 |

| Fact kind | Covered | Exposed @3 | Exposed @1 |
|---|---:|---:|---:|
| Attribute | 117 | 59 | 42 |
| Relationship | 48 | 19 | 12 |
| Hierarchy | 5 | 1 | 1 |
| Binding | 22 | 4 | 2 |
| Derived | 12 | 4 | 3 |

Individual probes expose more often than covers. Designated decoys expose in **86/280 individual probes (31%)**,
against **17/81 F0 probes (21%)**. F8 partial identity is strongest here: 24/51 (47%), followed by F1 sibling
fields or roles at 34/98 (35%) and F7 neighbouring values at 13/50 (26%).

Of 1,689 executions, 255 have counted grounding failures, 1,348 pass, 52 were ended by the budget, 20 fail only on
flawed decoys and earn no exposure, and 14 are void. These categories exhaust the regular executions.

## RQ5. How accurate is the automated judge?

Blind samples were drawn and manually labelled before reading the judge's verdicts. This section retains only
labels on the selected final executions. TP and TN mean agreement on failure and success; FP and FN mean false
alarms and missed failures. Void observations are counted separately.

**Table 9. Judge against blind labels on the final executions.** Source: [concise.json](numbers/concise.json),
`judge_accuracy` and `blind_label_keys`.

| Case type | Labelled executions | Agree | TP | FP | FN | TN | Both void | Label alone void | Same exposed facts on TP |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Regular | 105 | 105 | 16 | 0 | 0 | 88 | 1 | 0 | 16/16 |
| Absence | 107 | 106 | 65 | 0 | 0 | 33 | 8 | 1 | 65/65 |
| Underspecified | 94 | 94 | 40 | 0 | 0 | 45 | 9 | 0 | 40/40 |
| **All** | **306** | **305** | **121** | **0** | **0** | **166** | **18** | **1** | **121/121** |
| *blind_review_01, AI reference labels:* judge v2 | 132 | 128 | 68 | 4 | 0 | 51 | 9 | 0 | 68/68 |
| *blind_review_01:* pipeline (judge v2 or triage) | 199 | 195 | 68 | 4 | 0 | 118 | 9 | 0 | 68/68 |

The last two rows come from a second, separate review (below); the rest of this section uses the first four.
There are no false positives or false negatives in the **287 executions both call usable**. The approximate
rule-of-three 95% upper bounds are 2.5% for missed failures and 1.8% for false alarms; these describe this pooled
sample, not a guarantee over the suite. The one void disagreement is a timeout without a write; the budget
counts it as an agent failure regardless.

The final suite has **2,115 saved LLM verdicts**, of which 306 have retained blind labels. Mechanical triage
handles the other 879 executions; the LLM also audits a sample of mechanically clean executions.

**A second reference review: blind_review_01.** Codex labelled 200 of the 2,705 executions of the earlier
3,018-execution manifest (§0.4) that had no earlier label (seeded, stratified by service and form; 185 distinct
cases), with PI decisions affecting 12 of them, and locked the labels before seeing any verdict or mechanical score.
**These are AI reference labels, not a second human annotator.** The pipeline (judge v2 where it read the execution,
mechanical triage otherwise) agrees with them on **186 of 190** executions both call non-void: 68 TP, 4 FP, 0 FN,
118 TN. Judge v2 alone agrees on 119 of 123 and triage alone on 67 of 67 (all passes). Exposed facts agree on all 68
joint failures. The 4 false positives follow from three interpretation questions the PI settled before unblinding,
where the judge read the request more strictly. Case-cluster bootstrap 95% intervals for exact agreement, weighted
to the eligible pool: 96.1% to 99.5% for the pipeline and 94.3% to 99.3% for the judge. One execution stays
uncertain by the PI's choice and is left out. Sources: [blind_review_01](../blind_review_01/README.md),
`numbers.json` (`comparators`), `uncertainty.json`, `report.md`.

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

**Table 11. All eight policy cells.** Source: the decision records,
[decisions_population_absence.json](../openclaw_eval_01/runs/policy/decisions_population_absence.json) and
[decisions_population_underspecified.json](../openclaw_eval_01/runs/policy/decisions_population_underspecified.json),
which [policy.json](numbers/policy.json) copies; its valid counts keep both cases of each duplicate pair (below).

| Service and mode | Valid cases | Failing / usable executions | Rate [p10, p90] | Decision |
|---|---:|---:|---|---|
| Box, absence | 58 | 126/165 | 0.76 [0.70, 0.82] | Undecided |
| Calendar, absence | 42 | 101/124 | 0.82 [0.75, 0.87] | Undecided |
| Linear, absence | 99 | 160/263 | 0.61 [0.55, 0.67] | Not policy-level |
| Slack, absence | 43 | 75/125 | 0.60 [0.52, 0.68] | Not policy-level |
| Box, underspecified | 52 | 65/136 | 0.48 [0.41, 0.55] | Not policy-level |
| Calendar, underspecified | 30 | 37/81 | 0.46 [0.36, 0.56] | Not policy-level |
| Linear, underspecified | 78 | 83/205 | 0.41 [0.34, 0.47] | Not policy-level |
| Slack, underspecified | 31 | 63/82 | 0.77 [0.69, 0.84] | Undecided |

**Five cells are not policy-level and three remain undecided.** Every cell includes cases that always fail and
cases that never fail. This evidence does not support replacing the policy suite with eight representative
cases. The budget reading changes rates but none of these decisions: under the withdrawn eight-minute reading,
before the two rulings, the rates were 0.79, 0.83, 0.69, 0.62 (absence) and 0.58, 0.58, 0.51, 0.82 (underspecified).
Two underspecified pairs are one request each and count once here (Linear 79 → 78 and Slack 32 → 31 cases, RQ3). The
two rulings of 2026-09-30 left out 2 Box absence and 4 Box underspecified cases (§0.4).

**Table 12. Per-fact policy results.** Source: [policy.json](numbers/policy.json).
The last column counts **fact–mode pairs**, so the same fact may contribute once to each mode.

| | Absence | Underspecified | Combined |
|---|---:|---:|---:|
| Requirements: one per covered fact and mode | 204 | 204 | 408 |
| Valid executable cases | 242 | 193 | 435 |
| Facts with a valid policy case | 195 | 170 | 365 |
| Facts failing @3 | 157 | 111 | 268 |
| Facts failing @1 | 129 | 80 | 209 |
| Of facts with a case: both regular exposure and policy failure @3 | 77 | 52 | — |
| Policy failure only | 80 | 59 | — |
| Regular exposure only | 6 | 21 | — |
| Neither | 32 | 38 | — |

Why **435 cases for 408 requirements**? A fact can occur in several scenarios, each producing a policy case,
while some facts have no valid derivation. The 435 cases cover 365/408 fact–mode requirements (89.5%).
Another **80 facts** fail absence policy cases despite no regular exposure, and **59** fail underspecified
cases despite no regular exposure. They reveal behavior that the 563 regular cases alone miss.

Thus the accounting is **563 regular cases + 435 policy cases = 998**, with three executions per case.
The roughly 400 policy requirements are one component of that suite, not the entire methodology.

## A second agent: GPT-6.1 Sol on the same harness

GPT-6.1 Sol ran the Muse-written half of the suite on OpenClaw, with the same judge (v2 on Muse), rulings and
ten-minute budget, three executions per case. It ran **496 of the 513 Muse cases** (282 regular, 123 absence and 91
underspecified): **1,488 executions**, plus 3 of a probe that the rulings of 2026-09-30 left out after it ran. The Qwen
columns below are its final executions of the same cases, so they differ from Tables 7–12, which cover all 998 cases.
Source: [sol_eval_01](../sol_eval_01/README.md), Results, and the `eval/` files named under each table.

**What differs from the Qwen round:**

- **Access and thinking.** Sol ran on the PI's OpenAI plan in OpenClaw's own agent loop, with no proxy; usage comes
  from OpenClaw's session transcripts. Its thinking level is "medium", set explicitly. Qwen ran at "medium" as
  OpenClaw's fallback for a reasoning model; for GPT models the fallback is "off", which leaves OpenAI's default.
- **16 cases left out.** G4-LIN-08's 10 regular and 6 policy cases run under a test clock (2026-10-16) past the
  login's expiry (2026-10-10), and OpenClaw then fails before the first model call. One more underspecified case,
  U-G4-CAL-05-CalendarListEntry_summary_override, awaits the PI's reading and did not run.
- **memory_search fails.** OpenClaw's memory tool refuses the login copied into each execution, which carries the
  main agent's identity. 354 of the 1,491 executions called it; none needed memory, and 316 final answers mention
  the failure.
- **No visible reasoning.** Sol's record holds commands, responses, final answers and occasional reasoning
  summaries. The judge's mechanisms and the awareness count below rest on that visible text.
- **Infrastructure.** 17 failed attempts in 16 executions were re-run and never scored: 8 provider stalls and 9
  other provider errors.

**Table 12a. Regular cases: Sol and Qwen on the same 282.** Source: `sol_eval_01/eval/side_by_side_regular.json`
(`groups`, `trials`).

| Group | Cases | Exposing: Sol | Exposing: Qwen | Facts @3: Sol | Facts @3: Qwen | Facts @1: Sol | Facts @1: Qwen |
|---|---:|---:|---:|---:|---:|---:|---:|
| **All** | **282** | **13 (4.6%)** | **78 (27.7%)** | **7** | **47** | **7** | **33** |
| Box | 81 | 1 | 25 | 1 | 18 | 1 | 14 |
| Calendar | 60 | 4 | 23 | 2 | 11 | 2 | 9 |
| Linear | 103 | 5 | 18 | 3 | 13 | 3 | 6 |
| Slack | 38 | 3 | 12 | 1 | 5 | 1 | 4 |
| Cover | 51 | 2 | 8 | 2 | 8 | 1 | 5 |
| Individual probe | 181 | 8 | 56 | 7 | 43 | 7 | 31 |
| Fact probe | 50 | 3 | 14 | 3 | 14 | 3 | 6 |

| Executions of the 282 cases | Sol | Qwen |
|---|---:|---:|
| Counted grounding failures | 32 | 145 |
| Pass | 800 | 655 |
| Ended by the budget | 0 | 32 |
| Fail only on flawed decoys | 11 | 11 |
| Void | 3 | 3 |
| **All** | **846** | **846** |

Every fact Sol exposes, Qwen exposes too: 12 cases expose a fact for both agents, 1 for Sol only and 66 for Qwen
only.

- **What Sol exposes.** All 7 facts are attributes:
  - four partial names (F8 decoys expose in 5 of its 8 exposing probes);
  - three structured fields it did not read (Slack message blocks, a Calendar room resource, a Linear milestone's
    status).
- **How it fails.** In judge v2's mechanisms, Sol mostly never checked the deciding field: 23 of 32 counted
  failures (misread 8, saw the mismatch and acted 1). Qwen mostly saw the mismatch and acted anyway (79 of 145).
- **Voids.** Sol's 3 void executions come from a Linear replica defect.

**Table 12b. The eight policy cells on the same cases.** Source: `sol_eval_01/eval/policy_decisions.json` (`cells`
→ `sol`, `qwen_same_units`): RQ6's fixed rule on the Muse-parent policy cases, without G4-LIN-08's. Linear
underspecified counts its duplicate pair once, as in Table 11.

| Service and mode | Cases | Sol: failing / usable | Sol: rate [p10, p90] | Sol: decision | Qwen: failing / usable | Qwen: rate [p10, p90] | Qwen: decision |
|---|---:|---:|---|---|---:|---|---|
| Box, absence | 34 | 16/102 | 0.16 [0.09, 0.24] | Not policy-level | 70/95 | 0.74 [0.65, 0.82] | Undecided |
| Calendar, absence | 28 | 19/83 | 0.23 [0.13, 0.33] | Not policy-level | 74/82 | 0.90 [0.85, 0.95] | Policy-level |
| Linear, absence | 49 | 13/147 | 0.09 [0.04, 0.14] | Not policy-level | 68/125 | 0.54 [0.45, 0.63] | Not policy-level |
| Slack, absence | 12 | 4/36 | 0.11 [0.00, 0.22] | Not policy-level | 20/35 | 0.57 [0.42, 0.72] | Not policy-level |
| Box, underspecified | 30 | 0/90 | 0.00 [0.00, 0.00] | Not policy-level | 36/81 | 0.44 [0.35, 0.53] | Not policy-level |
| Calendar, underspecified | 21 | 7/59 | 0.12 [0.03, 0.22] | Not policy-level* | 31/55 | 0.56 [0.43, 0.69] | Not policy-level |
| Linear, underspecified | 32 | 0/99 | 0.00 [0.00, 0.00] | Not policy-level | 36/82 | 0.44 [0.33, 0.54] | Not policy-level |
| Slack, underspecified | 8 | 1/24 | 0.04 [0.00, 0.08] | Not policy-level | 20/24 | 0.83 [0.71, 0.92] | Undecided |

\* One case did not run for Sol (above), so the decision file marks the cell incomplete. If all three of its
executions failed, the rate would be 10/62 (0.16).

Sol's policy failures sit in few cases, counting cases with a usable execution:

| Mode | Sol: fail in some execution | Sol: … in all three | Qwen: fail in some execution | Qwen: … in all three |
|---|---:|---:|---:|---:|
| Absence | 21 of 123 | 15 | 92 of 119 | 71 |
| Underspecified | 4 of 90 | 2 | 56 of 87 | 29 |

Per fact, on the same cases:

| Mode | Facts with a valid case | Sol: failing @3 | Sol: failing @1 | Qwen: failing @3 | Qwen: failing @1 |
|---|---:|---:|---:|---:|---:|
| Absence | 115 | 19 | 16 | 87 | 75 |
| Underspecified | 100 | 5 | 4 | 61 | 46 |

12 of Sol's 19 absence facts and all 5 of its underspecified facts have no regular exposure.

**Table 12c. Judge v2 against blind labels on Sol's executions.** Source: `sol_eval_01/eval/judge_accuracy.json`.
180 executions were drawn before the runs, 45 per set, and labelled from the evidence before any verdict was read.
4 never ran, because their cases hold decoys that the rulings of 2026-09-30 made flawed.

| Case type | Labelled executions | Agree | TP | FP | FN | TN | Both void | Label alone void | Same exposed facts on TP |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Regular | 90 | 88 | 1 | 0 | 0 | 87 | 0 | 2 | 1/1 |
| Absence | 44 | 44 | 6 | 0 | 0 | 38 | 0 | 0 | 6/6 |
| Underspecified | 42 | 42 | 0 | 0 | 0 | 42 | 0 | 0 | – |
| **All** | **176** | **174** | **7** | **0** | **0** | **167** | **0** | **2** | **7/7** |

- **The two disagreements** are the executions the two rulings concern. They are labelled void (a flawed test)
  and judged failures by the construction. The rulings now leave the probe out and do not count the fact probe's
  execution.
- **The mechanism** agrees on 4 of the 7 failures. With Sol's reasoning unrecorded, it is the least certain part of
  a verdict.
- **Few failures.** Only 7 labelled executions are failures, so these figures rest on few cases.

**Speed and cost.** Sources: `sol_eval_01/eval/observations.json`, `judge_cost.json`.

| | Sol | Qwen, same cases |
|---|---:|---:|
| Median execution, by set | 37–53 s | 171–248 s |
| Ended by the budget | 0 of 1,491 | 99 of 1,491 |
| Agent hours | 19.6 | 100.2 |
| Model requests | 8,172 | 14,447 |
| Input tokens | 79.3M (72.6% cached) | 180.3M |
| Output tokens (of which reasoning) | 0.67M (16k) | 4.57M (2.76M) |

- Sol's longest execution took 134 s.
- The OpenAI plan has no per-token charge.
- Judging Sol's executions took 1,175 Muse calls, $32.60 at list price.

**Test awareness,** measured on visible text: Sol remarks on a trap, a decoy or a fixture in 11 of 1,491
executions, all in reasoning summaries. Qwen does so in 483, in its thinking. Neither does in a final answer.

**What it means.** The suite and its judge carry over unchanged to a second, stronger agent. Sol fails far less
often than Qwen: the same 282 cases expose 7 facts instead of 47, and all 7 are among Qwen's. It also fails
differently: it does not check, where Qwen sees the mismatch and acts anyway. Its failures reproduce. Detect@1 equals
detect@3 on regular cases, and 15 of its 21 failing absence cases fail all three executions. As for Qwen on OpenClaw,
no cell supports the eight-case policy shortcut, because Sol's policy failures depend on the case. The per-fact cases
find 17 fact–mode pairs with no regular exposure. Exposure counts therefore describe an agent as much as the suite,
and comparisons between agents need the same cases.

## RQ7. What happens outside the grounding criterion?

The judge grades which record the agent selects. Choosing the correct record can still produce a wrong value
or an unwanted side effect. Those errors do not count as fact exposure.

**Provenance clarification.** [beyond.py](kit/beyond.py) reads saved requests and state diffs directly to check
literal values and flag additional writes. Those measurements are independent of the judge's prose. A separate
analysis searches the judge's notes. The original author also states that every flagged execution was manually
reviewed. **Open point:** an itemized independent manual-review record establishing exactly which trajectories
were inspected, versus which interpretations came from judge notes, has not been located. The qualitative
side-effect classifications below retain the original author's review, except two rows corrected by
[values_01](../values_01/report.md), which re-read these categories from the raw evidence with an itemized record
(`values_01/eval/labels.jsonl`): every write-then-restore candidate and a sample of each side-effect kind.

**Table 13. Values written compared with literal values in requests.** Source:
[beyond.json](numbers/beyond.json), using the final manifest's 1,689 regular and 1,305 policy executions.

| Field | Regular writes checked | Wrong | Policy writes checked | Wrong |
|---|---:|---:|---:|---:|
| Linear priority | 58 | **42** | 91 | **63** |
| Linear estimate | 58 | 0 | 75 | 0 |
| Box tag | 99 | 0 | 184 | 0 |
| Slack reaction | 45 | 0 | 74 | 0 definite; 1 ambiguous |
| Slack archive state | 14 | 0 | 15 | 0 |
| Calendar hidden state | 21 | 0 | 17 | 0 |

**105/149 priority writes (70%) are wrong**, commonly reversing Linear's priority scale. Of 23 regular cover
executions that wrote the wrong priority to the right issue, 22 still score as correct grounding: 16 cleared
mechanical triage and six received a correct judge verdict. The remaining execution also wrote a decoy.

The separate text search of **2,115 retained judge verdicts** finds wrong-value language in 55, including ten
graded correct; side-effect language in one; and false-claim language in two. These are keyword matches in judge
notes, not an exhaustive error count. Source: [concise.json](numbers/concise.json), `judge_notes_on_final_executions`.

**Additional writes, classified in the original author's review:**

| Behavior | Regular | Absence | Underspecified | Example |
|---|---:|---:|---:|---|
| Created the presumed record | 3 | 10 | 2 | Posted the comment that the request used to identify a PDF. |
| Changed a record to fit the request | 0 | 2 | 0 | Reassigned an issue to the person the request presumed was its assignee. |
| Changed other fields, disclosed | 2 | 0 | 0 | Hid a calendar and also unchecked it. |
| Harmful additional change | 0 | 1 | 0 | Reset both attendees' replies with a full update while changing the room. |
| Other small writes | 2 | 0 | 0 | Opened a DM or set an icon. |
| Acted outside the declared candidate set | 0 | 4 | 0 | Hid a different calendar. |
| Wrote, then restored a record | 6 | 0 | 2 | Renamed the wrong team, then renamed it back. |
| Wrote a value already there, or a field the record lacks | 0 | 3 | 2 | "Hid" a calendar that was already hidden. |
| Posted a comment, then deleted it (no trace in the diff) | 1 | 1 | 0 | Posted "approved for launch" as the actor, then deleted it. |
| **Executions with any write** | **541/1,689** | **460/726** | **245/579** | |

A final diff alone cannot distinguish restoration from a write of an unchanged value. Read with their
trajectories (values_01), the 13 executions the original row counted (6, 3, 4) are 8 restorations and 5 no-op
writes; two more writes, comments posted and deleted, leave no trace in any diff. The meeting's time did not move:
the diff's time columns changed from 10:00 to 17:00 only because the replica stores times written through the API
in UTC and seeded times as local time; the API still shows 10:00, and the reply's time was right. Box also shows
32 changes caused by its replica clearing omitted lock or shared-link fields; these are recorded as replica effects.

**A fuller value audit: values_01.** A separate study checked all 3,018 executions of the earlier manifest (§0.4)
for what the grounding verdict does not grade: values written against a value declared per scenario, side effects in
the diff and the transcript, and the final reply against the diff ([report](../values_01/report.md)). Literal values
are copied exactly: 1,275 of 1,399 writes to a requested field hold the requested value. The errors are
interpretations: Linear's priority scale (105 of 149), a colour's palette, and a year taken from the run date. 179
executions carry such a finding, 52 of them with a passing grounding verdict. Replies repeat the priority belief: 96
state the requested value while another was written, and 60 misstate a priority. Of 15 writes the final state does
not show, 9 were not disclosed.

## RQ8. Baselines and ablations

These are **separate OpenClaw comparison experiments**, outside the 998-case methodology count and its token
estimate. The baseline study is [baselines_01](../baselines_01/report.md), now on main; the relevant summaries are
included in [concise.json](numbers/concise.json), `baseline_comparison` and `baseline_policy_facts`.

N0 asks Muse directly to write tests using the API and seeding documentation. N1 additionally supplies the fact
catalog. N0M and N1M add reviewer guidance about variety, difficulty and neutral identifiers. Each arm produces
48 tests, 12 per service, with manual labels written before reading assertion or judge results.

**Table 14. Baselines versus a 48-test Muse budget.** Our column is the exact expected value from uniform draws
of 12 valid cases per service from **all 292 Muse regular cases**, using final outcomes. It is not an additional run.

| | N0 | N0M | N1 | N1M | Methodology: Muse |
|---|---:|---:|---:|---:|---:|
| **Valid / generated tests** | **45/48** | **42/48** | **41/48** | **41/48** | **48/48 sampled from 292 valid** |
| Designated decoys / all declared decoys | 9/48 | 17/53 | 21/58 | 19/66 | — |
| Facts covered through designated decoys, valid tests | 7 | 12 | 17 | 13 | **38.3** |
| **Regular facts exposed @3** | **0** | **0** | **0** | **0** | **12.2** |
| **Regular facts exposed @1** | **0** | **0** | **0** | **0** | **7.7** |
| Failing tests @3, including policy and timeouts | 5 | 0 | 2 | 3 | 14.0 exposing tests |
| Policy facts failing @3, designated decoys only | 0 | 0 | 1 | 0 | — |
| Policy facts failing @1, designated decoys only | 0 | 0 | 1 | 0 | — |
| Policy facts failing @3, all decoy families | 4 | 0 | 2 | 1 | — |
| Policy facts failing @1, all decoy families | 3 | 0 | 2 | 0 | — |
| Own oracle precision, corrected for harness errors | 0.54 | 0 (21 false positives) | 0.27 | 0.03 | See RQ5 |
| Own oracle recall, same correction | 0.70 | Undefined: no true failures | 1.00 | 1.00 | See RQ5 |
| Generation cost for 48 tests: list (billed) | $0.51 ($0.03) | $1.20 ($0.06) | $0.67 ($0.03) | $1.14 ($0.06) | $6.04 ($0.34) |

The coverage row applies one rule to both sides: a fact counts when a valid test has an F1–F8 decoy for it
(baselines_01's rule; in this table, "designated" means F1–F8). The F0 rule (RQ2) would also credit plain decoys
for states and for the six facts without a usable lure; neither side is counted that way here. Counting every plain
decoy, the Muse expectation is **47.8 covered facts**; the baseline summaries give only the F1–F8 count. Writer cost
is amortized across all 292 valid Muse cases. The baseline and methodology failure-count row describes different
kinds of failure, so it is not a direct measure of fact-discrimination effectiveness.

Across **169 valid baseline tests, no fact is exposed in a regular, fact-sensitive test**. Baseline failures with
writes occur in presupposing requests, with one additional timeout-only test. Those still yield policy evidence:
N0 exposes four policy facts at detect@3 and three at detect@1. **That pair is not a fraction**; separate rows
avoid the original ambiguous `4 / 3` notation. Fractions such as `45/48` instead mean valid out of generated.

**Table 15. Component comparisons.** Sources: baseline summaries in [concise.json](numbers/concise.json),
the [paired-probe study](../baselines_01/plain48/README.md),
and Tables 8–10. Paired variants are distinct experimental conditions, not replacements of the main suite.

| Component | OpenClaw evidence |
|---|---|
| Probe form | N0 covers expose in 0/36 cases; its probe variants expose in 4/28, finding four facts @3 and three @1. |
| Designated lure, targeted comparison | In 12 selected probes, failing executions fall from 27/36 to 7/36 when the lure is replaced with a plain difference; excluding two confounded pairs gives 21/30 versus 2/30. |
| Designated lure, random comparison | Both variants of 48 randomly selected probes ran fresh: exposure in 14/48 with the lure versus 2/48 with a plain difference; 29/144 versus 3/144 executions. Discordant pairs: 13 versus one, paired sign test p = 0.002. |
| Forms in the methodology suite | Covers expose in 12/100, individual probes in 103/361, fact probes in 24/102. These are observations across different cases, not a controlled removal experiment. |
| Construction checks and reader | In a documented 31-draft Muse subset, 17 drafts were returned: ten for substantive flaws and seven for format. These are construction attempts, not extra solver cases. |
| Mechanical triage | 879/2,994 final executions have no LLM verdict; the other 2,115 include audits of clean results. Triage-alone accuracy has not been recomputed for this restricted scope. |
| Judge inputs | On the 39 shared retained executions, recall is 90.5% for the plain judge and J0, 95.2% for J1, and 100% for the methodology judge (Table 10). |

The paired random comparison supports the contribution of the designated lure. The baseline results support
the need for fact-sensitive forms. Neither supplies a baseline evaluation of underspecified policy cases.

## RQ9. Extensions awaiting OpenClaw evaluation

**Several-match requests** ask for every record satisfying the conditions, testing whether search reaches all
matches. **Capability-boundary requests** ask for changes the actor cannot perform, testing whether it reports
the limit instead of substituting an action. Neither extension has an OpenClaw result in this report. Both are
outside the 998 cases. Sources: [several-match study](../several_match_auto_01/report.md),
[boundary study](../boundary_auto_01/report.md).

## 10. Lessons

**Table 17. Failure mechanisms.** Sources: retained blind labels in [concise.json](numbers/concise.json),
automated regular judgments in [exposure.json](numbers/exposure.json).

| Mechanism | Regular blind failures (16) | Absence blind failures (65) | All counted regular failures, automated (255) |
|---|---:|---:|---:|
| Saw the mismatch and acted anyway | 10 | 50 | 164 |
| Skipped the deciding field | 5 | 10 | 63 |
| Checked and misread it | 1 | 5 | 28 |

Seeing the mismatch often does not stop the action. Conversely, in 45/85 usable blind underspecified executions,
the agent asked which match was intended. The requests' permission to stop or clarify matters alongside the fact.

Construction needs enforced decoy checks, an independent reader, opaque identifiers and appropriate dates for
time-sensitive requests. Correct grounding also needs to be separated from correct values: the priority errors
in RQ7 survive a correct grounding verdict. Replica behavior matters: some Linear writes succeed but return an
error, and omitted Box fields can be cleared unexpectedly.

## 11. Limits of the evidence

- Two models in one harness, OpenClaw. Qwen3.8-27B ran the whole final suite. GPT-6.1 Sol ran 496 of the 513
  Muse cases: G4-LIN-08's 16 could not run under their test clock, and one case awaits the PI's reading. No
  second model has run the Sonnet-written half, and Sol's reasoning is not recorded.
- One human annotator; 306 retained blind labels and no inter-rater measurement between people. blind_review_01
  adds AI reference labels (Codex, with the PI's adjudication) on 200 executions of the earlier manifest, not a
  second human. RQ7's detailed manual-review provenance remains open, except the two rows values_01 re-read with an
  itemized record.
- Validity rulings were made by the team, partly after outcomes were seen; two came from blind_review_01's reading
  on 2026-09-30 (§0.4). The ten-minute budget is OpenClaw's own turn limit, which every final execution used; an
  earlier eight-minute reading, applied after the runs, was withdrawn.
- Replicas have missing features and artifacts; 42 catalog facts are unservable.
- Writer comparisons use different briefs and method versions. Some coverage is weaker: 37 facts have only F0
  evidence (under the F0 rule the designated form for 36; the 37th is being regenerated), and two have cover-only
  evidence.
- Policy cases can share a fact or scenario. The bootstrap samples cases; dependence can limit generalization.
- Baseline arms are small. The cost comparison fixes token counts and caching, not model behavior or quality.

## 12. Cost estimates for the 998 methodology cases

These estimates replace the solver model while holding its total input, output and observed cache hit constant.
They cover **2,994 solver executions only**. They are hypothetical API charges, not payments made for the
self-hosted Qwen runs, and exclude test generation, judges, comparison studies and development.

| Estimated token category | Millions |
|---|---:|
| Input, total | **368.77** |
| Cached input reads | 326.79 |
| Input not served from cache | 41.98 |
| Of uncached input: cache creation | 30.70 |
| Output, including reasoning | **9.58** |
| **Input + output** | **378.36** |

The assumed input-cache hit is **88.62%**. Cache creation is part of input, not extra tokens. With prices per
million tokens, the calculation is:

`41.98079 × input price + 326.79366 × cache-read price + 9.58118 × output price`

Where cache writes have a premium, add `30.70467 × (cache-write price − input price)`. This assumes the same
cache creation volume and uses five-minute writes where that choice is offered. All rates below are USD per
million tokens, standard service and the applicable short-context tier, checked 2026-09-29.

**Table 18. Estimated API cost for the complete 998-case suite.** Provider links identify pricing sources.

| Provider and model | Input | Cache read | Output | Cache write rate if premium | Estimated total |
|---|---:|---:|---:|---:|---:|
| [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing): Haiku 4.5 | $1 | $0.10 | $5 | $1.25 | **$130.24** |
| Anthropic: Sonnet 5 / 5.5 | $2 | $0.20 | $10 | $2.50 | **$260.48** |
| Anthropic: Opus 5.5 | $4 | $0.20 | $20 | $5 | **$455.61** |
| [OpenAI: GPT-5.4 Mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini) | $0.75 | $0.075 | $4.50 | — | **$99.11** |
| [OpenAI: GPT-5.4](https://developers.openai.com/api/docs/models/gpt-5.4) | $2.50 | $0.25 | $15 | — | **$330.37** |
| [OpenAI: GPT-5.5](https://developers.openai.com/api/docs/models/gpt-5.5) | $5 | $0.50 | $30 | — | **$660.74** |
| [OpenAI](https://developers.openai.com/api/docs/pricing): GPT-6 Luna | $0.10 | $0.01 | $0.50 | $0.125 | **$13.02** |
| [OpenAI: GPT-6 Sol](https://developers.openai.com/api/docs/models/gpt-6-sol) | $2 | $0.20 | $10 | $2.50 | **$260.48** |
| OpenAI: GPT-6.1 Sol | $2 | $0.10 | $10 | $2.50 | **$227.81** |
| OpenAI: GPT-6 Astra | $10 | $1 | $50 | $12.50 | **$1,302.42** |
| [Google](https://ai.google.dev/gemini-api/docs/pricing): Gemini 3.5 Flash-Lite | $0.30 | $0.03 | $2.50 | — | **$46.35** |
| Google: Gemini 3.5 Flash | $1.50 | $0.15 | $9 | — | **$198.22** |
| Google: Gemini 3.6 / 3.7 / 3.8 Flash, promotional | $0.75 | $0.075 | $3.75 | — | **$91.92** |
| Google: Gemini 3.1 Pro Preview | $2 | $0.20 | $12 | — | **$264.29** |
| [xAI: Grok 4.7](https://docs.x.ai/developers/models/grok-4.7) | $2 | $0.50 | $6 | — | **$304.85** |
| [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/): V4.1 Flash, off-peak | $0.15 | $0.003 | $0.60 | — | **$13.03** |
| DeepSeek: V4.1 Flash, peak | $0.30 | $0.006 | $1.20 | — | **$26.05** |
| DeepSeek: V4 Pro, off-peak | $0.66 | $0.022 | $1.98 | — | **$53.87** |
| DeepSeek: V4 Pro, peak | $1.32 | $0.044 | $3.96 | — | **$107.74** |
| [Moonshot](https://platform.kimi.ai/): Kimi K2.6 | $0.95 | $0.16 | $4 | — | **$130.49** |
| Moonshot: Kimi K2.7 Code | $0.95 | $0.19 | $4 | — | **$140.30** |
| Moonshot: Kimi K3 | $3 | $0.30 | $15 | — | **$367.70** |
| [Z.ai](https://docs.z.ai/guides/overview/pricing): GLM-5 | $1 | $0.20 | $3.20 | — | **$138.00** |
| Z.ai: GLM-5.1 / 5.2 / 5.3 | $1.40 | $0.26 | $4.40 | — | **$185.90** |
| Z.ai: GLM-5.3 Flash | $0.15 | $0.03 | $0.50 | — | **$20.89** |
| [MiniMax](https://platform.minimax.io/docs/guides/pricing-paygo): M2.5 | $0.30 | $0.03 | $1.20 | $0.375 | **$36.20** |
| MiniMax: M2.7 | $0.30 | $0.06 | $1.20 | $0.375 | **$46.00** |
| MiniMax: M3 | $0.30 | $0.06 | $1.20 | — | **$43.70** |
| [Alibaba](https://www.alibabacloud.com/help/en/model-studio/model-pricing): hosted Qwen3.8-27B, International | $0.50 | $0.10 | $3 | — | **$82.41** |

Google's Flash promotion runs through 2026-12-31; its estimates assume implicit caching, with no explicit-cache
storage charge. The Qwen cache rate assumes [implicit caching at 20% of input price](https://www.alibabacloud.com/help/en/model-studio/context-cache).
Kimi K3 lists cache writes at its ordinary input rate, so there is no write premium in this calculation. Batch,
regional premiums, taxes, paid provider tools and any separate cache-storage costs are excluded. Actual models
may tokenize differently, make different numbers of calls and achieve different cache hits.

**Actual self-hosted Qwen dollar cost remains unmeasured:** there is no per-token API bill, but GPU operation is
not free. A dollar total requires the allocated GPU time and hardware or rental cost. The hosted-Qwen row is only
an API-equivalent estimate. Generation and judge totals across all historical development runs cannot be treated
as exact costs of the final 998 cases.

## 13. Remaining measurements

The main gaps are a second solver model on the Sonnet-written half (GPT-6.1 Sol ran the Muse-written half), a
second human blind annotator (blind_review_01's labels are an AI's), valid coverage of the nine remaining facts, the
43 missing fact–mode policy requirements, underspecified-policy baselines, both extensions on OpenClaw, value and
disclosure checks inside the pipeline (values_01 audited them once, on the earlier manifest), confirmed manual-review
provenance for RQ7's remaining rows, and exact usage and GPU cost for the selected 2,994 executions. No smaller suite
has yet been demonstrated to preserve all reported coverage and exposure findings.
