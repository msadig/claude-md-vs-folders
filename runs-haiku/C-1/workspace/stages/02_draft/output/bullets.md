## Fixed

- Workers now exit on `SIGTERM` while a job is running (#401)
- `schedule()` now respects the tz argument (#403)
- Results are no longer kept forever when `result_ttl` is unset (#407)
- `Job.retries` is no longer off by one (#411)
- `RedisBackend` releases connections after a timeout, fixing pool exhaustion (#414)

## Added

- `Queue.drain()` waits until all queued and running jobs finish (#405)
- `retry_backoff` option on `Worker` adds exponential backoff between retries, off by default (#409)
- `metrics_server()` serves a Prometheus endpoint for queue depth, durations and failures (#415)
- `Job.cancel()` cancels jobs that have not started yet (#422)
- `RedisBackend` supports Redis Sentinel connections (#427)

## Breaking changes

- Drop support for Python 3.9 (#412)
  - Migration: Upgrade to Python 3.10 or newer.
- `Queue.put_nowait()` is renamed to `Queue.try_put()`, which returns False when full (#418)
  - Migration: Replace calls to `Queue.put_nowait()` with `Queue.try_put()`.

## Deprecated

- `Queue.size` is deprecated; use `len(queue)` instead (#420)

## Security

- Restrict job payload unpickling to `serializer_allowlist` classes (CVE-0000-00000)
