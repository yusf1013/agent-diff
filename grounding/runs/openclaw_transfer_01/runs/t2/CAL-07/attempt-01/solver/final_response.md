I can't make that change — here's what I found and where it's stuck:

**The calendar you're describing:** `apac@northwind.example` ("APAC team")
- Owned by Kenji Sato (`kenji.sato@northwind.example`)
- Timezone: Asia/Tokyo
- Contains the "All-hands" event on June 21, 9:00 AM PT (20:00 Tokyo)

This is unambiguously the right calendar — it's the only Kenji-owned, Tokyo-timezone calendar with a June 21 all-hands.

**The problem:** I'm authenticated as Jordan Lee, and Jordan's access to this calendar is **writer** (can create events, but not modify the calendar itself). Changing a calendar's description requires **owner** permission, and the API returns:

> 403 — "You do not have permission to update this calendar"

I tried the update twice and also verified the ACL situation; writers can't edit calendar settings.

**To fix this, Kenji (the owner) would need to either:**
1. Change the description himself, or
2. Grant you owner access to the APAC team calendar — after which I can make the change immediately.

Want me to do anything else in the meantime?
