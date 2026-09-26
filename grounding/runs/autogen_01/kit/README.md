# Kit: automated fact-discrimination tests with Claude Code Sonnet agents

This kit generates grounding tests from a domain model and judges an agent's trials. Claude Code agents do the
judgment work, and code does everything that can be checked or derived.

| Step | Who | What |
|---|---|---|
| Brief | code, from your briefs file | a scenario id, a domain, and 2-4 catalog facts to test |
| Write | **writer agent** (Sonnet; Read, Write, Edit, Glob, Grep; no Bash) | `scenario.json`: request, seed, target, conditions, reference query, decoys with mutations, write call |
| Check | code ([scenario.py](scenario.py)) | format, seed expansion, `fdc.check_reference` (every decoy fails exactly its fact), anchors survive, no dangling keys, replica rules, request lint |
| Pre-check | code ([preflight.py](preflight.py)) | install on the replica, read every record, **observability** (each decoy's deciding value is visible), **write feasibility** (the action works on the target) |
| Read | **reader agent** (Sonnet, no tools, fresh session) | the request alone, then the records: which records match, which condition each decoy fails, genuine ambiguity, naturalness |
| Repair | the same writer session, resumed | every finding goes back to the writer; up to 6 check rounds and 2 reader rounds |
| Suite | code ([derive.py](derive.py)) | cover, one probe per decoy, one fact probe per fact with several decoys |
| Run | code (fact_coverage_02's runner) | the agent under test, 3 trials per test |
| Judge | **judge agent** (Sonnet, no tools) | one verdict per trial that is not mechanically clean: outcome, exposed facts, mechanism |
| Score | code ([score_run.py](score_run.py)) | distinct facts exposed (detect@1, detect@3), by form, family and domain |

Agents never certify their own work: the orchestrator runs every check itself, and repairs continue the same
conversation. Every call's prompt, result, transcript and token usage is saved next to the run.

## What you provide for a new domain
In `inputs/<domain>/`:
- `facts.json`: the fact catalog, with designated substitutes and suggested families per fact (`make_facts.py`
  derives it from a catalog);
- `replica.md`: how the service your agent talks to behaves: reads, writes, values it rejects, known gaps;
- `seed_ops.md`, and a builder class in [seedops.py](seedops.py): the operations a writer uses to build records;
- `api.md`: the API documentation your agent under test receives;
- the domain model (`model.md`).

Plus a replica or sandbox that can install a seed, answer reads and writes, and export its state for diffs.
AgentDiff provides this for Box, Calendar, Linear and Slack.

## Run
From the repository root, with the backend running and the Purdue key in `grounding/.env`:

```bash
L="python grounding/runs/fact_coverage_02/launch.py"
$L grounding.runs.autogen_01.kit.selftest                                   # offline checks of the kit
$L grounding.runs.autogen_01.kit.orchestrate --briefs BRIEFS.json --run RUN  # generate (Claude Code agents)
$L grounding.runs.autogen_01.kit.solve --gen-run RUN --out SOLVE_RUN         # run, retry, judge, score
```

Agents run with `claude -p --model sonnet --restricted --strict-mcp-config`, from workspaces under `/tmp` outside
any repository. So they read no project instructions or memory, and no files but the ones copied for them.

## Files
- [prompts/](prompts/): the role prompts (writer, reader, judge);
- [docs/](docs/): the writer's method notes and the scenario format;
- [examples/](examples/): the two worked examples every writer sees;
- [agent.py](agent.py): runs one agent turn and saves its evidence;
- [orchestrate.py](orchestrate.py), [reader.py](reader.py): generation;
- [judge.py](judge.py), [bundle.py](bundle.py): judging;
- [selftest.py](selftest.py), [preflight_selftest.py](preflight_selftest.py): tests of the kit itself.
