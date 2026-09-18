# Current generation workflow

Run commands from the repository root using a Python environment with the dependencies for that stage. The authoring/evaluator calls need `boto3` and `jsonschema`; the integrated run additionally needs AgentDiff's backend/SDK dependencies, `bedrock_llm`, the local backend/database, and Docker. This repository's available environments are `../bedrock-llm/.venv/bin/python` for model calls and `backend/.venv/bin/python` for the in-process native check. No command below needs a paid call unless explicitly marked.

| Stage | Entry point | Inputs | Output and boundary |
| --- | --- | --- | --- |
| Writer | `grounding.generation.concept_writer` | Fixed route/mode assignment, domain model, capability and operation brief; no seed | Short Markdown request, selection conditions, and match/decoy table |
| Self-reflection | `grounding.generation.concept_reflect` | Saved writer conversation plus a common follow-up | One native continuation, preserving original turns |
| Compiler | `grounding.generation.concept_compile` | Reflected sketch, selected mode instructions, schema/API definitions | Fresh seed, faithful selector, row bindings; computed cards and task specification |
| Mechanical checks | `selection.py`, `validate.py`, `check_compilation` | Compiler output and locked source | Schema, references, route, recomputed match sets, and row consistency; no semantic interpretation of prose |
| Construction reviewer | Invoked by compiler | Sketch, compiled case, mechanical results | Semantic faithfulness/validity/quality assessment; it is an LLM review, not ground truth |
| Native preflight | `grounding.integrations.agentdiff.runtime` | Accepted compiled case | Actual seed loading and deterministic API visibility checks; no automatic LLM access fallback in this workflow |
| Solver then evaluator | `grounding.generation.concept_batch` | Accepted case and native preflight; then recorded execution evidence | Solver trajectory/state, then automated grounding assessment |

The compiler and construction reviewer retain their 24,000-token output limits. Writer/reflection calls retain 6,000. These are existing settings, not tuning changes introduced by the reorganization. Requests record the effective model, limits, cache settings, and effort. The current pipeline still uses the fixed W01–W10 pilot assignment; reorganization does not make it a general coverage scheduler.

Prepare writer inputs without invoking a model:

```bash
python -m grounding.generation.concept_writer --folder /tmp/writer-next
```

Use a new folder for an actual experiment; add `--run` to make paid writer calls. Writer and reflection cache checks still warm the common prefix with the first two substantive cases. Reflection uses:

```bash
python -m grounding.generation.concept_reflect --folder /path/to/writer-run --run
```

Inspect compiler inputs without invoking a model:

```bash
python -m grounding.generation.concept_compile   --source grounding/runs/slack_campaign/writer_pilot_04   --case W01 --out /tmp/compiler-inputs-w01
```

Add `--run` for compilation and construction review. Standalone `--out` denotes a generation directory. A successful final case is `case.json`; source conflicts, truncation and unresolved reviews retain their records without being counted as accepted cases. Up to three compiler turns are allowed, with repair messages appended to the original conversation and the selector locked once syntactically valid.

For a new case-based batch, the following **only prepares its plan**:

```bash
python -m grounding.generation.concept_batch   --source grounding/runs/slack_campaign/writer_pilot_04   --folder /tmp/next-compiled-batch --cases W01 W02
```

Use a different new folder and `--run` to perform paid compilation/review, native preflight, solver and evaluation. Configure `--database-url` and `--base-url` for the running local AgentDiff service. Results use the [stage layout](../runs/README.md). The first case warms compiler cache before the remaining cases start. Repairs of the evaluator are mechanical conversation continuations, not feedback about the desired verdict.

`concept_continue.py` is an explicit development-intervention tool for a diagnosed saved compiler attempt. It preserves the previous result, records the supplied feedback, and can read the old or new layout. It is not an automatic semantic retry policy.

Cost/token accounting can be recomputed from records, without API calls:

```bash
python -m grounding.common.usage /path/to/run
```

It includes failed and repair calls and both old/new solver layouts. Dollar totals remain our historical-rate estimates; missing usage is reported rather than counted as free. Do not run accounting in a historical folder merely to inspect it if you want all original ledger bytes preserved; use its saved ledger or copy the folder first.
