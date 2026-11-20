### Breaking changes
- Drop support for Python 3.9, the minimum is now Python 3.10 (#412)
  - Migration: Upgrade to Python 3.10 or later
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace `Queue.put_nowait()` calls with `Queue.try_put()`, which returns False when the queue is full

### Security
- Restrict job payload deserialization with `serializer_allowlist`, on by default (CVE-0000-00000), thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add the `retry_backoff` option to `Worker` for exponential retry delays (#409)
- Add `metrics_server()` to expose queue depth, job durations and failures to Prometheus, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel a job that has not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size`, use `len(queue)` instead (#420)

### Fixed
- Fix `Worker` hanging on `SIGTERM` while a job is running, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Fix a memory leak in the result cache when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` running a job one time too many (#411)
- Fix `RedisBackend` not releasing connections after a timeout, thanks @rvdb (#414)
