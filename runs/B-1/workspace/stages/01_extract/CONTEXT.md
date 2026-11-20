# Stage 01: extract

## Inputs
- Layer 4 (working): `../../inputs/git-log.txt`, `../../inputs/issues.json`
- Layer 3 (reference): `references/inclusion-rules.md`
- Layer 3 (reference): `../../_config/release.md`

## Process
Go through every issue referenced in the git log and decide, with the inclusion rules, whether it ships in this release and in which section.

## Outputs
- `output/changes.md`: one line per shipped change: `<section> | #<number> | <issue title> | <issue author>`
