**Audit**

- Qualifying roots (message referents whose author holds membership in #mentorship-hub): M1 (Dana), M2 (Farid). Exactly 2, matching assigned MULTIPLE count. M2's extra unrelated reaction from Priya does not disqualify it — Farid's own membership chain is complete.
- Condition extracted from request, independent of downstream action: author's User record must hold a Conversation-Membership record whose Conversation is #mentorship-hub. The reaction-add operation itself imposes no eligibility filter (any message can receive a reaction), so it cannot be used to exclude candidates — confirmed no property-as-eligibility error.
- Condition→negative mapping:
  - "author lacks membership in #mentorship-hub, holds an unrelated channel" → M3 (Priya, #general only).
  - "author holds membership in a similarly-named but distinct channel" (near-name decoy, tests topic/name precision) → M4 (Owen, #mentors-lounge).
  - "author holds no conversation membership at all" (missing-edge) → M5 (Lucia).
  - "message posted inside #mentorship-hub but author not a member of it" (binding confusion between message location and membership channel) → M6 (Theo).
  All four negatives fail the sole condition (membership-in-#mentorship-hub) while otherwise reading as plausible candidates; none accidentally re-qualifies through another record.
- Capability check: downstream operation is "add a supported reaction" (👀/eyes), which is in the supported emoji list and requires no authorship restriction on the target message — matches the menu's preferred write exactly. No read-only fallback needed.
- No discrepancies found; no repairs required. Wording, roots, and negatives are internally consistent and preserved.

---

**Route:** Message → User → Conversation Membership → Conversation
**Resolution mode:** multiple

**Request:** "Add 👀 to the messages from people who are members of #mentorship-hub."

**Selection conditions:** the message's author holds a conversation-membership record in the conversation named #mentorship-hub (the message itself may be posted anywhere).

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 (Dana) | Dana authored M1 in #general; Dana holds membership in #mentorship-hub | Match |
| M2 (Farid) | Farid authored M2 in #random; Farid holds membership in #mentorship-hub; M2 also carries an unrelated 👍 from Priya | Match with unrelated activity |
| M3 (Priya) | Priya authored M3 in #general; Priya's only conversation membership is #general | Wrong conversation only |
| M4 (Owen) | Owen authored M4 in #general; Owen holds membership in #mentors-lounge (similarly named, distinct channel) | Wrong conversation only (near-name decoy) |
| M5 (Lucia) | Lucia authored M5 in #general; Lucia holds no conversation memberships (only workspace membership) | Missing membership relationship |
| M6 (Theo) | Theo authored M6 posted directly in #mentorship-hub; Theo holds no membership in #mentorship-hub (posted while not a member) | Message location mistaken for membership; membership condition fails |