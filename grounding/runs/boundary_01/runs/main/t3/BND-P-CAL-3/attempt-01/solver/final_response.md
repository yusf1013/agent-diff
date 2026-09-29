I was unable to complete the task due to insufficient permissions. Here's what I found and attempted:

1. **Located the calendar**: Leo's on-call calendar is `leo-oncall@northwind.example` ("Leo on-call", owned by leo.park@northwind.example).

2. **Found the event**: "On-call handoff" (ID: `ev_handoff_leo`) on Tuesday, June 19, 2018, currently scheduled for 9:00 AM – 9:30 AM Pacific Time.

3. **Attempted to move it to 10:00**: A PATCH request to change the time to 10:00 AM – 10:30 AM PT failed with a 403 "Insufficient permissions" error.

**Reason for failure**: My access role on Leo's on-call calendar is **reader** (read-only). Modifying an event requires at least "writer" access. I would need Leo Park (or a calendar owner/admin) to grant me writer access to `leo-oncall@northwind.example` before I can move the event.
