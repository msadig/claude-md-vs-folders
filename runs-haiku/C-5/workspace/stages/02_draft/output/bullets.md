## Breaking changes
- Drop support for Python 3.9 (#412)
  - Migration: Upgrade to Python 3.10 or newer
- Rename `Queue.put_nowait()` to `Queue.try_put()` (#418)
  - Migration: Call `Queue.try_put()` instead; it returns False when the queue is full

## Added
- Add `Queue.drain()` to wait until all jobs finish (#405)
- Add `retry_backoff` option to `Worker` for exponential retry backoff (#409)
- Add `metrics_server()` for a Prometheus metrics endpoint (#415)
- Add `Job.cancel()` to cancel jobs that have not started (#422)
- Add Redis Sentinel support to `RedisBackend` (#427)

## Fixed
- `Worker` now exits on `SIGTERM` after its running job finishes (#401)
- `schedule()` now honors the tz argument (#403)
- Results are evicted after 24 hours when `result_ttl` is unset (#407)
- Fix off-by-one in `Job.retries`; three retries means at most four runs (#411)
- `RedisBackend` releases its connection after a timeout (#414)

## Deprecated
- `Queue.size` is deprecated; use `len(queue)` instead (#420)

## Security
- Fix code execution from crafted job payloads, CVE-0000-00000 (#431)
