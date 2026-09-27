I checked the Marketing calendar (`marketing@northwind.example`) ACLs. Here's the situation:

- **dana.whitfield@northwind.example** — direct rule: `reader` (already read-only)
- **northwind.example** (domain) — `writer` — this is the rule actually granting Dana write access
- dana.white@northwind.example — `writer`
- jordan.lee@northwind.example — `owner`

Dana doesn't have a personal write grant; her write access comes from the **domain-level writer rule**, which covers everyone at northwind.example (including dana.white). Google Calendar has no way to exclude a single user from a domain rule, so the only way to strip her write access is to change the domain rule from `writer` to `reader` — which would also remove write access for every other northwind.example user.

How do you want to proceed?
1. Change the **domain rule** to `reader` (removes write access for all domain users, including dana.white), or
2. Leave it as is — I can't remove just Dana's write access in isolation with the current rules.

Let me know and I'll make the change.
