# Automated grounding evaluator

The evaluator assesses a completed run using supplied cards and task specifications. It does not generate new obligations or consume manual reference labels.

| File | Purpose |
| --- | --- |
| `prepare.py` | Adapt a saved baseline run, annotations, seed and docs into the evidence bundle |
| `adapter.py` | Build the bounded evidence packet and stable evidence references |
| `run.py` | Record one model assessment and optionally one mechanical repair continuation |
| `validate.py` | Check schema, references, line structure and diff/response accounting |
| `oracle-assessment.schema.json` | Canonical output schema |
| `batch.py` | Fixed cases/variants/repetitions with bounded concurrency |
| `samples/` | Handwritten format examples; not new empirical model results |

Instructions live in [prompts/evaluator](../prompts/evaluator/). The integrated generation run selects [ordered.md](../prompts/evaluator/ordered.md) with instructions after evidence, medium effort and at most one validation-error repair. Repair retains the original request and raw assistant response, including signed blocks. It does not restart with a fresh prompt or prescribe the semantic answer.

To prepare a recorded request without contacting Bedrock:

```bash
python -m grounding.evaluation.run   --inputs grounding/runs/slack_campaign/compiler_pilot_01/execution/W01/solver/oracle_input   --instructions grounding/prompts/evaluator/ordered.md   --schema grounding/evaluation/oracle-assessment.schema.json   --instruction-placement after-evidence --prepare-only --out /tmp/evaluator-input-w01
```

Omitting `--prepare-only` makes a paid API call. Add `--repair-on-validation-failure` only when the bounded repair is intended. Every call records instructions, evidence, request/response, available thinking, usage and validation results. A successful mechanical validation is not a correctness certificate for the model's judgments.

Saved comparisons live in [runs/oracle_evaluation](../runs/oracle_evaluation/). Manual truth lives separately in [reference_labels/slack](../reference_labels/slack/); use it only for the reference comparison stage.
