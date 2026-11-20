## [2.4.0] - 2026-11-02

### Breaking changes

- Drop support for Python 3.9, the minimum is now Python 3.10 (#412)
  - Migration: Upgrade to Python 3.10 or later.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`, which returns False when full.

### Security

- Fix unsafe pickle deserialization with new `serializer_allowlist` option, on by default (CVE-0000-00000), thanks @mira-k (#431)

### Added

- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential retry delays (#409)
- Add Prometheus metrics endpoint through `metrics_server()`, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel queued jobs that have not started (#422)
- Support Redis Sentinel in `RedisBackend`, thanks @dkowal (#427)

### Deprecated

- Deprecate `Queue.size` in favour of `len(queue)` (#420)

### Fixed

- Fix `Worker` hanging on `SIGTERM` while a job is running, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Fix memory leak in the result cache when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` being off by one (#411)
- Fix `RedisBackend` not releasing the connection after a timeout, thanks @rvdb (#414)
