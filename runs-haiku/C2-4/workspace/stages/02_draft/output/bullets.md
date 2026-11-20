## Breaking changes

- Python 3.9 is no longer supported (#412)
  - Migration: use Python 3.10 or newer.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: call `Queue.try_put()` instead of `Queue.put_nowait()`.

## Security

- Fix code execution via crafted job payloads (CVE-0000-00000), thanks @mira-k (#431)

## Added

- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` for exponential backoff between retries (#409)
- Add a Prometheus metrics endpoint with `metrics_server()`, thanks @ana-p (#415)
- Add `Job.cancel()` for queued jobs (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

## Deprecated

- Deprecate `Queue.size` in favor of `len(queue)` (#420)

## Fixed

- Fix `Worker` hanging on `SIGTERM` while a job is running, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Fix memory leak in result cache when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` off by one: retries=3 means at most four runs (#411)
- Fix `RedisBackend` not releasing connections after a timeout, thanks @rvdb (#414)
