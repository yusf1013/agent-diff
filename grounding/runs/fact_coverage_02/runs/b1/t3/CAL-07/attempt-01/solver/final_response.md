I identified the correct calendar: **`apac@northwind.example`** ("APAC team"), which is:
- Owned by Kenji Sato (kenji.sato@northwind.example)
- Timezone: Asia/Tokyo
- Contains the "All-hands" event on June 21, 2018

However, I was **unable to update the description** to "APAC team events" because the authenticated user only has **writer** access to this calendar (not owner). Both PATCH and PUT requests to modify calendar metadata returned **403 Forbidden: "You do not have permission to update this calendar"**. Only the calendar owner (Kenji Sato) can modify calendar-level properties like the description.
