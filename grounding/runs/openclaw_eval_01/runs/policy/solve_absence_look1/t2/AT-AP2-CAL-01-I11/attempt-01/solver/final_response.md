Ran into a wall — here's what happened:

1. **Calendar settings** (`PATCH /calendars/product_team_mkt`) → 403: "You do not have permission to update this calendar."
2. **Your calendar list entry** (`PATCH /calendarList/...`) → accepted, but the summary came back unchanged as "Product Team".

That's because **Product Team is a shared calendar** — it's owned by `dana.whitfield@northwind.example` and your account has **reader-only access**. You can't rename a shared calendar (not even how it displays for you); the owner controls that name.

To get it renamed to "Eng Product Sync," Dana would need to change it on her end. Want me to try anything else — like sending a message to Dana about it? (I'd need the channel/contact details for that.)
