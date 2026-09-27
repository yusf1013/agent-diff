I checked the Marketing calendar (`marketing@northwind.example`) and there's no write-access rule for dana.whitfield@northwind.example to remove. Here's what I found in its ACL:

- **dana.whitfield@northwind.example** — `reader` (view only)
- **northwind.example** (domain) — `writer`
- **dana.white@northwind.example** — `writer`
- **jordan.lee@northwind.example** — `owner`

So I didn't change anything, per your "if there isn't one" instruction.

Two things worth noting:
1. Dana Whitfield does have a rule on that calendar, but it's read-only — want me to remove that too?
2. Technically, Dana currently *can* write via the domain-wide `writer` rule for northwind.example. If your goal is to actually block their write access, we'd need to remove/restrict that domain rule (which affects everyone in the org) — let me know if you want that.
