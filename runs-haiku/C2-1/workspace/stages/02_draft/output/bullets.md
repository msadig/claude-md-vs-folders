### Breaking changes

- Removed Python 3.9 support, minimum is now Python 3.10 (#412)
  - Migration: Use Python 3.10 or newer.
- Renamed `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace `Queue.put_nowait()` calls with `Queue.try_put()`, which returns False when full.

### Security

- Fixed code execution from crafted job payloads, CVE-0000-00000, thanks @mira-k (#431)

### Added

- New `Queue.drain()` waits until all jobs finish, thanks @tobiaslund (#405)
- New `retry_backoff` option on `Worker` adds exponential backoff, off by default (#409)
- New `metrics_server()` exposes Prometheus queue depth, job durations, failures, thanks @ana-p (#415)
- New `Job.cancel()` cancels queued jobs that have not started (#422)
- New Redis Sentinel support in `RedisBackend`, thanks @dkowal (#427)

### Deprecated

- Deprecated `Queue.size`, use `len(queue)` instead (#420)

### Fixed

- Fixed `Worker` hanging on SIGTERM while a job runs, thanks @hollis (#401)
- Fixed `schedule()` ignoring the tz argument (#403)
- Fixed memory leak when `result_ttl` is unset, thanks @ana-p (#407)
- Fixed `Job.retries` being off by one (#411)
- Fixed `RedisBackend` not releasing connections after a timeout, thanks @rvdb (#414)
