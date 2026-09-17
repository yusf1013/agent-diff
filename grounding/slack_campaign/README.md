# Slack G1–G4 campaign

Recorded development results: [campaign report](../../experiments/slack_campaign/campaign_02/report.md).
The run has ended, but the requested evaluation is not complete: G2 mutation
remains a six-source pilot, and G3 authoring and quality checks are being revisited
with the user. Preserve all attempts, costs and original denominators. The
recorded cases and quality labels are evidence for that review, not an approved
generation method to scale again.

The next step is discussion and calibration of a conceptual writer that returns
a natural-language request and an environment table. Its replacement instructions
and input contract have not yet been finalized. Keep future experiments separate
from `campaign_02`; do not resume the paid commands below as part of housekeeping.

The [methods document](../../experiments/slack_campaign/campaign_02/methods.md)
records manual versus automated work, coverage accounting, repair passes and
provenance limits. The superseded one-author pilot is documented separately in
[HISTORICAL_PILOT.md](HISTORICAL_PILOT.md); its constraints are not the current policy.

## Recorded campaign_02 workflow

1. Code assigns a retained complete route and resolution mode. The writer receives
   the existing Slack seed, real model/schema and API context.
2. Sonnet writes a short natural prompt, role table, same-record bindings,
   grounding metadata and directly linked task lines. An independent reviewer
   checks the design.
3. A separate Sonnet compiler adds seed records and produces finite relational
   selectors/native bindings. Code assembles cards mechanically. Environment-only
   mutations reuse the existing source cards/spec rather than re-extracting them.
4. Mechanical checks and independent semantic review check the actual whole seed.
   A selector proves a seed property; it does not prove the prompt means that query.
5. A disposable environment provides real API observations. Conservative traversal
   plus a separate Sonnet access review establish accessible matches and negatives.
6. The unchanged existing solver runs on an isolated clone. The existing structured
   evaluator receives cards/spec, trajectory, response, installed state and net diff.
7. Saved data supplies tables; manual audits confirm new failures and coverage.
   Baseline ground-truth run labels enter only G4.

Conditions and negatives come from the identifying path; there is no artificial
three-condition limit or single privileged focal predicate. Preserve natural
short requests, ordinary plural wording, clearly excluded realistic negatives,
open-ended discovery and consequential operations or useful read answers. Do not
create new easy controls. Repairs continue native conversations with earlier
assistant/thinking blocks intact. Historical outputs and costs are never replaced.

## Main files

| File | Purpose |
|---|---|
| [workflow.py](workflow.py) | Fixed route/mode plan; writer, compiler, reviewer; source-preserving mutation assembly |
| [prompts/v2/](prompts/v2/) | Recorded development instructions; redesign pending |
| [route_contract.py](route_contract.py) | Mechanical route variables and real foreign-key relationships |
| [selection.py](selection.py), [validate.py](validate.py) | Finite seed query, field/key/card/link checks |
| [bedrock.py](bedrock.py) | Native recorded conversation and token usage |
| [runtime.py](runtime.py), [verify_access.py](verify_access.py) | Isolated environment, API probes, access gate and baseline solver reuse |
| [execute.py](execute.py) | Qualified solver run and existing evaluator with one mechanical repair |
| [campaign_metrics.py](campaign_metrics.py), [coverage_results.py](coverage_results.py) | Version-matched manual audit and linear coverage projections |
| [negative_audit.py](negative_audit.py) | One-filter near-miss diagnostic, not a semantic proof |
| [score_baseline.py](score_baseline.py) | G1/G4 saved-data comparison |
| [manual_baseline_review.py](manual_baseline_review.py) | Explicit manual G2 discovery/direct-judge matching records |
| [usage.py](usage.py), [build_report.py](build_report.py) | All-attempt native token accounting and report tables |

The small recovery entrypoints record distinct diagnosed development interventions.
They are not an unlimited retry policy. `revise_routes.py` now requires a separate
construction-only feedback field; mixed prose containing solver judgments must not
be forwarded to an author. One earlier violation is explicitly recorded in the
[provenance exception](../../experiments/slack_campaign/campaign_02/provenance_exceptions.json).

## Rebuild tables without model calls

From the repository root, use the configured Python environment (this campaign
used `../bedrock-llm/.venv/bin/python` with the repository backend and solver
requirements installed):

```sh
python -m grounding.slack_campaign.build_report
python -m grounding.slack_campaign.score_baseline
python -m grounding.slack_campaign.manual_baseline_review
```

Only use `build_report --final` after all assigned workers and audits are complete.
The current report/recovery scripts target `experiments/slack_campaign/campaign_02`;
they are research orchestration, not a portable multi-domain scheduler. Exact
requests/settings are saved beside every invocation; the latest prompt files do
not retroactively describe earlier calls.

## Paid execution

Construction and execution require configured AWS credentials for Sonnet 5 in
`us-west-1`. Execution additionally requires the repository backend and PostgreSQL,
with the backend serving the same database supplied to the runtime. The campaign
used backend `http://127.0.0.1:18000` and its owned local database on port 15432.
No production service data is used. Keep at most 15 simultaneous paid calls
across all processes.

```sh
python -m grounding.slack_campaign.workflow plan --all
python -m grounding.slack_campaign.workflow construct --ids G-R083 --concurrency 1
python -m grounding.slack_campaign.execute --ids G-R083 --concurrency 1
```

Existing accepted artifacts/runs are guarded. Inspect and preserve failed attempts
before deliberately resuming; these commands are not instructions to rerun the
recorded experiment. The runtime drops only its own UUID-named templates and
clones after checking ownership.

## Validation

```sh
python -m unittest grounding.slack_campaign.test_workflow grounding.slack_campaign.test_validation grounding.slack_campaign.test_generate grounding.slack_campaign.test_verify_access
```

`test_runtime` additionally uses `CAMPAIGN_TEST_DATABASE_URL` for actual local API
integration checks. Mechanical validation cannot certify natural-language
boundaries, complete API observability, or a reviewer’s semantic judgment.

Bedrock provides native input/output/cache token usage here, not billed dollars.
The report labels its historical-rate cost conversion as our estimate and lists
calls whose usage was not returned. Solver caching is recorded; authoring calls
in this campaign did not use prompt caching. Both repeated context and repair
costs remain in the ledger.
