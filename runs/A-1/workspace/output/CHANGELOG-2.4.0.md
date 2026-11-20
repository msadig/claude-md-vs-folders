## [2.4.0] - 2026-11-02

### Breaking changes
- Remove support for Python 3.9; Python 3.10 is now the minimum (#412)
  - Migration: Upgrade to Python 3.10 or later
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`

### Security
- Restrict unpickling of job payloads with `serializer_allowlist`, on by default (CVE-0000-00000), thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential delay between retries (#409)
- Add `metrics_server()` for Prometheus metrics, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size`; use `len(queue)` instead (#420)

### Fixed
- Fix `Worker` hanging on `SIGTERM` while a job runs, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Evict old job results when `result_ttl` is unset, fixing a memory leak, thanks @ana-p (#407)
- Fix `Job.retries` running one time too many (#411)
- Fix `RedisBackend` not releasing connections after a timeout, thanks @rvdb (#414)
