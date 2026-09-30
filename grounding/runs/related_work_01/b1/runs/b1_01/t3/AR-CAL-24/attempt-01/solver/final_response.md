I found the right calendar — "Front Desk" at Building 4, 3rd Floor (`c_a98f93ef…@group.calendar.google.com`) — and confirmed its current description:

> "Reserve front desk coverage for shift scheduling."

However, I can't update it via the API: this environment's Calendar proxy blocks all calendar metadata updates (PATCH/PUT on the calendar resource return a 404 by design), and I won't work around that.

**To do it manually** (takes ~15 seconds):
1. In Google Calendar, click the calendar name → **⋮ → Settings and share** → **More settings**
2. In the **About this calendar → Description** field, set it to:
   > Reserve front desk coverage for shift scheduling. Badge access is required after 6 pm.
3. Click **Save and Close**

I've noted this limitation in my local TOOLS.md so I don't hit this wall again.
