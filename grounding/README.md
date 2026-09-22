# Grounding research workspace

This directory owns our test generation, evaluation, domain annotations, and experiment records. AgentDiff supplies the environment and benchmark runtime in the repository's `backend/`, `sdk/`, `examples/`, `datasets/`, and `ops/`. Those platform directories were not moved or modified in this reorganization.

| Component | Location | Responsibility |
| --- | --- | --- |
| Generation | [generation/](generation/README.md) | Conceptual writer, reflection, faithful compiler, construction review, selector and case checks |
| Agent instructions | [prompts/](prompts/README.md) | Current prompt text and mode-specific fragments, including repair messages |
| Current prompt selection | [configs/current.json](configs/current.json) | Explicit paths used by the current harness |
| AgentDiff integration | [integrations/agentdiff/](integrations/agentdiff/README.md) | Our seed installation, native preflight, snapshots, diff capture, cleanup, and evaluator input assembly |
| Solver | [solver/slack/](solver/slack/README.md) | Our Bedrock runner and sandbox bridge using the benchmark's solver prompt |
| Automated evaluator | [evaluation/](evaluation/README.md) | Evidence adapter, recorded model calls, assessment schema, mechanical validation, and one repair turn |
| Domain materials | [domains/slack/](domains/slack/README.md) | Adopted model, capabilities, coverage catalog, cards, task specifications, and benchmark-coverage measurements |
| Cross-domain modeling | [domain comparison](domains/route_comparison.md), [modeling tools](modeling/README.md) | Box, Calendar and Linear conceptual models, source ledgers, API-read qualifications and exact structural route counts |
| Reference judgments | [reference_labels/slack/](reference_labels/slack/README.md) | Manual ground truth and adjudication; never supplied to evaluator calls |
| Reusable protocols | [protocols/](protocols/README.md) | Card extraction, ground-truth labeling, domain modeling, and evaluation plan |
| Experiment evidence | [runs/](runs/README.md) | Saved inputs, outputs, thinking supplied by the provider, usage, state records, and human reviews |
| Superseded workflows | [archive/](archive/README.md) | Previous campaign code and prompt versions; not the current entry points |
| Shared support | [common/](common/) | Recorded Bedrock conversation, JSON helpers, layout and usage accounting |
| Offline tests | [tests/](tests/) | Prompt dispatch, continuation integrity, selectors, validators, integration contracts, and layout checks |

Start with the [generation guide](generation/README.md) when iterating the writer/compiler. The construction reviewer and deterministic native preflight remain part of the current pipeline; reorganizing the files does not change their acceptance rules or settle whether a stage should later be removed.

Every invocation saves the assembled instructions and request, raw response, available provider thinking, and usage. Prompt source files explain what should be sent; the saved request is the record of what was actually sent. Failed attempts are retained.

Historical runs keep their internal directory structure. Relative links in human review documents have been repaired. Recorded JSON and model transcripts retain historical paths and bytes. To locate an old repository path:

```bash
python -m grounding.paths 'experiments/slack_campaign/compiler_pilot_01/W01/case.json'
```

See [relocation.json](relocation.json) for the complete prefix/file mapping and [the migration checks](REORGANIZATION.md). Pre-existing untracked work from other domains and the native failure audit were left in their original locations; this does not silently adopt them into the current harness.
