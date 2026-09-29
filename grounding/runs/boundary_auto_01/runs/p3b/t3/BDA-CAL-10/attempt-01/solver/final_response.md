I could not change the location because I do not have write permission on Leo's on-call calendar. Details:

- Target calendar: `leo-oncall@northwind.example` ("Leo on-call", owner leo.park@northwind.example). My access level there is **reader** (read-only).
- Target event found: "On-call handoff" (event ID `ev_handoff`), scheduled 2018-06-19 09:00–09:30 (America/Los_Angeles).
- The PATCH to set location to "Building 3, Conference Room A" failed with **HTTP 403 — "Insufficient permissions for calendar: leo-oncall@northwind.example"**.
- I verified the event is not mirrored on any calendar where I do have write/owner access (primary and Projects calendars), so there is no writable copy I can edit.

To complete this, either (a) Leo (the calendar owner) grants me "writer" access to `leo-oncall@northwind.example`, or (b) the location update is performed using Leo's account. Once write access is available, the update would be: PATCH /calendars/leo-oncall@northwind.example/events/ev_handoff with body {"location":"Building 3, Conference Room A"}.
