# Slack G2/G3 construction pilot

This package implements a bounded Sonnet construction/execution pilot for the
shared G2/G3 campaign. Coding, coverage modeling and pilot selection are manual work.
Requests, seeds or seed edits, updated grounding cards and task specifications
must come from the separate construction model; a manually written test is not
counted as an automatically generated case.

The pilot assignments are in [pilot_assignments.json](pilot_assignments.json),
with their rationale in [pilot_selection.md](pilot_selection.md). They fix 14
initial jobs: two mutations and twelve clean generations, two per referent
entity. The distribution is three single, five multiple, three absent and three
underspecified. One conditional mutation follow-up can add a fifteenth job.
Assignments are planned coverage, not achieved coverage. No new easy controls
are generated.

The initial prototype also includes manual review of generated-case quality and
explicitly requested repairs. These interventions are part of developing and
auditing the workflow, not evidence of fully unattended generation. Preserve
their feedback, preceding outputs and paid repair calls when reporting yield.
The canonical experiment folder is
[pilot_01](../../experiments/slack_campaign/pilot_01/); its changing results are
reported there, rather than fixed as totals in this implementation guide.

## Construction policy

| Starting point | Construction |
| --- | --- |
| Baseline with one identifying condition | Preserve its focal path and operation; enrich with up to two natural auxiliary conditions. If the resulting valid case has no demonstrated grounding failure, add a focal near miss as a separate stage. |
| Baseline already expressing a compound condition | Add a plausible negative that matches the auxiliary conditions and fails the focal condition. Preserve the original prompt and intended matches for this environment-only stage. |
| Missing referent route or other coverage requirement | Generate one valid case directly, including a focal near miss. Do not generate an easy counterpart. |

A relationship route can express one focal predicate with meaningful internal
bindings. It need not be expanded into multiple independent criteria before a
plausible near miss is possible: the same people or content can occur in a
different relationship. Preserve the selected referent entity and focal path in
mutations. Reusing a baseline environment for a new focal path is clean
generation, not mutation of that reference.

The initial mutation assignments are Slack 58 (name-based recipient, enrichment)
and Slack 66 (message content plus channel, direct near miss). Their selection
used prompts and design cards, without consulting solver judgments. The optional
Slack 58 follow-up is gated by the campaign evaluator after the valid enriched
case runs; invalid construction or an evaluation error does not satisfy the
gate. An accepted `not_established` judgment is not a demonstrated failure and
must remain separately visible in reporting.

Existing baseline runs supply comparisons where appropriate. An adapted request
compared with its original is an adapted variant, not a controlled
environment-only comparison. When enrichment is followed by a near miss, those
two observed stages share the enriched request. Clean-generated cases contribute
valid yield, new coverage and confirmed failure discoveries without manufactured
easy/strengthened pairs.

## Modes and coverage accounting

- **Single:** one entity is requested, including explicit delegated choice of one
  eligible entity.
- **Multiple:** the matching collection is jointly intended. This describes the
  request's selection semantics, not merely a seed containing two or more rows.
- **Absent:** the described reference has no match in its complete supplied scope.
- **Underspecified:** the intended selection is unresolved without delegated
  authority; possible candidate sets are not permission to choose one.

For example, Slack 66 asks about the MCP deployment **questions** in #general.
That is a jointly intended collection even though the existing seed has one
matching question. Its near-miss mutation preserves that one intended match;
it must not add a positive target merely to satisfy a numerical mode check.
Clean multiple-mode cases should contain at least two intended referents to
exercise collection handling. That is a construction-quality requirement, not
the definition of the mode. Record actual match cardinality separately.

The campaign's route, identifying-attribute, entity–mode and capability-limit
requirements are separate dimensions. A validated case can satisfy several
requirements simultaneously, without claiming untested cross-products. The pilot
does not cover all 28 entity–mode requirements or all 174 retained routes. Its
direct User name assignment has no fabricated relationship-route ID. Long-route
credit requires the complete relationship predicate, not merely the presence of
its tables somewhere in the seed.

## Construction and acceptance sequence

1. Supply one fixed assignment and allowed domain/API context.
2. The author designs the request, selection, resolution and negative, then
   materializes the seed or edits, cards, task lines and private selector in the
   same conversation.
3. Recompute matches and negatives from real fields and relationships; check
   native keys, constraints, card inventory, direct links and assignment locks.
   A bounded repair is a follow-up in the existing author conversation.
4. An independent reviewer checks the prompt's meaning, bindings, mode,
   realism, answer hints, API scope and mutation integrity. A machine-checkable
   selector is a construction claim, not proof that the prose means that query.
5. Install a fresh environment and export its actual initial state. Revalidate
   selection/cards on that state. Try the deterministic forward API-visibility
   check first. If it is inconclusive, an independent Sonnet access review may
   establish the facts using a different traversal of recorded, discoverable API
   observations. Neither successful authentication nor an existing database row
   establishes visibility by itself.
6. Run the same solver harness/configuration as the baseline on the isolated
   case. Obtain its trajectory, response and native net diff without mutant
   native-assertion grading.
7. Assess the completed run with the existing card-guided evaluator. Manually
   confirm reported grounding violations for G2/G3 discovery claims.

Do not count construction validity before the runtime checks, or count attempted
coverage as achieved. Keep invalid, unrealized and rejected cases, every repair,
and all paid invocations in the ledger. A failed generation is not a solver
grounding failure. A valid case on which the solver succeeds remains a valid
campaign result.

The solver receives the ordinary request and its normal API/tool environment.
It does not receive cards, private construction selectors, intended IDs or
near-miss labels. The evaluator receives the request, cards/task specification,
installed seed, observed response/trajectory, API documentation and recorded
diff. Author traces and coverage assignments are omitted from that evidence.

## Runtime and repair gates

`pilot.py execute` checks the source case, installs it, and validates the
selector/cards again against the exported state after database defaults. Before
the solver starts, the runtime verifies that its new clone matches that inspected
state and reruns the installed validation callback. Schema creation, cloning and
cleanup are serialized across campaign threads/processes to avoid PostgreSQL
catalog races; model calls and ordinary Slack operations remain concurrent.

The forward visibility check tracks discoverable IDs and whether the recorded
responses establish the required fields and complete relationship populations.
An inconclusive result can reflect that check's traversal limitations. Its
fallback, [verify_access.py](verify_access.py), receives the prompt, selector and
only discoverable successful API observations. It does not receive the seed,
expected matches, cards, declared negatives or the previous check's conclusion.
The model derives matches and provable focal negatives and cites supplied probe
indices. Code compares the result with the complete installed-state selector,
checks citations/completeness and verifies every declared negative. This is
model-assisted validation, not a formal proof of API access.

The fallback permits one conversational repair for a malformed or mechanically
inconsistent complete response. The follow-up gives validation errors without
the expected target IDs. A blocked, unresolved or still-invalid review prevents
solver execution. The original forward result and the accepted proof method are
both preserved. Author construction repairs and evaluator-output repairs likewise
continue their existing native conversations rather than rebuilding a prompt.

Construction permits a bounded mechanical repair, and `construct` automatically
requests one semantic repair after a rejected independent review. The explicit
`repair_construction` entrypoint additionally supports one recorded repair per
`semantic`, `runtime` or `annotation` stage; runtime and annotation repairs are
deliberate interventions, not an unlimited automatic retry loop. Annotation-only
repair freezes the request, seed, actor, private selector and concrete referents,
then checks the revised cards/task specification independently. Earlier attempts
remain evidence. A later quality hold can disqualify an apparently accepted case
without erasing its executions or costs.

## Code and entrypoints

Use module invocation from the repository root. Examples below use placeholder
paths; construction and solver commands make paid model calls.

| File | Role |
| --- | --- |
| [pilot.py](pilot.py) | Resumable construction, installed-state/access gates, solver/evaluator execution and report/usage aggregation. |
| [build_assignments.py](build_assignments.py) | Deterministically builds/checks the manually selected assignments and source hashes. |
| [generate.py](generate.py) | Author design/materialization, bounded mechanical repair and independent semantic review. |
| [bedrock.py](bedrock.py) | Native Bedrock conversation history and per-call recording. |
| [selection.py](selection.py) | Finite real-field relational selector; no generated Python/SQL execution. |
| [validate.py](validate.py) | Seed, referent, negative, card and task-spec checks. Semantic/API validation remains separate. |
| [runtime.py](runtime.py) | Local isolated templates, API visibility observations, baseline solver reuse and evaluator input preparation. |
| [verify_access.py](verify_access.py) | Independent API-evidence review after an inconclusive forward check, with one bounded conversational repair. |
| [prompts/author.md](prompts/author.md) / [prompts/reviewer.md](prompts/reviewer.md) | Construction and independent review instructions. |

```bash
python grounding/slack_campaign/build_assignments.py --check
python -m grounding.slack_campaign.pilot construct --folder /path/to/campaign --concurrency 15
python -m grounding.slack_campaign.pilot execute --folder /path/to/campaign --concurrency 15
python -m grounding.slack_campaign.pilot report --folder /path/to/campaign
```

The campaign folder must already contain `assignments/<case_id>.json`, one
assignment object per file, including `case_id`. Preserve the source manifest as
provenance. `--ids P01 P02` restricts a phase to named cases, and concurrency is
bounded to 1–15. Existing case directories are not overwritten or silently
re-executed. An incomplete execution directory requires inspection; preserve an
unsuccessful attempt under `preflight_failures/` before deliberately retrying.

`construct` makes author/reviewer calls. `execute` requires the local backend,
`DATABASE_URL`, platform credentials and Bedrock access; it may make access-review,
solver and evaluator calls. It invokes the existing ordered evaluator with one
validation-repair allowance. `report` reads artifacts without invoking a model,
and is also run after construction/execution phases. These commands provide the
pilot orchestration; they do not implement an autonomous scheduler over the full
coverage catalog.

The conditional follow-up is an explicit assignment with `parent_assignment_id`,
the accepted parent assessment in `stage_gate`, `locked_prompt`, and
`source_case_path`. The pilot does not silently invent or schedule that follow-up.
Check its recorded gate before adding it to `assignments/`; it contributes an
additional attempted case, not an easy control.

Lower-level entrypoints remain available for inspection:

```bash
python -m grounding.slack_campaign.generate --assignment /path/to/one-assignment.json --out /path/to/new-construction
python -m grounding.slack_campaign.validate /path/to/case.json
python -m grounding.slack_campaign.runtime prepare --case /path/to/case.json --out /path/to/new-preflight
```

`generate --assignment` takes one assignment object, not the whole manifest.
Runtime `prepare` installs/probes without a model call. Prefer `pilot execute`
for the full acceptance sequence; bare runtime commands do not replace every
orchestration check. Remove an unused prepared template with
`runtime cleanup --prepared ...`.

## Outputs and outcome interpretation

Each construction directory records its assignment/input, author and reviewer
conversations, candidate cases, validation results, repairs and `summary.json`.
`construction_validated` precedes runtime access validation. Each execution
directory records source/installed checks, initial state, API probes, original
forward result, accepted visibility certificate, solver run and evaluator output.
The evaluator bundle excludes private construction annotations and uses the
actual installed seed. The solver keeps its baseline configuration; native
mutant assertions are replaced by the platform's diff operation.

Execution summaries distinguish errors and unresolved access/evaluation from
`completed`. Completed summaries include grounding verdicts and `automated_flags`
for `demonstrated_incorrect` obligations. These are evaluator flags awaiting
confirmation, not confirmed failures. `not_established` is retained separately.
Manual validity holds and annotation-quality findings must accompany the report;
successful execution alone does not certify a valid construction or useful
coverage.

`report.json` combines assignment, construction and execution records. It includes
`recorded_invocations`, `unknown_usage_records`, `tokens`, `tokens_by_stage`,
`estimated_cost_usd` and the rate table. `usage_ledger.json` preserves individual
call records, including author/reviewer repairs, access review, solver turns,
evaluator repairs, baseline evaluator calls and retained preflight failures.
An unreturned/unknown-usage call is marked unknown rather than assumed free.
The report is an observation/usage aggregation, not an automatic certification
of all coverage credits or a completed G2 transition analysis.

## Evidence, costs and ground truth

Bedrock calls save requests, raw responses, returned thinking blocks, JSON
outputs, native token usage, elapsed time and errors. Conversation repair retains
the original assistant response and native content blocks. Bedrock does not
supply a dollar total here; any token-rate conversion is an explicitly labeled
estimate. Solver accounting follows the reused baseline runner. Sum successful
and unsuccessful construction, review, repair, solver and evaluator calls.

The primary outcome is a **confirmed grounding violation**. Applicability and
execution statuses are descriptive; they do not certify general downstream
correctness. G2/G3 use the campaign evaluator, with manual confirmation of its
failure reports. Previously established ground-truth run labels are held for G4
reliability analysis and do not select campaign cases or supply automated campaign
outcomes. Manual confirmation of a new discovery is reported as manual review,
not as part of automatic generation or grading.
