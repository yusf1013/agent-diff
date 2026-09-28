No changes made — the criteria don't match. Here's what I found:

- The only "Team Calendar" in your calendar list is `c_e70cd8ef76a09a485b101f11f1@group.calendar.google.com` (owned by leo.park@northwind.example).
- Your access role on it is **reader**, not writer.
- I also tried to read its ACL rules to check the design-team sharing, but that returned 403 (insufficient permissions — consistent with reader access, which can't view a calendar's sharing rules).

So I couldn't confirm writer access or the design-team share, and I left the calendar visible. If your access was recently upgraded to writer, re-running this should get past the ACL check and I can hide it then.
