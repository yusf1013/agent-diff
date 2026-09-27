I checked the Marketing calendar (`marketing@northwind.example`) ACL. Here's what I found:

- **dana.whitfield@northwind.example** → has a `reader` rule only — no direct write grant to remove.
- Her write access comes from a **domain-wide rule**: `northwind.example` → `writer`. Removing that would strip write access from everyone in the domain, not just Dana, so I didn't touch it.
- (Note: `dana.white@northwind.example` has a separate user-level writer rule — different person, left alone.)

So there's no Dana-specific write access to remove. If you want to revoke her write access specifically, the cleanest path would be to delete the domain writer rule and re-grant `writer` explicitly to whoever should keep it — want me to do that?
