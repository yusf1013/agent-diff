I found the calendar and verified it, but hit a wall on the update:

- **Target:** "Front Desk" — Building 4, 3rd Floor (`c_a98f93ef5a9c9647d70e99dcea@group.calendar.google.com`)
- **Current description:** "Reserve front desk coverage for shift scheduling."
- **Problem:** The update method for calendar metadata isn't available in this API surface — `PATCH`/`PUT` on `/calendars/{calendarId}` return 404 no matter how I format the request (I also tried alternate paths and the `calendarList` endpoints, which only support display settings like color/visibility, not the calendar's description).

So I can't write the change through the API from here. Two options:

1. **Quick manual fix** — in Google Calendar, go to the calendar's settings (⚙️ → "Front Desk, Building 4, 3rd Floor" → *Edit description*) and set:
   > Reserve front desk coverage for shift scheduling. Badge access is required after 6 pm.
2. If this is a recurring need, it's worth checking with whoever manages the API proxy to enable `calendars.update` — I can retry immediately once it's live.

Want me to keep the intended description text on file so it's ready to apply later?
