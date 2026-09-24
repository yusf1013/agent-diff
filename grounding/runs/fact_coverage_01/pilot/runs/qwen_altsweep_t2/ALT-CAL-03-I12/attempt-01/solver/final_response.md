There is no individual ACL entry for dana.whitfield@northwind.example on the **Marketing** calendar (marketing@northwind.example), so there is nothing specific to remove for her.

However, her write access comes from a **domain-level** ACL rule that grants "writer" access to the entire **northwind.example** domain. This means every @northwind.example user currently has write access to that calendar, including Dana.

If you'd like to remove write access specifically for Dana (or for the whole domain), let me know and I can:
- Remove the domain-level writer rule entirely (affects all @northwind.example users), or
- Remove the domain rule and add back individual entries for the other team members who should keep write access.
