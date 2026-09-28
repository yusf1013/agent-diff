No such calendar — so I didn't change anything. Here's what I found:

- There is one "Team Calendar" on your list (`c_e70cd8ef...@group.calendar.google.com`, owned by leo.park@northwind.example), but your access role on it is **reader**, not writer.
- I can't verify its sharing settings (design team as writer), since the ACL isn't readable with reader-level access — the API returned 403.

So the "Team Calendar" you'd want to hide — one you have **writer** access to, shared with the design team as a writer — doesn't exist in your calendar list. The only Team Calendar there is a read-only subscription, which is a different thing. Want me to hide that read-only one instead, or leave it as is?
