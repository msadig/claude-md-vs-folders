## Breaking changes

- Drop support for Python 3.9 (#412)
  - Migration: Upgrade to Python 3.10 or later.
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`, which returns False when the queue is full.

## Security

- Fix unsafe pickle deserialization of job payloads (CVE-0000-00000) with `serializer_allowlist`, thanks @mira-k (#431)

## Added

- Add `Queue.drain()` to wait until all jobs finish, thanks @tobiaslund (#405)
- Add `retry_backoff` option to `Worker` (#409)
- Add Prometheus metrics endpoint with `metrics_server()`, thanks @ana-p (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend`, thanks @dkowal (#427)

## Deprecated

- Deprecate `Queue.size` in favour of `len(queue)` (#420)

## Fixed

- Fix `Worker` hanging on `SIGTERM` while a job is running, thanks @hollis (#401)
- Fix `schedule()` ignoring the tz argument (#403)
- Fix memory leak in the result cache when `result_ttl` is unset, thanks @ana-p (#407)
- Fix `Job.retries` running jobs one extra time (#411)
- Fix `RedisBackend` not releasing connections after a timeout, thanks @rvdb (#414)
