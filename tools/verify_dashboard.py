#!/usr/bin/env python3
"""
Verify the PR dashboard against GitHub, so the PR Verifier's weekly check
takes minutes instead of clicking 130+ links.

    python3 tools/verify_dashboard.py                     # report to stdout
    python3 tools/verify_dashboard.py --since 2026-07-12  # also find new PRs since the cutoff
    python3 tools/verify_dashboard.py --out report.md

It checks, without changing README.md:
  1. every PR in "Merged Pull Requests" is actually merged, and was not
     merged by its own author or into the author's own account
  2. every PR in "Open / Under Review" is still open (flags merged -> move,
     closed -> remove)
  3. per-developer "- N merged" headers and the section total match the links
  4. (--since) merged and open PRs by each listed developer created or merged
     after the cutoff that the dashboard doesn't list yet - candidates only;
     a human still applies the scope rules in "How We Count"

Needs a GitHub token: GITHUB_TOKEN / GH_TOKEN, or a logged-in `gh` CLI.
No third-party packages.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
PR_RE = re.compile(r"https://github\.com/([\w.-]+)/([\w.-]+)/pull/(\d+)")
DEV_RE = re.compile(r"^### (.+?) \(\[@([\w-]+)\]\(https://github\.com/[\w-]+\)\) - (\d+) merged")


def token():
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(var):
            return os.environ[var]
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        sys.exit("No GitHub token: set GITHUB_TOKEN or log in with `gh auth login`.")


def graphql(tok, query):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"bearer {tok}", "User-Agent": "co-dashboard-verifier"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        body = json.load(r)
    if body.get("errors") and not body.get("data"):
        raise RuntimeError(body["errors"])
    return body.get("data") or {}


def section(text, start, stop_prefix="## "):
    lines, inside = [], False
    for line in text.splitlines():
        if line.startswith(start):
            inside = True
            continue
        if inside and line.startswith(stop_prefix):
            break
        if inside:
            lines.append(line)
    return lines


def parse(text):
    merged_lines = section(text, "## Merged Pull Requests")
    open_lines = section(text, "## Open / Under Review")
    header_total = re.search(r"## Merged Pull Requests by Developer \((\d+)\)", text)

    devs, merged, current = [], [], None
    for line in merged_lines:
        m = DEV_RE.match(line)
        if m:
            current = {"name": m.group(1), "handle": m.group(2), "claimed": int(m.group(3)), "prs": []}
            devs.append(current)
            continue
        if line.startswith("### "):
            current = None  # e.g. "Claimed, not yet linked"
            continue
        if current is not None and line.startswith("|"):
            for pr in PR_RE.findall(line):
                current["prs"].append(pr)
                merged.append((current["name"], pr))

    opened = []
    for line in open_lines:
        if line.startswith("|") and not line.startswith("| Developer") and not line.startswith("| ---"):
            name = line.split("|")[1].strip()
            for pr in PR_RE.findall(line):
                opened.append((name, pr))
    handles = {d["name"]: d["handle"] for d in devs}
    return devs, merged, opened, int(header_total.group(1)) if header_total else None, handles


SELF_MERGED = set()  # merged by their own author, or in the author's own account: not countable


def fetch_states(tok, prs):
    prs = sorted(set(prs))
    states = {}
    for i in range(0, len(prs), 40):
        chunk = prs[i:i + 40]
        parts = [
            f'p{j}: repository(owner: "{o}", name: "{r}") {{ owner {{ login }} pullRequest(number: {n}) {{ state mergedAt url author {{ login }} mergedBy {{ login }} }} }}'
            for j, (o, r, n) in enumerate(chunk)
        ]
        data = graphql(tok, "{ " + " ".join(parts) + " }")
        for j, pr in enumerate(chunk):
            node = (data.get(f"p{j}") or {}).get("pullRequest")
            states[pr] = node["state"] if node else "NOT_FOUND"
            repo = data.get(f"p{j}") or {}
            if node and node.get("author") and node.get("mergedBy"):
                author = node["author"]["login"].lower()
                if author == node["mergedBy"]["login"].lower() or author == repo["owner"]["login"].lower():
                    SELF_MERGED.add(pr)
    return states


def find_new(tok, handles, since, listed):
    found = []
    for name, handle in sorted(handles.items()):
        for kind, q in (("merged", f"is:pr author:{handle} is:merged merged:>{since}"),
                        ("open", f"is:pr author:{handle} is:open created:>{since}")):
            data = graphql(tok, 'query { search(type: ISSUE, first: 50, query: %s) { nodes { ... on PullRequest { url title repository { nameWithOwner isFork } } } } }' % json.dumps(q))
            for node in data["search"]["nodes"]:
                m = PR_RE.match(node.get("url", ""))
                if not m or m.groups() in listed:
                    continue
                if node["repository"]["nameWithOwner"].lower().startswith(handle.lower() + "/"):
                    continue  # PRs into the contributor's own repos/forks aren't upstream work
                found.append((name, kind, node["url"], node["title"]))
    return found


def fmt(pr):
    o, r, n = pr
    return f"[{o}/{r}#{n}](https://github.com/{o}/{r}/pull/{n})"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", help="cutoff date YYYY-MM-DD for discovering unlisted PRs")
    ap.add_argument("--out", help="write the markdown report to this file")
    ap.add_argument("--strict", action="store_true", help="exit 1 if anything needs attention (for CI)")
    args = ap.parse_args()

    tok = token()
    devs, merged, opened, header_total, handles = parse(README.read_text())
    states = fetch_states(tok, [pr for _, pr in merged + opened])

    out = ["# Dashboard verification report", ""]
    problems = 0

    bad = [(n, pr, states[pr]) for n, pr in merged if states[pr] != "MERGED"]
    out.append(f"## Merged section: {len(merged) - len(bad)}/{len(merged)} links confirmed merged")
    for n, pr, st in bad:
        out.append(f"- ❌ {n}: {fmt(pr)} is **{st}**, not merged")
    problems += len(bad)

    selfm = [(n, pr) for n, pr in merged if pr in SELF_MERGED]
    if selfm:
        out.append("")
        out.append(f"## Self-merged or own-repo PRs in the merged section: {len(selfm)} (How We Count excludes these)")
        for n, pr in selfm:
            out.append(f"- ❌ {n}: {fmt(pr)}")
        problems += len(selfm)

    out += ["", "## Per-developer counts"]
    recount = 0
    for d in devs:
        actual = sum(1 for pr in d["prs"] if states[pr] == "MERGED")
        recount += actual
        mark = "✓" if actual == d["claimed"] else "❌"
        if actual != d["claimed"]:
            problems += 1
        out.append(f"- {mark} {d['name']}: header says {d['claimed']}, links show {actual}")
    mark = "✓" if recount == header_total else "❌"
    if recount != header_total:
        problems += 1
    out.append(f"- {mark} **Total**: section header says {header_total}, verified links sum to {recount}")

    moved = [(n, pr) for n, pr in opened if states[pr] == "MERGED"]
    closed = [(n, pr) for n, pr in opened if states[pr] in ("CLOSED", "NOT_FOUND")]
    still = len(opened) - len(moved) - len(closed)
    out += ["", f"## Open section: {still}/{len(opened)} still open"]
    for n, pr in moved:
        out.append(f"- 🟢 {n}: {fmt(pr)} **merged**, move it to the merged section")
    for n, pr in closed:
        out.append(f"- ⚪ {n}: {fmt(pr)} is **{states[pr].lower()}**, remove it from open")
    problems += len(moved) + len(closed)

    if args.since:
        listed = {pr for _, pr in merged + opened}
        new = find_new(tok, handles, args.since, listed)
        out += ["", f"## Unlisted PRs since {args.since} (candidates, apply 'How We Count' before adding)"]
        out += [f"- {n} ({kind}): [{url.split('github.com/')[1]}]({url}) {title}" for n, kind, url, title in new] or ["- none found"]

    out += ["", f"**{problems} item(s) need attention.**" if problems else "**Dashboard matches GitHub.**"]
    report = "\n".join(out) + "\n"
    if args.out:
        Path(args.out).write_text(report)
    print(report)
    if args.strict and problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
