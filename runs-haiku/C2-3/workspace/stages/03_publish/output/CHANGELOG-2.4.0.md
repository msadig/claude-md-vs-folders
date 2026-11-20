## [2.4.0] - 2026-11-02

### Breaking changes
- Python 3.9 is no longer supported (#412)
  - Migration: use Python 3.10 or newer.
- `Queue.put_nowait()` is renamed to `Queue.try_put()` (#418)
  - Migration: rename calls to `Queue.try_put()`; it returns False when full instead of blocking.

### Security
- Fixes CVE-0000-00000: `serializer_allowlist` restricts job payloads by default, thanks @mira-k (#431)

### Added
- `Queue.drain()` waits until all queued and running jobs finish, thanks @tobiaslund (#405)
- `Worker` takes `retry_backoff` for exponential retry delays, off by default (#409)
- `metrics_server()` starts a Prometheus endpoint for queue depth, job durations and failures, thanks @ana-p (#415)
- `Job.cancel()` cancels a queued job that has not started yet (#422)
- `RedisBackend` connects through Redis Sentinel, thanks @dkowal (#427)

### Deprecated
- `Queue.size` is deprecated; use `len(queue)` instead (#420)

### Fixed
- `Worker` exits after `SIGTERM` while a job is running, thanks @hollis (#401)
- `schedule()` now respects its tz argument (#403)
- Memory leak fixed: results now expire after 24 hours if `result_ttl` is unset, thanks @ana-p (#407)
- `Job.retries` now matches its docs: retries=3 means at most 4 runs (#411)
- `RedisBackend` releases its connection after a timeout, thanks @rvdb (#414)
