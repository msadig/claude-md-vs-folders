### Breaking changes
- Python 3.9 is no longer supported; the minimum is Python 3.10 (#412)
  - Migration: Upgrade to Python 3.10 or newer
- Rename `Queue.put_nowait()` to `Queue.try_put()`, which returns False when full (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`

### Security
- Fix code execution from crafted job payloads (CVE-0000-00000) using `serializer_allowlist`, on by default, thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential backoff between retries (#409)
- Add `metrics_server()` to serve Prometheus metrics, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel queued jobs that have not started (#422)
- Connect through Redis Sentinel with `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size` in favour of `len(queue)` (#420)

### Fixed
- Fix `Worker` hanging on `SIGTERM` while a job is running, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Fix results being kept forever when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` running jobs one extra time (#411)
- Fix `RedisBackend` not releasing connections after a timeout, thanks @rvdb (#414)
