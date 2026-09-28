# Overfitting and leaks in the prompts (roadmap step 2)

*2026-09-27. For discussion with the PI at step 3; **nothing here has been changed.***

## What was checked

Every prompt source that reaches an agent of the automated system:
- **Writer:** its role prompt, method notes, format notes and the two worked examples.
- **Readers, judges, variant writers:** the cold reader, judge v1 and v2, the drop-F request editor and the clone
  author.
- **Per-domain notes** given to the writer, the clone author and the judge: replica notes, seed operations, and the
  domain model.

That is 22 sources.
- **Read as a whole:** each one, asking whether it reads like general instructions from someone who knows the domain,
  or whether it is shaped around our tests.
- **Scanned mechanically** ([overfit_scan.py](overfit_scan.py), [overfit_scan.json](overfit_scan.json)):
  - **What:** names, quoted phrases, identifiers and every 5-word phrase of each source were matched against 799 test
    cases. That is every regular and policy test of autogen_01, autogen_02 and the hand-made suite (requests and
    seeds), plus the hand labels.
  - **Set apart:** the seed builders' default people (Maya Chen, Leo Park, ...), since using them follows the seed
    conventions.

**Where a leak would matter.** A leak matters only where it reaches the component whose output we report:
- **The agent under test** (the failure rates): the solver.
- **The judge** (its agreement with the labels): the judge.
- **The generator** (validity and yield): the writer.

## Findings

| # | Finding | Reaches | Risk to a reported number |
|---|---|---|---|
| 1 | The solver's prompt is the benchmark's own, verbatim | – | none: nothing of ours reaches the agent under test |
| 2 | The judge prompts hold rules and generic examples only; no labelled trial appears in them, and the judge never reads labels | judge | none found |
| 3 | The writer copied the worked examples into 9 of the 29 Muse scenarios | writer | the generator's claims, not the agent's numbers |
| 4 | The method's "make the near miss tempting" section encodes how careless agents behave, learned from the pilot runs | writer | a reviewer may call it tuning to the evaluated agent |
| 5 | The Box example breaks the method's own rule 4, and a generated scenario inherited the flaw | writer | test quality (already in the known-defects list) |
| 6 | The reader, drop-F editor and clone author prompts have generic examples from outside the test set | – | none |

### 1. The solver sees nothing of ours

Qwen's system prompt is AgentDiff's: the authors' ReAct template, service config and API documentation, extracted
unchanged from their notebook (`smoke_runtime.official_prompt`). The writer's `api.md` is a verbatim copy of those
docs, and no replica note, method note or example is added to it. The test requests carry the escape clause ("If there
isn't one, just tell me") by design. **So the agent failure rates have no leak path from our prompts.**

### 2. The judge prompts are clean

- **Rules, not recalled trials.** Judge v1 and v2 define the outcomes, the policy-test rules and the mechanisms. Their
  examples are generic: "a wrong priority scale", "close enough", "the only candidate". Qwen's behaviour prompted some
  of them, but none names a test, a record or a trial.
- **The only words they share with the label files are the outcome names**, which the labels use by design.
- **Labels never reach the judge.** `judge2` reads labels only in `compare`, after the verdicts exist.
- **So the agreement figures (87/93, 90/93, 110/110) have no leak path from the prompt.**

### 3. The worked examples were copied into the Muse scenarios

All copying is in autogen_02's Phase 4 scenarios, which Muse wrote. autogen_01's scenarios (written by Sonnet) and
the hand-made scenarios share nothing distinctive with the prompts.

| Copied from | What | Phase 4 scenarios (tests) |
|---|---|---|
| Calendar example ("Move the design review that Priya Nair declined on Thursday to Room 5B") | "Room 5B" as the move destination | 6 of 7 Calendar scenarios (70 tests); G4-CAL-03 also copies "on Thursday to Room 5B" |
| Box example ("Add the tag q3-close to the PDF that Maya Chen owns directly in the Finance Reports folder (not in its subfolders) and that Leo Park modified last") | G4-BOX-05: the same tag, folder and people, with fewer conditions, and the example's decoy explanation word for word ("Owned by Maya Lopez, not Maya Chen"); "Finance Archive" in its seed | 1 near copy (5 tests) |
| the same | G4-BOX-06: "directly in the Marketing folder (not in its subfolders), and that Leo Park created"; the example's explanation pattern ("Folder listings show the modifier; only the folder's details show the owner") | 1 borrowed structure (13 tests) |
| method.md's F8 examples ("MOB-42 for ENG-42", "kenji.sato → kenji.satou") | G4-LIN-08: "the 3-point sub-issue of MOB-42", with decoy MOB-421; "kenji.satou" as a decoy in G4-CAL-02's seed (13 tests), a scenario already counted above | 1 more scenario (15 tests) |

- **What it affects:**
  - **Not the agent's results.** The solver never sees the examples, and the copied values are either valid
    conditions or incidental (an action's parameter such as "Room 5B" or a tag).
  - **The generator's claims.** One Muse scenario (G4-BOX-05) is essentially the expert's example, and two more borrow
    its shape. Once the prompts are published, a reader will find the example's words in the test set.
- **Proposed, for discussion:**
  1. Tell the writer not to reuse the examples' names, values or phrasing (one line in `writer.md`: the examples
     illustrate the method; the scenario must be designed for its own facts). This is a general rule, not a patch
     for one test.
  2. Give the examples distinctive values that nobody would reuse by accident, or say so in the examples.
  3. Keep the 9 existing scenarios, since they are valid tests, and disclose the copying. G4-BOX-05 could be
     regenerated if the report's generator numbers should exclude a near copy.

**The PI's reading (2026-09-27).**
- Not a validity threat. The writer's output is automation's output, and few-shot examples are allowed.
- Worth a small improvement that avoids the copying without changing performance.

Applied the same day:
- **`writer.md`** now says to match the examples' standard, not their content: the request, names, values and records
  are the writer's own, designed for its facts.
- **The examples themselves are unchanged,** apart from finding 5. They are fact_coverage_01's hand-built pilot cases
  BOX-01 and CAL-01; the kit's self-test checks that they reproduce those seeds, and it still passes.
- **Still unmeasured:** whether the line stops the copying without lowering acceptance. The next generation run
  (roadmap step 4) will show it.

### 4. "Make the near miss tempting" is learned agent behaviour

This section of `method.md` (method v2, autogen_01) tells the writer where an agent "looks first" (names, titles, what
a listing or search returns). It also says to let a partial identity contain the requested value, so that a search
returns the decoy too.
- **Not Qwen-specific.** Nothing in its wording names Qwen or a test.
- **But it was learned from the pilot runs** of which near misses caught the agent.
- **Proposed:** keep the content, and add one sentence of provenance to the method ("derived from which near misses
  exposed failures in the pilot runs"). The final evaluation on other agents then tests whether it generalizes.

### 5. The Box example breaks the method's rule 4

- **The conflict:** rule 4 forbids hints only a test would give. The Box example's request says "(not in its
  subfolders)", which is exactly such a hint.
- **The consequence:** G4-BOX-06 copied it, and my scenario review had already marked G4-BOX-06 flawed for that
  hint. It is in [known_defects.json](known_defects.json).
- **Proposed:** remove the parenthesis from the example. The F4 decoy it guards still works, because "directly in"
  states the condition.
- **Applied on 2026-09-27** with the PI's go-ahead for small fixes of known defects: the request and its condition
  now read "directly in the Finance Reports folder". The kit's self-test passes: the seed is unchanged and every
  defect check still fires.

### 6. The other prompts

- **Reader, drop-F editor, clone author:** their examples are "the Pricing sheet file", "a link pasted into the
  location", and a song on a playlist. None of them occurs in any test.
- **Replica notes:** they describe the mock (what it returns, ignores or rejects), including the gaps autogen_01 found
  in runs. That is knowledge about the mock, not about answers. One line in Slack's notes is about agents ("With few
  channels, the agent usually lists them all"); it could be restated as a fact about the mock.
- **Seed operations:** they give default people chosen to make near misses possible, such as Box's Maya Chen and Maya
  Lopez. That is design knowledge in the seed conventions, and it belongs to the code audit
  ([domain_code_audit.md](domain_code_audit.md)).

## Limits

- **User messages not checked separately.** The messages the code assembles from each test (the writer's facts, the
  reader's records, the judge's bundle) carry that test's own content by design, so they were not scanned apart from
  the templates.
  - A scenario that copied an example passes the copy on to the judge: G4-BOX-05's bundle explains its decoy with
    the example's own words ("Owned by Maya Lopez, not Maya Chen").
  - That is still the test's own definition, which the judge is meant to see, so it affects nothing the judge is
    measured on.
- **The benchmark's API documentation** was not checked for leaks; it is not ours.
