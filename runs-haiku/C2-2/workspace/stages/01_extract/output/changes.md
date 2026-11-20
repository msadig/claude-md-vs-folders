Breaking changes | #412 | Drop support for Python 3.9 | lena-ortiz | maintainer
Breaking changes | #418 | Rename Queue.put_nowait() to Queue.try_put() | lena-ortiz | maintainer
Security | #431 | Pickle payloads deserialized without an allow-list (CVE-0000-00000) | mira-k | external
Added | #405 | Add Queue.drain() to wait until all jobs finish | tobiaslund | external
Added | #409 | retry_backoff option on Worker | lena-ortiz | maintainer
Added | #415 | Prometheus metrics endpoint | ana-p | external
Added | #422 | Job.cancel() for queued jobs | lena-ortiz | maintainer
Added | #427 | Redis Sentinel support in RedisBackend | dkowal | external
Deprecated | #420 | Deprecate Queue.size in favour of len(queue) | sam-okafor | maintainer
Fixed | #401 | Worker hangs on SIGTERM while a job is running | hollis | external
Fixed | #403 | schedule() ignores the tz argument | sam-okafor | maintainer
Fixed | #407 | Memory leak in the result cache | ana-p | external
Fixed | #411 | Job.retries is off by one | sam-okafor | maintainer
Fixed | #414 | RedisBackend does not release the connection after a timeout | rvdb | external
