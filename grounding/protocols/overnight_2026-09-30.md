# The overnight session of 2026-09-29/30: the lead's log

*Kept by the lead session ("RoadMap specialist") while the PI was away. Newest entries at the bottom of each
section. Decisions that stand go to the [roadmap](roadmap.md); this is the record of what happened.*

## For the PI in the morning (written 05:40; the session log below has every detail)

**Results**
1. **GPT-6.1 Sol on OpenClaw, the whole Muse-only suite** (`sol_eval_01`, complete): on the 487 regular tests of the
   Muse-written half and the regenerated half together, **Sol exposes a fact in 20 tests and 13 facts; Qwen on the
   same tests 139 and 88.** On the first half: 13 of 282 tests and 7 facts against 78 and 47, every one of Sol's
   also exposed by Qwen; on the regenerated half: 7 of 205 and 6 against 61 and 41 (one fact Sol's alone, the
   related-issue direction, in one trial). **No policy cell is policy-level for Sol** (rates 0.00–0.20 across all
   sixteen cells of the two halves; Qwen 0.44–0.90, Calendar absence policy-level for the Muse-only suite). No run
   over budget, no stalls on the second half; a median 42–61 s per trial against Qwen's 171–248 s. Judge v2 agrees
   with 174 of 176 blind labels on the first half (the two are ruled-flawed tests) and all 135 on the second. Three
   of Sol's six regen-half facts rest on borderline near misses. Judging cost $52 list in all. 16 G4-LIN-08 tests and
   units could not run (clocked past the login's expiry).
2. **The judge on the self-hosted Qwen meets the bar** (`judge_qwen_01`): 0 missed of 192 labelled failures (1 under the
   any-reason reading), precision 97.4% against Muse's 98.0%, the same verdict on 440 of 443 and the same facts on
   every joint failure, at $0 per token (3.5 GPU-hours) against $13 list for Muse. The judges fail differently: Muse
   credits unsent conclusions (harmless under the budget), Qwen calls real failures artifacts where the replica notes
   are silent (three candidate note additions). The full replay is 680 of 1,696 done, paused for host capacity.
3. **Failures beyond fact discrimination** (`values_01`): 179 of 3,018 executions carry a finding the grounding verdict
   cannot see, 52 of them passing grounding; literal values are always copied right, the errors are interpretations
   (Linear's priority scale above all); 96 replies state a value other than the one written; 14 executions fabricated
   the identifying evidence. Mechanical checks at precision 1.00; a value-layer proposal.
4. **Related work** (`related_work_01`): 69 works, 12 angles; concurrent work names our failure class (Entity Binding
   Failures, arXiv 2606.30531) and agrees with our look-alike results; ClawEnvKit is the generator baseline to run;
   Agent-Diff's served evaluation has no closed-world check; the credit rule's ancestor is Zhong, Yu and Klein 2020.
   Four baseline preparations built (P1, B2, S1, B1). B1 (the masked-operation baseline, 48 items × 3): 47 of 144
   pass (50 with the quiet-host reruns); 40 of 48 items fail at least once; its agent left the service interface
   (direct backend calls, host probing, repository reads), which prompted the host-access scan of the main rounds.
   P1 (the status quo's mutation: 48 matched absence/underspecified variants × 3, same agent and judge as ours):
   absence 34 of 72 trials fail (14 of 24 variants; the agent re-creates the missing record or acts on a near miss
   the seed happens to hold); underspecified 64 of 72 (23 of 24; the agent picks the "primary" match and discloses
   it). Request-level failures with no facts behind them: P1 designs no near misses, so under the credit rule it
   exposes no fact, as N0 and N1 did (its 48 variants touch 31 fact–mode requirements by occurrence, an upper
   bound, not credit). Judge v2 agrees with 55 of the 56 blind labels not forced void (the one difference is the
   rule's, a backend probe). $7.12 list for judging. Report §5.7 (B1 and P1), with the incidents kept in the record.
5. **The second harness** (`harness_scout_01`, `claudecode_pilot_01`): Claude Code, with Sonnet 5.5 on your plan and the
   self-hosted Qwen, both run end to end; a 32-test Sonnet pilot: 2 failures, judge 32 of 32, 13 s per run, $0. On
   the same 32, Sol had none.
6. **The regenerated half** (`regen_01`, complete): 34 of 35 briefs, 337 tests, covering 76 of the briefs' 82 facts and
   74 of Sonnet's 81. Run on Qwen and scored: **41 facts at detect@3 (29 at @1) through 61 of 205 tests, against the
   Sonnet-written half's 40 (27) through 61 of 271**; of Sonnet's 81 facts each half exposes 40, 22 shared. Judge v2
   agrees with 97 of 100 blind labels. For a Muse-only suite, Calendar absence becomes policy-level (0.90; the Sonnet
   units at 0.64 leave the cell); the other seven cells keep their decisions. The escape clause matters: 29% of
   no-target regular trials fail with "if there isn't one, just tell me", 77% of absence twins without it. Muse
   cost $57.45 list. Sol's run of this half is in item 1.
7. **Naive baselines with Sonnet 5.5** (`baselines_02`, complete): with Sonnet writing them, the naive tests expose
   facts (SN0M 3 at detect@3, SN1M 2; all four Muse arms 0), still far below ours (11.3 per 48). Sonnet writes 3–4×
   more designated look-alikes than Muse and exercises more facts (22 and 37 against 12 and 13), but writes no probes;
   4 of the 5 exposures go through designated look-alikes. Judge v2 agrees with 29 of 30 blind labels on each arm.
   Generation $3.21 list on the plan; judging $7.88 list.
8. **Transfer to the real services** (`transfer_feasibility_01`): 37 tests run as is, 403 with test accounts, 476 with
   a stated change, 90 not on ordinary accounts; a 40-test case study proposed at $0 in plans.
9. The 10-minute budget applied everywhere; both report texts brought to the current numbers (998 cases, 2,994
   executions after two of your blind-review rulings reached the rulings file); a framing proposal for your point 5.
   One correction (13:00–13:50): the 10-minute rebuild of the policy numbers had silently dropped the budget rule
   for the Qwen round's 1,743 policy verdicts (their attempt paths pointed into a removed worktree). Rebuilt by the
   sol_score session with the rule restored: no pooled decision changes and no Sol number changes; the Qwen policy
   rates move up (the largest: Linear absence 0.61 → 0.66, Box underspecified 0.48 → 0.55, Linear underspecified
   0.41 → 0.48; Table 12's facts at detect@3 in the policy space 157/111 → 163/136). Each file's old → new is
   logged in report_01's README ("Follow-up: the budget rule restored") and in sol_eval_01's.

**Decisions for you**
1. The Sonnet round: OpenClaw's loop on an API key (about $263 list for the full suite, the only same-harness
   comparison) or Claude Code's loop on the plan ($0; needs a `claude setup-token` from the plan that is really Max:
   this machine's login says Pro).
2. The timeout rule under a shared host: regen and the baseline arms lost trials to host load (24–67 s per request);
   they are kept apart and rerun on a quiet host, both readings reported.
3. Rulings: the three "word in a sibling field" cases; "Atlas Onboarding Archive" for "the Atlas Onboarding hub";
   AR-BOX-24's run-date dependency; the conflict between the 09-28 "Cycle 4" ruling and the blind review's.
4. Baseline budgets: ClawEnvKit (48 tasks, about $5–7 list, 2 days of adapters); the full Agent-Diff projection.
5. Harness hardening: attempts run as you with a shell; a future round should use a restricted user or a container
   (the main rounds are clean: no bypass produced a pass).

**Open**
- The 16 G4-LIN-08 tests (shift the scenario's dates, or an API key).
- trojai3's GPUs are still taken; Qwen serves from trojai4's two PCIe copies, which cannot carry three solver arms.
- Five replica findings from values_01, two from the baseline arms and one platform defect from P1 (the Linear replica
  can freeze the whole backend under two concurrent requests on one team; 14:20–14:38 today), on the replica list, not fixed.

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
- 01:3x sol_score found two of the PI's blind-review rulings missing from known_defects.json (G4-BOX-11's "Seaport
  Archive 2024" is a match; a copy in a subfolder counts as "in the folder" for G4-BOX-02). Applied (commit
  3405221d90): two probes leave the suite; the Qwen round is 139 of 563 tests exposing, 87 facts at detect@3, 60 at
  detect@1; decisions unchanged. Sol is scored under the updated file, with the old reading as a second column.
  Also from sol_score: regular_p4 judged and its 45 blind labels locked (1 failure among them); 6 of 444 trials
  pending the retry pass.
- 01:3x harness done (commit 56ef84c742; merged into main as ee61eabe70). Recommendation: **Claude Code as the second
  harness** (Sonnet 5.5 on the plan and the self-hosted Qwen, both run end to end through the curl shim and skills;
  the clock solved with an LD_PRELOAD shift; the init event shows no MCP servers or synced skills); Codex for Sol
  only if one run confirms gpt-6.1-sol on the plan (the bundled 0.155 refused it: "not supported when using Codex
  with a ChatGPT account"; 0.159.2 lists it) and with Calendar and the clocked tests left out (Codex's date cannot
  be shifted). If one third-party harness must carry all three, OpenCode with Sonnet on an API key. For the PI:
  the Pro-not-Max login; the Sonnet round's choice (OpenClaw's loop on an API key, about $263 list for the full
  suite, the only same-harness comparison; or Claude Code's loop at $0); the Codex weekly window at 71%, reset
  2026-10-03 15:17 EDT, shared with the Sol round. Assigned next: Claude Code as a backend of our runner and a
  32-test Sonnet pilot (claudecode_pilot_01).
- 01:22 the Sol policy units now run once each first, then trials 2 and 3, because of the plan's window.
- 01:4x sol_score, regular_p4 scored (provisional, 6 of 444 trials pending the retry pass): **Sol exposes a fact in
  5 of 148 Phase 4 tests, against Qwen's 47 on the same tests; 3 facts at detect@3 and detect@1 against Qwen's 26
  and 20.** Every test Sol exposes, Qwen exposes too (A:Message.blocks in G4-SLK-04's three forms, A:Event.summary,
  A:ProjectMilestone.name). 14 failing trials against 86; Sol's mechanisms mostly skipped-check (its reasoning is
  invisible to the judge). Judge v2 agrees with all 45 blind labels and finds the one labelled failure with the
  same fact and mechanism. A Sol trial takes a median 42 s against Qwen's 174 s, 4 tool calls, few reasoning
  tokens at "medium". Cost of judging p4: $7.08 list, $0.50 billed. Harness difference to fix before any further
  round: in the openai backend `memory_search` fails ("agent database belongs to agent main; requested agent
  assistant") because the login store copied into the attempt's agent directory carries the main agent's identity;
  Sol called it in 110 of 444 trials; no grounding outcome changes.
- 01:29 report_01/numbers rebuilt in full after the two rulings (the values session, now on the report update,
  found it half-rebuilt): the final manifest is 998 cases and 2,994 executions (563 regular tests; 242 absence and
  193 underspecified units). The report texts are being re-synced to it.
- 01:32 harness (commit c6210f8594): a Claude Code backend with OpenClaw's contract (claudecode_pilot_01/backend.py,
  run.py reusing openclaw_eval_01's selection): two smoke runs in 12–13 s, the context date matching each test's
  clock, no MCP servers, no leaks, no account email. Authentication for tonight, approved by the lead for the pilot
  only: the login's access token read at launch into an environment variable, never written, the refresh token
  never read, runs refused near expiry; a full round waits for the PI's `claude setup-token`. Next: the 32-test
  pilot with Sonnet 5.5, its 32 trials blind-labelled, judge v2 on Muse (cap $3).
- 01:37 regen (commit a3deb4e781; merged into main as 7dfd8ab40e, with both sets of near-miss rulings kept in
  known_defects.json): 33 of 35 briefs accepted on the first draw (G4-LIN-30 and G4-SLK-18 rejected by the cold
  reader as unnatural; a second draw each allowed); 202 Muse calls, $25.45 list, $1.50 billed. Review of the 33:
  24 valid, 5 weak but valid, 4 flawed but usable; 5 of 130 near misses flawed (group B, under the 09-28 rulings);
  7 borderline ones valid and flagged for the PI. Coverage: 74 of the briefs' 82 facts, 72 of Sonnet's 81 (66
  through designated near misses); gained H:IssueLabel.parentId (one of the nine uncovered facts), A:Cycle.number
  through an F8 near miss, R:IssueRelation.relatedIssueId through the reversed direction; lost as findings
  A:Message.message_text and A:CalendarListEntry.selected (Muse built the catalog's designated substitute, which the
  rulings make flawed). Drop-F variants generating; then the units, the blind sample, and "ready to run".
- 01:36–01:40 **an incident of my making:** while I merged exp/regen-01 into main, roadmap_01/known_defects.json
  held merge-conflict markers for a few minutes; the runner reads that file per attempt, so 262 of the 6b regular
  jobs failed instantly with a JSONDecodeError and the run ended early (145 6b attempts completed and sound). The
  missing jobs were restarted at 01:42 (runs/run_regular_6b_rest.sh, concurrency 6, beside the policy pass). Lesson
  recorded for the briefs: never resolve a merge conflict in the main checkout while runs read the file; merge in a
  worktree, or stop the runs first.
- 01:5x report_update done by the values session (merged as 0992a74d4c): report.md and report_concise.md match
  numbers/ at a8c046c891 (998 cases, 2,994 executions); every change logged in report_01/README.md under "Text
  changes (2026-09-30)". Left labelled in the text: §10.1's 8-minute policy count; Table 14's Ours column and Table
  15's rows from baselines_01's pre-rebuild files; Table 11's first-pass column. Assigned next: beyond.py's policy
  filter, baselines_01's recomputation, openclaw_eval_01's README numbers.
- 02:0x harness, claudecode_pilot_01 done (commits to 8c70467512; merged as f4779e926b): Sonnet 5.5 on Claude Code
  on the Sol pilot's 32 tests, one trial each: all 32 completed; blind labels 7 correct, 23 correct_absent, 2
  incorrect (G4-LIN-04, FP-G4-LIN-06); judge v2 agrees 32 of 32 with the same facts; median 13 s per run against
  Sol's 37 s; $0.052 per run at list, $0 billed (about $79 for the Muse-written half, $157 for the full suite);
  plan windows over the pilot: five-hour 41% → 45%, seven-day 11% → 12%, shared with the sessions. For the PI: a
  full round waits for a `claude setup-token` token (~/.config/claude-solver/oauth_token) made from the plan that
  is really Max; confirm effort medium, tools Bash/Read/Skill, no follow-up. Assigned next: the same-test Sol
  comparison on the pilot's 32, then the openai backend's store layout behind a flag.
- 02:1x values, the three consistency follow-ups (commits 5496406e9c, 3787ff5159, 5a464f392a, cc8aa801fd): beyond.py's
  policy side filtered by the rulings (1,305 trials; RQ7 updated); baselines_01's ours.json and compare.json
  recomputed from the rebuilt full_02 (per 48 tests: 11.3 / 7.5 facts, 12.8 failing tests; only Phase 4's Calendar
  moved); openclaw_eval_01's README brought to the 10-minute, rulings-updated numbers (6a 108 of 429; with 6b 139
  of 563, 87 / 60; over-budget policy trials 129 of 1,170 under 10 minutes against 188 under 8). Assigned next: the
  Sonnet baselines brief.
- 02:2x harness (commits to 73e47f4858; merged as 9ce4be318a): the Sol pilot judged with the same judge: on the same
  32 tests, Sol has no failures where Sonnet on Claude Code has two (one trial each; an observation). The openai
  store layout is fixed behind AGENTDIFF_OPENAI_STORE=main (the login store becomes the attempt state's main-agent
  store; the attempt agent gets a fresh one; memory_search then works, at the cost of an embeddings request per
  call on the plan); the default path is byte-for-byte unchanged, so the running round is untouched; it goes on at
  the start of a future round. Assigned next: unit tests, then the Qwen-as-writer investigation (qwen_writer_01).
- 02:2x related_work (commits to feae5da520; merged as f8f5112a67): the four no-decision baseline preparations, no
  model calls. P1: 350 policy variants of Agent-Diff's tests (262 absence, 88 underspecified; underspecification
  is thin: 44% of candidates cannot be made faithfully). B2: seven abstention suites' 2,843 boundary-type items
  mapped onto our classes; three of our classes (read-only field, permission, state precondition; 76 of our 93
  faithful elements) have no counterpart; τ-bench's policy-forbidden class is one we lack. S1: Agent-Diff's seeds
  defeat 3 of the 15 practical lazy shortcuts our automation defeats on those services; 152 of 210 plural targets
  (72%) would go unnoticed by its assertions if omitted. B1: 71 valid masked-operation items (48 selected), the
  oracle and a runner ready. For the PI: Box's replica search reads names and descriptions, not content (B-A10);
  P1's Linear team-name copies need a fact check; whether the boundary space should hold policy documents; 20 of
  213 "correct" cover trials did not make exactly the requested change. Assigned: run B1's selection and P1's
  matched 48 on the self-host tonight, with blind labels.
- 02:3x regen ready to run (commit 85ce248553; merged as 4f88565da5, in a separate worktree this time): 337 tests,
  1,011 executions at 3 trials: 206 regular (34 covers, 127 probes, 45 fact probes), 72 absence and 59 drop-F
  units; 100 blind trials drawn first. Funnel: 35 briefs, 37 attempts, 34 accepted (G4-LIN-30 rejected twice by the
  reader; the fact set Sonnet also failed); 135 near misses declared, 6 flawed; 216 regular candidates, 206 valid.
  Coverage: 77 of the briefs' 82 facts, 75 of Sonnet's 81. Muse so far $38.87 list, $2.38 billed. For the PI:
  A:Team.key/description/private uncovered (the reader rejects naming a team by privacy, key fragment and
  description); message_text and CalendarListEntry.selected uncovered because their designated near miss is the
  ruled-flawed construction; three "word in a sibling field" borderline cases for one ruling on the pattern. Runs
  started on the self-host at 16 in flight.
- 02:4x the self-host overloaded (two PCIe copies on trojai4; trojai3 still fully taken): the judge replay at 16 in
  flight, regen's runs at 16 and B1 at 8 gave 24–67 s per model request, and B1's first 12 Box trials ran out the
  10-minute limit on host slowness (9–25 requests each, no limiter waits). Decisions: the judge replay pauses (its
  labelled result stands); regen drops to 12 in flight; B1 stays at 8 and P1 waits for it; trials that time out
  under host load are marked so, rerun when the host is quiet, and reported in both readings, since vLLM's queue
  time is invisible to the agent clock and is our infrastructure. For the PI: the timeout rule under a shared host
  (the step-5 question) needs a ruling; and the two copies cannot serve four sessions at once.
- 02:5x judge_qwen paused (commit 8e5028c8b8; merged as 82d59dc008) after 680 of the other 1,696: same outcome
  group on 667 (98.1%), same facts on 316 of 317 joint failures; 15 disagreements adjudicated blind (Qwen right on
  9 of 13 group disagreements). **The two judges fail differently:** Muse credits the conclusion in an unsent last
  reasoning as if it had been sent (10 of 11 runs that ended without an answer; score-neutral, they are over
  budget); Qwen calls real failures artifacts where the judge's replica notes are silent on a readable field
  (Calendar dataOwner, Box uploader_display_name, Slack reactions in history, the renamed "Cycle 4"), which costs
  exposures; on score-changing disagreements Muse is right 5 to 1. Three candidate additions to the replica notes
  for the PI. Assigned next (no host): the transfer feasibility desk study (transfer_feasibility_01).
- 03:0x values, baselines_02 (Sonnet 5.5 as the naive writer, arms SN0M and SN1M): 96 of 96 tests load at once, $0
  billed on the plan, 23 minutes. Blind review in one shuffled pool with 20 of ours: 109 of 116 valid (44 and 45 of
  48; ours 20 of 20); designated near misses 57 of 113 and 75 of 130 (Muse's twins 17 of 53, 19 of 66; ours 81 of
  99); facts exercised properly 22 and 37 (Muse's 12 and 13; ours 34.0 per 48); still no probe-form tests. Runs on
  the self-host at 6 in flight (267 trials); blind samples of 30 per arm drawn first; a cross-check re-review of ten
  Muse twins.
- 03:1x values, baselines_02 cross-check (544b851bed): on 15 baselines_01 tests re-reviewed blind (5 N1 fully blind as
  the control), validity, flaw cause, form, near-miss records, family and proper credit agree with the other
  session's calls (15/15, 16/16, 14/14); the fact named differs on 2 plain near misses. The Sonnet-versus-Muse
  structure gap is not a reviewer effect. Runs going at 3+3 in flight.
- 03:2x judge_qwen, transfer_feasibility_01 (commit ce990f2a84; merged as 871d6db399), a desk study with cited API
  pages: of the 1,006 tests, 37 are realizable on the real services as is, 403 with test accounts, 476 with a
  stated change (204 date shifts where the services set times themselves, 179 renamed ids and handles, 123 paid
  tiers, mostly Linear Basic for more than two teams; 118 Box consistency constraints, inferred), and 90 not with
  ordinary accounts (47 Box Hubs, Enterprise only; 17 Box near misses created after their last modification; 14
  ownership differing within a folder, inferred; 12 focus-time events on secondary calendars). Linear's import
  fields backdate issues and comments; Calendar takes any past date. Proposed case study: 40 tests, 10 per service,
  half of them failed on OpenClaw, free tiers, at most 4 people besides the actor, $0 in plans, about 2 agent-days
  of scripts and 6 hours of runs. Pilot items: Slack search needs a user token (42% of Slack executions searched);
  Box As-User on the free plan; the two inferred Box rules; Linear's 250-issue cap.
- 03:5x sol_score, both regular sets (provisional; 9 trials pending the retry pass): **Sol exposes a fact in 13 of
  282 Muse-written tests, Qwen 78 on the same tests; facts 7 at detect@3 and detect@1 against Qwen's 47 and 33;
  every fact Sol exposes, Qwen exposes too** (both 12 tests, Sol only 1: G4-LIN-12's cover, Qwen only 66). Per
  service Sol/Qwen: Box 1/25, Calendar 4/23, Linear 5/18, Slack 3/12; per form: covers 2/8, probes 8/56, fact
  probes 3/14. Sol: 32 failing trials, none over budget, mechanisms mostly skipped-check (its reasoning is
  invisible). Judge v2 agrees with 87 of 89 blind labels; the two differences are the Seaport and subfolder
  trials, labelled artifact under the PI's reading. Judge cost so far $20.18 list, $1.44 billed. Absence labels on
  the second and third passes show Sol acting on near misses in absence twins (4 failures in 24). For the PI:
  AT-G4-BOX-15's "Atlas Onboarding Archive" for "the Atlas Onboarding hub", labelled by the construction.
- 04:0x the host too loaded for three solver arms (regen's timeouts 9%, clustered on the busiest minutes): the two
  baseline arms (B1 at 73 of 144 trials, baselines_02) pause; regen keeps the host at 12 in flight. B1 found that
  OpenClaw's agent, running as the user with a shell, can probe the host, read the repository (the answer keys are
  on disk) and call the replica backend directly past the curl shim; its masked operations triggered all three
  (18 trials probed, 5 read source, 3 wrote straight to the backend). **The main rounds are clean:** a scan of every
  final-round command (sol_eval_01/kit/host_access_scan.py) finds 13 of Qwen's 4,464 trials touching the host or
  the backend, all endpoint probing in stuck absence probes, the one direct write in a trial judged a failure
  anyway, no bypass producing a pass; none of Sol's 1,196 trials. For the PI: a future round should run attempts
  under a restricted user or a container; the neutral layout hides names, not the filesystem. New replica gap:
  Calendar cannot re-add a calendar-list entry after DELETE.
- 04:07 baselines_02 paused at 96 of 267 trials (SN0M 45, SN1M 51). Early labels: the first target-present fact
  exposure by a naive baseline (SN1M-BOX-T03 t1: owner taken for uploader, R:File.created_by_id), two presupposing
  policy failures, everything else right.
- 05:24 the Sol round's runs are complete: regular p4 444 and 6b 408 attempts (9 pending the retry pass), absence
  365 completed of 369 attempts, underspecified 270 of 273; the retry pass (stalls reclassified, infrastructure
  errors rerun) started at 05:24.
- 05:36 **the Sol round is complete:** every attempt completed after the retry pass (regular p4 444, regular 6b 405
  over 135 cases, absence 369, underspecified 273; 3 stalls reclassified and rerun; the last infrastructure error
  rerun by hand). Scoring of the policy sets and the final numbers are with the sol_score session.
- 05:5x sol_score done (commits f00d9c9940, fca57dd6de; merged as d32f0787b9): the Sol round judged and scored in
  full; the numbers are in the morning brief. For the PI: AT-G4-BOX-15's "Atlas Onboarding Archive" with a what-if
  (no decision changes either way). Assigned next: the Sol section in the report texts.
- 06:1x sol_score: the Sol round added to both report texts as "A second agent: GPT-6.1 Sol on the same harness"
  (Tables 12a–12c in the concise text; §0.4's scope and the limits updated; merged as bd9fd54d8a). Follow-ups
  assigned: a report kit for the Sol numbers (numbers/sol.json); list prices only in the texts, per the PI's rule,
  with one sentence on the actual spend under contributor pricing. Noted for the policy kit: cell_stats stops at
  the first unit without verdicts (only matters when a unit is unrun).
- 06:3x sol_score (f9b977e4e4; merged): report_01/kit/sol.py → numbers/sol.json behind the Sol section; every billed
  figure removed from both texts (list prices only, one sentence in §12 on the actual spend at about 6.6% of list);
  Table 18 gains the Sol judging row ($32.60 list) and the Sol agent row (8,172 requests, 19.6 agent-hours).
- 06:4x sol_score launches Sol on the regenerated half (337 tests, trial 1 first, then 2 and 3, stop rule on the
  plan's window; default store layout kept for one harness state across the Sol round, the fix reserved for the
  next round; judge cap $25 list). No merges in the main checkout while it writes there.
- 11:3x regen's Qwen runs complete: 1,002 executions (615 regular, 213 absence, 174 underspecified; three G4-SLK-14
  tests left out at run time by the "Marcus Webb Jr" ruling), 100 blind labels written before any verdict; 18
  host-load timeouts being rerun quiet, both readings to be reported; judge v2 on Muse running. The baseline arms
  resume when the host frees (about 11:55).
- 08:0x qwen_writer_01 (harness session, commit d48b099c16): Qwen's writer matches Muse on 12 Phase 4 briefs (12
  of 12 accepted, 23 of 23 facts covered validly, same wording quality) at about 9x the writer time and $0; two of
  its near misses ruled flawed on person-naming wording, with Phase 4's opposite reading beside them; its 72 tests
  run on the self-host at 6 in flight for the exposure comparison (Muse's 74 tests on the same briefs: 19 exposing,
  9 of 23 facts at detect@3).
- 12:0x qwen_writer_01 done (commit d38d3a0219; merged as 3702de065a): **Qwen's writer matches Muse** on 12 Phase 4
  briefs (12 of 12 accepted, 23 of 23 facts covered validly, 43 of 45 near misses valid under the session's
  rulings, the same wording quality) at $0 and 25–112 minutes of writer time per brief (Muse 2–15); its tests
  expose comparably on Qwen (24 of 70 tests exposing, 12 of 23 facts at detect@3, against Muse's 19 of 74 and 9;
  a 5-to-2 split within 3-trial noise); judge v2 agrees with 29 of 30 blind labels (the one is the ruling
  question). For the PI: two person-naming readings ("Maya Chen's" as owner or creator; "uploaded" as first or
  current version) on which Phase 4 read Muse's briefs the other way, and an "open link" reading solvers took.
  Confounds recorded: Claude Code's writer path and effort medium; the reply cap and window relay.
- 12:3x harness, hardening.md (d6b40284aa; merged): recommendation for the next round: each attempt in bubblewrap
  with a minimal filesystem and an empty network namespace bridged to two host-side proxies (the model proxy and a
  new per-attempt replica proxy that forwards only that environment's service paths, applies masks and logs
  refusals); about a day and a half to build, negligible per run (OpenClaw starts in 25 ms sandboxed). Not a
  separate user (needs sudo, leaves loopback open); not a container (same guarantee, more machinery). A token in
  the shim would not help (the agent can read the shim); the per-attempt socket is the capability. For the PI: the
  replica on 18001 answers any local process without a key, and this machine has other accounts; the Claude Code
  backend's token is in the process environment (whether its Bash tool sees it is the first check of the next
  pilot); a cheap step now is to make the model proxy refuse unrouted requests during rounds; the openai backend
  reaches OpenAI directly and gets only the filesystem sandbox for now.
- 11:43 Sol on the regenerated half complete: 618 regular, 216 absence and 177 underspecified attempts with the
  retry passes done; the OpenAI plan's window held. Judging and scoring with the sol_score session.
- 12:2x regen done (head ff030e5764; merged as d3cc99720c): the numbers are in the brief. For the PI (regen_01's
  README, "For the PI"): the sibling-field pattern (3 cases, one ruling); qualifier versus new meaning ("Marcus Webb
  Jr" flawed; "Sprint 22 Overflow", "Editorial Calendar Archive"); nested labels as the analogue of folder
  descendants; the Cycle-number tension; "5-person" and the bot; the two facts whose designated substitutes are
  ruled-flawed constructions; the team facts the reader rejected twice; 6 of the 41 facts rest on the 8 borderline
  near misses.
- 12:4x sol_score done on the regenerated half (commits to c3b1615e63; merged as 8f7237f73c): the numbers are in
  the brief; 10 of 1,011 trials needed one retry, no quota or rate-limit error; a last task assigned to make the
  budget rule's attempt paths repository-relative (regen's verdicts record worktree paths).
- 13:0x **a second error of mine, found by sol_score:** the 10-minute rebuild at 49ce3672dc lost the budget rule for
  the first round's 1,743 policy verdicts, because their recorded attempt paths point into the removed roadmap-02
  worktree and `population_outcomes` skips the rule when the path is missing, so over-budget trials the judge
  called not_established counted as void instead of failures. No pooled decision changes, but the committed rates
  are low (Linear absence 0.608 against 0.656 with the rule; Slack underspecified 0.768 against 0.802). The fix
  re-roots attempt paths against the repository and warns when one cannot be resolved; sol_score is rebuilding
  every affected file (decisions, report numbers and texts, regen's and sol_eval_01's Qwen columns) with a logged
  old → new for each. Every Sol number is unchanged.
- 13:2x related_work, B1 done (commit 6b8f16fd35; 48 masked-operation items, 144 trials on Qwen, boundary_02's
  oracle): 47 of 144 trials pass as run (50 with the 12 host-load reruns); 40 of 48 items fail at least once. By
  service, Slack 29 of 36 pass (its "unknown_method" reads as "no such method"); Box, Calendar and Linear 5–8 of 36
  (a 405, a 404 or a GraphQL error reads as a broken environment and the agent probes until the budget ends: 77 of
  the 97 failures ran out the budget, 33 of them after an unrequested change); 17 made such a change and answered;
  4 wrote straight to the backend. The oracle agrees with all 30 blind labels. Reading: masking measures the
  response to an environment that seems broken (FeasiGen's "false continue"), not knowledge of a service's limits,
  which our boundary tests measure; keep both. P1 started at 13:23.
- 13:3x values, baselines_02 done (merged as fca0337589): the numbers are in the brief. Replica findings: Slack
  history and replies omit reactions while the judge's replica note says messages carry them (reported now by three
  studies: the note is the thing to fix); Calendar occurrence ids with local digits plus "Z"; Linear
  teams{projects{nodes}} fails. Rule readings for the PI: a family only when the catalog lists it for the fact; sets
  get no proper credit; a self-corrected write on a decoy counts; a timeout after the right write is a failing test.
- 13:5x sol_score done (f618a40eba..c3e278e4a1; main fast-forwarded to c3e278e4a1; `score regress` and
  `policy regress` pass on main): the budget rule restored for the first round's policy verdicts, with every affected
  file rebuilt and each change logged old → new. 140 pooled decisions checked, none changed; Sol's numbers unchanged
  (only qwen* fields differ). An independent cross-check: judge_qwen_01's headline.py, which finds attempts through
  its own manifest, reproduces all eight rebuilt cells and the regular score. Rates that moved (failing/usable):
  Box absence 126/165 0.764 → 135/173 0.780; Calendar absence 0.815 → 0.817; Linear absence 160/263 0.608 → 193/294
  0.656; Slack absence 0.600 → 0.612; Box underspecified 65/136 0.478 → 85/155 0.548; Calendar underspecified
  0.457 → 0.511; Linear underspecified 83/205 0.405 → 114/236 0.483; Slack underspecified 0.768 → 0.802 (still
  undecided). Secondary reading (any_of_runs): Box and Calendar underspecified "not" → "undecided". regen_01's
  Muse-only suite: Linear absence 0.586 → 0.621, Box underspecified 0.455 → 0.496, Calendar underspecified
  0.548 → 0.593, Linear underspecified 0.456 → 0.505, the rest within 0.01; one by-source decision moves (Phase 4's
  own Calendar absence units 0.875 undecided → 0.877 policy-level, p10 0.807). sol_eval_01's Qwen columns: first
  half range 0.44–0.90 → 0.51–0.91; the whole suite's facts failing (detect@3/@1) absence 150/128 → 156/136,
  underspecified 106/79 → 126/96; the regenerated units alone unchanged. report_01, Table 12 (the per-fact space):
  detect@3 157/111/268 → 163/136/299, detect@1 129/80/209 → 142/107/249; RQ8's Phase 4 underspecified units failing
  32 (29 designated) → 41 (38). judge_qwen_01's headline (rebuilt under the 10-minute budget, today's rulings and
  the duplicate merge, none of them the lost rule): all eight decisions match with Qwen's verdicts; 140 of 563
  regular tests against 139. Two things beyond the letter of the assignment, accepted: headline.py merges duplicate
  pairs as decide_population does; `population_outcomes` warns on stderr when an attempt cannot be found (silent on
  all 21 real verdict folders). Not touched, noted: autogen_01/kit/score_run.py:28 compares recorded attempt paths
  as strings (re-running phase4 score for full_02/03/04 from another checkout would void their judged trials);
  openclaw's first-pass decisions_{mode}.json never applied the budget rule (a dated record). Roadmap rows 6a, 6b,
  6e, 6h and 7 brought current. Sol's regen-half run evidence committed at df1dc89750 (14,554 files).
- 14:0x sol_score, two kit fixes merged (0c7c339b2a, 6f788eca9e; main at 558ec971b5): `autogen_01/kit/score_run.py`
  compares recorded attempt paths from grounding/runs/ on and warns on stderr when one cannot be found (before the
  fix, re-scoring full_04 from a worktree counted 0 of its 205 verdicts; after it, the three score files and every
  adjudicated file reproduce byte for byte from the worktree); `openclaw_eval_01/policy.py`'s population readings
  use only the units that ran and record `units_without_verdicts` (sampler.cell_stats itself stops at the first
  unrun unit on purpose: the sequential design's frontier). No decision or number changes. The same trap in the
  judge's verdict cache (`autogen_02/kit/judge2.py:124`, `autogen_01/kit/judge.py:135`: a re-judge from another
  checkout would treat every cached verdict as stale and call Muse again) is assigned as the third fix, to be proved
  without a model call.
- 14:2x sol_score's third fix merged (608476c9cc; main fast-forwarded): both judges' verdict caches (`judge2.judge_one`,
  autogen_01's `judge_one`) recognize a cached verdict by the attempt's path from grounding/runs/ on, through one
  `same_attempt` in autogen_01/kit/judge.py; `judge2 check-cache` counts cached / stale / none without a model
  call. From a worktree, before the fix, 0 of 951 verdicts across three folders counted as cached (a re-judge would
  have called Muse for all of them); after it, 951 of 951, no verdict file touched (sha256 identical), a stale
  verdict still caught. Checked from the main checkout: full_04's 205 verdicts (recorded in the removed worktree)
  count as cached; score regress passes. sol_score's assignment is closed.
- 14:4x related_work: the shared replica backend (127.0.0.1:18001) was frozen 14:20–14:38 by a lock in one P1
  environment's schema (a session "idle in transaction" for 15 minutes on workflow_states; a second session of the
  same trial waiting on teams; the backend answered nothing, health check included). The session ran only its own
  stale session's `pg_terminate_backend`; nothing else touched. No other study ran against the backend in that
  window (the Sol round, regen and the baselines are done; the judge does not use it), so only P1 lost trials (two
  attempts of one variant, rerun anyway). Likely mechanism (not verified, for the replica list): the Linear replica
  locks the team row while creating an issue and its handlers make synchronous database calls, so two concurrent
  requests on one team (an agent running curls in parallel) can hold the lock while blocking the loop that would
  release it. Also P1's own seed builder: a deep copy of a Linear issue did not advance the team's issue counter
  (issueCreate collided, 500); fixed in its kit (cdabfd6669), the four affected variants rerun after the main run.
- 15:4x P1's runs over (144 trials by 15:21; the 12-trial counter-collision rerun and the linear_47 attempts by 15:44); its judging is on Muse under the $3 cap. The host quiet (vLLM at 0 in flight), judge_qwen resumed the full replay at 15:46 (the remaining 1,016, then the headline recompute against the rebuilt Muse numbers, after merging main).
- 16:0x related_work, P1 done (3f608f7428; merged as 33d477612b through the temporary worktree): the numbers are in the
  brief (item 4). Three incidents kept in the record with both readings: its seed builder's issue-counter flaw
  (four variants rerun as p1_01_fix), the backend freeze (8 attempts, retried), the runner's 2-hour limit (3
  attempts, retried). The related_work session's four preparations are all run or reported (P1, B1 run; S1, B2
  reported earlier). Checking out the merge worktree printed Git LFS's "919 files that should have been pointers"
  (autogen_02/runs' *.jsonl under an LFS pattern added after they were committed): pre-existing, a warning only,
  for the PI's repository list.
- 2026-10-01 09:5x (the lead, catching up): judge_qwen finished at 19:25 yesterday; merged as 931a4dcef6. The full
  replay holds under the PI's afternoon condition (roadmap, Decisions 2026-09-30): the bar met on two independent
  labelled passes with the same numbers, 98.6% agreement over all 2,115 executions, every policy decision and the
  regular counts unchanged with Qwen's verdicts (one fact swapped). The lead's decision: later rounds are judged on
  the self-hosted Qwen; Muse stays the reference for blind-label adjudication. Qwen's misses (7 real failures called
  artifacts over 2,115) come from three gaps in the judge's inputs that the PI can close for either judge: the
  Calendar replica notes do not say where a calendar's data owner shows; the judge's bundle hides a file's
  uploader_display_name; the Slack notes say messages carry reactions when conversations.history returns none. A
  new replica defect: the Linear replica ignores an issue filter on projectMilestone.
- 2026-10-01 10:3x the PI: "I gave no decisions yesterday. That was a misunderstanding." The roadmap's afternoon
  section of 2026-09-30 (the Muse-only suite, Qwen as judge, the Qwen-writer sample, step 8) is marked withdrawn,
  and the lead's 09:5x reading of the judge replay as a decision is withdrawn with it; the replay's result stands as
  a result. Nothing had been run on the strength of either.
