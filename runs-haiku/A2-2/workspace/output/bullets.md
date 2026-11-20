### Breaking changes
- Python 3.9 is no longer supported (#412)
  - Migration: Upgrade to Python 3.10 or newer.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Call `Queue.try_put()` instead of `Queue.put_nowait()`.

### Security
- Fix CVE-0000-00000: job payloads are checked by `serializer_allowlist`, on by default (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` to `Worker` for exponential backoff between retries (#409)
- Add Prometheus metrics endpoint via `metrics_server()`, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel jobs that have not started yet (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- `Queue.size` is deprecated; use `len(queue)` instead (#420)

### Fixed
- `Worker` no longer hangs on `SIGTERM` while a job runs, thanks @hollis (#401)
- `schedule()` now respects the tz argument (#403)
- Results are evicted after 24 hours when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` being off by one (#411)
- `RedisBackend` no longer exhausts its connection pool after timeouts, thanks @rvdb (#414)
