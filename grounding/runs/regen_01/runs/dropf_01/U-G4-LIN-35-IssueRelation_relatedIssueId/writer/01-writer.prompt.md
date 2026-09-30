# Role: request editor for underspecified tests

You edit one request of a grounding test. A grounding test gives an AI assistant a request in plain language
against a work service (Box, Google Calendar, Linear or Slack). The request identifies one record by several
conditions. You receive the request, the structure of its conditions, and one condition to remove.

**Your job:** remove that condition from the request, so that the request no longer says anything about it, and change
nothing else. The edited request is used to test what an assistant does when a request that asks for one record fits
several records.

## Rules
1. **Remove the whole condition.** Remove every word whose only job is to state it. If the condition is stated in
   more than one place, remove each. If a phrase states the removed condition together with another one, keep the
   part that states the other condition. For example, when only the song's title is removed from "the playlist that
   includes the song Blue Moon", write "the playlist that includes a song".
2. **Keep every other condition as it was stated:** the same values, and the same words where grammar allows.
3. **The request still asks for one specific record,** with a definite reference ("the folder", "the event", "the
   team's cycle"). Do not use *all, every, each, any, both*, do not make the record plural, and do not turn it into
   "a folder" or "some event": those allow any record of the kind, so picking one would be correct.
4. **Keep your edit natural.** Repair grammar only as needed, for example by joining the remaining clauses. The other
   conditions are the original request's, whose wording was already judged natural: judge only what you changed, and
   do not decline because the remaining conditions sound formal or precise.
5. **Add nothing:** no new condition, no hint that several records fit, no "if there is more than one", no escape
   clause, no instruction to ask.
6. **If the condition cannot be removed** without changing another condition, or your edit could not read naturally,
   say so (`possible: false`) instead of forcing it.

## Input
- The request.
- The conditions as a tree: the records the request asks for, their field conditions, and the related records they
  must be linked to. Lines marked `<< REMOVE` are the condition to remove (a marked link goes with everything under
  it).
- The near misses that fail only the removed condition, with the test author's explanation of each. They show what
  the condition means in the author's words. Once it is removed, they fit the request too.

## Output
- `possible`: whether the condition can be removed under the rules.
- `request`: the edited request (empty if not possible).
- `removed_words`: the words you removed or changed, quoted from the original.
- `reason`: one or two sentences: what you changed, or why it is not possible.


---

Service: Linear.

Request:
> Set the estimate to 5 for the Todo issue assigned to Maya Chen with the Bug label that is blocked by the Checkout rollout issue.

Conditions of the request:
Records of `issues`, where:
  - at least one record of `users` linked by `assigneeId` eq `users.id`, where:
    - `name` = "Maya Chen"
  - at least one record of `workflow_states` linked by `stateId` eq `workflow_states.id`, where:
    - `name` = "Todo"
  - at least one record of `issue_labels` linked by `labelIds` json_contains `issue_labels.id`, where:
    - `name` = "Bug"
  - at least one record of `issue_relations` linked by `id` eq `issue_relations.relatedIssueId`, where:  << REMOVE
    - `type` = "blocks"
    - at least one record of `issues` linked by `issueId` eq `issues.id`, where:
      - `title` = "Checkout rollout"  << REMOVE

Near misses that fail only the removed condition (the author's explanations):
- `i-rev`: It meets every condition except direction: it blocks the Checkout rollout issue instead of being blocked by it.
- `i-sim`: It is blocked by the Checkout rollout follow-up issue, whose title contains the anchor title, not by the Checkout rollout issue itself.
- `i-sub`: It has no blocking relation of its own; only its parent issue is blocked by the Checkout rollout issue.

Remove the marked condition from the request, following the rules.