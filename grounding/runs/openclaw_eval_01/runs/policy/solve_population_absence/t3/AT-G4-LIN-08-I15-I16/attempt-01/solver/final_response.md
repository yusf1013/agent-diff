I checked Linear, and the request doesn't line up cleanly with the issue tree — here's what I found:

**MOB-42 "Checkout crash on launch"** has exactly one sub-issue:
- **MOB-57** "Polish saved-card search" — **5** points, due **Oct 22** ❌ (not 3-point, not Oct 15)

The only **3-point issues due Oct 15** in the workspace are:
- **MOB-56** "MOB-42 follow-up: Apple Pay sheet" — parent is **MOB-7**, not MOB-42 (it just *mentions* MOB-42 in the title)
- **MOB-55** "Fix Apple Pay sheet layout follow-up" — parent is **MOB-421** ("Checkout crash, enterprise follow-up"), a MOB-42-related issue but not MOB-42 itself

So strictly by hierarchy, MOB-42 has no 3-point sub-issue due Oct 15. Before I change anything, which one did you mean — **MOB-56** (title references MOB-42), **MOB-55** (child of the MOB-42 follow-up issue), or should I treat this as a mismatch and do nothing?
