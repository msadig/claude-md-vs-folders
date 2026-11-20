# Test plan: one big CLAUDE.md vs a folder of stages

Written 2026-11-18, **before any run**. The results go in `RESULTS.md`, and this file is not edited after the first run. Any later change is added at the bottom with a date.

## The question
The ICM paper (§4.6) says no controlled comparison exists between "everything in one context" and "each stage loads only its own files". Does the folder structure change the quality of the work on a real multi-step job?

## The job
Write the release notes for version 2.4.0 of **tinyqueue**, a fictional Python job-queue library. The input is a raw git log (about 45 commits) and an issue export (about 22 issues).

It's a good test job for four reasons:
- **It's multi-step:** decide what goes in, then write the bullets, then format and count.
- **It's scored by code, with no AI judge.** The ground truth is known because we wrote the data.
- **It has traps** that need a rule to be followed exactly:
  - a reverted feature;
  - a fix for a bug that never shipped;
  - internal, docs and CI issues;
  - an open issue;
  - an issue from the next milestone;
  - a fix with two commits (cherry-picked).
- **There's nothing client-related** and nothing about video.

## The arms
The rules text is **the same, word for word**, in every arm. `build_fixture.py` writes the folder version, then builds the monolith by joining those same files.

| Arm | What it is | How it's run |
|---|---|---|
| **A: one big CLAUDE.md** | Every stage's instructions, every reference file (inclusion rules, style guide, API reference, voice, past changelog) in one `CLAUDE.md` | One session. Prompt: "Prepare the 2.4.0 release notes." |
| **B: folder, one session** | ICM layout: a short `CLAUDE.md` (layer 0), a routing `CONTEXT.md`, and `stages/01_extract`, `02_draft`, `03_publish`, each with a `CONTEXT.md`, `references/` and `output/` | One session. The same prompt as A |
| **C: folder, a fresh session per stage** | The same folder as B | Three sessions, one per stage ("Run stage 01."), with no human edits between them |

- **A vs B** measures structure alone: same session, same prompt.
- **C** adds a fresh context per stage, the way ICM is used with review gates. There are no human edits, so the folder is the only thing tested.

**Settings for every arm**
- `claude -p` (Claude Code 2.1.327), `--model sonnet`, run in an empty scratch folder.
- User settings, hooks, plugins, MCP servers, skills and memory are all off.
- Tools: Read, Write, Edit, Glob, Grep only.
- **5 runs per arm**, so 15 sessions in all (25 `claude` calls, because each C run is 3 calls). Runs alternate A, B, C so that time of day doesn't favour one arm.

## Scoring (deterministic, `score.py`)
Each run gets a list of pass/fail checks. The **primary metric is the share of checks passed**. Checks are grouped so we can say *what* differs:

1. **Content.**
   - All 14 shipped changes are present (recall).
   - None of the 7 trap issues is present (precision).
   - Each change sits in the right section.
2. **Style rules, checked on every bullet:**
   - the issue reference format;
   - at most 14 words;
   - a capital first letter and no full stop at the end;
   - no banned words;
   - no emoji;
   - credit to external contributors;
   - API names exactly as written in the reference;
   - "tinyqueue" in lower case.
3. **Format.**
   - The exact header and date.
   - The section order and names.
   - Every breaking change has a Migration line.
   - The security item has its CVE.
   - `release.json` is valid and agrees with the Markdown.

**Also recorded:** tokens in and out, cost, number of turns and wall time, from `--output-format json`.

## What we expect, and what counts
- **H1:** B and C score higher than A on style and format rules (rules buried in a long context are followed less).
- **H2:** content (recall and precision) is about the same.
- With 5 runs per arm, we report every run's score, plus the mean and the range.
  - A difference smaller than the spread between runs of the same arm is reported as **"no clear difference"**.
  - A result where A wins is reported as such.
- **What this can't show:**
  - it's one job, one model and a small context (about 10k tokens of rules, not the paper's 42k);
  - it measures the rules being followed, not writing quality;
  - it says nothing about human review, which is the other half of the paper's argument.

## Changes before the first run (2026-11-18, same session)
- **Arm A2 added: one big CLAUDE.md with the repo's other jobs.** It holds the same release text, placed in the middle of a CLAUDE.md that also holds four other workflows: support replies, docs site, social announcements and on-call. That's about 29k tokens in all, near the paper's 42k "monolithic" figure.
  - Some of those workflows' rules conflict with the release rules on purpose, as happens in real repos: social posts allow emoji, write "TinyQueue" and credit with "shout-out to"; docs drop the class prefix.
  - The folder workspace holds the same four workflows in `workflows/<name>/`, where the release stages never read them.
  - **Why:** arm A alone is only about 3k tokens, smaller than any real CLAUDE.md that runs a whole repo.
  - Arms are now A, A2, B and C, with 5 runs each and rotation A, A2, B, C.
- **Scorer:** "starts with a capital" accepts a leading API name in backticks whose first letter is a capital (`Queue.drain()`). Strictly, my own hand-written perfect answer failed the rule as first coded.
- **Scorer self-check:** a hand-written correct answer scores 100. A copy with a reverted feature, an emoji, a trailing full stop and stale JSON scores lower and lists exactly those failures (`selfcheck/`).

## Follow-up added after the Sonnet results (2026-11-18)
Sonnet 5.5 scored 99.4–100 in every arm (results in `RESULTS.md`), so the test hit its ceiling. **Follow-up, decided after seeing those results:** the same four arms, 5 runs each, on **Haiku 5.5**, to see whether structure helps a smaller model. Nothing else changes: same fixture, same scorer. Results go in `runs-haiku/`.

## Second follow-up: the one-line fix (2026-11-18, after the Haiku results)
On Haiku, arm C lost the contributor credits. The maintainer list lives in stage 01's reference file, stage 02's card doesn't list it, and stage 01's hand-off carries only the author's name. **Fix (one line in the stage 01 card):** the hand-off now says "external or maintainer" for each change. Arm **C2** is that folder, run on Haiku 5 times exactly like C. Nothing else changes.
