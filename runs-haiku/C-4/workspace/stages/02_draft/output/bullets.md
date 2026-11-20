## Breaking changes
- Drop support for Python 3.9 (#412)
  - Migration: use Python 3.10 or later
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: call `Queue.try_put()` instead of `Queue.put_nowait()`

## Security
- Fix code execution from crafted job payloads (CVE-0000-00000), thanks @mira-k (#431)

## Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential delay between retries (#409)
- Add Prometheus metrics endpoint via `metrics_server()`, thanks @ana-p (#415)
- Add `Job.cancel()` for queued jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

## Fixed
- Fix `Worker` hanging on SIGTERM while a job runs, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Fix memory leak where results stay forever when `result_ttl` is unset, thanks @ana-p (#407)
- Fix off-by-one error in `Job.retries` (#411)
- Fix `RedisBackend` exhausting its connection pool after timeouts, thanks @rvdb (#414)

## Deprecated
- Deprecate `Queue.size`; use `len(queue)` instead (#420)
