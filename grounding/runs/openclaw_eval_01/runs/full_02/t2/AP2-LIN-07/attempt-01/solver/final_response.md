Done. The document is now in the Q4 Roadmap project.

**What I did:**
1. **Disambiguated** — six documents share the title "Retention Playbook." Only one matched all your criteria: `doc-target` (Growth team, content: "churn mitigation steps for at-risk accounts… discusses Q3 churn analysis"). The others were Platform/Growth Marketing docs or a similarly-titled "Retention Playbook Update."
2. **Located the project** — "Q4 Roadmap" (`p-q4-roadmap`).
3. **Moved the document** via `documentUpdate` setting `projectId: p-q4-roadmap`.

**Verified final state:** the document now shows project = **Q4 Roadmap**, team still **Growth** (https://linear.app/northwind/document/doc-target).

One hiccup: the update mutation's response payload errored on a non-nullable `success` field (server-side serialization quirk), so I re-queried the document directly to confirm the change actually landed — it did.
