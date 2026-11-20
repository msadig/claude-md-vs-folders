# Inclusion rules

1. Only issues in milestone `2.4.0` with state `closed` ship.
2. Leave out issues labelled `internal`, `docs`, `ci` or `test`: they have no user-facing change.
3. Leave out any change that was reverted before the release (look for `Revert` commits in the log).
4. Leave out fixes for bugs that were introduced in this same release and never shipped to users. The issue body says so.
5. One entry per issue, however many commits reference it (cherry-picks and follow-up commits are the same change).
6. Section, by the first matching label: `breaking` -> Breaking changes, `security` -> Security, `feature` -> Added, `deprecation` -> Deprecated, `bug` -> Fixed.
7. Maintainers: lena-ortiz, sam-okafor. Anyone else who opened a shipped issue is an external contributor.
