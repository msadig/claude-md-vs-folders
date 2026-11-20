### Breaking changes
- Python 3.9 is no longer supported; the minimum is now Python 3.10 (#412)
  - Migration: Upgrade to Python 3.10 or newer
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`, which returns False when the queue is full

### Security
- Enable `serializer_allowlist` by default to block code execution from crafted payloads (CVE-0000-00000), thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option on `Worker` for exponential backoff between retries (#409)
- Add `metrics_server()` to serve Prometheus metrics, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Support Redis Sentinel in `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size`; use `len(queue)` instead (#420)

### Fixed
- Exit `Worker` cleanly on `SIGTERM` while a job is running, thanks @hollis (#401)
- Respect the tz argument in `schedule()` (#403)
- Evict results after 24 hours when `result_ttl` is unset, thanks @ana-p (#407)
- Fix off-by-one error in `Job.retries` count (#411)
- Release `RedisBackend` connections after a timeout, thanks @rvdb (#414)
