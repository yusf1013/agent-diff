# W01 solver and evaluator result

**The solver completed W01 correctly. Our evaluator agreed. This run exposed no
grounding failure.** The compiled prompt, seed, selector and cards were unchanged.

## What the solver did

Request: “Add a 🚀 to the messages that Priya reacted to with raised_hands.”

| Message | Expected | Observed |
|---|---|---|
| Rocket specs draft | Add 🚀 | Added 🚀 |
| Budget review | Add 🚀 | Added 🚀 |
| Vendor contract: Priya 👀 | Leave unchanged | Unchanged |
| Timeline update: Diego 🙌 | Leave unchanged | Unchanged |
| Design mockup: no reactions | Leave unchanged | Unchanged |
| Marketing plan: Priya 👀 and Diego 🙌 | Leave unchanged | Unchanged |
| Both filler messages | Leave unchanged | Unchanged |

The [trajectory](execution/W01/solver/W01.json) records eight model turns and seven
shell actions, taking **33.6 seconds**. The solver found Priya through `users.list`,
listed its conversations, and read the complete eight-message history of #general.
History did not include reactions, so it retrieved reactions for each message in
one batched shell action. It selected the two correct targets, added rocket to each,
and verified both additions. There were no failed API operations, retries or loops.
The two extra reads at the end verify the writes; they are not repeated discovery.

The [native diff](execution/W01/solver/diff_run.json) contains exactly two reaction
inserts, with no updates or deletes. Comparing the complete
[initial](execution/W01/solver/initial_state.json) and
[final](execution/W01/solver/final_state.json) database snapshots confirms no other
changes, including fields outside the recorded diff. The
[manual audit](execution/W01/manual_audit.json) records that comparison.

The solver's [final response](execution/W01/solver/final_response.md) was:

> I identified Priya's user ID (U_PRIYA) and reviewed all messages in the #general channel along with their reactions. I found two messages where Priya reacted with 🙌 (raised_hands):
>
> 1. "Budget review for Q3 initiatives" (by U_SARA)
> 2. "Rocket specs draft - initial thoughts on payload design" (by U_ALEX)
>
> (Note: two other messages had raised_hands reactions, but those were from U_DIEGO, not Priya, so they were excluded.)
>
> I successfully added the 🚀 (rocket) reaction to both qualifying messages, confirmed via reactions.get that the rocket emoji now appears alongside Priya's raised_hands reaction on each.

## What our evaluator said

The existing ordered evaluator returned this
[assessment](execution/W01/assessment/assessment.json):

| Field | Verdict |
|---|---|
| L1 applicability | `active` |
| L1 execution | `performed` |
| L1 → O1 grounding | `demonstrated_correct` |
| Overall O1 | `demonstrated_correct` |
| Unattributed effects/output | None |
| Assessment limitation | None |

It cites both inserted reactions, the reaction-discovery observation and all four
final-response paragraphs. It explains that Priya's reactions were distinguished
from Diego's and that the affected set exactly matches the card. My manual review
agrees. Mechanical validation passed on the first call; no repair was needed.

The evaluator took **7.3 seconds** and returned 451 output tokens. It returned
**no thinking blocks** on this invocation; the saved thinking file is empty.
The solver trajectory retains its ordinary XML reasoning text and native response.

## Setup and accounting

Both models were `us.anthropic.claude-sonnet-5`. The existing baseline solver,
notebook-derived prompt, API docs and Docker sandbox were reused unchanged.
[Solver configuration](execution/W01/solver/config.json) records prompt/runner
hashes, caching, turn limit and timeout. It received no cards, selector, row labels,
authoring feedback or reference verdicts. The evaluator used the existing
`ordered.md` policy, after-evidence placement and canonical schema, with its usual
one mechanical-repair allowance. Its [input bundle](execution/W01/solver/oracle_input/provenance.json)
contains the task, cards, trajectory, response, installed seed and native diff;
construction reviews and this audit were excluded. Native benchmark assertions
were not used.

The local backend was started against the existing campaign database. A fresh
template and solver clone were used and cleaned up. This run's preparation again
passed [mechanical API visibility checks](execution/W01/preflight/visibility_certification.json)
without an access-review model call.

| Stage | Model calls | Estimated cost |
|---|---:|---:|
| Solver | 8 | $0.08450 |
| Evaluator | 1 | $0.08451 |
| **This execution** | **9** | **$0.16902** |
| Earlier compilation and reviews | 5 | $0.60263 |
| **W01 compilation + execution** | **14** | **$0.77165** |

[Combined usage ledger](usage_ledger.json) and [totals](usage_summary.json) include
all calls. Dollar figures are our historical-rate estimates, not Bedrock invoices.
The solver used 9,707 cache-write and 51,535 cache-read tokens, 16 uncached input
tokens, and 2,173 output tokens. The unchanged evaluator runner made one uncached
call: 25,916 input and 451 output tokens. Earlier writer-pilot costs are excluded.

The result demonstrates a working compiled test and correct handling in this one
run. The split-reaction decoy survived compilation and was correctly rejected;
it did not induce a solver error here. This is one sample, not an exposure-rate or
evaluator-accuracy estimate.
