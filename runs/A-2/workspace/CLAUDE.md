# tinyqueue release workspace

This workspace prepares the release notes for tinyqueue, a Python job-queue library.
Raw inputs are in `inputs/` (git log and issue export). Never edit them.
Everything you need is in this file. Do the three steps below in order (extract, draft, publish). File paths inside the steps refer to sections of this file; write every output file to `output/`.

<!-- from _config/release.md -->
# Release

- Version: 2.4.0
- Release date: 2026-11-02
- Previous version: 2.3.0

<!-- from _config/voice.md -->
# Voice

- Plain, direct, present tense where possible. Say what changed for the user, not how the code changed.
- Prefer the user's words: "jobs", "queue", "worker". Avoid internal names (registry, backend plumbing) unless the user touches them.
- Write "deprecated", never "obsolete". Write "removed", never "killed".
- One idea per bullet. If a bullet needs "and", it is probably two changes or too much detail.

<!-- from stages/01_extract/CONTEXT.md -->
# Stage 01: extract

## Inputs
- Layer 4 (working): `../../inputs/git-log.txt`, `../../inputs/issues.json`
- Layer 3 (reference): `references/inclusion-rules.md`
- Layer 3 (reference): `../../_config/release.md`

## Process
Go through every issue referenced in the git log and decide, with the inclusion rules, whether it ships in this release and in which section.

## Outputs
- `output/changes.md`: one line per shipped change: `<section> | #<number> | <issue title> | <issue author>`

<!-- from stages/01_extract/references/inclusion-rules.md -->
# Inclusion rules

1. Only issues in milestone `2.4.0` with state `closed` ship.
2. Leave out issues labelled `internal`, `docs`, `ci` or `test`: they have no user-facing change.
3. Leave out any change that was reverted before the release (look for `Revert` commits in the log).
4. Leave out fixes for bugs that were introduced in this same release and never shipped to users. The issue body says so.
5. One entry per issue, however many commits reference it (cherry-picks and follow-up commits are the same change).
6. Section, by the first matching label: `breaking` -> Breaking changes, `security` -> Security, `feature` -> Added, `deprecation` -> Deprecated, `bug` -> Fixed.
7. Maintainers: lena-ortiz, sam-okafor. Anyone else who opened a shipped issue is an external contributor.

<!-- from stages/02_draft/CONTEXT.md -->
# Stage 02: draft

## Inputs
- Layer 4 (working): `../01_extract/output/changes.md`, `../../inputs/issues.json` (for detail only)
- Layer 3 (reference): `references/style-guide.md`, `references/api-reference.md`
- Layer 3 (reference): `../../_config/voice.md`

## Process
Write one bullet per change, following the style guide exactly. Do not add or drop changes.

## Outputs
- `output/bullets.md`: the bullets grouped under their section headings

<!-- from stages/02_draft/references/style-guide.md -->
# Style guide for changelog bullets

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

<!-- from stages/02_draft/references/api-reference.md -->
# tinyqueue API reference (2.4.0)

tinyqueue is a small job queue for Python 3.10+. Jobs are pickled callables stored in a backend (memory or Redis) and run by workers.

## Queue

A named queue. `Queue(name, backend=None, result_ttl=None)`.

## Queue.put()

Add a job. Blocks when the queue has a max size and is full.

## Queue.try_put()

Add a job without blocking. Returns False when the queue is full. New name in 2.4.0.

## Queue.put_nowait()

Removed in 2.4.0. Use Queue.try_put().

## Queue.get()

Take the next job. Used by workers; rarely called directly.

## Queue.drain()

Block until every queued and running job has finished. Takes an optional timeout.

## Queue.size

Number of queued jobs. Deprecated in 2.4.0: use len(queue).

## len(queue)

Number of queued jobs.

## QueueFull

Raised by Queue.put() with block=False when the queue is full.

## Worker

Runs jobs from one or more queues. `Worker(queues, concurrency=1, retry_backoff=None)`.

## retry_backoff

Worker option. Base delay in seconds for exponential backoff between retries. None disables it.

## Job

A queued call. Has an id, status, result and retries.

## Job.cancel()

Cancel a job that has not started. Returns False if it is already running or done.

## Job.retries

How many times a failed job is retried. retries=3 means at most 4 runs.

## schedule()

Queue a job for later: `schedule(func, at=datetime, tz=None)`.

## RedisBackend

Redis storage. Accepts `url` or `sentinels=[(host, port), ...]` with `service_name`.

## metrics_server()

Start a Prometheus metrics endpoint on a port: queue depth, job durations, failures.

## serializer_allowlist

Backend option. Only these classes may be unpickled from job payloads. On by default since 2.4.0.

## result_ttl

Queue option. Seconds to keep job results. None used to mean forever; since 2.4.0 results are evicted after 24 hours.

## SIGTERM

Workers finish the running job, then exit.

## tq stats

Command line: print queue depth and worker status.

## Configuration

### concurrency

Default and behaviour of `concurrency` are documented in the user guide, section 3. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### poll_interval

Default and behaviour of `poll_interval` are documented in the user guide, section 4. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### visibility_timeout

Default and behaviour of `visibility_timeout` are documented in the user guide, section 5. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### max_size

Default and behaviour of `max_size` are documented in the user guide, section 6. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### prefetch

Default and behaviour of `prefetch` are documented in the user guide, section 7. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### heartbeat

Default and behaviour of `heartbeat` are documented in the user guide, section 8. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### log_level

Default and behaviour of `log_level` are documented in the user guide, section 9. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### job_timeout

Default and behaviour of `job_timeout` are documented in the user guide, section 10. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

## Names

These are the only names that may appear in backticks in the changelog:

- `Queue`
- `Queue.put()`
- `Queue.try_put()`
- `Queue.put_nowait()`
- `Queue.get()`
- `Queue.drain()`
- `Queue.size`
- `len(queue)`
- `QueueFull`
- `Worker`
- `retry_backoff`
- `Job`
- `Job.cancel()`
- `Job.retries`
- `schedule()`
- `RedisBackend`
- `metrics_server()`
- `serializer_allowlist`
- `result_ttl`
- `SIGTERM`
- `tq stats`

<!-- from stages/03_publish/CONTEXT.md -->
# Stage 03: publish

## Inputs
- Layer 4 (working): `../02_draft/output/bullets.md`
- Layer 3 (reference): `references/format.md`, `references/changelog-history.md`
- Layer 3 (reference): `../../_config/release.md`

## Process
Assemble the changelog entry and the JSON summary, following the format rules. Check that the counts match.

## Outputs
- `output/CHANGELOG-2.4.0.md`
- `output/release.json`

<!-- from stages/03_publish/references/format.md -->
# Format of the changelog entry

1. The first line is exactly `## [2.4.0] - 2026-11-02`.
2. Then the sections, in this order, each as `### <Section>`, leaving out empty ones: Breaking changes, Security, Added, Deprecated, Fixed.
3. Bullets as written in stage 02, unchanged.
4. `release.json` has exactly these keys:
   - `version`: "2.4.0"
   - `date`: "2026-11-02"
   - `counts`: an object mapping each section name used to its number of bullets
   - `issues`: every issue number in the entry, as integers, sorted ascending
5. The counts and issue list in `release.json` must match the Markdown entry exactly.
6. Older entries in the history use an older format (for example `### Bug fixes`). Follow these rules, not the old entries.

<!-- from stages/03_publish/references/changelog-history.md -->
# Changelog history (older entries, for reference)

## [2.3.0] - 2026-08-14

### Added
- `Queue.get()` accepts a timeout, thanks @rvdb (#371)
- Worker heartbeats every 10 seconds (#366)

### Fixed
- Jobs scheduled across a DST change ran an hour late (#368)
- `RedisBackend` retried forever on auth errors, thanks @dkowal (#373)

## [2.2.0] - 2026-06-02

### Deprecated
- Positional `ttl` argument on `Queue` (#341)

### Fixed
- Worker crashed on jobs returning generators, thanks @hollis (#344)

## [2.1.0] - 2026-03-20

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.

## [2.0.0] - 2026-01-11

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.

## [1.9.0] - 2025-10-30

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.

## [1.8.0] - 2025-08-01

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.

