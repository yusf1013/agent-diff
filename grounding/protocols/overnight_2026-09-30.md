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
- 00:2x values (commit 35a9639cb4 on exp/values-01): mechanical counts on all 3,018 executions. 1,399 writes to a
  requested field, 1,275 with the requested value; literal values always right; the errors are interpretations
  (Linear priority 105/149; the year of an undated "July 15" in AR-BOX-24, a run-date dependency the date check
  missed; "red" as another palette entry). Replies: 96 state a value other than the one written; 40 misstate a
  priority merely read; 10 claim a change the diff lacks; 3 claim absence with a match present. Side effects in 43
  executions, 14 of them fabricating the evidence the request used to identify the record. Next: the precision
  sample and the restore cases.
- 00:2x judge_qwen: the labelled replay running on the self-host (97 of 443 at 00:21).
- 00:3x related_work (commit 279aed6736 on exp/related_work-01): the map (12 angles, 6 new), 34 cards, the verdict
  table (report.md §1–3). Early findings: concurrent work names our failure class, "Entity Binding Failures in
  Tool-Augmented Agents" (arXiv 2606.30531, 2026-06-29; 60 hand-built single-step tasks; look-alikes rarely bite,
  true ambiguity almost always does; no requirement space, no absence, no live exploration, no validated oracle);
  AgentAbstain (2607.10059) has 263 should-act/should-abstain pairs (missing parameter ≈ our underspecified;
  insufficient tools ≈ our "no operation" boundary; no presupposed absence); semi-automated suites leave to people
  what we automate (Agent-Diff's paper, AppWorld's hand-written distractors); ClawEnvKit (2604.18543) supports
  OpenClaw natively and is the generator baseline to run; saved Sonnet 5 runs on 59 Agent-Diff Slack tests: the
  suite's assertions pass 7 of 13 tests with a hand-labelled wrong-record error; the credit rule's ancestor is
  Zhong, Yu and Klein (EMNLP 2020). Next: the projection plan (Agent-Diff first, AgentDojo second) and the three
  baseline proposals.
- 00:45 related_work done (report.md 724 lines, commit 00263f657b; merged into main as 5093ad1cec): 69 works in 35
  cards, 12 angles (6 new); nothing tests against a model of the world the agent acts on; Agent-Diff's served
  evaluation has no closed-world check (an extra write no assertion matches passes); its assertions pass 7 of 13
  tests with a hand-labelled grounding error. For the PI: run ClawEnvKit as a generator baseline (48 tasks, about
  $5–7 list, 2 days of adapters); the full Agent-Diff projection (3–4 session-days, 672 self-host trials); the
  §5.5 baseline choices. Assigned next: the no-decision preparations P1, B2, S1, B1.
- 00:46 sol_score launched (sixth session): scripts first, judging after each set's retry pass.
- 00:55 sol_score found provider stalls: OpenClaw gives up after 120 s of silence ("LLM idle timeout") and ends
  the turn as a timeout, which the scoring would charge to the agent (3 of the first 350 Sol runs; Qwen never ended
  a timeout under 590 s). Now runtime rule R3 (commit fd38a82dec); the earlier ones are reclassified before the
  retry pass. Sol's steps carry no visible thinking (about 20% of steps have visible text): the judge sees
  commands, responses and the final answer; awareness is measured on visible text only.
- 01:0x values done (commit 7ecf7f3828; merged into main): 179 of 3,018 executions (31 scenarios) carry a finding the
  grounding verdict cannot see, 52 of them passing grounding (23 wrote the wrong value to the right record, 27
  misstate priorities in the reply). Literal values are copied exactly; the errors are interpretations (Linear's
  priority scale 105/149; a palette; a year from the run date; a substitute reaction). Side effects by cause: agent
  (14 fabricated the identifying evidence, 4 outside the candidate set, 2 reassigned to fit, 1 full PUT reset
  replies) and replica (17 cleared Box fields, 15 imperfect repairs). Precision 1.00 on every mechanical flag read;
  prose-stance checks weak; 30 unflagged writers had no missed error. For the PI: AR-BOX-24 as a known defect with a
  clock; five replica findings (Slack history omits reactions; no white_check_mark; Calendar stores API-written
  times in UTC but seeded ones as local; Linear attachmentLinkURL resolves by URL; Box 412 after a comment);
  report_01 RQ7's restore row counts no-ops as restorations and its "changed meeting time" is a storage artifact.
  Proposal: declare the requested value per written field at construction (13 kinds), mechanical checks, one added
  judge question for the residual. Assigned next: the report_update brief.
- 01:1x judge_qwen (commit f85f957415): **Qwen meets the bar as the judge.** On 443 labelled executions (192 labelled
  failures): 0 missed failures (strict reading; 1 void under the any-reason reading; the bar allowed 2); precision
  191/196 (97.4%) against Muse's 192/196 (98.0%); the same verdict on 440 of 443; the same exposed facts on all 196
  joint failures. Of the 3 disagreements (adjudicated blind, hash-locked), Muse was right on 2 and Qwen on 1. All
  443 verdicts on the first attempt, one fingerprint, 53 minutes at 16 in flight (about 3.5 GPU-hours, $0), against
  $13.00 at list for Muse. Candidate prompt change for the PI: the Calendar replica notes don't say where a
  calendar's data owner shows (calendarList, GET /calendars). Now replaying the other 1,696 (about 3 hours), then the
  headline numbers under Qwen's verdicts.
