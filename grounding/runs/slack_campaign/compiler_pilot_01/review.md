# W01 fresh-environment compilation

W01 compiled successfully after one automatic binding repair and one manually
identified card-annotation repair. Its seed, request and selector were unchanged
across those repairs. This is one development example, not an autonomous success
rate. The subsequent [solver and evaluator run](execution_review.md) succeeded:
exactly two requested reactions, grounding demonstrated correct, no failure exposed.
The construction-stage findings and costs below remain as originally recorded.

## Input and resulting world

The input is the unchanged [reflected W01 sketch](../writer_pilot_04/W01/writer/turn-02/output.md).
The adapter saves its [exact assignment and source hash](W01/input.json) and extracts
the [final story](W01/story.md), excluding the writer's self-review commentary.

Route: **Message → Reaction → User**, resolution mode: **multiple**, two matches.

> Add a 🚀 to the messages that Priya reacted to with raised_hands.

The [compiled case](W01/case.json) contains one workspace, five users, one public
channel, five workspace memberships, five channel memberships, eight messages and
nine reactions. The two filler messages introduce no additional matches.

| Story row | Concrete message text | Reactions | Python selection |
|---|---|---|---|
| M1 | Rocket specs draft - initial thoughts on payload design | Priya 🙌 | Match |
| M2 | Budget review for Q3 initiatives | Priya 🙌; Diego 👀 | Match |
| M3 | Vendor contract needs signature by Friday | Priya 👀 | Excluded: wrong emoji |
| M4 | Timeline update: launch pushed to next month | Diego 🙌 | Excluded: wrong person |
| M5 | Design mockup for new landing page | None | Excluded: missing reaction |
| M6 | Marketing plan for spring campaign | Priya 👀; Diego 🙌 | Excluded: different reaction records |
| Filler | Standup notes for today | Alex 👍 | Excluded |
| Filler | Lunch plans anyone? | Sara ❤️ | Excluded |

The [locked selector](W01/locked_selector.json) joins messages to reaction records
and then reacting users. Both conditions must hold in that same joined tuple;
M6 therefore cannot become a match by mixing two reactions. Selection covers all
eight messages, without a target-ID filter. Priya has one matching profile in this
world, concretely named Priya Sharma.

The final card resolves to `1700000001.000001` and `1700000002.000001`.
Its computation set is `[[messages.message_id]]`, supplying the message reference
for the new reaction. Written attributes are `message_reactions.message_id` and
`message_reactions.reaction_type`; the requested rocket is a prompt constant, and
the runtime supplies the actor. The single task line retains the exact request.

## What happened

1. [First compiler answer](W01/compiler/turn-01/answer.txt) produced the correct
   seed and selector, but used null referents for all four negative rows even
   though their message records existed. The [fixed check rejected it](W01/checks-1.json).
2. A [native conversational follow-up](W01/compiler/turn-02/request.json) corrected
   only those bindings. Its [thinking summary](W01/compiler/turn-02/thinking.txt)
   identifies that null means a genuinely missing root, not a nonmatching root.
   [Mechanical checks passed](W01/checks-2.json).
3. The [independent first review](W01/review-2.json) accepted validity but missed
   incorrect card annotations. My manual review found that selection fields had
   been listed as separate change-computation alternatives and the new reaction's
   message reference was missing from written attributes. This was an instruction
   omission: the compact compiler contract named these fields without defining
   their existing meanings precisely.
4. I added those existing definitions to the shared compiler/reviewer contract.
   The [manual feedback](W01/manual_followup/feedback.txt) was sent as turn three
   of the same compiler conversation, preserving prior responses. Its
   [answer](W01/compiler/turn-03/answer.txt) changed only annotation, and its
   [thinking summary](W01/compiler/turn-03/thinking.txt) gives the correct field
   distinction. [Final checks](W01/checks-3.json) and a
   [fresh independent review](W01/review-3.json) passed.

The [original automatic result](W01/automatic_summary.json) and all intermediate
cases remain saved. The [final summary](W01/summary.json) explicitly records manual
intervention. The generic checker was also tightened to reject any null referent
whose support already lists a root record; a regression test covers this. That
change was not needed to reject the original all-null submission.

## Native checks and remaining limits

The [native load/read summary](W01/native_check_02/summary.json) reports a successful
PostgreSQL load, 19 successful read probes, unchanged state, and the same two
matches after loading. [API observations](W01/native_check_02/visibility.json)
mechanically establish the needed fields and relationships and exclude all four
[declared negatives](W01/native_check_02/visibility_check.json). This check used
case-2's seed, which is byte-for-byte identical to the final seed. It used no model,
solver or requested writes. The disposable database schema was cleaned up.

The first native attempt encountered a harness compatibility error with the
installed Starlette version; its [failure record](W01/native_check/summary.json)
is retained. Switching to supported `add_middleware` fixed the harness. The local
backend Python environment was used for these native checks; the separate model
environment lacks Starlette. The backend environment needed boto3 installed because
the campaign's shared imports load it even for this model-free path.

Validity of W01's selection is strong: all specified distinctions survived, with
no new matches. I assess the challenge as **adequate**, not demonstrated difficult:
the relevant information fits in one small history. Two quality qualifications:

- “Rocket specs draft” weakly echoes the requested 🚀. This was inherited from
  the writer, not introduced by compilation. The first reviewer flagged it but
  incorrectly called it a compilation issue and referred to a single positive;
  there are two. The second reviewer rated the unchanged world “strong” without
  mentioning it. This is reviewer variation, not a quality improvement.
- Numeric message timestamps encode a different date from `created_at`. There is
  no temporal criterion in this request, so selection is unaffected, but this
  is an instantiation consistency issue to fix before temporal-case compilation.

Mechanical checks do not prove that an arbitrary natural-language condition was
faithfully translated. The reviewer missed the annotation issue here. The short
definition correction is in place, but a fresh case is needed to test whether it
prevents recurrence without manual help. This pilot does not justify scaling yet.

## Verification and cost

Compiler, validation, Bedrock-conversation and runtime tests: **34 passed, two
opt-in external integration tests skipped**. The separate W01 native load/read
check described above passed. The source hash is unchanged, all three seeds and
selectors agree, and repairs used the original conversation history.

[Native usage ledger](W01/usage_ledger.json) and [totals](W01/usage_summary.json):

| Scope | Model calls | Estimated cost |
|---|---:|---:|
| Automatic compiler + binding repair + review | 3 | $0.3466 |
| Manual annotation follow-up + independent re-review | 2 | $0.2560 |
| Total | 5 | **$0.6026** |

Total native token counts: 37,588 uncached input, 49,357 cache-write, 12,723
cache-read, and 20,064 output. Explicit prefix caching was used; the immediate
compiler repair hit the cache. The later manual follow-up recreated its prefix
after the five-minute cache window. Compiler calls took 42, 50 and 30 seconds;
review calls took 36 and 31 seconds. Dollar figures use the recorded historical
rates; Bedrock returns token usage, not a billed dollar amount. Earlier writer
pilot costs are excluded from these incremental compilation costs.
