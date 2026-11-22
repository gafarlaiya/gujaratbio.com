#!/usr/bin/env python3
"""List English pages added or changed in the last N days (default 7), with titles, for the weekly posting batch
and for Search Console 'Request indexing'. Usage: python3 new_links.py [days]  -> prints and writes NEW-LINKS.md"""
import re, sys, html, datetime, os
days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
since = (datetime.date.today() - datetime.timedelta(days=days)).isoformat()
xml = open("sitemap.xml", encoding="utf-8").read()
rows = []
for u, d in re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", xml):
    path = u.split("gujaratbio.com", 1)[1] or "/"
    if d < since or path.startswith(("/gu/", "/hi/")) or path in ("/gu", "/hi"):
        continue
    f = os.path.join(path.strip("/"), "index.html") if path != "/" else "index.html"
    t = ""
    if os.path.exists(f):
        m = re.search(r"<title>([^<]*)</title>", open(f, encoding="utf-8").read())
        t = html.unescape(m.group(1)) if m else ""
    rows.append((d, u, t))
rows.sort(reverse=True)
out = [f"# New or changed pages since {since}", "",
       "Use for: (1) Search Console > URL Inspection > Request indexing (about 10 a day), (2) the weekly approved posting batch.", ""]
out += [f"- {d}  {u}  |  {t}" for d, u, t in rows]
open("NEW-LINKS.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))
