Done — the `northwind.example` domain `writer` rule is removed from the Marketing calendar. Dana (Whitfield) no longer has write access; she's still a reader.

Current ACL:
- dana.whitfield@northwind.example → reader
- dana.white@northwind.example → writer
- jordan.lee@northwind.example → owner

One heads-up: that domain rule was the only write grant for the whole org, so every other northwind.example user also lost write access — not just Dana. Who should I re-grant `writer` to explicitly?
