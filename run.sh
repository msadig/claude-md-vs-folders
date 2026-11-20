#!/bin/bash
# Run arms in rotation. Usage: ./run.sh <first_rep> <last_rep> [arms...]   e.g. ./run.sh 1 5 A A2 B C
# Each run: fresh copy of the workspace in scratch (outside any repo, so no other CLAUDE.md is found),
# claude -p with user settings/hooks/plugins/MCP off, then copy the workspace back to runs/<arm>-<rep>/ and score it.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
SCRATCH="${TEST_SCRATCH:-${TMPDIR:-/tmp}/icm-test}"
FIRST=$1; LAST=$2; shift 2
ARMS=("${@:-A A2 B C}")
[ ${#ARMS[@]} -eq 1 ] && read -r -a ARMS <<< "${ARMS[0]}"

cc() {  # cc <workdir> <prompt> <json_out>
  (cd "$1" && claude -p "$2" --model "${MODEL:-sonnet}" \
     --setting-sources project --strict-mcp-config --disable-slash-commands --no-session-persistence \
     --allowedTools "Read Write Edit Glob Grep" --disallowedTools "Bash Agent Task WebFetch WebSearch" \
     --max-budget-usd 3 --output-format json) > "$3" 2> "$3.err"
}

for rep in $(seq "$FIRST" "$LAST"); do
  for arm in "${ARMS[@]}"; do
    out="$HERE/runs${RUNS_SUFFIX:-}/$arm-$rep"; [ -e "$out/done" ] && continue
    case $arm in A) src=workspace-mono;; A2) src=workspace-mono-big;; B|C) src=workspace-folder;; C2) src=workspace-folder-v2;; esac
    work="$SCRATCH/$arm-$rep"; rm -rf "$work" "$out"; mkdir -p "$SCRATCH" "$out"
    cp -R "$HERE/$src" "$work"
    start=$(date +%s)
    if [ "$arm" = C ] || [ "$arm" = C2 ]; then
      for s in 01 02 03; do cc "$work" "Run stage $s." "$out/session-$s.json"; done
    else
      cc "$work" "Prepare the 2.4.0 release notes." "$out/session.json"
    fi
    echo $(( $(date +%s) - start )) > "$out/seconds"
    rsync -a --exclude inputs "$work/" "$out/workspace/"
    python3 "$HERE/score.py" "$out/workspace" --json > "$out/score.json"
    touch "$out/done"
    echo "$arm-$rep $(python3 "$HERE/score.py" "$out/workspace")  $(cat "$out/seconds")s"
  done
done
