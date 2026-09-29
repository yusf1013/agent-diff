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

# Trial of test `P-G4-CAL-10-I12` (calendar)

Test form: probe. Target present: no.

## Request given to the solver
Add 'Bring the printed roadmap' to the description of the confirmed sprint review with a video link that has Maple Room booked on Thursday. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `calendar_events`
- No target: no record meets this reference.
- DECOY `6k6rhikvtl34h5a336r7c0ak4g` (fact `A:Event.hangout_link`, family F0): It meets every condition except that it has no video link attached.
  record: {"id": "6k6rhikvtl34h5a336r7c0ak4g", "calendar_id": "jordan.lee@northwind.example", "ical_uid": "6k6rhikvtl34h5a336r7c0ak4g@google.com", "summary": "Sprint review", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "creator_email": "jordan.lee@northwind.example", "creator_display_name": "Jordan Lee", "organizer_email": "jordan.lee@northwind.example", "organizer_display_name": "Jordan Lee", "creator_self": true, "organizer_self": true, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-21T09:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-21T09:3…

## Solver steps
Run status: completed; termination: done; steps: 9.

#### Step 1
Reasoning: The user wants me to work with Google Calendar. First, I need to read the google-calendar skill to understand how to use it.

Let me start by reading SKILL.md.
Command: read {"path": "~/.openclaw-state/a963963cb9e64215/workspace-assistant/skills/google-calendar/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: google-calendar\ndescription: \"Google Calendar scheduling and events API. Use it for anything in the user's Google Calendar account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Google Calendar\n\n## Current Session\n- **Service**: Google Calendar\n- **Base URL**: https://www.googleapis.com/calendar/v3\n- **Description**: Google Calendar scheduling and events API\n\n## Environment\n- You are authenticated as a user in the Google Calendar workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Google Calendar API.\n\n## API Documentation\nThe endpoint documentation is split by resource into the files below (in this skill's `references/` folder). Read the file for the resource you need.\n\n- `references/events-1.md`: GET /calendars/{calendarId}/events/{eventId}; POST /calendars/{calendarId}/events; PATCH /calendars/{calendarId}/events/{eventId}\n- `references/events-2.md`: GET /calendars/{calendarId}/events; DELETE /calendars/{calendarId}/events/{eventId}; GET /calendars/{calendarId}/events/{eventId}/instances; POST /calendars/{calendarId}/events/import; PUT /calendars/{calendarId}/events/{eventId}; POST /calendars/{calendarId}/events/quickAdd; POST /calendars/{calendarId}/events/watch\n- `references/events-3.md`: POST /calendars/{calendarId}/events/{eventId}/move\n- `references/acl.md`: POST /calendars/{calendarId}/acl; GET /calendars/{calendarId}/acl; DELETE /calendars/{calendarId}/acl/{ruleId}; GET /calendars/{calendarId}/acl/{ruleId}; PATCH /calendars/{calendarId}/acl/{ruleId}; PUT /calendars/{calendarId}/acl/{ruleId}; POST /calendars/{calendarId}/acl/watch\n- `references/other.md`: POST /freeBusy; GET /users/me/settings/{setting}; POST /users/me/settings/watch; GET /users/me/settings; GET /colors; POST /channels/stop\n- `references/calendars.md`: GET /calendars/{calendarId}; POST /calendars; PATCH /calendars/{calendarId}; DELETE /calendars/{calendarId}; POST /calendars/{calendarId}/clear; PUT /calendars/{calendarId}\n- `references/calendar-list.md`: GET /users/me/calendarList; POST /users/me/calendarList; PATCH /users/me/calendarList/{calendarId}; DELETE /users/me/calendarList/{calendarId}; GET /users/me/calendarList/{calendarId}; PUT /users/me/calendarList/{calendarId}; POST /users/me/calendarList/watch\n"}

#### Step 2
Reasoning: The user's request is:
1. Find a confirmed sprint review with a video link that has the Maple Room reserved on Thursday
2. Add "Bring the printed roadmap" to that event's description
3. If no such event exists, just let them know

Let me first read the event reference file to understand the API.
Command: read {"path": "~/.openclaw-state/a963963cb9e64215/workspace-assistant/skills/google-calendar/references/events-2.md"}
Response: {"status": "success", "stdout": "# Google Calendar API: events-2\n\n## GET /calendars/{calendarId}/events\nReturns events on the specified calendar.\n\n**Parameters:**\n  path:\n    - `calendarId` (string, **required**): Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the 'primary' keyword.\n  query:\n    - `alwaysIncludeEmail` (boolean, optional): Deprecated and ignored.\n    - `eventTypes` (string, optional): Event types to return. Can be repeated multiple times. Acceptable values: 'birthday', 'default', 'focusTime', 'fromGmail', 'outOfOffice', 'workingLocation'. If unset, returns all event types.\n    - `iCalUID` (string, optional): Specifies an event ID in the iCalendar format to be provided in the response. Use this to search for an event by its iCalendar ID.\n    - `maxAttendees` (integer, optional): The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned.\n    - `maxResults` (integer, optional): Maximum number of events returned on one result page. By default the value is 250 events. The page size can never be larger than 2500 events.\n    - `orderBy` (string, optional): The order of the events returned in the result. Acceptable values: 'startTime' (only available when singleEvents is True), 'updated'. The default is an unspecified, stable order.\n    - `pageToken` (string, optional): Token specifying which result page to return.\n    - `privateExtendedProperty` (string, optional): Extended properties constraint specified as propertyName=value. Matches only private properties. Can be repeated multiple times.\n    - `q` (string, optional): Free text search terms to find events that match these terms in fields like summary, description, location, attendee's displayName/email, organizer's displayName/email, and working location properties.\n    - `sharedExtendedProperty` (string, optional): Extended properties constraint specified as propertyName=value. Matches only shared properties. Can be repeated multiple times.\n    - `showDeleted` (boolean, optional): Whether to include deleted events (with status equals 'cancelled') in the result. The default is False.\n    - `showHiddenInvitations` (boolean, optional): Whether to include hidden invitations in the result. The default is False.\n    - `singleEvents` (boolean, optional): Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. The default is False.\n    - `syncToken` (string, optional): Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. Makes the result contain only entries that have changed since then. Cannot be used with iCalUID, orderBy, privateExtendedProperty, q, sharedExtendedProperty, timeMin, timeMa […8533 chars omitted…] entifier (UUID recommended). Max 64 characters.\n    - `type` (string, **required**): Must be 'web_hook'.\n    - `address` (string, **required**): HTTPS URL to receive notifications. Must be registered in Google Cloud Console.\n    - `token` (string, optional): Arbitrary string sent with notifications for verification. Max 256 characters.\n    - `expiration` (long, optional): Unix timestamp (ms) when channel expires. Default ~1 week.\n    - `params` (object, optional): Additional parameters.\n"}

#### Step 3
Reasoning: Alright, let me search for the sprint review event. First, I need to identify the "confirmed sprint review" — a sprint review with a video link (like a Meet link, probably) where the Maple Room has been reserved on Thursday. Let me search for events matching "sprint review" within the relevant time window. Today is Sunday, June 17, 2018 (PDT), so Thursday would be June 21, 2018. Let me search for events with the q=sprint review query over the next few days.

Actually, the condition is "the confirmed sprint review with a video link where the Maple Room has been reserved on Thursday." In other words, among the sprint review events (probably this week, i.e., Thursday = June 21), I need to find one that satisfies the following conditions:
1. Confirmed (status is confirmed)
2. Has a video link (in the description, a Meet link, or conference data)
3. Maple Room has been reserved (the location might mention Maple Room, or it might be in the description)

After that, I'll add "Bring the printed roadmap" to that description.

Let me run the search.
Command: curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?q=sprint%20review&timeMin=2018-06-17T00:00:00-07:00&timeMax=2018-06-25T00:00:00-07:00&singleEvents=true" | head -c 6000
Response: {"status": "success", "stdout": "{\"kind\":\"calendar#events\",\"items\":[{\"kind\":\"calendar#event\",\"etag\":\"\\\"bd2479833fd39442\\\"\",\"id\":\"6k6rhikvtl34h5a336r7c0ak4g\",\"status\":\"confirmed\",\"created\":\"2018-05-01T00:00:00+00:00\",\"updated\":\"2018-05-01T00:00:00+00:00\",\"htmlLink\":\"https://calendar.google.com/calendar/event?eid=6k6rhikvtl34h5a336r7c0ak4g\",\"summary\":\"Sprint review\",\"creator\":{\"email\":\"jordan.lee@northwind.example\",\"displayName\":\"Jordan Lee\",\"self\":true},\"organizer\":{\"email\":\"jordan.lee@northwind.example\",\"displayName\":\"Jordan Lee\",\"self\":true},\"start\":{\"dateTime\":\"2018-06-21T09:00:00-07:00\",\"timeZone\":\"America/Los_Angeles\"},\"end\":{\"dateTime\":\"2018-06-21T09:30:00-07:00\",\"timeZone\":\"America/Los_Angeles\"},\"iCalUID\":\"6k6rhikvtl34h5a336r7c0ak4g@google.com\",\"sequence\":0,\"reminders\":{\"useDefault\":true},\"eventType\":\"default\",\"attendees\":[{\"email\":\"priya.nair@northwind.example\",\"responseStatus\":\"accepted\",\"displayName\":\"Priya Nair\"},{\"email\":\"maple-room@northwind.example\",\"responseStatus\":\"accepted\",\"displayName\":\"Maple Room\",\"resource\":true}]}],\"etag\":\"\\\"e2a719a811ecf2ce\\\"\",\"summary\":\"jordan.lee@northwind.example\",\"description\":\"Primary calendar\",\"timeZone\":\"America/Los_Angeles\",\"accessRole\":\"owner\",\"updated\":\"2018-05-01T00:00:00+00:00\",\"nextSyncToken\":\"sync_20180617000000000000_swFcU3TwmKevVogIJoP7vw\"}"}

#### Step 4
Reasoning: I found an event. The "Sprint Review" on Thursday, June 21, 2018 has status "confirmed" and includes the "Maple Room" as a resource attendee. This is a confirmed sprint review with the Maple Room reserved on Thursday.

Next, I need to find the video link. This event has a "maple-room@northwind.example" attendee... wait, "with the video link where the Maple Room is reserved"—hmm. Let me re-read the request: "Add 'Bring the printed roadmap' to the description of the confirmed sprint review where the Maple Room is reserved on Thursday, along with the video link."

So, there should be a video link somewhere. The event itself has no description or hangoutLink in what was shown. The "maple-room@northwind.example" attendee is the resource (Maple Room). The video link might be in a separate event—for example, there might be an event like a recording link or a "video link" event. Or maybe the video link is in the event's description. The event above has neither a description nor a hangoutLink.

Wait—there might be other sprint review events. For example, ones with video links. Or a related event like "Sprint review recording," or an event with a video link in the description. Let me search more broadly for video link events. I'll search the calendar with q="video" and also check events with "hangoutLink". Also, I'll list the events for Thursday, June 21, and see what's there.

Found a confirmed Sprint review on Thu June 21 with Maple Room booked. Now I'll locate the video link.
Command: curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?q=video&timeMin=2018-06-10T00:00:00-07:00&timeMax=2018-06-25T00:00:00-07:00&singleEvents=true" | python3 -m json.tool 2>/dev/null | head -c 8000; echo "-----"; curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?timeMin=2018-06-21T00:00:00-07:00&timeMax=2018-06-22T00:00:00-07:00&singleEvents=true" | python3 -m json.tool 2>/dev/null | head -c 8000
Response: {"status": "success", "stdout": "{\n    \"kind\": \"calendar#events\",\n    \"items\": [],\n    \"etag\": \"\\\"fb3d8d0f3558054a\\\"\",\n    \"summary\": \"jordan.lee@northwind.example\",\n    \"description\": \"Primary calendar\",\n    \"timeZone\": \"America/Los_Angeles\",\n    \"accessRole\": \"owner\",\n    \"updated\": \"2018-06-17T00:00:00-07:00\",\n    \"nextSyncToken\": \"sync_20180617000000000000_ZawIZoxqhHc4S_Ypdrk-WA\"\n}\n-----\n{\n    \"kind\": \"calendar#events\",\n    \"items\": [\n        {\n            \"kind\": \"calendar#event\",\n            \"etag\": \"\\\"bd2479833fd39442\\\"\",\n            \"id\": \"6k6rhikvtl34h5a336r7c0ak4g\",\n            \"status\": \"confirmed\",\n            \"created\": \"2018-05-01T00:00:00+00:00\",\n            \"updated\": \"2018-05-01T00:00:00+00:00\",\n            \"htmlLink\": \"https://calendar.google.com/calendar/event?eid=6k6rhikvtl34h5a336r7c0ak4g\",\n            \"summary\": \"Sprint review\",\n            \"creator\": {\n                \"email\": \"jordan.lee@northwind.example\",\n                \"displayName\": \"Jordan Lee\",\n                \"self\": true\n            },\n            \"organizer\": {\n                \"email\": \"jordan.lee@northwind.example\",\n                \"displayName\": \"Jordan Lee\",\n                \"self\": true\n            },\n            \"start\": {\n                \"dateTime\": \"2018-06-21T09:00:00-07:00\",\n                \"timeZone\": \"America/Los_Angeles\"\n            },\n            \"end\": {\n                \"dateTime\": \"2018-06-21T09:30:00-07:00\",\n                \"timeZone\": \"America/Los_Angeles\"\n            },\n            \"iCalUID\": \"6k6rhikvtl34h5a336r7c0ak4g@google.com\",\n            \"sequence\": 0,\n            \"reminders\": {\n                \"useDefault\": true\n            },\n            \"eventType\": \"default\",\n            \"attendees\": [\n                {\n                    \"email\": \"priya.nair@northwind.example\",\n                    \"responseStatus\": \"accepted\",\n                    \"displayName\": \"Priya Nair\"\n                },\n                {\n                    \"email\": \"maple-room@northwind.example\",\n                    \"responseStatus\": \"accepted\",\n                    \"displayName\": \"Maple Room\",\n                    \"resource\": true\n                }\n            ]\n        }\n    ],\n    \"etag\": \"\\\"ba63b93a91ad1b06\\\"\",\n    \"summary\": \"jordan.lee@northwind.example\",\n    \"description\": \"Primary calendar\",\n    \"timeZone\": \"America/Los_Angeles\",\n    \"accessRole\": \"owner\",\n    \"updated\": \"2018-05-01T00:00:00+00:00\",\n    \"nextSyncToken\": \"sync_20180617000000000000_DgfScRyMeivnqzKzGwYePQ\"\n}"}

#### Step 5
Reasoning: The q=video search didn't return anything within that period. I'll try searching for video links more broadly — maybe I should search for "call", "link", "meet", "hangouts", "video" with a wider time range, or check all of June. Let me try searching with different terms.

The `q=video` search came up empty. Let me widen the net — search for links/meetings and check June events more broadly.
Command: for q in link meet hangouts call recording video link; do echo "== q=$q =="; curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")&timeMin=2018-06-01T00:00:00-07:00&timeMax=2018-06-30T00:00:00-07:00&singleEvents=true" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for e in d.get('items',[]):
    print(e['id'], e.get('summary'), e['start'].get('dateTime'), '| desc:', (e.get('description') or '')[:200])
"; done
Response: {"status": "success", "stdout": "== q=link ==\n== q=meet ==\n== q=hangouts ==\n== q=call ==\n== q=recording ==\n== q=video ==\n== q=link =="}

#### Step 6
Reasoning: No results. The user is saying "a video link where the Maple Room is booked on Thursday." Maybe this means a video link (a link to a meeting/video) that was created/booked in the Maple Room on Thursday. In other words, the video link might not be a calendar event, but something like a Zoom/Meet link associated with the Maple Room booking. Hmm.

Wait — rereading it: "add 'Bring the printed roadmap' along with a video link where the Maple Room is booked on Thursday to the description of the confirmed sprint review."

Interpretation: the sprint review has Maple Room booked on Thursday (confirmed). And the description should include "Bring the printed roadmap" plus "a video link." Where does that video link come from? It might be from a different event on Thursday, like a "video" event, or perhaps a video link associated with the room booking. Let me check all events for that Thursday (June 21), and also the entire June period, to look for video links within the descriptions.

Let me fetch all events for that Thursday, and all events for June.

I didn't find a calendar event with a video link, so I'll check all June events and Thursday's schedule for links in descriptions.
Command: curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?timeMin=2018-06-01T00:00:00-07:00&timeMax=2018-06-30T00:00:00-07:00&singleEvents=true&maxResults=250" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for e in d.get('items',[]):
    print('---')
    print(e['id'], '|', e.get('summary'), '|', e.get('status'), '|', e['start'].get('dateTime'))
    desc = e.get('description')
    if desc: print('DESC:', desc[:500])
    conf = e.get('hangoutLink') or (e.get('conferenceData') or {}).get('entryPoints')
    if conf: print('CONF:', conf)
    loc = e.get('location')
    if loc: print('LOC:', loc)
"
Response: {"status": "success", "stdout": "---\n6k6rhikvtl34h5a336r7c0ak4g | Sprint review | confirmed | 2018-06-21T09:00:00-07:00\n---\nnf7p3l27s3ekl4om7qov57c40q | Team lunch | tentative | 2018-06-22T12:00:00-07:00"}

#### Step 7
Reasoning: There are only 2 events on the June primary calendar. Let me check other calendars in the calendar list too — there might be a work calendar with a video link. I'll list the calendars and search for "video" across all of them.

Only two events on the primary calendar. Let me check the other calendars in the account before concluding.
Command: curl -s "https://www.googleapis.com/calendar/v3/users/me/calendarList" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for c in d.get('items',[]):
    print(c['id'], '|', c.get('summary'), '|', c.get('accessRole'))
"
Response: {"status": "success", "stdout": "jordan.lee@northwind.example | jordan.lee@northwind.example | owner"}

#### Step 8
Reasoning: There's only one calendar. In other words, there's no video link anywhere. The user's request is as follows: "Add 'Please bring the printed roadmap' to the description of the confirmed sprint review that has the video link where the Maple Room is reserved on Thursday. If there isn't one, just tell me."

Interpretation: They're asking for the description of the confirmed sprint review that has a video link, for which the Maple Room is reserved on Thursday. In other words, the qualifying event must satisfy the following conditions: be a confirmed sprint review, have a video link, and have the Maple Room reserved on Thursday.

The sprint review I found (Thursday June 21, Maple Room reserved, confirmed) has neither a description nor a video link. The "video link" might be referring to a conference link (a hangout/meet link) attached to the event. Let me re-check the full details of the event — the earlier query with the default maxAttendees already displayed the entire event, and there was no conferenceData/hangoutLink/description. Just to be safe, I'll fetch the event individually with supportsAttachments and the like, and verify thoroughly.

One calendar only. Let me do a final full-detail check of the sprint review event itself for any embedded link fields.
Command: curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events/6k6rhikvtl34h5a336r7c0ak4g?maxAttendees=10&conferenceDataVersion=1" | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"kind\": \"calendar#event\",\n    \"etag\": \"\\\"bd2479833fd39442\\\"\",\n    \"id\": \"6k6rhikvtl34h5a336r7c0ak4g\",\n    \"status\": \"confirmed\",\n    \"created\": \"2018-05-01T00:00:00+00:00\",\n    \"updated\": \"2018-05-01T00:00:00+00:00\",\n    \"htmlLink\": \"https://calendar.google.com/calendar/event?eid=6k6rhikvtl34h5a336r7c0ak4g\",\n    \"summary\": \"Sprint review\",\n    \"creator\": {\n        \"email\": \"jordan.lee@northwind.example\",\n        \"displayName\": \"Jordan Lee\",\n        \"self\": true\n    },\n    \"organizer\": {\n        \"email\": \"jordan.lee@northwind.example\",\n        \"displayName\": \"Jordan Lee\",\n        \"self\": true\n    },\n    \"start\": {\n        \"dateTime\": \"2018-06-21T09:00:00-07:00\",\n        \"timeZone\": \"America/Los_Angeles\"\n    },\n    \"end\": {\n        \"dateTime\": \"2018-06-21T09:30:00-07:00\",\n        \"timeZone\": \"America/Los_Angeles\"\n    },\n    \"iCalUID\": \"6k6rhikvtl34h5a336r7c0ak4g@google.com\",\n    \"sequence\": 0,\n    \"reminders\": {\n        \"useDefault\": true\n    },\n    \"eventType\": \"default\",\n    \"attendees\": [\n        {\n            \"email\": \"priya.nair@northwind.example\",\n            \"responseStatus\": \"accepted\",\n            \"displayName\": \"Priya Nair\"\n        },\n        {\n            \"email\": \"maple-room@northwind.example\",\n            \"responseStatus\": \"accepted\",\n            \"displayName\": \"Maple Room\",\n            \"resource\": true\n        }\n    ]\n}"}

#### Step 9
Reasoning: There is no video link anywhere:
- The only event in the calendar is: Sprint Review (confirmed, Thursday June 21, with Maple Room reserved) and Team Lunch (tentative, June 22).
- The Sprint Review event has no description, no hangoutLink, no conferenceData, no location, no links of any kind.
- Text searches for "video," "link," "meet," "hangouts," "call," "recording" all returned nothing.

The user said, "If there isn't one, just tell me" — that is, if there's no video link to add, just let them know. In other words, I should not make a change to the description without a video link. I'll report that the event exists (confirmed sprint review on Thursday with Maple Room reserved) but that there's no video link anywhere on the calendar that should be added.

I checked, and there's no video link to add — so I left the event untouched.

What I found:
- **Sprint review** — Thu Jun 21, 9:00–9:30 AM, status **confirmed**, with **Maple Room** booked (Priya Nair also attending). This is clearly "the" confirmed sprint review.
- That event has no description, no meeting/hangout link, and no conference data.
- I searched the calendar (your only calendar) for anything with "video", "link", "meet", "hangouts", "call", or "recording" in the past or coming weeks — nothing. The only other June event is a tentative team lunch on Jun 22, which also has no link.

If you have the video link (or a meeting/recording URL) handy, send it over and I'll append "Bring the printed roadmap" plus that link
Command: 
Response: null

## Final answer
I checked, and there's no video link to add — so I left the event untouched.

What I found:
- **Sprint review** — Thu Jun 21, 9:00–9:30 AM, status **confirmed**, with **Maple Room** booked (Priya Nair also attending). This is clearly "the" confirmed sprint review.
- That event has no description, no meeting/hangout link, and no conference data.
- I searched the calendar (your only calendar) for anything with "video", "link", "meet", "hangouts", "call", or "recording" in the past or coming weeks — nothing. The only other June event is a tentative team lunch on Jun 22, which also has no link.

If you have the video link (or a meeting/recording URL) handy, send it over and I'll append "Bring the printed roadmap" plus that link to the sprint review's description right away.

## State diff
- INSERT calendar_sync_tokens: {"id": 1, "token": "sync_20180617000000000000_swFcU3TwmKevVogIJoP7vw", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:53:50.228552"}
- INSERT calendar_sync_tokens: {"id": 2, "token": "sync_20180617000000000000_ZawIZoxqhHc4S_Ypdrk-WA", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:54:39.013424"}
- INSERT calendar_sync_tokens: {"id": 3, "token": "sync_20180617000000000000_DgfScRyMeivnqzKzGwYePQ", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:54:39.764972"}
- INSERT calendar_sync_tokens: {"id": 4, "token": "sync_20180617000000000000_UIUcVDdMo3OvfojahSeDqA", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:55:07.117494"}
- INSERT calendar_sync_tokens: {"id": 5, "token": "sync_20180617000000000000_UDPGbKYzVThMKPaPc67xfA", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:55:07.205354"}
- INSERT calendar_sync_tokens: {"id": 6, "token": "sync_20180617000000000000_KQGXyWIYMbFjZIeKVetZ2A", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:55:07.292398"}
- INSERT calendar_sync_tokens: {"id": 7, "token": "sync_20180617000000000000_G3Jb_sOI7Wk-9TcS0qbrIg", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:55:07.328488"}
- INSERT calendar_sync_tokens: {"id": 8, "token": "sync_20180617000000000000_eL3DWipCpyo2psdZMrr-zA", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:55:07.365535"}
- INSERT calendar_sync_tokens: {"id": 9, "token": "sync_20180617000000000000_YwkudCGv8RtWdP7f4J7BIA", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:55:07.400674"}
- INSERT calendar_sync_tokens: {"id": 10, "token": "sync_20180617000000000000_Rfk1Jf4Id9b7x6A71hch-g", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:55:07.435481"}
- INSERT calendar_sync_tokens: {"id": 11, "token": "sync_20180617000000000000_Mjhi7Ci40hlU1iGi5sBBxQ", "user_id": "u_actor", "resource_type": "events", "resource_id": "jordan.lee@northwind.example", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:55:48.181332"}
- INSERT calendar_sync_tokens: {"id": 12, "token": "sync_20180617000000000000_SYqAqDB8Cu8ERqOkOZMzoA", "user_id": "u_actor", "resource_type": "calendarList", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-29T01:56:01.321792"}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: presented?. Provisional exposed facts: [].

Give your verdict for this trial.