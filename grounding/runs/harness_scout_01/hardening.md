# Hardening the attempt: options for the next round

*harness_scout_01, 2026-09-30, a desk study for the lead (no runs). Line numbers are at commit `cde6317112`.*

**Recommendation in one line:** run each attempt in a bubblewrap sandbox with a minimal filesystem and an empty
network namespace, bridged to exactly two host-side proxies (the model proxy and a new per-attempt replica proxy),
and move every rule the agent must not get around (environment scoping, B1's masks, logging) out of the sandbox into
those proxies. Do not rely on a separate Unix user, or on a token the shim injects.

## What the scans found, and why it is possible

**The findings.**
- **The main rounds** ([sol_eval_01/eval/host_access_scan.json](../sol_eval_01/eval/host_access_scan.json)): trials
  with at least one hit.

  | Round | Qwen on OpenClaw | Sol on OpenClaw |
  |---|---|---|
  | full_02 | 2 of 1,314 | |
  | full_03 | 3 of 999 | |
  | full_04 | 2 of 408 | |
  | Policy stage | 6 of 1,743 | |
  | All four Sol rounds | | 0 of 1,196 |

  The hits: calls to the replica at `127.0.0.1:18001` past the curl shim, some of them writes; host probing (`env`,
  `ss -tlnp`, `ps aux`, `/etc/hosts`); reading the attempt's OpenClaw state; and a `grep` of the repository, where
  the answer keys are. The lead judged the main rounds clean.
- **B1** ([related_work_01/b1](../related_work_01/b1/README.md)) puts its masks in a curl wrapper on the agent's PATH
  (`install.py:69-75`, `mask_curl.py`). Its README notes that the agent can read that wrapper. A mask the agent can
  read, or go around with a direct call, is not a boundary.

**Why it is possible:**
1. **The attempt runs as the user, unsandboxed.**
   - OpenClaw: `run_turn` starts it with `subprocess.Popen(cmd, cwd=workspace, env=env, ..., start_new_session=True)`
     (`integrations/openclaw/runtime.py:282`). Its exec tool runs bash with the user's rights.
   - Claude Code: `run_process` (`claudecode_pilot_01/backend.py:169-173`), with Bash and
     `--permission-mode bypassPermissions` (`command`, 162).
2. **The agent sees the real home.** `process_env` sets `HOME` to it and puts `~/.npm-global/bin` on `PATH`
   (`runtime.py:237-238`; `backend.py:141-159`). The repository `/home/yusf/PyProj/agent-diff` is readable by that
   user.
3. **The agent is told where the replica is.**
   - `process_env` puts `SVC_BASE_URL` and `SVC_ENV_ID` in the environment (`runtime.py:239-240`; the neutral names
     at 90-92).
   - The shim is a readable bash script that spells out the pattern `<base>/api/env/<id>/services/<service>`
     (`integrations/openclaw/bin/curl`).
   - The Claude Code backend writes the URL and the environment id into its copy of the shim (`curl_shim`,
     `backend.py:112-129`).
4. **The replica answers any local process.** The backend on 18001 runs with `ENVIRONMENT=development`, so
   `is_dev_mode()` is true (`backend/src/platform/api/auth.py:23`). Neither middleware asks for a key
   (`middleware.py:36`, `116`), and `get_principal_id` returns "dev-user" (`auth.py:90`). Every route answers,
   including the platform API (environments, templates, test suites).
5. **The model proxy forwards unrecorded traffic.** `purdue_proxy.py` records `/run/<token>/v1/...` (`ROUTE`, 52),
   but `forward` also relays plain `/v1/...` (147-157). A model call outside the record is possible.

## Option A: a separate Unix user

The attempt runs as an account (say `solver`) that cannot read `/home/yusf`, through a `sudo -u solver` rule.

- **What it stops:**
  - reading the repository and the rest of the home directory (`/home/yusf` is `drwxr-x---`);
  - reading other attempts' state, once each attempt's directory is group-shared with the runner.
- **What it does not stop:**
  - **The network.** Loopback is shared, so `127.0.0.1:18001` (the replica, in dev mode) and the model proxy stay
    reachable. Stopping that needs root-level firewalling (an `iptables` owner match on the solver's uid).
  - **The process table.** `ps` and `ss` still show the host.
- **Build:**
  - Admin work by the PI, since sudo needs a password here: create the account; add a `NOPASSWD` sudoers rule for
    the two launchers; add the firewall rules.
  - Make node and OpenClaw readable by `solver`. Both live under `/home/yusf` (`~/.nvm`, `~/.npm-global`), so this
    needs ACLs on those trees or a system-wide install.
  - About half a day, most of it the PI's. It is a root change to a shared machine: `getent passwd` lists two other
    users.
- **Per run:** a `sudo` hop (milliseconds). Attempt folders become written by two users (group permissions), and
  the runner must read what `solver` wrote.
- **OpenClaw:** `run_turn`'s command gets the `sudo -u solver` prefix. The state directory must be group-writable,
  and `OPENCLAW_STATE_DIR` stays as is.
- **Claude Code:** the same prefix around `run_process`. The config and work directories must be group-shared, and
  the clock `.so` under `~/.cache/harness-clock` readable by `solver`.
- **Evidence:** no change to what is recorded; ownership of the files changes.

## Option B: a sandbox with a minimal filesystem

The attempt runs inside bubblewrap (or a container) that sees only what it needs. The kit already builds such a
sandbox for Muse (`autogen_01/kit/agent.py:219`, `_sandbox`), so the pattern is proven on this machine.

**What it sees.** Unprivileged user namespaces are enabled here (bubblewrap 0.6.1, Ubuntu 22.04). The mounts:
- `/usr` and `/etc` read-only; `/tmp` as a tmpfs; its own `/proc` and `/dev`;
- the node install and `~/.npm-global`, read-only;
- the attempt's state (or run) directory, read-write, bound at a neutral path such as
  `/home/assistant/.openclaw-state/<id>`;
- a private `HOME`; `--unshare-all --die-with-parent --new-session --clearenv` with an explicit environment.

**Measured without a model:** `openclaw --version` (2026.7.1-2) starts in exactly this sandbox (no home, the network
unshared) in 25 ms, against 24 ms outside.

- **What it stops:**
  - reading the repository, the home directory, other attempts and `~/.openclaw`;
  - seeing the host's processes (its own PID namespace).
- **What it does not stop on its own:** the network. With `--share-net`, loopback, and so the replica, stays
  reachable. That is option C.
- **Build:** about half a day. The mount lists for both harnesses; neutral in-sandbox paths; model-free checks (the
  repository unreadable, OpenClaw reading its skills, the leak guard passing).
- **Per run:** about 1 ms (measured above).
- **OpenClaw:**
  - `run_turn` (`runtime.py:282`) prefixes the command with the bwrap argument list.
  - `process_env` (233-248) sets the sandbox's `HOME`, a `PATH` inside the mounts, and `OPENCLAW_STATE_DIR` at the
    neutral path.
  - The state directory is built on the host exactly as now (`build_state_dir`, 160-224), and its shim, fake clock
    and skills are inside it.
  - The kill at the time limit (`killpg`, 330 and 334) is unchanged: `--die-with-parent` takes the sandbox down.
- **Claude Code:**
  - `run_process` (`backend.py:169-173`) gets the same prefix.
  - Mounts: the `claude` binary (a Bun executable under the node install, dynamically linked, so the sandbox needs the `/lib64` loader link that `_sandbox` already has), the run's
    `CLAUDE_CONFIG_DIR` and work directory read-write, and the clock `.so` read-only.
  - `--permission-mode bypassPermissions` can stay, since the sandbox is the boundary.
- **The container variant:**
  - an image with node, OpenClaw, claude, curl and python, run with `docker run --network none`;
  - about a day plus the image's upkeep, and about a second per start;
  - the docker group is root-equivalent (this user is in it);
  - the same guarantee as bubblewrap for more machinery, so it is not recommended.

## Option C: a network namespace in which only the proxies are reachable

The sandbox gets an empty network namespace (`--unshare-net`: its own loopback, nothing else) and exactly two ways
out: the model proxy and a per-attempt replica proxy.

**The bridge.** Nothing ready-made is installed here: no slirp4netns, pasta or socat.
- **Inside the sandbox:** a small forwarder (about 60 lines of Node; node is already in the mounts), started before
  OpenClaw. It listens on `127.0.0.1:<model port>` and `127.0.0.1:<replica port>`, and forwards each connection to a
  Unix socket in a per-attempt directory the runner bind-mounts. Mount the directory, not the socket file, so the
  listeners can start on either side of bwrap.
- **Host side, the model proxy:** `purdue_proxy.py` gets a Unix-socket listener. It is a `ThreadingHTTPServer`, so
  this is a small subclass with `address_family = AF_UNIX`.
- **Host side, the replica proxy (new, about 150 lines):**
  - forwards only `/api/env/<this environment>/services/<this service>/...` to 18001 and refuses everything else
    (other environments, the platform API);
  - applies the item's masks (B1's rules move from `state/bin/curl` into the proxy);
  - logs every request and every refusal in the attempt folder.

**What it stops:** calls to the replica other than the attempt's own service routes, the platform API, other
environments, port scans, and unrecorded model calls (the bridge reaches only the recorded route). A real hostname
without the shim fails to resolve, which leaves visible evidence of the attempt.

**Build and cost:**
- About a day: the forwarder, the Unix listener, the replica proxy with scoping, masks and log, the shim change, and
  model-free checks.
- Per run: the forwarder's start (an estimate: under 100 ms) and one local hop per request (an estimate: under 1 ms).

**OpenClaw changes:**
- The provider `baseUrl` (`build_state_dir`, `runtime.py:207`) points at the forwarder. The route token can be added
  on the host side of the bridge, since the socket is already per attempt.
- `SVC_BASE_URL` (239) becomes the forwarder's replica port. The environment id need not enter the sandbox at all:
  the replica proxy knows it, and the shim rewrites to `<base>/<service>/...`.
- **The openai backend (Sol) is the gap.** OpenClaw talks to OpenAI directly (`BACKENDS["openai"]`, port `None`,
  `runtime.py:66-76`), so it would need an egress allowlist proxy through the bridge, and OpenClaw would have to
  honour a proxy setting. That is unverified. Until then that backend gets option B only, and with a shared network
  the replica stays reachable. Sol made no such call in its rounds.

**Claude Code changes:**
- With the self-hosted Qwen, `ANTHROPIC_BASE_URL` points at the bridge. The window relay of
  `qwen_writer_01/backend.py` can sit on the host side of it.
- With Sonnet on the plan, it needs `api.anthropic.com`. Claude Code honours `HTTPS_PROXY`, so an allowlist CONNECT
  proxy through the bridge serves; TLS stays end to end.

**The per-run token the shim injects does not do what it is meant to.**
- The shim runs with the agent's rights and is a script on its PATH; B1's README notes the agent can read it. A token
  the shim injects is a token the agent can read and reuse in a direct call.
- What a token buys is separation between runs on one shared proxy. What makes a direct call harmless is enforcement
  in the proxy: forward only the attempt's own routes, apply the masks there, log everything.
- With a per-attempt Unix socket bound into the sandbox, the socket is the capability and a token adds nothing. The
  shim should keep only its URL rewriting: no secret, no rule.

## Comparison

| | A: separate user | B: filesystem sandbox | C: B plus the network namespace |
|---|---|---|---|
| Stops repository and home reads | yes | yes | yes |
| Stops direct replica calls (and the platform API) | no (only with root firewalling) | no | yes |
| Stops host probing (processes, ports) | partly | processes, files | yes |
| Makes B1's masks unbypassable | no | no | yes (masks in the proxy) |
| Needs the PI's sudo | yes | no | no |
| Build | half a day, mostly admin | half a day | a further day |
| Per run | milliseconds (sudo) | about 1 ms (measured) | under 100 ms (estimated) |
| OpenClaw change | command prefix, shared folders | command prefix, env, mounts | plus baseUrl, `SVC_BASE_URL`, bridge |
| Claude Code change | command prefix, shared folders | command prefix, mounts | plus base URL or egress proxy |
| Evidence | file ownership | none lost (the state dir is bind-mounted) | plus the replica proxy's log |

## Recommendation

**B and C together, with bubblewrap, for the self-hosted backends first** (OpenClaw with Qwen, Claude Code with
Qwen). Enforcement lives outside the sandbox.

1. **Build and check without a model.** From inside the sandbox:
   - the repository and home are unreadable;
   - `curl 127.0.0.1:18001` fails;
   - the replica proxy refuses another environment's routes, the platform API and a masked operation;
   - OpenClaw starts and reads its skills;
   - the leak guard passes with the new paths.
2. **A 20-test A/B at the lead's word** (runs): the same tests at 3 trials, sandboxed against the current setup, to
   check that failure rates and the judge's verdicts do not move beyond noise. An empty home and a dead network
   change what a probing agent sees.
3. **Then the round.**

**Now, cheaply:**
- During rounds, make the model proxy refuse unrouted `/v1/...` (`forward`, `purdue_proxy.py:156`, one condition).
- Keep `host_access_scan` as a post-run guard, with a "blocked" category so that failed probes are counted after
  the change.

**Not A:** it needs root on a shared machine and still leaves the network open. **Not the container:** the same
guarantee as bubblewrap for more machinery.

## What changes in the code

| Where | Now | Change |
|---|---|---|
| `integrations/openclaw/runtime.py:275-282` `run_turn` | `Popen(cmd, cwd=workspace, env=env, start_new_session=True)` | prefix `cmd` with the bwrap list (mounts, `--unshare-all`, `--die-with-parent`); start the forwarder first (C) |
| `runtime.py:233-248` `process_env` | real `HOME`, `PATH` with `~/.npm-global/bin`, `SVC_BASE_URL`, `SVC_ENV_ID` | sandbox `HOME` and `PATH`; `SVC_BASE_URL` = the forwarder (C); no `SVC_ENV_ID` (C) |
| `runtime.py:160-224` `build_state_dir` | provider `baseUrl` `127.0.0.1:<port>/run/<route>/v1` (207); `pathPrepend` (210); shim copy (181) | `baseUrl` to the forwarder (C); the shim rewrites to `<base>/<service>` (C) |
| `runtime.py:666-848` `run_attempt` | state path (688); `init_env` (693); cleanup in `finally` (825) | the per-attempt socket directory and replica proxy start and stop here; cleanup unchanged (`qwen_writer_01/cleanup_cut_off.py` remains the pattern for killed attempts) |
| `runtime.py:258`, `578`, `94` (`prompt_leaks`, `transcript_leaks`, `LEAK_TOKENS`) | check the host paths | recheck with the in-sandbox paths (OpenClaw writes the state path into every system prompt, 81-88) |
| `integrations/openclaw/bin/curl` | rewrites to `<base>/api/env/<id>/services/<service>` | rewrites to `<base>/<service>`; no rule, no secret |
| `integrations/openclaw/purdue_proxy.py:52`, `147-157` | TCP only; relays unrouted `/v1` | a Unix listener; refuse unrouted `/v1` in rounds |
| new: the replica proxy | (the shim and B1's wrapper hold the rules) | path scoping to the attempt's routes, B1's masks, a per-request log |
| `claudecode_pilot_01/backend.py:112-129` `curl_shim`, `131-139` `build_run_dir`, `141-159` `process_env`, `169-173` `run_process` | shim with the URL and id written in; real `HOME`; unsandboxed `Popen` | as for OpenClaw; mount the clock `.so` read-only |
| `related_work_01/b1/install.py:69-75`, `mask_curl.py` | the mask replaces `state/bin/curl` | the same rules handed to the replica proxy |
| `openclaw_eval_01/run.py:118` `write_plan` | records code hashes and settings | also records the sandbox spec: mounts, namespaces, bridge ports |

## What it does to the evidence

- **New:** the replica proxy's log, an authoritative record of every replica call and every refusal. Today these are
  inferred from the transcript and the database diff; B1's oracle would get a cleaner input.
- **Unchanged:**
  - the session transcripts: the state directory is bind-mounted, the same files in the same place;
  - the model proxy's recordings by route;
  - `execution_summary.json` and the state diff.
  bubblewrap keeps the caller's uid, so the attempt folders' ownership does not change (unlike option A).
- **Changed:**
  - the paths the agent sees, and so the system prompt; the leak guard is rechecked;
  - `host_access_scan` becomes a check that should find no successful bypass, with blocked probes counted as such.
- **Behaviour:** a probing agent now meets errors (a missing file, a refused connection, an unresolvable host) where
  it met answers. The A/B in the recommendation measures whether that moves results.

## Open items

- **The openai backend:** egress to OpenAI needs an allowlist proxy that OpenClaw honours. That is unverified; until
  then, option B only.
- **Claude Code's credential in the shell's environment.** `auth_env` (`backend.py:72-87`) puts
  `CLAUDE_CODE_OAUTH_TOKEN` in the process environment, and the Bash tool inherits it unless Claude Code scrubs it.
  Whether it does is unverified. Checking needs a model turn (one trial running `env | grep -c OAUTH`), so it is the
  first check of the next pilot. The sandbox does not fix this. A credential-injecting egress proxy would, and it
  raises the terms question this study reported ([report.md](report.md)). For the PI.
- **Whether an OpenClaw agent turn touches anything under `HOME` beyond its state directory.** The `--version`
  check does not show it; it is a stage-1 check.

## Out of scope, for the PI

**The dev-mode replica on a shared machine.** The backend on 18001 answers any local process without a key
(`auth.py:23`, `90`; `middleware.py:36`, `116`), and this machine has other user accounts. Sandboxing protects a
round against its own solver; it does not close the backend to other users. Production mode validates keys against a
control plane (`auth.py:101`, `validate_with_control_plane`), which is not a local option. Binding the backend to a
Unix socket, or firewalling it, would be.
