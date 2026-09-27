Found it — there's one all-day offsite on June 29:

- **Offsite** — Jun 29, 2018 (all day), organized by **Maya Chen** (created by Sam Rivera)

I patched the event to set **Omar Haddad** to `role: "optional"` (keeping Maya and you as required attendees), and the API accepted it — the event was updated (sequence bumped 0 → 1). 

One caveat: the response came back with the attendee list re-issued, but it didn't echo the `role` field back on the attendees, so I couldn't independently confirm the optional flag from the API's reply. It should show up as optional in the Google Calendar UI — worth a quick glance if you want certainty.
