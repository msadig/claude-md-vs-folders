### Breaking changes
- Drop support for Python 3.9; Python 3.10 is now the minimum (#412)
  - Migration: Upgrade to Python 3.10 or later.
- `Queue.put_nowait()` is removed and replaced by `Queue.try_put()` (#418)
  - Migration: Replace `Queue.put_nowait()` calls with `Queue.try_put()`, which returns False when the queue is full.

### Security
- Fix unsafe pickle deserialization (CVE-0000-00000) with `serializer_allowlist`, on by default, thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential delay between retries (#409)
- Add `metrics_server()` to expose a Prometheus metrics endpoint, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- `Queue.size` is deprecated; use `len(queue)` instead (#420)

### Fixed
- Fix `Worker` hanging on `SIGTERM` while a job is running, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Fix memory leak when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` running jobs one time too many (#411)
- Fix `RedisBackend` not releasing connections after a timeout, thanks @rvdb (#414)
