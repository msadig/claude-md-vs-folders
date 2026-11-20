### Breaking changes
- Drop support for Python 3.9; the minimum is now 3.10 (#412)
  - Migration: upgrade to Python 3.10 or newer.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: replace calls to `Queue.put_nowait()` with `Queue.try_put()`.

### Security
- Fix CVE-0000-00000: only allow-listed classes are unpickled from job payloads, thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential delays between retries (#409)
- Add `metrics_server()` to expose queue metrics to Prometheus, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel queued jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size` in favour of `len(queue)` (#420)

### Fixed
- Fix `Worker` not exiting on `SIGTERM` while a job is running, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Fix memory leak: results with `result_ttl` unset are now evicted after 24 hours, thanks @ana-p (#407)
- Fix `Job.retries` off by one, so failed jobs ran an extra time (#411)
- Fix `RedisBackend` exhausting its connection pool after timeouts, thanks @rvdb (#414)
