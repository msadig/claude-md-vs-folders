### Breaking changes
- Python 3.9 is no longer supported; the minimum is Python 3.10 (#412)
  - Migration: Upgrade to Python 3.10 or newer.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`, which returns False when the queue is full.

### Security
- Add `serializer_allowlist`, on by default, to block code execution from job payloads (CVE-0000-00000), thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential delay between retries (#409)
- Add `metrics_server()` to serve Prometheus metrics, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel a job that has not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size`; use `len(queue)` instead (#420)

### Fixed
- Fix `Worker` hanging on `SIGTERM` while a job runs, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Fix result cache memory leak when `result_ttl` is unset, thanks @ana-p (#407)
- Fix off-by-one in `Job.retries` (#411)
- Fix `RedisBackend` not releasing its connection after a timeout, thanks @rvdb (#414)
