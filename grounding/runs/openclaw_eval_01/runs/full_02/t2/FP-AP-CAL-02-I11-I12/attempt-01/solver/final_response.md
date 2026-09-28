I checked, and there's no calendar that matches. Here's what I found:

- **There is a "Team Calendar"** on your list (`team-sales@northwind.example`), but you have **reader** access to it — not writer.
- The **only calendar you have writer-level access to** is your own primary (`jordan.lee@northwind.example`).
- I can't verify the design-team sharing on that Team Calendar either — with reader access, the API returns 403 when I try to read its ACL, so I can't confirm whether it's shared with a design team as a writer.

Since the only "Team Calendar" doesn't meet the writer-access requirement, I left it as-is rather than hiding it. If you actually wanted that reader-level Team Calendar hidden anyway, or if the design-team calendar has a slightly different name, let me know and I'll take care of it.
