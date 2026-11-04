# Extract translatable text units from built English pages: top-most elements whose content is only inline markup.
import os, re, json, sys
from bs4 import BeautifulSoup, NavigableString, Comment
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INLINE = {"a", "b", "strong", "em", "i", "br", "span", "small", "sup", "sub", "u", "abbr", "code"}
SKIP = {"script", "style", "noscript", "svg", "iframe", "video", "template"}
ATTRS = [("meta", "content", {"name": "description"}), ("meta", "content", {"property": "og:title"}), ("meta", "content", {"property": "og:description"})]

def is_inline_only(el):
    for c in el.descendants:
        if isinstance(c, Comment): continue
        if getattr(c, "name", None) and c.name not in INLINE: return False
    return True

def _direct_text(el):
    return any(isinstance(x, NavigableString) and not isinstance(x, Comment) and x.strip() for x in el.children)

def units(soup):
    out = []
    def take(c):
        kids = [k for k in c.children if getattr(k, "name", None)]
        if not _direct_text(c) and len(kids) >= 2:   # e.g. a menu of links, or <b>title</b><span>line</span>: one unit each
            for k in kids:
                if k.get_text(strip=True): take(k)
        else:
            out.append(c)
    def walk(el):
        for c in el.children:
            if isinstance(c, NavigableString) or not getattr(c, "name", None): continue
            if c.name in SKIP: continue
            has_text = c.get_text(strip=True) != ""
            if has_text and is_inline_only(c) and (c.name not in INLINE or (c.parent is not None and not is_inline_only(c.parent))):
                take(c); continue
            walk(c)
    walk(soup.body if soup.body else soup)
    return out

def inner(el): return "".join(str(x) for x in el.contents).strip()

def page_file(p): return os.path.join(ROOT, p.strip("/"), "index.html") if p != "/" else os.path.join(ROOT, "index.html")

if __name__ == "__main__":
    paths = json.load(open(os.path.join(ROOT, "i18n", "pages.json")))
    seen = {}
    for p in paths:
        s = BeautifulSoup(open(page_file(p), encoding="utf-8").read(), "lxml")
        t = s.title.get_text() if s.title else ""
        for v in [t] + [m.get("content", "") for m in s.find_all("meta", attrs={"name": "description"})] + [i.get("alt", "") for i in s.find_all("img") if i.get("alt")] + [x.get("aria-label") for x in s.find_all(attrs={"aria-label": True})]:
            if v and re.search("[A-Za-z]", v): seen.setdefault(v, p)
        for u in units(s):
            h = inner(u)
            if re.search("[A-Za-z]{2}", re.sub("<[^>]+>", "", h)): seen.setdefault(h, p)
    json.dump(list(seen.keys()), open(os.path.join(ROOT, "i18n", "strings_en.json"), "w"), ensure_ascii=False, indent=0)
    print(len(seen), "strings,", sum(len(re.sub("<[^>]+>", "", k)) for k in seen), "chars of text")
