# Routing

| Request | Stage |
|---|---|
| "Prepare the release notes" | run 01, then 02, then 03, in order |
| "Run stage 01" (or 02, 03) | only that stage |

Stages:
1. `stages/01_extract/`: decide which changes ship and in which section.
2. `stages/02_draft/`: write one bullet per change.
3. `stages/03_publish/`: format the changelog entry and `release.json`.

Shared: `_config/release.md` (version and date), `_config/voice.md` (tone).

Other jobs in this repo, each in `workflows/<name>/CONTEXT.md` (not used for release notes): support replies, docs site, social announcements, on-call.
