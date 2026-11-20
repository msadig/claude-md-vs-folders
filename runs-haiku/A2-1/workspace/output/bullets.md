### Breaking changes
- Drop Python 3.9 support; Python 3.10 is now the minimum (#412)
  - Migration: use Python 3.10 or newer before upgrading.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: replace `Queue.put_nowait()` with `Queue.try_put()`, which returns False when full.

### Security
- Fix CVE-0000-00000: `serializer_allowlist` is on by default, thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait for jobs to finish, thanks @tobiaslund (#405)
- Add `retry_backoff` on `Worker` to space out retries, off by default (#409)
- Add `metrics_server()` for Prometheus queue depth, job durations, failures, thanks @ana-p (#415)
- Add `Job.cancel()` for jobs that have not started yet (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size`; use `len(queue)` instead (#420)

### Fixed
- Fix `Worker` not exiting on `SIGTERM` while a job runs, thanks @hollis (#401)
- Fix `schedule()` ignoring the time zone argument (#403)
- Fix memory leak in result cache when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` off by one (#411)
- Fix `RedisBackend` pool exhaustion after repeated timeouts, thanks @rvdb (#414)
