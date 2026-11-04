# Builds /gu/... and /hi/... versions of selected English pages from the built HTML, using the translation
# dictionaries in i18n/<lang>.json ({english inner HTML: translated inner HTML}).
# A page is published in a language only when every text unit on it has a translation (no mixed-language pages).
# Run after build.py (build.py calls it at the end).
import os, re, json, html as H, sys
from bs4 import BeautifulSoup
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import units, inner, page_file, ROOT

SITE = "https://www.gujaratbio.com"
LANGS = {"gu": "ગુજરાતી", "hi": "हिन्दी"}
LOCALE = {"en": "en-IN", "gu": "gu-IN", "hi": "hi-IN"}

def load(lang):
    f = os.path.join(ROOT, "i18n", f"{lang}.json")
    return json.load(open(f, encoding="utf-8")) if os.path.exists(f) else {}

def tr_text(d, v):
    """Translate a plain-text value (attribute, title, JSON-LD) using the HTML-keyed dictionary."""
    if v in d: return H.unescape(re.sub("<[^>]+>", "", d[v]))
    e = H.escape(v, quote=False)
    if e in d: return H.unescape(re.sub("<[^>]+>", "", d[e]))
    return None

def missing(soup, d):
    out = []
    for u in units(soup):
        h = inner(u)
        if re.search("[A-Za-z]{2}", re.sub("<[^>]+>", "", h)) and h not in d: out.append(h)
    for v in [soup.title.get_text() if soup.title else ""] + [m.get("content", "") for m in soup.find_all("meta", attrs={"name": "description"})] + \
             [i.get("alt", "") for i in soup.find_all("img") if i.get("alt")] + [x.get("aria-label") for x in soup.find_all(attrs={"aria-label": True})]:
        if v and re.search("[A-Za-z]{2}", v) and tr_text(d, v) is None: out.append(v)
    return out

def lpath(lang, p): return f"/{lang}" + ("" if p == "/" else p)

def switcher(cur, p, avail):
    items = []
    for lg, label in [("en", "English")] + list(LANGS.items()):
        href = p if lg == "en" else (lpath(lg, p) if lg in avail else lpath(lg, "/") if "/" in DONE.get(lg, set()) else None)
        if not href: continue
        a = f'<a href="{href}" hreflang="{lg}"' + (' aria-current="true"' if lg == cur else "") + f'>{label}</a>'
        items.append(a)
    return '<div class="langsw" aria-label="Language">' + "".join(items) + "</div>"

def alt_links(p, avail):
    s = f'<link rel="alternate" hreflang="en-IN" href="{SITE}{p}"><link rel="alternate" hreflang="x-default" href="{SITE}{p}">'
    for lg in avail: s += f'<link rel="alternate" hreflang="{LOCALE[lg]}" href="{SITE}{lpath(lg, p)}">'
    return s

def put_switcher(s, html):
    strip = s.select_one("div.strip div.wrap")
    el = BeautifulSoup(html, "lxml").div
    if strip and strip.find("span"): strip.find("span").replace_with(el)
    else: (s.find("header") or s.body).insert(0, el)

def ld_tr(o, d):
    if isinstance(o, dict): return {k: (ld_tr(v, d) if k not in ("@context", "@type", "@id", "url", "item", "mainEntityOfPage", "image", "logo", "sameAs") else v) for k, v in o.items()}
    if isinstance(o, list): return [ld_tr(x, d) for x in o]
    if isinstance(o, str):
        t = tr_text(d, o); return t if t is not None else o
    return o

PAGES = json.load(open(os.path.join(ROOT, "i18n", "pages.json")))
DICT = {lg: load(lg) for lg in LANGS}
DONE = {lg: set() for lg in LANGS}
REPORT = {}
for lg in LANGS:
    for p in PAGES:
        s = BeautifulSoup(open(page_file(p), encoding="utf-8").read(), "lxml")
        m = missing(s, DICT[lg])
        if m:
            REPORT.setdefault(lg, {})[p] = len(m)
            if os.environ.get("I18N_DEBUG"): print("MISSING", lg, p, m[:4])
        else: DONE[lg].add(p)

for lg in LANGS:
    d = DICT[lg]
    for p in sorted(DONE[lg]):
        s = BeautifulSoup(open(page_file(p), encoding="utf-8").read(), "lxml")
        for u in units(s):
            h = inner(u)
            if h in d:
                u.clear(); u.append(BeautifulSoup(d[h], "lxml").body or "")
                if u.body: u.body.unwrap()
        for sv in s.find_all("svg"):          # buttons with an icon: translate the text next to the icon
            par = sv.parent
            for t in list(par.children):
                if isinstance(t, str) and t.strip() and t.strip() in d:
                    t.replace_with(t.replace(t.strip(), d[t.strip()]))
        for el in s.find_all(["img"]):
            if el.get("alt"): el["alt"] = tr_text(d, el["alt"]) or el["alt"]
        for el in s.find_all(attrs={"aria-label": True}):
            el["aria-label"] = tr_text(d, el["aria-label"]) or el["aria-label"]
        if s.title: s.title.string = tr_text(d, s.title.get_text()) or s.title.get_text()
        for m in s.find_all("meta"):
            if m.get("name") == "description" or m.get("property") in ("og:title", "og:description"):
                m["content"] = tr_text(d, m["content"]) or m["content"]
            if m.get("property") == "og:url": m["content"] = SITE + lpath(lg, p)
        for c in s.find_all("link", rel="canonical"): c["href"] = SITE + lpath(lg, p)
        for sc in s.find_all("script", type="application/ld+json"):
            try: sc.string = json.dumps(ld_tr(json.loads(sc.string), d), ensure_ascii=False)
            except Exception: pass
        # internal links to pages that exist in this language
        for a in s.find_all("a", href=True):
            hr = a["href"]
            if hr.startswith("/") and not hr.startswith("/assets") and not hr.startswith(f"/{lg}/"):
                base, frag = (hr.split("#", 1) + [""])[:2]
                base = base.rstrip("/") or "/"
                if base in DONE[lg]: a["href"] = lpath(lg, base) + (f"#{frag}" if frag else "")
        s.html["lang"] = lg
        avail = [x for x in LANGS if p in DONE[x]]
        s.head.append(BeautifulSoup(alt_links(p, avail), "lxml").head)
        if s.head.head: s.head.head.unwrap()
        put_switcher(s, switcher(lg, p, avail))
        out = os.path.join(ROOT, lg, p.strip("/"), "index.html") if p != "/" else os.path.join(ROOT, lg, "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(str(s))

# English pages: add hreflang and the switcher where a translation exists
for p in PAGES:
    avail = [x for x in LANGS if p in DONE[x]]
    if not avail: continue
    f = page_file(p); s = BeautifulSoup(open(f, encoding="utf-8").read(), "lxml")
    s.head.append(BeautifulSoup(alt_links(p, avail), "lxml").head)
    if s.head.head: s.head.head.unwrap()
    put_switcher(s, switcher("en", p, avail))
    open(f, "w", encoding="utf-8").write(str(s))

# sitemap
sm_f = os.path.join(ROOT, "sitemap.xml")
if os.path.exists(sm_f) and any(DONE.values()):
    sm = open(sm_f, encoding="utf-8").read()
    add = "".join(f'<url><loc>{SITE}{lpath(lg, p)}</loc><priority>0.6</priority></url>\n' for lg in LANGS for p in sorted(DONE[lg]))
    sm = sm.replace("</urlset>", add + "</urlset>")
    open(sm_f, "w", encoding="utf-8").write(sm)
print("languages:", {lg: len(DONE[lg]) for lg in LANGS}, "incomplete:", {lg: len(v) for lg, v in REPORT.items()})
