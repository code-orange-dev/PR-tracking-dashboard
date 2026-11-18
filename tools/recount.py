#!/usr/bin/env python3
"""
Monthly recount: compare data/prs.json with GitHub and (optionally) apply the safe changes.

    python3 tools/recount.py                 # report only
    python3 tools/recount.py --apply         # also update data/prs.json, then run tools/build.py

Uses GitHub's issue search (`author:LOGIN is:pr`) through the `gh` CLI or a GITHUB_TOKEN.

--apply changes only what needs no judgement:
  * listed open PR now merged  -> merged (month = merge month, firstSeen = today)
  * listed open PR now closed  -> removed
  * new merged/open PR by a listed developer in a repo already in data/prs.json
    (and not in the developer's own account) -> added with firstSeen = today
and sets "checked" to today. Everything else is printed for a human to decide:
new repos (scope check per "How We Count"), PRs merged by their own author
(search can't tell; check the merge commit), and developers search can't see.
"""

import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "prs.json"


def search(q):
    items, page = [], 1
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    while True:
        if tok:
            url = "https://api.github.com/search/issues?" + urllib.parse.urlencode({"q": q, "per_page": 100, "page": page})
            req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}", "User-Agent": "co-recount"})
            with urllib.request.urlopen(req, timeout=60) as r:
                body = json.load(r)
        else:
            out = subprocess.run(["gh", "api", "-X", "GET", "search/issues", "-f", f"q={q}", "-f", "per_page=100", "-f", f"page={page}"],
                                 capture_output=True, text=True, check=True).stdout
            body = json.loads(out)
        items += body.get("items", [])
        if len(body.get("items", [])) < 100 or page >= 10:
            return items
        page += 1
        time.sleep(2)


def month(iso):
    return datetime.strptime(iso[:10], "%Y-%m-%d").strftime("%b %Y")


def main():
    apply = "--apply" in sys.argv
    today = date.today().isoformat()
    d = json.loads(DATA.read_text())
    listed = {(p["repo"].lower(), p["number"]): p for p in d["prs"]}
    known_repos = {r.lower(): r for r in d["projects"]}
    changes, review, invisible = [], [], []

    for c in d["contributors"]:
        gh = c["github"]
        items = search(f"author:{gh} is:pr")
        time.sleep(3)
        if not items:
            invisible.append(c["name"])
            continue
        for it in items:
            repo = it["repository_url"].split("/repos/")[1]
            key = (repo.lower(), it["number"])
            merged_at = (it.get("pull_request") or {}).get("merged_at")
            state = "merged" if merged_at else it["state"]  # open | closed (unmerged)
            p = listed.get(key)
            link = it["html_url"]
            if p:
                if p["status"] == "open" and state == "merged":
                    changes.append(f"MERGED  {c['name']}: {link}")
                    if apply:
                        p.update(status="merged", month=month(merged_at), firstSeen=today)
                elif p["status"] == "open" and state == "closed":
                    changes.append(f"CLOSED  {c['name']}: {link} (removed)")
                    if apply:
                        d["prs"].remove(p)
                elif p["status"] == "merged" and state != "merged":
                    review.append(f"Listed as merged but GitHub says {state}: {link}")
                continue
            if state == "closed":
                continue
            owner = repo.split("/")[0].lower()
            if owner == gh.lower():
                continue  # own account: never counted
            when = merged_at or it["created_at"]
            if repo.lower() in known_repos:
                if when[:10] < "2026-01-01" and state == "merged":
                    continue  # old history already decided by hand
                changes.append(f"NEW {state.upper():6} {c['name']}: {link} {it['title']}")
                if apply:
                    d["prs"].append({"github": gh, "repo": known_repos[repo.lower()], "number": it["number"],
                                     "status": state, "month": month(when), "firstSeen": today})
                    listed[key] = d["prs"][-1]
            elif when >= (d["checked"]):
                review.append(f"New repo, check scope: {c['name']} {state}: {link} {it['title']}")

    print(f"# Recount {today} (last: {d['checked']})\n")
    print("## Changes" + (" applied" if apply else " (run with --apply)"))
    print("\n".join(f"- {x}" for x in changes) or "- none")
    print("\n## Needs a human")
    print("\n".join(f"- {x}" for x in review) or "- none")
    if invisible:
        print(f"- GitHub search shows no PRs for: {', '.join(invisible)}. Check their repos by hand "
              "(git log of the project, refs/pull/N/head and refs/pull/N/merge).")
    print("- For every newly merged PR, check it wasn't merged by its own author (merge commit author).")
    if apply:
        d["checked"] = today
        DATA.write_text(json.dumps(d, indent=1, ensure_ascii=False))
        subprocess.run([sys.executable, str(ROOT / "tools" / "build.py")], check=True)


if __name__ == "__main__":
    main()
