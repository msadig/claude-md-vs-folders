# Workflow: support replies

Used when answering GitHub Discussions and email. Not used for release notes.

## Tone
- Warm and short. Greet the person by name. Sign off with 'Happy queueing!'.
- Emoji are fine in support replies (one per reply at most).
- Link the docs page instead of pasting long code.

## Canned answers

### Q1. How do I retry a failed job?

Set retries on the job and, if you want spacing, retry_backoff on the worker.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q2. Why is my worker not picking up jobs?

Check the queue name matches, the backend URL is the same, and the worker is not paused.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q3. Can I run jobs at a fixed time?

Use schedule with an aware datetime; pass tz when you give a naive one.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q4. How do I see queue depth?

Run tq stats, or scrape the metrics endpoint.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q5. Is Redis required?

No. The memory backend works for tests and single-process apps.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q6. How do I stop a worker cleanly?

Send SIGTERM. The running job finishes, then the worker exits.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q7. Where do results go?

Into the backend, kept for result_ttl seconds.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q8. Can I cancel a job?

Yes, before it starts, with cancel on the job.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q9. How many workers should I run?

Start with one per CPU core for CPU-bound work; more for IO-bound work.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q10. Does tinyqueue support async functions?

Not yet; an async API is being designed.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q11. How do I pass large payloads?

Store the data elsewhere and pass a key; payloads are pickled.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q12. Why are my jobs running twice?

A worker died mid-job and visibility_timeout expired; make jobs idempotent.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q13. How do I connect through Sentinel?

Pass sentinels and service_name to the Redis backend.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q14. Can I prioritise jobs?

Yes, with the priority argument on put.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q15. How do I test code that queues jobs?

Use the memory backend and drain the queue at the end of the test.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q16. What Python versions are supported?

Python 3.10 and newer.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q17. How do I upgrade safely?

Read the changelog's breaking changes, upgrade workers first, then producers.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q18. Why do I get a pickling error?

The callable must be importable at module level; lambdas and closures fail.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q19. Can I limit concurrency per queue?

Run a dedicated worker for that queue with the concurrency you want.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q20. Where are the logs?

Workers log to stderr; set log_level to change the detail.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q21. How do I retry a failed job?

Set retries on the job and, if you want spacing, retry_backoff on the worker.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q22. Why is my worker not picking up jobs?

Check the queue name matches, the backend URL is the same, and the worker is not paused.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q23. Can I run jobs at a fixed time?

Use schedule with an aware datetime; pass tz when you give a naive one.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q24. How do I see queue depth?

Run tq stats, or scrape the metrics endpoint.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q25. Is Redis required?

No. The memory backend works for tests and single-process apps.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q26. How do I stop a worker cleanly?

Send SIGTERM. The running job finishes, then the worker exits.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q27. Where do results go?

Into the backend, kept for result_ttl seconds.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q28. Can I cancel a job?

Yes, before it starts, with cancel on the job.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q29. How many workers should I run?

Start with one per CPU core for CPU-bound work; more for IO-bound work.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q30. Does tinyqueue support async functions?

Not yet; an async API is being designed.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q31. How do I pass large payloads?

Store the data elsewhere and pass a key; payloads are pickled.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q32. Why are my jobs running twice?

A worker died mid-job and visibility_timeout expired; make jobs idempotent.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q33. How do I connect through Sentinel?

Pass sentinels and service_name to the Redis backend.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q34. Can I prioritise jobs?

Yes, with the priority argument on put.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q35. How do I test code that queues jobs?

Use the memory backend and drain the queue at the end of the test.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q36. What Python versions are supported?

Python 3.10 and newer.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q37. How do I upgrade safely?

Read the changelog's breaking changes, upgrade workers first, then producers.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q38. Why do I get a pickling error?

The callable must be importable at module level; lambdas and closures fail.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q39. Can I limit concurrency per queue?

Run a dedicated worker for that queue with the concurrency you want.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q40. Where are the logs?

Workers log to stderr; set log_level to change the detail.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q41. How do I retry a failed job?

Set retries on the job and, if you want spacing, retry_backoff on the worker.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q42. Why is my worker not picking up jobs?

Check the queue name matches, the backend URL is the same, and the worker is not paused.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q43. Can I run jobs at a fixed time?

Use schedule with an aware datetime; pass tz when you give a naive one.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q44. How do I see queue depth?

Run tq stats, or scrape the metrics endpoint.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q45. Is Redis required?

No. The memory backend works for tests and single-process apps.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q46. How do I stop a worker cleanly?

Send SIGTERM. The running job finishes, then the worker exits.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q47. Where do results go?

Into the backend, kept for result_ttl seconds.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q48. Can I cancel a job?

Yes, before it starts, with cancel on the job.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q49. How many workers should I run?

Start with one per CPU core for CPU-bound work; more for IO-bound work.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q50. Does tinyqueue support async functions?

Not yet; an async API is being designed.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q51. How do I pass large payloads?

Store the data elsewhere and pass a key; payloads are pickled.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q52. Why are my jobs running twice?

A worker died mid-job and visibility_timeout expired; make jobs idempotent.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q53. How do I connect through Sentinel?

Pass sentinels and service_name to the Redis backend.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q54. Can I prioritise jobs?

Yes, with the priority argument on put.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q55. How do I test code that queues jobs?

Use the memory backend and drain the queue at the end of the test.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q56. What Python versions are supported?

Python 3.10 and newer.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q57. How do I upgrade safely?

Read the changelog's breaking changes, upgrade workers first, then producers.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q58. Why do I get a pickling error?

The callable must be importable at module level; lambdas and closures fail.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q59. Can I limit concurrency per queue?

Run a dedicated worker for that queue with the concurrency you want.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q60. Where are the logs?

Workers log to stderr; set log_level to change the detail.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q61. How do I retry a failed job?

Set retries on the job and, if you want spacing, retry_backoff on the worker.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q62. Why is my worker not picking up jobs?

Check the queue name matches, the backend URL is the same, and the worker is not paused.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q63. Can I run jobs at a fixed time?

Use schedule with an aware datetime; pass tz when you give a naive one.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q64. How do I see queue depth?

Run tq stats, or scrape the metrics endpoint.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q65. Is Redis required?

No. The memory backend works for tests and single-process apps.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q66. How do I stop a worker cleanly?

Send SIGTERM. The running job finishes, then the worker exits.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q67. Where do results go?

Into the backend, kept for result_ttl seconds.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q68. Can I cancel a job?

Yes, before it starts, with cancel on the job.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q69. How many workers should I run?

Start with one per CPU core for CPU-bound work; more for IO-bound work.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q70. Does tinyqueue support async functions?

Not yet; an async API is being designed.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q71. How do I pass large payloads?

Store the data elsewhere and pass a key; payloads are pickled.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q72. Why are my jobs running twice?

A worker died mid-job and visibility_timeout expired; make jobs idempotent.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q73. How do I connect through Sentinel?

Pass sentinels and service_name to the Redis backend.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q74. Can I prioritise jobs?

Yes, with the priority argument on put.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q75. How do I test code that queues jobs?

Use the memory backend and drain the queue at the end of the test.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q76. What Python versions are supported?

Python 3.10 and newer.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q77. How do I upgrade safely?

Read the changelog's breaking changes, upgrade workers first, then producers.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q78. Why do I get a pickling error?

The callable must be importable at module level; lambdas and closures fail.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q79. Can I limit concurrency per queue?

Run a dedicated worker for that queue with the concurrency you want.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q80. Where are the logs?

Workers log to stderr; set log_level to change the detail.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q81. How do I retry a failed job?

Set retries on the job and, if you want spacing, retry_backoff on the worker.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q82. Why is my worker not picking up jobs?

Check the queue name matches, the backend URL is the same, and the worker is not paused.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q83. Can I run jobs at a fixed time?

Use schedule with an aware datetime; pass tz when you give a naive one.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q84. How do I see queue depth?

Run tq stats, or scrape the metrics endpoint.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q85. Is Redis required?

No. The memory backend works for tests and single-process apps.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q86. How do I stop a worker cleanly?

Send SIGTERM. The running job finishes, then the worker exits.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q87. Where do results go?

Into the backend, kept for result_ttl seconds.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q88. Can I cancel a job?

Yes, before it starts, with cancel on the job.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q89. How many workers should I run?

Start with one per CPU core for CPU-bound work; more for IO-bound work.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q90. Does tinyqueue support async functions?

Not yet; an async API is being designed.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q91. How do I pass large payloads?

Store the data elsewhere and pass a key; payloads are pickled.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q92. Why are my jobs running twice?

A worker died mid-job and visibility_timeout expired; make jobs idempotent.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q93. How do I connect through Sentinel?

Pass sentinels and service_name to the Redis backend.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q94. Can I prioritise jobs?

Yes, with the priority argument on put.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q95. How do I test code that queues jobs?

Use the memory backend and drain the queue at the end of the test.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q96. What Python versions are supported?

Python 3.10 and newer.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q97. How do I upgrade safely?

Read the changelog's breaking changes, upgrade workers first, then producers.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q98. Why do I get a pickling error?

The callable must be importable at module level; lambdas and closures fail.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q99. Can I limit concurrency per queue?

Run a dedicated worker for that queue with the concurrency you want.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.

### Q100. Where are the logs?

Workers log to stderr; set log_level to change the detail.

If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` and their Python version. If they report a crash, ask for the full traceback and the backend they use. Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.
