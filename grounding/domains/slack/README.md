# Slack domain and benchmark annotations

- [model.md](model.md): adopted conceptual ER model.
- [contextualization.md](contextualization.md) and [model_source_ledger.md](model_source_ledger.md): extraction discipline and evidence mapping.
- [coverage/](coverage/): retained routes, identifying attributes, resolution-mode requirements and capability limitations; [catalog.json](coverage/catalog.json) is the operational linear catalog.
- [analysis/](analysis/README.md): baseline obligation tables/cards, task specifications and assertion-coverage measurements. Its editable source is [analysis.json](analysis/analysis.json).
- [writer_capabilities.md](writer_capabilities.md), [root_operations.json](root_operations.json), [compiler_contract.md](compiler_contract.md): domain-specific authoring context used by the active prompts.

These are model/input materials, separate from executed trajectories and reference judgments. The reorganization changes their location, not their annotations or coverage denominator. Historical provenance files retain original source paths; [the path resolver](../../README.md) finds their new locations.

Check existing Slack annotation projections without writing them:

```bash
python -m grounding.domains.slack.analysis.build --check
```
