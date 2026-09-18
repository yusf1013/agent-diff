# Assignment W03

Referent: Conversation

Route: Conversation → Message → Reaction → User

Resolution mode: underspecified

Relationship meanings (positions identify conceptual roles, not database IDs):
- Conversation (position 0) contains Message (position 1).
- Message (position 1) receives Reaction (position 2).
- Reaction (position 2) is contributed by User (position 3).

Identify the first entity using this complete chain. Conditions on one intermediate role must concern that same record. Do not invent equality between a membership channel and a message location.

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
