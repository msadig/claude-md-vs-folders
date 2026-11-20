Fixed | #401 | Worker hangs on SIGTERM while a job is running | hollis
Fixed | #403 | schedule() ignores the tz argument | sam-okafor
Added | #405 | Add Queue.drain() to wait until all jobs finish | tobiaslund
Fixed | #407 | Memory leak in the result cache | ana-p
Added | #409 | retry_backoff option on Worker | lena-ortiz
Fixed | #411 | Job.retries is off by one | sam-okafor
Breaking changes | #412 | Drop support for Python 3.9 | lena-ortiz
Fixed | #414 | RedisBackend does not release the connection after a timeout | rvdb
Added | #415 | Prometheus metrics endpoint | ana-p
Breaking changes | #418 | Rename Queue.put_nowait() to Queue.try_put() | lena-ortiz
Deprecated | #420 | Deprecate Queue.size in favour of len(queue) | sam-okafor
Added | #422 | Job.cancel() for queued jobs | lena-ortiz
Added | #427 | Redis Sentinel support in RedisBackend | dkowal
Security | #431 | Pickle payloads deserialized without an allow-list (CVE-0000-00000) | mira-k
