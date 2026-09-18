# Oracle evaluator experiments

The reusable adapter, Bedrock runner, validator, bounded conversational repair, and batch launcher are in [grounding/oracle_bedrock](../../evaluation/README.md). The [lean](../../prompts/evaluator/lean.md), [ordered](../../prompts/evaluator/ordered.md), and [separated](../../prompts/evaluator/separated.md) prompts are exact preserved snapshots. No variant has been promoted on reliability grounds.

Browse the [100-evaluation comparison](ten_case_comparison/review.md) and [earlier workflow comparison](workflow_variants/review.md). Their input bundles, reports, returned thinking summaries, validation results, and usage ledgers are checked in. Historical absolute paths in recorded metadata are provenance, not prerequisites for reading reports. Historical launch scripts are preserved for audit; use the portable batch launcher for new experiments.

The [archive manifest](archive-manifest.json) maps every original temporary file to a SHA-256 digest and an archive. The Git LFS archives retain complete original directories, including native responses, signed conversation histories, prompt-generation scripts, the programmatic Claude Code pilot, and earlier failed attempts. Byte content has not been rewritten. Python cache files are excluded. Archives also retain logs omitted from the browsable projection. To inspect one, run `tar -xzf archive/<name>.tar.gz -C /a/new/directory` from this folder after fetching Git LFS objects. Extract into a new directory; do not overwrite current work.

Do not supply this folder, ground-truth reports, or earlier evaluator outputs to an evaluator as evidence. Use only prepared case inputs. Signed historical Bedrock histories must not be edited; they describe earlier invocations and policy versions.

For a fresh comparison (cost-incurring unless `--prepare-only` is included):

```bash
python grounding/oracle_bedrock/batch.py \
  --inputs experiments/oracle_evaluation/ten_case_comparison/inputs \
  --cases slack_62 slack_67 \
  --variants ordered separated --repeats 5 --concurrency 15 \
  --out /path/to/new-results
```

The launcher has no reference judgments and never sends ground truth to the model. It refuses an existing output directory. Usage remains native provider token usage; dollar cost is null when the provider does not supply it. The older Claude Code pilot separately preserves CC's own dollar estimates.
