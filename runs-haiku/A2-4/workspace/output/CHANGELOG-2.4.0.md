## [2.4.0] - 2026-11-02

### Breaking changes
- Drop Python 3.9; the minimum version is now Python 3.10 (#412)
  - Migration: use Python 3.10 or newer
- Rename `Queue.put_nowait()` to `Queue.try_put()`; it returns False when full (#418)
  - Migration: call `Queue.try_put()` instead of `Queue.put_nowait()`

### Security
- Fix CVE-0000-00000: `serializer_allowlist`, on by default, limits unpickled job payloads, thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until queued and running jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker`: exponential delay between retries, off by default (#409)
- Add `metrics_server()` for a Prometheus endpoint: queue depth, job durations, failures, thanks @ana-p (#415)
- Add `Job.cancel()` for jobs that have not started yet (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Mark `Queue.size` as deprecated; use `len(queue)` instead (#420)

### Fixed
- Fix `Worker` hanging after `SIGTERM` while a job runs, thanks @hollis (#401)
- Fix `schedule()` ignoring its tz argument (#403)
- Fix memory leak: results are now evicted after 24 hours when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` off-by-one in the retry count (#411)
- Fix `RedisBackend` pool exhaustion after repeated timeouts, thanks @rvdb (#414)
