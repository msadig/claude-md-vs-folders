"""Score one run directory deterministically (no LLM). Usage: python3 score.py <run_dir> [--json]
Finds CHANGELOG-2.4.0.md and release.json anywhere under the run's workspace."""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).parent
TRUTH = json.loads((HERE / "truth.json").read_text())
SECTIONS = ["Breaking changes", "Security", "Added", "Deprecated", "Fixed"]
BANNED = ["simply", "just", "easily", "seamless", "seamlessly", "robust", "leverage", "powerful"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅]")
BULLET = re.compile(r"^- (.+) \(#(\d+)\)$")

def find(root, name):
    hits = sorted(p for p in Path(root).rglob(name) if "inputs" not in p.parts)
    return hits[-1] if hits else None

def parse(md):
    """-> header line, [(section, [bullet lines with their sub-lines])]"""
    lines = [l.rstrip() for l in md.splitlines()]
    header = next((l for l in lines if l.strip()), "")
    sections, cur = [], None
    for l in lines:
        if l.startswith("### "):
            cur = (l[4:].strip(), [])
            sections.append(cur)
        elif l.startswith("- ") and cur:
            cur[1].append([l])
        elif l.startswith("  - ") and cur and cur[1]:
            cur[1][-1].append(l)
    return header, sections

def score(run):
    checks = []  # (group, name, ok)
    def c(group, name, ok): checks.append((group, name, bool(ok)))
    md_p, js_p = find(run, "CHANGELOG-2.4.0.md"), find(run, "release.json")
    c("format", "changelog file exists", md_p)
    c("format", "release.json exists", js_p)
    md = md_p.read_text() if md_p else ""
    header, sections = parse(md)

    # content
    found = {}  # issue -> list of sections
    for sec, bullets in sections:
        for b in bullets:
            for n in re.findall(r"\(#(\d+)\)", b[0]):
                found.setdefault(n, []).append(sec)
    for n, t in TRUTH["shipped"].items():
        c("content", f"#{n} listed exactly once", len(found.get(n, [])) == 1)
        c("content", f"#{n} in {t['section']}", found.get(n, [None])[0] == t["section"])
    for n, why in TRUTH["traps"].items():
        c("content", f"trap #{n} ({why}) left out", n not in found)

    # style, per top-level bullet
    api = set(TRUTH["api_names"])
    for sec, bullets in sections:
        for b in bullets:
            line = b[0]
            m = BULLET.match(line)
            c("style", f"format: {line[:40]}", m)
            if not m:
                continue
            text, n = m.group(1), m.group(2)
            credit = re.search(r", thanks @([\w-]+)$", text)
            core = text[:credit.start()] if credit else text
            c("style", f"#{n} <=14 words", len(core.split()) <= 14)
            c("style", f"#{n} starts with a capital", core.lstrip("`")[:1].isupper())  # a leading API name in backticks counts
            c("style", f"#{n} no trailing full stop", not core.rstrip().endswith("."))
            words = re.findall(r"[a-z]+", text.lower())
            c("style", f"#{n} no banned words", not set(words) & set(BANNED))
            c("style", f"#{n} no emoji", not EMOJI.search("\n".join(b)))
            t = TRUTH["shipped"].get(n)
            if t:
                want = t["author"] if t["external"] else None
                c("style", f"#{n} credit right", (credit.group(1) if credit else None) == want)
            ticks = re.findall(r"`([^`]+)`", "\n".join(b))
            c("style", f"#{n} API names exact", all(x in api for x in ticks))
            c("style", f"#{n} tinyqueue lower case", not re.search(r"TinyQueue|Tinyqueue|TINYQUEUE", "\n".join(b)))

    # format
    c("format", "header exact", header.strip() == f"## [{TRUTH['release']}] - {TRUTH['date']}")
    names = [s for s, _ in sections]
    c("format", "only allowed section names", names and all(s in SECTIONS for s in names))
    c("format", "sections in order", names == [s for s in SECTIONS if s in names])
    c("format", "no empty sections", all(b for _, b in sections))
    for sec, bullets in sections:
        if sec == "Breaking changes":
            for b in bullets:
                c("format", f"migration line: {b[0][:30]}", any(x.startswith("  - Migration:") for x in b[1:]))
        if sec == "Security":
            c("format", "CVE in security bullet", any(TRUTH["cve"] in b[0] for b in bullets))
    try:
        js = json.loads(js_p.read_text()) if js_p else None
    except Exception:
        js = None
    c("format", "json valid", isinstance(js, dict))
    js = js if isinstance(js, dict) else {}
    c("format", "json keys exact", set(js) == {"version", "date", "counts", "issues"})
    c("format", "json version/date", js.get("version") == TRUTH["release"] and js.get("date") == TRUTH["date"])
    md_counts = {s: len(b) for s, b in sections if b}
    c("format", "json counts match md", js.get("counts") == md_counts)
    md_issues = sorted(int(n) for n in found)
    c("format", "json issues match md, sorted ints", js.get("issues") == md_issues)
    return checks

def summary(checks):
    out = {}
    for g in ("content", "style", "format"):
        gs = [ok for gg, _, ok in checks if gg == g]
        out[g] = round(100 * sum(gs) / len(gs), 1) if gs else 0.0
    out["total"] = round(100 * sum(ok for *_, ok in checks) / len(checks), 1)
    out["failed"] = [f"{g}: {n}" for g, n, ok in checks if not ok]
    return out

if __name__ == "__main__":
    s = summary(score(sys.argv[1]))
    print(json.dumps(s, indent=1) if "--json" in sys.argv else f"total {s['total']}  content {s['content']}  style {s['style']}  format {s['format']}  fails {len(s['failed'])}")
