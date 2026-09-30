# regen_01: the Sonnet-written half, regenerated with Muse

Session "regen", started by the lead session ("RoadMap specialist") from the brief
[regen.md](../../protocols/briefs/regen.md), under the [shared rules](../../protocols/briefs/README.md).

## Status

- **2026-09-30 02:45 EDT. Running on OpenClaw** with the self-hosted Qwen (on trojai4, the lead's go): `full_01`,
  then `absence_01`, then `underspecified_01`, 3 trials, 12 in flight (the lead lowered it from 16 when the shared
  host was overloaded). 1,008 executions: 336 tests, the probe of G4-SLK-14's newly flawed near miss left out.
- **Funnel:** 35 briefs, 37 attempts, 34 accepted; my review: 22 valid, 6 weak but valid, 6 flawed but usable; 7 of
  135 near misses flawed (in `known_defects.json`), 8 borderline flagged. Coverage: 76 of the briefs' 82 facts, 74 of
  Sonnet's 81 credited. Muse so far: $38.87 at list price, $2.38 billed ([eval/funnel.json](eval/funnel.json)).
- **Next:** my labels of the 100 blind trials as they finish (before any verdict), then judge v2, then the score.

## The question

How can the frozen pipeline (tag `grounding-freeze-01`, as completion_01 ran it), with Muse as the writer,
regenerate valid tests for the briefs that autogen_01's Sonnet writer covered, so that the whole evaluated suite
comes from one pipeline version and one writer? And what does the regenerated half give, against the Sonnet half:
the generation funnel, the facts covered (against Sonnet's 81), the facts exposed on OpenClaw, the judge's accuracy,
and the cost?

Why: 271 of the 565 regular tests, and their policy units, come from the 49 scenarios Sonnet wrote in autogen_01
while the method was still being tuned. The PI does not want a suite that mixes writers. The Sonnet suite stays as it
is, as a record and for a later writer comparison.

**What a good result is:** every brief has an accepted scenario that my review finds valid; the facts the Sonnet
half covered are covered again, by valid near misses; three facts get their designated near miss where a valid one
exists (below). **How it is checked:** the pipeline's own checks and cold reader, then my review of every accepted
scenario and every policy variant, before any run; coverage by the credit rule on the derived tests.

## Layout

| Path | What |
|---|---|
| [inputs/make_briefs.py](inputs/make_briefs.py), [inputs/briefs_regen.json](inputs/briefs_regen.json) | The briefs and their mapping to the Sonnet briefs |
| [generate.py](generate.py) | completion_01's generator call, unchanged but for the briefs file: Phase 4's generator on the frozen kit |
| `runs/gen_*` | One folder per generation batch or retry (versions, checks, reader, outcome, accepted case, `calls.jsonl`) |
| [batches.py](batches.py) | Per batch: attempts, accepted, rejected and why, rounds, calls and cost |
| [eval/review.json](eval/review.json) | My validity review of every accepted scenario, before any run |
| [cases.py](cases.py) | The accepted scenario used per brief (one; inputs/choices.json names it if a brief has several) |
| [suite.py](suite.py), [policy_units.py](policy_units.py), [variants.py](variants.py) | completion_01's suite, policy-unit and drop-F scripts, pointed at this study |
| [rules.py](rules.py) | openclaw_eval_01's rulings taught this study's opaque ids, with the 10-minute budget |
| [view.py](view.py) | My review viewer: a scenario's history, request, near misses and whole seed (never agent input) |
| [defects.py](defects.py) | Writes my flawed near misses (and, later, invalid variants) into `roadmap_01/known_defects.json` |
| [coverage.py](coverage.py) | Facts covered by a valid near miss, against the briefs' facts and Sonnet's credited facts |
| [run.py](run.py), [cut.py](cut.py), [blind.py](blind.py) | The runner (openclaw_eval_01's, with rules.py), the cases folders the runs read, the stratified blind sample |
| [label_view.py](label_view.py), `eval/labels_<run>.json` | My blind labels, from the judge's evidence without the triage, written before any verdict |
| [score.py](score.py) | The regular score: adjudicate.py's logic (reproduces openclaw_eval_01's full_04 exactly), the exposure filter, timeouts under host load |
| [policy_decide.py](policy_decide.py) | The policy decisions for a Muse-only suite (Phase 4, 6b and this study's units; reproduces openclaw_eval_01's Phase 4 and 6b figures) |
| [compare.py](compare.py), [funnel.py](funnel.py), [duplicates.py](duplicates.py) | The halves side by side; the funnel and costs; duplicate units |

## The briefs (step 1)

autogen_01 made 50 brief attempts: arm R's 18, arm P's 16 and arm P v2's 16. Their format is already the frozen
pipeline's (`scenario_id`, `domain`, `facts`); the facts are copied unchanged.

- **35 briefs** ([briefs_regen.json](inputs/briefs_regen.json), built by [make_briefs.py](inputs/make_briefs.py)):
  - **34 distinct fact sets.** Arm P and arm P v2 are the same 16 fact sets under two method versions (the v2 run
    was a method comparison). Under one frozen pipeline a second generation is a replicate, so each set gets one
    brief. AP-LIN-03 (rejected) and AP2-LIN-03 (accepted) are one of them.
  - **The related-issue brief**, G4-LIN-35: `R:IssueRelation.relatedIssueId` alone. Muse's G4-LIN-17 credited it
    only through a plain near miss; its designated substitute is the reversed direction.
- **Ids** continue Phase 4's numbering (G4-BOX-16 to 21, G4-CAL-11 to 16, G4-LIN-22 to 35, G4-SLK-10 to 18), as
  completion_01 did for its new briefs. The frozen code recognizes generated scenarios by their prefix, and the
  PI's rulings are keyed by the Sonnet scenarios' ids, which new scenarios must not reuse.
- **Facts:** the 35 briefs name 82 facts: Sonnet's 81 brief facts and the related-issue fact. Sonnet's 81
  *credited* facts differ by one each way:
  - `H:IssueLabel.parentId` is in AR-LIN-25's brief (G4-LIN-26 here), but that scenario was invalid, so Sonnet never
    covered it;
  - `B:EventAttendee.event_id` is credited to Sonnet through a near miss outside any brief (AR-CAL-23's split
    attendee). Muse's G4-CAL-07 covers it too, so the suite keeps it either way.

| New | Sonnet | Facts |
|---|---|---|
| G4-BOX-16 | AR-BOX-21 | A:Folder.created_at, D:Folder.item_count, R:Folder.collections, R:Folder.modified_by_id |
| G4-BOX-17 | AR-BOX-22 | A:File.name, R:Hub.updated_by_id, R:HubItem.file |
| G4-BOX-18 | AR-BOX-23 | A:File.description, A:File.extension, A:File.size, D:File.comment_count |
| G4-BOX-19 | AR-BOX-24 | A:Task.created_at, A:Task.message, A:User.login |
| G4-BOX-20 | AP-BOX-01 = AP2-BOX-01 | A:Folder.size, A:Folder.shared_link, A:Folder.modified_at |
| G4-BOX-21 | AP-BOX-02 = AP2-BOX-02 | A:File.created_at, A:Comment.created_at |
| G4-CAL-11 | AR-CAL-21 | A:Event.description, A:Event.end |
| G4-CAL-12 | AR-CAL-22 | A:Calendar.description |
| G4-CAL-13 | AR-CAL-23 | A:EventAttendee.email, A:EventAttendee.optional |
| G4-CAL-14 | AR-CAL-24 | A:Calendar.location |
| G4-CAL-15 | AP-CAL-01 = AP2-CAL-01 | A:Calendar.summary, A:CalendarListEntry.selected |
| G4-CAL-16 | AP-CAL-02 = AP2-CAL-02 | R:CalendarListEntry.calendar_id, B:AclRule.calendar_id |
| G4-LIN-22 | AR-LIN-21 | A:Issue.createdAt, R:Issue.creatorId, R:Issue.teamId |
| G4-LIN-23 | AR-LIN-22 | R:Document.projectId, R:Document.updatedById |
| G4-LIN-24 | AR-LIN-23 | R:Comment.resolvingUserId |
| G4-LIN-25 | AR-LIN-24 | A:Cycle.number |
| G4-LIN-26 | AR-LIN-25 | H:IssueLabel.parentId |
| G4-LIN-27 | AR-LIN-26 | R:issue_subscriber_user_association |
| G4-LIN-28 | AP-LIN-01 = AP2-LIN-01 | A:Issue.completedAt, A:Issue.description, R:Issue.stateId |
| G4-LIN-29 | AP-LIN-02 = AP2-LIN-02 | A:User.email, A:User.name, A:User.guest |
| G4-LIN-30 | AP-LIN-03 = AP2-LIN-03 | A:Team.key, A:Team.description, A:Team.private |
| G4-LIN-31 | AP-LIN-04 = AP2-LIN-04 | A:Cycle.name, A:Cycle.startsAt, B:Issue.cycleId |
| G4-LIN-32 | AP-LIN-05 = AP2-LIN-05 | A:Comment.createdAt, A:Comment.resolvedAt, B:Comment.issueId |
| G4-LIN-33 | AP-LIN-06 = AP2-LIN-06 | A:Attachment.title, A:Attachment.url, R:Attachment.issueId |
| G4-LIN-34 | AP-LIN-07 = AP2-LIN-07 | A:Document.title, A:Document.content, R:Document.teamId |
| G4-LIN-35 | (new) | R:IssueRelation.relatedIssueId |
| G4-SLK-10 | AR-SLK-21 | A:Message.created_at, R:messages.channel_id, R:messages.user_id |
| G4-SLK-11 | AR-SLK-22 | H:messages.parent_id, R:messages.user_id |
| G4-SLK-12 | AR-SLK-23 | A:Conversation.is_private, A:Conversation.purpose_text |
| G4-SLK-13 | AR-SLK-24 | R:channel_members |
| G4-SLK-14 | AP-SLK-01 = AP2-SLK-01 | A:User.username, A:User.display_name, A:User.real_name |
| G4-SLK-15 | AP-SLK-02 = AP2-SLK-02 | A:Conversation.channel_name, A:Conversation.topic_text, A:Conversation.is_archived |
| G4-SLK-16 | AP-SLK-03 = AP2-SLK-03 | A:Reaction.reaction_type, R:message_reactions, B:message_reactions.user |
| G4-SLK-17 | AP-SLK-04 = AP2-SLK-04 | D:reply_count, A:Message.message_text, B:messages.user_id |
| G4-SLK-18 | AP-SLK-05 = AP2-SLK-05 | D:member_count, A:Conversation.created_at, A:WorkspaceMembership.role |

## The three facts that need their designated near miss

The brief asks for the lure, not a plain different value, for three facts. The PI has already ruled two of those
lures flawed (group B: a natural reading of the request includes them), in
[known_defects.json](../roadmap_01/known_defects.json):
- **`A:Cycle.number`**, lure "a cycle named 'Cycle 4' whose number isn't 4": AR-LIN-24's `i-web-101` is exactly
  this, ruled flawed ("a user saying 'Cycle 4' can mean the cycle displayed with that name"). It can be valid only
  if the request itself fixes the number reading, which the frozen writer cannot be told.
- **`A:Message.message_text`**, lure "the words only in the formatted blocks": AP-SLK-04's `U_OMAR` and AP2-SLK-04's
  message, ruled flawed ("the blocks are what Slack shows"). A valid form may not exist in this service.
- **`R:IssueRelation.relatedIssueId`**, lure "the relation pointing the other way": no ruling against it; its own
  brief, G4-LIN-35.

Nothing in the pipeline is changed for them: the writer already sees each fact's designated substitutes and is told
to prefer them. My review applies the PI's rulings to whatever comes back.

**The lead's answer (2026-09-30):** the rulings in `known_defects.json` decide, not the brief.
- **`A:Cycle.number` and `A:Message.message_text`:** a plain near miss is the acceptable form. They join the facts
  whose designated lure is unavailable. A name lure or a blocks lure that comes back is reviewed under the 09-28
  rulings (flawed).
- **A tension for the PI, recorded, not acted on:** [blind_review_01](../blind_review_01/README.md) (a Codex
  review of 2026-09-29) records later PI adjudications: "PI rules also require the cycle's number for Cycle 4"
  (which would make the name lure valid), and a Slack decision "conditional on a real structured-card distinction"
  between section-block cards and plain text. Both sit beside the 09-28 rulings, which this study follows.
- **`R:IssueRelation.relatedIssueId`** keeps its own brief, G4-LIN-35. If its accepted scenario has only a plain near
  miss on the fact, I generate the brief again under a new run name, at most 3 attempts in all, every attempt logged
  (a choice on a construction property, never on a solver outcome). If still plain, it is reported so.

## Settled with the lead (2026-09-30)

- **Second draws** for the two rejected briefs (G4-LIN-30, G4-SLK-18): one each, run `gen_04`, counted as attempts.
  No draw for the two facts whose only near miss is the ruled-flawed designated one; they go to the PI as a finding.
- **Main merged in** (the lead merged this branch into main, 7dfd8ab40e, then main came back here): `rulings.py` now
  has the 10-minute budget and the duplicate-unit rule itself, so `rules.py` only adds this study's id folder (and
  any duplicate units the derivation makes). `known_defects.json` holds my 5 rulings and 2 the lead added from the
  PI's blind-review rulings (G4-BOX-11, G4-BOX-02).
- **Coverage credit follows the F0 rule** (roadmap, decisions of 2026-09-29): the designated near miss; a plain miss
  only where the domain model names no alternative, and for A:Cycle.number and A:Message.message_text.
- **Exposure is counted only for facts with a valid near miss in the scenario.** A cover trial that acts on the
  target and on a flawed near miss is otherwise counted (`trial_not_counted` fires only when every acted-on record is
  flawed), and would credit the flawed near miss's fact. The lead agreed.

- **35 briefs,** one per distinct fact set; arm P v2 is not replicated. Coverage is reported against both fact lists
  (the briefs' 81 and Sonnet's credited 81).
- **My rulings on new near misses** go into `roadmap_01/known_defects.json` on this branch, in a separate block keyed
  by the new ids, listed in this README; the lead merges.
- **Ids** continue Phase 4's numbering; the suite index carries `source` = `regen_01/runs/gen_NN`. report_01 is not
  edited here: when done, I tell the lead what its `WRITERS` map needs.

## Generation (step 2)

Each brief was generated once through the frozen generator (writer, code checks, replica pre-checks, cold reader;
up to 6 check rounds and 2 reader rounds), in three batches. Per brief: [batches.py](batches.py).

| Batch | Briefs | Accepted | Rejected | Muse calls (failed) | List price | Billed |
|---|---:|---:|---:|---:|---:|---:|
| `gen_01` (pilot) | 4 | 4 | 0 | 24 (0) | $2.94 | $0.18 |
| `gen_02` (Box, Calendar, Slack) | 18 | 17 | 1 | 113 (1) | $13.01 | $0.78 |
| `gen_03` (Linear) | 13 | 12 | 1 | 65 (2) | $9.50 | $0.54 |
| `gen_04` (second draws, the lead's yes) | 2 | 1 | 1 | 23 (1) | $2.62 | $0.16 |
| **All** | **37 attempts of 35 briefs** | **34** | **3** | **225 (4)** | **$28.07** | **$1.67** |

- **Rejected, both by the cold reader for unnatural wording** (the pipeline's final answer on a brief; no retry
  without the lead's word):
  - **G4-LIN-30** (team key, description, privacy; Sonnet's AP-LIN-03 failed the same way in arm P): three
    versions, each identifying a team by its privacy flag, a key fragment and its description, read as "constructed
    to force a lookup".
  - **G4-SLK-18** (member count, channel creation date, workspace role): six check rounds (a seed-helper argument,
    duplicate users, a near miss that also matched, a creation date no read shows as a date, a type error), then
    three reader rounds ("a real user would name the channel").
- **Second draws** (`gen_04`): G4-SLK-18 accepted after 6 versions; G4-LIN-30 rejected again by the reader, for
  the same reason (a team named by its privacy flag, a key fragment and its description reads as constructed). So
  the frozen pipeline covers none of the three team facts: a finding, not a retry.
- **The 4 failed calls** were Muse stream timeouts (180 s idle), on G4-LIN-30's and G4-SLK-18's writers; the
  orchestrator resumed the same session, as it does after a missing scenario. They are counted in the costs.
- **What the checks caught** (per version: [batches.py](batches.py), each brief's `outcome.json`): invalid JSON (the
  most common: 13 versions), query nodes without a table or a wrong key, near misses the claim check did not kill,
  anchors that vanished with the target, write calls with GraphQL syntax errors, unreadable values, and reader
  findings: stacked metadata wording, attachment ambiguities, undeclared near misses, a near miss failing two
  conditions.

## My review (step 3)

Every accepted scenario, before any run ([eval/review.json](eval/review.json)), by the PI's criteria of 2026-09-28 and
the rulings in `known_defects.json`: a near miss is flawed when the agent cannot check it, or when a natural reading of
the request includes it; ambiguous ones case by case. Read with [view.py](view.py) and the replica's reads.

| | Count |
|---|---:|
| Scenarios reviewed | 34 |
| Valid | 22 |
| Weak but valid (contrived; impossible times) | 6: G4-BOX-19, G4-BOX-21, G4-LIN-24, G4-LIN-28, G4-LIN-29, G4-LIN-32 |
| Flawed but usable (a near miss flawed, the rest kept) | 6: G4-LIN-25, G4-CAL-15, G4-SLK-14, G4-SLK-15, G4-SLK-17, G4-SLK-18 (the last two also contrived) |
| Invalid | 0 |
| Near misses declared | 135 |
| Near misses flawed | 7 |
| Near misses valid but borderline (flagged for the PI) | 8 |

**The 7 flawed near misses** (all group B; in `known_defects.json`, `near_misses`, source "regen_01: …"):
- **G4-LIN-25 `i-f1`:** a cycle *named* "Cycle 7" but numbered 9, for "cycle 7": the PI's AR-LIN-24 ruling.
- **G4-CAL-15 `ev_kickoff_social`:** a calendar the user's own list shows as "Editorial Calendar" (its override),
  for "my Editorial Calendar".
- **G4-CAL-15 `ev_kickoff_draft`:** a second "Editorial Calendar" of the user's, only not selected for display; the
  accepted wording no longer names the display flag, which Sonnet's AP-CAL-01 and AP2-CAL-01 did.
- **G4-SLK-15 `C_DEPLOY`:** "the active launch channel" names no channel, and #deploy-ops, whose purpose is "Launch
  coordination for the go-live", is such a channel: the PI's AP-SLK-02 ruling.
- **G4-SLK-17 `U_FELIX`:** the words only in the message's blocks, which Slack displays: the PI's AP-SLK-04 ruling.
- **G4-SLK-14 `1789992600.000003`** (ruled 2026-09-30 after the cut, while the runs were going, before any label or
  verdict): its fire reaction is from Marcus Webb Jr, and "Marcus Webb", unquoted, includes him. The PI ruled in
  blind_review_01 that "the Seaport Archive folder" includes "Seaport Archive 2024" although an exact one exists
  (known_defects G4-BOX-11); a generational suffix is dropped like a year. `A:User.real_name` loses its only near miss.
- **G4-SLK-18 `1711109400.000003`:** "the small 5-person release channel": release-hub has six members counting the
  bot, as Slack does, but five *people*, while the target has four people and the bot. The PI's ruling that the bot
  counts as a member was about "members"; "5-person" counts people. The drop-F writer declined a variant for the same
  reason. Ruled flawed so that a trial acting on it does not count; the target stays right under the member count.

**Weak but valid:** G4-BOX-19 (task assignments dated before their tasks), G4-BOX-21 (a comment dated before its file
existed), G4-LIN-28 (issues last updated before their completion), G4-LIN-24 and G4-LIN-32 (comments resolved
after their last update; found by a mechanical scan of every scenario after the review, before any verdict), G4-LIN-29 (look-alike users, a display name that
is someone else's email), G4-SLK-14 (three people named by three kinds of identifier); and G4-SLK-18 (channel topics
that repeat the creation date for the pre-check, channels named for their month).

**Replica defects met, reported, not fixed:** Linear's `documentUpdate` and `attachmentUpdate` apply the change but
answer with an error (G4-LIN-23, G4-LIN-33, G4-LIN-34); the nested `issue { attachments }` connection fails
(G4-LIN-33); the issues filter on subscribers is ignored (G4-LIN-27). All three are in the replica notes judge v2
reads; none makes a test unanswerable.

## Coverage

By [coverage.py](coverage.py) ([eval/coverage.json](eval/coverage.json)): a fact is covered when an accepted scenario
holds a near miss on it that my review does not rule flawed; credit follows the F0 rule.

| | Covered and credited | Of |
|---|---:|---:|
| The briefs' facts | 77 | 82 |
| Sonnet's credited facts (report_01) | 75 | 81 |
| Through a designated near miss (F1 to F8) | 69 | 77 covered |

- **Gained against the Sonnet half:** `H:IssueLabel.parentId` (G4-LIN-26, F4; one of the nine servable facts no
  valid scenario covered); `A:Cycle.number` now with a designated near miss (G4-LIN-25, F8) where Sonnet's was F0
  only; `R:IssueRelation.relatedIssueId` with the reversed direction (G4-LIN-35, F3), the lure the brief asked for.
- **Recovered by the second draw:** `D:member_count`, `A:Conversation.created_at`, `A:WorkspaceMembership.role`
  (G4-SLK-18).
- **Not covered (5 of the briefs' facts), two findings for the PI:**
  - **The team facts** `A:Team.key`, `A:Team.description`, `A:Team.private`: G4-LIN-30 was rejected twice by the cold
    reader, each time because naming a team by its privacy flag, a key fragment and its description reads as
    constructed (Sonnet's arm P failed the same set once, and its v2 passed). No other Muse scenario covers them.
  - **The designated substitute is a ruled-flawed construction:** `A:Message.message_text` (G4-SLK-17: the words only
    in the blocks) and `A:CalendarListEntry.selected` (G4-CAL-15: a display flag the wording no longer names). The
    method tells the writer to prefer designated substitutes, and for these two facts that is exactly what the PI's
    rulings make flawed; the wording that would make the selected flag valid ("that's selected for display") is what
    the reader pushes out as unnatural. A second draw would most likely reproduce both, so none was run (the lead).
- **Not in any brief:** `B:EventAttendee.event_id` (Sonnet's AR-CAL-23 split attendee); Muse's G4-CAL-07 covers it.
- **Covered only through plain near misses (8):** A:Folder.shared_link, A:EventAttendee.optional,
  A:Comment.resolvedAt, A:User.guest, A:Conversation.channel_name, A:Conversation.is_archived,
  A:Conversation.is_private, A:Reaction.reaction_type. None has a designated substitute in the catalog, so under the
  F0 rule the plain miss is the alternative and earns credit.

## The funnel against the Sonnet half (report_01's Table 5)

The Sonnet column is report_01's (autogen_01's arms R, P and P v2, as reported there). The writers had the same fact
sets, but the Sonnet half drew the 16 arm-P sets twice (P and P v2, as a method comparison), and here each set once
(plus two second draws, and the related-issue brief). So the columns compare one frozen pipeline with Muse against
the Sonnet runs as they were, not two draws of the same design.

| | Sonnet (autogen_01) | Muse (this study) |
|---|---:|---:|
| Briefs (distinct fact sets) | 34 | 35 (34 + the related-issue brief) |
| Brief attempts | 50 | 37 |
| Accepted scenarios | 49 | 34 |
| Attempts rejected | 1 | 3 |
| Usable scenarios after review | 48 | 34 |
| Declared near misses | 185 | 135 |
| Near misses ruled flawed | 7 | 7 |
| Derived regular candidates | 285 | 216 |
| Dropped: near miss loses its distinguishing condition | 5 | 4 |
| Further cases excluded by validity rulings | 9 | 6 |
| **Valid regular cases** | **271** | **206** |
| Valid absence units | 116 | 72 |
| Valid underspecified units | 98 | 59 |
| Facts covered by a valid near miss | 81 (report_01's credited count, of its 81 brief facts, before the F0 rule) | 76 of 82 (all credited under the F0 rule) |
| Writer cost, list price (billed) | $208 (subscription, $0) | $28.07 ($1.67); with the drop-F variants $38.87 ($2.38) |

## The policy variants (step 3, continued)

autogen_02's drop-F derivation, unchanged, on the accepted scenarios (`runs/dropf_01` for the first 33,
`runs/dropf_02` for G4-SLK-18's second draw): one job per fact, the Muse writer rewords the request without the
condition, code checks it, the cold reader reads it, up to two repairs. Then my read of every accepted variant
([eval/variant_review.json](eval/variant_review.json), with [variant_view.py](variant_view.py)), with the one
question: can the action be done to each intended match?

| | Count |
|---|---:|
| Jobs | 80 |
| Accepted | 64 |
| Rejected by the reader / declined by the writer / not derivable by code | 8 / 5 / 3 |
| Read as invalid (in `known_defects.json`, curated, leave out) | 4 |
| Duplicate of another unit (the PI's rule: one test; `rules.DUPLICATES`) | 1 |
| **Valid underspecified units** | **59** |

- **The 4 invalid:** `U-G4-CAL-15-CalendarListEntry_selected` (the display flag had no words, so the request is the
  original's, which also fits the flawed near misses); `U-G4-CAL-16-CalendarListEntry_calendar_id` (two of its three
  matches are calendars off the user's list, which the agent cannot list); `U-G4-SLK-17-reply_count` and
  `U-G4-SLK-18-WorkspaceMembership_role` (each keeps a flawed near miss that a natural reading makes a match).
- **The duplicate:** `U-G4-SLK-16-message_reactions_user` has the same request, actor and seed as
  `U-G4-SLK-16-message_reactions` (two facts of one reaction clause); found by [duplicates.py](duplicates.py).
- **Absence twins:** code derives them (autogen_02's `absence_twins`): 80 candidates, 2 dropped by the derivation
  (the near miss no longer fails its fact once the target is gone), 6 left out by the rulings (they hold a flawed
  near miss): **72 valid**.

## The suite (step 4)

Built as completion_01 built 6b's: [suite.py](suite.py) (every test equals the frozen derivation's, then opaque
ids, with the same checks, then the clock: the moment each scenario was written, since no scenario has an event
after it), [policy_units.py](policy_units.py) (the units, with the same ids and clocks), and [cut.py](cut.py) (the
cases folders the rulings keep, cut once).

| Run | Cases folder | Tests | Left out | Executions at 3 trials |
|---|---|---:|---:|---:|
| `full_01` (covers, probes, fact probes) | `runs/full_01_cases` | 206 | 6 probes holding a flawed near miss | 618 |
| `absence_01` | `runs/absence_01_cases` | 72 | 6 twins holding a flawed near miss | 216 |
| `underspecified_01` | `runs/underspecified_01_cases` | 59 | 4 invalid, 1 duplicate | 177 |
| **All** | | **337** | | **1,011** |

- **Regular tests by form:** 34 covers, 127 probes, 45 fact probes (216 derived: 135 probes and 47 fact probes
  before the witness check dropped 2 of each, and the rulings 6 probes).
- **Ids:** 638 made-up ids replaced by opaque ones; every check passed (the derivation commutes, no old id left, the
  reference check selects the same records).
- **The blind sample** ([blind.py](blind.py), seed 5311, drawn before any run from the cases folders alone): 5
  trials in each of 20 strata (4 services × cover, probe, fact probe, absence, underspecified), 100 in all
  ([eval/blind_strata.json](eval/blind_strata.json), `eval/blind_<run>.json`).
- **For report_01's `WRITERS` map:** the suite index's `source` is `regen_01/runs/gen_01` to `gen_04` (writer: Muse).

## Cost

| | Muse calls | List price | Billed |
|---|---:|---:|---:|
| Generation (4 batches) | 225 | $28.07 | $1.67 |
| Drop-F variants (2 runs) | 279 | $10.80 | $0.72 |
| **All so far** | **504** | **$38.87** | **$2.38** |

## For the PI (from this study)

- **One pattern, three rulings:** the requested words sit in a sibling text field. G4-CAL-11 `ev_plan_loc` (the
  roadmap in the event's *location*, for "covering the roadmap") and G4-CAL-12 `ev_panel_f1` ("onsite interviews" in
  the calendar's *location*, for "about onsite interviews") are ruled valid: a location says where, not what about.
  G4-SLK-15 `C_DEPLOY` ("Launch coordination" in the channel's *purpose*, for "the launch channel") is ruled flawed:
  a purpose says what a channel is for, and the request names no channel (AP-SLK-02). One ruling on the pattern
  would settle all three.
- **A second pattern, qualifier or new meaning:** after the PI's Seaport Archive ruling (an unquoted name includes
  the same name with a qualifier such as a year), "Marcus Webb Jr" is ruled flawed for "Marcus Webb", while "Sprint 22
  Overflow" for "the Sprint 22 cycle" (G4-LIN-31) and "Editorial Calendar Archive" for "my Editorial Calendar"
  (G4-CAL-15) stay valid: "Overflow" and "Archive" name a different thing. If the PI extends the ruling to them, G4-CAL-15
  keeps no valid near miss and `A:Calendar.summary` goes with it. Handles and quoted names (`#launch-plans`,
  `nadia.rahman.khan`, `sarod_ops`, a quoted file or document title) are exact and stay valid.
- **The folder-descendants ruling and its Linear analogue:** the PI allows descendants for folder containment
  (known_defects G4-BOX-02); G4-LIN-26's label nested in Platform's Mobile group is the same shape for label groups,
  ruled valid here with the lead's sub-team rulings. None of this study's Box near misses is a subfolder copy.
- **The 8 borderline near misses ruled valid:** G4-LIN-22 `i-d4` (a sub-team's issue for "in the Web team", as
  G4-LIN-15); G4-LIN-26 `i-web-2` (an Android label nested in Platform's Mobile group; blind_review_01 records the PI
  allowing descendants for folder wording); G4-LIN-31 `c-num` (cycle number 22 named "Cycle 22", for "the Sprint 22
  cycle"; contested under blind_review_01's number reading); G4-LIN-34 `d-team-decoy` (a document in a *project*
  named Payments, for "in the Payments team", as AP-LIN-07's d-team-f1 but with identical names); G4-LIN-31
  `c-overflow` and G4-CAL-15 `ev_kickoff_arch` (above); G4-SLK-15 `C_RELEASE` (#release-ops, never called "launch");
  G4-BOX-18 `8217` (two comments and a reply, for "only has the two comments").
- **The designated substitutes of two facts are ruled-flawed constructions,** and the team facts are out of the
  frozen pipeline's reach (Coverage, above).
- **"5-person" and the bot** (G4-SLK-18): ruled flawed here; the PI's bot ruling was about "members".

## Log

- **2026-09-30 00:06 EDT, cycle 0 (setup).** Read the shared rules, the brief, the PI's notes, the roadmap, the
  concise report, and completion_01, autogen_01, autogen_02's generator and openclaw_eval_01. Checked: since the tag,
  the generation path (autogen_01's kit but `opaque_ids.py`, autogen_02's generator, the inputs, the domain models)
  is unchanged; only the OpenClaw integration, `opaque_ids.py` and the drop-F naming fix changed. Local services up
  (AgentDiff health 200 on :18001, the campaign Postgres on :15432, Muse's key present). Wrote the briefs and
  generate.py.
- **00:07 to 00:30 EDT, cycle 1 (pilot, `gen_01`).** G4-BOX-16, G4-CAL-11, G4-LIN-35, G4-SLK-10, concurrency 4.
  - **4 of 4 accepted:** G4-CAL-11 after one reader round ("unnatural" wording); G4-LIN-35 after one check round (a
    mutation type outside the format); G4-SLK-10 after one (invalid JSON); G4-BOX-16 after one check round (an
    item-count near miss the claim check did not kill) and two reader rounds (four stacked metadata conditions read
    as test filters, until a conversational wording passed).
  - **Cost:** 24 Muse calls (10 writer, 14 reader), $2.94 at list price, $0.18 billed; 7 to 23 minutes per brief.
  - **My review:** all 4 valid ([eval/review.json](eval/review.json)). G4-LIN-35's `i-rev` is the lure the brief
    wanted (it blocks Checkout rollout rather than being blocked by it); the replica reads both directions
    (`relations`, `inverseRelations`).
  - **Learned:** the plumbing holds (Muse, the replica pre-checks, the reader); the reader pushes multi-condition
    metadata requests toward conversational wording, as in Phase 4.
- **Tooling written while the pilot ran:** the suite, policy-unit and drop-F scripts (completion_01's, pointed here),
  `cases.py`, and `rules.py`. `rules.py` exists because openclaw_eval_01's `rulings.py` finds opaque ids only in 6a's
  and 6b's id folders, so a flawed near miss of this study would not be recognized under its opaque id. It also still
  reads the withdrawn 8-minute budget. `rules.py` adds this study's id folder and uses 10 minutes, without editing
  openclaw_eval_01. The `.gitattributes` LFS pattern for this study's transcripts mirrors completion_01's.
- **00:32 to 01:35 EDT, cycle 2 (`gen_02`, `gen_03`, run side by side, concurrency 6 and 5).** 31 briefs: 29
  accepted, 2 rejected (G4-SLK-18, G4-LIN-30; above). Reviewed each scenario as it landed.
  - **Learned, about the writer:** Muse realizes the designated substitute when one exists (the reversed relation,
    the cycle's name, the message's blocks, the calendar-list override), which is right for coverage and wrong where
    the PI has ruled that construction flawed. Its most common defect is invalid JSON, which the checks return.
  - **Learned, about validity:** the recurring review questions are containment (sub-team, nested label group,
    project for team), display names (list override, cycle name, display name), and where a word sits (location,
    purpose, blocks). Dates are safe: every date-bearing value sits 10:00 to 16:00 UTC or has no zone.
  - **Kept for the PI:** the three sibling-field cases and the seven borderline near misses (above).
- **01:30 EDT, cycle 3 (the drop-F derivation, `runs/dropf_01`)**, started on the 33 accepted scenarios; each
  accepted variant gets my read before it runs.
- **01:40 EDT.** `defects.py` wrote the 5 flawed near misses into `roadmap_01/known_defects.json` (the lead's option
  (a)); the advisor agreed with the flawed set and suggested presenting the sibling-field cases together, retrying
  only the rejected briefs, and filtering exposures to facts with a valid near miss when scoring (a cover trial that
  acts on the target and a flawed near miss is otherwise counted).
- **01:40 to 02:10 EDT, cycle 3 (the variants).** `runs/dropf_01`: 77 jobs, 62 accepted; read every accepted variant
  as it landed (58 valid, 3 invalid, 1 duplicate). The lead said yes to a second draw of the two rejected briefs
  (`gen_04`): G4-SLK-18 accepted, G4-LIN-30 rejected again. Main merged back in (the lead's merge of this branch, the
  10-minute budget and the duplicate-unit rule in `rulings.py`, 2 more flawed near misses from the PI's blind-review
  rulings); `rules.py` cut down to the id folder and this study's duplicates; the F0 rule applied in coverage.
  - **Learned:** the drop-F writer's declines are informative. For G4-SLK-18 it declined because '5-person' leaves "a
    bot-vs-human counting ambiguity", which made me rule that near miss flawed. Variants whose dropped condition had
    no words of its own (the display flag) repeat the original request, which exposes the original's flaw.
- **02:10 to 02:30 EDT, cycle 4 (the suite).** G4-SLK-18's review and variants (`runs/dropf_02`: 2 accepted, 1 read
  invalid); `suite.py`, `policy_units.py`, `cut.py`: 337 tests; the blind sample (seed 5311). Ready to run.
