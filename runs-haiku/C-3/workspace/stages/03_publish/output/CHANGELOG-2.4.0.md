## [2.4.0] - 2026-11-02

### Breaking changes

- Drop support for Python 3.9 (#412)
  - Migration: Install Python 3.10 or newer.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Call `Queue.try_put()` instead of `Queue.put_nowait()`.

### Security

- Fix crafted job payloads running code on workers (CVE-0000-00000) (#431)

### Added

- Add `Queue.drain()` to wait until all jobs finish (#405)
- Add `retry_backoff` option to Worker for exponential retry delays (#409)
- Add Prometheus metrics endpoint via `metrics_server()` (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend` (#427)

### Deprecated

- Deprecate `Queue.size` in favour of `len(queue)` (#420)

### Fixed

- Fix worker hanging on `SIGTERM` while a job is running (#401)
- Fix `schedule()` ignoring its timezone argument (#403)
- Fix memory leak in the result cache when `result_ttl` is unset (#407)
- Fix `Job.retries` off by one (#411)
- Fix `RedisBackend` not releasing connections after a timeout (#414)
