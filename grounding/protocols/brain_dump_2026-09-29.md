# The PI's notes of 2026-09-29: the research view and next steps

*Organized from the PI's brain dump of 2026-09-29 and the same-day follow-up. Both are kept verbatim in the
appendices. **Read this before proposing next steps or asking about the research goal.** It records the PI's
thinking on that date. Decisions reached in discussion go to the [roadmap](roadmap.md), not here.*

Labels: **Decided**, **Open**, **Idea**, **Task** and **Context** mark the PI's items. **Fact** marks something
looked up in the repository, with its source. Sections are lettered; the PI's point numbers are in brackets.

## The PI's follow-up, the same day

- **Why section A is here.** Some sessions took wrong steps, or asked questions that showed they did not understand
  the research goal or why the work is done. Section A records the overall picture. It needs no decision now and
  will be iterated.
- **Self-judging is acceptable.** A model may judge its own runs. The judge's architecture gives it enough guidance,
  and the result could be interesting in itself.
- **Blind samples** continue to be labelled by a coding agent, with the PI helping where needed. Work by Claude (the
  lead session), an Opus agent or a GPT Astra agent counts as manual.
- **The 8-minute budget is settled:** an agent that does not answer within 8 minutes has failed. End of story.
- **The PI's lever:** Claude Code sessions in which an Opus agent takes an investigation task and works for hours,
  with large usage limits. To be used smartly.
- **Reading choices, confirmed:**
  - "Coen" is Qwen, "OpenCLA" is OpenClaw, "Soul Agent" is Sol, and "GPT-4.1" is GPT-6.1 Sol.
  - "234 facts" stands for the report's counts: 255 in the catalog, 213 servable, 204 covered.
  - Point 8 means those failures are *not* grounding failures.
  - "Five rounds left" means three models on two harnesses, minus the one done.

## The PI's second follow-up, the same evening

Verbatim in Appendix C.

- **The repository:** maintaining it, including commits, is up to the lead session.
- **Judge:** keep Muse, and also test Qwen as the judge.
- **The self-hosted Qwen** may start on any free GPUs on trojai3: four for two copies, or two for one. It takes only
  free GPUs and does not start if too few are free. Since 2026-09-29, `qwen up [2|1|auto]` does this.
- **Writer, reader and variant writers stay on Muse.** The bulk of generation is done and paid for.
  - A suite that mixes Claude-written and Muse-written tests "would be bad".
  - So the Sonnet-written half may have to be regenerated with Muse, which "feels like a risky business". Open.
- **Solver:** GPT-6.1 Sol for now. OpenClaw officially supports both the Anthropic and the OpenAI subscriptions (its
  docs agree), and the PI does the login.
- **The second harness** is an investigation question.
- **The time budget:** keep 10 minutes if all runs used 10, otherwise 8. All 3,018 final executions used OpenClaw's
  600-second limit, so the budget is **10 minutes**.
- **Undone probes: look closer, and be very cautious with blanket rules.** For each case, ask:
  - Was the edit authorized?
  - Did it leave unintended effects?
  - Was it called for?
- **The F0 rule and the rulings on individual tests** need plain explanations. The PI is happy to regenerate the
  facts that got false credit.
- **The Purdue calibration** is dropped, since that row is historical.
- **Awareness remarks** need no decision, but observations like these are always welcome: "I'm happy to be surprised
  by new information."
- **How parallel work runs:** the lead session starts separate Claude Code sessions, each in a new worktree on an
  investigation question. They are not internal subagents, so the PI can talk to them directly. None start yet:
  first agree on the plan, sync, and do the OpenAI login.

# The story

## A. Research view and name [6]
*Roadmap: new; it shapes the report (6e).*

- **Open:** The research view, the bigger picture (see the follow-up above: context, no decision needed now).
- **Decided:** "Grounding obligation" has to go; it undercuts the work. **Open:** what to call it instead.
  - **Fact:** report_01 already says "fact-discrimination coverage (FDC)" and "fact-discrimination tests";
    "grounding" survives in RQ7 ("outside the grounding criterion").
- **Context, the motivation story.** It was written to answer "why not just use model-based testing?" The full
  text is in Appendix A, from "Traditional software testing techniques do not transfer directly…". Its argument:
  1. **Two systems.** There is the agent and the services it uses. We test the agent's use of them, not the
     services, so a method must tell a dumb agent from a competent one. A suite inherited from the services may not
     tell an intelligent agent from a parser that maps commands to APIs.
  2. **State machines fit the wrong layer.** FSMs and EFSMs fit the tools and execution layer, not the agent. A
     research agent with only web search has a trivial tool FSM, yet its sophistication lies in "deciding what
     transitions and intermediate actions should occur".
  3. **State becomes knowledge.** An agent's relevant state is its knowledge of the task and environment, which is
     open-ended and cannot be fixed in advance. An EFSM `knowledge_base` variable leaves the state space unbounded
     and does not say what to extract from language.
  4. **Language must become a task specification first.** This may be the hardest part, and it is not done in one
     shot: interpretation, planning and execution interleave. Once a specification exists, testing is familiar
     again, but it then tests the execution substrate, not the intelligence layer.
  5. **Open world.** The agent holds observations and beliefs, not the state.
  6. **Oracles.** Correctness depends on interpretation, and several outputs can be right. An LLM oracle, "or even
     the same model", risks reproducing the failures it should catch.
  7. **Adequacy.** Structural coverage (statements, branches, transitions, states) says little about semantic
     behavior.
  8. **Benchmarks versus testing.** Benchmarks estimate capability over a distribution of tasks; testing hunts
     situational failures. A high score can coexist with severe corner-case failures.
  9. **Hence a neuro-symbolic approach** that extends traditional testing rather than replacing it: "LLM agents
     make the construction of that specification part of the system under test."
- **Context, the professor.**
  - He was sold on the problem space.
  - He suggested state variables for a research agent. The PI answered that the variables are finite but their
    domain is potentially infinite.
  - He replied "we need to model the world", the line that sold the pitch.
  - His next question: how do you show that this dimension, which you came up with, matters?
- **Context, the answer so far.** A coding agent analyzed AgentDiff's results:
  - Nearly all of its hand-designed tests involve at least one grounding obligation. Only necessary ones were
    labelled, so missing one fails the whole test.
  - The existing assertions do not check them: a problem "hiding in plain sight".
  - More benchmarks can be analyzed the same way (see D).
- **Decided:** There is no need to keep the original pitch; a lot has changed.
- **Context, what carries over:**
  - we model only "the relevant slice of the world";
  - the slice yields distinct requirements systematically;
  - requirements make testing and oracle generation systematic, where otherwise both stay mostly manual.
  - It can be shown that without the domain model few requirements get tested and oracles are flawed (false
    positives and false negatives).
- **Idea, presentation layers.** None is a deal-breaker, and the implementation stays the same:
  - equivalence partitioning, with valid and invalid classes (view 2 in B);
  - model-based testing: requirements in a formal notation such as B, where the condition checks give decision
    coverage and probes become decision-coverage cases;
  - "everything is a policy" (view 1 in B).

## B. Fitting several-match and capability boundaries into the method [5]
*Roadmap: step 5 is done (manual investigations, then automation, on the toy harness); report_01 RQ9.*

- **Context, the problem.** Several-match is partly in the report but "feels very dangling", like "wait, there is
  one more thing". A method that is proposed and automated has to fit together.
- **Context, what fits today.**
  - The domain model gives the facts this mock supports (213 servable of 255), and each fact is a requirement.
  - Facts are sampled and packed into covers, and the credit rule and the probes build on them.
  - Policy tests feel like an addition, but are not really separate.
- **Idea, view 1: everything is a policy.** Regular, underspecified and absence are three policies, each tested
  through the facts.
- **Idea, view 2: valid and invalid inputs,** from standard software engineering. The valid inputs are the regular
  tests. The invalid ones, adapted to agents, are the underspecified and absent requests.
- **Open:** Several-match fits neither view yet.
- **Open:** Several-match brings traps, which look like input. Are they inputs, or something the agent should
  reason out, as our generator does?
- **Open:** The coverage spaces for several-match and for capability boundaries, framed to fit rather than added
  on.
- **Fact:** Each step-5 study defined its own space:
  - several-match: 33 "shortcuts" over 6 kinds of request, 19 of them lazy and practical to defeat;
  - boundaries: 152 elements drawn from the catalog, of which 93 are faithful to the replica, mostly from 80 facts.
- **Fact:** report.md's RQ9 already proposes how they fit (the concise report dropped this):
  - several-match is "one more test form over the same catalog facts";
  - its traps are "construction choices, like near-miss families";
  - its misses are a policy, reported per service;
  - boundaries are a separate space, linked to the catalog "the way the policy panel is".
  - The roadmap's goal still says boundary tests cover the catalog's "unsupported side", but RQ9 calls the 42
    unservable facts "a different axis".

## C. Failures outside the criterion [8]
*Roadmap: report_01 RQ7 and §13.*

- **Open:** Are we wrongly ignoring other failures, such as misreporting, a wrong priority, or hallucinations in the
  reply?
- **Context:** Not counting them does not hurt, because the definition excludes them: they are not grounding
  failures.
- **Open:** Are we leaving valuable information on the table?
- **Fact:**
  - RQ7: 105 of 149 Linear priority writes are wrong.
  - In 22 of 23 cover runs that wrote a wrong priority to the right issue, the run still scored as correct.
  - §13 lists systematic checks of values and disclosures as not done.

## D. Related work [7]
*Roadmap: new.*

- **Task:** A lot of literature work is needed:
  - other benchmarks: manual, partly automated, or in the same domains;
  - environment-generation work, which builds environments and trajectories for reinforcement learning, some of it
    claiming evaluation or testing. These may supply baselines, or the related work explains why they cannot.
- **Idea:** Analyze more manual and automatic test suites, and measure how much of our coverage space they cover.
- **Fact:** baselines_01 has a pending decision on adding the AgentDiff suite as a "status-quo row", which overlaps
  with this idea.

# The experiments

## E. Agents under test: models and harnesses [4]
*Roadmap: goal 1 and step 7 said "more models and harnesses later"; this brings them forward.*

- **Decided:** Two or three harnesses and several frontier models. Qwen stays, since it suits people who self-host.
- **Decided:** Frontier models, but not the very best:
  - Sonnet, and one GPT model, GPT-6.1 Sol;
  - not Fable, Opus or Astra;
  - Gemini and Grok are not needed.
- **Context:** If cost were no concern, Sonnet and 6.1 would be enough.
- **Context, subscriptions:**
  - Claude: the maximum tier, with a lot of usage; Sonnet is efficient on it.
  - OpenAI: the $100 plan, cancelling a week after 2026-09-29. With three banked resets and 50% of the week used,
    it has about a month of usage left, so OpenAI testing should happen now. A $20 plan can cover leftovers.
  - Subscriptions are more cost-efficient than API prices.
- **Fact:** report_concise's Table 18 estimates one 1,006-case round at API prices, assuming Qwen's token profile:
  about $263 for Sonnet 5 and 5.5, and about $230 for GPT-6.1 Sol.
- **Context, harness:** OpenClaw is the only harness so far. It can connect to both subscriptions.
- **Task:** Find a second harness: a real-world one, not the toy harness.
- **Open:** Will people ask how Claude (web chat) or Codex do as the solver agents themselves? Should it be
  entertained, and if so, much later?
- **Context:** One round is done. Two more models go on OpenClaw, then the same three on another harness: five
  rounds left.

## F. Models for our own pipeline: writer, reader, judge [1]
*Roadmap: "Muse for every agent role" (2026-09-27). Option A keeps it; options B and C change it.*

- **Context:**
  - API costs are not reimbursed.
  - This evaluation ran about 3,000 executions, and generation took hundreds more.
  - Each round needs many judge calls, and every new agent repeats them.
- **Idea, option A: keep Muse Code.**
  - For: contributor pricing has not been bad so far.
  - For: at general pricing, Muse Spark 1.3 is still cheaper than Sonnet and GPT-6.1 Sol.
  - For: Muse is not considered a top model, so the method working with it is a plus.
  - Against: it still costs real money, over five more rounds.
- **Decided:** Reports give the general price (Muse Spark 1.3's), never the contributor price, which would mislead.
- **Idea, option B: the self-hosted Qwen for judging, and perhaps generation.**
  - For: free, open-source and practical to host. If it is comparable to Muse, the accessibility and cost story
    improves.
  - Against: it is not known whether its generation and judging hold up.
- **Idea, option C: Claude Code with Sonnet, on the subscription.**
  - For: no extra cost, and the top tier's limits should hold.
  - Against: a stronger model is more expensive when reported, and probably adds little to test or judgment quality.
- **Idea:** A later experiment on how generation and judging change with the model. Can weaker models following
  this pipeline match stronger ones? People assume only the strongest model tests well.
- **Open:** Try a little of that now?
- **Fact** (report_01 §12):
  - Generation happens once and the suite is reused; only judging repeats for each new agent.
  - Judging costs $0.020 per run at list price ($0.0014 billed). That is about $60 list, or $4 billed, per
    3,018-run round, from about 2,100 LLM verdicts.
  - All Muse use so far: about $340 list, $23 billed.
- **Fact:** Sonnet on the Claude Code subscription wrote autogen_01's scenarios ($208 at list price, $0 billed). So
  some data on writer strength exists (report Tables 3 and 5), though different briefs and method versions confound
  it.

## G. Baselines [3]
*Roadmap: 6d is done, with Muse only; this extends it.*

- **Context:** The current baseline is Muse Code itself, which is fair because we use Muse too.
- **Task:** Reviewers will want stronger coding agents, Sonnet 5 or GPT-6.1 Sol (a Codex agent, on the subscription
  this week). Maybe both.
- **Task:** Fix the baseline sample size, which is 48 now.
- **Fact, how the 48 was drawn:**
  - Each baseline arm wrote 48 tests, 12 per service.
  - Our column in report_concise's Table 14 is not a run. It is the expected result of drawing 12 valid regular
    Muse tests per service from all 294.
  - Policy tests are not included.
- **Context:** There is no baseline comparison for the policy tests. Several-match and boundary tests would need
  one too if included. The comparison as it is is "kind of good", but may need revisiting.
- **Idea, match token cost.** The Muse baselines cost an order of magnitude less ($0.51 to $1.20 list per 48 tests,
  against our $6.00). Give them more budget, for example a reviewer that re-checks after each batch against generic
  requirements such as distinct abilities tested and distinct bugs.
- **Idea, a repo-explorer baseline:** a fresh checkout of AgentDiff plus additional docs, encouraged to explore the
  whole repository and test.
- **Fact:** baselines_01 proposes a full comparison (its report, "Proposal for the full comparison"):
  - two arms on all 51 briefs;
  - budgets matched by test count, about 280 tests per arm;
  - 60 blind-labelled runs per arm;
  - three decisions pending for the PI.

## H. Mock-to-real transfer [2]
*Roadmap: new.*

- **Context:** People will ask whether results on the mock transfer to real Slack, Linear, Calendar and Box. The
  mock was chosen for easy setup: a message from someone two days ago is trivial to seed in it and hard in real
  Slack.
- **Decided:** Do a case study. Sample tests, connect the solver to the real services, rerun, and see whether the
  failures reproduce.
- **Open, how:**
  - (a) A coding agent, given access, does it as a manual case study. It is reported as a comparison, with no
    automation claim: "the process is already transferred, and this is a case study".
  - (b) Extend the domain model with what can be set up in the real world, and generate tests for the real
    environment from it.
  - (c) From the domain model, a coding agent finds which facts or tests become unrealizable in the real
    environment, filters them out, and the rest are rerun there. Possibly just a smarter (a).

# Constraints and method

## I. Budget (runs through points 1 to 4)

- **Context:** API costs are not reimbursed.
- **Money goes to:**
  - the judge, every round;
  - baselines: stronger agents, bigger budgets, and policy and extension baselines;
  - solver models;
  - real services for the transfer study;
  - more harnesses.
- **Subscriptions can absorb:**
  - on the Claude plan: Sonnet as solver, as option C, or as a baseline;
  - on the OpenAI plan, until about 2026-10-06: Sol as solver, or Codex as a baseline.

## J. How work gets done [the closing note]
*Roadmap: this is already the practice.*

- **Context:** Handing investigations to coding agents turned the project around.
  - Give an agent an investigation question. It investigates, generates tests, runs them and iterates.
  - The learning comes from running, analyzing and iterating.
  - Investigation effort and budget stay separate from the method's.
- **Automation:** once an answer belongs in the method, an agent automates it. When the automation meets or exceeds
  the manual quality, it runs over the whole space.
- **Context:** This has been ten times more effective, or more, than thinking more and executing less.

# Tensions noted on 2026-09-29

- **Resolved by the follow-up:**
  - a judge model judging its own agent's runs;
  - who labels the blind samples for each new agent.
- **Still open:**
  - **Two agreed baseline rules.** Stronger baseline agents, a reviewer loop and a repo explorer would change "Muse
    for every agent role, baselines included" and "baselines prompted naively, not engineered". The pending proposal
    matches budgets by test count; the idea in G matches by token cost.
  - **Order.** Point 5's framing decides what the suite contains. Agent rounds run before it may need topping up
    with several-match or boundary tests.
  - **The OpenAI week.** Sol as solver, Codex as baseline and Codex as solver compete for it. The second harness
    and "Claude or Codex as solvers" may be one question.
  - **Provider terms.** Before using a Claude or OpenAI subscription inside a third-party harness such as OpenClaw,
    check each provider's current terms.

# Where things stood against the roadmap (2026-09-29)

| PI's point | Roadmap then | Effect |
|---|---|---|
| 1 Pipeline models | "Muse for every agent role" | A keeps it; B or C changes it |
| 2 Transfer | none | new |
| 3 Baselines | 6d done; full comparison proposed, 3 decisions pending | extends a done step |
| 4 Agents under test | "more models and harnesses later" | brings it forward |
| 5 Several-match, boundaries | step 5 done on the toy harness; RQ9 | reopens the framing |
| 6 Research view, name | 6e: report_01 | new; shapes the report |
| 7 Related work | none | new |
| 8 Other failures | RQ7; §13 | extends |

**Open on the roadmap, not in the dump:**
- **For the PI, after 6a and 6b:**
  - the F0 counting rule;
  - the lead session's rulings on G4-CAL-10, G4-LIN-15, G4-LIN-11 and AP-LIN-07;
  - the post-freeze drop-F naming fix;
  - duplicate units from one request;
  - G4-LIN-12;
  - calibrating the self-host against Purdue;
  - the awareness remarks.
  - The 8-minute budget was also on this list; the PI settled it in the follow-up.
- **From step 5:**
  - the judge's blindness to written values;
  - whether the round-trip ruling covers probes the agent undoes.
- **From baselines_01:**
  - the AgentDiff suite as a status-quo row;
  - the same-name-pair pattern;
  - whether the baselines' fact list keeps the kinds' definitions.
- **Not committed:** blind_review_01 (a Codex reference review of 200 final runs; in neither report) and
  report_concise.
- **Out of date:**
  - report_concise's baseline references point at a removed worktree;
  - the roadmap's step 5 and 6d rows predate the merges.
- **Housekeeping:**
  - decide whether the read probes are input or pipeline code;
  - derive the clone fields and the replica-gap list;
  - move Slack onto the common runner;
  - count the seed helpers.

---

# Appendix A. The brain dump, verbatim

So I mainly want to discuss the next steps, and I want to discuss where we stand with regards to the roadmap and the next things that we will have to do. So let me share everything like a brain dump, and I'm hoping you can help me sort through it. The first starts with, I think, the model choices. So the key restriction being that I will not be reimbursed for the API costs here. So as you can see, in this evaluation alone, we have run around 3,000 trials, and the generation also had to go through hundreds of trials. And each evaluation turn would take hundreds of calls to the judge, and this is for one agent. So if we add another agent, then that will incur a lot of these costs again. So the practical options that I have would be to continue using Muse code, and the contributor pricing that I'm using so far hasn't been that bad. So maybe I continue using that. The advantage is that, to the best of my knowledge, Muse is not a very strong model, or, I mean, regardless of Meta's internal reporting, as far as I know, it is not generally considered as powerful as, let's say, the Sonnet-level agents or in GPT's frontier models. So in that, if my method is working well with not so strong model, so why do we—I mean, that's a good thing if I can show that my method is working well with a model that is not one of the best. In terms of cost, it is not costing me much because of the contributor pricing, and in terms of the general pricing, that is also cheaper than Claude Sonnet, for example. It is even cheaper than OpenAI's GPT sol 6.1. So whenever we're reporting cost, I will probably not be reporting the contributor pricing because that would be misleading to the readers. So even if I'm reporting the general Muse Spark 1.3 price, then it still comes out to be cheaper than these models. So there is that incentive in keeping the Muse judge. But the disadvantage is that it still costs real money. So the more that I run, let's say I plan to do evaluation on two more models. So currently we have done evaluation on one model. I would pair OpenClaw with two more, and then I would repeat the same evaluation on another agent harness. So that makes this a total five rounds of evaluation left. So the cost would probably add up. The other option is we use Coen for judging as well. So this is something we have self-hosted, and this is always going to be free, and it is an open source model. It's something people can practically host. So if its generation power and judgment power is comparable to that of Muse, then that is clearly a big advantage because the accessibility or cheaper side of things is also better looking here, and it is also actually free for me. We get those advantages. But the disadvantage is that we are not sure if its generation quality and judgment quality will hold up to what we have seen so far. Relating this, I actually plan to do a little bit of experiment in the future where I show how generation and judgment performance varies with the differing models, because people tend to think that only the strongest model can do the best testing. So an interesting question is whether, following this pipeline of mine, whether weaker models can match the level of effectiveness of testing as the stronger models. So perhaps this is related to that, and maybe we could do a little bit of that now to get some idea. And the third option is to use my subscription. So I have subscription with Claude Code. So maybe we use Claude Code with Sonnet agent. So the bright side is that that fits in my subscription, so there is no extra cost, and I have the highest tier, so I'm pretty sure my usage limits will hold up. But the downside is that we are now using a stronger model that would make it more expensive when we are reporting, but we wouldn't probably gain much in terms of the quality of test cases or the result of judgment. This issue of managing budget is something you will see along The rest of the plan. So this is definitely something to keep in mind. 

Continuing, the next point, and by the way, this is not ordered in any way, so I'm just sharing in the order that it comes to my mind. The next point is we are testing this whole suite on a mock environment. So definitely people will ask how this transfers to a real-world environment. So for that, I've decided to do a case study where I could ask my coding agent to perhaps sample a set of these tests and connect the solver agent with a real-world environment, like real-world Slack, Linear, Calendar, or Box, and try to do this, repeat the test and see if the failure can be reproduced or if the results transfer, actually. So the question is whether the result will transfer to real-world environment. The reason I've been using this mock is because a setup is very easy. So I can set up whatever data I like. So let's say I need a message from someone two days ago. That's very easy to set up in a mock, but in a real-world Slack, that is very difficult to set up. So to avoid issues like that, I used the mock. Now, how should I handle this? Should I, like, keep the case study manual where I ask my coding agent to just do it, and of course I'll give my coding agent access to that. So in the paper, this will be reported that, okay, how does it compare, and I do not have to make any automation claims about the transfer thing. The process is already transferred, and this is a case study. That's one approach. The other approach could be that I— Like modify the domain model to capture the limitations of what we can set up in a real world, and that we use that to actually generate test cases for the real world environment and repeat the test. Or perhaps we could just take a middle ground where, from the domain model, I ask my coding agent to do some analysis and say which ones would become unrealizable in the real environment, and that could let us do some filtering. And then we can simply repeat the rest of the test cases in the real environment. Or perhaps this is not a middle ground. Perhaps this is just a smart way of doing the first option, which is the manual case study. Well, okay, this is what is in my mind about this. The third point is about the baselines. So currently the baseline is Muse code itself, which I think is very fair because we are also using that. In any case, I have been told that people would also want to see how stronger coding agents would do here. So I would need a coding agent that is either Sonnet 5 or GPT's Sol 6.1. Now, in terms of GPT, I also have a subscription for the next week, so we could use a Codex agent for that. Or we might even have both of them. We'll have to fix the sample size for the baseline. As of now, it is 48. And I don't know how the 48 has been sampled from our tests, whether it has been from the valid ones or the invalid, I mean the policy level ones. In any case, there is no comparison for baseline for the policy level tests. And if we decide to include the multiple case and capability boundary one, then those will also need corresponding baseline comparison. So baseline comparison as it is is kind of good, but I mean, given the bigger picture, we may have to come back to this. So the other thing about baseline comparison is the cost. Currently the muse code variants cost order of magnitude less, so we need to give them more budget to match token costs. Perhaps we can instruct it to have a reviewer where it rechecks its results after batches for the core requirements of distinct abilities tested, distinct bugs etc. All generic instructions. I will need another version that has access to the whole agent diff architecture too and encouraged to explore it. SO a fresh checkout of agent diff, plus additional docs and whatever needed, explore the whole repo and test. 

4. The fourth point is about the solver agent. So as I said, we want to evaluate this on around two to three harnesses and a bunch of frontier models. So Qwen is an interesting choice. I think that is a good choice for the users who would like to self-host. But then to test the frontier models, I would have to test Sonnet on the Anthropic side and one GPT model, probably GPT-4.1, on the OpenAI side. Now we are not going after the absolute best, so we are not going after, let's say, Fable or Opus, or on the OpenAI side, we are not going after Astra. So a choice has to be made here, and again the subscription or the cost concern comes up. I have subscription for both Claude and OpenAI. For Claude, I have the maximum subscription, so I have a lot of usage, which is great. And for models like Sonnet, it will be very efficient. And on the OpenAI side, I have just one week left till my subscription is canceled, but I have three banked reset, and my current weekly usage is at 50%. So come to think about it, I have almost a month's worth of usage on the $100 plan. So, given that we will be using Soul Agent, I think that will last us very well. So if we are using OpenAI, then we would like to do most or almost all of the testing right now to utilize the active subscription period. And if we somehow end up having something left, then I can always go back and get a $20 subscription. I mean, definitely subscription is going to be more cost efficient than paying for API. So that is what I am considering. So here, I mean, if the cost was not a concern, then at least one, so Sonnet and 6.1 would have been enough. And I mean, I would be happy with that as well. So I'm not too concerned about missing out on models from other providers like Gemini or the Grok family. This also includes the harness, though. So for now, OpenCLA is the only harness that we have considered. And luckily there is a way to link OpenCLA with both Anthropic and OpenAI subscriptions, so we are good with that. But we'll need another harness. So I don't want to use Toy Harness. Rather, I want to show the performance on real-world harnesses. And speaking of harness, I am wondering if people could question that. How would, let's say, Claude Sonnet on its web chat API, or let's say Codex, do as the solver agents themselves? I do not know this is a question if I should entertain, if that should be part of the evaluation. Even if it is, perhaps it's much later because first we have to finish the more basic ones. 

5. Then there's the case of multiple matches cases and capability boundary. So with multiple cases, there has been a suggestion, and a part of it has made to the report. But as of now, it feels very dangling. So it just doesn't fit into the thing that we are doing. It feels like I am telling a story, and then I'm telling everyone, but wait, there is one more thing. It doesn't work that way, right? So if I'm proposing a methodology and I'm saying I'm automating the methodology, so then the things of the methodology should fit there well. For example, so far what do we have? We have that we did domain modeling, and from domain modeling we got 234 facts that are supported by this particular mock. Each of these facts become one requirement. We are trying to see if the agent can uphold this requirement. So we do sampling from these to pack them together in the cover cases, as we call them, and this becomes the medium to test the agent's ability to uphold the requirement. And then we have the credit rule, we have probes, and really the policy-level tests are not that separate. So currently it's there, it feels a bit separate, or it feels like an addition, but it's not. So there are two views to this. One is that we could view everything as a policy-level test. The regular tests are one policy of regular. Under-specified is the under-specified policy, and then there's the absence policy. So everything is a policy. Once we add a policy, then in order to test the policy, we take help of the 234 facts. That is one way to go about it. The other is that we could say we are taking motivation from standard software engineering, where an input could be invalid or valid. So the valid cases are the regular ones, and for invalid, we adopt that in this context of agentic testing, and that gives us under-specification and missing, which is the absence case. These are all fitting, but the multiple, I'm struggling to fit that in here. And that also brings in some extra input-shaped things, which are the traps. Are those inputs or are those things that the agent should reason and figure out, like our generator agent? These decisions have to be made. So the coverage space, or how we define the coverage space for the multiple case for capability boundaries, not clear. And that should be in a way which fits together with the framing that we already have, rather than feel like a dangling supplemental. 

6. Perhaps the most important thing to do is to discuss what the research view is, what the whole idea or the bigger picture is. So first of all, we need a better name. I don't think grounding obligation is a good name. I think it is largely undercutting what we are doing.  So to provide more context, let me share with, let me share about what I have considered before this or how we got to this point. So before starting this effort, I was stuck or struggling to answer why we are doing this. Why can't we just use existing software engineering techniques like model-based testing? I mean, of course, what we are doing could sound like model-based testing or could be fit into model-based testing, but I would have to answer why we couldn't naively apply model-based testing from traditional software engineering. So in order to answer those, this is the story that I came up with. So I said that in testing agentic systems, there are two systems involved at least: the agent and the underlying system, which in this case are the four domains. So we have to understand that we are not testing the underlying domains; rather, we are testing the agent's ability to use them. So a testing methodology for agentic systems should be able to test its intelligence given the context. It should be able to tell a dumb agent apart from a competent agent. Traditional software testing techniques do not transfer directly to LLM agents because the agent is not merely another interface to an underlying software system. It introduces an intelligence layer that interprets natural language, constructs task specifications, plans, acquires information, and decides how and when to invoke underlying tools. Testing the tools alone therefore does not amount to testing the agent. A test suite inherited from the underlying system may verify that APIs behave correctly, but it can fail to distinguish an intelligent agent from a simple parser that merely maps known commands to those APIs.
This distinction becomes clear when considering traditional state-based testing. Software systems are often modeled using finite-state machines (FSMs) or extended finite-state machines (EFSMs), where behavior is characterized by control states, variables, guards, and transitions. Such models remain useful for an agent's underlying tools and execution layer, but they become poor abstractions of the agent as a whole. Consider a research agent whose only external capability is web search. At the tool level, its state machine may contain little more than issuing a query, receiving results, and returning an answer. Yet research can require some of the most sophisticated agentic behavior: decomposing an ambiguous question, deciding what must be established, generating successive searches, recognizing conflicting evidence, revising hypotheses, determining when enough evidence has been gathered, and synthesizing an answer. The sophistication lies not in the search tool's transition structure but in deciding what transitions and intermediate actions should occur.

The underlying difficulty is that the notion of **state** changes for an LLM agent. In conventional software, relevant history can often be compressed into a fixed sufficient statistic: variables such as `authenticated`, `approved`, `current_page`, or `retry_count`. The designer can specify in advance which facts may affect future transitions. For an LLM agent, however, the relevant state is increasingly the agent's **knowledge about the task and environment**. Future behavior may depend on arbitrary facts, relationships, qualifications, exceptions, references, assumptions, and pieces of discourse introduced through natural language. Consequently, the agent's relevant knowledge, ontology, and even task specification cannot necessarily be fixed in advance.

An EFSM can syntactically hide this complexity inside a variable such as `knowledge_base`, but this does not remove the problem. The knowledge base may contain an open-ended number of propositions and newly introduced concepts, making the induced state space unbounded. More importantly, the EFSM does not itself solve the semantic problem of determining what knowledge should be extracted from natural language or what follows from it. Symbolic reasoning can be very effective once concepts, facts, and relations have been formalized; the difficulty is that constructing and continually revising that formalization is itself part of agent behavior.

This leads to a second distinction between conventional software and agents: **natural language must first be transformed into a task specification**. That transformation may be one of the hardest parts of the task. A user request can require resolving references, interpreting implicit constraints, understanding exceptions, inferring unstated subgoals, or deciding among several plausible interpretations. Moreover, task specification is not always a one-shot operation. The agent may have to perform intermediate actions—searching the web, reading an email, querying a database, or asking another system—before it can determine what the task actually requires. Planning, interpretation, and execution therefore become interleaved.

Once a sufficiently explicit task specification has been constructed, much of the remaining behavior returns to familiar software-engineering territory. Tool calls, permissions, sequencing constraints, retries, safety policies, and preconditions can be represented symbolically and tested using state-based techniques. But this reveals the limitation: at that point the model is primarily testing the agent's execution substrate rather than the intelligence layer that produced the task specification and plan.

External interaction makes the problem still harder. Agents generally operate in an open world whose state is only partially observable and may change independently of both the user and the agent. A Gmail agent does not possess the mailbox state; it possesses observations and beliefs about that state. A research agent does not possess the state of the world; it accumulates evidence from imperfect and possibly contradictory sources. Agent behavior therefore depends not only on explicit program state but on assumptions and beliefs that can be incomplete, uncertain, ill-defined, mutually inconsistent, or invalidated by later observations. These assumptions themselves belong to the agent's open-ended semantic state.

This modeling problem is accompanied by an **oracle problem**. In conventional testing, a test often specifies an input and an expected output or invariant. For agents, correctness frequently depends first on the interpretation of the input. A natural-language request may admit several reasonable interpretations, and even under one interpretation there may be many acceptable plans and outputs. A research agent may use entirely different sequences of searches and still produce equally valid answers. Correctness is therefore often set-valued rather than defined by a single expected trace or output.

Even when a human can recognize a correct result, automatically checking it creates another difficulty: the test oracle must be sufficiently independent of the system being tested. Using another LLM—or even the same model—to determine whether an LLM agent interpreted a request correctly risks reproducing the same semantic failures that the test is intended to detect. Consequently, important aspects of agent evaluation still depend on human judgment, heuristic evaluators, or ad-hoc combinations of checks rather than deterministic test oracles.

Traditional notions of test adequacy are similarly difficult to transfer. Structural measures such as statement, branch, transition, or state coverage make sense when the implementation or behavioral model has a reasonably enumerable structure. They say much less about whether an agent has exercised the important parts of its semantic behavior. Two prompts may traverse exactly the same tool-level transition sequence while requiring fundamentally different reasoning, and two semantically equivalent tasks may produce completely different execution traces. Covering the underlying EFSM therefore need not imply meaningful coverage of the agent's interpretation, reasoning, or planning space.

The usual response for systems whose behavior is difficult to specify explicitly—such as learned models, chess engines, or increasingly LLM agents—is benchmarking. Benchmarks are valuable, but they answer a different question from traditional software testing. A benchmark estimates general capability over a distribution of tasks: how often does the system succeed, or how well does it perform relative to alternatives? Software testing is particularly concerned with finding situational failures: boundary conditions, unusual interactions, rare combinations of state, adversarial cases, and systematic classes of faults. A high benchmark score can therefore coexist with severe failures in precisely the corner cases that a testing discipline is intended to expose.

The resulting gap motivates a neuro-symbolic approach to agent testing. Purely symbolic methods remain valuable for the parts of an agent that can be specified explicitly: tool semantics, permissions, state transitions, invariants, and execution constraints. Neural methods are better suited to the open-ended semantic layer: interpreting language, constructing and revising task specifications, extracting relevant knowledge, proposing plans, and recognizing semantic similarity across superficially different situations. The goal is therefore not to replace traditional software testing, but to extend it with representations and test-generation mechanisms capable of reasoning about the semantic state of an agent.

The central challenge is thus broader than testing whether an agent's tools work correctly. It is testing whether the agent constructs the right problem from an open-ended input, maintains the right knowledge while interacting with an uncertain environment, chooses an acceptable course of action among many possibilities, and does so across situations that cannot be enumerated in advance. Traditional testing provides strong machinery once behavior has been symbolically specified; LLM agents make the construction of that specification part of the system under test.

So when I was sharing this with my professor, I think the thing that he got sold on is that on the problem space. So when I was discussing why EFSM would not be good abstractions, he immediately said that for things like a research agent, you would technically have a more complex system where you would not just model its action, but have state variables. And then I said that my very next point was that for a more complex system like this, we run into the problem where we have finite state variables, but the domain is potentially infinite. And he said that the problem, which means is we need to model the world. So from his side, this needing to model the world was actually the single line that sold the entire pitch to him. But okay, that being said, his next question was that, okay, you are proposing to solve this grounding obligation thing or test that. How do you show that this is actually an important thing? Because this is a dimension that you have come up with. So for that, what I did and what I could further do is to dig into the existing benchmarks. So like this agent diff benchmark, I had a coding agent run or analyze its result, and it found out that, like, nearly all of the manually designed test cases involve at least one grounding obligation, meaning that failing just one grounding obligation would result in failure of the whole test. So that clearly shows that this thing is coming up in the manually generated or manually designed test cases. So since this is necessary, I mean, we labeled only the necessary grounding obligations. Since it's necessary, so clearly now its importance cannot be denied. But we also showed that the existing assertions do not check that, which is again a good framing that we found this problem that is actually hiding there in plain sight, but nobody is talking about it or nobody is testing it. And after that, I started working in this repository. Now, a lot has changed since then, so there is absolutely no reason to try to maintain the original pitch that I had going into this project. I mean, the very high-level ideas transfer, those being that we are not modeling or trying to model the whole world; rather, we identify the relevant slice of the world which is relevant to this problem. And that slice lets us systematically identify distinct requirements, and these requirements now enable systematic testing and oracle generation, which otherwise remains mostly manual. And we can show things like, without using the domain model, only a few of the requirements will be tested. Perhaps the oracles will be flawed, there will be false positives and false negatives, and so on. We might further borrow other concepts from standard testing, like the invalid and valid cases of equivalent partitioning, or we could take ideas from model-based testing, where once we have these requirements, we could convert these requirements into some formal notation like B modeling, and the condition check then becomes, or lets us do decision coverage. Right, so these test cases where we are saying things like probes and etc., they become a decision coverage thing. So we could borrow from that concept if needed. These are not deal breakers. These are not substantial changes. In fact, these are just presentation layers, so our implementation can remain the same, but they would only vary in the presentation layer. But in any case, these are like the floating ideas or the candidate ideas that I had, which I just wanted to share. 

7. A lot of work needed in literature study or researching the related works. So there could be other benchmarks that are perhaps manually generated, perhaps part of it are automated, perhaps they are testing the same domains. There is a whole line of work in environment generation side. So there they concern how to generate environment and trajectory for, let's say, reinforcement learning, and some of them even claim evaluation or testing side of things. So we may have to look into that. They might supply some baselines to us, or at least we could discuss them in the related work and say why they wouldn't be a baseline. In any case, it would be helpful to analyze a bunch of more either manually designed or automatic test cases and show how much of our coverage space they are actually covering. 

8. The next thing is, are we missing out or wrongfully ignoring other types of failures like misreporting? So I have heard that there has been a lot of other failures exposed, like mislabeling a priority or any type of hallucination. That's perhaps in its response. I'm not counting them doesn't hurt us because we have a definition for grounding obligations and these types of failure are grounding failure. But here the concern is if we are missing a lot of valuable information that's right in front of us. 

So that's everything in my mind right now. One more small thing to share is how my, how the workflow has been in the past few days. So earlier I was struggling a lot with this project until I started delegating more investigation work to my coding agents. So it started with assigning an investigation question, letting the coding agent investigate, generate test cases, run and iterate. And as I've always said, it is in actually testing, analyzing the results and in iterating that we learn the most. So the agent does a lot of that manually to gather insights to learn about them and to answer the investigation question. Effort and budget in investigation is always separate from that in the methodology. Once investigation done, then the next phase is to try to automate that. Whatever answer we have got, if that is something that's going to be part of the methodology, then I would ask that now try to build an agent or use another coding agent or instruct another to automate the same thing that you have done. And once the automation is done and it either reaches or exceeds the quality of the manual effort, then that can be run broadly for the whole space to cover. This has been the workflow so far, and this has worked extremely well, as opposed to previously when I, when I did more thinking and less execution. That approach, I have been struggling with that approach for a very long time. But moving on to this investigation followed by automation followed by full scale has been like 10 times or even more effective than my previous approaches, because the goal of investigation is to learn, expose insights. And more often than not, we end up learning a lot of things where it becomes possible to automate that reliably in the next phase. 

# Appendix B. The follow-up, verbatim

Yes, by all means, save it. Edits are allowed for you. Mention thi file in either claude or agents.md or memory, so that other sessions know about its existence. The 4 reading choices are all correct. 

now I want to discuss what you suggest would be the next right step. I guess we could start off with the choices, which is something that must concern me. The reason I said that discussing the research view is most important is because I wanted you to know about the overall picture. Because in many cases, it seemed to me that the other sessions, they were sometimes taking some wrong steps or they were asking some questions which made me feel that they do not understand the overall research goal or why I am doing this in the first place. Since we will be working on this together and you will be helping me in a lot of decisions, so I figured it will be very helpful if you know them. But apart from that, that point doesn't call for any specific decision to be made now or to be settled now, and we can always keep iterating between them. So, I mean, given the recent success of the investigation approach, I'm still thinking that. So perhaps we could settle some open decisions, things like choosing models for our automation or the judge or the solver agent. Those. You did mention some points about the model judging itself. That is something I'm no longer concerned about because I feel like given the architecture that we have, a model will be able to or will have enough guidance to be able to judge itself, and that could be an interesting result of its own. The blind samples will continue like that, where a coding agent labels them, and again, I'm happy to help where needed. So work done by you or an Opus agent or GPT Astra agent are considered manual. And the other sessions have been pointing out some open points. I don't even know or I don't even remember what they are. F zero counting rule, rulings about a bunch of tests, eight-minute budget. I already clarified that. So from these, it feels like, I don't know, I don't even know if these are legitimate questions. Like the eight-minute budget, what about that? I already said the rule about eight-minute budget. If an agent fails to answer in eight minutes, that's the agent's failure. End of story. So I think these are from the step five sessions. I do not know if these questions are legitimate, but if they are, then I'm happy to share further. So let's tackle through these points together. On my side, the biggest power that I have is my access to Claude Code, where I can create a new session, give an investigation task to an Opus agent, and come back a few hours later and have it done. Like I said, that thing has been extremely helpful in the past few days, and that is something I would try to utilize smartly as much as possible. And I also have a ton of usage limits, so yeah, that's something that can speed us up a lot. 

# Appendix C. The second follow-up, verbatim

As for maintaining this repository, that's up to you. You can commit or you can maintain the repository as you deem fit. So I leave that up to you. As for the judge, that sounds okay. We could keep Muse, but we could also test on Quen. As for Quen, you would have to run a command to get that up and running again. Check ~/qwen-selfhost (or sth like that). 

I think there is a rule that it will not start up unless GPUs zero to three are free. But that is actually unnecessary, and we can start it, or we should be able to start it up with any four free GPUs. And if that's not possible, then we might want an option to start it with just two free GPUs. The key is to only take free GPUs and to not start if GPUs are not available. Writer, reader, and variant writers, I'm happy to stay on Muse because the bulk of the generation work has already been done and the cost has been paid. The only thing here is that a lot of the tests have been generated with Claude, so I cannot have a mix of these. That would be bad. So I think we might have to regenerate the other half with Muse. That feels like a risky business. As for the solver, sure, we can work on GPT-6.1 for now. I did find out that OpenClaude has official integration support with subscription for both Anthropic and OpenAI, so that is fine. I think the only thing needed from me would be to do the login. Second harness is indeed an investigation question. I did not understand what you said about the F-zero counting rule, so I would need you to elaborate. So it feels like you're saying that seven facts have got false credit. If that's the case, I'm always happy to regenerate seven more. For baseline comparison, I don't understand what you said. This gives 167. As for the eight-minute budget, if all the runs have been run on 10 minutes, then we can keep 10 minutes because I personally like the number better. However, if all those runs have been run on 8, or maybe all have not been run on 10, then I'm also fine to settle with 8 minutes. As for the undone probes, I would encourage you to look closer into the scenario. It does sound like fitting, but I would be very cautious to apply blanket rules like that. Was this an unauthorized edit? Did it leave unintended effects? Was this called for or completely uncalled for? So look into this. As for the tests, I have no concept, so I have no idea what you mean. Mechanical is fine. Perduce calibration can go because that is indeed historical. Awareness remarks need no decision, but they are interesting, and I always welcome interesting observations like this or anything. So I'm happy to be surprised by new information. So OpenCL is set up. Look into this. I'm happy to help with the login or integration. Perhaps if you give me a link, I click on it and I do the login or something like that. And after that, so what I'm mainly planning is, is that you would start parallel Claude Code sessions, and you would instruct each of them to go to a new work tree and tackle some investigation problem or something similar like that. So that would give us very good speed. But I would encourage you to start them in other Claude Code sessions rather than handling sub-agents internally, so that I can also interact with them directly through my CLI. Just letting you know, you don't have to start that right now. Let's first agree on the plan. Let's sync first. Let's get the OpenAI login done, and then let's see. 
