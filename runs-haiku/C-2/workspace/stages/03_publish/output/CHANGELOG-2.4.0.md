## [2.4.0] - 2026-11-02

### Breaking changes

- Drop support for Python 3.9 (#412)
  - Migration: upgrade to Python 3.10 or later.
- `Queue.put_nowait()` is renamed to `Queue.try_put()` (#418)
  - Migration: replace `Queue.put_nowait()` with `Queue.try_put()`, which returns False when full.

### Security

- Pickle payloads are restricted by `serializer_allowlist`, fixing CVE-0000-00000, thanks @mira-k (#431)

### Added

- `Queue.drain()` waits until all jobs finish, with an optional timeout, thanks @tobiaslund (#405)
- `Worker` has a `retry_backoff` option for exponential delay between retries, off by default (#409)
- `metrics_server()` adds a Prometheus endpoint for queue depth, job durations, failures, thanks @ana-p (#415)
- `Job.cancel()` cancels queued jobs that have not started yet (#422)
- `RedisBackend` supports Redis Sentinel connections, thanks @dkowal (#427)

### Deprecated

- `Queue.size` is deprecated; use `len(queue)` instead (#420)

### Fixed

- `Worker` finishes its running job, then exits on `SIGTERM`, thanks @hollis (#401)
- `schedule()` respects the tz argument (#403)
- Results are no longer kept forever when `result_ttl` is unset, thanks @ana-p (#407)
- `Job.retries` is no longer off by one; retries=3 means at most four runs (#411)
- `RedisBackend` releases the connection after a timeout, thanks @rvdb (#414)
