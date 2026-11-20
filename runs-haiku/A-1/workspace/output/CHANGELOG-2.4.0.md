## [2.4.0] - 2026-11-02

### Breaking changes
- Dropped Python 3.9 support; minimum is now Python 3.10 (#412)
  - Migration: upgrade to Python 3.10 or newer.
- Removed `Queue.put_nowait()`; use `Queue.try_put()`, which returns False when full (#418)
  - Migration: replace calls to `Queue.put_nowait()` with `Queue.try_put()`.

### Security
- Fixed unsafe unpickling of job payloads, CVE-0000-00000, thanks @mira-k (#431)

### Added
- New `Queue.drain()` waits until all queued and running jobs finish, thanks @tobiaslund (#405)
- New `retry_backoff` option on `Worker` for exponential backoff between retries, off by default (#409)
- New `metrics_server()` serves a Prometheus endpoint with queue depth, job durations and failures, thanks @ana-p (#415)
- New `Job.cancel()` cancels a job that has not started yet (#422)
- New Redis Sentinel support in `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecated `Queue.size`; use `len(queue)` instead (#420)

### Fixed
- Fixed `Worker` hanging on `SIGTERM` while a job runs, thanks @hollis (#401)
- Fixed `schedule()` ignoring the tz argument (#403)
- Fixed memory leak: results are kept forever when `result_ttl` is unset, thanks @ana-p (#407)
- Fixed `Job.retries` off-by-one in the number of runs (#411)
- Fixed `RedisBackend` exhausting its connection pool after many timeouts, thanks @rvdb (#414)
