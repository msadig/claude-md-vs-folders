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
