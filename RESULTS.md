# Results: one big CLAUDE.md vs a folder of stages

Run 2026-11-18 with Claude Code 2.1.327 in clean sessions (no user settings, hooks, plugins, MCP servers or memory). The plan is in `PLAN.md`, written before the first run, with its later changes dated at the bottom. Each run's files, score and usage numbers (cost, tokens, turns, time, model; the agent's own messages are left out) are in `runs/` (Sonnet) and `runs-haiku/` (Haiku). Re-score any run with `python3 score.py <run>/workspace --json`, and rebuild the tables with `python3 summarize.py runs runs-haiku`.

**Arms**
- **A:** one CLAUDE.md, about 3k tokens.
- **A2:** one CLAUDE.md that also holds the repo's other four jobs, about 29k tokens, with the release rules in the middle.
- **B:** the ICM folder, one session.
- **C:** the ICM folder, a fresh session per stage.
- **C2:** C with one line of the stage 01 card fixed.

Scores are the % of about 90 deterministic checks passed per run.

## Sonnet 5.5 (5 runs per arm)
| Arm | Scores | Mean | Content | Style | Format | Cost/run | Tokens/run | Time/run |
|---|---|---|---|---|---|---|---|---|
| A | 100, 99.4, 100, 100, 100 | 99.9 | 100 | 99.8 | 100 | $0.127 | 97k | 31 s |
| A2 | 100, 100, 100, 100, 100 | 100 | 100 | 100 | 100 | $0.218 | 216k | 38 s |
| B | 100, 100, 100, 100, 100 | 100 | 100 | 100 | 100 | $0.155 | 173k | 41 s |
| C | 100, 100, 100, 100, 100 | 100 | 100 | 100 | 100 | $0.230 | 351k | 60 s |

There was one failure in 20 runs: an A bullet that started with a lower-case API name.

## Haiku 5.5 (follow-up, 5 runs per arm)
| Arm | Scores | Mean | Content | Style | Format | Cost/run | Tokens/run | Time/run |
|---|---|---|---|---|---|---|---|---|
| A | 100, 98.9, 100, 100, 98.9 | 99.6 | 100 | 99.4 | 100 | $0.014 | 137k | 59 s |
| A2 | 100, 98.9, 99.4, 100, 100 | 99.7 | 100 | 99.5 | 100 | $0.022 | 288k | 83 s |
| B | 100, 99.4, 100, 99.4, 99.4 | 99.6 | 100 | 99.5 | 100 | $0.017 | 263k | 77 s |
| C | 92.8, 98.9, 96.0, 100, 95.4 | **96.6** | 98.9 | 95.6 | 100 | $0.018 | 348k | 88 s |
| C2 (one-line fix) | 100, 99.4, 98.9, 100, 100 | **99.7** | 100 | 99.5 | 100 | $0.019 | 336k | 90 s |

**Failures by arm**
- **A:** lower-case start ×3, wrong credit ×1.
- **A2:** lower-case start ×2, wrong credit ×1.
- **B:** lower-case start ×2, one API name not in the reference ×1.
- **C:** **wrong credit ×20** across 4 of 5 runs, lower-case start ×6. In one run the security bullet lost its issue number, so #431 counted as missing.
- **C2:** lower-case start ×3, **wrong credit ×0**.

## What happened in C
- **The cause.** The list of maintainers lives in stage 01's reference file (`inclusion-rules.md`). Stage 01's hand-off (`changes.md`) carried only the author's handle. Stage 02's card lists the style guide ("thank external contributors") but not the maintainer list.
- **Why only C failed.** A fresh Haiku session at stage 02 couldn't tell who was external, so it thanked nobody. In B, the same session had already read the list during stage 01. Sonnet in C got it right every time.
- **The fix.** One line in the stage 01 card: the hand-off now includes "external or maintainer" for each change. C2 got every credit right.
- **Whose mistake.** The gap was in the cards as I wrote them. It's the kind of gap ICM's own paper describes in §6.3: "Editing the output fixes this run. Editing the source fixes every future run."
- **How it was found.** We read `changes.md` and `bullets.md` in the stage folders, which is the "observable by default" property the paper claims (§5.3).

**How Sonnet got the credits right in C.** One extra Sonnet stage-02 run with a full trace (the raw trace isn't published; this is what it showed):
- It read its card, the hand-off, the style guide, the API reference, the voice file and `issues.json`.
- Then it searched the whole workspace for `external|maintainer|core team` and found the list in stage 01's reference file, outside its card's Inputs.
- So the stronger model filled the gap by breaking the "read only what the card lists" rule. The smaller one followed the card and missed the fact.

## What this shows
1. **On these models, at this size, the structure didn't change quality.**
   - Sonnet 5.5 followed every rule in a 29k-token CLAUDE.md that also held conflicting rules for other jobs: 100 in all 5 runs.
   - Haiku scored 99.6–99.7 in A, A2 and B.
   - The paper's quality argument (rules lost in long context) didn't show up here.
2. **Cost and time.**
   - The smallest single file was the cheapest and fastest.
   - The folder in one session (B) took more turns (about 20 against 10) and more tokens than A, because reading files means more steps.
   - Against the realistic big file (A2), B used fewer tokens: on Sonnet 173k against 216k, and $0.155 against $0.218 a run.
   - A fresh session per stage (C) cost the most and was the slowest.
   - All of these are cents on one small job. They are not a cost claim about real work.
3. **The real difference was where a mistake can come from and how you find it.**
   - Splitting the work into fresh sessions made each stage depend on what its card and hand-off carry. One missing fact cost a smaller model 20 credits.
   - Because every hand-off is a file, the cause was visible in one place and fixed with one line, and the fix held in all 5 re-runs.

## Limits
- **A ceiling, not proof of no effect.** Every arm except Haiku C scored 99.6–100, so this job was too easy to separate them. A harder job or a weaker model might.
- **A2's padding is uneven.** Its extra ~26k tokens are four workflows built from a few blocks repeated 5 or 6 times, each headed "not used for release notes". That's easier to ignore than a real repo's varied CLAUDE.md.
- **Token totals are mostly overhead.** They are dominated by Claude Code's own system prompt and tools being re-read every turn (cache reads), so turns drive them more than the rules' size.
- **C's time is suspicious.** Sonnet C took exactly 60 s on every run, which looks like a fixed overhead, not work.
- **The CVE id was replaced.** The original fixture used an id that turned out to belong to a real, unrelated CVE. In this published copy it is `CVE-0000-00000` everywhere, including the recorded outputs; all 45 runs re-score the same.
- One job, about 90 checks, 5 runs per arm.
- Two models from one family, Sonnet 5.5 and Haiku 5.5.
- The checks measure whether rules were followed, not how good the writing is.
- No human review between stages. That is half of the paper's argument and isn't measured here.
- The Haiku arms and the C2 fix were follow-ups decided after seeing earlier results, as dated in `PLAN.md`.
- The cost figures come from Claude Code's `total_cost_usd` and include prompt caching.
- **Total spend for the test:** about $3.80 on Sonnet (including the pilot) and $0.50 on Haiku.
