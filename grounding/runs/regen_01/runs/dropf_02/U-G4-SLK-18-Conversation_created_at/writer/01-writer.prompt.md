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

Service: Slack.

Request:
> Can you add an eyes reaction to the "deploy checklist is green" message? It was posted by one of our workspace admins in the small 5-person release channel we set up in March 2024 - I don't remember its exact name since there are a few similar ones.

Conditions of the request:
Records of `messages`, where:
  - `message_text` contains_ci "deploy checklist is green"
  - at least one record of `users` linked by `user_id` eq `users.user_id`, where:
    - at least one record of `user_teams` linked by `user_id` eq `user_teams.user_id`, where:
      - `role` = "admin"
  - at least one record of `channels` linked by `channel_id` eq `channels.channel_id`, where:
    - `created_at` >= "2024-03-01T00:00:00Z"  << REMOVE
    - `created_at` < "2024-04-01T00:00:00Z"  << REMOVE
    - a number = 5 of records of `channel_members` linked by `channel_id` eq `channel_members.channel_id`

Near misses that fail only the removed condition (the author's explanations):
- `1711111200.000009`: Same text, admin author and 5 members, but the channel was created on April 2, just outside March.
- `1711111500.000010`: Its message was posted in March, but the channel itself was created in January; reading the message date for the channel creation selects it.

Remove the marked condition from the request, following the rules.