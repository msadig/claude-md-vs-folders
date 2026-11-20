## [2.4.0] - 2026-11-02

### Breaking changes
- Python 3.9 is no longer supported; the minimum is Python 3.10 (#412)
  - Migration: Upgrade to Python 3.10 or newer before installing 2.4.0.
- `Queue.put_nowait()` is removed; use `Queue.try_put()` instead (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`.

### Security
- Fixes CVE-0000-00000 by restricting job payload classes with `serializer_allowlist`, thanks @mira-k (#431)

### Added
- `Queue.drain()` waits until all jobs have finished, thanks @tobiaslund (#405)
- New `retry_backoff` option on `Worker` sets exponential delay between retries, off by default (#409)
- New `metrics_server()` serves queue depth, job durations and failures, thanks @ana-p (#415)
- `Job.cancel()` cancels a job that has not started yet (#422)
- `RedisBackend` now connects through Redis Sentinel, thanks @dkowal (#427)

### Deprecated
- `Queue.size` is deprecated; use `len(queue)` instead (#420)

### Fixed
- `Worker` exits on `SIGTERM` after the running job finishes, thanks @hollis (#401)
- `schedule()` now respects the tz argument instead of always using UTC (#403)
- Results are evicted after 24 hours when `result_ttl` is unset, not kept forever, thanks @ana-p (#407)
- Fixes an off-by-one error in `Job.retries` (#411)
- `RedisBackend` no longer exhausts its connection pool after timeouts, thanks @rvdb (#414)
