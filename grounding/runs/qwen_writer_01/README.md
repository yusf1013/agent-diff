# qwen_writer_01: the frozen pipeline with the self-hosted Qwen as the writer

Session "harness", an investigation the PI asked for, assigned by the lead ("RoadMap specialist") on 2026-09-30.

## Status

- **2026-09-30, 02:30 EDT.** The question, the design and the draw are fixed ([plan.json](plan.json)); the writer
  backend passed its probe. Generation of the 12 briefs started (`runs/gen_01`).

## The question

**Does the frozen pipeline produce tests of the same validity and coverage when the writer is the self-hosted
Qwen3.8-27B instead of Muse Spark 1.3?** How close can an open, self-hostable model come as the pipeline's writer,
on the same briefs, the same prompts and the same checks?

What answers it, on 12 Phase 4 briefs that Muse already turned into accepted scenarios:
1. **Generation:** acceptance, check failures (mechanical, replica, reader), writer rounds, near-miss families, the
   facts covered validly (after my review under the PI's rulings), and the wording quality, against Muse's
   scenarios on the same briefs.
2. **Exposure:** the valid tests run on OpenClaw with the self-hosted Qwen at 3 trials and judged by judge v2 on
   Muse, against the exposure of Muse's tests on the same briefs (openclaw_eval_01: `full_03` for Calendar, Linear and
   Slack with opaque ids, `full_02` for Box).

## Design

- **The draw** ([plan.json](plan.json), fixed before any generation or reading): the pool is the 29 Phase 4 briefs
  Muse's generation accepted (7 Box, 7 Calendar, 7 Linear, 8 Slack; the rulings leave none out at the scenario
  level); seed 20260930, three per service: Box 03, 05, 08; Calendar 03, 05, 06; Linear 05, 07, 08; Slack 01, 05, 08.
- **What stays the same:** the frozen generation pipeline as Phase 4 ran it (`autogen_02/kit/generate.py`: autogen_01's
  orchestrator with autogen_02's replica notes): the writer's prompt (`prompts/writer.md`), its first message and
  feedback texts, its workspace (method, format, the two examples, the domain files, `brief.json`), the mechanical
  checks, the replica pre-checks, the round limits (6 check rounds, 2 reader rounds) and the derivation of the suite.
- **The cold reader stays on Muse** (cap $3 billed), so the comparison isolates the writer.
- **The writer:** Qwen3.8-27B, self-hosted (vLLM 0.30, `http://127.0.0.1:18000`), through its Anthropic Messages
  endpoint, in **Claude Code** (the kit's original writer harness, `autogen_01/kit/agent.py`'s Claude path:
  `claude -p` in restricted mode, file tools only, no MCP, resumed for every repair round). The backend is
  [backend.py](backend.py): the writer role goes to Qwen, every other role to Muse unchanged.
- **Known confound, stated before the first run:** Muse's writers ran in Muse Code, Meta's harness; this writer runs
  in Claude Code. The writer's texts are identical; the harness around them (system prompt, tool definitions,
  compaction, Muse's verify-reminder) is not. Muse Code cannot serve another model: it has no custom-provider mode,
  and its catalog and chat protocols are Meta's own (probed on 2026-09-30: it fetches `/muse-code/models` first and
  rejects other shapes). So a difference between the halves measures the model and the harness together, as
  judge_qwen_01 reported for the judge.
- **Settings:** Qwen's reasoning at the served default, `xhigh` (`--effort xhigh`: Claude Code's own default,
  "high", is refused by the server, which accepts xhigh, medium or low; judge_qwen_01's judge ran at the served
  default too; Muse's writers ran at Muse's "high"); Claude Code's compaction at the served window
  (`--autocompact 131k`); the writer reaches the endpoint directly, outside the shared limiter, so at most 4 briefs
  run at once; cost 0 (self-hosted), Claude Code's own estimate kept only as `claude_code_estimate_usd`.
- **A second harness difference** comes with Claude Code: the kit's Claude path puts the writer prompt
  (`prompts/writer.md`) in the system prompt (`--append-system-prompt-file`), while the Muse path prepends it to the
  first message. The text is the same.
- **Opaque ids:** the frozen pipeline gives new Calendar, Linear and Slack scenarios opaque ids
  (`autogen_01/kit/opaque_ids.py`) before they run; Qwen's accepted suites get the same step, so both halves run on
  the same footing. Box ids are numbers and stay.
- **Rulings:** Muse's scenario-specific rulings (known defects, near-miss rulings, clocks) belong to Muse's
  scenarios and are not applied to Qwen's, which share only the brief ids. Qwen's scenarios get my review under the
  PI's criteria, and a clock by the rule of 2026-09-28 where a request depends on the date.

## Log

### Cycle 0 (2026-09-30, 02:15-02:40): orientation and the draw

- Read the frozen generation path (`autogen_02/kit/generate.py`, `autogen_01/kit/orchestrate.py`, `agent.py`) and
  judge_qwen_01's backend (a tool-free drop-in; the writer needs tools and resumable sessions).
- Muse Code with the self-host: it requests `GET /muse-code/models` before any model call and rejected both catalog
  shapes tried; its chat protocol is Meta's. Dropped in favour of Claude Code, the kit's original writer harness,
  which harness_scout_01 showed running Qwen through the Anthropic Messages endpoint.
- The draw (above), before reading any drawn scenario.

### Cycle 1 (2026-09-30, 02:15-02:30): the writer backend and its probe

- [backend.py](backend.py): the writer through the kit's own Claude command (`agent._command`), on the self-host;
  every other role to the kit's Muse path, refused past $3 billed for the readers. Each writer call's init event is
  checked (the tools asked for, no MCP server, the model) and a failed check fails the brief.
- Probe 1 failed on its first request: `API Error: 400 Unexpected reasoning effort high. Supported types are xhigh
  (default), medium, and low.` Without `--effort`, Claude Code 2.1.285 sends "high". Set to `xhigh`, the served
  default. (Probe 1's folder was removed before this note; the error is quoted from it.)
- Probe 2 (`runs/probe_02`): two turns, the second resuming the first. The init event lists Edit, Glob, Grep, Read
  and Write, no MCP server, model `qwen3.8-27b`; it read `note.txt`, wrote `out.txt` and edited it in the resumed
  session; only `qwen3.8-27b` in the usage; Qwen's reasoning comes back as thinking blocks; no key and no account
  email in the evidence. The opening context is about 10k tokens (Claude Code's system prompt and tool definitions).
