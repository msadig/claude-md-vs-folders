### Breaking changes
- Drop support for Python 3.9 (#412)
  - Migration: use Python 3.10 or newer.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: call `Queue.try_put()` instead of `Queue.put_nowait()`.

### Security
- Fix CVE-0000-00000: job payloads are checked by `serializer_allowlist`, on by default, thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker`: exponential delays between retries, off by default (#409)
- Add `metrics_server()` for a Prometheus metrics endpoint, thanks @ana-p (#415)
- Add `Job.cancel()` to stop jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size` in favor of `len(queue)` (#420)

### Fixed
- Workers now exit cleanly on `SIGTERM` while a job runs, thanks @hollis (#401)
- `schedule()` now respects the tz argument (#403)
- Results are evicted after 24 hours when `result_ttl` is unset, thanks @ana-p (#407)
- Fix off-by-one in `Job.retries`, so run count matches the docs (#411)
- `RedisBackend` now releases connections after a timeout, thanks @rvdb (#414)
