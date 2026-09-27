// Shift Node's wall clock so OpenClaw reports AGENTDIFF_FAKE_NOW (ISO 8601) as the time at process start.
// Loaded with NODE_OPTIONS="--require <this file>" for Calendar runs only. It replaces the global Date
// with one offset by a constant, so elapsed times, timers (monotonic clock) and TLS certificate checks
// (OpenSSL's own clock) are unaffected. Processes that are not Node (bash, date, curl) keep the real
// clock; the runner scans Calendar trajectories for such time sources.
"use strict";
const target = Date.parse(process.env.AGENTDIFF_FAKE_NOW || "");
if (!Number.isNaN(target) && !globalThis.__agentdiffFakeClock) {
  const RealDate = Date;
  const offset = target - RealDate.now();
  function FakeDate(...args) {
    if (!new.target) return new RealDate(RealDate.now() + offset).toString();
    return args.length ? new RealDate(...args) : new RealDate(RealDate.now() + offset);
  }
  FakeDate.prototype = RealDate.prototype;
  FakeDate.now = () => RealDate.now() + offset;
  FakeDate.parse = RealDate.parse;
  FakeDate.UTC = RealDate.UTC;
  Object.defineProperty(FakeDate, "name", { value: "Date" });
  Object.setPrototypeOf(FakeDate, RealDate);
  globalThis.Date = FakeDate;
  globalThis.__agentdiffFakeClock = { target, offset };
}
