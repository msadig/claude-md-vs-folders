## [2.4.0] - 2026-11-02

### Breaking changes
- Drop support for Python 3.9 (#412)
  - Migration: Upgrade to Python 3.10 or later
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace `Queue.put_nowait()` calls with `Queue.try_put()`

### Security
- Restrict unpickled job payloads with `serializer_allowlist` (CVE-0000-00000), thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option on `Worker` for exponential retry delays (#409)
- Add Prometheus metrics endpoint through `metrics_server()`, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size` in favour of `len(queue)` (#420)

### Fixed
- Fix `Worker` hanging on `SIGTERM` while a job is running, thanks @hollis (#401)
- Fix `schedule()` ignoring the time zone argument (#403)
- Fix memory leak in the result cache, thanks @ana-p (#407)
- Fix off-by-one in `Job.retries` (#411)
- Fix `RedisBackend` not releasing connections after a timeout, thanks @rvdb (#414)
