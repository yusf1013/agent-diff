"""Local OpenAI-compatible proxy between OpenClaw and Purdue GenAI Studio.

    PURDUE_GENAI_STUDIO_API_KEY=... python -m grounding.integrations.openclaw.purdue_proxy [--port 18777]

Why it exists:
- Purdue ends every streamed response by closing the connection without the final
  chunk of the chunked encoding. Node's fetch reports that as "terminated" and OpenClaw
  fails the turn, although the stream already carried `data: [DONE]`. The proxy
  re-sends the stream with a proper ending.
- Every request draws a slot from the shared cross-process limiter
  (grounding/solver/slack/purdue_rate_limit.py), so OpenClaw runs and our Python runners
  share the same 60-requests/minute budget.
- Test runs get complete evidence: requests to /run/<token>/v1/... are recorded
  (request body, raw response, timing, retries, usage) in the directory the runner
  registered for <token>. Plain /v1/... traffic (interactive use) is forwarded with
  metadata-only logging.

The proxy listens on 127.0.0.1 only, ignores the client's Authorization header and
sends the key from its own environment. It never writes the key anywhere.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import re
import sys
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import httpx

from grounding.solver.slack.purdue_rate_limit import _budget, _reserve, _state_path

UPSTREAM = "https://genai.rcac.purdue.edu/api"
DEFAULT_PORT = 18777
RETRY_STATUSES = {429, 500, 502, 503, 504}
# Purdue signals rate limiting with HTTP 400 and one of these phrases (as PurdueClient handles it).
TRANSIENT_400 = ("rate limit", "server connection error", "overloaded")
MAX_ATTEMPTS = 7  # waits 10+20+40+60+60+60 s at most, under OpenClaw's 300 s provider timeout
ROUTE = re.compile(r"^/run/([A-Za-z0-9_-]{8,64})(/v1/.*)$")


def runtime_dir() -> Path:
    base = os.getenv("XDG_RUNTIME_DIR") or "/tmp"
    return Path(base) / "agentdiff-openclaw-proxy"


def routes_dir() -> Path:
    return runtime_dir() / "routes"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def acquire_slot() -> float:
    """Block until the shared limiter grants a slot; return seconds waited."""
    if os.getenv("PURDUE_RATE_LIMIT_DISABLE") == "1":
        return 0.0
    started = time.time()
    while True:
        wait = _reserve(time.time(), _budget(), _state_path())
        if wait <= 0:
            return time.time() - started
        time.sleep(wait)


class RunLog:
    """Numbered evidence files for one registered run."""

    _locks: dict[str, threading.Lock] = {}
    _guard = threading.Lock()

    def __init__(self, directory: Path):
        self.directory = directory
        self.directory.mkdir(parents=True, exist_ok=True)
        with RunLog._guard:
            self.lock = RunLog._locks.setdefault(str(directory), threading.Lock())

    def next_index(self) -> int:
        with self.lock:
            counter = self.directory / ".counter"
            value = int(counter.read_text()) + 1 if counter.exists() else 1
            counter.write_text(str(value))
            return value


def lookup_route(token: str) -> RunLog | None:
    path = routes_dir() / f"{token}.json"
    try:
        spec = json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return RunLog(Path(spec["log_dir"]))


def parse_stream_usage(raw: bytes) -> tuple[dict | None, str | None, bool]:
    usage, finish, done = None, None, False
    for line in raw.decode("utf-8", "replace").splitlines():
        if not line.startswith("data:"):
            continue
        payload = line[5:].strip()
        if payload == "[DONE]":
            done = True
            continue
        try:
            chunk = json.loads(payload)
        except json.JSONDecodeError:
            continue
        if chunk.get("usage"):
            usage = chunk["usage"]
        for choice in chunk.get("choices") or []:
            if choice.get("finish_reason"):
                finish = choice["finish_reason"]
    return usage, finish, done


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "agentdiff-purdue-proxy/1"
    client: httpx.Client
    api_key: str
    metadata_log: Path

    def log_message(self, fmt, *args):  # keep stdout quiet; metadata goes to files
        pass

    def do_GET(self):
        self.forward("GET")

    def do_POST(self):
        self.forward("POST")

    def forward(self, method: str) -> None:
        run_log, path = None, self.path
        match = ROUTE.match(self.path)
        if match:
            run_log = lookup_route(match.group(1))
            path = match.group(2)
            if run_log is None:
                self.send_json(404, {"error": {"message": f"unknown run route {match.group(1)}"}})
                return
        if not path.startswith("/v1/"):
            self.send_json(404, {"error": {"message": "expected /v1/..."}})
            return
        length = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(length) if length else b""
        url = UPSTREAM + path[len("/v1"):]
        meta = {"started": now_iso(), "method": method, "path": path, "attempts": []}
        index = run_log.next_index() if run_log else None
        if run_log:
            (run_log.directory / f"{index:04d}.request.json.gz").write_bytes(gzip.compress(body))
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json",
                   "Accept": self.headers.get("Accept") or "application/json"}
        started = time.time()
        for attempt in range(1, MAX_ATTEMPTS + 1):
            waited = acquire_slot()
            record = {"attempt": attempt, "limiter_wait_s": round(waited, 3), "sent": now_iso()}
            meta["attempts"].append(record)
            try:
                request = self.client.build_request(method, url, content=body or None, headers=headers)
                response = self.client.send(request, stream=True)
            except httpx.HTTPError as exc:
                record["error"] = f"{type(exc).__name__}: {exc}"
                time.sleep(min(60, 5 * 2 ** (attempt - 1)))
                continue
            record["status"] = response.status_code
            if response.status_code in RETRY_STATUSES or response.status_code == 400:
                data = response.read()
                response.close()
                detail = data.decode("utf-8", "replace")
                rate_limited = response.status_code == 429 or (
                    response.status_code == 400 and any(p in detail.lower() for p in TRANSIENT_400))
                if (response.status_code in RETRY_STATUSES or rate_limited) and attempt < MAX_ATTEMPTS:
                    record["body"] = detail[:2000]
                    record["rate_limited"] = rate_limited
                    time.sleep(min(60, (10 if rate_limited else 2) * 2 ** (attempt - 1)))
                    continue
                self.relay_bytes(response.status_code, response.headers.get("content-type", "application/json"),
                                 data, meta, run_log, index)
                break
            self.relay(response, meta, run_log, index)
            break
        else:
            self.send_json(502, {"error": {"message": "upstream unavailable after retries"}})
            meta["final_status"] = 502
        meta["ended"] = now_iso()
        meta["duration_s"] = round(time.time() - started, 3)
        self.write_meta(meta, run_log, index)

    def relay_bytes(self, status: int, content_type: str, data: bytes, meta: dict, run_log: RunLog | None,
                    index: int | None) -> None:
        """Pass through a response that was already read (a non-retryable or last-attempt error)."""
        meta["final_status"] = status
        meta["response_bytes"] = len(data)
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)
        if run_log:
            (run_log.directory / f"{index:04d}.response.json.gz").write_bytes(gzip.compress(data))

    def relay(self, response: httpx.Response, meta: dict, run_log: RunLog | None, index: int | None) -> None:
        content_type = response.headers.get("content-type", "application/json")
        meta["final_status"] = response.status_code
        captured = bytearray()
        if not content_type.startswith("text/event-stream"):
            data = response.read()
            response.close()
            captured += data
            self.send_response(response.status_code)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            if response.status_code == 200:
                try:
                    parsed = json.loads(data)
                    meta["usage"] = parsed.get("usage")
                    meta["finish_reason"] = (parsed.get("choices") or [{}])[0].get("finish_reason")
                except (json.JSONDecodeError, AttributeError):
                    pass
        else:
            self.send_response(response.status_code)
            self.send_header("Content-Type", content_type)
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Transfer-Encoding", "chunked")
            self.end_headers()
            client_gone = False
            try:
                for chunk in response.iter_raw():
                    captured += chunk
                    if not client_gone:
                        try:
                            self.wfile.write(b"%x\r\n%s\r\n" % (len(chunk), chunk))
                            self.wfile.flush()
                        except (BrokenPipeError, ConnectionResetError):
                            client_gone = True
                            meta["client_disconnected"] = True
                            break
            except httpx.HTTPError as exc:
                # Purdue closes the connection after [DONE] without ending the chunked body.
                meta["upstream_stream_error"] = f"{type(exc).__name__}: {exc}"
            finally:
                response.close()
            if not client_gone:
                try:
                    self.wfile.write(b"0\r\n\r\n")
                    self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError):
                    meta["client_disconnected"] = True
            usage, finish, done = parse_stream_usage(bytes(captured))
            meta.update(usage=usage, finish_reason=finish, done_seen=done)
            if meta.get("upstream_stream_error") and done:
                meta["upstream_stream_error_after_done"] = True
        meta["response_bytes"] = len(captured)
        if run_log:
            suffix = "sse" if content_type.startswith("text/event-stream") else "json"
            (run_log.directory / f"{index:04d}.response.{suffix}.gz").write_bytes(gzip.compress(bytes(captured)))

    def write_meta(self, meta: dict, run_log: RunLog | None, index: int | None) -> None:
        if run_log:
            (run_log.directory / f"{index:04d}.meta.json").write_text(json.dumps(meta, indent=1))
        line = {k: meta.get(k) for k in ("started", "path", "final_status", "duration_s", "usage", "finish_reason")}
        line["attempts"] = len(meta["attempts"])
        line["run_logged"] = bool(run_log)
        with open(self.metadata_log, "a") as handle:
            handle.write(json.dumps(line) + "\n")

    def send_json(self, status: int, payload: dict) -> None:
        data = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--port", type=int, default=int(os.getenv("OPENCLAW_PURDUE_PROXY_PORT", DEFAULT_PORT)))
    args = parser.parse_args()
    key = os.getenv("PURDUE_GENAI_STUDIO_API_KEY") or os.getenv("GENAI_API_KEY")
    if not key:
        sys.exit("PURDUE_GENAI_STUDIO_API_KEY (or GENAI_API_KEY) is not set")
    routes_dir().mkdir(parents=True, exist_ok=True)
    Handler.api_key = key
    Handler.client = httpx.Client(timeout=httpx.Timeout(300.0, connect=30.0), http2=False)
    Handler.metadata_log = runtime_dir() / "requests.jsonl"
    ThreadingHTTPServer.request_queue_size = 64
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    server.daemon_threads = True
    print(f"purdue proxy on http://127.0.0.1:{args.port}/v1 -> {UPSTREAM}; routes in {routes_dir()}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
