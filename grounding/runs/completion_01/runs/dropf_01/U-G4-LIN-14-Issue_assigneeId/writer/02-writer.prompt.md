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
> Set the 'Checkout outage' issue in the Platform team on the Atlas project assigned to Priya Nair to Urgent priority.

Conditions of the request:
Records of `issues`, where:
  - `title` contains_ci "checkout outage"
  - at least one record of `teams` linked by `teamId` eq `teams.id`, where:
    - `name` = "Platform"
  - at least one record of `projects` linked by `projectId` eq `projects.id`, where:
    - `name` = "Atlas"
  - at least one record of `users` linked by `assigneeId` eq `users.id`, where:  << REMOVE
    - `name` = "Priya Nair"

Near misses that fail only the removed condition (the author's explanations):
- `i-d3`: Same title, team and project, but it is assigned to Leo Park; Priya Nair's same-titled issue belongs to another team and project.
- `i-d5`: Same title, team and project, but Priya Nair created it; Leo Park is the assignee.

Remove the marked condition from the request, following the rules.