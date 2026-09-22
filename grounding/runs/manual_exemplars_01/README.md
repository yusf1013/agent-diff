# Manual Slack test suite

This suite contains **57 manually designed tests: 10 original exemplars, 32 resolution variants, and 15 additional ambiguity-location variants**. It is manual research work, not an automated generation result. No solver or paid model has been run on this suite.

- [Original stories](story.md)
- [Variant stories](story2.md)
- [Ambiguity-location stories and index of all 26 underspecified cases](story3.md)
- [Review, counts, and links to every executable test](review.md)
- [Machine-readable manifest](manifest.json)

Each `cases/*.json` is a complete case in the existing grounding runtime format: exact request, acting user, fresh seven-table seed, grounding card with identifying paths, task specification and obligation link, deterministic selector, manually specified expected referents, negatives, ambiguity alternatives, and a private reference outcome. W09/W10 also contain required API probes for the answer fields.

Supply the case file to the [existing runtime adapter](../../integrations/agentdiff/README.md) when running a solver. The adapter gives the solver the request and environment, and gives the evaluator the card, task specification, state and recorded execution. The private selector, reference outcome, story table, and manual judgments are not solver inputs. These tests use our grounding evaluator; they do not substitute native existence/count assertions for it.

## Reproduce the fixtures and checks

Run from the repository root:

```bash
python grounding/runs/manual_exemplars_01/build_suite.py
python grounding/runs/manual_exemplars_01/audit_suite.py grounding/runs/manual_exemplars_01/cases
backend/.venv/bin/python grounding/runs/manual_exemplars_01/check_reads.py
backend/.venv/bin/python grounding/runs/manual_exemplars_01/check_writes.py --database-url postgresql://postgres@127.0.0.1:15432/agentdiff_campaign
```

The last two commands require the local PostgreSQL database. They create and remove isolated schemas, use the real Slack handlers in process, and make no model calls. `check_reads.py` also accepts `--database-url` and `--cases`; selected reruns retain saved results only when their case hashes still match. `check_writes.py --cases W07-single W07-multiple` reruns only those write fixtures and retains the other results.

[checks.json](checks.json) records schema/selector/card validation and independent joins. [read_checks.json](read_checks.json) records native load/access/answer-field checks. [write_checks.json](write_checks.json) records actual native calls and exact net changes for the 16 resolved mutation cases. Read/write evidence contains case hashes; rerun it after changing a case.

`suite_w01_w02.py`, `suite_w03_w06.py`, and `suite_w07_w10.py` contain the original manual designs; `suite_locations_*.py` contain the additions. `suite_support.py` serializes them, and `build_suite.py` emits the variants and executable cases together. `story_locations.py` renders the contrast index. `audit_locations.py` independently traverses the new fixtures to check the target set under each competing interpretation. The original `story.md` remains the reviewed source for the base prompts. No agent architecture or production prompt was changed to construct this suite.
