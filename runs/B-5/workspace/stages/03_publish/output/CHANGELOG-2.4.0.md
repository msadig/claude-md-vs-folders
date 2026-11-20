## [2.4.0] - 2026-11-02

### Breaking changes
- Require Python 3.10 or newer (#412)
  - Migration: Upgrade to Python 3.10 or newer.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`, which returns False when the queue is full.

### Security
- Restrict job payload unpickling with `serializer_allowlist`, on by default (CVE-0000-00000), thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential delay between retries (#409)
- Add `metrics_server()` to expose Prometheus metrics, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel a job that has not started (#422)
- Support Redis Sentinel in `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size`; use `len(queue)` instead (#420)

### Fixed
- Exit `Worker` cleanly on `SIGTERM` while a job runs, thanks @hollis (#401)
- Respect the tz argument in `schedule()` (#403)
- Fix memory leak in result cache when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` running jobs one time too many (#411)
- Release the `RedisBackend` connection after a timeout, thanks @rvdb (#414)
