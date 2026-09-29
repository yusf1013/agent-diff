I could not add Omar Haddad as an optional attendee because I only have read-only (reader) access to Leo's on-call calendar.

Details:
- Calendar: "Leo on-call" (ID: `leo-oncall@northwind.example`), data owner: leo.park@northwind.example. My access role is `reader`.
- Event: "On-call handoff" (ID: `ev_handoff`), Tue 2018-06-19 09:00–09:30 PT, organizer Leo Park. It currently has no attendees.
- Attempted a PATCH to add `omar.haddad@northwind.example` (displayName "Omar Haddad", optional: true) → returned HTTP 403 "Insufficient permissions for calendar: leo-oncall@northwind.example" (reproduced on retry).

Modifying an event (adding an attendee) requires at least `writer` access, which I do not have. To proceed, the calendar owner (Leo Park) would need to grant me writer/organizer access to `leo-oncall@northwind.example`, or make the change directly.
