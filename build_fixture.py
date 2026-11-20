"""Build the test workspaces: workspace-folder/ (ICM layout) and workspace-mono/ (one big CLAUDE.md).

The monolith is assembled from the folder's own files, so the rules text is identical in both.
Also writes truth.json, the ground truth score.py checks against.
Run: python3 build_fixture.py
"""
import hashlib, json, shutil
import extras
from pathlib import Path

HERE = Path(__file__).parent
FOLDER, MONO, MONO_BIG = HERE / "workspace-folder", HERE / "workspace-mono", HERE / "workspace-mono-big"
RELEASE, DATE = "2.4.0", "2026-11-02"
MAINTAINERS = ["lena-ortiz", "sam-okafor"]

# number, kind/labels, title, author, state, milestone, body
ISSUES = [
    (401, ["bug"], "Worker hangs on SIGTERM while a job is running", "hollis", "closed", "2.4.0", "Sending SIGTERM to a busy Worker never exits; the job finishes but the process stays up."),
    (403, ["bug"], "schedule() ignores the tz argument", "sam-okafor", "closed", "2.4.0", "schedule(at=..., tz='Europe/Berlin') runs the job at UTC time."),
    (405, ["feature"], "Add Queue.drain() to wait until all jobs finish", "tobiaslund", "closed", "2.4.0", "Useful in tests and graceful shutdowns."),
    (407, ["bug"], "Memory leak in the result cache", "ana-p", "closed", "2.4.0", "Results are kept forever when result_ttl is unset. Fix landed in two commits (one cherry-picked)."),
    (409, ["feature"], "retry_backoff option on Worker", "lena-ortiz", "closed", "2.4.0", "Exponential backoff between retries, off by default."),
    (411, ["bug"], "Job.retries is off by one", "sam-okafor", "closed", "2.4.0", "A job with retries=3 runs four times."),
    (412, ["breaking"], "Drop support for Python 3.9", "lena-ortiz", "closed", "2.4.0", "Python 3.9 is end of life. Minimum is now Python 3.10."),
    (414, ["bug"], "RedisBackend does not release the connection after a timeout", "rvdb", "closed", "2.4.0", "Pool exhaustion after many timeouts."),
    (415, ["feature"], "Prometheus metrics endpoint", "ana-p", "closed", "2.4.0", "New metrics_server() helper serves queue depth, job durations and failures."),
    (416, ["feature"], "Add Queue.peek_many()", "dkowal", "closed", "2.4.0", "Look at the next n jobs without taking them."),
    (418, ["breaking"], "Rename Queue.put_nowait() to Queue.try_put()", "lena-ortiz", "closed", "2.4.0", "put_nowait() suggested asyncio semantics it never had. try_put() returns False when full instead of blocking."),
    (419, ["feature"], "Queue.stats() dashboard", "sam-okafor", "open", "2.4.0", "Work in progress behind a flag."),
    (420, ["deprecation"], "Deprecate Queue.size in favour of len(queue)", "sam-okafor", "closed", "2.4.0", "Queue.size still works and warns; removal planned for 3.0."),
    (422, ["feature"], "Job.cancel() for queued jobs", "lena-ortiz", "closed", "2.4.0", "Cancels a job that has not started yet."),
    (426, ["internal"], "Refactor the backend registry", "lena-ortiz", "closed", "2.4.0", "No user-facing change."),
    (427, ["feature"], "Redis Sentinel support in RedisBackend", "dkowal", "closed", "2.4.0", "Pass sentinels=[...] to connect through Redis Sentinel."),
    (429, ["bug"], "Queue.try_put() raises ValueError instead of QueueFull", "rvdb", "closed", "2.4.0", "Introduced by #418, which has not been released yet."),
    (431, ["security", "bug"], "Pickle payloads deserialized without an allow-list (CVE-0000-00000)", "mira-k", "closed", "2.4.0", "A crafted job payload could run code on the worker. Fixed by the new serializer_allowlist option, on by default."),
    (433, ["docs"], "Fix typo in README", "hollis", "closed", "2.4.0", "'recieve' -> 'receive'."),
    (435, ["ci"], "Move CI to ubuntu-24.04", "sam-okafor", "closed", "2.4.0", "Runner image update."),
    (438, ["bug"], "Worker logs every poll at DEBUG", "rvdb", "closed", "2.5.0", "Too noisy. The fix is merged to main and scheduled for 2.5.0."),
    (440, ["feature"], "Async Queue API", "ana-p", "open", "2.5.0", "Design discussion."),
]

SECTION_OF = {"breaking": "Breaking changes", "security": "Security", "feature": "Added", "deprecation": "Deprecated", "bug": "Fixed"}
SHIPPED = {401, 403, 405, 407, 409, 411, 412, 414, 415, 418, 420, 422, 427, 431}
TRAPS = {416: "reverted", 429: "fixes an unreleased bug", 426: "internal", 433: "docs", 435: "ci", 419: "open", 438: "milestone 2.5.0"}

# date, git author, message
COMMITS = [
    ("2026-10-01", "Lena Ortiz", "Start 2.4.0 development"),
    ("2026-10-02", "Sam Okafor", "ci: move runners to ubuntu-24.04 (#435)"),
    ("2026-10-02", "Lena Ortiz", "Drop Python 3.9 from classifiers and CI matrix (#412)"),
    ("2026-10-03", "Hollis Grant", "worker: exit cleanly on SIGTERM while a job runs (#401)"),
    ("2026-10-04", "Sam Okafor", "chore: bump dev dependencies"),
    ("2026-10-05", "Sam Okafor", "schedule: respect tz argument (#403)"),
    ("2026-10-06", "Tobias Lund", "queue: add drain() (#405)"),
    ("2026-10-06", "Tobias Lund", "tests for drain() (#405)"),
    ("2026-10-07", "Ana Pereira", "cache: evict results when result_ttl is unset (#407)"),
    ("2026-10-08", "Lena Ortiz", "worker: retry_backoff option (#409)"),
    ("2026-10-09", "Sam Okafor", "job: fix retries off-by-one (#411)"),
    ("2026-10-09", "Lena Ortiz", "Merge branch 'fix/retries'"),
    ("2026-10-10", "Lena Ortiz", "Refactor backend registry (#426)"),
    ("2026-10-11", "Ruben van den Berg", "redis: release connection after timeout (#414)"),
    ("2026-10-12", "Ana Pereira", "metrics: add metrics_server() (#415)"),
    ("2026-10-13", "Dawid Kowalski", "queue: add peek_many() (#416)"),
    ("2026-10-14", "Lena Ortiz", "queue: rename put_nowait() to try_put() (#418)"),
    ("2026-10-15", "Sam Okafor", "WIP: stats dashboard behind TQ_STATS flag (#419)"),
    ("2026-10-16", "Sam Okafor", "queue: deprecate size property (#420)"),
    ("2026-10-17", "Lena Ortiz", "job: add cancel() (#422)"),
    ("2026-10-18", "Dawid Kowalski", "Revert \"queue: add peek_many() (#416)\" - breaks fairness guarantees"),
    ("2026-10-19", "Dawid Kowalski", "redis: Sentinel support (#427)"),
    ("2026-10-20", "Ruben van den Berg", "queue: try_put() raises QueueFull, not ValueError (#429)"),
    ("2026-10-21", "Hollis Grant", "docs: fix typo in README (#433)"),
    ("2026-10-22", "Ana Pereira", "cache: evict results when result_ttl is unset (#407) (cherry picked from commit 7d1c0e2)"),
    ("2026-10-23", "Ruben van den Berg", "worker: quieter DEBUG logging (#438)"),
    ("2026-10-24", "Mira Kaur", "security: serializer_allowlist, on by default (#431)"),
    ("2026-10-25", "Lena Ortiz", "docs: document serializer_allowlist (#431)"),
    ("2026-10-26", "Sam Okafor", "chore: typing fixes"),
    ("2026-10-27", "Lena Ortiz", "Merge branch 'release/2.4.0'"),
    ("2026-10-28", "Sam Okafor", "ci: cache pip downloads"),
    ("2026-10-29", "Lena Ortiz", "Update copyright year"),
    ("2026-10-30", "Lena Ortiz", "Bump version to 2.4.0"),
]

API_NAMES = ["Queue", "Queue.put()", "Queue.try_put()", "Queue.put_nowait()", "Queue.get()", "Queue.drain()",
             "Queue.size", "len(queue)", "QueueFull", "Worker", "retry_backoff", "Job", "Job.cancel()",
             "Job.retries", "schedule()", "RedisBackend", "metrics_server()", "serializer_allowlist",
             "result_ttl", "SIGTERM", "tq stats"]

CLAUDE_MD = """# tinyqueue release workspace

This workspace prepares the release notes for tinyqueue, a Python job-queue library.
Raw inputs are in `inputs/` (git log and issue export). Never edit them.

- Start at `CONTEXT.md`: it says which stage handles a request.
- Each stage lives in `stages/<NN>_<name>/` and has its own `CONTEXT.md` (the stage contract).
- Read only the files a stage's contract lists. Write only to that stage's `output/`.
"""

ROUTING_MD = """# Routing

| Request | Stage |
|---|---|
| "Prepare the release notes" | run 01, then 02, then 03, in order |
| "Run stage 01" (or 02, 03) | only that stage |

Stages:
1. `stages/01_extract/`: decide which changes ship and in which section.
2. `stages/02_draft/`: write one bullet per change.
3. `stages/03_publish/`: format the changelog entry and `release.json`.

Shared: `_config/release.md` (version and date), `_config/voice.md` (tone).

Other jobs in this repo, each in `workflows/<name>/CONTEXT.md` (not used for release notes): support replies, docs site, social announcements, on-call.
"""

STAGE_01 = """# Stage 01: extract

## Inputs
- Layer 4 (working): `../../inputs/git-log.txt`, `../../inputs/issues.json`
- Layer 3 (reference): `references/inclusion-rules.md`
- Layer 3 (reference): `../../_config/release.md`

## Process
Go through every issue referenced in the git log and decide, with the inclusion rules, whether it ships in this release and in which section.

## Outputs
- `output/changes.md`: one line per shipped change: `<section> | #<number> | <issue title> | <issue author>`
"""

STAGE_02 = """# Stage 02: draft

## Inputs
- Layer 4 (working): `../01_extract/output/changes.md`, `../../inputs/issues.json` (for detail only)
- Layer 3 (reference): `references/style-guide.md`, `references/api-reference.md`
- Layer 3 (reference): `../../_config/voice.md`

## Process
Write one bullet per change, following the style guide exactly. Do not add or drop changes.

## Outputs
- `output/bullets.md`: the bullets grouped under their section headings
"""

STAGE_03 = """# Stage 03: publish

## Inputs
- Layer 4 (working): `../02_draft/output/bullets.md`
- Layer 3 (reference): `references/format.md`, `references/changelog-history.md`
- Layer 3 (reference): `../../_config/release.md`

## Process
Assemble the changelog entry and the JSON summary, following the format rules. Check that the counts match.

## Outputs
- `output/CHANGELOG-2.4.0.md`
- `output/release.json`
"""

INCLUSION = f"""# Inclusion rules

1. Only issues in milestone `{RELEASE}` with state `closed` ship.
2. Leave out issues labelled `internal`, `docs`, `ci` or `test`: they have no user-facing change.
3. Leave out any change that was reverted before the release (look for `Revert` commits in the log).
4. Leave out fixes for bugs that were introduced in this same release and never shipped to users. The issue body says so.
5. One entry per issue, however many commits reference it (cherry-picks and follow-up commits are the same change).
6. Section, by the first matching label: `breaking` -> Breaking changes, `security` -> Security, `feature` -> Added, `deprecation` -> Deprecated, `bug` -> Fixed.
7. Maintainers: {', '.join(MAINTAINERS)}. Anyone else who opened a shipped issue is an external contributor.
"""

STYLE = """# Style guide for changelog bullets

Each bullet is one line: `- <text> (#<issue>)`.

1. `<text>` is at most 14 words.
2. `<text>` starts with a capital letter and does not end with a full stop.
3. If the issue was opened by an external contributor, end `<text>` with `, thanks @<handle>` (their issue author handle, counted outside the 14 words).
4. Name API items in backticks, exactly as in the Names list of the API reference, with the class prefix: `Queue.try_put()`, not `try_put()`. Put nothing else in backticks.
5. Never use these words: simply, just, easily, seamless, seamlessly, robust, leverage, powerful.
6. No emoji.
7. Write the product name as `tinyqueue`, all lower case, if you mention it at all.
8. Every breaking change gets one sub-bullet under it, indented two spaces: `  - Migration: <what to change>`.
9. The security bullet includes the CVE id from the issue title.
"""

FORMAT = f"""# Format of the changelog entry

1. The first line is exactly `## [{RELEASE}] - {DATE}`.
2. Then the sections, in this order, each as `### <Section>`, leaving out empty ones: Breaking changes, Security, Added, Deprecated, Fixed.
3. Bullets as written in stage 02, unchanged.
4. `release.json` has exactly these keys:
   - `version`: "{RELEASE}"
   - `date`: "{DATE}"
   - `counts`: an object mapping each section name used to its number of bullets
   - `issues`: every issue number in the entry, as integers, sorted ascending
5. The counts and issue list in `release.json` must match the Markdown entry exactly.
6. Older entries in the history use an older format (for example `### Bug fixes`). Follow these rules, not the old entries.
"""

VOICE = """# Voice

- Plain, direct, present tense where possible. Say what changed for the user, not how the code changed.
- Prefer the user's words: "jobs", "queue", "worker". Avoid internal names (registry, backend plumbing) unless the user touches them.
- Write "deprecated", never "obsolete". Write "removed", never "killed".
- One idea per bullet. If a bullet needs "and", it is probably two changes or too much detail.
"""

RELEASE_MD = f"""# Release

- Version: {RELEASE}
- Release date: {DATE}
- Previous version: 2.3.0
"""

def api_reference():
    lines = ["# tinyqueue API reference (2.4.0)", "",
             "tinyqueue is a small job queue for Python 3.10+. Jobs are pickled callables stored in a backend (memory or Redis) and run by workers.", ""]
    docs = {
        "Queue": "A named queue. `Queue(name, backend=None, result_ttl=None)`.",
        "Queue.put()": "Add a job. Blocks when the queue has a max size and is full.",
        "Queue.try_put()": "Add a job without blocking. Returns False when the queue is full. New name in 2.4.0.",
        "Queue.put_nowait()": "Removed in 2.4.0. Use Queue.try_put().",
        "Queue.get()": "Take the next job. Used by workers; rarely called directly.",
        "Queue.drain()": "Block until every queued and running job has finished. Takes an optional timeout.",
        "Queue.size": "Number of queued jobs. Deprecated in 2.4.0: use len(queue).",
        "len(queue)": "Number of queued jobs.",
        "QueueFull": "Raised by Queue.put() with block=False when the queue is full.",
        "Worker": "Runs jobs from one or more queues. `Worker(queues, concurrency=1, retry_backoff=None)`.",
        "retry_backoff": "Worker option. Base delay in seconds for exponential backoff between retries. None disables it.",
        "Job": "A queued call. Has an id, status, result and retries.",
        "Job.cancel()": "Cancel a job that has not started. Returns False if it is already running or done.",
        "Job.retries": "How many times a failed job is retried. retries=3 means at most 4 runs.",
        "schedule()": "Queue a job for later: `schedule(func, at=datetime, tz=None)`.",
        "RedisBackend": "Redis storage. Accepts `url` or `sentinels=[(host, port), ...]` with `service_name`.",
        "metrics_server()": "Start a Prometheus metrics endpoint on a port: queue depth, job durations, failures.",
        "serializer_allowlist": "Backend option. Only these classes may be unpickled from job payloads. On by default since 2.4.0.",
        "result_ttl": "Queue option. Seconds to keep job results. None used to mean forever; since 2.4.0 results are evicted after 24 hours.",
        "SIGTERM": "Workers finish the running job, then exit.",
        "tq stats": "Command line: print queue depth and worker status.",
    }
    for n in API_NAMES:
        lines += [f"## {n}", "", docs[n], ""]
    # realistic bulk: configuration and examples the stage-02 writer may consult
    lines += ["## Configuration", ""]
    for i, opt in enumerate(["concurrency", "poll_interval", "visibility_timeout", "max_size", "prefetch", "heartbeat", "log_level", "job_timeout"]):
        lines += [f"### {opt}", "", f"Default and behaviour of `{opt}` are documented in the user guide, section {i + 3}. "
                  "Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.", ""]
    lines += ["## Names", "", "These are the only names that may appear in backticks in the changelog:", ""]
    lines += [f"- `{n}`" for n in API_NAMES]
    return "\n".join(lines) + "\n"

def changelog_history():
    out = ["# Changelog history (older entries, for reference)", ""]
    out += ["## [2.3.0] - 2026-08-14", "", "### Added", "- `Queue.get()` accepts a timeout, thanks @rvdb (#371)", "- Worker heartbeats every 10 seconds (#366)", "",
            "### Fixed", "- Jobs scheduled across a DST change ran an hour late (#368)", "- `RedisBackend` retried forever on auth errors, thanks @dkowal (#373)", ""]
    out += ["## [2.2.0] - 2026-06-02", "", "### Deprecated", "- Positional `ttl` argument on `Queue` (#341)", "",
            "### Fixed", "- Worker crashed on jobs returning generators, thanks @hollis (#344)", ""]
    for v, d in [("2.1.0", "2026-03-20"), ("2.0.0", "2026-01-11"), ("1.9.0", "2025-10-30"), ("1.8.0", "2025-08-01")]:
        out += [f"## [{v}] - {d}", "", "### New features",
                "- TinyQueue now supports job priorities, which makes it easy to run urgent work first.",
                "- Added a simple way to inspect failed jobs from the command line.", "",
                "### Bug fixes",
                "- Fixed a robust handling issue where the worker would just stop polling after a network blip.",
                "- Fixed: results were not cleaned up when a job was cancelled during startup.", ""]
    return "\n".join(out) + "\n"

def git_log():
    rows = []
    for date, author, msg in COMMITS:
        h = hashlib.sha1(f"{date}{author}{msg}".encode()).hexdigest()[:7]
        rows.append(f"{h} {date} {author}: {msg}")
    return "\n".join(reversed(rows)) + "\n"  # newest first, like git log

def issues_json():
    return json.dumps([{"number": n, "title": t, "labels": l, "author": a, "state": s, "milestone": m, "body": b}
                       for n, l, t, a, s, m, b in ISSUES], indent=2) + "\n"

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)

def build():
    for d in (FOLDER, MONO, MONO_BIG):
        shutil.rmtree(d, ignore_errors=True)
    files = {
        "CLAUDE.md": CLAUDE_MD, "CONTEXT.md": ROUTING_MD,
        "inputs/git-log.txt": git_log(), "inputs/issues.json": issues_json(),
        "_config/release.md": RELEASE_MD, "_config/voice.md": VOICE,
        "stages/01_extract/CONTEXT.md": STAGE_01, "stages/01_extract/references/inclusion-rules.md": INCLUSION,
        "stages/02_draft/CONTEXT.md": STAGE_02, "stages/02_draft/references/style-guide.md": STYLE,
        "stages/02_draft/references/api-reference.md": api_reference(),
        "stages/03_publish/CONTEXT.md": STAGE_03, "stages/03_publish/references/format.md": FORMAT,
        "stages/03_publish/references/changelog-history.md": changelog_history(),
    }
    for rel, text in files.items():
        write(FOLDER / rel, text)
    for name, fn in extras.WORKFLOWS.items():
        write(FOLDER / "workflows" / name / "CONTEXT.md", fn())
    for s in ("01_extract", "02_draft", "03_publish"):
        (FOLDER / "stages" / s / "output").mkdir(parents=True, exist_ok=True)

    # The monolith: the same texts, joined into one CLAUDE.md, one output folder.
    order = ["CLAUDE.md", "_config/release.md", "_config/voice.md",
             "stages/01_extract/CONTEXT.md", "stages/01_extract/references/inclusion-rules.md",
             "stages/02_draft/CONTEXT.md", "stages/02_draft/references/style-guide.md", "stages/02_draft/references/api-reference.md",
             "stages/03_publish/CONTEXT.md", "stages/03_publish/references/format.md", "stages/03_publish/references/changelog-history.md"]
    head = ("# tinyqueue release workspace\n\nThis workspace prepares the release notes for tinyqueue, a Python job-queue library.\n"
            "Raw inputs are in `inputs/` (git log and issue export). Never edit them.\n"
            "Everything you need is in this file. Do the three steps below in order (extract, draft, publish). "
            "File paths inside the steps refer to sections of this file; write every output file to `output/`.\n")
    body = [head] + [f"\n<!-- from {rel} -->\n" + files[rel] for rel in order[1:]]
    write(MONO / "CLAUDE.md", "".join(body))
    write(MONO / "inputs/git-log.txt", files["inputs/git-log.txt"])
    write(MONO / "inputs/issues.json", files["inputs/issues.json"])
    (MONO / "output").mkdir(parents=True, exist_ok=True)

    # A2: the same release text inside a big CLAUDE.md that also holds the repo's other jobs,
    # release section in the middle (support, docs, RELEASE, social, on-call).
    W = extras.WORKFLOWS
    release_part = "\n# Workflow: release notes\n\n" + "".join(body[1:])
    big = (head.replace("Everything you need is in this file. Do the three steps below in order",
                        "This file holds every workflow in this repo. For release notes, do the three steps of the release-notes workflow in order")
           + "\n" + W["support"]() + "\n" + W["docs-site"]() + "\n" + release_part + "\n" + W["social"]() + "\n" + W["oncall"]())
    write(MONO_BIG / "CLAUDE.md", big)
    write(MONO_BIG / "inputs/git-log.txt", files["inputs/git-log.txt"])
    write(MONO_BIG / "inputs/issues.json", files["inputs/issues.json"])
    (MONO_BIG / "output").mkdir(parents=True, exist_ok=True)

    # C2: the same folder with one line of the stage-01 card changed (the "edit the source" fix):
    # the hand-off now carries whether the author is external, which stage 02 needs for credits.
    V2 = HERE / "workspace-folder-v2"
    shutil.rmtree(V2, ignore_errors=True)
    shutil.copytree(FOLDER, V2)
    card = V2 / "stages/01_extract/CONTEXT.md"
    card.write_text(card.read_text().replace(
        "| <issue author>`", "| <issue author> | external or maintainer`"))
    assert "external or maintainer" in card.read_text()

    truth = {
        "release": RELEASE, "date": DATE,
        "shipped": {str(n): {"section": SECTION_OF[l[0]], "external": a not in MAINTAINERS, "author": a}
                    for n, l, t, a, s, m, b in ISSUES if n in SHIPPED},
        "traps": {str(k): v for k, v in TRAPS.items()},
        "api_names": API_NAMES,
        "cve": "CVE-0000-00000",
    }
    write(HERE / "truth.json", json.dumps(truth, indent=1) + "\n")

    # self-check: the truth agrees with the inclusion rules applied mechanically
    reverted = {416}
    unreleased_fix = {n for n, l, t, a, s, m, b in ISSUES if "has not been released" in b}
    rule = {n for n, l, t, a, s, m, b in ISSUES
            if m == RELEASE and s == "closed" and not set(l) & {"internal", "docs", "ci", "test"}} - reverted - unreleased_fix
    assert rule == SHIPPED, (rule ^ SHIPPED)
    assert not SHIPPED & set(TRAPS)
    for n in SHIPPED | set(TRAPS):
        assert f"(#{n})" in git_log(), n
    print("ok:", len(SHIPPED), "shipped,", len(TRAPS), "traps;",
          "mono CLAUDE.md ~", len((MONO / "CLAUDE.md").read_text()) // 4, "tokens; big ~", len((MONO_BIG / "CLAUDE.md").read_text()) // 4, "tokens")

if __name__ == "__main__":
    build()
