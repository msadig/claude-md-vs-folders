## [2.4.0] - 2026-11-02

### Breaking changes
- Drop Python 3.9 support; minimum is now Python 3.10 (#412)
  - Migration: Use Python 3.10 or newer
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`

### Security
- Fix code execution from crafted job payloads, CVE-0000-00000, thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential delays between retries (#409)
- Add `metrics_server()` with a Prometheus endpoint for queue metrics, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size`; use `len(queue)` instead (#420)

### Fixed
- Fix worker hanging on `SIGTERM` while a job runs, thanks @hollis (#401)
- Fix `schedule()` ignoring its tz argument (#403)
- Fix memory leak in results cache when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` running jobs one time too many (#411)
- Fix `RedisBackend` running out of connections after timeouts, thanks @rvdb (#414)
