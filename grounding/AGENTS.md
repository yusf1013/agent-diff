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

## Dates: never change the agent's clock

Changing an agent's clock, or anything else in the agent's own environment, so that a test's hard-coded dates come out right is a severe anti-pattern. The PI discontinued it on 2026-10-03, calling it "the absolute stupidest thing we could have done", and strongly advises against it for every harness, model and test. It hides a stale test instead of fixing it, and it broke in every way it could:

- GPT-6.1 Sol could not run 15 items of the denominator. OpenClaw checks its login's expiry against the shifted clock, and a test clock of October 16 lay past the expiry.
- Only the agent's Node process was shifted. `date`, `ls -l` and HTTP headers showed the real day, so agents saw two different "nows".
- Calendar's tests are dated 2018, which fights the model's own sense of the year: in 40 of Qwen's 657 Calendar trials its reasoning named 2025 or 2026 as the year (dates_01).
- It cannot carry over to the real services, whose servers stamp records with the real time.

Dates belong to the test. Every date in a test (its data, its request, its expected values, what the judge reads) is held relative to the moment the test was written for, and is rendered against the real date when the test's environment is created. The agent always runs on the real clock. The investigation and the fix are in [runs/dates_02](runs/dates_02/README.md): every test behind the denominator tables has a verified template in `runs/dates_02/suite/`, and the runners render it (`for_run` in [common/dates.py](common/dates.py), called by the OpenClaw runtime and the Claude Code backend). The shims' code paths are removed; a test made for a shifted clock (one with a `clock`, or a Calendar test dated 2018) is refused. A new scenario gets the same treatment: template it with `common/dates.py` before it runs.

## Reporting to the PI

These rules apply to everything the PI reads: chat replies, the Status and "For the PI" sections of study READMEs, logs, briefs, the roadmap, and anything the lead session relays from another session. The PI shared the research goal so that every report can say why a step is taken. A report works only if the PI can follow it, and act on it, without opening a file.

### Top-down, in the PI's points

- Organize status by the PI's points: the sections of [the PI's notes](protocols/brain_dump_2026-09-29.md) and every later request. Never by study folder, session or roadmap step number.
- Order by how far an item moves the research. Case-level rulings and housekeeping come last.
- When the PI asks for status, give the whole picture, top-down, in this shape:
  1. The PI's points, each with what is done, what happened, what is left and open decisions.
  2. What was decided on the PI's behalf since the last report, with reasons.
  3. Decisions the PI must make, the most consequential first. Each decision must be listed with background context. When the PI must decide, give the context in plain words, the options, what each option changes (numbers, claims, cost, time), and your recommendation with its reason. Ask the question that actually needs the PI.
  4. What is running, and what is planned to run next.
  5. Observations worth the PI's attention, each with its case. The PI welcomes surprises.

### Cases

- Never give a test ID, fact ID, study name, session name or step label on its own.
- When a case matters, describe it:
  - the request, verbatim;
  - what the data holds: the target, the decoy, and the field where they differ;
  - what the agent did;
  - what depends on it: which facts and tests move, which numbers change.

  Put the ID after the description, as a pointer.
- Elaborate on the case, not the concept. The PI designed the method: do not explain decoys, probes, covers or the credit rule. When asked to elaborate, give the specific evidence, reason and consequence.
- Example (2026-09-30): "AR-BOX-24's run-date dependency" and "'Atlas Onboarding Archive' for 'the Atlas Onboarding hub'" reached the PI with no scenario and nothing on what depended on them. Asked to elaborate on open decisions, a report explained what a decoy is.

### Plain words

- Write full sentences, not one-line summaries packed with labels.
- A label the PI did not coin (study and session names, step numbers such as 6h, arm names such as P1, verdict labels, fact IDs) comes after a plain description, or not at all.
- Write as much as the PI needs to follow without opening a file. Put further detail behind a link.

## The denominator

Every reported number is read against the tests the methodology prescribes from the domain model alone:
[protocols/denominator.md](protocols/denominator.md) (732 cases without several-match: 213 servable facts × a
packed probe, an absence test and an underspecified test, plus 93 faithful capability boundaries; per service and
with what is excluded). Production counts (cases built, runs made) are never denominators; a study that reports
coverage or exposure says how many of the prescribed items its tests fill, with `runs/denominator_01`'s kit. The three summary tables are [denominator_tables.md](denominator_tables.md). Only OpenClaw runs count as runs of an agent under test; bare-loop (toy harness) runs are intermediate results and are never reported as such.

## Writing custom tests
Use the existing custom Slack workflow in grounding/integrations/agentdiff/runtime.py, following grounding/AGENTS.md. Use grounding/runs/slack_campaign/compiler_pilot_01/W01/case.json and its execution review as examples. Author the seed, prompt, cards, and task specification before execution. Run the solver without native assertions, then manually review its trajectory, output, and diff. Keep the evidence bundle ready for our custom evaluator. Save everything in a new persistent directory under grounding/runs/, and preserve all test files and execution evidence during cleanup. Keep the new folder directory simple and protect it from bloat. 