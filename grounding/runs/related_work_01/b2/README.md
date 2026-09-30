# B2: the abstention and feasibility suites' categories, projected onto our boundary classes

*related_work_01, 2026-09-30, for the lead. The arm B2 of [report.md](../report.md) §5.4: reading only, no runs.
Counts come from each suite's paper or data files, fetched 2026-09-30 (sources at the end).*

## What it produces

A map from every category of seven established suites that tests "the agent should not (or cannot) do this" onto our
five capability-boundary classes, with item counts, plus the categories that land in our policy modes instead. The
table is also in [projection.json](projection.json).

**Our space, for reference** (93 faithful boundary elements, `grounding/runs/boundary_02/space.json`): read-only field
32, permission 31, no operation 15, state precondition 13, value limit 2. Each is a change the service itself refuses
this actor (faithful: the replica refuses as the real service does).

## The projection

| Suite | Category (their definition) | Items | Our boundary class | Or our policy mode |
|---|---|---:|---|---|
| AgentAbstain | S5 Insufficient tool capability ("available tools fundamentally cannot achieve the goal; visible from the tool inventory") | 34 pairs | **no operation**, of the tool-withheld kind | – |
| AgentAbstain | S1 Missing critical parameter | 39 pairs | – | underspecified, of an argument, not a record |
| AgentAbstain | S2 Ambiguous action; S3 Conflicting constraints; S4 High stakes; S6 Tool failure; S7 Conflicting evidence; S8 Emergent risk | 30, 32, 31, 34, 30, 33 pairs | – | – (action ambiguity, logical infeasibility, confirmation, runtime failure, evidence, safety) |
| ToolBeHonest | Missing necessary tools (a golden tool removed; 3 subtasks) | 150 unsolvable | **no operation**, tool withheld | – |
| ToolBeHonest | Potential tools (an OS or web tool the task does not permit) | 100 unsolvable | **permission**, by the task's instruction, not by the service | – |
| ToolBeHonest | Limited functionality tools (a function removed, or a constraint added) | 100 unsolvable | **no operation** or **value limit** | – |
| BFCL (multi-turn) | Missing functions ("no available function can fulfill the user request") | 200 | **no operation**, function withheld | – |
| BFCL (multi-turn) | Missing parameters | 200 | – | underspecified, of an argument |
| BFCL | Irrelevance, live irrelevance (no provided function applies) | 239 + 884 | no operation, loosely: many are questions needing no tool | – |
| When2Call | "Unable to answer" with the tools provided | 1,295 | **no operation**, tool not offered | – |
| When2Call | "Request for information" (a required parameter missing) | 1,062 | – | underspecified, of an argument |
| FeasiGen | Critical tools masked, on BFCL, StableToolBench, API-Bank and τ-bench tasks | 1,036 | **no operation**, tool withheld | – |
| ToolSandbox | Insufficient Information (a needed tool withheld on purpose; a few with a device state: cellular off, low battery) | 28 base scenarios | **no operation**, tool withheld (a few with a device state) | – |
| τ-bench | Intentionally impossible tasks (for example, changing a non-refundable ticket): 38% of airline, 6% of retail | about 19 of 50, 7 of 115 | none: **policy-forbidden** (the API allows it, the domain policy forbids) | – |

## What it shows

- **Nearly every boundary-type item in these suites is one class: "no operation" of the tool-withheld kind.** 2,843
  items (34 + 150 + 100 + 200 + 1,295 + 1,036 + 28, before the 1,123 loose irrelevance items) withhold or never offer
  a tool the task needs. In the real service the operation exists; the limit is the agent's configuration. Ours are
  refusals the service itself makes (no API to change a message's author, a read-only creation date, a bot that may
  not edit another user's message).
- **Three of our five classes have no counterpart at all:** read-only fields (32 of our 93), permissions the service
  enforces (31), and state preconditions (13): **76 of our 93 faithful elements.** The nearest items are
  ToolBeHonest's potential tools (a permission set by the task's instruction) and ToolSandbox's device states.
- **A class we lack:** τ-bench's policy-forbidden actions, which the service allows and the domain rules forbid. Our
  space is derived from what the service refuses, so a normative boundary ("the policy says no") is outside it. Worth
  a sentence in the paper, and a question for the PI whether the boundary space should include policy documents when a
  service has them.
- **The missing-information categories** (AgentAbstain S1, BFCL missing parameters, When2Call request for
  information: 1,301 items) are the nearest counterparts of our underspecified mode, but they concern an argument's
  value, not which record is meant. **None names a presupposed-absence condition.**
- **None of these suites is on our services**, so B2 cannot be run; it places our boundary space in the literature and
  motivates B1 (masking an operation on our replicas reproduces their dominant class on our services).

## What a later session would run, and the cost

Nothing: B2 is a reading result. If the PI wants a behavioural comparison of the tool-withheld class, B1 is that
comparison on our services.

## Sources (fetched 2026-09-30)

- AgentAbstain: arXiv 2607.10059, Table 4 ("Pair counts by scenario and deliverable semantics"; totals 39, 30, 32, 31,
  34, 34, 30, 33 for S1–S8; 263 in all) and §2 for the S5 definition.
- ToolBeHonest: arXiv 2406.20015, §3.3 and Table 1: 7 subtasks with 50 solvable and 50 unsolvable samples each (missing
  necessary tools: 3 subtasks; potential tools: OS and web; limited functionality: 2).
- BFCL: the data files `BFCL_v4_multi_turn_miss_func.json` (200 lines), `BFCL_v4_multi_turn_miss_param.json` (200),
  `BFCL_v4_irrelevance.json` (239), `BFCL_v4_live_irrelevance.json` (884) in
  <https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard/bfcl_eval/data>; category
  definitions from <https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html>.
- When2Call: arXiv 2504.18851, the dataset table (test split: tool call 1,295; request for information 1,062; unable to
  answer 1,295).
- FeasiGen: arXiv 2605.28532, Table 1 ("Statistics of generated infeasible tasks": 445, 300, 184, 107; total 1,036).
- ToolSandbox: `tool_sandbox/scenarios/insufficient_information_scenarios.py` in
  <https://github.com/apple-aiml-research/ToolSandbox> (28 `ScenarioExtension` entries); the category's definition in
  arXiv 2408.04682 ("by withholding a tool that would be needed for the task").
- τ-bench: ABC, arXiv 2507.02825 ("τ-bench contains intentionally unsolvable tasks—38% of the airline subset and 6% of
  the retail subset"); subset sizes 50 and 115 (ToolSandbox's Table 4 lists τ-bench's 165 test cases).
