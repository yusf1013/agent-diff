# Grounding research guidance

This directory contains our grounding research: benchmark coverage (G1), mutation (G2), generation (G3), and evaluator accuracy against manual reference labels (G4). AgentDiff supplies the environment and benchmark runtime. This guidance supplements the repository's root `AGENTS.md` for work under `grounding/`.

## Read only what the task needs

Start with [README.md](README.md) for the component map, then the relevant guide. Do not recursively read all protocols, experiment records, or archives.

- **The research goal, planning, or next steps:** read [the PI's notes of 2026-09-29](protocols/brain_dump_2026-09-29.md), then the [roadmap](protocols/roadmap.md).
- **Cards, task specifications, or coverage annotations:** read [card extraction](protocols/card_extraction.md).
- **Manual reference labeling:** also read [ground-truth evaluation](protocols/ground_truth_evaluation.md).
- **Generation changes:** read [generation/README.md](generation/README.md) and the affected agent prompts.
- **Evaluator changes:** read [evaluation/README.md](evaluation/README.md), its selected instructions, and assessment schema.
- **Experiments:** read [runs/README.md](runs/README.md) and the component guide's execution and accounting instructions.
- **Study design:** consult [evaluation plan](protocols/evaluation_plan.md).

[configs/current.json](configs/current.json) identifies active prompt sources; [prompts/README.md](prompts/README.md) maps them to agents. Saved requests establish what a particular run actually received. `archive/` contains superseded workflows, not default entry points.

Raw run evidence (episode folders under each study in `runs/`) is tracked but hidden from default ripgrep searches by each study's `.ignore`. To find an episode, start from the study's README, labels or run index, then open or search that folder by name (`rg PATTERN <folder>`; add `--no-ignore` if nothing comes back). `find` and `ls -R` do not honor `.ignore`.

## Ownership and responsibilities

Our harness, prompts, domain annotations, reference labels, and experiment evidence live here. AgentDiff core lives in the repository's `backend/`, `sdk/`, `examples/`, `datasets/`, and `ops/`. Prefer our [integration adapters](integrations/agentdiff/README.md) for harness-specific integration changes; change upstream code when the task requires it.

The writer designs the conceptual scenario. The compiler faithfully instantiates it; it must not silently change its meaning or selection condition to make validation pass. Deterministic checks verify executable properties, not arbitrary prose semantics. The construction reviewer assesses semantic faithfulness, validity, and quality. The solver executes the task; the evaluator assesses recorded execution. Respect these boundaries when diagnosing failures.

## Agent development and experimental integrity

- Write explicit, generalizable procedures. Select instructions for known conditions, such as the assigned resolution mode, in code before sending the prompt. Leave genuinely discoverable decisions to the agent.
- Repairs and reflection continue the recorded conversation, preserving prior responses; do not replace them with a fresh prompt. Record development interventions separately.
- Codex-authored cases and judgments are manual work. Claims of automation require recorded runs of the designated experimental agents. Preserve provenance for manual changes.
- Reference labels support G4 comparison; keep them and manual verdicts out of evaluator input bundles. Do not use them to steer a verdict during repair.
- Distinguish test validity, test difficulty, solver failures, and evaluator errors. Passing a mechanical check alone does not establish semantic validity. Report uncertainties and denominators explicitly.

## Evidence, cost, and verification

Use new run directories and preserve failed attempts. Save assembled instructions, requests, responses, available provider thinking, effective settings, and usage for every invocation, including retries. Use prompt caching where supported and verify recorded cache usage. Include input, output, and cache tokens in accounting; identify estimated versus provider-reported cost and missing usage.

Historical transcripts and outcomes remain evidence. Record repairs or revised judgments separately. Resolve old paths with `python -m grounding.paths OLD_PATH` from the repository root.

Follow the affected component's testing instructions. Check prepared requests and offline behavior before paid experiments where practical; run experiments within the user's authorized scope. Link findings to source artifacts. Keep commits scoped to the work and preserve unrelated changes. Update the relevant guide when entry points or responsibilities change.

## Writing custom tests
Use the existing custom Slack workflow in grounding/integrations/agentdiff/runtime.py, following grounding/AGENTS.md. Use grounding/runs/slack_campaign/compiler_pilot_01/W01/case.json and its execution review as examples. Author the seed, prompt, cards, and task specification before execution. Run the solver without native assertions, then manually review its trajectory, output, and diff. Keep the evidence bundle ready for our custom evaluator. Save everything in a new persistent directory under grounding/runs/, and preserve all test files and execution evidence during cleanup. Keep the new folder directory simple and protect it from bloat. 