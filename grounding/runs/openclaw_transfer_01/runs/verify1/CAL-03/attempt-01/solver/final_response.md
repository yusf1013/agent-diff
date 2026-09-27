I checked the Marketing calendar's (`marketing@northwind.example`) ACL, and the condition doesn't match — Dana Whitfield currently has **read-only** access (role: `reader`), not write access. No change needed on her rule:

- `dana.whitfield@northwind.example` → reader
- `dana.white@northwind.example` → writer (different person)
- `northwind.example` (whole domain) → writer
- `jordan.lee@northwind.example` → owner

Two things worth flagging:

1. If you meant **dana.white@northwind.example**, I can change her role from writer to reader — just confirm.
2. Note that the **entire northwind.example domain has writer access** (rule `acl_2`), so Dana Whitfield may effectively have write access through that domain rule. If you want to truly remove her write access, that domain-level rule would need to be addressed (which would affect everyone at northwind.example).

Want me to proceed with either of those?
