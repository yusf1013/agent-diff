// LD_PRELOAD wall-clock shift for dynamically linked harness binaries (Claude Code's Bun executable) and their
// children. SHIFT_OFFSET=<seconds> is added to the wall clock; the runner computes it once (target - now) at launch, so
// the whole process tree agrees and time keeps flowing. SHIFT_FUNCS selects what is shifted (any of clock_gettime,
// gettimeofday, time; default all three). Monotonic clocks are never shifted, so timers keep real durations.
// The interposed functions must not allocate: Bun's allocator reads the clock while it initializes, and a malloc (or
// setenv) from here deadlocks it.
#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <time.h>

static volatile long long offset_s = 0;
static volatile int ready = 0, f_cg = 1, f_gtod = 1, f_time = 1;
static int (*real_cg)(clockid_t, struct timespec *);
static int (*real_gtod)(struct timeval *, void *);
static time_t (*real_time)(time_t *);

static long long parse_ll(const char *s) {
    long long v = 0; int neg = 0;
    if (*s == '-') { neg = 1; s++; }
    while (*s >= '0' && *s <= '9') v = v * 10 + (*s++ - '0');
    return neg ? -v : v;
}

static int has(const char *list, const char *name) {
    size_t n = strlen(name);
    for (const char *p = list; (p = strstr(p, name)) != NULL; p += n)
        if ((p == list || p[-1] == ',') && (p[n] == ',' || p[n] == '\0')) return 1;
    return 0;
}

static void init(void) {
    if (ready) return;
    real_cg = dlsym(RTLD_NEXT, "clock_gettime");
    real_gtod = dlsym(RTLD_NEXT, "gettimeofday");
    real_time = dlsym(RTLD_NEXT, "time");
    const char *funcs = getenv("SHIFT_FUNCS");
    if (funcs) { f_cg = has(funcs, "clock_gettime"); f_gtod = has(funcs, "gettimeofday"); f_time = has(funcs, "time"); }
    const char *off = getenv("SHIFT_OFFSET");
    offset_s = off ? parse_ll(off) : 0;
    ready = 1;
}

int clock_gettime(clockid_t id, struct timespec *ts) {
    init();
    int rc = real_cg(id, ts);
    if (rc == 0 && f_cg && (id == CLOCK_REALTIME || id == CLOCK_REALTIME_COARSE)) ts->tv_sec += offset_s;
    return rc;
}

int gettimeofday(struct timeval *tv, void *tz) {
    init();
    int rc = real_gtod(tv, tz);
    if (rc == 0 && f_gtod && tv) tv->tv_sec += offset_s;
    return rc;
}

time_t time(time_t *t) {
    init();
    time_t now = real_time(NULL);
    if (f_time) now += offset_s;
    if (t) *t = now;
    return now;
}
