Done. I changed the domain rule (`northwind.example`) on the Marketing calendar from **writer → reader**, which removes Dana's write access (and the domain-wide write grant, as agreed).

Current ACL on `marketing@northwind.example`:
- dana.whitfield@northwind.example — reader (unchanged)
- northwind.example (domain) — reader (was writer)
- dana.white@northwind.example — writer (unchanged)
- jordan.lee@northwind.example — owner
