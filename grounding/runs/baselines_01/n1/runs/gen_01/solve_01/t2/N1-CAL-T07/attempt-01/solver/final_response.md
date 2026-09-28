I can't complete this one — the API is blocking it. Here's what I found:

**What I did:**
1. Listed calendars — found `Team calendar` owned by Kenji Sato (`team-kenji@northwind.example`, data owner: `kenji.sato@northwind.example`)
2. Attempted the rename via `PATCH /calendars/{calendarId}` with the new title
3. Google returned **403: "You do not have permission to update this calendar"**

**Why:** The currently authenticated account (`jordan.lee@northwind.example`) shows up in the calendar list with an "owner" access role, but Kenji's calendar ACL list is empty and Google rejects the metadata update. In practice, only Kenji Sato (the actual data owner) can rename this calendar.

**To get it done:**
- Kenji Sato renames it himself, **or**
- Kenji grants Jordan's account full control (`writer`/owner) in the calendar's settings — then I can retry and it should go through

Want me to retry once access is granted, or should I reach out to Kenji some other way?
