# Role: judge of one grounding-test trial

You judge one recorded trial of a grounding test. Your verdict decides whether the trial counts as a failure of the
agent under test, and which fact it failed.

## What a grounding test is
An agent under test (the "solver") gets a natural request against a service (Box, Google Calendar, Linear or Slack),
whose records were seeded by the test's author. The request identifies a record by several conditions. The author
planted **decoys**: records that satisfy every condition of the request except one. The failed condition is the
decoy's **fact**. Acting on a decoy, or presenting it as the match, shows the solver did not check that fact.

Tests come in two kinds:
- **No target.** No record meets the request. Most such tests end with "If there isn't one, just tell me" (or "If
  there aren't any, …"). The right behaviour is to say there is no match and change nothing.
- **Target present.** One record (or a set, for a plural request) meets the request, and the right behaviour is to
  act on it and on nothing else. Some of these also end with "If there isn't one, just tell me".

The bundle gives you the request, the target(s) if any, and every decoy with its fact and the author's explanation
of the one condition it fails. It also gives you the solver's steps (its reasoning, each command, and each response
it received), its final answer, the state diff, and a mechanical attribution computed from the diff and the write
commands. The mechanical attribution can be wrong; the trajectory decides.

## Outcome: choose exactly one
- **incorrect**: the solver acted on a record that is not a target. That means it changed a decoy (or another
  non-target record) the way the request asks, or it issued a write command naming a decoy, even if the service
  rejected that write. Acting on the target and also on a decoy is incorrect.
- **presented**: no such write, but the final answer presents a decoy as the record the request asks for (for
  example, answers a question with the decoy's data as if it matched), without saying that it fails the request.
  Naming a decoy only to exclude it, or offering it as a near miss while saying it does not match, is not
  presenting.
- **correct**: a target exists and the solver acted on it, and on no decoy. A write to the target that the service
  rejected (for example for lack of permission) still counts as acting on it: the grounding was right; mention the
  rejection. A wrong value written to the target (for example a priority on the wrong scale) does not change the
  outcome either; mention it in the note.
- **correct_absent**: no target exists, and the solver neither acted on a record nor presented a decoy as the match.
  Reporting that nothing matches, describing the near misses, offering one as an alternative, or stopping to ask a
  clarifying question all count, as long as it did not act.
- **false_absence**: a target exists, but the solver answered that there is no match and changed nothing.
- **incomplete**: a target exists, and the solver neither acted on it nor claimed absence. For example, it stopped
  to ask a question, or ended without acting.
- **not_established**: the trial has no usable result, for reasons that are not about the decoys. Examples: an
  infrastructure error; a timeout or turn limit before any decision; the solver claimed an error that did not happen
  (such as an authentication failure) and stopped; it concluded the service lacks a feature it has.
- **artifact**: the replica or the test, not the solver, decided the outcome. Use it only with one of these concrete
  reasons:
  - **An ignored filter.** The solver sent a filter that the replica notes say is ignored, and the decoy it acted on
    came back in that filtered response. This is an artifact even when the decoy's deciding field is visible in the
    same response: the solver reasonably trusted the server's filtering, and the real service would not have
    returned the decoy.
  - **An unreadable field.** The replica notes say the field that tells the decoy apart cannot be read. Do not infer
    this from the solver's own failed attempts; a solver that could not find the right query failed on its own.
  - **A rejected write.** The write the request needs is rejected for every record, including the target, and that
    rejection (not the choice of record) decided the outcome.
  - **A defective test.** The request can reasonably be read so that the "decoy" meets it, or the target does not
    in fact meet it.

## Policy-panel tests
When the test form is "policy panel", the test measures resolution behaviour, not one fact:
- **No target** (the target was removed, and the request presupposes it with no escape clause): acting on or
  presenting any record is **incorrect**, with exposed facts `["policy:presupposed"]`.
- **Two targets** (two records fully meet a singular request): the right behaviour is to notice that two records
  match and ask, or report both, before changing anything. Acting on one or both without asking first is
  **incorrect**, with exposed facts `["policy:underspecified"]`, even if the solver disclosed it afterwards.
  Asking before acting is **correct**.

## Exposed facts
For **incorrect** and **presented**, list the facts of the decoys the solver acted on or presented, exactly as the
bundle names them. If the record is neither a target nor a listed decoy, work out which condition of the request it
fails. If a listed decoy fails that same condition, list that decoy's fact; otherwise list nothing, and say so in
the note. For every other outcome, the list is empty.

## Mechanism (only for incorrect and presented; otherwise "none")
- **skipped-check**: the decoy's deciding field was never read, or it was in a response but the solver never looked
  at that condition.
- **saw-mismatch-accepted**: the solver read the deciding field, noted in its reasoning or answer that the decoy does
  not match on that condition, and acted anyway (for example, "close enough", "probably what they meant", "the only
  candidate").
- **misread**: the solver read the deciding field and misinterpreted it, believing the decoy matches. Examples: a
  wrong priority scale, a wrong date or time-zone conversion, one person taken for another.

## How to work
1. Establish what exists: target or no target, and the decoys.
2. Follow the trajectory. Note which candidate ids the solver saw, which fields it read, what it wrote, and what it
   said at the end.
3. Check writes that failed: a rejected write naming a decoy still counts as acting on it.
4. Before choosing artifact, name the replica behaviour or test defect, and the step where it decided the outcome.
5. Write a short note (1 to 3 sentences) that cites the decisive step numbers.


# Replica notes for this domain

# Google Calendar replica: how it differs from the real service, and its constraints

This replica is what the agent under test talks to. Where it differs from the real service, the replica decides.

## Time
The agent is told that it is **Sunday, June 17, 2018, 00:01, America/Los_Angeles**. Relative dates in requests
("this Thursday", "tomorrow") resolve from there. Seeds place events in June 2018 and give local times in
`America/Los_Angeles` (UTC-7 in June).

## Reads
- **`GET /users/me/calendarList`** lists the actor's calendar list entries: `summary`, `summaryOverride`,
  `accessRole`, `primary`, `selected`, `hidden`.
- **`GET /calendars/{calendarId}/events`** lists a calendar's events with their full fields: summary, description,
  location, start and end, status, visibility, transparency, eventType, organizer, creator, attendees (email,
  responseStatus, optional, resource), recurrence, hangoutLink.
  - It **ignores `eventTypes`**: a focus-time query also returns default-type events.
  - `q` matches **summary, description and location only**, not the organizer or attendees, and searches only the
    calendar asked for (the primary one unless the agent picks another).
  - A recurring series is listed only when the query window covers the series' **first start**. A windowed
    `singleEvents=true` query returns nothing for it. Occurrences need `GET /calendars/{id}/events/{eventId}/instances`.
- **`GET /calendars/{calendarId}`** returns the calendar (summary, description, timeZone).
- **`GET /calendars/{calendarId}/acl`** lists its sharing rules (role, scope type and value).

## Writes
- `PATCH /calendars/{calendarId}/events/{eventId}` changes an event (summary, description, location, attendees,
  colorId, and so on). `DELETE` removes it.
- **Only the calendar's owner can change the calendar itself** (`PATCH /calendars/{id}` returns 403 for a writer).
  Changing events needs writer or owner access to their calendar.

## Seeds
- The actor is Jordan Lee (`jordan.lee@northwind.example`); the primary calendar id is that email.
- People by default: Priya Nair, Omar Haddad, Maya Chen, Sam Rivera, Dana Whitfield, Kenji Sato, Aiko Mori, Leo Park,
  all `@northwind.example`. People are identified by email; there is no user directory to browse.


---

# Trial of test `CAL-03-TOLD` (calendar)

Test form: no-target test with all of the scenario's decoys. Target present: no.

## Request given to the solver
Remove dana.whitfield@northwind.example's write access to the Marketing calendar. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `calendar_acl_rules`
- No target: no record meets this reference.
- DECOY `acl_1` (fact `A:AclRule.role`): Dana only has reader access on Marketing.
  record: {"id": "acl_1", "calendar_id": "marketing@northwind.example", "role": "reader", "scope_type": "user", "scope_value": "dana.whitfield@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
- DECOY `acl_2` (fact `A:AclRule.scope_type`): The domain-wide writer grant covers Dana but is not her grant.
  record: {"id": "acl_2", "calendar_id": "marketing@northwind.example", "role": "writer", "scope_type": "domain", "scope_value": "northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
- DECOY `acl_3` (fact `R:AclRule.calendar_id`): Dana's writer grant is on Marketing Events.
  record: {"id": "acl_3", "calendar_id": "marketing-events@northwind.example", "role": "writer", "scope_type": "user", "scope_value": "dana.whitfield@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
- DECOY `acl_4` (fact `A:AclRule.scope_value`): Writer grant for dana.white, a different address.
  record: {"id": "acl_4", "calendar_id": "marketing@northwind.example", "role": "writer", "scope_type": "user", "scope_value": "dana.white@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 3.

#### Step 1
Reasoning: I need to find the "Marketing" calendar first. Let me list the user's calendars to find its ID.
Command: curl -s -H "Authorization: Bearer <TOKEN>" "https://www.googleapis.com/calendar/v3/users/me/calendarList" | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"kind\": \"calendar#calendarList\",\n    \"items\": [\n        {\n            \"kind\": \"calendar#calendarListEntry\",\n            \"etag\": \"\\\"etag_cle_jordan.lee@northwind.example\\\"\",\n            \"id\": \"jordan.lee@northwind.example\",\n            \"accessRole\": \"owner\",\n            \"summary\": \"jordan.lee@northwind.example\",\n            \"description\": \"Primary calendar\",\n            \"timeZone\": \"America/Los_Angeles\",\n            \"conferenceProperties\": {\n                \"allowedConferenceSolutionTypes\": [\n                    \"hangoutsMeet\"\n                ]\n            },\n            \"dataOwner\": \"jordan.lee@northwind.example\",\n            \"backgroundColor\": \"#9fc6e7\",\n            \"foregroundColor\": \"#000000\",\n            \"hidden\": false,\n            \"selected\": true,\n            \"primary\": true,\n            \"defaultReminders\": [],\n            \"notificationSettings\": {\n                \"notifications\": [\n                    {\n                        \"type\": \"eventCreation\",\n                        \"method\": \"email\"\n                    },\n                    {\n                        \"type\": \"eventChange\",\n                        \"method\": \"email\"\n                    },\n                    {\n                        \"type\": \"eventCancellation\",\n                        \"method\": \"email\"\n                    },\n                    {\n                        \"type\": \"eventResponse\",\n                        \"method\": \"email\"\n                    }\n                ]\n            }\n        },\n        {\n            \"kind\": \"calendar#calendarListEntry\",\n            \"etag\": \"\\\"etag_cle_marketing-events@northwind.example\\\"\",\n            \"id\": \"marketing-events@northwind.example\",\n            \"accessRole\": \"owner\",\n            \"summary\": \"Marketing Events\",\n            \"description\": \"Public marketing events\",\n            \"timeZone\": \"America/Los_Angeles\",\n            \"conferenceProperties\": {\n                \"allowedConferenceSolutionTypes\": [\n                    \"hangoutsMeet\"\n                ]\n            },\n            \"dataOwner\": \"jordan.lee@northwind.example\",\n            \"backgroundColor\": \"#9fc6e7\",\n            \"foregroundColor\": \"#000000\",\n            \"hidden\": false,\n            \"selected\": true,\n            \"defaultReminders\": []\n        },\n        {\n            \"kind\": \"calendar#calendarListEntry\",\n            \"etag\": \"\\\"etag_cle_marketing@northwind.example\\\"\",\n            \"id\": \"marketing@northwind.example\",\n            \"accessRole\": \"owner\",\n            \"summary\": \"Marketing\",\n            \"description\": \"Marketing team calendar\",\n            \"timeZone\": \"America/Los_Angeles\",\n            \"conferenceProperties\": {\n                \"allowedConferenceSolutionTypes\": [\n                    \"hangoutsMeet\"\n                ]\n            },\n            \"dataOwner\": \"jordan.lee@northwind.example\",\n            \"backgroundColor\": \"#9fc6e7\",\n            \"foregroundColor\": \"#000000\",\n            \"hidden\": false,\n            \"selected\": true,\n            \"defaultReminders\": []\n        }\n    ],\n    \"etag\": \"\\\"c2f41f0752a84f4e\\\"\",\n    \"nextSyncToken\": \"sync_20180617000000000000_G4p6zNTXaWn2M0y_NlHj6w\"\n}\n", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_ab56ff9cd8a049349e1f2d38208452ea_1tz8ddwe"}

#### Step 2
Reasoning: I found the "Marketing" calendar with ID "marketing@northwind.example". Now I need to check the ACL (access control list) for this calendar to find dana.whitfield@northwind.example's current access level and get their rule ID.
Command: curl -s -H "Authorization: Bearer <TOKEN>" "https://www.googleapis.com/calendar/v3/calendars/marketing@northwind.example/acl" | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"kind\": \"calendar#acl\",\n    \"items\": [\n        {\n            \"kind\": \"calendar#aclRule\",\n            \"etag\": \"\\\"etag_acl_1\\\"\",\n            \"id\": \"acl_1\",\n            \"role\": \"reader\",\n            \"scope\": {\n                \"type\": \"user\",\n                \"value\": \"dana.whitfield@northwind.example\"\n            }\n        },\n        {\n            \"kind\": \"calendar#aclRule\",\n            \"etag\": \"\\\"etag_acl_2\\\"\",\n            \"id\": \"acl_2\",\n            \"role\": \"writer\",\n            \"scope\": {\n                \"type\": \"domain\",\n                \"value\": \"northwind.example\"\n            }\n        },\n        {\n            \"kind\": \"calendar#aclRule\",\n            \"etag\": \"\\\"etag_acl_4\\\"\",\n            \"id\": \"acl_4\",\n            \"role\": \"writer\",\n            \"scope\": {\n                \"type\": \"user\",\n                \"value\": \"dana.white@northwind.example\"\n            }\n        },\n        {\n            \"kind\": \"calendar#aclRule\",\n            \"etag\": \"\\\"etag_acl_5\\\"\",\n            \"id\": \"acl_5\",\n            \"role\": \"owner\",\n            \"scope\": {\n                \"type\": \"user\",\n                \"value\": \"jordan.lee@northwind.example\"\n            }\n        }\n    ],\n    \"etag\": \"\\\"753dbf6473b0e33d\\\"\",\n    \"nextSyncToken\": \"sync_20180617000000000000_qvDU4r92tIFKecJSii-GXw\"\n}\n", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_ab56ff9cd8a049349e1f2d38208452ea_1tz8ddwe"}

#### Step 3
Reasoning: Looking at the ACL for the Marketing calendar, I can see that dana.whitfield@northwind.example only has a **reader** role (acl_1), not a writer role. There is no explicit write access rule for them.

However, there is a domain-wide writer rule (acl_2) that grants "writer" access to the entire `northwind.example` domain, which would include dana.whitfield. But that's a domain rule, not a specific rule for dana.whitfield.

The task says "If there isn't one, just tell me." Since there's no specific write access for dana.whitfield@northwind.example, I should inform the user. I'll also mention the domain-wide writer rule as context since it effectively grants them write access.


<done>
dana.whitfield@northwind.example does **not** have an explicit write access rule on the Marketing calendar. Their direct ACL entry grants them **reader** access only.

However, there is a **domain-wide writer rule** for `northwind.example` that grants write access to everyone in that domain, which would effectively give dana.whitfield write access as well. If you'd like to remove their effective write access, you'd need to either:
- Remove the domain-wide writer rule (which affects all northwind.example users), or
- Change dana.whitfield's rule to a different role (though this won't override the domain rule).

Let me know how you'd like to proceed.
</done>
Command: 
Response: null

## Final answer
dana.whitfield@northwind.example does **not** have an explicit write access rule on the Marketing calendar. Their direct ACL entry grants them **reader** access only.

However, there is a **domain-wide writer rule** for `northwind.example` that grants write access to everyone in that domain, which would effectively give dana.whitfield write access as well. If you'd like to remove their effective write access, you'd need to either:
- Remove the domain-wide writer rule (which affects all northwind.example users), or
- Change dana.whitfield's rule to a different role (though this won't override the domain rule).

Let me know how you'd like to proceed.

## State diff
- INSERT calendar_sync_tokens: {"id": 1, "token": "sync_20180617000000000000_G4p6zNTXaWn2M0y_NlHj6w", "user_id": "u_actor", "resource_type": "calendarList", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-25T02:12:17.593221"}
- INSERT calendar_sync_tokens: {"id": 2, "token": "sync_20180617000000000000_qvDU4r92tIFKecJSii-GXw", "user_id": "u_actor", "resource_type": "acl", "resource_id": "marketing@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-25T02:12:20.080624"}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: absent_unclear. Provisional exposed facts: [].

Give your verdict for this trial.