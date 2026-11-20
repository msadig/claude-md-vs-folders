## [2.4.0] - 2026-11-02

### Breaking changes
- Drop Python 3.9 support (#412)
  - Migration: Use Python 3.10 or newer.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace `Queue.put_nowait()` calls with `Queue.try_put()`.

### Security
- Fix code execution from crafted job payloads, CVE-0000-00000, thanks @mira-k (#431)

### Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential retry delays (#409)
- Add `metrics_server()` to serve Prometheus queue and job metrics, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

### Deprecated
- Mark `Queue.size` as deprecated; use `len(queue)` instead (#420)

### Fixed
- Fix workers hanging on `SIGTERM` while a job runs, thanks @hollis (#401)
- Fix `schedule()` ignoring its timezone argument (#403)
- Fix memory leak when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` count being off by one (#411)
- Fix `RedisBackend` leaking connections after timeouts, thanks @rvdb (#414)
