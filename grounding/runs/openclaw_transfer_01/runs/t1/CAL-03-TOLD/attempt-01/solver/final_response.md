Dana doesn't have a personal write-access rule on the Marketing calendar, so there was nothing to remove. Here's what I found on `marketing@northwind.example`:

- **dana.whitfield@northwind.example** → `reader` (view-only)
- **northwind.example (domain)** → `writer`
- dana.white@northwind.example → writer
- jordan.lee (you) → owner

She can view but not write via her own ACL rule. Heads-up: the whole `northwind.example` domain has writer access, so she technically still *can* write through that domain rule. If you want to actually block her writing, you'd need to remove the domain-level writer rule — let me know if you want that.
