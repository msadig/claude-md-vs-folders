## [2.4.0] - 2026-11-02

### Breaking changes
- Dropped Python 3.9 support; Python 3.10 is now the minimum (#412)
  - Migration: run tinyqueue on Python 3.10 or later
- Renamed `Queue.put_nowait()` to `Queue.try_put()`, which returns False when full (#418)
  - Migration: replace `Queue.put_nowait()` calls with `Queue.try_put()`

### Security
- Crafted job payloads can no longer run code on workers, CVE-0000-00000, thanks @mira-k (#431)

### Added
- New `Queue.drain()` waits for all jobs to finish, thanks @tobiaslund (#405)
- New `retry_backoff` option on `Worker` adds exponential backoff between retries (#409)
- New `metrics_server()` exposes Prometheus queue depth, job durations and failures, thanks @ana-p (#415)
- New `Job.cancel()` cancels a queued job before it starts (#422)
- New Redis Sentinel support in `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecated `Queue.size`; use `len(queue)` instead (#420)

### Fixed
- Workers no longer hang on SIGTERM while a job runs, thanks @hollis (#401)
- Scheduled jobs now respect the time zone passed to `schedule()` (#403)
- Results are now evicted after 24 hours when `result_ttl` is unset, thanks @ana-p (#407)
- Fixed `Job.retries` off-by-one; retries=3 now means at most four runs (#411)
- Redis pool no longer runs out of connections after timeouts, thanks @rvdb (#414)
