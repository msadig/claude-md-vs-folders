### Breaking changes
- Remove support for Python 3.9; Python 3.10 is the minimum (#412)
  - Migration: Upgrade to Python 3.10 or newer
- `Queue.put_nowait()` is removed and replaced by `Queue.try_put()` (#418)
  - Migration: Call `Queue.try_put()` instead of `Queue.put_nowait()`

### Security
- Job payloads load only allowed classes via `serializer_allowlist`, fixing CVE-0000-00000, thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential delay between retries (#409)
- Add `metrics_server()` to expose Prometheus queue metrics, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Support Redis Sentinel in `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- `Queue.size` is deprecated; use `len(queue)` instead (#420)

### Fixed
- Workers now exit on `SIGTERM` after finishing the running job, thanks @hollis (#401)
- `schedule()` now respects the tz argument (#403)
- Fix memory leak: results are now evicted when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` running one extra time (#411)
- Release `RedisBackend` connections after a timeout, thanks @rvdb (#414)
