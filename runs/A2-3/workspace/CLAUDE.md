# tinyqueue release workspace

This workspace prepares the release notes for tinyqueue, a Python job-queue library.
Raw inputs are in `inputs/` (git log and issue export). Never edit them.
This file holds every workflow in this repo. For release notes, do the three steps of the release-notes workflow in order (extract, draft, publish). File paths inside the steps refer to sections of this file; write every output file to `output/`.

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

# Workflow: docs site

Used when editing pages under docs/. Not used for release notes.

## Rules for docs pages
- In docs prose, name methods without the class prefix after first mention: write `try_put()` once the page has introduced `Queue`.
- Every page starts with a one-sentence summary, then a runnable example.
- Headings in sentence case. Code samples must run on Python 3.10.

## Page plan

### Getting started

The getting started page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Queues

The queues page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Workers

The workers page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Jobs

The jobs page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Scheduling

The scheduling page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Retries

The retries page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Results

The results page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Redis backend

The redis backend page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Memory backend

The memory backend page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Metrics

The metrics page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Command line

The command line page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Testing

The testing page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Deployment

The deployment page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Security

The security page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Upgrading

The upgrading page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### FAQ

The faq page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Getting started

The getting started page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Queues

The queues page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Workers

The workers page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Jobs

The jobs page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Scheduling

The scheduling page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Retries

The retries page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Results

The results page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Redis backend

The redis backend page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Memory backend

The memory backend page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Metrics

The metrics page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Command line

The command line page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Testing

The testing page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Deployment

The deployment page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Security

The security page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Upgrading

The upgrading page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### FAQ

The faq page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Getting started

The getting started page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Queues

The queues page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Workers

The workers page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Jobs

The jobs page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Scheduling

The scheduling page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Retries

The retries page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Results

The results page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Redis backend

The redis backend page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Memory backend

The memory backend page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Metrics

The metrics page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Command line

The command line page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Testing

The testing page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Deployment

The deployment page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Security

The security page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Upgrading

The upgrading page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### FAQ

The faq page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Getting started

The getting started page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Queues

The queues page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Workers

The workers page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Jobs

The jobs page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Scheduling

The scheduling page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Retries

The retries page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Results

The results page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Redis backend

The redis backend page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Memory backend

The memory backend page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Metrics

The metrics page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Command line

The command line page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Testing

The testing page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Deployment

The deployment page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Security

The security page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Upgrading

The upgrading page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### FAQ

The faq page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Getting started

The getting started page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Queues

The queues page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Workers

The workers page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Jobs

The jobs page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Scheduling

The scheduling page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Retries

The retries page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Results

The results page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Redis backend

The redis backend page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Memory backend

The memory backend page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Metrics

The metrics page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Command line

The command line page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Testing

The testing page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Deployment

The deployment page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Security

The security page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### Upgrading

The upgrading page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.

### FAQ

The faq page explains the concept in two paragraphs, gives one complete example, lists the options in a table (name, default, what it does), and ends with 'See also' links to two related pages. Keep examples under 25 lines. When an option was added in a recent version, note it with 'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.


# Workflow: release notes


<!-- from _config/release.md -->
# Release

- Version: 2.4.0
- Release date: 2026-11-02
- Previous version: 2.3.0

<!-- from _config/voice.md -->
# Voice

- Plain, direct, present tense where possible. Say what changed for the user, not how the code changed.
- Prefer the user's words: "jobs", "queue", "worker". Avoid internal names (registry, backend plumbing) unless the user touches them.
- Write "deprecated", never "obsolete". Write "removed", never "killed".
- One idea per bullet. If a bullet needs "and", it is probably two changes or too much detail.

<!-- from stages/01_extract/CONTEXT.md -->
# Stage 01: extract

## Inputs
- Layer 4 (working): `../../inputs/git-log.txt`, `../../inputs/issues.json`
- Layer 3 (reference): `references/inclusion-rules.md`
- Layer 3 (reference): `../../_config/release.md`

## Process
Go through every issue referenced in the git log and decide, with the inclusion rules, whether it ships in this release and in which section.

## Outputs
- `output/changes.md`: one line per shipped change: `<section> | #<number> | <issue title> | <issue author>`

<!-- from stages/01_extract/references/inclusion-rules.md -->
# Inclusion rules

1. Only issues in milestone `2.4.0` with state `closed` ship.
2. Leave out issues labelled `internal`, `docs`, `ci` or `test`: they have no user-facing change.
3. Leave out any change that was reverted before the release (look for `Revert` commits in the log).
4. Leave out fixes for bugs that were introduced in this same release and never shipped to users. The issue body says so.
5. One entry per issue, however many commits reference it (cherry-picks and follow-up commits are the same change).
6. Section, by the first matching label: `breaking` -> Breaking changes, `security` -> Security, `feature` -> Added, `deprecation` -> Deprecated, `bug` -> Fixed.
7. Maintainers: lena-ortiz, sam-okafor. Anyone else who opened a shipped issue is an external contributor.

<!-- from stages/02_draft/CONTEXT.md -->
# Stage 02: draft

## Inputs
- Layer 4 (working): `../01_extract/output/changes.md`, `../../inputs/issues.json` (for detail only)
- Layer 3 (reference): `references/style-guide.md`, `references/api-reference.md`
- Layer 3 (reference): `../../_config/voice.md`

## Process
Write one bullet per change, following the style guide exactly. Do not add or drop changes.

## Outputs
- `output/bullets.md`: the bullets grouped under their section headings

<!-- from stages/02_draft/references/style-guide.md -->
# Style guide for changelog bullets

Each bullet is one line: `- <text> (#<issue>)`.

1. `<text>` is at most 14 words.
2. `<text>` starts with a capital letter and does not end with a full stop.
3. If the issue was opened by an external contributor, end `<text>` with `, thanks @<handle>` (their issue author handle, counted outside the 14 words).
4. Name API items in backticks, exactly as in the Names list of the API reference, with the class prefix: `Queue.try_put()`, not `try_put()`. Put nothing else in backticks.
5. Never use these words: simply, just, easily, seamless, seamlessly, robust, leverage, powerful.
6. No emoji.
7. Write the product name as `tinyqueue`, all lower case, if you mention it at all.
8. Every breaking change gets one sub-bullet under it, indented two spaces: `  - Migration: <what to change>`.
9. The security bullet includes the CVE id from the issue title.

<!-- from stages/02_draft/references/api-reference.md -->
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

<!-- from stages/03_publish/CONTEXT.md -->
# Stage 03: publish

## Inputs
- Layer 4 (working): `../02_draft/output/bullets.md`
- Layer 3 (reference): `references/format.md`, `references/changelog-history.md`
- Layer 3 (reference): `../../_config/release.md`

## Process
Assemble the changelog entry and the JSON summary, following the format rules. Check that the counts match.

## Outputs
- `output/CHANGELOG-2.4.0.md`
- `output/release.json`

<!-- from stages/03_publish/references/format.md -->
# Format of the changelog entry

1. The first line is exactly `## [2.4.0] - 2026-11-02`.
2. Then the sections, in this order, each as `### <Section>`, leaving out empty ones: Breaking changes, Security, Added, Deprecated, Fixed.
3. Bullets as written in stage 02, unchanged.
4. `release.json` has exactly these keys:
   - `version`: "2.4.0"
   - `date`: "2026-11-02"
   - `counts`: an object mapping each section name used to its number of bullets
   - `issues`: every issue number in the entry, as integers, sorted ascending
5. The counts and issue list in `release.json` must match the Markdown entry exactly.
6. Older entries in the history use an older format (for example `### Bug fixes`). Follow these rules, not the old entries.

<!-- from stages/03_publish/references/changelog-history.md -->
# Changelog history (older entries, for reference)

## [2.3.0] - 2026-08-14

### Added
- `Queue.get()` accepts a timeout, thanks @rvdb (#371)
- Worker heartbeats every 10 seconds (#366)

### Fixed
- Jobs scheduled across a DST change ran an hour late (#368)
- `RedisBackend` retried forever on auth errors, thanks @dkowal (#373)

## [2.2.0] - 2026-06-02

### Deprecated
- Positional `ttl` argument on `Queue` (#341)

### Fixed
- Worker crashed on jobs returning generators, thanks @hollis (#344)

## [2.1.0] - 2026-03-20

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.

## [2.0.0] - 2026-01-11

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.

## [1.9.0] - 2025-10-30

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.

## [1.8.0] - 2025-08-01

### New features
- TinyQueue now supports job priorities, which makes it easy to run urgent work first.
- Added a simple way to inspect failed jobs from the command line.

### Bug fixes
- Fixed a robust handling issue where the worker would just stop polling after a network blip.
- Fixed: results were not cleaned up when a job was cancelled during startup.


# Workflow: release announcements (social)

Used when writing the release post for X, Mastodon and LinkedIn. Not the changelog.

## Rules for announcements
- Write the brand as TinyQueue (camel case) in announcements.
- Up to 25 words per bullet; lead with the user benefit.
- Credit contributors as 'shout-out to @handle'.
- End the post with 🚀 and a link to the changelog.
- Highlight at most three changes; never list fixes.

## Past announcements (for tone)

### TinyQueue 2.3.0

TinyQueue 2.3.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.2.0

TinyQueue 2.2.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.1.0

TinyQueue 2.1.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.0.0

TinyQueue 2.0.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.9.0

TinyQueue 1.9.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.8.0

TinyQueue 1.8.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.7.0

TinyQueue 1.7.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.6.0

TinyQueue 1.6.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.3.0

TinyQueue 2.3.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.2.0

TinyQueue 2.2.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.1.0

TinyQueue 2.1.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.0.0

TinyQueue 2.0.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.9.0

TinyQueue 1.9.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.8.0

TinyQueue 1.8.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.7.0

TinyQueue 1.7.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.6.0

TinyQueue 1.6.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.3.0

TinyQueue 2.3.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.2.0

TinyQueue 2.2.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.1.0

TinyQueue 2.1.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.0.0

TinyQueue 2.0.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.9.0

TinyQueue 1.9.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.8.0

TinyQueue 1.8.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.7.0

TinyQueue 1.7.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.6.0

TinyQueue 1.6.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.3.0

TinyQueue 2.3.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.2.0

TinyQueue 2.2.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.1.0

TinyQueue 2.1.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.0.0

TinyQueue 2.0.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.9.0

TinyQueue 1.9.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.8.0

TinyQueue 1.8.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.7.0

TinyQueue 1.7.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.6.0

TinyQueue 1.6.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.3.0

TinyQueue 2.3.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.2.0

TinyQueue 2.2.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.1.0

TinyQueue 2.1.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.0.0

TinyQueue 2.0.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.9.0

TinyQueue 1.9.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.8.0

TinyQueue 1.8.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.7.0

TinyQueue 1.7.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.6.0

TinyQueue 1.6.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.3.0

TinyQueue 2.3.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.2.0

TinyQueue 2.2.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.1.0

TinyQueue 2.1.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 2.0.0

TinyQueue 2.0.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.9.0

TinyQueue 1.9.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.8.0

TinyQueue 1.8.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.7.0

TinyQueue 1.7.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

### TinyQueue 1.6.0

TinyQueue 1.6.0 is out! Faster workers, friendlier errors and a few long-requested features. Huge shout-out to everyone who reported bugs and sent pull requests this cycle. Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀

# Workflow: on-call runbook

Used when an alert fires on the hosted demo. Not used for release notes.

## Alert: Queue depth above 10k

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Worker heartbeat missing

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Redis memory above 80%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Job failure rate above 5%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Metrics endpoint down

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Scheduler drift above 60s

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Result cache above 1 GB

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Sentinel failover

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Queue depth above 10k

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Worker heartbeat missing

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Redis memory above 80%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Job failure rate above 5%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Metrics endpoint down

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Scheduler drift above 60s

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Result cache above 1 GB

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Sentinel failover

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Queue depth above 10k

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Worker heartbeat missing

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Redis memory above 80%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Job failure rate above 5%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Metrics endpoint down

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Scheduler drift above 60s

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Result cache above 1 GB

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Sentinel failover

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Queue depth above 10k

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Worker heartbeat missing

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Redis memory above 80%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Job failure rate above 5%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Metrics endpoint down

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Scheduler drift above 60s

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Result cache above 1 GB

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Sentinel failover

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Queue depth above 10k

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Worker heartbeat missing

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Redis memory above 80%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Job failure rate above 5%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Metrics endpoint down

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Scheduler drift above 60s

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Result cache above 1 GB

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Sentinel failover

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Queue depth above 10k

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Worker heartbeat missing

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Redis memory above 80%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Job failure rate above 5%

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Metrics endpoint down

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Scheduler drift above 60s

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Result cache above 1 GB

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.

## Alert: Sentinel failover

1. Acknowledge in the pager within 5 minutes.
2. Check the dashboard for the last hour and note when it started.
3. Look at recent deploys; roll back the last one if it lines up.
4. If the cause is unclear after 20 minutes, page the second on-call.
5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.
