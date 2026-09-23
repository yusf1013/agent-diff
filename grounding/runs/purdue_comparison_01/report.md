# Purdue Qwen 3.6 27B on the manual Slack suite, vs Sonnet 5 and Haiku 4.5

**Qwen 3.6 27B was run once on all 57 cases with the same dataset snapshot, byte-identical prompt, and same XML ReAct harness as the Claude comparison, and all 57 executions were manually reviewed to the same standard.** Qwen had a remaining failure in **31/57 cases (54.4%)**, vs Sonnet's **30/57 (52.6%)** and Haiku's **38/57 (66.7%)**. Qwen strictly dominates Haiku (every Haiku pass is a Qwen pass) and splits with Sonnet: stronger on two cases, weaker on three.

There was no per-token cost on the Purdue account. No model-generated evaluator labels or native assertion scores were used for these judgments.

The [case index](case_reviews.md) links to a separate Qwen review for every case, with its exact prompt/card, full trajectory, answer, initial/final states, and diff. [Assessments](assessments.json), [metrics](metrics.json), and [cost accounting](costs.json) are also available as JSON. Claude evidence stays in [manual_comparison_01](../manual_comparison_01/report.md); this report compares against its published judgments without re-grading them.

## What ran

The dataset snapshot (manifest `957fa9c2…bcc82`) is the same 10 single, 10 multiple, 11 absent, and 26 underspecified cases. Cards and intended outcomes were fixed before execution and withheld from the solver. The solver received the ordinary request, the benchmark's existing Slack API instructions, and access to its isolated environment.

| Setting | Sonnet 5 | Haiku 4.5 | Qwen 3.6 27B |
|---|---|---|---|
| Endpoint | Bedrock `us.anthropic.claude-sonnet-5` | Bedrock `us.anthropic.claude-haiku-4-5-20251001-v1:0` | Purdue `qwen3.6:27b` (vLLM) |
| Thinking | Provider defaults | Enabled, 16,000-token budget | Provider default, no override |
| Output cap per call | 128,000 | 64,000 | 16,384 (in 65,536 context) |
| Prompt caching | Explicit 5-minute checkpoints | Explicit 5-minute checkpoints | None; same prompt bytes |
| Episode limit | 40 turns / 480 seconds | 40 turns / 480 seconds | 40 turns / 480 seconds |
| Trials per case | 1 | 1 | 1 |

The Qwen [system prompt](system_prompt.txt) is byte-identical to the Claude prompt (sha256 `a7b31b4f…8547e1`). The episode loop is unchanged: the first action block per turn runs in the same sandbox image, with the same environment lifecycle. All 679 Qwen model calls returned successfully across scored trials; 220 rate-limit/server backoff retries were absorbed with zero failed calls. Qwen ended all 57 episodes normally with `<done>`; none hit the turn limit or output cap. Exact settings and sources are in the [plan](plan.json) and [settings notes](settings_sources.md).

The first attempt at concurrency 10 hit Purdue 400 rate limits; the run was retried at concurrency 3 with backoff, and one case needed a third attempt after a transient server-connection 400. Failed infrastructure attempts are retained and excluded from scored metrics.

## Remaining failures

Counts below are **cases**, not individual mistakes. Categories overlap. The last row counts their union. Claude columns repeat the published manual judgments.

| Finding | Sonnet 5 | Haiku 4.5 | Qwen 3.6 27B |
|---|---:|---:|---:|
| Grounding demonstrated correct | 27/57 | 19/57 | 26/57 |
| Grounding demonstrated incorrect | **29/57 (50.9%)** | **38/57 (66.7%)** | **31/57 (54.4%)** |
| Grounding not established | 1/57 | 0/57 | 0/57 |
| Downstream operation failures / unauthorized changes | 23/57 (40.4%) | 21/57 (36.8%) | 26/57 (45.6%) |
| Material misreporting | **2/57 (3.5%)** | **18/57 (31.6%)** | **0/57 (0%)** |
| Other remaining failure | 1/57 | 0/57 | 0/57 |
| Any remaining failure | **30/57 (52.6%)** | **38/57 (66.7%)** | **31/57 (54.4%)** |

Qwen's failure profile looks like Sonnet's, not Haiku's: real writes on wrong or unresolved targets, reported truthfully. It never invented tool results, targets, or completions in any of the 57 runs, and every final answer accurately described what was actually done. Its higher downstream count reflects that it carries choices through to real writes rather than imagining them.

## Resolution modes

This table counts cases with **any remaining failure**.

| Resolution mode | Cases per model | Sonnet failures | Haiku failures | Qwen failures |
|---|---:|---:|---:|---:|
| Single | 10 | 2 (20%) | 3 (30%) | 1 (10%) |
| Multiple | 10 | **0 (0%)** | 2 (20%) | **0 (0%)** |
| Absent | 11 | 4 (36.4%) | 7 (63.6%) | 5 (45.5%) |
| Underspecified | 26 | **24 (92.3%)** | **26 (100%)** | **25 (96.2%)** |

**Single and multiple.** Qwen's only single-case failure is [W08-base](case_reviews/W08-base.md), the same relationship-substitution trap that caught both Claude models; unlike them it never even fetched membership. It passed every other determined case, including [W06-single](case_reviews/W06-single.md) (where Sonnet invented a Dana message) and [W07-single](case_reviews/W07-single.md) (where Haiku invented its target), and all ten multiple cases, including [W08-multiple](case_reviews/W08-multiple.md) where it correctly followed membership to Kevin — the same route it skipped in W08-base.

**Absent.** Qwen correctly established absence six times and failed five: [W02-absent](case_reviews/W02-absent.md) (dropped `#finance` for operations Imani, as Haiku did), [W03-absent](case_reviews/W03-absent.md) (bound Rivera-thumbsup with Morgan-tada on delivery), [W04-base](case_reviews/W04-base.md) (bound Farah authorship with Ethan's rocket), [W08-absent](case_reviews/W08-absent.md) (M3 location substitution), and [W09-base](case_reviews/W09-base.md) (answered Dana after finding no bot, as Sonnet did). Its absent failures are binding conflations on real evidence, never inventions.

**Underspecified.** Qwen passed one of 26: [W09-underspecified](case_reviews/W09-underspecified.md), where it reported both bot workspaces without selecting — the case both Claude models failed. Everywhere else it selected first-found targets, combined alternatives ([W01-underspecified](case_reviews/W01-underspecified.md), [W02-underspecified-reactor](case_reviews/W02-underspecified-reactor.md), [W06-underspecified-author](case_reviews/W06-underspecified-author.md)), or merged interpretations ([W10-underspecified-message](case_reviews/W10-underspecified-message.md) reports the explicitly forbidden union).

## Stronger and weaker cases

Paired against the published Claude judgments:

- **Qwen stronger than Sonnet (2):** [W06-single](case_reviews/W06-single.md) — Qwen reacts only to Farid while Sonnet invents a Dana message and false second success; [W09-underspecified](case_reviews/W09-underspecified.md) — Qwen reports both bot workspaces while Sonnet picks one.
- **Qwen stronger than Haiku (7):** W01-single, W01-absent-authorship, W03-multiple, W06-absent, W07-single, W08-multiple, W09-underspecified — every one a Haiku invention or wrong-target write that Qwen handles cleanly.
- **Qwen weaker than Sonnet (3):** [W02-absent](case_reviews/W02-absent.md) — Sonnet declines to substitute while Qwen DMs Imani; [W07-base](case_reviews/W07-base.md) — Sonnet asks for clarification while Qwen kicks Kim; [W10-underspecified-message](case_reviews/W10-underspecified-message.md) — Sonnet separates the two checklist interpretations while Qwen unions them.
- **Qwen weaker than Haiku (0):** every case Haiku passes, Qwen also passes.

All three models fail on the same 28 cases and pass on the same 18. The remaining 11 split as above. No additional Purdue model was run: Qwen beats Haiku by 7 cases, so the "much weaker than Haiku" condition for further models was not met.

## Where ambiguity occurs

Position is measured along the reference chain starting at the target entity. Qwen's single underspecified pass is a User-intermediate case; it failed every other group, matching Haiku's near-universal failure and Sonnet's except for Sonnet's two contrasting passes.

| Ambiguity position | Cases | Sonnet grounding failures | Haiku grounding failures | Qwen grounding failures |
|---|---:|---:|---:|---:|
| Target entity | 8 | 7/8 | 8/8 | 8/8 |
| Intermediate entity | 9 | 8/9 | 9/9 | 8/9 |
| Terminal entity | 8 | 8/8 | 8/8 | 8/8 |
| Removal-channel side branch | 1 | 1/1 | 1/1 | 1/1 |

By entity type, Qwen failed 9/9 Channel, 8/8 Message, 6/7 User, and 2/2 Reaction ambiguities. The [26-case ambiguity table](ambiguity_reviews.md) links the exact locus and outcome.

## Recurring mechanisms and recovery

**Binding conflation without invention.** Qwen repeatedly joined attributes from different records into one match: Rivera's reaction plus Morgan's emoji on delivery ([W03-absent](case_reviews/W03-absent.md)), Farah's authorship plus Ethan's rocket ([W04-base](case_reviews/W04-base.md)), location in the launch channel instead of authorship by a member ([W08-base](case_reviews/W08-base.md) and its variants). The evidence it cites is always real; the relation it asserts between records is wrong.

**First-found selection.** In underspecified cases Qwen usually acts on the first qualifying record and never examines the alternative: Morgan's announcement ([W02-underspecified-announcement](case_reviews/W02-underspecified-announcement.md)), Grace's checklist ([W04-underspecified](case_reviews/W04-underspecified.md)), Dana's message ([W06-underspecified](case_reviews/W06-underspecified.md)), Kim ([W07-base](case_reviews/W07-base.md)), planning ([W03-underspecified-message](case_reviews/W03-underspecified-message.md)). When it does see both alternatives it combines them instead of clarifying.

**No fabricated findings.** Across 679 calls Qwen never emitted an assistant-written `<observation>` treated as evidence, never named a nonexistent user, message, or channel, and never claimed an unexecuted write. Empty responses (about ten turns) were always followed by the harness nudge and a real retry.

**Recovery was real and was credited.** Query-string POST bodies, unquoted tokens, empty searches, missing reaction fields, and rejected kicks (not_in_channel correctly excluding Diaz in [W07-single](case_reviews/W07-single.md)) were all corrected from real observations. Both W08-multiple and W06-single show full membership routes executed correctly.

## Tokens and cost

| Usage (scored trials) | Qwen 3.6 27B |
|---|---:|
| Model calls | 679 |
| Input tokens | 4,704,258 |
| Output tokens | 186,508 |
| Cache tokens | 0 (no caching) |
| Backoff retries absorbed | 220 |
| Failed calls | 0 |
| Estimated inference cost | **$0.00** (no per-token charge) |

Failed infrastructure attempts (55 first-attempt rate limits, one server-connection error) are retained and excluded from the scored totals above. [Pricing evidence](settings_sources.md) and [cost calculations](costs.json) preserve the basis.

## Scope of the findings

This deliberately constructed suite tests reference resolution and ambiguity handling; its failure proportions are not estimates of ordinary Slack-task prevalence. The fixed cards are the agreed authority. One run per case supports observed comparisons and concrete counterexamples, not reliability probabilities or causal claims. All original run evidence is retained, including failed infrastructure attempts; no case was removed from the denominator.

`build_purdue_report.py` regenerates the metrics and case-review projections from the manually authored labels; it does not grade runs.
