"""Other jobs the same repo's agent does. They sit in the big CLAUDE.md (arm A2) or in their own
workflow folders (arms B, C), where the release stages never read them. Some rules conflict with the
release rules on purpose, as they do in real repos (social posts allow emoji and 'TinyQueue')."""

QUESTIONS = [
    ("How do I retry a failed job?", "Set retries on the job and, if you want spacing, retry_backoff on the worker."),
    ("Why is my worker not picking up jobs?", "Check the queue name matches, the backend URL is the same, and the worker is not paused."),
    ("Can I run jobs at a fixed time?", "Use schedule with an aware datetime; pass tz when you give a naive one."),
    ("How do I see queue depth?", "Run tq stats, or scrape the metrics endpoint."),
    ("Is Redis required?", "No. The memory backend works for tests and single-process apps."),
    ("How do I stop a worker cleanly?", "Send SIGTERM. The running job finishes, then the worker exits."),
    ("Where do results go?", "Into the backend, kept for result_ttl seconds."),
    ("Can I cancel a job?", "Yes, before it starts, with cancel on the job."),
    ("How many workers should I run?", "Start with one per CPU core for CPU-bound work; more for IO-bound work."),
    ("Does tinyqueue support async functions?", "Not yet; an async API is being designed."),
    ("How do I pass large payloads?", "Store the data elsewhere and pass a key; payloads are pickled."),
    ("Why are my jobs running twice?", "A worker died mid-job and visibility_timeout expired; make jobs idempotent."),
    ("How do I connect through Sentinel?", "Pass sentinels and service_name to the Redis backend."),
    ("Can I prioritise jobs?", "Yes, with the priority argument on put."),
    ("How do I test code that queues jobs?", "Use the memory backend and drain the queue at the end of the test."),
    ("What Python versions are supported?", "Python 3.10 and newer."),
    ("How do I upgrade safely?", "Read the changelog's breaking changes, upgrade workers first, then producers."),
    ("Why do I get a pickling error?", "The callable must be importable at module level; lambdas and closures fail."),
    ("Can I limit concurrency per queue?", "Run a dedicated worker for that queue with the concurrency you want."),
    ("Where are the logs?", "Workers log to stderr; set log_level to change the detail."),
]

def support():
    out = ["# Workflow: support replies", "",
           "Used when answering GitHub Discussions and email. Not used for release notes.", "",
           "## Tone", "- Warm and short. Greet the person by name. Sign off with 'Happy queueing!'.",
           "- Emoji are fine in support replies (one per reply at most).", "- Link the docs page instead of pasting long code.", "",
           "## Canned answers", ""]
    for i, (q, a) in enumerate(QUESTIONS * 5):
        out += [f"### Q{i + 1}. {q}", "", a, "",
                "If the person is on an old version, ask them to upgrade first and to include the output of `tq stats` "
                "and their Python version. If they report a crash, ask for the full traceback and the backend they use. "
                "Never promise a release date. If it is a bug, open an issue, label it `bug`, and link it in the reply.", ""]
    return "\n".join(out)

PAGES = ["Getting started", "Queues", "Workers", "Jobs", "Scheduling", "Retries", "Results", "Redis backend",
         "Memory backend", "Metrics", "Command line", "Testing", "Deployment", "Security", "Upgrading", "FAQ"]

def docs():
    out = ["# Workflow: docs site", "", "Used when editing pages under docs/. Not used for release notes.", "",
           "## Rules for docs pages",
           "- In docs prose, name methods without the class prefix after first mention: write `try_put()` once the page has introduced `Queue`.",
           "- Every page starts with a one-sentence summary, then a runnable example.",
           "- Headings in sentence case. Code samples must run on Python 3.10.", "",
           "## Page plan", ""]
    for p in PAGES * 5:
        out += [f"### {p}", "",
                f"The {p.lower()} page explains the concept in two paragraphs, gives one complete example, lists the options "
                "in a table (name, default, what it does), and ends with 'See also' links to two related pages. "
                "Keep examples under 25 lines. When an option was added in a recent version, note it with "
                "'New in 2.x' in the options table, not in the prose. Screenshots are not used; output is shown as text.", ""]
    return "\n".join(out)

def social():
    out = ["# Workflow: release announcements (social)", "",
           "Used when writing the release post for X, Mastodon and LinkedIn. Not the changelog.", "",
           "## Rules for announcements",
           "- Write the brand as TinyQueue (camel case) in announcements.",
           "- Up to 25 words per bullet; lead with the user benefit.",
           "- Credit contributors as 'shout-out to @handle'.",
           "- End the post with 🚀 and a link to the changelog.",
           "- Highlight at most three changes; never list fixes.", "",
           "## Past announcements (for tone)", ""]
    for v in ["2.3.0", "2.2.0", "2.1.0", "2.0.0", "1.9.0", "1.8.0", "1.7.0", "1.6.0"] * 6:
        out += [f"### TinyQueue {v}", "",
                f"TinyQueue {v} is out! Faster workers, friendlier errors and a few long-requested features. "
                "Huge shout-out to everyone who reported bugs and sent pull requests this cycle. "
                "Upgrade with pip and tell us what you build. Full notes in the changelog. 🚀", ""]
    return "\n".join(out)

def oncall():
    out = ["# Workflow: on-call runbook", "", "Used when an alert fires on the hosted demo. Not used for release notes.", ""]
    alerts = ["Queue depth above 10k", "Worker heartbeat missing", "Redis memory above 80%", "Job failure rate above 5%",
              "Metrics endpoint down", "Scheduler drift above 60s", "Result cache above 1 GB", "Sentinel failover"]
    for a in alerts * 6:
        out += [f"## Alert: {a}", "", "1. Acknowledge in the pager within 5 minutes.",
                "2. Check the dashboard for the last hour and note when it started.",
                "3. Look at recent deploys; roll back the last one if it lines up.",
                "4. If the cause is unclear after 20 minutes, page the second on-call.",
                "5. Write a short incident note in incidents/ with what you saw, what you did, and what to change.", ""]
    return "\n".join(out)

WORKFLOWS = {"support": support, "docs-site": docs, "social": social, "oncall": oncall}
