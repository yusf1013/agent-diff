I found the calendar but couldn't complete the change. Here's the situation:

- **Calendar found:** "Tokyo office" (`tokyo-office@northwind.example`) — timezone Asia/Tokyo, Kenji Sato has writer access, and it contains the "All-hands" event on June 21 (11:00–12:00, created/organized by Aiko Mori).
- **The change failed:** PATCH to update the calendar description returned `403 — "You do not have permission to update this calendar"`. I retried once with a clean request and got the same error.

Notably, the ACL lists the authenticated account (jordan.lee@northwind.example) as *owner* while the calendar's data owner is aiko.mori@northwind.example, so it looks like a permission conflict on the server side rather than the right target being missing. I'd suggest checking calendar sharing/ownership in Google Calendar settings, or having Aiko make the change — otherwise let me know and I can try a different approach.
