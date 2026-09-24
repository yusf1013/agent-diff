# Our AgentDiff integration

These adapters belong to the grounding project. AgentDiff itself remains in `backend/`, `sdk/`, and `examples/`.

`smoke_runtime.py` supplies the native-case Box/Calendar/Linear Qwen lifecycle. Its fixed-seed scope, setup commands, evidence, and limitations are documented in the [solver handoff](../../solver/README.md). It shares the Purdue client and request limiter with Slack.

`custom_runtime.py` extends the smoke lifecycle to a case's own Box/Calendar/Linear seed: it installs the seed with
the backend seed script's functions, records read probes and the installed state, and runs the unchanged episode loop
(used by `grounding/runs/fact_coverage_01`). It creates and removes only its own UUID-named templates.

`runtime.py` installs an isolated generated seed, exports its actual state, exercises documented reads, checks selector-relevant visibility, runs our solver through AgentDiff, captures the final snapshot and native diff, assembles evaluator inputs, and cleans up the isolated template/environment. Its `prepare`, `run`, and `cleanup` CLI subcommands expose those operations.

`native_compile_check.py` is a smaller in-process load/read smoke check against the real PostgreSQL schema and Slack handlers. It uses no LLM, HTTP server, or sandbox. It does not certify requested writes or platform authentication. Its summary separates successful loading/reads from selector visibility certification; the integrated batch requires certified visibility before running the solver.

```bash
backend/.venv/bin/python -m grounding.integrations.agentdiff.native_compile_check   grounding/runs/slack_campaign/compiler_pilot_01/W01/case.json   --out /tmp/native-check-w01   --database-url postgresql://postgres@127.0.0.1:15432/agentdiff_campaign
```

Use a new output directory. The compiler's deterministic selection checks belong to [generation](../../generation/); native environment loading and API observations belong here. The current batch does not fall back to an LLM when visibility cannot be certified. Preserve and inspect that result rather than interpreting it as a solver failure.
