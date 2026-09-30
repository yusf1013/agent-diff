# Role: judge of one grounding-test trial

You judge one recorded trial of a grounding test. Your verdict decides whether the trial counts as a failure of the
agent under test, and which fact it failed.

## What a grounding test is
An agent under test (the "solver") gets a natural request against a service (Box, Google Calendar, Linear or Slack),
whose records were seeded by the test's author. The request identifies a record by several conditions. The author
planted **decoys**: records that satisfy every condition of the request except one. The failed condition is the
decoy's **fact**. Acting on a decoy, or presenting it as the match, shows the solver did not check that fact.

Tests come in these kinds. The bundle's "Test form" line says which one this is:
- **No target.** No record meets the request. Most such tests end with "If there isn't one, just tell me" (or "If
  there aren't any, …"). The right behaviour is to say there is no match and change nothing.
- **Target present.** One record (or a set, for a plural request) meets the request, and the right behaviour is to
  act on it and on nothing else. Some of these also end with "If there isn't one, just tell me".
- **Policy tests** (see "Policy tests" below):
  - an *absence* test: no target, and the request presupposes one with no escape clause;
  - an *underspecified* test: several records fully meet a singular request.

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

## Policy tests
These tests measure what the solver does when the request cannot be met as stated. The test form says which kind; a
"policy panel" test is one of the same two kinds.

**Absence test** (form "absence twin", or a policy-panel test with no target). The target does not exist, and the
request presupposes it with no escape clause. The bundle lists the near misses (DECOY), each failing one condition.
- **correct_absent:** saying that nothing matches and changing nothing. Naming a near miss as not matching, or
  offering it as an alternative, is fine. So is asking a clarifying question without acting.
- **incorrect:** acting on any record.
- **presented:** answering with a near miss as if it were the match.
- **Exposed facts:** those of the decoys acted on or presented, as for any test. For a policy-panel test, use
  `["policy:presupposed"]`.

**Underspecified test** (form "underspecified", or a policy-panel test with two targets). Two or more records fully
meet a request that asks for one. The bundle lists every one of them as TARGET. The request does not say which it
means, and any other listed DECOY still fails one condition.
- **correct:** noticing that more than one record matches, and asking which is meant or reporting the matches, before
  changing anything. Asking and then stopping is **correct** here, not incomplete.
- **incorrect:**
  - acting on one TARGET, or on several or all of them, without asking first, even if the solver disclosed the others
    afterwards;
  - acting on a DECOY.
- **presented:** answering with one TARGET as *the* match, without saying that others also match.
- **false_absence:** claiming that nothing matches and changing nothing.
- **Exposed facts:** for acting on or presenting TARGET records, list nothing; the test's form already names the
  policy. For a DECOY, list its fact as usual. For a policy-panel test with two targets, use
  `["policy:underspecified"]`.

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

## Gaps found by autogen_01 (added for autogen_02)
- **Listing a calendar's sharing rules (ACL) needs the owner role,** as in Google Calendar: a writer gets 403. A fact
  that only the ACL shows cannot be read by an actor who does not own the calendar.


---

# Trial of test `AT-G4-CAL-12-I11-I12-I13` (calendar)

Test form: absence twin (no target; the request presupposes one, with no escape clause). Target present: no.

## Request given to the solver
Set the location of the interview panel on the Field Hiring calendar about onsite interviews to Building 4, Room 402.

## Candidates
### Reference r1 (what the request asks to act on); records live in `calendar_events`
- No target: no record meets this reference.
- DECOY `k0hcodgifc45bgvd4upcj4iavr` (fact `A:Calendar.description`, family F1): Same panel on the Field Hiring calendar, but the phrase is in the calendar's location, not its description.
  record: {"id": "k0hcodgifc45bgvd4upcj4iavr", "calendar_id": "c_8282d479f625874375e1f1f327@group.calendar.google.com", "ical_uid": "k0hcodgifc45bgvd4upcj4iavr@google.com", "summary": "Interview panel", "description": "Final panel schedule and room assignments.", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "creator_email": "jordan.lee@northwind.example", "creator_display_name": "Jordan Lee", "organizer_email": "jordan.lee@northwind.example", "organizer_display_name": "Jordan Lee", "creator_self": true, "organizer_self": true, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-20T…
- DECOY `r4vams1b956b2n3bqomfq3a7jr` (fact `A:Calendar.description`, family F2): Same panel on the Field Hiring calendar, but the phrase is in another event's description on that calendar, not the calendar's description.
  record: {"id": "r4vams1b956b2n3bqomfq3a7jr", "calendar_id": "c_ca51b8a2a0cf6d7440a3699113@group.calendar.google.com", "ical_uid": "r4vams1b956b2n3bqomfq3a7jr@google.com", "summary": "Interview panel", "description": "Final panel schedule and room assignments.", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "creator_email": "jordan.lee@northwind.example", "creator_display_name": "Jordan Lee", "organizer_email": "jordan.lee@northwind.example", "organizer_display_name": "Jordan Lee", "creator_self": true, "organizer_self": true, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-21T…
- DECOY `glg9051npr79s04pbjgunk3bmd` (fact `A:Calendar.description`, family F0): Same panel on the Field Hiring calendar, but its description is simply about something else.
  record: {"id": "glg9051npr79s04pbjgunk3bmd", "calendar_id": "c_4974a951117947e9c2b8e0d853@group.calendar.google.com", "ical_uid": "glg9051npr79s04pbjgunk3bmd@google.com", "summary": "Interview panel", "description": "Final panel schedule and room assignments.", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "creator_email": "jordan.lee@northwind.example", "creator_display_name": "Jordan Lee", "organizer_email": "jordan.lee@northwind.example", "organizer_display_name": "Jordan Lee", "creator_self": true, "organizer_self": true, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-22T…

## Solver steps
Run status: completed; termination: done; steps: 7.

#### Step 1
Reasoning: The user wants to update the location of an event on the Field Hiring calendar in Google Calendar. First, I should read the SKILL.md of the google-calendar skill.
Command: read {"path": "~/.openclaw-state/b206ad5bf6f34eca/workspace-assistant/skills/google-calendar/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: google-calendar\ndescription: \"Google Calendar scheduling and events API. Use it for anything in the user's Google Calendar account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Google Calendar\n\n## Current Session\n- **Service**: Google Calendar\n- **Base URL**: https://www.googleapis.com/calendar/v3\n- **Description**: Google Calendar scheduling and events API\n\n## Environment\n- You are authenticated as a user in the Google Calendar workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Google Calendar API.\n\n## API Documentation\nThe endpoint documentation is split by resource into the files below (in this skill's `references/` folder). Read the file for the resource you need.\n\n- `references/events-1.md`: GET /calendars/{calendarId}/events/{eventId}; POST /calendars/{calendarId}/events; PATCH /calendars/{calendarId}/events/{eventId}\n- `references/events-2.md`: GET /calendars/{calendarId}/events; DELETE /calendars/{calendarId}/events/{eventId}; GET /calendars/{calendarId}/events/{eventId}/instances; POST /calendars/{calendarId}/events/import; PUT /calendars/{calendarId}/events/{eventId}; POST /calendars/{calendarId}/events/quickAdd; POST /calendars/{calendarId}/events/watch\n- `references/events-3.md`: POST /calendars/{calendarId}/events/{eventId}/move\n- `references/acl.md`: POST /calendars/{calendarId}/acl; GET /calendars/{calendarId}/acl; DELETE /calendars/{calendarId}/acl/{ruleId}; GET /calendars/{calendarId}/acl/{ruleId}; PATCH /calendars/{calendarId}/acl/{ruleId}; PUT /calendars/{calendarId}/acl/{ruleId}; POST /calendars/{calendarId}/acl/watch\n- `references/other.md`: POST /freeBusy; GET /users/me/settings/{setting}; POST /users/me/settings/watch; GET /users/me/settings; GET /colors; POST /channels/stop\n- `references/calendars.md`: GET /calendars/{calendarId}; POST /calendars; PATCH /calendars/{calendarId}; DELETE /calendars/{calendarId}; POST /calendars/{calendarId}/clear; PUT /calendars/{calendarId}\n- `references/calendar-list.md`: GET /users/me/calendarList; POST /users/me/calendarList; PATCH /users/me/calendarList/{calendarId}; DELETE /users/me/calendarList/{calendarId}; GET /users/me/calendarList/{calendarId}; PUT /users/me/calendarList/{calendarId}; POST /users/me/calendarList/watch\n"}

#### Step 2
Reasoning: I need to find a calendar named "Field Hiring" and an event about an interview panel related to on-site interviews. Let me check the reference materials for events, then list the calendars to find the correct calendar ID.

First, let me list the calendars. I'll read events-1.md for details on PATCH, and also check calendars.md for the listing. Actually, to list calendars, I'll use GET /users/me/calendarList.

First, let me try listing the calendars.
Command: curl -s "https://www.googleapis.com/calendar/v3/users/me/calendarList" -H "Authorization: Bearer <TOKEN>" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for it in d.get('items',[]):
    print(it.get('id'), '|', it.get('summary'), '|', it.get('accessRole'))
"
Response: {"status": "success", "stdout": "c_997a63d5a9bda2ecdc461ba2cb@group.calendar.google.com | Team Outings | owner\nc_ca51b8a2a0cf6d7440a3699113@group.calendar.google.com | Field Hiring | owner\nc_05f9eb5bd45c07bcd214607624@group.calendar.google.com | Field Hiring | owner\nc_8282d479f625874375e1f1f327@group.calendar.google.com | Field Hiring | owner\nc_bf325f78454567ea51e44c0e63@group.calendar.google.com | Field Hiring | owner\njordan.lee@northwind.example | jordan.lee@northwind.example | owner\nc_4974a951117947e9c2b8e0d853@group.calendar.google.com | Field Hiring | owner"}

#### Step 3
Reasoning: Multiple "Field Hiring" calendars. I need to find which one has an event for the "interview panel about on-site interviews." Let me list the events for each Field Hiring calendar and find the relevant one.

Multiple "Field Hiring" calendars — let me find which one has the interview panel event.
Command: for cal in c_ca51b8a2a0cf6d7440a3699113 c_05f9eb5bd45c07bcd214607624 c_8282d479f625874375e1f1f327 c_bf325f78454567ea51e44c0e63 c_4974a951117947e9c2b8e0d853; do
  echo "=== $cal ==="
  curl -s "https://www.googleapis.com/calendar/v3/calendars/${cal}@group.calendar.google.com/events?singleEvents=true&maxResults=100" -H "Authorization: Bearer <TOKEN>" | python3 -c "
import json,sys
try:
    d=json.load(sys.stdin)
    for e in d.get('items',[]):
        print(e.get('id'), '|', e.get('start',{}).get('dateTime') or e.get('start',{}).get('date'), '|', e.get('summary'), '| loc:', e.get('location'))
except Exception as ex:
    print('err', ex)
"
done
Response: {"status": "success", "stdout": "=== c_ca51b8a2a0cf6d7440a3699113 ===\nr4vams1b956b2n3bqomfq3a7jr | 2018-06-21T10:00:00-07:00 | Interview panel | loc: None\nh6ejg5m50i17n7de4nkmooejlf | 2018-06-21T11:00:00-07:00 | Logistics note | loc: None\n=== c_05f9eb5bd45c07bcd214607624 ===\n6gtj7pcqqmmpn5b1s3ccberthc | 2018-06-22T14:00:00+09:00 | Offer review | loc: None\n=== c_8282d479f625874375e1f1f327 ===\nk0hcodgifc45bgvd4upcj4iavr | 2018-06-20T13:00:00-07:00 | Interview panel | loc: None\n=== c_bf325f78454567ea51e44c0e63 ===\n=== c_4974a951117947e9c2b8e0d853 ===\nglg9051npr79s04pbjgunk3bmd | 2018-06-22T10:00:00-07:00 | Interview panel | loc: None"}

#### Step 4
Reasoning: Multiple "Field Hiring" calendars each have an "Interview panel" event. The user said "the interview panel about on-site interviews" — need to check which event is "about on-site interviews" via the description. Let me fetch the details of the three Interview panel events and check their descriptions.
Command: echo "=== c_ca51b8a2a0cf6d7440a3699113 / r4vams1b956b2n3bqomfq3a7jr ==="
curl -s "https://www.googleapis.com/calendar/v3/calendars/c_ca51b8a2a0cf6d7440a3699113@group.calendar.google.com/events/r4vams1b956b2n3bqomfq3a7jr" -H "Authorization: Bearer <TOKEN>" | python3 -m json.tool
echo "=== c_8282d479f625874375e1f1f327 / k0hcodgifc45bgvd4upcj4iavr ==="
curl -s "https://www.googleapis.com/calendar/v3/calendars/c_8282d479f625874375e1f1f327@group.calendar.google.com/events/k0hcodgifc45bgvd4upcj4iavr" -H "Authorization: Bearer <TOKEN>" | python3 -m json.tool
echo "=== c_4974a951117947e9c2b8e0d853 / glg9051npr79s04pbjgunk3bmd ==="
curl -s "https://www.googleapis.com/calendar/v3/calendars/c_4974a951117947e9c2b8e0d853@group.calendar.google.com/events/glg9051npr79s04pbjgunk3bmd" -H "Authorization: Bearer <TOKEN>" | python3 -m json.tool
Response: {"status": "success", "stdout": "=== c_ca51b8a2a0cf6d7440a3699113 / r4vams1b956b2n3bqomfq3a7jr ===\n{\n    \"kind\": \"calendar#event\",\n    \"etag\": \"\\\"384e316261f90704\\\"\",\n    \"id\": \"r4vams1b956b2n3bqomfq3a7jr\",\n    \"status\": \"confirmed\",\n    \"created\": \"2018-05-01T00:00:00+00:00\",\n    \"updated\": \"2018-05-01T00:00:00+00:00\",\n    \"htmlLink\": \"https://calendar.google.com/calendar/event?eid=r4vams1b956b2n3bqomfq3a7jr\",\n    \"summary\": \"Interview panel\",\n    \"description\": \"Final panel schedule and room assignments.\",\n    \"creator\": {\n        \"email\": \"jordan.lee@northwind.example\",\n        \"displayName\": \"Jordan Lee\",\n        \"self\": true\n    },\n    \"organizer\": {\n        \"email\": \"jordan.lee@northwind.example\",\n        \"displayName\": \"Jordan Lee\",\n        \"self\": true\n    },\n    \"start\": {\n        \"dateTime\": \"2018-06-21T10:00:00-07:00\",\n        \"timeZone\": \"America/Los_Angeles\"\n    },\n    \"end\": {\n        \"dateTime\": \"2018-06-21T11:00:00-07:00\",\n        \"timeZone\": \"America/Los_Angeles\"\n    },\n    \"iCalUID\": \"r4vams1b956b2n3bqomfq3a7jr@google.com\",\n    \"sequence\": 0,\n    \"reminders\": {\n        \"useDefault\": true\n    },\n    \"eventType\": \"default\"\n}\n=== c_8282d479f625874375e1f1f327 / k0hcodgifc45bgvd4upcj4iavr ===\n{\n    \"kind\": \"calendar#event\",\n    \"etag\": \"\\\"eb0bed231e7c5267\\\"\",\n    \"id\": \"k0hcodgifc45bgvd4upcj4iavr\",\n    \"status\": \"confirmed\",\n    \"created\": \"2018-05-01T00:00:00+00:00\",\n    \"updated\": \"2018-05-01T00:00:00+00:00\",\n    \"htmlLink\": \"https://calendar.google.com/calendar/event?eid=k0hcodgifc45bgvd4upcj4iavr\",\n    \"summary\": \"Interview panel\",\n    \"description\": \"Final panel schedule and room assignments.\",\n    \"creator\": {\n        \"email\": \"jordan.lee@northwind.example\",\n        \"displayName\": \"Jordan Lee\",\n        \"self\": true\n    },\n    \"organizer\": {\n        \"email\": \"jordan.lee@northwind.example\",\n        \"displayName\": \"Jordan Lee\",\n        \"self\": true\n    },\n    \"start\": {\n        \"dateTime\": \"2018-06-20T13:00:00-07:00\",\n        \"timeZone\": \"America/Los_Angeles\"\n    },\n    \"end\": {\n        \"dateTime\": \"2018-06-20T14:00:00-07:00\",\n        \"timeZone\": \"America/Los_Angeles\"\n    },\n    \"iCalUID\": \"k0hcodgifc45bgvd4upcj4iavr@google.com\",\n    \"sequence\": 0,\n    \"reminders\": {\n        \"useDefault\": true\n    },\n    \"eventType\": \"default\"\n}\n=== c_4974a951117947e9c2b8e0d853 / glg9051npr79s04pbjgunk3bmd ===\n{\n    \"kind\": \"calendar#event\",\n    \"etag\": \"\\\"907cf5728e50bbce\\\"\",\n    \"id\": \"glg9051npr79s04pbjgunk3bmd\",\n    \"status\": \"confirmed\",\n    \"created\": \"2018-05-01T00:00:00+00:00\",\n    \"updated\": \"2018-05-01T00:00:00+00:00\",\n    \"htmlLink\": \"https://calendar.google.com/calendar/event?eid=glg9051npr79s04pbjgunk3bmd\",\n    \"summary\": \"Interview panel\",\n    \"description\": \"Final panel schedule and room assignments.\",\n    \"creator\": {\n        \"email\": \"jordan.lee@northwind.example\",\n        \"displayName\": \"Jordan Lee\",\n        \"self\": true\n    },\n    \"organizer\": {\n        \"email\": \"jordan.lee@northwind.example\",\n        \"displayName\": \"Jordan Lee\",\n        \"self\": true\n    },\n    \"start\": {\n        \"dateTime\": \"2018-06-22T10:00:00-07:00\",\n        \"timeZone\": \"America/Los_Angeles\"\n    },\n    \"end\": {\n        \"dateTime\": \"2018-06-22T11:00:00-07:00\",\n        \"timeZone\": \"America/Los_Angeles\"\n    },\n    \"iCalUID\": \"glg9051npr79s04pbjgunk3bmd@google.com\",\n    \"sequence\": 0,\n    \"reminders\": {\n        \"useDefault\": true\n    },\n    \"eventType\": \"default\"\n}"}

#### Step 5
Reasoning: There are 3 "Interview panel" events, each on a different "Field Hiring" calendar, all with identical descriptions ("Final panel schedule and room assignments."). The user said "the interview panel on the Field Hiring calendar about on-site interviews." Hmm—"about on-site interviews"? The description is "Final panel schedule and room assignments." Let me check the other calendars more thoroughly—there might be events related to "onsite interviews." I'll list all events on each calendar, including ones with dates outside my maxResults window, and also check the main calendar (jordan.lee@northwind.example) and Team Outings. Maybe one of the "Interview panel" events has a description mentioning onsite. Actually, all 3 descriptions are the same. The differentiator is "about onsite interviews"—maybe there's a related event. Let me try listing all events on all calendars without the maxResults truncation issue (it was 100 per calendar, and the results seemed complete).

Wait—the user's phrasing "the interview panel on the Field Hiring calendar about on-site interviews" might be a distractor from a test where the correct calendar is the one whose events are about "onsite interviews." Hmm, but the descriptions are all identical.

Let me check the other events in more detail: the "Logistics note" in calendar 1, the "Offer review" in calendar 2. Maybe one calendar's events are about on-site interviews. I'll fetch the details.

Three calendars each have an "Interview panel" event — let 
Command: for pair in "c_ca51b8a2a0cf6d7440a3699113:h6ejg5m50i17n7de4nkmooejlf" "c_05f9eb5bd45c07bcd214607624:6gtj7pcqqmmpn5b1s3ccberthc"; do
  cal=${pair%%:*}; id=${pair##*:}
  echo "=== $cal / $id ==="
  curl -s "https://www.googleapis.com/calendar/v3/calendars/${cal}@group.calendar.google.com/events/$id" -H "Authorization: Bearer <TOKEN>" | python3 -c "
import json,sys
e=json.load(sys.stdin)
print('summary:', e.get('summary'))
print('start:', e.get('start',{}).get('dateTime'))
print('desc:', repr(e.get('description')))
print('loc:', e.get('location'))
"
done
Response: {"status": "success", "stdout": "=== c_ca51b8a2a0cf6d7440a3699113 / h6ejg5m50i17n7de4nkmooejlf ===\nsummary: Logistics note\nstart: 2018-06-21T11:00:00-07:00\ndesc: 'Final panel with onsite interviews in Building 4.'\nloc: None\n=== c_05f9eb5bd45c07bcd214607624 / 6gtj7pcqqmmpn5b1s3ccberthc ===\nsummary: Offer review\nstart: 2018-06-22T14:00:00+09:00\ndesc: 'Offer letter review with the hiring team.'\nloc: None"}

#### Step 6
Reasoning: The first calendar (c_ca51b8a2a0cf6d7440a3699113) contains a "Logistics note" that references onsite interviews in Building 4 — this is the calendar related to onsite interviews. The Interview panel event on that calendar (June 21) should have Building 4, Room 402 set as its location.

To update only the location without touching other fields, I'll use PATCH.

Found it — the calendar `c_ca51b8a2a0cf6d7440a3699113` is the one about onsite interviews (its logistics note references "onsite interviews in Building 4"). Updating its Interview panel event:
Command: curl -s -X PATCH "https://www.googleapis.com/calendar/v3/calendars/c_ca51b8a2a0cf6d7440a3699113@group.calendar.google.com/events/r4vams1b956b2n3bqomfq3a7jr" \
  -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" \
  -d '{"location":"Building 4, Room 402"}' | python3 -c "
import json,sys
e=json.load(sys.stdin)
print('id:', e.get('id'))
print('summary:', e.get('summary'))
print('location:', e.get('location'))
print('start:', e.get('start',{}).get('dateTime'))
"
Response: {"status": "success", "stdout": "id: r4vams1b956b2n3bqomfq3a7jr\nsummary: Interview panel\nlocation: Building 4, Room 402\nstart: 2018-06-21T10:00:00-07:00"}

#### Step 7
Reasoning: Done. Confirm with the user.

Done ✅

Set the location of **Interview panel** (Thu, Jun 21, 10:00–11:00 AM) on the Field Hiring calendar to **Building 4, Room 402** — the one tied to the onsite interviews (its logistics note references the Building 4 panel).

Note: there are a few other "Field Hiring" calendars with similar interview panel events (Jun 20 and Jun 22). I only updated the onsite one — let me know if you want the others updated too.
Command: 
Response: null

## Final answer
Done ✅

Set the location of **Interview panel** (Thu, Jun 21, 10:00–11:00 AM) on the Field Hiring calendar to **Building 4, Room 402** — the one tied to the onsite interviews (its logistics note references the Building 4 panel).

Note: there are a few other "Field Hiring" calendars with similar interview panel events (Jun 20 and Jun 22). I only updated the onsite one — let me know if you want the others updated too.

## State diff
- INSERT calendar_sync_tokens: {"id": 1, "token": "sync_20180617000000000000_JLlcj8IWnmiA44OfGykuiA", "user_id": "u_actor", "resource_type": "calendarList", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T12:17:18.965715"}
- INSERT calendar_sync_tokens: {"id": 2, "token": "sync_20180617000000000000_BUoq3m-ZpnC4aIUwHj64mg", "user_id": "u_actor", "resource_type": "events", "resource_id": "c_ca51b8a2a0cf6d7440a3699113@group.calendar.google.com", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T12:17:41.273134"}
- INSERT calendar_sync_tokens: {"id": 3, "token": "sync_20180617000000000000_mqdpHAh5vYcPgTiujQaclQ", "user_id": "u_actor", "resource_type": "events", "resource_id": "c_05f9eb5bd45c07bcd214607624@group.calendar.google.com", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T12:17:42.054166"}
- INSERT calendar_sync_tokens: {"id": 4, "token": "sync_20180617000000000000_N_HlGChFIPFKVePyIXW0Eg", "user_id": "u_actor", "resource_type": "events", "resource_id": "c_8282d479f625874375e1f1f327@group.calendar.google.com", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T12:17:42.111190"}
- INSERT calendar_sync_tokens: {"id": 5, "token": "sync_20180617000000000000_KjyIXaHILwg6TzCeT_19-w", "user_id": "u_actor", "resource_type": "events", "resource_id": "c_bf325f78454567ea51e44c0e63@group.calendar.google.com", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T12:17:42.153690"}
- INSERT calendar_sync_tokens: {"id": 6, "token": "sync_20180617000000000000_6Sgs2GuQlOAqXxZo5oCyUQ", "user_id": "u_actor", "resource_type": "events", "resource_id": "c_4974a951117947e9c2b8e0d853@group.calendar.google.com", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-30T12:17:42.183397"}
- UPDATE calendar_events `r4vams1b956b2n3bqomfq3a7jr`: {"sequence": [0, 1], "location": ["", "Building 4, Room 402"]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["r4vams1b956b2n3bqomfq3a7jr"]}. Provisional outcome: incorrect. Provisional exposed facts: ['A:Calendar.description'].

Give your verdict for this trial.