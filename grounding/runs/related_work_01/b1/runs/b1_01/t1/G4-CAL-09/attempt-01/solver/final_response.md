I found the right event but hit a wall updating it. Here's the situation:

**The event:** "Team offsite," all-day Thursday June 21–22, with Omar Haddad (accepted) and Priya Nair (accepted) — id `pb1lnlha3konukela07avfvq1v`. I disambiguated from four similar events: a timed 10–11am offsite, a "Team offsite debrief," a June 22 offsite, and another June 21 one where Omar hadn't responded yet. This is the only all-day "Team offsite" on June 21 that Omar accepted.

**The problem:** The Calendar API connection here is read-only-ish. I tried:
- `PATCH /events/{id}` with `{"location": "Room 5B"}` → 404
- `PUT /events/{id}` with full event data → 404
- Re-inserting with the existing id → 409 (already exists)
- PATCH with the email address as calendarId → 404

GETs work fine, but no update endpoint is reachable through this proxy.

**Fallback option:** I could delete the event and re-create it with the same id, details, and attendees, adding "Room 5B" — but that resets the event's internal metadata (creation time, sequence number) and it's a destructive move, so I don't want to do it without your OK. Want me to go ahead with that?
