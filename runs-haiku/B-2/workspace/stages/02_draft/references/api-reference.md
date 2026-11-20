# tinyqueue API reference (2.4.0)

tinyqueue is a small job queue for Python 3.10+. Jobs are pickled callables stored in a backend (memory or Redis) and run by workers.

## Queue

A named queue. `Queue(name, backend=None, result_ttl=None)`.

## Queue.put()

Add a job. Blocks when the queue has a max size and is full.

## Queue.try_put()

Add a job without blocking. Returns False when the queue is full. New name in 2.4.0.

## Queue.put_nowait()

Removed in 2.4.0. Use Queue.try_put().

## Queue.get()

Take the next job. Used by workers; rarely called directly.

## Queue.drain()

Block until every queued and running job has finished. Takes an optional timeout.

## Queue.size

Number of queued jobs. Deprecated in 2.4.0: use len(queue).

## len(queue)

Number of queued jobs.

## QueueFull

Raised by Queue.put() with block=False when the queue is full.

## Worker

Runs jobs from one or more queues. `Worker(queues, concurrency=1, retry_backoff=None)`.

## retry_backoff

Worker option. Base delay in seconds for exponential backoff between retries. None disables it.

## Job

A queued call. Has an id, status, result and retries.

## Job.cancel()

Cancel a job that has not started. Returns False if it is already running or done.

## Job.retries

How many times a failed job is retried. retries=3 means at most 4 runs.

## schedule()

Queue a job for later: `schedule(func, at=datetime, tz=None)`.

## RedisBackend

Redis storage. Accepts `url` or `sentinels=[(host, port), ...]` with `service_name`.

## metrics_server()

Start a Prometheus metrics endpoint on a port: queue depth, job durations, failures.

## serializer_allowlist

Backend option. Only these classes may be unpickled from job payloads. On by default since 2.4.0.

## result_ttl

Queue option. Seconds to keep job results. None used to mean forever; since 2.4.0 results are evicted after 24 hours.

## SIGTERM

Workers finish the running job, then exit.

## tq stats

Command line: print queue depth and worker status.

## Configuration

### concurrency

Default and behaviour of `concurrency` are documented in the user guide, section 3. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### poll_interval

Default and behaviour of `poll_interval` are documented in the user guide, section 4. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### visibility_timeout

Default and behaviour of `visibility_timeout` are documented in the user guide, section 5. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### max_size

Default and behaviour of `max_size` are documented in the user guide, section 6. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### prefetch

Default and behaviour of `prefetch` are documented in the user guide, section 7. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### heartbeat

Default and behaviour of `heartbeat` are documented in the user guide, section 8. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### log_level

Default and behaviour of `log_level` are documented in the user guide, section 9. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

### job_timeout

Default and behaviour of `job_timeout` are documented in the user guide, section 10. Changing it affects every worker that reads the same queue, so set it once per deployment and keep it in version control.

## Names

These are the only names that may appear in backticks in the changelog:

- `Queue`
- `Queue.put()`
- `Queue.try_put()`
- `Queue.put_nowait()`
- `Queue.get()`
- `Queue.drain()`
- `Queue.size`
- `len(queue)`
- `QueueFull`
- `Worker`
- `retry_backoff`
- `Job`
- `Job.cancel()`
- `Job.retries`
- `schedule()`
- `RedisBackend`
- `metrics_server()`
- `serializer_allowlist`
- `result_ttl`
- `SIGTERM`
- `tq stats`
