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
