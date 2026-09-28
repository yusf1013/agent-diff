There isn't one that matches. Here's what I found:

- Your calendar list has one calendar named **"Team Calendar"** (`team-sales@northwind.example`, owned by leo.park@), but your access role on it is **reader**, not writer — so it doesn't meet the "I have writer access" condition.
- I tried verifying whether the design team has writer access on that calendar's sharing rules, but the API returned a 403 (insufficient permissions) since you're only a reader there.
- The rest of your list: your primary calendar (owner) and "Marketing Sync" (reader) — neither is a "Team Calendar" nor a writer-share.

So I didn't hide anything. If you meant the `team-sales@northwind.example` "Team Calendar" despite the reader access, say the word and I'll hide it from your list.
