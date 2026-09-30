Done. Added **Needs Review** to all 3 of Priya's open issues in the Web team:

- **WEB-1** – Rate limiter drops valid requests (Todo)
- **WEB-2** – Cache invalidation misses on deploy (In Progress) — kept its existing Backend label
- **WEB-3** – Add retry to webhook sender (Backlog)

One heads-up: Linear's `labelIds` input *replaces* the full label set rather than appending, so on the first pass WEB-2 briefly lost its Backend label — I caught it in a verification query and restored both labels, so everything's intact now.
