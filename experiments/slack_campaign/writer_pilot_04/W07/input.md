# Assignment W07

Referent: Conversation Membership

Route: Conversation Membership → User → Reaction → Message → Conversation

Resolution mode: underspecified

Relationship meanings (positions identify conceptual roles, not database IDs):
- Conversation Membership (position 0) is held by User (position 1).
- User (position 1) contributes Reaction (position 2).
- Reaction (position 2) is attached to Message (position 3).
- Message (position 3) is located in Conversation (position 4).

Identify the first entity using this complete chain. Conditions on one intermediate role must concern that same record. Do not invent equality between a membership channel and a message location.

Downstream operation menu for this referent:
Prefer removing the selected member from the conversation belonging to that membership. User and conversation are both part of the selected membership; do not invent equality with another channel appearing along the route. Membership join times and per-channel admin roles are unavailable.

# Instructions for this assigned mode

The assigned mode is UNDERSPECIFIED. The request intends one root, but leaves
exactly 2 distinct candidate sets unresolved without delegated
authority to choose. For this pilot each set contains one root. Use partial
identifying information on an observable path attribute. Privately imagine a
fully specified reference, then omit its disambiguating detail from the request.
Only the real alternatives appear in the table; omit any hypothetical prototype.

Begin with the competing alternatives, labeled "Alternative", not full-match
answers or negatives. Show why both satisfy the supplied partial description
while identifying different roots. Do not announce ambiguity, supply a candidate
menu, use "best/any", or ask for both. Then derive one-requirement negatives from
the supplied partial description. The omitted disambiguating information is not
a condition the negatives can be required to satisfy. Recheck that shared records
do not make the supposedly different candidate sets identical.

Keep the alternatives equally supported by the supplied description and differently
consequential: selecting either changes a different target or yields a distinguishable
read answer. Do not use an identical yes/no answer for both as the only deliverable.

Style example:

Route: Conversation → Message → Reaction → User
Request: Set the topic of the channel with the deployment announcement Alex
reacted to with 👍 to “Release review on Friday”.

| Referent | Environment facts | Interpretation |
|---|---|---|
| release-updates | Alex Chen reacted 👍 to its deployment announcement | Alternative through Alex Chen |
| platform-news | Alex Patel reacted 👍 to its deployment announcement | Alternative through Alex Patel |
| delivery-notes | Alex Chen reacted 👀 to its deployment announcement | Wrong emoji only |
| office-news | Alex Chen reacted 👍 to its office-move announcement | Wrong message topic only |

No choice between Alex Chen and Alex Patel is authorized by the request.
