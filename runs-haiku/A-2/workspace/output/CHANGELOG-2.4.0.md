## [2.4.0] - 2026-11-02

### Breaking changes
- Python 3.9 is no longer supported; minimum is Python 3.10 (#412)
  - Migration: Use Python 3.10 or newer before upgrading
- `Queue.put_nowait()` is removed; use `Queue.try_put()` instead (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`

### Security
- Fixes CVE-0000-00000: `serializer_allowlist` limits which classes job payloads may unpickle, thanks @mira-k (#431)

### Added
- `Queue.drain()` waits until all jobs finish, thanks @tobiaslund (#405)
- `Worker` accepts `retry_backoff` for exponential delay between retries (#409)
- `metrics_server()` starts a Prometheus endpoint for queue metrics, thanks @ana-p (#415)
- `Job.cancel()` cancels a job that has not started yet (#422)
- `RedisBackend` connects through Redis Sentinel when you pass sentinels, thanks @dkowal (#427)

### Deprecated
- `Queue.size` is deprecated; use `len(queue)` instead (#420)

### Fixed
- Workers exit on `SIGTERM` after the running job finishes, thanks @hollis (#401)
- `schedule()` runs jobs at the time zone you pass, not UTC (#403)
- Results are evicted after 24 hours when `result_ttl` is unset, thanks @ana-p (#407)
- `Job.retries` now counts retries correctly, no longer off by one (#411)
- `RedisBackend` releases the connection after a timeout, thanks @rvdb (#414)
