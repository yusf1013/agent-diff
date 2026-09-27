I found the right calendar, but I can't change its description.

**What matches:** `apac@northwind.example` ("APAC team") — Kenji Sato's (`kenji.sato@northwind.example`) Tokyo-time (Asia/Tokyo) calendar, which contains the June 21 "All-hands" event. (The other Tokyo calendar owned by Kenji, "Kenji team", has its all-hands on June 22, so it doesn't match.)

**The blocker:** The API returns `403 — You do not have permission to update this calendar` on both the metadata PATCH and PUT. Your access to this calendar is **writer** (can add events), but changing calendar metadata like the description requires **owner** access. I tried both update methods to be sure; neither is allowed.

**Options:**
- Ask Kenji Sato (the calendar's data owner) to make the change, or
- Ask him to grant you owner access on `apac@northwind.example`, and I'll retry.

Want me to draft a short message to Kenji requesting the description change to "APAC team events"?
