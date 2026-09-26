# Google Calendar seed operations

A seed is a list of `[operation, {arguments}]`. Every operation also accepts:
- `"ref": "name"`, so that `"@name"` stands for the created row's id anywhere in the scenario;
- `"set": {column: value}`, for extra columns of the created row.

## Already present
- **People** (key → name, email `first.last@northwind.example`): `actor` Jordan Lee (the acting user), `priya` Priya
  Nair, `omar` Omar Haddad, `maya` Maya Chen, `sam` Sam Rivera, `dana` Dana Whitfield, `kenji` Kenji Sato,
  `aiko` Aiko Mori, `leo` Leo Park.
- **The actor's primary calendar**, id `jordan.lee@northwind.example`. Write `"primary"` as the calendar argument of
  an operation, or `"@primary"` elsewhere.

## Time
The agent under test is told it is **Sunday 2018-06-17, 00:01, America/Los_Angeles**. Give event times as local
Los Angeles wall-clock times without an offset (`"2018-06-21T10:00:00"`); the operation stores them with the June
offset (-07:00). All-day events take dates (`"2018-06-21"`), and their end date is exclusive.

## Operations
| Operation | Arguments (defaults) | Creates |
|---|---|---|
| `person` | `key`, `name`, `email` (from the name) | a person who can organize, create or attend events |
| `calendar` | `id` (usually an email-like id, for example `"apac@northwind.example"`), `summary`, `owner` ("actor"), `tz` (America/Los_Angeles), `description` (""), `access` (the actor's role: "owner", "writer", "reader", "freeBusyReader"), `primary` (false), `hidden` (false), `selected` (true), `override` (a summaryOverride on the actor's list entry), `data_owner` (the owner's email), `in_list` (true: on the actor's calendar list), `location` | a calendar and the actor's calendar-list entry for it |
| `event` | `id`, `calendar`, `summary`, `start`, `end`, `all_day` (false), `organizer` ("actor"), `creator` (organizer), `attendees` ([]), `description` (""), `location` (""), `status` ("confirmed"; also "tentative", "cancelled"), `transparency` ("opaque" or "transparent"), `visibility` ("default", "public", "private"), `event_type` ("default", "focusTime", "outOfOffice"), `recurrence` (a list such as `["RRULE:FREQ=WEEKLY;BYDAY=TU"]`), `utc_start` (overrides the stored start instant, for example `"2018-06-21T03:00:00Z"`), `hangout` (false, true, or a Meet URL), `color_id` | an event with its attendees |
| `acl` | `id`, `calendar`, `role` ("owner", "writer", "reader", "freeBusyReader"), `scope_type` ("user", "group", "domain", "default"), `scope_value` (an email or domain) | a sharing rule |
| `row` | `table`, `values` | any other row; required columns you leave out get neutral defaults |

**Attendees.** Each attendee is either `[person key, response]`, `[person key, response, "optional"]`, or an object
`{"person": key or "email": ..., "name": ..., "status": ..., "optional": bool, "resource": bool}`. A room or other
resource is an object with an email and `"resource": true`. Responses are "accepted", "declined", "tentative" or
"needsAction".

## Example
```json
[["calendar", {"id": "apac@northwind.example", "summary": "APAC team", "owner": "kenji", "access": "writer",
               "tz": "Asia/Tokyo"}],
 ["event", {"id": "ev_review", "calendar": "primary", "summary": "Design review: Checkout",
            "start": "2018-06-21T10:00:00", "end": "2018-06-21T11:00:00", "organizer": "priya",
            "attendees": [["priya", "accepted"], ["omar", "declined", "optional"]], "ref": "target"}]]
```
