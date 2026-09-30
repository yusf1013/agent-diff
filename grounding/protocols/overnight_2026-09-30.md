# The overnight session of 2026-09-29/30: the lead's log

*Kept by the lead session ("RoadMap specialist") while the PI was away. Newest entries at the bottom of each
section. Decisions that stand go to the [roadmap](roadmap.md); this is the record of what happened.*

## For the PI in the morning

1. **The Sonnet round cannot run on the plan in OpenClaw's own loop** (the `harness` session's survey, sections 1–3
   of `grounding/runs/harness_scout_01/report.md`): Anthropic allows plan usage only inside Claude Code's binary;
   third-party loops with Claude logins are prohibited or billed per token. OpenClaw's "claude-cli" backend is
   Claude Code's loop with OpenClaw's prompt appended. The choice: OpenClaw's own loop with an API key (about $263
   for the full suite at list price, about half for the Muse-written half), or Claude Code's loop on the plan. The
   Sol round is within terms: OpenAI's "Sign in with ChatGPT" (DevDay, 2026-09-29) names OpenClaw.
2. **This machine's Claude login reports a Pro plan, not Max.** If you upgraded, log in again; it decides a Sonnet
   round's quota.
3. **16 G4-LIN-08 tests and units** are clocked to 2026-10-16, after the OpenAI login's expiry, and cannot run on
   the plan as they are (shift the scenario's dates, or an API key).
4. **Two of the three F0 lures are flawed under your 09-28 rulings** (a cycle named "Cycle 4"; Slack's blocks), so
   those facts keep plain near misses; the blind review's later "Cycle 4 needs the number" adjudication conflicts
   with the first ruling.
5. **A framing proposal** for your point 5: [framing_proposal.md](framing_proposal.md).

## What ran

- 23:37 the Sol pilot (32 tests, 1 trial): 31 completed, median 37 s, about 45k input tokens per run.
- 23:54 five sessions launched on briefs: judge_qwen, regen, related_work, harness, values.
- 23:58 the Sol round's regular tests (852 runs, 10 in flight); the policy units (663 runs) queued after them.
- Qwen: trojai3's GPUs were all taken; the setup was copied to trojai4 (`/data4`) and serves from GPUs 4–7 there.

## Decisions taken by the lead (within the PI's delegation)

- The budget is 10 minutes (verified: every final run used 600 s); scores and report numbers rebuilt.
- Duplicate policy units (two true pairs) count once.
- Thinking level "medium" set explicitly for GPT runs (OpenClaw's "off" label means the provider's default).
- The Sol round runs the Muse-written half first; the regenerated half follows.

## Session log

- 00:0x judge_qwen: Muse's saved judge prompts equal judge_v2.md + replica notes + bundle byte for byte; it sends
  the same to Qwen with the same schema, from a backend inside its study folder. Told to use the self-host.
- 00:0x harness: Codex CLI's system-wide binary is broken (the VS Code extension's works); Codex's cache lists
  gpt-6-sol, not 6.1. Budget set at 4 Codex runs. Survey findings above; Sonnet smoke allowed with strict
  isolation (no MCP servers, connectors or synced skills; restricted tools; never copy ~/.claude credentials).
- 00:0x regen: 35 distinct briefs (arm P v2 repeated arm P's sets), plus G4-LIN-35 for the related-issue lure;
  ids continue Phase 4's numbering; rulings appended to known_defects.json on its branch.
- 00:0x related_work: my brief's pointer to the MCP-Bench account was wrong; the account is now Appendix D of the
  notes; the PI's audit files are under ~/PyProj/mcp-bench.
