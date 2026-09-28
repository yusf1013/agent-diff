I found a name collision in Linear that I want to flag before I touch anything:

- There's a literal **Priya Chen** (`priya.chen@vendorworks.example`, guest) — but she currently has **no assigned issues at all**, so no security review ticket belongs to her.
- The only security review ticket assigned to a vendorworks guest is **GRC-3 "Security review: Mobile app"** (currently **Medium**), and it's assigned to **Priyanka Chen** (`priyanka.chen@vendorworks.example`, guest).
- (The other security review ticket, GRC-5 "Network access," is assigned to internal teammate Dana Whitfield, so it doesn't match your description.)

So it looks like the person you mean is **Priyanka Chen** and the ticket is **GRC-3**. Since there's a distinct "Priya Chen" in the system too, I don't want to bump the wrong one on a guess.

Want me to bump **GRC-3 → Urgent**? If you actually meant the literal Priya Chen, let me know — but she has no assigned security review ticket to bump.
