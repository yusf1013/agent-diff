Task could not be completed. I located Maya's team calendar (ID: maya-team@northwind.example), but I only have "writer" access, not owner access. Updating the calendar's location requires owner permissions:

- PATCH /calendars/maya-team@northwind.example → 403 "You do not have permission to update this calendar"
- GET /calendars/maya-team@northwind.example/acl → 403 "Insufficient permissions" (can't modify ACL either)

The calendar is owned by maya.chen@northwind.example. To set the location to "Building 2", the request must be made by the calendar owner, or the owner would need to grant me owner access. No available action can bypass this permission restriction.
