### Breaking changes
- Drop support for Python 3.9; minimum is now Python 3.10 (#412)
  - Migration: upgrade to Python 3.10 or newer before installing 2.4.0.
- Rename `Queue.put_nowait()` to `Queue.try_put()`, which returns False when full (#418)
  - Migration: replace `Queue.put_nowait()` calls with `Queue.try_put()`.

### Security
- Fix CVE-0000-00000: job payloads may only unpickle `serializer_allowlist` classes, thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential retry delays (#409)
- Add `metrics_server()` that serves Prometheus queue depth, durations, failures, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel queued jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Deprecate `Queue.size` in favor of `len(queue)` (#420)

### Fixed
- `Worker` exits on `SIGTERM` while a job runs instead of hanging, thanks @hollis (#401)
- `schedule()` respects the tz argument instead of running at UTC (#403)
- Fix memory leak: results evicted after 24 hours when `result_ttl` is unset, thanks @ana-p (#407)
- Fix off-by-one in `Job.retries`: retries=3 means at most four runs (#411)
- `RedisBackend` releases its connection after a timeout, fixing pool exhaustion, thanks @rvdb (#414)
