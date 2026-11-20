### Breaking changes
- Rename `Queue.put_nowait()` to `Queue.try_put()`, which returns False when full (#418)
  - Migration: call `Queue.try_put()` in place of `Queue.put_nowait()`
- Drop Python 3.9 support; minimum is now Python 3.10 (#412)
  - Migration: run on Python 3.10 or newer before upgrading

### Security
- Fix code execution from crafted payloads with `serializer_allowlist` on by default (CVE-0000-00000), thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential retry delays, off by default (#409)
- Add `metrics_server()`, a Prometheus endpoint for queue metrics, thanks @ana-p (#415)
- Add `Job.cancel()` to stop a job that has not started yet (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size`; use `len(queue)` instead (#420)

### Fixed
- Fix workers that hung on `SIGTERM` while a job ran, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument, so jobs ran at UTC (#403)
- Fix memory leak where results were kept forever if `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` off-by-one; retries=3 means at most four runs (#411)
- Fix `RedisBackend` not releasing connections after timeouts, thanks @rvdb (#414)
