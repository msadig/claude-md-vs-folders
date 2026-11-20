## Breaking changes

- Drop support for Python 3.9 (#412)
  - Migration: Use Python 3.10 or later.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace `Queue.put_nowait()` calls with `Queue.try_put()`, which returns False when full.

## Security

- Pickle payloads are checked against `serializer_allowlist` by default (CVE-0000-00000), thanks @mira-k (#431)

## Added

- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential retry delays (#409)
- Add `metrics_server()` for Prometheus metrics: queue depth, job durations, failures, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

## Deprecated

- `Queue.size` is deprecated; use `len(queue)` instead (#420)

## Fixed

- Worker no longer hangs on `SIGTERM` while a job runs, thanks @hollis (#401)
- `schedule()` now respects the tz argument (#403)
- Fix memory leak when `result_ttl` is unset, thanks @ana-p (#407)
- Fix off-by-one error in `Job.retries` (#411)
- `RedisBackend` releases connections after a timeout, thanks @rvdb (#414)
