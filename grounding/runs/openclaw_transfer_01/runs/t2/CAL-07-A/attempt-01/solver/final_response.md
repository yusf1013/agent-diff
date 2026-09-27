I dug into this one and hit a snag — here's what I found:

**Kenji Sato's calendars:**
- **"Kenji planning"** (`kenji-home@northwind.example`) — timezone **America/Los_Angeles**. Its All-hands is **June 21** (1:00 PM PDT).
- **"Kenji team"** (`kenji-team@northwind.example`) — timezone **Asia/Tokyo**. Its All-hands is **June 22** (9:00 AM PDT / 1:00 AM JST).

So the "Tokyo-time" and "all-hands on June 21" clues point to two different calendars — only "Kenji team" is actually in Asia/Tokyo, but its all-hands is June 22, not June 21.

I went with the best match for the core descriptor — **"Kenji team"** (Kenji Sato's Tokyo-time calendar) — and tried to set its description to "APAC team events", but the API rejected it:

> 403 Forbidden — "You do not have permission to update this calendar"

I only have **writer** access on Kenji's calendars (enough to create/edit events, not metadata). Changing a calendar's description requires **owner** access.

Want me to:
1. Wait for owner access to be granted on `kenji-team@northwind.example` (and I'll retry), or
2. Did you actually mean "Kenji planning" (the one with the June 21 all-hands)? I don't own that one either, so it would hit the same wall.

Note: the other Tokyo-time calendar on your list, "Tokyo office," is owned by Aiko Mori — I do own that one, but it's not Kenji's, so I haven't touched it.
