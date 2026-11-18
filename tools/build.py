#!/usr/bin/env python3
"""
Build README.md from data/prs.json, the dashboard's single source of truth.

    python3 tools/build.py           # rewrite README.md (and tidy data/prs.json)
    python3 tools/build.py --check   # exit 1 if README.md is out of date (used by CI)

Everything between <!-- data:start --> and <!-- data:end --> in README.md is generated:
summary, data contract dates, "New this month", merged PRs by developer, and open PRs.
The change log and "How We Count" stay hand-written. codeorange.dev reads data/prs.json
directly, so the website updates as soon as a change to it is merged.

Fields of a PR in data/prs.json:
  github, repo, number, status ("merged" | "open"), month ("Nov 2026")
  note           optional short description shown after the link
  beforeJoining  true if merged before the author joined Code Orange (marked *)
  firstSeen      date of the recount that first listed it in its current state;
                 PRs with the latest "checked" date make up "New this month"
"""

import json
import re
import sys
from collections import OrderedDict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "prs.json"
README = ROOT / "README.md"
START, END = "<!-- data:start -->", "<!-- data:end -->"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def load():
    return json.loads(DATA.read_text())


def dump(d):
    """Stable, diff-friendly JSON: one PR per line."""
    head = {k: v for k, v in d.items() if k != "prs"}
    text = json.dumps(head, indent=1, ensure_ascii=False)[:-2]
    rows = ",\n".join("  " + json.dumps(p, ensure_ascii=False) for p in d["prs"])
    return text + ',\n "prs": [\n' + rows + "\n ]\n}\n"


def month_key(m):
    mon, year = m.split()
    return int(year) * 12 + MONTHS.index(mon)


def month_range(ms):
    ks = sorted({month_key(m) for m in ms})
    a, b = ks[0], ks[-1]
    name = lambda k: (MONTHS[k % 12], k // 12)
    (am, ay), (bm, by) = name(a), name(b)
    if a == b:
        return f"{am} {ay}"
    if ay == by:
        return f"{am}–{bm} {by}"
    return f"{am} {ay}–{bm} {by}"


def long_date(iso):
    return datetime.strptime(iso, "%Y-%m-%d").strftime("%-d %B %Y")


def url(p):
    return f"https://github.com/{p['repo']}/pull/{p['number']}"


def stats(d):
    merged = [p for p in d["prs"] if p["status"] == "merged"]
    opened = [p for p in d["prs"] if p["status"] == "open"]
    return {
        "merged": len(merged),
        "before": sum(1 for p in merged if p.get("beforeJoining")),
        "open": len(opened),
        "repos": len({p["repo"].lower() for p in merged}),
        "contributors": len({p["github"] for p in merged}),
    }


def new_this_month(d):
    return [p for p in d["prs"] if p.get("firstSeen") == d["checked"]]


def link_list(prs, projects, with_repo_labels):
    out = []
    last_repo = None
    for p in prs:
        label = f"#{p['number']}"
        prefix = ""
        if with_repo_labels and p["repo"] != last_repo:
            prefix = p["repo"].split("/")[1] + " "
        last_repo = p["repo"]
        s = f"{prefix}[{label}]({url(p)})" + ("*" if p.get("beforeJoining") else "")
        if p.get("note"):
            s += f" {p['note']}"
        out.append(s)
    return " · ".join(out)


def render(d):
    s = stats(d)
    projects = d["projects"]
    names = {c["github"]: c["name"] for c in d["contributors"]}
    checked = long_date(d["checked"])
    L = []
    a = L.append
    a(START)
    a("<!-- Generated from data/prs.json by tools/build.py. Edit the JSON, not this block. -->")
    a("")
    a("## Summary")
    a("")
    a(f"Counted from the links below on {checked}. Every number here is a count of linked PRs, nothing else.")
    a("")
    a("| Metric | Count |")
    a("| --- | --- |")
    a(f"| **Merged PRs (each linked below)** | **{s['merged']}** ({s['before']} of these predate the author joining Code Orange, marked *) |")
    a(f"| **Open PRs (each linked below)** | **{s['open']}** |")
    a(f"| **Distinct repositories with a merged PR** | **{s['repos']}** |")
    a(f"| **Contributors with a merged PR** | **{s['contributors']}** |")
    a("")
    a("A PR listed here is the work of its author. Listing it records that the author is part of the Code Orange community; it doesn't claim Code Orange wrote, directed or caused it.")
    a("")
    a("The data lives in [`data/prs.json`](data/prs.json). This page and [codeorange.dev/dashboard](https://codeorange.dev/dashboard) are both built from it, so they always show the same numbers.")
    a("")

    fresh = new_this_month(d)
    fm = [p for p in fresh if p["status"] == "merged"]
    fo = [p for p in fresh if p["status"] == "open"]
    a("---")
    a("")
    a(f"## New This Month ({checked})")
    a("")
    if not fresh:
        a("Nothing new since the last recount.")
    else:
        a(f"**{len(fm)} newly merged** and **{len(fo)} newly opened** since the last recount.")
        a("")
        by = OrderedDict()
        for p in fm:
            by.setdefault(p["github"], []).append(p)
        for gh, ps in by.items():
            a(f"- **{names[gh]}**: " + link_list(ps, projects, True))
        if fo:
            a("")
            a("Newly opened: " + ", ".join(
                f"{names[gh]} ({n})" for gh, n in OrderedDict(
                    (gh, sum(1 for p in fo if p["github"] == gh)) for gh in dict.fromkeys(p["github"] for p in fo)
                ).items()))
    a("")
    a("---")
    a("")
    a("## Current Metrics Data Contract")
    a("")
    a("This dashboard is Code Orange's public source for **current PR output**. Historical reports and contributor profiles may use earlier snapshots and must link here rather than repeat these totals.")
    a("")
    a("| Field | Rule |")
    a("| --- | --- |")
    a(f"| **Reporting cutoff** | Link-level verification through **{checked}**. |")
    a("| **Attribution** | Count only in-scope Bitcoin OSS PRs with a direct link. PRs made before a developer joined Code Orange may be listed as history, but are excluded from program-outcome claims. |")
    a("| **PR state** | *Merged* means accepted upstream. *Open / under review* means submitted and neither merged nor closed at the reporting cutoff. Closed-unmerged PRs are not counted as open. |")
    a("| **Metric owner** | The named Code Orange **PR Verifier**, recorded in the weekly operating scorecard. |")
    a("| **Cadence** | Verify state changes weekly; recount and publish a refreshed snapshot on the 1st of each month, with the cutoff date shown. |")
    a("")
    a("---")
    a("")
    a(f"## Merged Pull Requests by Developer ({s['merged']})")
    a("")
    merged = [p for p in d["prs"] if p["status"] == "merged"]
    order = sorted(d["contributors"], key=lambda c: -sum(1 for p in merged if p["github"] == c["github"]))
    for c in order:
        mine = [p for p in merged if p["github"] == c["github"]]
        if not mine:
            continue
        a(f"### {c['name']} ([@{c['github']}](https://github.com/{c['github']})) - {len(mine)} merged")
        a("| Project | PR | Date |")
        a("| --- | --- | --- |")
        rows = OrderedDict()
        for p in mine:
            rows.setdefault(p["repo"], []).append(p)
        rows = sorted(rows.items(), key=lambda kv: (not projects[kv[0]].get("key"), -max(month_key(p["month"]) for p in kv[1])))
        for repo, ps in rows:
            ps.sort(key=lambda p: -p["number"])
            name = projects[repo]["name"]
            if projects[repo].get("key"):
                name = f"**{name}**"
            if projects[repo].get("education"):
                name += " (education)"
            a(f"| {name} | {link_list(ps, projects, False)} | {month_range([p['month'] for p in ps])} |")
        a("")
        if c.get("note"):
            a(f"*{c['note']}")
            a("")
    a("---")
    a("")
    opened = [p for p in d["prs"] if p["status"] == "open"]
    a(f"## Open / Under Review ({s['open']})")
    a("")
    a(f"Link states re-checked {checked}.")
    a("")
    a("| Developer | Project | PR |")
    a("| --- | --- | --- |")
    for c in order:
        mine = [p for p in opened if p["github"] == c["github"]]
        if not mine:
            continue
        repos = list(OrderedDict.fromkeys(p["repo"] for p in sorted(mine, key=lambda p: p["repo"] != mine[0]["repo"])))
        mine.sort(key=lambda p: (repos.index(p["repo"]), -p["number"]))
        proj = " · ".join(projects[r]["name"] for r in repos)
        a(f"| {c['name']} | {proj} | {link_list(mine, projects, len(repos) > 1)} |")
    a("")
    a("---")
    a("")
    a(END)
    return "\n".join(L)


def build():
    d = load()
    for p in d["prs"]:
        assert p["repo"] in d["projects"], f"add {p['repo']} to projects"
        assert p["github"] in {c["github"] for c in d["contributors"]}, f"add {p['github']} to contributors"
        assert p["status"] in ("merged", "open"), p
        month_key(p["month"])
    keys = [(p["repo"].lower(), p["number"]) for p in d["prs"]]
    dupes = {k for k in keys if keys.count(k) > 1}
    assert not dupes, f"duplicate PRs: {dupes}"
    readme = README.read_text()
    block = render(d)
    if START in readme:
        new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block, readme, flags=re.S)
    else:
        # first run: replace everything from "## Summary" up to the change log
        i, j = readme.index("## Summary"), readme.index("## Change Log")
        new = readme[:i] + block + "\n\n" + readme[j:]
    new = re.sub(r"> Last updated: [^|]+\|", f"> Last updated: {long_date(d['checked'])} |", new, count=1)
    return d, new


if __name__ == "__main__":
    d, new = build()
    if "--check" in sys.argv:
        if new != README.read_text() or dump(d) != DATA.read_text():
            sys.exit("README.md or data/prs.json is out of date: run python3 tools/build.py")
        print("README.md matches data/prs.json")
    else:
        DATA.write_text(dump(d))
        README.write_text(new)
        s = stats(d)
        print(f"README.md built: {s['merged']} merged, {s['open']} open, {s['repos']} repos, {s['contributors']} contributors")
