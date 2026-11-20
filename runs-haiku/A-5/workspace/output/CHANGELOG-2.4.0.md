## [2.4.0] - 2026-11-02

### Breaking changes
- Drop Python 3.9 support; minimum is now Python 3.10 (#412)
  - Migration: Use Python 3.10 or newer.
- Rename `Queue.put_nowait()` to `Queue.try_put()`, which returns False when full (#418)
  - Migration: Replace `Queue.put_nowait()` calls with `Queue.try_put()`.

### Security
- Fix CVE-0000-00000 by allow-listing classes unpickled from job payloads (#431)

### Added
- Add `Queue.drain()` to wait until all queued and running jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential backoff, off by default (#409)
- Add Prometheus endpoint with `metrics_server()` for queue depth, durations and failures, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel a job that has not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- `Queue.size` is deprecated; use `len(queue)` instead (#420)

### Fixed
- `Worker` exits cleanly on `SIGTERM` while a job runs, thanks @hollis (#401)
- `schedule()` now respects the tz argument (#403)
- Fix memory leak: results now expire after 24 hours when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` being off by one (#411)
- Fix `RedisBackend` running out of connections after repeated timeouts, thanks @rvdb (#414)
