# qwen_writer_01: the frozen pipeline with the self-hosted Qwen as the writer

Session "harness", an investigation the PI asked for, assigned by the lead ("RoadMap specialist") on 2026-09-30.

## Status

- **2026-09-30, 12:00 EDT. Done.** Both halves are complete and reported to the lead. The answer is below; the two
  near-miss rulings (43 or 45 of 45 valid) and the harness settings are for the PI.

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

## The answer

**Yes, on these 12 briefs: the frozen pipeline with the self-hosted Qwen3.8-27B as the writer produced tests of the
same validity and coverage as Muse's, and they expose facts comparably.**
- **Validity and coverage:** 12 of 12 briefs accepted, all 12 scenarios kept after my review, 23 of 23 facts covered
  validly, as Muse's. 43 of 45 near misses valid under my rulings, 45 of 45 under the reading Phase 4's review
  applied to Muse's scenarios on the same briefs (for the PI to settle). The wording is rated the same (7 natural,
  3 stilted, 2 contrived on both sides); Qwen's requests carry more role ambiguities and its seeds more data slips.
- **Exposure** (OpenClaw on the self-hosted Qwen, 3 trials, judge v2): Qwen's 70 counted tests expose 12 of the 23
  facts at detect@3 and 8 at detect@1; Muse's 74 tests on the same briefs exposed 9 and 7. Together 14. The
  difference (5 facts only Qwen's tests exposed, 2 only Muse's) is within the noise of 3 trials (exact McNemar,
  p about 0.45): comparable, not better.
- **The cost is time and fiddling, not money:** 25-112 minutes of writer time per brief (Muse: 2-15), $0 per token,
  and three harness settings found by stopped runs: effort medium (not the served default), a 64,000-token reply cap
  with a relay that fits each request to the 131k window, and a 4-hour call limit.
- **Confounds:** Qwen wrote in Claude Code, Muse in Muse Code; Qwen at medium effort, Muse at high; the two
  exposure runs are two days apart under different server loads and clocks (see "Results: exposure").

## Design

- **The draw** ([plan.json](plan.json), fixed before any generation or reading): the pool is the 29 Phase 4 briefs
  Muse's generation accepted (7 Box, 7 Calendar, 7 Linear, 8 Slack; the rulings leave none out at the scenario
  level); seed 20260930, three per service: Box 03, 05, 08; Calendar 03, 05, 06; Linear 05, 07, 08; Slack 01, 05, 08.
  So Muse's acceptance on these 12 is 12 of 12 by construction. For context, Phase 4 attempted 32 briefs: 29
  accepted, 2 rejected after their reader rounds (G4-BOX-02, G4-LIN-03), 1 ended by a failed writer call
  (G4-CAL-08).
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
- **Settings:** Qwen's reasoning at `medium` (`--effort medium`), the level OpenClaw's Qwen rounds run at. The server
  accepts xhigh (its default), medium or low; Claude Code's own default, "high", is refused. The served default was
  tried first and stopped (cycle 2). Muse's writers ran at Muse's "high": all 72 writer calls of Phase 4 record
  `reasoning_effort: high`. So the effort levels differ, a second stated confound. A writer reply may run to 64,000
  output tokens, lowered per request to the room the window has left (Claude Code's own cap for a model it does not
  know is 32,000; cycles 3 and 4) and a writer call to
  4 hours (the kit's limit, 3600 s, was sized for API models and would measure the host's throughput; the wall
  time is reported instead). Claude Code's compaction at the served window
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
  PI's criteria ([rulings.json](rulings.json), read by [rules.py](rules.py) in place of known_defects.json), and the
  clock rule for new scenarios (roadmap, 2026-09-28; as regen_01 and completion_01 apply it): every non-Calendar
  test starts at the moment its scenario's accepted version was written, or a day after its data's latest event if
  that is later. Muse's tests on these briefs ran on the real clock (2026-09-28), except G4-LIN-08's (2026-10-16).

## Results: generation

Twelve briefs, 23 facts. Muse's side is Phase 4's record (`autogen_02/runs/phase4_gen`), its review
(`autogen_02/eval/phase4_review.json`) and the PI's rulings; Qwen's is the attempt that counts per brief
([cases.py](cases.py): gen_02 for 3 briefs, gen_04 for 9) and my review ([eval/review.json](eval/review.json)).
Both reviews use one standard for "weak but valid" (review.json, `_standard`; [eval/data_scan.py](eval/data_scan.py)
checks both writers' data alike). Numbers: [eval/generation.json](eval/generation.json) ([compare_gen.py](compare_gen.py)).

| | Muse (Phase 4) | Qwen |
|---|---|---|
| Accepted | 12 of 12 (by construction of the pool) | 12 of 12 |
| Kept after review (valid or weak but valid) | 12 (2 weak but valid) | 12 (2 weak but valid) |
| Facts covered validly | 23 of 23 | 23 of 23 |
| Near misses: valid of declared | 44 of 44 | 43 of 45 |
| Scenario versions | 24 | 18 |
| Rounds: check (mechanical and replica) / reader | 11 / 1 | 3 / 3 |
| Rejected versions by stage | invalid JSON 5, replica 4, checks 2, reader 1 | reader 3, checks 1, replica 1, invalid JSON 1 |
| Near-miss families (writer's labels) | F0 9, F1 15, F2 3, F6 3, F7 6, F8 8 | F0 11, F1 11, F2 2, F6 1, F7 9, F8 11 |
| Plain (F0) share | 0.20 | 0.24 |
| Wording: natural / stilted / contrived | 7 / 3 / 2 | 7 / 3 / 2 |
| Requests with a test-only hint / with a role ambiguity | 2 / 1 | 2 / 4 |
| Writer wall time, counted attempts (per brief) | 73 min (2-15 min) | 11.3 h (25-112 min) |
| Writer output tokens | 283k | 482k |
| Writer cost (list) | $4.87 | $0 (self-hosted) |
| Reader calls, cost (list; billed) | 26, $1.22; $0.08 | 30, $1.31; $0.09 |

- **Validity and coverage are the same:** every brief accepted, every scenario kept, every fact covered by at least
  one valid near miss. Qwen's two flawed near misses (my rulings, for the PI to overrule) come from request wording
  that names a person without naming the role: "Maya Chen's onboarding checklist" also fits a file she created
  (G4-BOX-05, 9103), and "that Maya Chen uploaded" also fits a file whose first version she uploaded (G4-BOX-03, 4203).
  **Phase 4's review read Muse's scenarios on the same briefs the other way:** it ruled valid Muse's G4-CAL-06 near
  miss that holds an owner ACL grant under "Leo Park's calendar" (a possessive naming no role), and accepted Muse's
  G4-BOX-03 target, created by Jordan, as "that Maya Chen uploaded" on its uploader field. So Qwen's near misses are
  43 of 45 valid under my reading and 45 of 45 under Phase 4's; for the PI to settle. Coverage is 23 of 23 either
  way. The OpenClaw run runs both probes ([rulings_run.json](rulings_run.json): nothing left out at selection), and
  adjudication applies my rulings ([rulings.json](rulings.json)), so an overrule needs no re-run.
- **The pipeline's path differs:** Qwen's first versions were more often mechanically sound (1 invalid JSON against
  Muse's 5; no replica observability loop like Muse's 4 on G4-CAL-05), and the reader sent back 3 of its versions
  (two for an undeclared near miss, one for unnatural wording) against 1 of Muse's.
- **Near misses:** a similar mix; Qwen leans on F7 and F8 and uses fewer F1, F2 and F6. Qwen's labels are looser: F7
  on unordered values (conversation kinds, G4-SLK-05 and G4-SLK-08), F8 where the request names no number
  (G4-LIN-08), F0 for a creator-role substitute (G4-BOX-05).
- **Wording:** the same distribution; the contrived ones are the same briefs on both sides (G4-CAL-05 and G4-SLK-01,
  whose facts invite them). Qwen's requests carry more role ambiguities (4: owner or creator, first or current
  uploader, data owner or owner access, who assigned).
- **Data:** Qwen's seeds have more implausibilities (4 scenarios against 2; data_scan.json), one of which touches a
  tested condition (G4-LIN-05: two overlapping active cycles; weak but valid).
- **Cost and time:** the self-hosted writer costs nothing per token but is slow on the shared server: 25-112 minutes
  per brief at 7-13 tokens/s per stream (Qwen reasons 14-49k tokens in a design step), and the harness needed three
  stopped runs to find settings that work (cycles 2-4; the stopped attempts are kept, per brief, in
  generation.json). Muse's writers took 2-15 minutes.

## Results: exposure

**The run** (`runs/oc_01`, [run.py](run.py)): OpenClaw 2026.7.1-2 (the version of full_02 and full_03) on the
self-hosted Qwen through the proxy on 18778, 72 tests x 3 trials = 216 trials, the 600 s turn limit; 16 in flight for
its first 3 minutes, then 6 at the lead's request (cycle 6). No ruling applied at selection (rulings_run.json); my
rulings apply in adjudication. 216 trials completed; 2 ended at the time limit under host load by the lead's rule (11
and 12 requests, medians 33.8 and 41.6 s against 13 s for the run's median trial), were reclassified and rerun on the
quiet server at 11:30 (both then finished in 97 s; [eval/host_load_oc_01.json](eval/host_load_oc_01.json),
[reclassify_host_load.py](reclassify_host_load.py)); 2 ordinary timeouts (15 and 14 requests, medians 25.6 and 28.6 s)
are the solver's failures and expose nothing.

**The judge:** judge v2 on Muse, the regular suite's selection (every trial not mechanically clean, 20% of the clean
ones, the blind sample): 121 calls, $0.17 billed ($2.73 list). My 30 blind labels, each written before any verdict on
its trial ([eval/labels_oc_01.json](eval/labels_oc_01.json)): **29 of 30 agree; failures 7 of 7 in precision and in
recall, the same exposed facts 7 of 7.** The one disagreement is the probe of near miss 9103: artifact in my label
(under my ruling), incorrect in the judge's (Phase 4's reading). One verdict depended on the form the judge was told:
the rerun of FP-G4-CAL-06-I14-I15 t1, first judged without its form (my slip in the second pass), was "artifact";
judged again as a fact probe, "incorrect, skipped-check" (my label). The first verdict is kept beside the second.

**Exposure on the 23 brief facts** ([eval/exposure.json](eval/exposure.json), [compare_exposure.py](compare_exposure.py);
Muse's from openclaw_eval_01's full_02 for Box and full_03 for Calendar, Linear and Slack, under the PI's rulings; Qwen's
from runs/oc_01.adjudicated.json, under mine):

| | Muse's tests | Qwen's tests |
|---|---|---|
| Tests counted | 74 | 70 (2 probes of flawed near misses left out) |
| Tests exposing a fact (detect@3) | 19 | 24 |
| Facts exposed, detect@3 | 9 of 23 | 12 of 23 |
| Facts exposed, detect@1 | 7 of 23 | 8 of 23 |
| Covers / fact probes / probes exposing | 2 of 12 / 6 of 18 / 11 of 44 | 0 of 12 / 7 of 15 / 17 of 43 |

- **By fact:** 7 exposed by both; only Muse's: G4-BOX-03 A:File.modified_at, G4-LIN-07 R:Issue.cycleId; only Qwen's:
  G4-BOX-05 A:User.name, G4-CAL-03 D:primary, G4-CAL-05 A:CalendarListEntry.hidden and .summary_override, G4-CAL-06
  A:Calendar.time_zone. Together 14 of 23. The split (5 against 2) is within the noise of 3 trials (exact McNemar, p
  about 0.45).
- **Under Phase 4's reading** (my two rulings overturned): 72 tests, 28 exposing, the same 12 facts at detect@3 and 9
  at detect@1. Adjudication set aside 4 trials that acted only on the two near misses I ruled flawed.
- **Per brief** (tests, exposing, facts at detect@3; Muse then Qwen): BOX-03 8/5/3, 8/4/2; BOX-05 4/0/0, 4/1/1;
  BOX-08 5/3/1, 5/4/1; CAL-03 4/0/0, 6/3/1; CAL-05 6/0/0, 6/3/2; CAL-06 8/4/1, 8/5/2; LIN-05 5/0/0, 3/0/0; LIN-07
  10/1/1, 10/0/0; LIN-08 10/0/0, 6/0/0; SLK-01 5/4/2, 5/3/2; SLK-05 4/2/1, 5/1/1; SLK-08 5/0/0, 4/0/0. Linear exposed
  almost nothing on either side; Qwen's Calendar scenarios exposed where Muse's did not.
- **What the trials show about the readings:** in G4-BOX-03's cover, the solver first took "uploaded" as the creator
  and found two matches, then chose the target by the uploader field ("though Maya created it"); in G4-BOX-05's probe
  of 9103 it took "Maya Chen's" as the file she created and never read the owner; in G4-BOX-03's fact probe it took
  an open link as "company-wide … and beyond" (near miss 4206, valid in my review); in G4-CAL-06's fact probe it took
  the calendar list's "owner" role as "I own" (the near misses kept valid as Phase 4 kept Muse's). Evidence for the
  PI's rulings, not a basis for mine (a flaw is judged on the test).

**Confounds of the exposure comparison:**
- The runs are two days apart: Muse's tests ran on 2026-09-28 at 24 in flight; Qwen's on 2026-09-30 at 6 (16 for 3
  minutes) while regen_01's runs held the server.
- Clocks: Muse's tests ran on the real clock (2026-09-28) except G4-LIN-08's (2026-10-16); Qwen's at the moment each
  scenario was written (2026-09-30); Calendar on June 17, 2018 on both sides.
- The runner changed since full_03 (the openai backend, off for these runs; the R3 rule, which counts a timeout far
  short of the budget as infrastructure: no trial of this run ended so, and none of full_03's did, per its commit).
- The solver's model, harness and OpenClaw version are the same.

**Spend for the study:** readers $0.10 billed ($1.40 list) of $3; judge $0.17 billed ($2.73 list) of $3; the
self-hosted writer and solver $0.

**Evidence kept:** every writer call's prompt, result, transcript and event stream (the streams over 1 MB are
xz-compressed, `*-writer.events.jsonl.xz`, G4-LIN-05's in two parts that `xz -dc part1 part2` joins; they repeat
the transcripts), each stopped run's live transcripts, the
OpenClaw attempts as the runner writes them, and the judge's bundles and verdicts.

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

### Cycle 2 (2026-09-30, 02:24-03:14): generation at the served default, stopped

- `runs/gen_01_xhigh`: the first 4 briefs (G4-BOX-03, G4-BOX-05, G4-CAL-03, G4-SLK-01) at `--effort xhigh`,
  concurrency 4, with regen_01's OpenClaw run on the same server (its trials hold a 10-minute budget, so I kept my
  concurrency at 4). The server gave each writer stream about 10 tokens/s (measured from the connections' byte
  counts, about 126 bytes per streamed token, and from `/metrics`).
- Each writer read the docs and domain files (about 32-40k tokens of context), then reasoned in one step
  ([xhigh_steps.json](runs/gen_01_xhigh/xhigh_steps.json)):

  | Brief | First design step: output tokens | Reasoning (characters) | Ended with | Minutes |
  |---|---|---|---|---|
  | G4-CAL-03 | 29,621 | 100,300 | a Write of scenario.json | 34 |
  | G4-SLK-01 | 28,809 | 105,375 | a Grep (still exploring) | 37 |
  | G4-BOX-03 | 32,000 | 108,282 | Claude Code's output cap (`max_tokens`), no text, no tool call | 43 |
  | G4-BOX-05 | 32,000 | 117,049 | the same cap | 43 |

- G4-CAL-03's first writer call took 46 minutes (2,783 s); its scenario passed the mechanical checks and the replica
  pre-checks, and the cold reader sent it back (a near miss that fails two conditions). Its repair would have been
  another step of the same size, and the context (about 70k after the first call) would not have held two.
- Stopped at 03:14 (orchestrator and writers killed; each writer's live transcript and G4-CAL-03's scenario kept in
  its folder). G4-BOX-03 and G4-BOX-05 had written nothing ten minutes before the kit's 3600 s limit.
- Change for `runs/gen_02`: `--effort medium` and a 7200 s writer limit ([backend.py](backend.py)). Nothing else:
  the prompts, the checks, the reader and the round limits stay.

### Cycle 3 (2026-09-30, 03:15-04:33): medium effort, stopped at Claude Code's reply cap

- `runs/gen_02`: the briefs at `--effort medium`, concurrency 4, the same server load (7-13 tokens/s per stream).
- **Accepted, each at its first version** (no check or reader rounds): G4-BOX-05 (54 minutes), G4-CAL-03
  (62 minutes), G4-BOX-03 (73 minutes). Their largest writer replies were 30,103, 16,526 and 23,909 output tokens.
- **First design steps at medium:** 13,978 (G4-CAL-03), 16,006 (G4-BOX-03), 30,103 (G4-BOX-05) and 32,000 output
  tokens (G4-SLK-01, at Claude Code's cap, with nothing but reasoning: 122,000 characters). So medium halved some
  steps and not others.
- **What the cap does:** Claude Code adds a user message ("Output token limit hit. Resume directly — no apology, no
  recap of what you were doing. Pick up mid-thought if that is where the cut happened. Break remaining work into
  smaller pieces.") and continues. The reasoning stays in the prompt: Claude Code sends it back (G4-CAL-03's next
  step had 54,071 tokens of input after 39,956 plus its 13,978), and the server keeps it (a probe: 920 prompt tokens
  with an earlier reasoning block, 80 without). Still, G4-SLK-01's next step ran past 21,000 tokens without writing
  anything: it began again rather than picking up.
- **The long reasoning is design work, not a loop:** the capped 117,049-character block of cycle 2 has no repeated
  200-character chunk (585 of 585 distinct) and drafts the whole scenario, query included, before writing it.
- **What the cap changes in the request** (captured with a local listener, 2026-09-30): only `max_tokens` (32,000 or
  64,000); `thinking` stays `adaptive` with no budget, `output_config.effort` stays as set. So below the cap the
  generation is the same, and the three accepted briefs (none reached it) stand.
- Stopped at 04:33 (G4-SLK-01 77 minutes into its first call; G4-CAL-05, G4-LIN-05 and G4-SLK-05 23, 16 and 5
  minutes into theirs; live transcripts kept).
- Change for `runs/gen_03` (the 9 other briefs): a 64,000-token reply cap (`CLAUDE_CODE_MAX_OUTPUT_TOKENS`, which fits
  the window after the writer's reading of about 40k) and a 4-hour writer limit.

### Cycle 4 (2026-09-30, 04:36-05:25): the 64,000-token cap without the room, stopped; the window relay

- `runs/gen_03`, the 9 other briefs at the 64,000-token cap. Two first writer calls failed within 37 minutes (G4-LIN-05,
  G4-CAL-05): `API Error: 400 This model's maximum context length is 131072 tokens. However, you requested 64000
  output tokens and your prompt contains at least 67073 input tokens`. The server refuses any request whose prompt and
  max_tokens together pass the window, and Claude Code sends the same max_tokens whatever the prompt's size (it
  takes this model's window for 200,000). Once a writer's context passed 67,072 tokens (about 40k of reading and one
  long step), every request failed, repair rounds included. (Claude Code's own 32,000 fits: prompts up to 99k.)
  G4-SLK-05 and G4-SLK-01 finished their first calls (35 and 37 minutes); stopped at 05:13.
- The server's message is no guide to the prompt: its "at least N input tokens" is the window less the output asked
  for, plus one.
- **The window relay** ([backend.py](backend.py)): the writer's requests go through a relay in the generation
  process, unchanged, to the server. When the server refuses one for that reason, the relay counts the prompt with the
  server's own counter (`/v1/messages/count_tokens`), lowers max_tokens to the window less the prompt less 256, and
  sends it again; each lowering is logged (`runs/gen_NN/clamps.jsonl`). Tested: a 731-token prompt asking 131,000
  (lowered to 130,085) and a 115,533-token prompt asking 64,000 (lowered to 15,283, streamed through); and Claude Code
  through it with every request lowered (`runs/probe_03_relay`: two turns, the resume, the edit, all as before).
- `runs/gen_04`: the 9 briefs again, the relay on. [cases.py](cases.py) takes each brief's accepted scenario from
  gen_02 or gen_04; no request of gen_02's three was refused, so the relay would have passed them unchanged.

### Cycle 5 (2026-09-30, 05:19-07:55): generation with the relay; the review

- `runs/gen_04`: all 9 accepted: G4-SLK-05 (31 min), G4-CAL-05 (51, one check round), G4-SLK-01 (59, one reader
  round), G4-BOX-08 (27), G4-CAL-06 (56, a replica and a reader round), G4-LIN-05 (114), G4-LIN-07 (68, one reader
  round), G4-SLK-08 (57, one invalid-JSON round), G4-LIN-08 (67). The relay lowered max_tokens on requests past a
  67k prompt (clamps.jsonl); none was refused after it. G4-LIN-05's first design step ran to 48,973 output tokens,
  past the old 32,000 cap.
- My review, scenario by scenario as each was accepted ([eval/review.json](eval/review.json)), before any solver run;
  the wording rubric fixed on Muse's twelve before any Qwen scenario existed ([eval/wording.json](eval/wording.json)).
  The one standard for "weak but valid" was set after a plausibility scan of both sides' data
  ([eval/data_scan.json](eval/data_scan.json)); it moved Qwen's G4-SLK-01 to weak but valid, as Muse's is.
- The suite ([suite.py](suite.py)): 72 tests (12 covers, 15 fact probes, 45 probes; Muse's scenarios gave 74), 205 ids
  made opaque, clocks at the written moment for Box, Linear and Slack. The rulings leave out the 2 probes of the
  flawed near misses at run time ([rulings.json](rulings.json), from the review by
  [rulings_from_review.py](rulings_from_review.py)).
- The blind sample for the judge: 30 of the 216 trial slots, drawn from the cases folder with seed 20260930 before any
  run ([eval/blind_oc_01.json](eval/blind_oc_01.json)).

### Cycle 6 (2026-09-30, 07:58-): the OpenClaw run

- `runs/oc_01` started at 07:58 at 16 in flight ([run.py](run.py); OpenClaw 2026.7.1-2, the version of full_03; the
  self-hosted Qwen through the proxy on 18778; the 600 s turn limit). At 08:01 the lead asked for 6 in flight: the
  self-host carries regen_01's runs at 12, its priority, and higher totals had produced host-load timeouts. Stopped
  (the runner, then its 12 OpenClaw process groups; `runs/oc_01_children_at_stop.txt`): 1 trial had completed and is
  kept, 16 were cut off. Restarted at 08:02 at 6 with `--retry-infrastructure`, which redoes the cut-off attempts
  (new attempt folders; the old ones stay) and never a completed one. The trial plans (`t*/plan.json`, written once)
  still say 16. The cut-off attempts left their AgentDiff environments, templates and OpenClaw state directories
  behind; [cleanup_cut_off.py](cleanup_cut_off.py) removed them with the runtime's own calls after the run (15
  environments, 15 templates, 15 state directories; the 16th attempt had stopped in preflight and recorded none;
  `runs/oc_01_cleanup.json`).
- The lead's rule for host load: a trial that times out with few requests, each over 30 s, is marked "timeout under
  host load" and kept apart for a quiet rerun.
- The run ended at 10:39. [host_load.py](host_load.py) put the rule as "at most 12 requests with a median over 30 s"
  before reading any timed-out trial; 2 of 4 met it. After regen_01's run ended (11:29, 1 request a minute on the
  limiter) they were rerun (11:30-11:33). Judge pass 1 (117 trials, the selection less those 2) ran 10:40-11:25;
  pass 2 judged the 2 reruns, then again with their form. Scoring (`phase4 score`), adjudication
  ([adjudicate.py](adjudicate.py)) and the comparison followed.
