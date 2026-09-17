# Campaign methods and interpretation

This is a recorded development campaign, not a preregistered held-out evaluation.
The source model, cards, coverage mapping, construction audits and reference run
labels are manual work. Writer, compiler, reviewer, solver and evaluator outputs
come from `us.anthropic.claude-sonnet-5` on Bedrock in `us-west-1`.

## What is fixed

The coverage inventory consists of 174 retained complete routes, 26 identifying
attributes, 28 entity/resolution-mode requirements and 25 representative
capability boundaries. These are separate linear inventories, not a Cartesian
product. The first six route assignments are explicitly marked calibration.
Other route modes are assigned by cycling modes within each root entity before
observing solver outcomes. Six baseline mutation assignments were chosen from
compound-reference tasks without reading ground-truth run labels.

The existing 59 baseline solver runs are reused. New solver episodes use the
same repository baseline harness and instructions. Solvers receive the user
request and documented service interface, not private selectors, cards,
construction plans, expected referents, access-review conclusions or ground
truth. Initial/final snapshots, native diffs, final responses and trajectories
are preserved. A turn limit or other unresolved run is not silently called a
successful grounding demonstration.

## Automated authoring

1. Code selects a route/mode assignment and supplies the existing full seed,
   model/schema and API context. Later recovery requests also supply mechanical
   variable/foreign-key bindings to make relationship roles explicit.
2. A writer produces a short natural request, role table, binding explanation,
   grounding metadata and task lines. Conditions and plausible negatives arise
   from the assigned path. The role table is a construction plan, not seed data.
3. An independent reviewer checks the plan. Necessary design repairs return to
   the writer in the same native conversation. Adequate wording is retained.
4. A separate compiler produces seed patches, native bindings and finite
   relational selectors. Code applies patches to the existing seed and assembles
   cards. The compiler must preserve the writer-approved prompt.
5. Mechanical checks validate actual fields/keys, the complete selected set,
   alternatives, negative exclusions, card inventory and assignment. Independent
   model review checks the request's ordinary meaning, route, access and quality.
6. Disposable live environments test whether the selector's facts are exposed
   by discoverable API calls. An independent API-observation review may establish
   access when the conservative mechanical traversal is inconclusive. Its input
   omits the seed, expected matches, cards and author claims. Its proposed sets
   and evidence locators are mechanically checked against recorded observations
   and the actual seed before solver execution.
7. Eligible cases run through the unchanged solver and existing card evaluator.
   The evaluator may receive one native conversational repair for mechanical
   validation errors. Returned semantic judgments are not selected against labels.

A selector establishes a database property, not natural-language equivalence.
For example, a workspace-member join does not prove message authorship. Nor does
an assigned route or a private join earn route coverage by itself. Manual audits
check this distinction and record rejected route claims.

Environment-only mutations retain the original prompt and intended referents.
The later source-preserving adapter copies existing cards/task lines mechanically
and asks the compiler only for the focal selector and environment patch. Earlier
attempts that unnecessarily re-extracted those references remain recorded. An
unchanged seed is a no-op replication, not a mutation. An access-only change
cannot by itself establish that a useful negative was introduced.

## Repairs, versions and exclusions

All role conversations preserve native assistant content, including returned
thinking blocks/signatures. Repair messages follow those responses; transport
failures have no fabricated assistant answer. Exact requests, instructions,
usage, responses and intermediate artifacts are saved per turn.

The first construction pass used bounded design and compilation review loops.
Subsequent development passes address diagnosed format/transport problems,
actual API access failures, or manual route findings. They are separately marked;
manual construction feedback is intended to exclude solver responses and reference
labels. One audited exception, G-R094’s explicit route revision, received a summary
of the earlier solver answer. That revised case is excluded from primary
outcome-blind coverage/failure counts; see `provenance_exceptions.json`. No
baseline reference run labels were supplied to authoring. Some recovery output limits were raised to 24,000 tokens after truncated
responses. Each recorded request, rather than the latest prompt file, identifies
the settings used for that invocation. There is no claim of one unchanged prompt
throughout the campaign.

Old cases/runs live in `execution_attempts/`, construction `*-before-*` files and
`manual_review_history/`. Revisions require new manual confirmation: judgments
are tied to a hash of the reviewed case. Costs and failed attempts remain in the
ledger. An explicit technical retry repeats the same evaluator request when no
response was received; it does not choose between semantic answers.

Automated review acceptance, API accessibility, manual validity, route realization
and solver failure are separate measurements. A valid shorter-route task can
fail its assigned long-route requirement. An unsupported requested deliverable
can be meaningful as a capability probe but is not silently counted as a normal
executable route task. Incidental API limitations do not automatically fill the
capability catalog. Boundary probes performed directly by Codex are manual
engineering evidence and are not automated generation successes.

## Goals and scoring

**G1** projects the manually reviewed baseline cards and source mapping. Requested
plurality is distinguished from seed cardinality; optional delegated subsets
remain separate. Join-only foreign keys do not automatically earn identifying-
attribute coverage.

**G2** uses fresh automated assessments of the unchanged baseline runs to flag
native-oracle false passes, followed by manual evidence confirmation. No reference
labels are fed into that process. Mutation comparisons distinguish whole-run
correct-to-incorrect transitions from focal-obligation transitions. An initially
incorrect run does not establish a whole-run regression. An invalid/no-op mutant
cannot establish a transition, even if a later solver answer differs.

**G3** records every assignment, construction failure, repaired artifact, review,
access failure and solver outcome. Automated flags require evidence confirmation
before they are called discovered grounding failures. A bad card cannot establish
a solver bug. Required-route coverage describes the request; runnable coverage additionally requires successful access qualification. An explicitly named workspace is a requested endpoint even if its name is not exposed, whereas merely adding a current-workspace join does not create a requested endpoint. Early absence can legitimately short-circuit later conditions, with weaker challenge quality recorded separately.

Manually rejected route claims and human-assisted development
revisions remain visible rather than being removed from attempt denominators.
Manual reviews are diagnostic, not a random sample unless explicitly stated;
small inspected subsets cannot establish an overall validity percentage.

**G4 alone** loads the existing 59-case reference run labels. A structured evaluator
and card-free direct judge receive the same underlying request/state/diff/answer/
trajectory/API evidence; the structured approach additionally receives manually
curated cards and task specifications. Direct localized reports are manually
matched to reference violations. Report precision and obligation recall have
different denominators; case-level failing-run detection is shown separately.
Some policies/examples were developed using these cases, so this is not held-out
accuracy or proof of generalization to other domains.

## Costs and reproduction

`usage_summary.json` and `usage_ledger.json` count saved calls and solver turns,
including repair and archived execution attempts. Calls without returned usage
remain unknown. Dollar totals are our historical-rate estimates from native
usage, not provider-billed dollar amounts. Existing baseline solver cost is not
charged again merely because those saved runs are reused.

From the repository root, using the configured Python environment:

```sh
python -m grounding.slack_campaign.campaign_metrics
python -m grounding.slack_campaign.usage
python -m grounding.slack_campaign.score_baseline
python -m grounding.slack_campaign.manual_baseline_review
```

The first two commands project saved artifacts only. The latter two reproduce
baseline measurements and explicit manual matching/confirmation records. Paid
construction/execution entry points are documented in the campaign package; do
not rerun them merely to regenerate tables. Keep at most 15 paid calls active
across all worker processes, not 15 per process.
