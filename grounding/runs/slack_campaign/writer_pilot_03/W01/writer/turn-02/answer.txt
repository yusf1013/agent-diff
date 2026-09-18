**Audit**

- Identifying conditions from the request: (1) message located in channel **#product-launch**; (2) message has a reaction contributed by **Priya**; (3) that same reaction's emoji is **🚀**. The binding between person and emoji must be on one reaction record.
- Checked shared facts: each row is a distinct message; no message reused across rows in contradictory states. Channel #product-launch and #eng-internal are distinct containers.
- Recomputed selection: A and B each have a complete chain (message→🚀 reaction→Priya) inside #product-launch — two distinct qualifying roots, matching the "multiple" mode's required count. C–F each fail exactly one requirement (emoji, person, missing relation, binding). G fails only the container condition (right person+emoji+binding, wrong location) — a useful additional negative not overlapping the other single-condition failures.
- Route/mode check: exactly 2 distinct positive roots (A, B), route Message→Reaction→User preserved, no invented equalities between membership and message location.
- Downstream operation: "add a ✅" is a supported reaction-write (check is in the allowed emoji set), applied to the identified Message referents — consistent with capabilities.
- No defects found; table stands as designed.

**Final sketch**

Route: Message → Reaction → User
Resolution mode: multiple

Request: "Add a ✅ to the messages Priya reacted to with a 🚀 in #product-launch."

| Referent | Environment facts | Interpretation |
|---|---|---|
| A | Message "Shipping build 4.2 to prod tonight" in #product-launch; Priya 🚀 | Match |
| B | Message "Landing page copy finalized" in #product-launch; Priya 🚀, and also Dan 👀 on the same message | Match with unrelated activity |
| C | Message "Rollback plan drafted" in #product-launch; Priya 👀 (no 🚀 from her) | Wrong emoji only |
| D | Message "QA sign-off received" in #product-launch; Wen 🚀 (Priya did not react) | Wrong person only |
| E | Message "Marketing embargo lifted" in #product-launch; no reactions at all | Missing reaction relationship |
| F | Message "Launch retro scheduled" in #product-launch; Priya 👀 and Wen 🚀 (Priya's reaction and the 🚀 reaction are different reactions) | Person and emoji occur on different reactions |
| G | Message "Beta invite list finalized" in #eng-internal (not #product-launch); Priya 🚀 | Right person/emoji, wrong container location |