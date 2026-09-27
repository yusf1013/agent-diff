I couldn't complete this — I found the right calendar but my access doesn't allow the change.

**Identified target:** the "APAC team" calendar (`apac@northwind.example`, Asia/Tokyo) — it contains the June 21 all-hands created and organized by Kenji Sato. (The other Tokyo-time calendar's all-hands on June 21 was created by Aiko Mori, and "Kenji team" has an all-hands on June 22, not 21.)

**Blocker:** I have only **writer** access to that calendar, and the API returns `403: You do not have permission to update this calendar` for calendar metadata changes (summary/description). That requires owner or admin access.

Options:
1. Have Kenji Sato (the calendar owner) run it: `PATCH /calendars/apac@northwind.example` with `{"description": "APAC team events"}`.
2. Upgrade my account's access to the calendar to **admin**, and I can make the change.
