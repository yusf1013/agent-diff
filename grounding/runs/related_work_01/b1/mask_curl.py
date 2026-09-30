#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys
from urllib.parse import parse_qs, urlsplit

RULES = __RULES__
BASE = __BASE__

VALUED = set("XdoHwFDuAebcKTmrEy")
LONG_VALUED = {"--request", "--data", "--data-raw", "--data-binary", "--data-urlencode", "--data-ascii", "--json",
               "--form", "--output", "--header", "--write-out", "--dump-header", "--user", "--user-agent", "--url",
               "--max-time", "--connect-timeout", "--retry", "--cookie", "--referer", "--config"}
DATA = {"-d", "--data", "--data-raw", "--data-binary", "--data-urlencode", "--data-ascii", "--json", "-F", "--form"}


def parse(argv):
    opts, urls, i = [], [], 0
    while i < len(argv):
        a = argv[i]
        if a.startswith("--"):
            name, eq, val = a.partition("=")
            if name in LONG_VALUED:
                if not eq:
                    i += 1
                    val = argv[i] if i < len(argv) else ""
                opts.append((name, val))
                if name == "--url":
                    urls.append(val)
            else:
                opts.append((name, None))
        elif a.startswith("-") and len(a) > 1:
            j = 1
            while j < len(a):
                c = a[j]
                if c in VALUED:
                    val = a[j + 1:]
                    if not val:
                        i += 1
                        val = argv[i] if i < len(argv) else ""
                    opts.append(("-" + c, val))
                    break
                opts.append(("-" + c, None))
                j += 1
        elif re.match(r"https?://", a):
            urls.append(a)
        i += 1
    return opts, urls


def body_of(opts, stdin):
    parts = []
    for name, val in opts:
        if name in DATA and val is not None:
            if val.startswith("@"):
                src = val[1:]
                if src == "-":
                    parts.append(stdin.decode("utf-8", "replace"))
                else:
                    try:
                        with open(os.path.expanduser(src), encoding="utf-8", errors="replace") as fh:
                            parts.append(fh.read())
                    except OSError:
                        pass
            else:
                parts.append(val)
    return "&".join(parts)


def method_of(opts):
    for name, val in opts:
        if name in ("-X", "--request") and val:
            return val.upper()
    if any(n in ("-G", "--get") for n, _ in opts):
        return "GET"
    return "POST" if any(n in DATA for n, _ in opts) else "GET"


def graphql_fields(text):
    docs = []
    try:
        payload = json.loads(text)
        for p in payload if isinstance(payload, list) else [payload]:
            if isinstance(p, dict) and isinstance(p.get("query"), str):
                docs.append(p["query"])
    except ValueError:
        docs.append(text)
    names = set()
    for d in docs:
        if "mutation" in d:
            names |= set(re.findall(r"\b([A-Za-z_]\w*)\s*\(", d))
    return names, docs


def refusal(url, method, body):
    u = urlsplit(url)
    host, path = u.netloc.lower(), u.path
    for rule in RULES:
        svc = rule[0]
        if svc == "slack" and host in ("slack.com", "api.slack.com") and path.rstrip("/") == "/api/" + rule[1]:
            return 200, {"ok": False, "error": "unknown_method", "req_method": rule[1]}
        if svc == "linear" and host == "api.linear.app":
            text = body or "".join(parse_qs(u.query).get("query", []))
            names, _ = graphql_fields(text)
            if rule[1] in names:
                return 400, {"errors": [{"message": f'Cannot query field "{rule[1]}" on type "Mutation".',
                                         "extensions": {"code": "GRAPHQL_VALIDATION_FAILED"}}]}
        if svc == "box" and host in ("api.box.com", "upload.box.com"):
            sub = re.sub(r"^(/api)?/2\.0", "", path)
            if method in rule[1] and re.match(rule[2], sub):
                return 405, {"type": "error", "status": 405, "code": "method_not_allowed",
                             "message": "Method Not Allowed"}
        if svc == "calendar" and host == "www.googleapis.com" and path.startswith("/calendar/v3"):
            sub = path[len("/calendar/v3"):]
            if method in rule[1] and re.match(rule[2], sub):
                return 404, {"error": {"errors": [{"domain": "global", "reason": "notFound", "message": "Not Found"}],
                                       "code": 404, "message": "Not Found"}}
    return None


def emit(status, payload, opts):
    names = {n for n, _ in opts}
    silent = ("-s" in names or "--silent" in names) and not ("-S" in names or "--show-error" in names)
    if status >= 400 and ({"-f", "--fail"} & names):
        if not silent:
            sys.stderr.write(f"curl: (22) The requested URL returned error: {status}\n")
        return 22
    text = json.dumps(payload)
    head = f"HTTP/2 {status} \r\ncontent-type: application/json\r\n\r\n"
    out = dict(opts)
    target = out.get("-o") or out.get("--output")
    for name, val in opts:
        if name in ("-D", "--dump-header") and val:
            if val == "-":
                sys.stdout.write(head)
            else:
                with open(os.path.expanduser(val), "w") as fh:
                    fh.write(head)
    if {"-i", "--include"} & names:
        text = head + text
    if target and target != "-":
        with open(os.path.expanduser(target), "w") as fh:
            fh.write(text)
    else:
        sys.stdout.write(text)
    fmt = out.get("-w") or out.get("--write-out")
    if fmt:
        fmt = fmt.replace("%{http_code}", str(status)).replace("%{response_code}", str(status))
        sys.stdout.write(fmt.replace("\\n", "\n").replace("\\t", "\t"))
    sys.stdout.flush()
    return 0


def strip_fields(node, gone):
    if isinstance(node, dict):
        if isinstance(node.get("fields"), list):
            node["fields"] = [f for f in node["fields"] if not (isinstance(f, dict) and f.get("name") in gone)]
        for v in node.values():
            strip_fields(v, gone)
    elif isinstance(node, list):
        for v in node:
            strip_fields(v, gone)


def main(argv):
    opts, urls = parse(argv)
    needs_stdin = any(n in DATA and (v or "") == "@-" for n, v in opts)
    stdin = sys.stdin.buffer.read() if needs_stdin else b""
    body = body_of(opts, stdin)
    method = method_of(opts)
    for url in urls:
        hit = refusal(url, method, body)
        if hit:
            return emit(hit[0], hit[1], opts)
    gone = {r[1] for r in RULES if r[0] == "linear"}
    introspect = gone and any("api.linear.app" in u for u in urls) and ("__schema" in body or "__type" in body)
    if not needs_stdin and not introspect:
        os.execv(BASE, [BASE] + argv)
    done = subprocess.run([BASE] + argv, input=stdin, capture_output=True)
    out = done.stdout
    if introspect:
        try:
            data = json.loads(out)
            strip_fields(data, gone)
            out = json.dumps(data).encode()
        except ValueError:
            pass
    sys.stdout.buffer.write(out)
    sys.stderr.buffer.write(done.stderr)
    return done.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
