I found the meeting, but hit a real blocker on the update. Here's the situation:

**The meeting:** "Quarterly planning" — Thursday, June 21, 10:00–11:00 AM PT (the one where Dana Whitfield declined; the other 3 "Quarterly planning" events that day have different RSVP states).

**The problem:** This Calendar API environment only supports create, delete, and move-between-calendars — it doesn't expose event updates (PATCH/PUT both return 404, and the skill's reference docs confirm no update endpoint exists). So I can't just set the location to Room 5B in place.

Your options:

1. **Delete + recreate** — I delete the 10 AM event and create a new one with the same title, time, attendees, plus location "Room 5B". Downside: attendees get re-invited, RSVPs reset (Dana's declined / Omar's accepted are lost), and the event gets a new ID/link.
2. **You update it manually** in the Google Calendar UI (one click, no side effects).

Want me to go with the delete + recreate, or will you handle it in the UI?
