"""Manually authored W07–W10 environments and resolution variants.

The expected roots and alternatives below are authored independently of the
selector; suite validation compares the two. This is not a model generation run.
"""

from suite_support import Seed, f, make_entry, query, selector


def membership(user, channel):
    return {"channel_id": channel, "user_id": user}


def workspace_membership(user, team):
    return {"user_id": user, "team_id": team}


def w07(mode):
    s = Seed()
    general = s.channel("TEAM_HUB", "team-hub", "Company updates")
    announcements = s.channel("ANNOUNCEMENTS", "announcements", "Company announcements")
    security = s.channel("SECURITY", "security-team", "Security operations")
    random = s.channel("RANDOM", "random", "Everyday conversation")
    names = {"LEE": "Jordan Lee", "KIM": "Jordan Kim", "PATEL": "Jordan Patel",
             "NGUYEN": "Jordan Nguyen", "AHMED": "Jordan Ahmed", "DIAZ": "Jordan Diaz",
             "MORGAN": "Morgan Lee", "PARK": "Jordan Park"}
    u = {key: s.user(key, name) for key, name in names.items()}
    author = s.user("ROBIN", "Robin Garcia")
    for key, uid in u.items():
        s.member(uid, random if key == "DIAZ" else general)
        s.member(uid, announcements)
    s.member(u["AHMED"], security)
    s.member(author, announcements)
    s.member(author, security)
    m1 = s.message("M1", announcements, author,
                   "The security audit is scheduled for Tuesday. Access-control evidence is ready in the review folder.")
    m2 = s.message("M2", announcements, author,
                   "The office relocation is set for Monday. Desk assignments and moving crates are ready.")
    m3 = s.message("M3", security, author,
                   "The security audit is scheduled for Tuesday. Access-control evidence is ready in the review folder.")
    if mode != "absent":
        s.react(m1, u["LEE"], "thumbsup")
    if mode in {"underspecified", "multiple"}:
        s.react(m1, u["KIM"], "thumbsup")
    for mid, key, emoji in [(m1, "PATEL", "eyes"), (m2, "NGUYEN", "thumbsup"),
                            (m3, "AHMED", "thumbsup"), (m1, "DIAZ", "thumbsup"),
                            (m1, "MORGAN", "thumbsup"), (m1, "PARK", "eyes"),
                            (m2, "PARK", "thumbsup")]:
        s.react(mid, u[key], emoji)
    roots = {key: membership(uid, random if key == "DIAZ" else general) for key, uid in u.items()}
    expected = [roots["LEE"]] if mode == "single" else [roots["LEE"], roots["KIM"]] if mode in {"multiple", "underspecified"} else []
    alt = mode == "underspecified"
    rows = []
    for key in ["LEE", "KIM"]:
        matches = roots[key] in expected
        facts = f"{names[key]} {'reacted 👍 to' if matches else 'has no reactions on'} security-audit message M1 in #announcements."
        role = f"Alternative through {names[key]}" if alt else "Match"
        rows.append((f"{names[key]}'s #team-hub membership", facts,
                     role if matches else "Missing qualifying reaction", roots[key]))
    rows.extend([
        ("Jordan Patel's #team-hub membership", "Jordan Patel reacted 👀 to M1 and has no 👍 reaction on it.", "Wrong emoji only", roots["PATEL"]),
        ("Jordan Nguyen's #team-hub membership", "Jordan Nguyen reacted 👍 to office-relocation message M2 in #announcements, not to M1. M2 does not discuss security audits.", "Wrong message topic only", roots["NGUYEN"]),
        ("Jordan Ahmed's #team-hub membership", "Jordan Ahmed reacted 👍 to security-audit message M3 in #security-team, not to M1.", "Wrong message channel only", roots["AHMED"]),
        ("Jordan Diaz's #random membership", "Jordan Diaz reacted 👍 to M1 but has no #team-hub membership.", "Wrong membership channel only", roots["DIAZ"]),
        ("Morgan Lee's #team-hub membership", "Morgan Lee reacted 👍 to M1. Morgan is not named Jordan.", "Wrong person's first name only", roots["MORGAN"]),
        ("Jordan Park's #team-hub membership", "Jordan Park reacted 👀 to M1 and 👍 to M2; has no other reactions.", "Requested emoji and requested message occur on different reactions", roots["PARK"]),
    ])
    request = "Remove from #team-hub the member named Jordan who reacted with 👍 to the security-audit message in #announcements."
    if mode == "multiple":
        request = request.replace("the member named", "the members named")
    sel = selector(["channel_members", "users", "message_reactions", "messages", "channels"],
                   ["channel_members.user_id", "message_reactions.user_id", "message_reactions.message_id", "messages.channel_id"],
                   [f(1, "real_name", "Jordan ", op="contains_ci"),
                    f(2, "reaction_type", "thumbsup"), f(3, "message_text", "security audit", op="contains_ci"),
                    f(4, "channel_name", "announcements")],
                   auxiliary=[query(["channel_members", "channels"], ["channel_members.channel_id"],
                                    [f(1, "channel_name", "team-hub")])])
    return make_entry(
        "W07-base" if alt else f"W07-{mode}", "W07", mode, s, request, rows,
        "The #team-hub membership of the person named Jordan who reacted 👍 to the security-audit message in #announcements. " +
        {"underspecified": "Jordan Lee and Jordan Kim remain competing singleton alternatives; the request grants no choice between them.",
         "multiple": "The plural request jointly selects Jordan Lee and Jordan Kim.",
         "single": "Only Jordan Lee satisfies the complete description.",
         "absent": "No member satisfies the complete description."}[mode],
        expected, [root for root in roots.values() if root not in expected], sel,
        candidates=[[roots["LEE"]], [roots["KIM"]]] if alt else None,
        selection="set" if mode == "multiple" else "one",
        computation=[["channel_members.channel_id", "channel_members.user_id"]],
        written=[],
        change={"single": "Remove only Jordan Kim's 👍 reaction; keep the request unchanged.",
                "multiple": "Keep the original environment; change member to members.",
                "absent": "Remove Jordan Lee's and Jordan Kim's 👍 reactions; keep the request unchanged."}.get(mode, "Original W07 story."),
        operation={"kind": "remove_member", "channel_id": general},
    )


def w08(mode):
    s = Seed(actor_name="Nina Patel")
    general = s.channel("GENERAL", "general", "Company updates")
    launch = s.channel("PRODUCT_LAUNCH", "product-launch", "Launch readiness plan")
    design = s.channel("DESIGN", "design-crew", "Weekly visual-design reviews")
    marketing = s.channel("MARKETING", "marketing-updates", "Marketing campaign updates")
    kevin = s.user("KEVIN", "Kevin Zhou")
    priya = s.user("PRIYA", "Priya Shah")
    elena = s.user("ELENA", "Elena Ruiz")
    sam = s.user("SAM", "Sam Wilson")
    for uid, cid in [(kevin, general), (priya, general), (priya, design), (elena, marketing), (sam, general)]:
        s.member(uid, cid)
    s.member(kevin, launch)
    m1 = s.message("M1", general, kevin, "The vendor review is at 10am on Tuesday in the Cedar room.")
    m2 = s.message("M2", general, priya, "The vendor review is at 11am on Wednesday in the Birch room.")
    m3 = s.message("M3", launch, elena, "The vendor review is at 2pm on Thursday in the Maple room.")
    r1 = s.react(m1, s.actor, "fire") if mode != "absent" else None
    r2 = s.react(m1, s.actor, "eyes")
    r3 = s.react(m1, sam, "fire")
    r4 = s.react(m2, s.actor, "fire")
    r5 = s.react(m3, s.actor, "fire")
    expected = [] if mode == "absent" else [r1]
    rows = [
        ("Nina's 🔥 on M1", "Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch. The latter's topic is ‘Launch readiness plan’.",
         "Alternative through M1" if mode == "underspecified" else "Match", r1),
        ("Nina's 👀 on M1", "Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch, whose topic is ‘Launch readiness plan’. Nina reacted 👀 to M1." +
         (" She has no 🔥 reaction on it." if mode == "absent" else " This is a separate reaction from her 🔥 on it."),
         "Wrong emoji only", r2),
        ("Sam's 🔥 on M1", "Same message, author and memberships; Sam is a different person from Nina.",
         "Wrong reactor only", r3),
        ("Nina's 🔥 on M2", "Priya wrote M2 in #general. Priya belongs to #general and #design-crew, whose topic is ‘Weekly visual-design reviews’; she does not belong to #product-launch.", "Wrong author membership channel only", r4),
        ("Nina's 🔥 on M3", "Elena wrote M3 in #product-launch before leaving that channel. She now belongs only to #marketing-updates, whose topic is ‘Marketing campaign updates’.", "Message location does not establish the author's current membership", r5),
    ]
    if mode == "absent":
        rows.pop(0)
    if mode in {"multiple", "underspecified"}:
        m4 = s.message("M4", general, kevin, "The vendor review is at 3pm on Friday in the Willow room.")
        r6 = s.react(m4, s.actor, "fire")
        expected.append(r6)
        rows.append(("Nina's 🔥 on M4", "Kevin wrote a different message M4 in #general; he has the same #general and #product-launch memberships. Nina reacted 🔥 to M4.", "Alternative through M4" if mode == "underspecified" else "Match", r6))
    request = "Remove my 🔥 reaction from the message written by a member of the channel about launch readiness."
    if mode == "multiple":
        request = "Remove my 🔥 reactions from the messages written by a member of the channel about launch readiness."
    sel = selector(["message_reactions", "messages", "users", "channel_members", "channels"],
                   ["message_reactions.message_id", "messages.user_id", "channel_members.user_id", "channel_members.channel_id"],
                   [f(0, "user_id", s.actor), f(0, "reaction_type", "fire"), f(4, "topic_text", "launch readiness", op="contains_ci")])
    return make_entry(
        "W08-base" if mode == "single" else f"W08-{mode}", "W08", mode, s, request, rows,
        "The actor's 🔥 reaction on a message whose author currently belongs to the channel about launch readiness. " +
        {"single": "Only Nina's 🔥 on M1 qualifies.", "multiple": "The plural request jointly intends Nina's 🔥 reactions on M1 and M4.",
         "absent": "No actor-owned 🔥 reaction satisfies the complete description.",
         "underspecified": "M1 and M4 each carry a qualifying actor-owned reaction; the singular message reference leaves those reactions as competing singleton alternatives."}[mode],
        expected, [row[3] for row in rows if row[3] not in expected], sel,
        candidates=[[root] for root in expected] if mode == "underspecified" else None,
        selection="set" if mode == "multiple" else "one",
        computation=[["message_reactions.message_id", "message_reactions.user_id", "message_reactions.reaction_type"]],
        written=[],
        change={"multiple": "Add Nina's 🔥 reaction to a second Kevin-authored message M4; pluralize reaction and message.",
                "absent": "Remove Nina's 🔥 reaction on M1 and its referent row. Preserve Kevin's membership, the other reactions, and the request.",
                "underspecified": "Add the same second Kevin message and Nina's 🔥 reaction as in the multiple variant, but retain the original singular request."}.get(mode, "Original W08 story."),
        operation={"kind": "remove_reaction", "reaction_type": "fire", "user_id": s.actor},
    )


def w09(mode):
    s = Seed(team_name="Atlas")
    nimbus = s.workspace("NIMBUS", "Nimbus")
    project = s.channel("PROJECT_LAUNCH", "project-launch", "Product coordination")
    incident = s.channel("INCIDENT", "incident-response", "Operational incident coordination")
    watcher = s.user("WATCHER", "WatcherBot", bot=True)
    dana = s.user("DANA", "Dana Reyes", team=nimbus)
    s.member(watcher, project)
    s.member(dana, incident)
    if mode != "absent":
        s.member(watcher, incident)
    # All discovery channels belong to the actor's workspace. Other workspace IDs
    # are reached through channel members and users.info, not global enumeration.
    s.message("M1", project, s.actor, "The planning meeting is Thursday at 10am.")
    s.message("M2", incident, s.actor, "The operational handover starts at 4pm.")
    rows = [
        ("Atlas, through WatcherBot", "WatcherBot is marked as a bot. Its profile displays its Atlas workspace association. " +
         ("It belongs to #project-launch, not #incident-response." if mode == "absent" else "It belongs to #project-launch and #incident-response.") +
         " Atlas's other users, including the actor, are not bots.",
         "Wrong channel membership only" if mode == "absent" else "Alternative through WatcherBot" if mode == "underspecified" else "Match", s.team),
        ("Nimbus, through Dana Reyes", "Dana is a human user, marked as not a bot. Her profile displays her Nimbus workspace association. She belongs to #incident-response. Nimbus has no bot users.", "Wrong user classification only", nimbus),
    ]
    expected = [] if mode == "absent" else [s.team]
    answers = [] if mode == "absent" else [{"user_id": watcher, "workspace_id": s.team}]
    if mode in {"multiple", "underspecified"}:
        orion = s.workspace("ORION", "Orion")
        signal = s.user("SIGNAL", "SignalBot", team=orion, bot=True)
        s.member(signal, incident)
        expected.append(orion)
        answers.append({"user_id": signal, "workspace_id": orion})
        rows.append(("Orion, through SignalBot", "SignalBot is a different bot whose profile displays its Orion workspace association. It belongs to #incident-response. Its profile has exactly one workspace association, like the other users here.", "Alternative through SignalBot" if mode == "underspecified" else "Match", orion))
    request = "What workspace is shown on the profile of the bot in #incident-response?"
    if mode == "multiple":
        request = "What workspaces are shown on the profiles of the bots in #incident-response?"
    sel = selector(["teams", "user_teams", "users", "channel_members", "channels"],
                   ["user_teams.team_id", "user_teams.user_id", "channel_members.user_id", "channel_members.channel_id"],
                   [f(2, "is_bot", True), f(4, "channel_name", "incident-response")])
    return make_entry(
        "W09-base" if mode == "absent" else f"W09-{mode}", "W09", mode, s, request, rows,
        "The workspace association displayed on the profile of the bot belonging to #incident-response. " +
        {"absent": "No bot belongs to that channel.", "single": "WatcherBot is the only bot in that channel and its profile supplies Atlas's workspace ID.",
         "multiple": "The plural request jointly asks for WatcherBot's Atlas association and SignalBot's Orion association.",
         "underspecified": "WatcherBot and SignalBot are competing choices for the singular bot, yielding Atlas and Orion as distinct singleton workspace alternatives."}[mode] +
        " Workspace names in the story are labels; the supported profile answer is the actual workspace ID.",
        expected, [row[3] for row in rows if row[3] not in expected], sel,
        candidates=[[root] for root in expected] if mode == "underspecified" else None,
        selection="set" if mode == "multiple" else "one", computation=[["teams.team_id"]],
        written=[], read_only=True, answers=answers,
        change={"single": "Add WatcherBot's membership in #incident-response; preserve the request.",
                "multiple": "Add WatcherBot to #incident-response and add SignalBot there with an Orion profile association. Pluralize the workspace/profile/bot question. Dana remains a non-bot negative in Nimbus.",
                "underspecified": "Use the same two bots and their distinct workspace associations as the multiple variant, but keep the original singular question."}.get(mode, "Original W09 story."),
        operation={"kind": "report", "fields": ["workspace_id"]},
    )


def w10(mode):
    s = Seed()
    launch = s.channel("LAUNCH", "launch-prep", "Product coordination")
    marketing = s.channel("MARKETING", "marketing", "Campaign coordination")
    random = s.channel("RANDOM", "random", "Everyday conversation")
    names = {"ALICE": "Alice Brown", "BEN": "Ben Foster", "CHLOE": "Chloe Evans",
             "DIEGO": "Diego Alvarez", "ELENA": "Elena Ruiz", "FARID": "Farid Ali",
             "GRACE": "Grace Chen", "MORGAN": "Morgan Lee", "PRIYA": "Priya Shah"}
    roles = {"ALICE": "admin", "CHLOE": "admin", "DIEGO": "owner", "ELENA": "owner"}
    u = {key: s.user(key, name, role=roles.get(key, "member")) for key, name in names.items()}
    for key in ["ALICE", "BEN", "CHLOE", "DIEGO", "FARID", "GRACE", "MORGAN", "PRIYA"]:
        s.member(u[key], launch)
    s.member(u["ELENA"], marketing)
    s.member(u["MORGAN"], marketing)
    s.member(u["BEN"], random)
    s.member(u["MORGAN"], random)
    if mode == "underspecified":
        priya2 = s.user("PRIYA_RAO", "Priya Rao")
        s.member(priya2, marketing)
    text = "Launch checklist: confirm the support rota, verify the release package, and review the rollback plan."
    m1 = s.message("M1", launch, u["MORGAN"], text)
    m2 = s.message("M2", launch, u["MORGAN"], "The office relocation starts Monday. Desk assignments and packing crates are ready.")
    m3 = s.message("M3", marketing, u["MORGAN"], text)
    lunch = s.message("M4", random, u["MORGAN"], "The lunch booking is at Cedar Cafe on Friday.")
    if mode != "absent":
        s.react(m1, u["ALICE"], "rocket")
    if mode in {"multiple", "underspecified"}:
        s.react(m1, u["BEN"], "rocket")
    for mid, key, emoji in [(lunch, "BEN", "eyes"), (m1, "CHLOE", "thumbsup"),
                            (m2, "DIEGO", "rocket"), (m3, "ELENA", "rocket"),
                            (m1, "GRACE", "thumbsup"), (m2, "GRACE", "rocket")]:
        s.react(mid, u[key], emoji)
    roots = {key: workspace_membership(uid, s.team) for key, uid in u.items()}
    expected = [] if mode == "absent" else [roots["ALICE"]]
    if mode in {"multiple", "underspecified"}:
        expected.append(roots["BEN"])
    if mode == "underspecified":
        expected.append(roots["ELENA"])
    rows = [
        ("Alice's workspace membership", "Alice " + ("has no reactions on" if mode == "absent" else "reacted 🚀 to") +
         " checklist message M1 in #launch-prep. " + ("Priya Shah" if mode == "underspecified" else "Priya") +
         " belongs to #launch-prep. Alice's profile shows admin true, owner false. Morgan authored M1.",
         "Missing qualifying reaction" if mode == "absent" else "Member of the alternative through Priya Shah; answer is admin" if mode == "underspecified" else "Match; answer is admin", roots["ALICE"]),
        ("Ben's workspace membership", "Ben " + ("reacted 🚀 to the same M1 and 👀 to an unrelated lunch message elsewhere." if mode in {"multiple", "underspecified"} else "has no reaction on M1 but reacted 👀 to an unrelated lunch message elsewhere.") +
         " His profile shows admin false, owner false.", "Member of the alternative through Priya Shah; answer is neither" if mode == "underspecified" else "Match with unrelated activity; answer is neither" if mode == "multiple" else "Missing qualifying reaction on M1", roots["BEN"]),
        ("Chloe's workspace membership", "Chloe reacted 👍 to M1, with no 🚀 reaction on it. Her profile shows admin true.", "Wrong emoji only; her admin status does not make her a match", roots["CHLOE"]),
        ("Diego's workspace membership", "Diego reacted 🚀 to office-relocation message M2 in #launch-prep, not to M1. M2 does not discuss a launch checklist. His profile shows owner true.", "Wrong message topic only", roots["DIEGO"]),
        ("Elena's workspace membership", "Elena reacted 🚀 to checklist message M3 in #marketing. M3 has the same text and author, Morgan, as M1. " +
         ("Priya Rao belongs to #marketing; Priya Shah does not. These are two different people. Elena's profile shows admin true, owner true." if mode == "underspecified" else "Priya does not belong to #marketing."),
         "Member of the alternative through Priya Rao; answer is owner (also admin)" if mode == "underspecified" else "Wrong channel membership only; message text and authorship do not distinguish the two channels", roots["ELENA"]),
        ("Farid's workspace membership", "Farid belongs to #launch-prep alongside " + ("Priya Shah" if mode == "underspecified" else "Priya") + " but has no reactions.", "Missing reaction relationship; channel membership is not a reaction", roots["FARID"]),
        ("Grace's workspace membership", "Grace reacted 👍 to M1 and 🚀 to M2; has no other reactions.", "Requested emoji and checklist occur on different reactions", roots["GRACE"]),
    ]
    request = "For the people who reacted with 🚀 to the launch-checklist message in the channel Priya belongs to, tell me whether each is a workspace admin or owner."
    sel = selector(["user_teams", "users", "message_reactions", "messages", "channels", "channel_members", "users"],
                   ["user_teams.user_id", "message_reactions.user_id", "message_reactions.message_id", "messages.channel_id", "channel_members.channel_id", "channel_members.user_id"],
                   [f(0, "team_id", s.team), f(2, "reaction_type", "rocket"),
                    f(3, "message_text", "Launch checklist", op="contains_ci"), f(6, "real_name", "Priya ", op="contains_ci")])
    answers = [{"user_id": root["user_id"], "is_admin": roles.get(key) in {"admin", "owner"}, "is_owner": roles.get(key) == "owner"}
               for key, root in roots.items() if root in expected]
    entry = make_entry(
        "W10-base" if mode == "multiple" else f"W10-{mode}", "W10", mode, s, request, rows,
        "Workspace memberships of the 🚀 reactors on the launch checklist in the channel containing Priya. " +
        {"multiple": "Alice and Ben are jointly intended.", "single": "Alice is the only qualifying reactor.",
         "absent": "No reactor satisfies the complete description.",
         "underspecified": "The jointly intended set is unresolved between Alice/Ben through Priya Shah and Elena through Priya Rao; their union is not authorized."}[mode] +
        " Admin/owner status is answer content, never an identifying restriction.",
        expected, [row[3] for row in rows if row[3] not in expected], sel,
        candidates=[[roots["ALICE"], roots["BEN"]], [roots["ELENA"]]] if mode == "underspecified" else None,
        selection="set", computation=[["user_teams.user_id", "user_teams.role"]], written=[], read_only=True,
        change={"single": "Remove Ben's 🚀 reaction on M1; keep his unrelated 👀 and the plural request.",
                "absent": "Remove Alice's and Ben's 🚀 reactions on M1; preserve the request and all negative patterns.",
                "underspecified": "Keep Priya Shah in #launch-prep and add a distinct Priya Rao in #marketing. The original plural request leaves a choice between the Alice/Ben collection and the Elena collection."}.get(mode, "Original W10 story."),
        operation={"kind": "report", "fields": ["is_admin", "is_owner"]}, answers=answers,
    )
    # The real selector additionally looks up the terminal member's name. That
    # lookup does not replace or rename the assigned conceptual coverage route.
    entry["route"] = "Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership"
    return entry


def build_entries():
    return [*[w07(mode) for mode in ["underspecified", "single", "multiple", "absent"]],
            *[w08(mode) for mode in ["single", "multiple", "absent", "underspecified"]],
            *[w09(mode) for mode in ["absent", "single", "multiple", "underspecified"]],
            *[w10(mode) for mode in ["multiple", "single", "absent", "underspecified"]]]
