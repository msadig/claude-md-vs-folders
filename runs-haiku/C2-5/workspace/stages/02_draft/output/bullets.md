## Breaking changes
- Drop support for Python 3.9 (#412)
  - Migration: Use Python 3.10 or newer.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace `Queue.put_nowait()` calls with `Queue.try_put()`.

## Security
- Crafted job payloads can no longer run code on workers (CVE-0000-00000), thanks @mira-k (#431)

## Added
- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option on `Worker` for exponential retry delays (#409)
- Add `metrics_server()` endpoint for Prometheus metrics, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

## Deprecated
- Deprecate `Queue.size` in favour of `len(queue)` (#420)

## Fixed
- Fix `Worker` hanging on `SIGTERM` while a job runs, thanks @hollis (#401)
- Fix `schedule()` so the tz argument is respected (#403)
- Fix memory leak where results were kept forever without `result_ttl`, thanks @ana-p (#407)
- Fix off-by-one in `Job.retries` run count (#411)
- Fix `RedisBackend` leaking connections after timeouts, thanks @rvdb (#414)
