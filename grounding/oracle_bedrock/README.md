# Direct Bedrock oracle pilot

This adapter evaluates saved runs with a Bedrock conversation. It supplies evidence directly, with no model tools, repository access, or execution of recorded commands. An optional single follow-up repairs mechanical validation failures using the existing conversation history. It does not make the judgments reliable by itself: the September 15 pilot repeatedly found incorrect applicability judgments despite correct reference verdicts. Inspect validation and substantive findings before using results as measurements.

The existing cards, task specification, policy, and canonical schema remain the authorities. There are no test-ID branches, hardcoded expected verdicts, or answer-key checks in this adapter. Applicability follows the supplied instruction version; the adapter does not decide it.

## Components

- `prepare.py` adapts Agent-Diff saved-run/test-entry/annotation formats into an explicit input bundle. It excludes benchmark assertions/scores and solver private thinking/signatures. Saved commands, observations, assistant text, final response, initial seed, and the benchmark's net diff are preserved. No final database snapshot or new diff is reconstructed.
- `adapter.py` renders that bundle. It includes every seed row and diff entry, decodes API JSON strings for display, indexes records and response paragraphs at their original locations, and references exact duplicate command/final-answer text instead of repeating it. Distinct narrative text is retained. The final task/reference index copies resolution states and derives indentation ancestry without evaluating conditions. The accounting index lists all supplied changes and response paragraphs.
- `run.py` makes one `InvokeModel` call with adaptive thinking, explicitly requesting `display: summarized`. It records the request, source/packet hashes, raw response, returned thinking blocks, thinking text, usage, elapsed time, stop reason, and validation. SDK retries are disabled. The optional validation repair appends the original assistant content and a short user message to the original request history; its output is saved separately. Medium effort and 16,000 total output tokens are the defaults; thinking and answer share that cap.
- `validate.py` checks structure, inventories, source locations, direct links, key aggregation constraints, and supplied-effect/response coverage. It never edits verdicts. Semantic attribution, applicability, factual truth, and authorization still require review. Bare syntax markers are checked against the informal spec's supported marker words; novel syntax should be reviewed rather than silently accepted.

There is one canonical assessment schema. The experimental applicability-only diagnostic projects existing fields from it and writes `applicability.json`, not a full assessment. It is not a recommended replacement evaluator: it reproduced the same applicability mistake in the pilot.

## Run a prepared case

Requirements: Python 3.10+, boto3, jsonschema, and configured AWS credentials/model access. Credentials are resolved by boto3 and are not written into requests or results.

```bash
python grounding/oracle_bedrock/run.py \
  --inputs /path/to/prepared-case \
  --instructions /path/to/oracle-check-instructions-lean.md \
  --schema 'docs/for eval/oracle-assessment.schema.json' \
  --instruction-placement after-evidence \
  --effort medium \
  --out /tmp/my-oracle-run
```

Input files are explicitly named: `task.json`, `task_spec.json`, `cards.json`, `initial_state.json`, `recorded_diff.json`, `response.json`, `trajectory.json`, and optional `api_docs/*.json` and `final_state.json`. The model cannot access any other file. The runner does not read assessment files present in the input directory. Each new output directory must not already exist. Keep reports outside directories used as future model inputs.

The packet presents source locations, not a new evidence-ID scheme. Decoded stdout is cited at its original string location, e.g. trajectory `/steps/19/observation/stdout`; invented child pointers inside that original string do not resolve. Response paragraphs use the protocol's blank-line split. Initial/final state and diff records retain source indices and all fields. No semantic relevance filter removes possible counterevidence.

API docs are supplied in full; this first adapter does not select them using semantic guesses. Large evidence still means substantial input-token usage. Direct calls eliminate repeated model-driven retrieval, not the cost of reading the evidence. No prompt cache breakpoints were enabled in this pilot.

## One conversational validation repair

For new full assessments, add `--repair-on-validation-failure` to permit at most one follow-up after a completed answer fails mechanical validation. The repair is written to a sibling directory named `<out>-repair-1`. A passed initial assessment makes no extra call. API errors and token-limit interruptions do not trigger this repair.

To continue an existing failed assessment:

```bash
python grounding/oracle_bedrock/run.py \
  --repair-from /tmp/bedrock-oracle-applicability-procedure/run-2 \
  --out /tmp/my-oracle-repair
```

This uses the saved request, model settings, source snapshots, and unchanged schema. The outgoing `messages` array retains every original message, then appends the complete native assistant response content (including untouched thinking/signatures), followed by this user message and the actual validator errors:

> Thanks. Validation failed with the errors below. Please make only the changes required to fix them, preserving unrelated judgments and evidence. Return the complete corrected JSON object.

The evidence prompt is not rebuilt or summarized, and no desired semantic verdicts are inserted into the follow-up. Passing complete unchanged thinking blocks follows [AWS's multi-turn guidance](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-thinking-encryption.html).

Original reports remain intact. Repair artifacts include `followup.txt`, `repair_errors.json`, the full outgoing `request.json`, returned `response.json`, complete `conversation.json`, thinking summaries, corrected assessment, and fresh validation. Each API invocation has its own summary and usage-ledger entry; the repair links to its parent. A repair that still fails returns nonzero and stops; a repair output cannot itself be repaired by this runner. Mechanical success does not certify semantics or guarantee that the model preserved every unrelated field—compare reports when auditing repairs.

## Prepare a case from Agent-Diff artifacts

```bash
python grounding/oracle_bedrock/prepare.py \
  --run /path/to/saved-run.json \
  --analysis grounding/slack_analysis/analysis.json \
  --tests datasets/agent-diff-bench/all_numbered.jsonl \
  --seed examples/slack/seeds/slack_bench_v2.json \
  --docs examples/slack/testsuites/slack_docs/slack_api_full_docs.json \
  --out /tmp/prepared-case
```

Supply the seed actually referenced by the test. Preparation checks that saved and test prompts agree. A recorded error/timeout/turn-limit run without a final field gets an empty designated final-response inventory, with that fact recorded in task metadata; unexplained missing final output is rejected. This does not manufacture a final answer from the trajectory. Other benchmark formats need an adapter into this same input layout, not changes to the oracle policy.

## Results and limits

`assessment.json` contains the parsed model report; `answer.txt` preserves the raw text. A single surrounding Markdown JSON fence may be stripped deterministically and is recorded as a formatting note. No field values or judgments are repaired. `response.json` is the native API response; `sources/response.json` is the solver's answer being evaluated.

`thinking.txt` and `thinking_blocks.json` contain whatever the provider returns. These are provider-produced thinking summaries, not complete internal reasoning. They can help diagnose a failure but cannot prove its precise cause. `max_tokens` or timeout results are incomplete and must not be counted as completed evaluations.

`summary.json` and the parent directory's `usage_ledger.jsonl` record every attempted invocation, including API rejection and incomplete output. Successful calls record native input/output/thinking token usage. Errors with no returned usage remain unknown; they are not silently billed as zero. Direct Bedrock did not return a dollar amount, so `cost_usd` remains null rather than substituting a locally calculated figure for the previously used CC estimate.

`--native-schema` is an explicit compatibility probe. This account/model endpoint rejected `output_config.format` before generation during the pilot. Normal mode includes the unchanged schema in the prompt and validates locally. The runner does not weaken it to fit a native grammar or silently fall back after a rejection.

Failed API calls, incomplete responses, and validation failures return a nonzero process exit code. Mechanical validation passing is not a correctness certificate. For example, active/performed on an underspecified mutation can be valid JSON and still violate the applicability policy.

Pilot artifacts and a linked review are at `/tmp/bedrock-oracle-pilot/`. They are not model inputs. No prior CC answers, audit notes, or manually written expected verdicts were sent to Bedrock.

## Verification

```bash
python -m unittest discover -s grounding/oracle_bedrock -p 'test_*.py' -v
```

Tests cover complete record preservation, decoded observations with original locators, exact duplicate-text handling, indentation, paragraph/index conventions, invalid links/locators, substantive-line replacement by a marker, and accounting for incidental updates and memberships.

API references: [AWS adaptive thinking](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-adaptive-thinking.html), [AWS structured output](https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html), [Anthropic thinking-display documentation](https://platform.claude.com/docs/en/about-claude/models/extended-thinking-models). Actual endpoint compatibility is recorded by the invocation, not inferred from the documentation.
