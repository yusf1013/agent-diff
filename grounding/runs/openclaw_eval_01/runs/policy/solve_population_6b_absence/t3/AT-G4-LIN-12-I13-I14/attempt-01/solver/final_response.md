I dug into Linear and found a mismatch I want to flag before changing anything — the identifying details don't line up with the actual assignees.

**The one person matching "Rae Ellison" + Chicago + status "Reviewing support queue"** is Raquel Ellison (`raquel.ellison@`). But she has **no assigned issues** — no offline sync issue.

**The two Apex offline sync issues** are:
- **APX-4** — "Offline sync queue ordering" — assigned to **Raquel Vance** (`raquel.vance@`, Chicago, status "Heads down shipping") — estimate 1
- **APX-5** — "Offline sync progress indicator" — assigned to **Raquel Ford** (`raquel.ford@`, Chicago, status "Out on parental leave") — estimate 1

So neither offline sync issue is assigned to the person whose status is "Reviewing support queue" — that status belongs to a third Rae Ellison (`raquel.ellison@`) who has nothing in Apex. The status hint you gave doesn't match either assignee, so I don't want to guess and set the wrong one.

Which should I set to 3 — **APX-4** or **APX-5**? (Or did you mean a different person/issue than the one the status points to?)

⚠️ 🛠️ Exec failed: `print text → run command -> search "linear" → print text → run command -> search "proxy"`
