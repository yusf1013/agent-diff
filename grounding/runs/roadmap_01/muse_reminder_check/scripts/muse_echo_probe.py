"""Offline probe of Muse settings: run `muse exec --provider echo` in a no-network bubblewrap sandbox with a given
settings.json, then report the reminder roster the session log records, the reminder tasks linked, and any settings
warnings. No API key, no network, no model calls.

    python muse_echo_probe.py '<settings json or "none">' [extra muse args...]
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BIN = "/home/yusf/.local/bin/muse-bin-1.4.0-R4302.1"
settings = sys.argv[1]
extra = sys.argv[2:]
home = Path(tempfile.mkdtemp(prefix="muse_echo_home.", dir="/home/yusf/.claude/jobs/5840209d/tmp"))
work = Path(tempfile.mkdtemp(prefix="muse_echo_work.", dir="/home/yusf/.claude/jobs/5840209d/tmp"))
(home / "prompts").mkdir()
(home / "prompts" / "p.md").write_text("Say hello.\n")
if settings != "none":
    (home / ".config" / "muse").mkdir(parents=True)
    (home / ".config" / "muse" / "settings.json").write_text(settings)
cmd = ["bwrap", "--ro-bind", "/usr", "/usr", "--symlink", "usr/bin", "/bin", "--symlink", "usr/lib", "/lib",
       "--symlink", "usr/lib64", "/lib64", "--ro-bind", "/etc", "/etc", "--proc", "/proc", "--dev", "/dev",
       "--tmpfs", "/tmp", "--dir", "/home", "--bind", str(home), "/home/agent", "--bind", str(work), "/work",
       "--ro-bind", BIN, "/opt/muse/muse", "--unshare-all", "--die-with-parent", "--new-session", "--clearenv",
       "--setenv", "HOME", "/home/agent", "--setenv", "PATH", "/usr/bin:/bin", "--setenv", "LANG", "C.UTF-8",
       "--chdir", "/work", "/opt/muse/muse", "exec", "--json", "--provider", "echo",
       "--prompt-file", "/home/agent/prompts/p.md", "--workspace", "/work", "--disable-shell",
       "--disable-web-tools", "--no-foreign-personal-context", "--approval-mode", "never", "--approval-judge", "off",
       *extra]
proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
print("exit", proc.returncode)
if proc.returncode != 0:
    print("stderr:", proc.stderr[-1500:])
logs = sorted((home / ".local" / "share" / "muse" / "sessions").rglob("session.jsonl"))
print("session logs:", len(logs))
for log in logs:
    for line in log.read_text().splitlines():
        try:
            d = json.loads(line)
        except ValueError:
            continue
        p = d.get("payload")
        ev = (p or {}).get("event", {}) if isinstance(p, dict) else {}
        k = ev.get("kind")
        if k == "model_request_configured":
            roster = ev.get("reminder_roster") or {}
            print("roster preset:", roster.get("preset"), "source:", roster.get("source"),
                  "agents:", [a.get("id") for a in roster.get("agents", [])])
        elif k == "task_stream_linked":
            print("task linked:", (ev.get("display") or {}).get("label"))
        elif k in ("model_completed",):
            print("model_completed:", ev.get("model"), (ev.get("usage") or {}).get("input_tokens"))
    text = log.read_text()
    for needle in ("settings", "unknown_member", "invalid", "reminder_roster"):
        hits = [ln for ln in text.splitlines() if needle in ln and "warning" in ln.lower()]
        for h in hits[:3]:
            print("warning line:", h[:300])
for line in (proc.stdout or "").splitlines():
    if "settings" in line.lower() and ("warn" in line.lower() or "invalid" in line.lower() or "unknown" in line.lower()):
        print("stdout warning:", line[:300])
shutil.rmtree(home)
shutil.rmtree(work)
