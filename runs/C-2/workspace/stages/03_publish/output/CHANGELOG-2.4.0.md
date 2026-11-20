## [2.4.0] - 2026-11-02

### Breaking changes

- Python 3.9 is no longer supported (#412)
  - Migration: Upgrade to Python 3.10 or later
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`

### Security

- Restrict unpickling of job payloads with `serializer_allowlist`, fixing CVE-0000-00000, thanks @mira-k (#431)

### Added

- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` (#409)
- Add Prometheus metrics endpoint with `metrics_server()`, thanks @ana-p (#415)
- Add `Job.cancel()` for queued jobs (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated

- Deprecate `Queue.size` in favour of `len(queue)` (#420)

### Fixed

- Fix `Worker` hanging on `SIGTERM` while a job is running, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Fix memory leak in the result cache, thanks @ana-p (#407)
- Fix `Job.retries` being off by one (#411)
- Fix `RedisBackend` not releasing the connection after a timeout, thanks @rvdb (#414)
