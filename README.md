# One big CLAUDE.md vs a folder of stages

A small, rerunnable test of one claim from *Interpretable Context Methodology* (Van Clief and McDermott, arXiv:2603.16021): that an agent does better work when each step of a job reads only its own folder of Markdown, instead of one long instruction file. The paper says no controlled comparison exists (§4.6). This is one, on one job.

## The job

Claude Code writes the 2.4.0 release notes for `tinyqueue`, a made-up Python library: 33 commits and 22 issues, with 7 traps (a reverted feature, a fix for a bug that never shipped, an internal change, a docs change, a CI change, an open issue, and one planned for 2.5.0). Plain Python scores each run on about 90 checks: every shipped change listed once in the right section, no trap listed, bullet style, contributor credits, format. No model judges anything.

## The setups

The release rules are the same text, word for word, in every setup.

| Arm | Setup | Built in |
|---|---|---|
| A | One CLAUDE.md with the release rules (~3k tokens) | `workspace-mono/` |
| A2 | One CLAUDE.md that also holds four other jobs with clashing rules (~29k tokens) | `workspace-mono-big/` |
| B | The ICM folder, one session | `workspace-folder/` |
| C | The ICM folder, a fresh session per stage | `workspace-folder/` |
| C2 | C with one line of the stage 01 card fixed | `workspace-folder-v2/` |

## What happened

On Sonnet 5.5 every arm scored 99.9 to 100. On Haiku 5.5, A, A2 and B scored 99.6 to 99.7 and C dropped to 96.6: it left out 20 thank-yous to outside contributors, because the maintainer list lived only in stage 01's files and stage 02's card never pointed to it. One added line in the stage 01 card (C2) brought it to 99.7 with no credits missing.

So at this size the folder didn't make the model better; this job sits near the ceiling for both models. What the folder did give was a visible hand-off between stages, which is where the failure was found and fixed. Tables, failure counts, the cause and the limits are in [`RESULTS.md`](RESULTS.md). The plan, written before the first run and amended with dates, is in [`PLAN.md`](PLAN.md).

## Run it

You need Python 3 and [Claude Code](https://docs.claude.com/en/docs/claude-code) logged in.

```bash
python3 build_fixture.py              # regenerates workspace-*/ and truth.json
python3 score.py runs/A-1/workspace   # re-score a recorded run
python3 summarize.py runs runs-haiku  # rebuild the results tables
RUNS_SUFFIX=-mine ./run.sh 1 5 A A2 B C        # your own runs into runs-mine/ (MODEL=haiku to switch)
```

`run.sh` copies each workspace into a scratch folder outside any repo and runs `claude -p` with user settings, hooks, plugins and MCP servers off, and only the Read, Write, Edit, Glob and Grep tools. Each call is capped at $3; the 20 Sonnet runs here, plus a pilot, cost about $3.80 in all.

## Notes

- Each recorded run keeps its workspace, its score and the usage numbers from Claude Code's JSON output (cost, tokens, turns, time, model). The agent's own messages and session ids are left out.
- The security issue's CVE id is `CVE-0000-00000`. The original fixture used an id that turned out to belong to a real, unrelated CVE; it was replaced everywhere, including the recorded outputs, and all 45 runs re-score the same.
