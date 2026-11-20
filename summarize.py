"""Summarize runs: python3 summarize.py runs [runs-haiku]"""
import json, glob, os, sys, statistics as st
from collections import defaultdict, Counter
for base in sys.argv[1:]:
    print("##", base)
    rows = defaultdict(list); fails = defaultdict(Counter); cost = defaultdict(list); tok = defaultdict(list); secs = defaultdict(list); turns = defaultdict(list)
    for d in sorted(glob.glob(f"{base}/*-[1-9]")):
        arm = os.path.basename(d).rsplit("-", 1)[0]
        s = json.load(open(d + "/score.json")); rows[arm].append(s)
        for f in s["failed"]:
            g, rest = f.split(": ", 1)
            fails[arm][g + ": " + (rest.split(" ", 1)[1] if rest.startswith("#") else rest)] += 1
        c = t = n = 0
        for j in glob.glob(d + "/session*.json"):
            try: x = json.load(open(j))
            except Exception: continue
            c += x.get("total_cost_usd", 0); u = x.get("usage", {})
            t += u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0); n += x.get("num_turns", 0)
        cost[arm].append(c); tok[arm].append(t); turns[arm].append(n); secs[arm].append(int(open(d + "/seconds").read()))
    print("| Arm | Scores (5 runs) | Mean | Content | Style | Format | Cost/run | Tokens/run | Time/run |")
    print("|---|---|---|---|---|---|---|---|---|")
    for arm in [a for a in ["A", "A2", "B", "C", "C2"] if a in rows]:
        r = rows[arm]; m = lambda k: round(st.mean(x[k] for x in r), 1)
        print(f"| {arm} | {', '.join(str(x['total']) for x in r)} | {m('total')} | {m('content')} | {m('style')} | {m('format')} | ${st.mean(cost[arm]):.3f} | {int(st.mean(tok[arm])/1000)}k | {round(st.mean(secs[arm]))} s |")
    for arm in [a for a in ["A", "A2", "B", "C", "C2"] if a in rows]:
        print(f"- {arm} failures: " + ("; ".join(f"{k} ×{v}" for k, v in fails[arm].most_common()) or "none"))
