"""Shared JSON helpers; independent of historical campaign orchestration."""
import json
from pathlib import Path
from grounding.paths import REPO_ROOT as ROOT

TABLES = ('teams', 'users', 'channels', 'user_teams', 'channel_members', 'messages', 'message_reactions')


def read(path):
    return json.loads(Path(path).read_text())


def dump(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))
