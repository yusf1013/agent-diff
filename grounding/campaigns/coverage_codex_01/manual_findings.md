# What the accepted three-model manual experiment tells us about coverage

This is a secondary analysis of the accepted 57-case Slack suite, run once each on Sonnet 5, Haiku 4.5 and Qwen 3.6 27B. It excludes the rejected Muse coverage campaign. It does not change existing verdicts, infer independent internal model faults, or claim cross-domain validation. **Resolution mode dominates the aggregate results, but does not explain all of them. There are useful structural failures, substantial repeated evidence, and confounded ambiguity tests.**

All 171 existing assessment summaries and failure/recovery explanations were read. Selected raw episodes were checked for the structural contrasts discussed below. The new mechanism annotations describe observed behavior; the original reference labels remain the authority. [Script](analyze_manual.py), [metrics](manual_metrics.json), [57-case linked matrix](manual_matrix.md), [episode annotations](manual_episode_analysis.json), and [exact changes in four selected pairs](manual_pair_changes.json) make this analysis inspectable. The script verifies byte-identical case inputs across all three model snapshots. No new model calls were made for this analysis.

## 1. Mode is a strong coarse predictor, not a sufficient explanation

These are **demonstrated grounding errors**, not the broader union of every kind of unfinished or incorrect task outcome.

| Mode | Cases per model | Sonnet | Haiku | Qwen |
|---|---:|---:|---:|---:|
| Single | 10 | 2 | 3 | 1 |
| Multiple | 10 | 0 | 2 | 0 |
| Absent | 11 | 3 | 7 | 5 |
| Underspecified | 26 | 24 | 26 | 25 |

There are 98 demonstrated grounding errors across 171 episodes. Of those, 75 occur on underspecified cases: **76.5% of errors**. But there are also **23 errors on the 93 non-underspecified episodes**. Sonnet's additional W04-absent run exhausted the turn limit without an answer or mutation; its grounding remains **not established**, so it is not the fourth demonstrated absence error.

This deliberate suite is not a random sample of Slack tasks. These proportions describe the suite and harness, not normal task prevalence or repeat-trial reliability. Multiple runs of different models on one case also do not create additional independent test designs.

## 2. The non-ambiguity errors contain concrete domain-model signal

The 23 non-underspecified errors divide into the following observed manifestations. This grouping is for diagnosis, not a proposed universal fault taxonomy.

| Manifestation | Episodes | What was confused | Model facts involved |
|---|---:|---|---|
| Relationship substitution | 8 | A message's location substituted for its author's current membership; or the author's membership substituted for the reactor's membership | Message author, message container, reaction contributor, conversation membership |
| Conditions joined across different records | 1 | Alex's reaction and another user's requested emoji treated as Alex's requested reaction | Reaction identity is message + user + emoji |
| Selection condition discarded | 6 | Wrong announcement channel, wrong message topic, non-bot user, or bot in the wrong channel | Channel identity, message text, user classification, membership |
| Invented reference evidence | 8 | Fictional tool observations, matches, or targets retained in the final account | Evidence provenance; not evidence that a particular ER relationship is difficult |

The first three groups provide **15 genuine selection errors using real environment records**. They should not be combined with the eight fabricated-evidence episodes when judging a structural coverage proposal. The [model](../../domains/slack/model.md) explicitly distinguishes the relationships, Reaction's composite identity, User's bot flag, and the derived membership/profile views used here.

### A. Membership versus message location is a real structural fault

[W08-single](../../runs/manual_comparison_01/case_reviews/W08-base.md) asks to remove the actor's fire reaction from a message **written by a member** of the launch-readiness channel. Kevin belongs to that channel and wrote the correct message in #general. Elena wrote a different message inside the launch channel but is no longer a member. All three models remove the reaction from Elena's message.

Sonnet and Haiku had already received membership evidence excluding Elena. Qwen did not fetch membership. The error therefore cannot uniformly be described as inaccessible evidence or a missing mandatory API call. The final selected relationship is wrong.

In [W08-multiple](../../runs/purdue_comparison_01/case_reviews/W08-multiple.md), Sonnet and Qwen correctly remove reactions from Kevin's two messages and exclude Elena. Haiku repeats the location substitution. The multiple variant adds one Kevin message/reaction and pluralizes the request; the rest of the seed is unchanged. This shows that the route is executable and that the observed mistake is not an invariant inability to traverse it. It does **not** establish that plurality causes improvement: the two trials also differ in target count and record content, and there are no repetitions.

### B. Same absent case, different incorrect interpretations

[W03-absent, Sonnet](../../runs/manual_comparison_01/case_reviews/W03-absent.md) discovers that no budget-approved message has Alex Rivera's celebration reaction. It then drops the budget requirement and posts in the office-relocation channel.

[Qwen on the same case](../../runs/purdue_comparison_01/case_reviews/W03-absent.md) instead selects a budget message with **Rivera's thumbs-up plus Morgan's celebration reaction**. The final answer explicitly describes those two facts as sufficient. Haiku invents a different qualifying reaction and successful post.

Thus the same absent result exposes a text-condition violation, a same-record binding violation, and fabricated evidence. The mode alone does not describe what failed, and three failed verdicts are not three replications of one demonstrated structural error.

[Qwen W04-absent](../../runs/purdue_comparison_01/case_reviews/W04-base.md) adds another role distinction: it replies to a checklist **authored by** a beta-testers member, although its rocket **reactor** is not a member. This differs from W03's split reaction and W08's message-location shortcut.

### C. Attributes and classifications matter, too

In [W09-absent](../../runs/manual_comparison_01/case_reviews/W09-base.md), no bot belongs to #incident-response. Sonnet and [Qwen](../../runs/purdue_comparison_01/case_reviews/W09-base.md) answer through a human who does belong. Haiku answers through a bot who does not belong. These are two different dropped conditions: **bot classification** and **channel membership**. An edge-only inventory would fail to name one of them.

In [W02-absent](../../runs/purdue_comparison_01/case_reviews/W02-absent.md), removing only Dana's fire reaction from the single-case seed leaves no intended recipient. Qwen and Haiku then message the reactor on a different channel's announcement; Sonnet preserves the channel condition and reports absence. The prompt is unchanged. This is a particularly clean existing contrast between finding a legitimate match and preserving all conditions when none exists.

## 3. Some apparent ambiguity evidence is masked by a different error

For all nine W08 underspecified episodes, the models fail to handle the supplied ambiguity. However:

- **Eight** select the same nonmember Elena's message, which is outside the union of legitimate alternatives.
- **One** (Haiku, channel ambiguity) invents a target instead.

Those nine runs do not isolate whether moving ambiguity along the path changes the model's choice behavior. The earlier relationship error prevents a clean comparison. Likewise, Haiku's two W06 ambiguity runs confuse message location with author membership, and Qwen's W07 removal-channel run removes Diaz from #random, outside either intended channel alternative.

Across the 75 incorrect underspecified episodes, the secondary annotations identify **57 selections/unions of genuine alternatives**, **11 additional selection-rule violations**, and **7 invented-reference cases**. These are mutually exclusive primary descriptions for this analysis; they do not imply that ambiguity handling was correct in the latter two groups. Details remain in the linked original judgments.

This distinction matters when reporting *new failure evidence*. It does not retroactively remove the designed test's coverage: the benchmark's requirements are determined before execution, independently of what a solver happened to do.

## 4. Much of the ambiguity set is repetitive, but not entirely

Two existing pairs keep the **entire seed identical** and alter singular/plural wording:

| Pair | Change | Observed result |
|---|---|---|
| W01-multiple → W01-message-underspecified | “messages” → “message” | All three succeed on the collection and fail on the unresolved singular reference |
| W02-multiple → W02-reactor-underspecified | “people” → “person” | All three succeed on the collection and fail on the unresolved singular recipient |

These strongly support a recurring distinction between retrieving matching records and having authority to act on their union. They are cleaner evidence for that issue than a complicated route that the model already misreads. They do not justify multiplying that same distinction across every possible route.

However, three underspecified episodes are correct, on three different cases:

- [Sonnet W07, person ambiguity](../../runs/manual_comparison_01/case_reviews/W07-base.md): asks which Jordan, removes neither. It fails the message and removal-channel variants of that family.
- [Sonnet W10, message ambiguity](../../runs/manual_comparison_01/case_reviews/W10-underspecified-message.md): reports both message interpretations with their separate reactor sets and roles. It fails the person and channel variants.
- [Qwen W09, bot ambiguity](../../runs/purdue_comparison_01/case_reviews/W09-underspecified.md): reports both bot/workspace alternatives. It fails the channel variant.

So “underspecified always fails” is false. The set demonstrates exceptions and useful within-family contrasts, but does not support a stable ranking of ambiguity locations. Haiku fails at every tested location, and the other models supply only three correct ambiguity episodes in total.

There are also domain-specific rationalizations inside the broad selection failure. [Sonnet W05](../../runs/manual_comparison_01/case_reviews/W05-underspecified.md) excludes the private channel because the API marks it `is_channel: false, is_group: true`, despite the adopted model including private channels as conversations. This is useful evidence about representation/type interpretation. One trial does not show that it is a separate persistent model defect rather than an improvised tie-break.

## 5. Successful cases constrain what we can honestly claim

- W01's resolved collection contains the split-person/emoji decoy and unrelated extra reactions; **all three models reject those decoys correctly**. Merely adding a split-binding negative does not guarantee failure.
- W01's message-text-emoji absence case is correct for **all three models**. The pilot supplies no evidence that this representation distinction is difficult here.
- W05's single, multiple and absent variants are correct for **all three**. Exact member counts, below/above-count negatives and a private channel did not create a general counting failure.
- W10's single, multiple and absent variants are correct for **all three**, despite its longer chain. Route length alone does not account for the results.
- No determined multiple collection produces a genuine selection error in Sonnet or Qwen. Haiku's two failures comprise one relationship substitution and one fabricated-reference episode, not a demonstrated general inability to handle collections.

Passes are meaningful coverage evidence too. We should not discard modeled distinctions just because this pilot did not find failures on them, nor claim difficulty merely from the number of edges or decoys.

## 6. A concrete minimal-cover check

I tested the user's suggestion directly, using a deliberately simple linear comparator. Across the existing 57 cases it recognizes:

| Requirement kind | Count |
|---|---:|
| Entity used as the reference target | 7 |
| Named relationship role used in selection | 8 |
| Ordinary identifying attribute | 6 |
| Derived membership count | 1 |
| Resolution mode, once suite-wide | 4 |
| **Total** | **26** |

Reference columns are counted as roles, not duplicated as ordinary attributes. Traversal direction is not an additional requirement in this comparator. This denominator is **what these cases express**, not the entire Slack model; it deliberately does not claim complete attribute, state, identity, operation, or relationship-interaction coverage. The extraction uses the fixed executable selectors, whose meaning still depends on the accepted manual cards and prompts.

An exact minimum in this finite candidate pool is **seven cases**: seven different target entities require at least seven of these single-target cases, and complete seven-case covers exist. This is not a global minimum over every possible newly authored or multi-action task.

| Equally small complete cover | Cases | Requirements covered | Recorded incorrect grounding episodes | Of those, underspecified |
|---|---:|---:|---:|---:|
| Lowest observed error count among minimum covers | 7 | 26/26 | 3/21 | 2 |
| Highest observed error count among minimum covers | 7 | 26/26 | 18/21 | 12 |

The [exact calculation and incidence matrix](manual_cover_probe.json) and [reproduction script](probe_manual_cover.py) record both case lists and the minimum-size proof. The comparison is intentionally **retrospective**: it uses already observed labels to exhibit the range admitted by the criterion, not to claim prospective test effectiveness. The higher-error cover also has three invented-reference episodes among its ambiguity failures. A higher exposure rate alone would overstate its diagnostic advantage.

There is a specific limitation: any seven-case minimum must use W05 for the membership-count requirement and therefore cannot also contain W03, another Conversation-target family. Qwen's observed split-reaction binding error occurs on W03-absent. It is invisible to every minimum cover under this criterion, even though the criterion credits all of W03's individual roles and identifying fields elsewhere. This does not prove that W03 requires a new route cell: a newly authored count-bearing Conversation test could exercise its binding contrast too. It shows why **construction and packing matter**, and why a generic set-cover solver cannot create those useful combinations on its own.

This supports investigating linear coverage rather than rejecting it. It also establishes a concrete baseline for improving the construction technique: keep the requirement list defensible, explicitly specify the discriminating alternatives, and measure which distinctions a compact suite actually preserves.

## 7. Implications for the coverage investigation

The immediate candidate is still **linear model-fact coverage with explicit discriminating alternatives**, plus a small separate set of resolution-policy checks. This is a proposal to investigate, not a validated final catalog.

1. **Count model facts, not arbitrary path instances.** Candidate requirements include relationship roles, identifying values/classifications, and relevant modeled representations or derived quantities. A natural request may use several facts, and its row table can contain a different counterexample for each. This uses more of the model than edges alone without enumerating every route.
2. **Require an observable distinction to award a fact credit.** “Member” mentioned in a prompt is weak evidence if every candidate message is both in the channel and written by its members. W08's cross-location/current-membership contrast makes the role distinction consequential. This credit rule is checked from the designed task and seed, not from the solver's chosen trajectory.
3. **Do not equate all negative construction with changing an attribute.** W03 and W04 show why facts must remain bound to the same associated record and correct role. A compiler can preserve all individual values yet build an ineffective test if those distinctions disappear.
4. **Use selected empty-result counterparts.** A positive case with excellent negatives can pass while its empty counterpart exposes fallback substitution. W02 demonstrates this with one removed reaction. This motivates controlled counterparts, not automatically multiplying every fact by all four modes.
5. **Separate broad policy checks from structural probes.** Use unambiguous cases to diagnose relationships where possible; retain a compact ambiguity panel with explicit alternatives. Investigate a new location when it can distinguish a hypothesis or exposes a new kind of record/relationship, rather than because every path needs another ambiguity case.
6. **Minimize over declared requirements, not observed failures.** The 57 cases have only seven three-model grounding-verdict signatures. Keeping one case per signature would destroy distinctions between wrong channel, wrong user classification, wrong binding, and invented evidence. A case-to-requirement matrix must preserve the facts and discriminating witnesses, even when several cases get the same verdicts.

One additional structural warning comes from the successful W10 tests. Their [full identifying path](../../runs/manual_exemplars_01/cases/W10-base.json) contains **User twice in different roles**: the reactor being reported and Priya, whose channel identifies the source checklist. This is an ordinary meaningful request, not a useless loop back to the same record. A path catalog that forbids every repeated *entity type* would miss it. A model-fact criterion can accommodate such compositions without declaring all walks to be separate requirements.

The manual suite supports this direction but cannot settle a minimal cross-domain cover. It contains ten deliberately chosen scenario families, only one domain, and one trial per model/case. Next work must define the fact-credit rules precisely, construct the incidence matrix, and challenge both the compactness and omissions in the other domains. New experiments should test those open questions rather than accumulate more copies of the already dominant underspecification result.
