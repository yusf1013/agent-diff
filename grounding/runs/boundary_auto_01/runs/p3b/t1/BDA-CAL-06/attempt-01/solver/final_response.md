I couldn't grant edit access directly. The "Leo on-call" calendar (`leo-oncall@northwind.example`) is owned by Leo Park (leo.park@northwind.example), and you currently only have **reader** access. Only the calendar owner can change access control rules, so the API returns a 403 when attempting to modify the ACL.

To get edit access, you'll need to ask Leo to share the calendar with you using the "Make changes to events" permission. Once he does, your access role will upgrade from `reader` to `writer` (edit access) automatically.
