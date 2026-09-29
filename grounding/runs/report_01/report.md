# Automated fact-discrimination tests for tool-using agents: evaluation and results

*A stub for the evaluation and results sections of a paper, written 2026-09-29 from the committed runs. It covers
the experiments, what they show and what they do not. There is no introduction, background or related work. Every
table names its source: a script in [kit/](kit/) and the JSON it writes into [numbers/](numbers/), or a run record.
Rows marked "–" or "not measured" are measurements not yet made.*

## 0. Setup

### 0.1 What is tested

An agent receives one natural-language request to change something in a business service: Box, Google Calendar,
Linear or Slack. It works through the service's API. Each request identifies its record by several conditions, for
example "Add the tag launch-ready to the PDF in the Launch Assets folder with a top-level comment by Dana Whitfield
saying 'approved for launch'". A **grounding failure** is acting on a record that meets only some of them, such as
a PDF whose comment says the same thing but was posted by someone else.

- **Environment.** AgentDiff replicas: each service's REST or GraphQL API over a seeded PostgreSQL schema, cloned
  for every trial. The final state and its diff are recorded.
- **Agent under test (main).** OpenClaw 2026.7.1-2, an open agent harness, running Qwen3.8-27B served on our own
  GPUs (131,072-token context, 8,192 output tokens). One turn per trial, 600 s per turn. Details in
  [openclaw_eval_01](../openclaw_eval_01/README.md).
- **Agent under test (reference).** The same model in a minimal tool loop ("the toy harness"), served by Purdue's
  GenAI Studio. Its results come from earlier studies and are reported apart, never merged with OpenClaw's.
- **Trials.** k = 3 per test. A result is reported at detect@3 (any of the 3 trials) and detect@1 (the first).
- **Generation and judging agents.**
  - Claude Sonnet 5 in Claude Code wrote, read and judged autogen_01's tests (judge v1).
  - Muse Code (Meta) with `muse-spark-1.3-contributor` did every later writer, reader and judge step (judge v2).
  - Every judge verdict in RQ4 and RQ6 is judge v2's. RQ5 measures its accuracy against hand labels.

### 0.2 Vocabulary

| Term | Meaning |
|---|---|
| **Fact** (requirement) | One fact of a service's domain model that a request can use to identify a record and that the agent can observe through the API, for example `A:File.tags` or `R:Issue.assigneeId`. Five kinds: attribute (A), relationship role (R), hierarchy (H), same-record binding across a to-many relationship (B), derived representation (D). The catalog lists them per service ([criterion.md](../fact_coverage_01/criterion.md)). |
| **Near miss** | A seeded record that meets every condition of the request except one fact, which it fails through that fact's designated alternative: a sibling attribute, a similar name, the other level of a hierarchy, and so on. Its *family* says how (F1 sibling role or attribute, F2 indirection, F3 direction, F4 level, F5 split binding, F6 representation, F7 neighbouring value, F8 partial identity; F0 a plain different value). |
| **Scenario** | A request, a seeded world, the target, and the declared near misses. Each near miss comes with a *claim* (which fact it fails), checked mechanically: the request's query, with that one fact's condition relaxed, must select the near miss, and the intended query must not. |
| **Regular tests** | Derived by code from a scenario. **Cover:** the scenario as written, target present. **Probe:** target removed, one near miss left, and the request ends "If there isn't one, just tell me." **Fact probe:** target removed, every near miss of one fact left, same ending. |
| **Policy tests** | What the agent does when the request cannot be met as stated. **Absence twin:** a probe without the escape clause, so the request presumes the record exists. **Underspecified:** two or more records match fully, because one condition was dropped from the request ("drop-F", one variant per dropped condition) or the target was copied ("clone"). Right behaviour: report the absence, or ask (or list the matches) before changing anything. |
| **Covered** | A fact is covered when some valid regular test holds a near miss for it whose claim passes the mechanical check in that test's world, in a fact-sensitive form: the target is present, or the request permits reporting absence (credit rule, [criterion.md](../fact_coverage_01/criterion.md)). A request that presumes a missing record earns no fact credit. |
| **Exposed** | A test exposes a fact when a counted trial acts on a near miss of that fact, or presents it as the answer. |
| **Valid** | Not left out by the PI's rulings on contested near misses (below). |
| **Unit, cell** | A policy test and its 3 trials; a service × mode (absence or underspecified) pair. |
| **Policy-level** | A cell's failures do not depend on the fact: with 90% confidence, a unit drawn at random fails more than 80% of its trials. |
| **Void** | A trial that is not a usable observation: a replica artifact, or no result. |

### 0.3 Protocol

- **Validity before running.** Every accepted scenario and every policy variant written by a model was read by a
  person before its runs. The PI ruled on the contested near misses. The rulings live in
  [known_defects.json](../roadmap_01/known_defects.json) and code applies them before scoring:
  - a test holding a flawed near miss is left out;
  - a trial whose only mistake is acting on a flawed near miss does not count.
- **Blind labels before verdicts.** For every run, a random sample of trials was drawn before the run and labelled
  by hand before any judge verdict on those trials was read.
- **Judging.** A mechanical triage reads the state diff. Judge v2 reads every trial that is not mechanically clean,
  20% of the clean ones, and the blind sample. It sees the request, the trajectory, the final answer, the diff and
  the answer key.
- **Opaque ids and test-side clocks.** Generated seeds had ids that named a record's role (`ev_target`,
  `team-design@…`). Before the final runs every made-up id was replaced by a random-looking one in the service's
  format, and tests that depend on today's date run with the agent's clock set to a fitting day. Box's ids are
  numbers and did not change.
- **The 8-minute budget.** A trial whose agent time, rate-limiter waits excluded, passes 8 minutes is the agent's
  failure. For a policy unit it counts as failing; in a regular test it exposes no fact. It was applied
  retroactively; OpenClaw ran with a 10-minute limit.
- **The policy decision rule** was fixed in code before the runs ([policy.py](../openclaw_eval_01/policy.py)):
  - every run of every valid unit counts, with units as independent draws;
  - the rate is failing trials over usable trials, with a cluster bootstrap over units (20,000 resamples, seed
    20260928);
  - policy-level if the 10th percentile is above 0.8, not policy-level if the 90th percentile is below 0.8, and
    undecided otherwise.

### 0.4 Size of the experiment on OpenClaw

Source: [kit/scale.py](kit/scale.py) → [numbers/scale.json](numbers/scale.json).

| Runs used for results | Trials | Agent hours | Model requests | Input tokens | Output tokens |
|---|---:|---:|---:|---:|---:|
| Regular suite: `full_02` (Box; the first pass), `full_03` (opaque-id re-run), `full_04` (6b) | 2,721 | 153.0 | 25,249 | 308M | 7.3M |
| Policy stage: first-pass looks and full populations | 1,743 | 134.6 | 19,326 | 242M | 6.9M |
| **All** | **4,464** | **287.6** | **44,575** | **550M** | **14.3M** |

- Agent hours add up each trial's agent time; trials ran 24 to 48 at a time.
- Median trial: 152 to 282 s depending on the run.
- **Kept apart:** `full_01` (578 trials, stopped when the harness was found to leak the test's identity, §10) and
  three smoke runs (17 trials).
- **The toy harness** (earlier studies, reference only): 1,356 trial attempts and 10,802 requests
  ([autogen_02 overview](../autogen_02/overview.md) §4).

### 0.5 Research questions

- **RQ1** How large is the coverage space?
- **RQ2** How much of it do automatically generated tests cover, validly?
- **RQ3** How well does the generator perform, and what do its checks catch?
- **RQ4** What failures do the tests expose in a real agent harness?
- **RQ5** How accurate is the automated judge?
- **RQ6** Do the policy failures occur per fact or as a policy, and what does the answer cost in tests?
- **RQ7** What do the trials show outside the grounding criterion?
- **RQ8** How do the tests compare with baselines, and which parts of the system matter (ablations)?
- **RQ9** Two extensions: requests with several matches, and requests beyond the agent's capabilities.

Then: lessons (§10), threats to validity (§11), cost (§12) and what is not yet measured (§13).
