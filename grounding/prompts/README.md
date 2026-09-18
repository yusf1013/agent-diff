# Agent instructions

[Current configuration](../configs/current.json) selects the active prompt directories. Python selects known mode fragments before sending requests; agents are not asked to choose among all four resolution-mode instruction sets.

| Agent | Shared instructions | Case-specific/continuation instructions |
| --- | --- | --- |
| Writer | [writer/writer.md](writer/writer.md), [Slack capability brief](../domains/slack/writer_capabilities.md), [domain model](../domains/slack/model.md) | [assignment template](writer/assignment.md), exactly one [mode fragment](writer/modes/), relevant [operation menu](../domains/slack/root_operations.json), optional [count hint](writer/member_count_hint.md) |
| Writer reflection | Original writer conversation/system | [self_reflection.md](writer/self_reflection.md) |
| Compiler | [compiler/instructions.md](compiler/instructions.md), [domain contract](../domains/slack/compiler_contract.md), [selector syntax](compiler/selector_syntax.md), mechanically projected real schema/API definitions | Exactly one [mode fragment](compiler/modes/), saved sketch packet, compiler `*_repair.md` files |
| Construction reviewer | [construction_reviewer/instructions.md](construction_reviewer/instructions.md), the same domain/schema/API/selector context | Exactly one compiler mode fragment and the proposed compilation/checks |
| Evaluator | [ordered.md](evaluator/ordered.md) and [schema](../evaluation/oracle-assessment.schema.json) | Evidence bundle and at most one [repair](evaluator/repair.md) appended to recorded history |

The evaluator's full/lean/separated variants remain available for explicit comparisons; `ordered.md` is selected by the integrated pipeline. Older generation prompts live in [archive/slack_campaign/prompts](../archive/slack_campaign/prompts/). [Generation history](GENERATION_HISTORY.md) records how the current versions developed.

To inspect exactly what an agent received, open the run's `instructions.md` and each `request.json` (plus `followup.txt` where recorded). The writer's prepared `input.md` and compiler dry-run `compiler_input.md` offer a readable view before making paid calls. Raw requests include the exact history and runtime settings. No manual verdicts or ground truth enter the evaluator bundle.

The solver prompt has different ownership: our [solver runner](../solver/slack/run.py) extracts it from AgentDiff's original notebook and appends its API documentation. It is saved as `solver/system_prompt.txt` for generated-case runs.
