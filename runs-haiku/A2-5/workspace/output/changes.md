Breaking changes | #412 | Drop Python 3.9 support | lena-ortiz
Breaking changes | #418 | Rename Queue.put_nowait() to Queue.try_put() | lena-ortiz
Security | #431 | Pickle payloads deserialized without an allow-list (CVE-0000-00000) | mira-k
Added | #405 | Add Queue.drain() to wait until all jobs finish | tobiaslund
Added | #409 | retry_backoff option on Worker | lena-ortiz
Added | #415 | Prometheus metrics endpoint | ana-p
Added | #422 | Job.cancel() for queued jobs | lena-ortiz
Added | #427 | Redis Sentinel support in RedisBackend | dkowal
Deprecated | #420 | Deprecate Queue.size in favour of len(queue) | sam-okafor
Fixed | #401 | Worker hangs on SIGTERM while a job is running | hollis
Fixed | #403 | schedule() ignores the tz argument | sam-okafor
Fixed | #407 | Memory leak in the result cache | ana-p
Fixed | #411 | Job.retries is off by one | sam-okafor
Fixed | #414 | RedisBackend does not release the connection after a timeout | rvdb
