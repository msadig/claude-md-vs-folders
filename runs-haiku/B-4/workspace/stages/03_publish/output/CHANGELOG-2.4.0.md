## [2.4.0] - 2026-11-02

### Breaking changes
- Dropped support for Python 3.9 (#412)
  - Migration: use Python 3.10 or later
- Renamed `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: call `Queue.try_put()` instead of `Queue.put_nowait()`

### Security
- Fixed code execution on workers from crafted job payloads, CVE-0000-00000, thanks @mira-k (#431)

### Added
- Added `Queue.drain()` to wait until all queued and running jobs finish, thanks @tobiaslund (#405)
- Added `retry_backoff` option to `Worker` for exponential backoff between retries, off by default (#409)
- Added `metrics_server()` to serve Prometheus metrics, thanks @ana-p (#415)
- Added `Job.cancel()` to cancel jobs that have not started yet (#422)
- Added Redis Sentinel support to `RedisBackend` through `sentinels`, thanks @dkowal (#427)

### Deprecated
- Deprecated `Queue.size`, use `len(queue)` instead (#420)

### Fixed
- Fixed `schedule()` ignoring its tz argument (#403)
- Fixed workers not exiting on `SIGTERM` while a job runs, thanks @hollis (#401)
- Fixed memory leak where results were kept forever if `result_ttl` was unset, thanks @ana-p (#407)
- Fixed `Job.retries` off by one, so jobs ran one extra time (#411)
- Fixed `RedisBackend` not releasing connections after timeouts, thanks @rvdb (#414)
