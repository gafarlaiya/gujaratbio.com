# Auto-publishing helper: find every English string on the translated pages that has no Hindi or Gujarati translation yet.
# Usage (after python3 build.py):
#   python3 i18n/missing_auto.py <tag> [--add /articles/slug-1 /articles/slug-2 ...]
# --add puts new pages into i18n/pages.json first (they get /hi/ and /gu/ versions once fully translated).
# Writes i18n/src<tag>.json (the English keys) and i18n/src<tag>.txt ("### path" headers, then "N<TAB>English").
# Translate each line into i18n/tr/hi<tag>_01.tsv and i18n/tr/gu<tag>_01.tsv as "N<TAB>translation" (keep every tag and href),
# then run: python3 i18n/merge.py && python3 build.py   (build prints "incomplete: {}" when every page is complete)
import json, os, re, sys, subprocess
from bs4 import BeautifulSoup
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import units, inner, page_file, ROOT

tag = sys.argv[1]
assert re.fullmatch(r"[a-z]\w+", tag), "tag like a20261109"
pj = os.path.join(ROOT, "i18n", "pages.json")
pages = json.load(open(pj))
if "--add" in sys.argv:
    for p in sys.argv[sys.argv.index("--add") + 1:]:
        if p not in pages: pages.append(p)
    json.dump(pages, open(pj, "w"), indent=0)
hi = json.load(open(os.path.join(ROOT, "i18n", "hi.json"), encoding="utf-8"))
gu = json.load(open(os.path.join(ROOT, "i18n", "gu.json"), encoding="utf-8"))
keys, lines, seen = [], [], set()
for p in pages:
    s = BeautifulSoup(open(page_file(p), encoding="utf-8").read(), "lxml")
    vals = [s.title.get_text() if s.title else ""] + [m.get("content", "") for m in s.find_all("meta", attrs={"name": "description"})] \
         + [i.get("alt", "") for i in s.find_all("img") if i.get("alt")] + [x.get("aria-label") for x in s.find_all(attrs={"aria-label": True})]
    vals = [v for v in vals if v and re.search("[A-Za-z]", v)] + [h for h in (inner(u) for u in units(s)) if re.search("[A-Za-z]{2}", re.sub("<[^>]+>", "", h))]
    new = [v for v in vals if v not in seen and (v not in hi or v not in gu)]
    if new: lines.append(f"### {p}")
    for v in new:
        seen.add(v); lines.append(f"{len(keys)}\t{v}"); keys.append(v)
json.dump(keys, open(os.path.join(ROOT, "i18n", f"src{tag}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
open(os.path.join(ROOT, "i18n", f"src{tag}.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(len(keys), "strings to translate ->", f"i18n/src{tag}.txt")
