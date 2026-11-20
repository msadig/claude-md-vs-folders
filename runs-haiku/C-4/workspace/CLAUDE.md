# tinyqueue release workspace

This workspace prepares the release notes for tinyqueue, a Python job-queue library.
Raw inputs are in `inputs/` (git log and issue export). Never edit them.

- Start at `CONTEXT.md`: it says which stage handles a request.
- Each stage lives in `stages/<NN>_<name>/` and has its own `CONTEXT.md` (the stage contract).
- Read only the files a stage's contract lists. Write only to that stage's `output/`.
