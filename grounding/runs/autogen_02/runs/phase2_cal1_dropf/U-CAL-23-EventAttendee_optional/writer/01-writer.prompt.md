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
3. **The request still asks for one record** ("the folder", "the event"). Do not use *all, every, each, any, both*,
   and do not make the record plural.
4. **Keep it natural.** It must read like something a real user would write. Repair grammar only as needed, for
   example by joining the remaining clauses.
5. **Add nothing:** no new condition, no hint that several records fit, no "if there is more than one", no escape
   clause, no instruction to ask.
6. **If the condition cannot be removed** without changing another condition, or the result could not read naturally,
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

Service: Google Calendar.

Request:
> Delete Friday's architecture review that Kenji Sato (kenji.sato@northwind.example) attends as an optional guest.

Conditions of the request:
Records of `calendar_events`, where:
  - `summary` contains_ci "architecture review"
  - `start_datetime` >= "2018-06-22T00:00:00"
  - `start_datetime` < "2018-06-23T00:00:00"
  - at least one record of `calendar_event_attendees` linked by `id` eq `calendar_event_attendees.event_id`, where:
    - `email` = "kenji.sato@northwind.example"
    - `optional` = true  << REMOVE

Near misses that fail only the removed condition (the author's explanations):
- `ev_ar_required`: Kenji is a required attendee.

Remove the marked condition from the request, following the rules.