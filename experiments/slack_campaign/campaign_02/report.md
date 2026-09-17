# Slack G1–G4 campaign — in progress

This report is a checkpoint, not the completed campaign. Clean generation and
mutation are still running. Source modeling, cards and reference labels are
manual work; writer/compiler/reviewer/solver/evaluator calls use Sonnet 5 on
Bedrock. The historical premature pilot is preserved separately in `pilot_01`
and is not pooled into these generation yields.

## G1: baseline design

| Measure | Result |
|---|---:|
| Baseline tasks | 59 |
| Tasks with grounding obligations | 58 / 59 |
| Grounding obligations | 198 |
| Fully checked by native assertions | 74 / 198 |
| Partially checked | 37 / 198 |
| Unchecked | 87 / 198 |
| Complete retained routes represented | 12 / 174 |
| Entity–resolution-mode requirements represented | 12 / 28 |

Requested modes: 129 single, 34 determined collections, 11 absent, 20
underspecified. Four delegated optional subsets are tracked separately, rather
than relabeled as determined collections. A plural request can remain multiple
when its supplied seed has only one matching record.

[Counts](g1.json) come from the manually reviewed source cards.
[Baseline mapping](../../../grounding/slack_coverage/baseline_mapping_review.md)
records identifying paths and requested modes without consulting run labels.
The [linear catalog](../../../grounding/slack_coverage/catalog.md) also has 26
identifying-attribute and 25 capability-boundary requirements; their detailed
realization accounting is being completed.

## G2: native false passes

Fresh card-based assessments were run on all 59 existing solver runs. Manual
confirmation found **nine grounding violations in seven native-accepted runs**.
The native oracle accepted 47 runs in total. This is a count of confirmed
discoveries, not a claim that all possible failures were found.

| Native-accepted task | Confirmed grounding obligations |
|---|---|
| slack_67 | O1: incomplete lunch set and wrong extra target |
| slack_74 | O1: omitted question source |
| slack_95 | O1: unresolved channel choice presented as settled |
| slack_97 | O4: substituted CDN discussion source |
| slack_101 | O2, O5, O8: false absence / unauthorized channel selections |
| slack_107 | O5: circuit-tracer source substitution |
| slack_110 | O7: unauthorized edit-target selection |

[Manual confirmations and source links](g2_native_manual_review.json) preserve
the evidence and reasoning. Environment-only mutations are still being built;
no transition yield is claimed yet. Their assignment list was fixed without
using ground-truth labels. Existing incorrect baselines remain in accounting but
cannot establish correct-to-incorrect transitions.

## G3: generation

The fixed plan contains 174 route assignments. The first six are explicitly
marked development/calibration; they must remain distinguishable from later
production authoring. Each uses the existing seed, a short writer design,
separate compiler, mechanical card assembly, independent review, live API access
checks, the unchanged baseline solver and the existing evaluator. Repairs use
native conversation continuations; failed/unrealized attempts remain recorded.

One confirmed example so far is [G-R108](construction/G-R108/case.json):
“Which emoji reactions have been added to messages written by members of the
project-alpha-dev channel?” The solver reported no reactions, although three
qualifying reaction records were accessible. See its
[answer and trajectory](execution/G-R108/solver/G-R108.json),
[assessment](execution/G-R108/assessment/assessment.json), and
[manual confirmation](manual_review.json).

G-R001 is a useful counterexample to automatic coverage credit: the reviewer
accepted its channel-topic task, but manual review found its workspace relation
was merely fixed context. It receives no credit for the assigned
Conversation→Workspace route. A query join alone does not establish that the
request exercises a route.

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

## Cost and provenance

[Usage ledger](usage_ledger.json) and [summary](usage_summary.json) include saved
attempts and repairs. Dollar figures are our estimates at recorded historical
rates, not provider-billed amounts. Running/unreturned calls remain explicitly
unknown. Update these files as the campaign progresses; do not read a checkpoint
cost as the final total.
