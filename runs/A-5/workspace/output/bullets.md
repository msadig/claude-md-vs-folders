### Breaking changes
- Drop support for Python 3.9; Python 3.10 is now the minimum (#412)
  - Migration: Upgrade to Python 3.10 or later.
- Rename `Queue.put_nowait()` to `Queue.try_put()`, which returns False when full (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`.

### Security
- Restrict unpickled job classes with `serializer_allowlist`, on by default (CVE-0000-00000), thanks @mira-k (#431)

### Added
- `Queue.drain()` waits until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential delays between retries (#409)
- Add `metrics_server()` to serve Prometheus metrics, thanks @ana-p (#415)
- Cancel queued jobs that have not started with `Job.cancel()` (#422)
- Connect `RedisBackend` through Redis Sentinel, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size`; use `len(queue)` instead (#420)

### Fixed
- Fix `Worker` hanging on `SIGTERM` while a job runs, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Fix results kept forever when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` running jobs one extra time (#411)
- Fix `RedisBackend` not releasing connections after a timeout, thanks @rvdb (#414)
