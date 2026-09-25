# Decisions log

This log records the decisions taken with the user after the v2 method ([report.md §11](report.md)). Each entry gives
the decision, why, where the evidence is, and a status:
- **settled:** the user agreed;
- **proposed:** discussed, not yet ruled on;
- **open:** needs work or a later discussion.

All entries date from 2026-09-25. [method.md](method.md) holds the pre-registered procedure and its addenda. This log
is the source for the next version of the method.

## Settled

**D1. What a policy-level failure is.** A failure is policy-level when it is indiscriminate across facts: its rate
does not depend on which fact is involved.
- **Judged per agent** (model plus harness), because instructions change it. OpenClaw's "check every condition" rule
  cut acting under presupposition from 63% to 23%, and what remained sat in specific fact families.
- **A fact-dependent failure is fact-level.** If a harness makes the agent lenient on some facts and cautious on
  others, that failure counts as fact-level, even under presupposition.

**D2. The scope of a policy claim.** A policy failure can only show when the presupposed target is missing (or two
things match, or the match is out of sight) and a candidate matches most of the description. That means a
multi-condition request whose near misses each fail one condition.
- **Tests below that level say nothing about the policy:** no candidate at all, or a one-condition request with a
  plain decoy (a .txt for "the PDF").
- **The same fact can sit inside or outside the scope.** In the pilot, an .xlsx matching owner, folder and modifier
  was taken as "the PDF"; a .docx missing type, owner and folder was refused.
- **Indiscriminateness is checked at fixed closeness:** the same request, with a different near miss.

**D3. The policy panel: keep P1 and P3, drop P2.**
- **P1:** the scenario with its target removed, wording presupposing.
- **P3:** two records that both fully match a singular request.
- **P2** (one plain decoy, presupposing) added a measurement, not a bug ([report.md §5.2](report.md)).

**D4. Deciding policy against fact level: paired, sequential and per domain.**
- **The pair:** each fact's probe (no target, one near miss, "just tell me"), which the suite runs anyway, plus a
  presupposing twin (the same test without "just tell me"). Only the twin is extra.
- **Per domain:** a failure can be policy-level in one domain and fact-level in another.
- **Stopping:** sampling continues until every test has run or the statistical conclusion is reached. There are no
  fixed checkpoints, but the stopping rule must hold under repeated looks (for example Wald's sequential probability
  ratio test).
- **Fixed before the first test:** ε, δ, and how much spread across facts still counts as indiscriminate.
- **Order:** facts are tested in a randomized order stratified by domain and substitute family.
- **What is measured:** the rate and the spread across facts. The 3 trials per test show the spread: all 0/3 and
  3/3 means fact-level, even at the same average.
- **Outcomes:**
  - policy-level: a small proof; stop adding twins;
  - fact-level: the twins stay as fact tests, recording conditions the agent relaxes;
  - no hole.
- **P3 is sampled per scenario, not per fact.**
- **Sampling is an optimization.** It may later be dropped in favour of running every test.

**D5. Repetitions and metrics.**
- **Unit:** distinct fact failures. A test exposes a fact when it fails in at least 1 of k trials, which is 1 − pass^k
  per test. pass@k is not used for finding failures, because it hides intermittent ones.
- **Budget:** repetitions stay off the budget only when every method and baseline runs the same k.
- **Every comparison reports detect@1 and detect@3.** A baseline that cannot run 3 trials is compared at 1.
- **Where runs are the real cost,** the yield-against-runs curve applies (§12.1): probes once, then repeats,
  target-present tests last.
- **k = 3 is a detection budget,** not a reliability estimate.
- **Metrics:**
  - distinct facts found (detect@1, detect@3);
  - yield per test and per run;
  - catalog coverage (facts tested out of 255, facts exposed out of tested);
  - review precision and test validity;
  - facts found only by the method;
  - the mix of failure types (skipped the check, saw the mismatch and accepted, misread the field, false "none");
  - requests and tokens.
- **Against future baselines:**
  - fix the agent, the catalog and k;
  - map each method's confirmed failures to catalog facts;
  - measure every method against the union of confirmed failures from all methods;
  - report counts with their sample sizes, and use significance only as a check.

**D6. One target-present test per scenario.**
- **Hidden-target test where a layout passes the checks** ([report.md §12.3](report.md)). Read it against the same
  decoy's probe: if the hidden-target test fails and the probe passes, the agent settled for the first candidate; if
  both fail, it misread the fact.
- **The plain cover otherwise.** It is where values written to the correct record are checked, such as the Linear
  priority scale.
- **A request whose answer is a set keeps the plain cover.**
- **This test is not the main source of findings.** Under a run budget it runs last.

**D7. Probes.**
- **A fact with several decoys:** one fact probe holding all of them first ([report.md §12.2](report.md)); its
  single-decoy probes are added when the budget allows.
- **A fact with one decoy:** its single probe.
- **Never pack decoys of different facts.** That suppressed failures: 4 of 84 against 17 of 93.

**D8. Hidden-target tests: how to build them** ([method.md](method.md) addendum, [hiding.py](hiding.py)).
- **Layout:** one decoy on the path the request leads to, and the target off every such path.
- **Checks:** the seed check and the replica check.
- **Wording:** no phrase that can describe two things. BOX-31 failed this.
- **No layouts built on a replica gap.**
- **A cheap listing of everything defeats hiding.** Hiding held in Box and CAL-09, but not in a small Linear
  workspace.
- **A probe's "none" certifies rejection, not search depth.** Adding "just tell me" to a hidden cover produced false
  "none" answers in 6 of 6 trials.

**D9. Request size is not forced** ([report.md §12.4](report.md)).
- Conditions per request vary (median 5, range 1–9), as do facts tested (median 3) and decoys (median 4). The ranges
  allow statistical analysis.
- A small ablation can cover thin tails later. This is a note for future study.

**D10. Corrections accepted.**
- BOX-09's cover failure read the creator and accepted the mismatch; it did not skip the check.
- 2 facts, not 3, are found only by covers once fact probes count.
- BOX-31 is an invalid test.

## Proposed, not yet decided

- **P4:** a hidden target plus "just tell me", once per domain, to measure false "there isn't one" answers.
- **Three outcomes for panel tests:** acted, reported the mismatch, or reported and offered the near miss.
- **A far-miss test per domain** when calibrating a new agent, to find where its policy stops.
- **The look-alike rule:** the author flags decoys of one fact that look alike on the surface, and their single probes
  are added. To be validated by the swap experiment (turn standouts into look-alikes and back: 4 fact probes × 6
  runs).
- **The request-size ablation:** requests at about 2, 5 and 8 conditions with the same decoys, if the tails are
  needed.

## Open

- **Look-alike detection.** The labels were judged by hand, and no mechanical proxy yet catches SLK-22's structural
  cue.
- **The Claude rerun** (Sonnet 5, Haiku 4.5), optionally with modified OpenClaw, to test the split between policy and
  fact.
- **Capability boundaries:** the replica gaps listed in [report.md §9](report.md).
- **Where run evidence is stored, and the merge to main.** To be recorded here once decided.
- **Method v3:** a single procedure written from this log and method.md.
