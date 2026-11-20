## [2.4.0] - 2026-11-02

### Breaking changes
- Python 3.9 is no longer supported; Python 3.10 is the minimum (#412)
  - Migration: Upgrade to Python 3.10 or later
- `Queue.put_nowait()` is removed; use `Queue.try_put()` instead (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`, which returns False when full

### Security
- Job payloads are unpickled only from allowed classes via `serializer_allowlist` (CVE-0000-00000), thanks @mira-k (#431)

### Added
- Wait for all jobs to finish with `Queue.drain()`, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential delay between retries (#409)
- Add `metrics_server()` to serve Prometheus metrics, thanks @ana-p (#415)
- Cancel jobs that have not started with `Job.cancel()` (#422)
- Connect `RedisBackend` through Redis Sentinel, thanks @dkowal (#427)

### Deprecated
- `Queue.size` is deprecated; use `len(queue)` (#420)

### Fixed
- Fix `Worker` hanging on `SIGTERM` while a job runs, thanks @hollis (#401)
- Fix `schedule()` ignoring the time zone argument (#403)
- Fix memory leak when `result_ttl` is unset, thanks @ana-p (#407)
- Fix off-by-one error in `Job.retries` (#411)
- Fix `RedisBackend` not releasing connections after a timeout, thanks @rvdb (#414)
