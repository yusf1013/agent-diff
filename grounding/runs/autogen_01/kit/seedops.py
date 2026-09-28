"""Seed operations: the vocabulary a writer uses to build a scenario's seed, expanded into replica table rows.

A seed is a list of operations, each `[op, {arguments}]`. Every operation may carry
- `"ref": "name"`: the id of the row it creates can then be written `"@name"` anywhere in the scenario;
- `"set": {column: value}`: extra columns for the row it creates (checked against the table).

`["row", {"table": ..., "values": {...}}]` inserts any table's row directly; required columns it leaves out get
neutral defaults. The domain operations wrap the helpers the hand-built scenarios used (fact_coverage_01 pilot and
fact_coverage_02), so the rows follow the same conventions.
"""
from __future__ import annotations

import copy
import json
import re
import uuid
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from grounding.runs.autogen_01.kit import seed_linear as LIN
from grounding.runs.autogen_01.kit import seed_slack as SLK

UUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
T0 = "2026-06-01T09:00:00+00:00"


class SeedError(ValueError):
    pass


def local_offset(local: str, tz: str) -> str:
    """The UTC offset ("-07:00") of zone `tz` at the naive local time `local` ("2018-06-21T10:00:00")."""
    delta = datetime.fromisoformat(local).replace(tzinfo=ZoneInfo(tz)).utcoffset()
    minutes = int(delta.total_seconds() // 60)
    sign = "-" if minutes < 0 else "+"
    return f"{sign}{abs(minutes) // 60:02d}:{abs(minutes) % 60:02d}"


def resolve(value, refs):
    """Replace "@name" strings (whole strings only) by the referenced ids, recursively."""
    if isinstance(value, str) and value.startswith("@") and len(value) > 1:
        if value[1:] not in refs:
            raise SeedError(f"unknown reference {value}")
        return refs[value[1:]]
    if isinstance(value, list):
        return [resolve(v, refs) for v in value]
    if isinstance(value, dict):
        return {k: resolve(v, refs) for k, v in value.items()}
    return value


def _metadata(domain):
    if domain == "slack":
        from grounding.integrations.agentdiff import runtime
        return runtime.dependencies()[1]
    from grounding.integrations.agentdiff import smoke_runtime as smoke
    return smoke.load_seed_module(domain).Base.metadata


def _default(column, table, row):
    from sqlalchemy import JSON, Boolean, DateTime, Enum, Float, Integer, Numeric
    try:
        from sqlalchemy.dialects.postgresql import JSONB
    except ImportError:  # pragma: no cover
        JSONB = JSON
    t = column.type
    name = column.name
    if isinstance(t, Enum):
        return list(t.enums)[0]
    if isinstance(t, Boolean):
        return False
    if isinstance(t, (Integer,)):
        return 0
    if isinstance(t, (Float, Numeric)):
        return 0.0
    if isinstance(t, DateTime):
        return T0
    if isinstance(t, (JSON, JSONB)):
        return [] if name.endswith(("History", "Ids", "ids")) else {}
    if name in ("url", "inboxUrl"):
        return f"https://example.invalid/{table}/{row.get('id', 'x')}"
    if name == "slugId":
        return str(row.get("id", "x"))
    return ""


class Builder:
    domain = ""
    actor = ""

    def __init__(self):
        self.t = {}
        self.refs = {}
        self.meta = None

    # -- generic -------------------------------------------------------------------------------------------
    def _table(self, name):
        if self.meta is None:
            self.meta = _metadata(self.domain)
        table = self.meta.tables.get(name)
        if table is None:
            raise SeedError(f"unknown {self.domain} table {name}")
        return table

    def _check_columns(self, table_name, row):
        table = self._table(table_name)
        unknown = set(row) - set(table.columns.keys())
        if unknown:
            raise SeedError(f"unknown {table_name} columns: {sorted(unknown)}")

    def _last(self, table):
        rows = self.t.get(table) or []
        if not rows:
            raise SeedError(f"no {table} row to update")
        return rows[-1]

    def _set(self, table, extra):
        if extra:
            row = self._last(table)
            self._check_columns(table, extra)
            row.update(extra)

    def op_row(self, table, values):
        table_obj = self._table(table)
        row = dict(values)
        self._check_columns(table, row)
        for column in table_obj.columns:
            if column.name in row or column.nullable or column.default is not None or column.server_default is not None:
                continue
            if column.primary_key and column.autoincrement is True:
                continue
            row[column.name] = _default(column, table, row)
        self.t.setdefault(table, []).append(row)
        pk = [c.name for c in table_obj.primary_key.columns]
        return row.get(pk[0]) if len(pk) == 1 else None

    def run(self, ops):
        if not isinstance(ops, list):
            raise SeedError("seed must be a list of [operation, {arguments}]")
        for i, op in enumerate(ops):
            if not (isinstance(op, list) and len(op) == 2 and isinstance(op[0], str) and isinstance(op[1], dict)):
                raise SeedError(f"seed[{i}] is not [operation, {{arguments}}]: {json.dumps(op)[:200]}")
            name, args = op[0], dict(op[1])
            ref = args.pop("ref", None)
            extra = args.pop("set", None)
            fn = getattr(self, f"op_{name}", None)
            if fn is None:
                raise SeedError(f"seed[{i}]: unknown operation '{name}' for {self.domain}")
            try:
                ident = fn(**resolve(args, self.refs))
            except SeedError as exc:
                raise SeedError(f"seed[{i}] {name}: {exc}") from None
            except TypeError as exc:
                raise SeedError(f"seed[{i}] {name}: {exc}") from None
            except (KeyError, StopIteration) as exc:
                raise SeedError(f"seed[{i}] {name}: unknown key or id {exc}") from None
            if extra:
                table = self.last_table
                self._set(table, resolve(extra, self.refs))
            if ref:
                if ref in self.refs:
                    raise SeedError(f"seed[{i}]: ref '{ref}' defined twice")
                self.refs[ref] = ident
        return self

    @property
    def last_table(self):
        return getattr(self, "_last_table", None)

    def _append(self, table, row):
        self.t.setdefault(table, []).append(row)
        self._last_table = table
        return row

    def seed(self):
        return {k: copy.deepcopy(v) for k, v in self.t.items() if v}


# ---------------------------------------------------------------------------------------------------------------
class BoxSeed(Builder):
    domain = "box"
    actor = "30000000001"
    DEFAULT_PEOPLE = {"JL": "Jordan Lee", "MC": "Maya Chen", "ML": "Maya Lopez", "LP": "Leo Park",
                      "DW": "Dana Whitfield", "PN": "Priya Nair", "OH": "Omar Haddad", "SR": "Sam Rivera"}
    HUB_FLAGS = {"is_ai_enabled": False, "is_collaboration_restricted_to_enterprise": False,
                 "can_non_owners_invite": True, "can_shared_link_be_created": True, "view_count": 0}

    def __init__(self):
        super().__init__()
        for t in ["box_users", "box_collections", "box_folders", "box_files", "box_file_versions", "box_comments",
                  "box_tasks", "box_task_assignments", "box_hubs", "box_hub_items"]:
            self.t[t] = []
        self.people = {}
        for i, (key, name) in enumerate(self.DEFAULT_PEOPLE.items()):
            self.op_person(key, name, id=f"3000000000{i + 1}")
        self._append("box_folders", {"id": "0", "type": "folder", "name": "All Files", "parent_id": None,
                                     "owned_by_id": self.actor, "description": "", "item_status": "active", "size": 0})

    def uid(self, key):
        if key in self.people:
            return self.people[key][0]
        if any(r["id"] == key for r in self.t["box_users"]):
            return key
        raise SeedError(f"unknown person '{key}' (use a person key such as MC, or add one with the person operation)")

    def op_person(self, key, name, login=None, id=None, role=None):
        uid = id or f"3000000{len(self.people) + 1:04d}"
        login = login or name.lower().replace(" ", ".") + "@northwind.example"
        self.people[key] = (uid, name)
        self._append("box_users", {"id": uid, "type": "user", "name": name, "login": login, "status": "active",
                                   "role": role or ("admin" if uid == self.actor else "user"),
                                   "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"})
        return uid

    def op_collection(self, id, name="Favorites", collection_type="favorites"):
        self._append("box_collections", {"id": id, "type": "collection", "name": name,
                                         "collection_type": collection_type})
        return id

    def _shared(self, iid, access="company"):
        return json.dumps({"url": f"https://app.box.com/s/{iid}", "access": access, "effective_access": access})

    def op_folder(self, id, name, parent="0", owner="JL", creator=None, modifier=None, description="", tags=None,
                  collections=None, created=T0, modified=T0, size=0, shared=None):
        row = {"id": id, "type": "folder", "name": name, "parent_id": parent, "owned_by_id": self.uid(owner),
               "created_by_id": self.uid(creator or owner), "modified_by_id": self.uid(modifier or creator or owner),
               "description": description, "item_status": "active", "size": size, "tags": json.dumps(tags or []),
               "collections": json.dumps(collections or []), "created_at": created, "modified_at": modified,
               "sequence_id": "0", "etag": "0"}
        if shared:
            row["shared_link"] = self._shared(id, shared if isinstance(shared, str) else "company")
        self._append("box_folders", row)
        return id

    def op_file(self, id, name, parent, owner="JL", creator=None, modifier=None, description="", tags=None,
                collections=None, version=1, shared=None, locked=False, uploader=None, created=T0, modified=T0,
                size=48213):
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
        uploader_name = self.people.get(uploader or modifier or creator or owner, (None, "Jordan Lee"))[1]
        row = {"id": id, "type": "file", "name": name, "parent_id": parent, "owned_by_id": self.uid(owner),
               "created_by_id": self.uid(creator or owner), "modified_by_id": self.uid(modifier or creator or owner),
               "description": description, "size": size, "extension": ext, "item_status": "active",
               "version_number": str(version), "comment_count": 0, "tags": json.dumps(tags or []),
               "collections": json.dumps(collections or []), "created_at": created, "modified_at": modified,
               "sequence_id": "0", "etag": "0", "uploader_display_name": uploader_name}
        if shared:
            row["shared_link"] = self._shared(id, shared if isinstance(shared, str) else "company")
        if locked:
            row["lock"] = json.dumps({"type": "lock", "id": "L" + id, "created_by": {"type": "user", "id": self.uid(owner)},
                                      "created_at": T0, "is_download_prevented": False})
        self._append("box_files", row)
        self.t["box_file_versions"].append({"id": "9" + id, "type": "file_version", "file_id": id, "name": name,
                                            "size": size, "version_number": str(version), "created_at": modified,
                                            "modified_at": modified, "modified_by_id": row["modified_by_id"]})
        return id

    def op_comment(self, id, file, author, message, reply_to=None, created="2026-06-10T15:00:00+00:00"):
        self._append("box_comments", {"id": id, "type": "comment", "file_id": file, "item_id": reply_to or file,
                                      "item_type": "comment" if reply_to else "file", "message": message,
                                      "created_by_id": self.uid(author), "created_at": created, "modified_at": created,
                                      "is_reply_comment": bool(reply_to)})
        for row in self.t["box_files"]:
            if row["id"] == file:
                row["comment_count"] += 1
        return id

    def op_task(self, id, file, creator, message, action="review", done=False, due=None, created=T0):
        self._append("box_tasks", {"id": id, "type": "task", "item_id": file, "item_type": "file", "message": message,
                                   "action": action, "is_completed": done, "completion_rule": "all_assignees",
                                   "due_at": due, "created_by_id": self.uid(creator), "created_at": created})
        return id

    def op_assign(self, id, task, to, by, state="incomplete"):
        file_id = next(t["item_id"] for t in self.t["box_tasks"] if t["id"] == task)
        self._append("box_task_assignments", {"id": id, "type": "task_assignment", "task_id": task, "item_id": file_id,
                                              "item_type": "file", "assigned_to_id": self.uid(to),
                                              "assigned_by_id": self.uid(by), "resolution_state": state,
                                              "assigned_at": T0})
        return id

    def op_hub(self, id, title, creator="JL", updater=None, description=None, created=T0, updated=T0):
        self._append("box_hubs", {"id": id, "type": "hubs", "title": title,
                                  "description": description if description is not None else f"{title} materials",
                                  "created_by_id": self.uid(creator), "updated_by_id": self.uid(updater or creator),
                                  "created_at": created, "updated_at": updated, **self.HUB_FLAGS})
        return id

    def op_hub_item(self, id, hub, item, item_type="file", added_by="JL", position=1):
        table = "box_files" if item_type == "file" else "box_folders"
        name = next(r["name"] for r in self.t[table] if r["id"] == item)
        self._append("box_hub_items", {"id": id, "type": "hub_item", "added_at": T0, "added_by_id": self.uid(added_by),
                                       "hub_id": hub, "item_id": item, "item_type": item_type, "item_name": name,
                                       "position": position})
        return id


# ---------------------------------------------------------------------------------------------------------------
class CalendarSeed(Builder):
    domain = "calendar"
    actor = "u_actor"
    DOMAIN_MAIL = "northwind.example"
    DEFAULT_PEOPLE = {"actor": "Jordan Lee", "priya": "Priya Nair", "omar": "Omar Haddad", "maya": "Maya Chen",
                      "sam": "Sam Rivera", "dana": "Dana Whitfield", "kenji": "Kenji Sato", "aiko": "Aiko Mori",
                      "leo": "Leo Park"}
    TZ = "America/Los_Angeles"

    def __init__(self):
        super().__init__()
        for t in ["calendar_users", "calendars", "calendar_list_entries", "calendar_events", "calendar_event_attendees",
                  "calendar_acl_rules"]:
            self.t[t] = []
        self.people = {}
        self.att = 0
        for key, name in self.DEFAULT_PEOPLE.items():
            self.op_person(key, name)
        self.primary = self.email("actor")
        self.op_calendar(self.primary, self.primary, owner="actor", description="Primary calendar", primary=True)

    def email(self, key):
        if key in self.people:
            return self.people[key][1]
        if isinstance(key, str) and "@" in key:
            return key
        raise SeedError(f"unknown person '{key}' (use a person key such as priya, or add one with the person operation)")

    def name_of(self, key):
        return self.people[key][0] if key in self.people else key

    def op_person(self, key, name, email=None):
        email = email or name.lower().replace(" ", ".") + "@" + self.DOMAIN_MAIL
        self.people[key] = (name, email)
        self._append("calendar_users", {"id": self.actor if key == "actor" else f"u_{key}", "email": email,
                                        "display_name": name, "self": key == "actor",
                                        "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"})
        return email

    def cal_id(self, cal):
        return self.primary if cal == "primary" else cal

    def op_calendar(self, id, summary, owner="actor", tz=None, description="", access="owner", primary=False,
                    hidden=False, selected=True, override=None, data_owner=None, in_list=True, location=None):
        owner_id = self.actor if owner == "actor" else f"u_{owner}"
        row = {"id": id, "summary": summary, "description": description, "time_zone": tz or self.TZ,
               "owner_id": owner_id, "etag": f'"etag_{id}"', "data_owner": data_owner or self.email(owner),
               "deleted": False, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
        if location is not None:
            row["location"] = location
        self._append("calendars", row)
        if in_list:
            row = {"id": f"cle_{id}", "user_id": self.actor, "calendar_id": id, "access_role": access,
                   "primary": primary, "selected": selected, "hidden": hidden, "deleted": False,
                   "etag": f'"etag_cle_{id}"', "created_at": "2018-01-01T00:00:00",
                   "updated_at": "2018-01-01T00:00:00"}
            if override:
                row["summary_override"] = override
            self.t["calendar_list_entries"].append(row)
        return id

    def op_event(self, id, calendar, summary, start, end=None, all_day=False, organizer="actor", creator=None,
                 attendees=(), description="", location="", status="confirmed", transparency="opaque",
                 visibility="default", event_type="default", recurrence=None, utc_start=None, hangout=False,
                 color_id=None):
        creator = creator or organizer
        cal = self.cal_id(calendar)
        row = {"id": id, "calendar_id": cal, "ical_uid": f"{id}@{self.DOMAIN_MAIL}", "summary": summary,
               "description": description, "location": location, "status": status, "visibility": visibility,
               "transparency": transparency, "event_type": event_type, "sequence": 0, "etag": f'"etag_{id}"',
               "creator_email": self.email(creator), "creator_display_name": self.name_of(creator),
               "organizer_email": self.email(organizer), "organizer_display_name": self.name_of(organizer),
               "creator_self": creator == "actor", "organizer_self": organizer == "actor",
               "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00"}
        if color_id:
            row["color_id"] = color_id
        if all_day:
            row.update(start={"date": start}, end={"date": end}, start_date=start, end_date=end)
        else:
            if end is None:
                raise SeedError("a timed event needs an end")
            # The event keeps its calendar's time zone, with that zone's offset on its date. (Until 2026-09-27 every
            # event got Los Angeles at -07:00, whatever its calendar; roadmap step 3.)
            tz = next((c["time_zone"] for c in self.t["calendars"] if c["id"] == cal), self.TZ)
            row.update(start={"dateTime": utc_start or f"{start}{local_offset(start, tz)}", "timeZone": tz},
                       end={"dateTime": f"{end}{local_offset(end, tz)}", "timeZone": tz},
                       start_datetime=start, end_datetime=end)
        if recurrence:
            row["recurrence"] = recurrence
        if hangout:
            row["hangout_link"] = hangout if isinstance(hangout, str) else f"https://meet.google.com/{id[:3]}-abcd-efg"
        self._append("calendar_events", row)
        for a in attendees:
            if isinstance(a, dict):
                key = a.get("person")
                email = a.get("email") or self.email(key)
                name = a.get("name") or (self.name_of(key) if key else email)
                status_ = a.get("status", "needsAction")
                optional, resource = bool(a.get("optional")), bool(a.get("resource"))
            else:
                key, status_ = a[0], a[1]
                email, name = self.email(key), self.name_of(key)
                optional, resource = len(a) > 2 and a[2] == "optional", False
            self.att += 1
            self.t["calendar_event_attendees"].append({
                "id": self.att, "event_id": id, "email": email, "display_name": name, "response_status": status_,
                "optional": optional, "organizer": key == organizer, "self": key == "actor", "resource": resource})
        self._last_table = "calendar_events"
        return id

    def op_acl(self, id, calendar, role, scope_type, scope_value):
        self._append("calendar_acl_rules", {"id": id, "calendar_id": self.cal_id(calendar), "role": role,
                                            "scope_type": scope_type, "scope_value": scope_value,
                                            "etag": f'"etag_{id}"', "deleted": False,
                                            "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"})
        return id


# ---------------------------------------------------------------------------------------------------------------
class LinearSeed(Builder):
    domain = "linear"
    actor = LIN.ACTOR

    def __init__(self):
        super().__init__()
        self.s = LIN.Seed()
        self.t = self.s.t
        self.label_ids = {}

    def _after(self, table):
        self._last_table = table

    def op_person(self, key, name, **fields):
        uid = self.s.user(key, name)
        self._after("users")
        self._set("users", fields)
        return uid

    def op_team(self, id, name, key, parent=None):
        self.s.team(id, name, key, parent)
        self._after("teams")
        return id

    def op_member(self, team, person, owner=False):
        self.s.member(team, person, owner)
        self._after("team_memberships")
        return f"tm-{team}-{person}"

    def op_label(self, name, id=None, team=None, parent=None, group=False):
        if id is not None and not UUID.match(str(id)):
            raise SeedError(f"label id '{id}' is not a UUID; the replica rejects such label ids in issueUpdate. "
                            "Omit id (one is generated) and use a ref")
        lid = id or str(uuid.uuid5(uuid.NAMESPACE_URL, f"label/{team}/{parent}/{name}/{len(self.t['issue_labels'])}"))
        self.s.label(lid, name, team, parent, group)
        self._after("issue_labels")
        return lid

    def op_state(self, team, name):
        return self.s.state(team, name)

    def op_issue(self, id, team, title, state="Todo", assignee=None, creator="actor", priority=0, estimate=None,
                 due=None, project=None, milestone=None, cycle=None, parent=None, labels=(), description="",
                 created=LIN.T0, subscribers=(), number=None):
        iid = (id, number) if number else id
        if number:
            self.s.issue_numbers[id] = number
        self.s.issue(iid, team, title, state=state, assignee=assignee, creator=creator, priority=priority,
                     estimate=estimate, due=due, project=project, milestone=milestone, cycle=cycle, parent=parent,
                     labels=labels, description=description, created=created, subscribers=subscribers)
        self._after("issues")
        return id

    def op_status(self, id, name, type, position=0):
        self.s.status(id, name, type, position)
        self._after("project_statuses")
        return id

    def op_project(self, id, name, lead=None, creator="actor", status=None, state="started", start=None, target=None,
                   priority=0, description=""):
        self.s.project(id, name, lead=lead, creator=creator, status=status, state=state, start=start, target=target,
                       priority=priority, description=description)
        self._after("projects")
        return id

    def op_milestone(self, id, project, name, target=None, status="unstarted"):
        self.s.milestone(id, project, name, target, status)
        self._after("project_milestones")
        return id

    def op_cycle(self, id, team, number, starts, ends, active=False, next=False, past=False, future=False,
                 previous=False):
        self.s.cycle(id, team, number, starts, ends, active=active, nxt=next, past=past, future=future, prev=previous)
        self._after("cycles")
        return id

    def op_comment(self, id, issue, author, body, parent=None, resolver=None, created=None, resolved=None):
        self.s.comment(id, issue, author, body, parent, resolver)
        self._after("comments")
        row = self._last("comments")
        if created:
            row["createdAt"] = row["updatedAt"] = created
        if resolved:
            row["resolvedAt"] = resolved
        return id

    def op_relation(self, id, issue, related, type="blocks"):
        self.s.relation(id, issue, related, type)
        self._after("issue_relations")
        return id

    def op_attachment(self, id, issue, title, url, creator="actor", source="api"):
        self.s.attachment(id, issue, title, source, creator, url)
        self._after("attachments")
        return id

    def op_initiative(self, id, name, owner=None, creator="actor", status="Active"):
        self.s.initiative(id, name, owner, creator, status)
        self._after("initiatives")
        return id

    def op_document(self, id, title, creator="actor", updater=None, project=None, initiative=None, team=None,
                    content=""):
        self.s.document(id, title, creator, updater, project, initiative, team, content)
        self._after("documents")
        return id

    def op_row(self, table, values):
        rid = super().op_row(table, values)
        self._last_table = table
        return rid


# ---------------------------------------------------------------------------------------------------------------
class SlackSeed(Builder):
    domain = "slack"
    actor = SLK.ACTOR

    def __init__(self):
        super().__init__()
        self.s = SLK.Seed()
        self.t = self.s.t
        self.t.setdefault("message_reactions", [])

    def op_person(self, key, name, username=None, display=None, bot=False, role=None):
        self.s.user(key, name, username=username, display=display, bot=bot)
        self._last_table = "users"
        if role:
            self.t["user_teams"][-1]["role"] = role
        return SLK.uid(key)

    def uid(self, key):
        uid = SLK.uid(key)
        if not any(u["user_id"] == uid for u in self.t["users"]):
            raise SeedError(f"unknown person '{key}' (use a person key such as priya, or add one with the person "
                            "operation)")
        return uid

    def op_channel(self, id, name, members, private=False, topic="", purpose="", gc=False):
        for m in members:
            self.uid(m)
        self.s.channel(id, name, members, private=private, topic=topic, purpose=purpose, gc=gc)
        self._last_table = "channels"
        return id

    def op_dm(self, id, person):
        self.uid(person)
        self.t["channels"].append({"channel_id": id, "channel_name": id, "team_id": "T1", "topic_text": "",
                                   "purpose_text": "", "is_private": True, "is_dm": True, "is_gc": False,
                                   "created_at": "2026-01-05T09:00:00Z", "is_archived": False})
        for key in ("actor", person):
            self.t["channel_members"].append({"channel_id": id, "user_id": SLK.uid(key),
                                              "joined_at": "2026-01-05T09:05:00Z"})
        self._last_table = "channels"
        return id

    def op_message(self, channel, author, text, at, parent=None, mentions=()):
        self.uid(author)
        if not any(c["channel_id"] == channel for c in self.t["channels"]):
            raise SeedError(f"unknown channel '{channel}'")
        mid = self.s.message(channel, author, text, at, parent=parent, mentions=mentions)
        self._last_table = "messages"
        return mid

    def op_reaction(self, message, person, name, at="2026-09-01T12:00:00Z"):
        self.t["message_reactions"].append({"message_id": message, "user_id": self.uid(person), "reaction_type": name,
                                            "created_at": at})
        self._last_table = "message_reactions"
        return message


BUILDERS = {"box": BoxSeed, "calendar": CalendarSeed, "linear": LinearSeed, "slack": SlackSeed}


def expand(domain, ops):
    """(seed tables, refs, actor id) for a list of operations."""
    builder = BUILDERS[domain]()
    builder.run(ops)
    return builder.seed(), dict(builder.refs), builder.actor
