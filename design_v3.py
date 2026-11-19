# Design v3 (Nov 2026): a picture in every reading-page hero, a desktop side column
# (on-this-page menu + ask-an-expert card) and YouTube farmer videos on matching pages.
# Executed from build.py; uses its helpers (esc, sec, btn_wa, ROOT, SITE, CROPS, ARTICLES).
exec(open(os.path.join(ROOT, "content_videos.py"), encoding="utf-8").read())
from PIL import Image as _PI

_SIDE_DIR = os.path.join(ROOT, "assets", "media", "side")
os.makedirs(_SIDE_DIR, exist_ok=True)
def _side_img(src_rel, name):
    """640x480 crop of an existing photo, small enough to be the page's first image without slowing it."""
    out = os.path.join(_SIDE_DIR, name + ".webp")
    if not os.path.exists(out):
        im = _PI.open(os.path.join(ROOT, src_rel)).convert("RGB")
        w, h = im.size; t = 4 / 3
        if w / h > t: nw = int(h * t); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
        else: nh = int(w / t); top = max(0, int((h - nh) * 0.35)); im = im.crop((0, top, w, top + nh))
        im.resize((560, 420), _PI.LANCZOS).save(out, "WEBP", quality=66, method=6)
    return f"/assets/media/side/{name}.webp"

_CROP_PHOTO = {c["slug"]: c["name"] for c in CROPS if os.path.exists(os.path.join(ROOT, "assets", "media", f"crop-{c['slug']}-hero.webp"))}
_KW = [("sugarcane", "sugarcane"), ("ratoon", "sugarcane"), ("गन्न", "sugarcane"), ("mango", "mango"), ("kesar", "mango"), ("potato", "potato"), ("apple", "apple"),
       ("citrus", "citrus"), ("lemon", "citrus"), ("banana", "banana"), ("cotton", "cotton"), ("कपास", "cotton"), ("chilli", "chilli"), ("tomato", "vegetables"),
       ("vegetable", "vegetables"), ("onion", "onion"), ("cumin", "cumin"), ("paddy", "paddy"), ("rice", "paddy"), ("maize", "maize"), ("groundnut", "groundnut"),
       ("coconut", "coconut"), ("pomegranate", "pomegranate"), ("tea", "tea"), ("fruit", "fruits")]
_FIELD = [f"gallery/field-{i:02d}.webp" for i in range(1, 17) if os.path.exists(os.path.join(ROOT, "assets", "media", "gallery", f"field-{i:02d}.webp"))]
ELEM = {"zinc": ("Zn", 30, "Zinc"), "boron": ("B", 5, "Boron"), "iron": ("Fe", 26, "Iron"), "manganese": ("Mn", 25, "Manganese"), "copper": ("Cu", 29, "Copper"),
        "molybdenum": ("Mo", 42, "Molybdenum"), "chlorine": ("Cl", 17, "Chlorine"), "nickel": ("Ni", 28, "Nickel"), "cobalt": ("Co", 27, "Cobalt"),
        "silicon": ("Si", 14, "Silicon"), "calcium": ("Ca", 20, "Calcium"), "magnesium": ("Mg", 12, "Magnesium"), "sulphur": ("S", 16, "Sulphur")}
_READ = ("/guides/", "/articles/", "/crop-problems/", "/knowledge/", "/micronutrients/")

def _crop_of(path, h1):
    if path.startswith("/articles/"):
        a = next((a for a in ARTICLES if a["slug"] == path.split("/")[2]), None)
        if a and a.get("crop") in _CROP_PHOTO: return a["crop"]
    t = (path + " " + h1).lower()
    return next((c for k, c in _KW if k in t and c in _CROP_PHOTO), None)

def side_visual(path, h1):
    seg = path.strip("/").split("/")
    if seg[0] == "micronutrients" and len(seg) > 1 and seg[1] in ELEM:
        s, n, name = ELEM[seg[1]]
        return f'<div class="el"><span class="el-n">{n}</span><span class="el-s">{s}</span><span class="el-name">{name}</span></div>'
    c = _crop_of(path, h1)
    if c:
        src, alt = _side_img(f"assets/media/crop-{c}-hero.webp", c), f"{_CROP_PHOTO[c]} crop in the field"
    elif _FIELD:
        f = _FIELD[sum(map(ord, path)) % len(_FIELD)]
        src, alt = _side_img(f"assets/media/{f}", os.path.basename(f)[:-5]), "Field visit with farmers by the Gujarat Bio Organics team"
    else: return ""
    return f'<figure class="leaf"><img src="{src}" alt="{esc(alt)}" width="560" height="420" fetchpriority="high" decoding="async"></figure>'

def _slug(t): return re.sub(r"[^a-z0-9]+", "-", H.unescape(re.sub("<[^>]+>", "", t)).lower()).strip("-")[:48] or "s"

def side_column(prose):
    """Adds ids to h2s and returns (prose, aside)."""
    seen, toc = set(), []
    def rep(m):
        txt = m.group(1); i = _slug(txt)
        while i in seen: i += "-2"
        seen.add(i); toc.append((i, txt))
        return f'<h2 id="{i}">{txt}</h2>'
    prose = re.sub(r"<h2>(.*?)</h2>", rep, prose)
    nav = ('<nav class="otp" aria-label="On this page"><p class="otp-h">On this page</p><ol>' +
           "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc) + "</ol></nav>") if len(toc) >= 3 else ""
    ask = f'<div class="ask"><p class="ask-h">Problem in your field?</p><p>Send a photo of the crop on WhatsApp. Our team replies with what to check.</p>{btn_wa("Hello, I have a question about my crop.", "Send a photo")}</div>'
    return prose, f'<aside class="side">{nav}{ask}</aside>'

def video_block(path):
    vs = VIDEOS.get(path, [])[:2]
    if not vs: return "", []
    figs = "".join(f'<figure class="yt"><div class="yt-f"><iframe loading="lazy" src="https://www.youtube.com/embed/{v[0]}?rel=0" title="{esc(v[3])}" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div><figcaption>{esc(v[3])}</figcaption></figure>' for v in vs)
    html = sec(f'<div class="vgrid">{figs}</div><p class="note">From our YouTube channel. Farmers describe their own fields; results differ with soil, weather and care.</p>', "Watch: from the field", id="watch")
    ld = [{"@context": "https://schema.org", "@type": "VideoObject", "name": v[3][:100], "description": f"{v[3]}. A video from the Gujarat Bio Organics YouTube channel.",
           "thumbnailUrl": f"https://i.ytimg.com/vi/{v[0]}/hqdefault.jpg", "uploadDate": v[1] + "T09:00:00+05:30", "duration": v[2],
           "embedUrl": f"https://www.youtube.com/embed/{v[0]}", "publisher": {"@id": SITE + "/#org"}} for v in vs]
    return html, ld

def enhance(path, body):
    """Returns (body, extra_ld). Reading pages get the hero picture and side column; mapped pages get videos."""
    extra = []
    if path.startswith(_READ) and path.count("/") >= 2 and '<section class="hero light">' in body and "hero-grid" not in body[:3000]:
        m = re.search(r'<section class="hero light"><div class="wrap">(.*?)</div></section>', body, re.S)
        h1 = re.search(r"<h1>(.*?)</h1>", m.group(1)).group(1) if m else ""
        vis = side_visual(path, H.unescape(h1)) if m else ""
        if vis:
            body = body[:m.start()] + f'<section class="hero light hero-pic"><div class="wrap"><div class="hero-grid"><div>{m.group(1)}</div><div class="hero-vis">{vis}</div></div></div></section>' + body[m.end():]
        k = body.find('<section class="sec"><div class="wrap"><div class="prose">')
        if k > 0:
            e = body.find("</section>", k)
            seg = body[k:e]
            a = seg.find('<div class="prose">') + len('<div class="prose">'); b = seg.rfind("</div></div>")
            prose, aside = side_column(seg[a:b])
            body = body[:k] + seg[:a - len('<div class="prose">')] + f'<div class="artgrid"><div class="prose">{prose}</div>{aside}</div>' + seg[b + 6:] + body[e:]
    hm = re.search(r'<section class="hero[^"]*">.*?</section>', body, re.S)  # first photo in the hero: load it first (LCP)
    if hm and 'loading="lazy"' in hm.group(0):
        hs = hm.group(0).replace('loading="lazy"', 'fetchpriority="high"', 1)
        mm = re.search(r'src="/assets/media/([^"]+\.webp)"[^>]*width="(\d+)" height="(\d+)"', hs)
        if mm and os.path.getsize(os.path.join(ROOT, "assets", "media", mm.group(1))) > 90000:
            fn = mm.group(1); w, h = int(mm.group(2)), int(mm.group(3)); nw = min(w, 600); nh = round(h * nw / w)
            out = os.path.join(_SIDE_DIR, os.path.basename(fn)[:-5] + "-h.webp")
            if not os.path.exists(out): _PI.open(os.path.join(ROOT, "assets", "media", fn)).convert("RGB").resize((nw, nh), _PI.LANCZOS).save(out, "WEBP", quality=60, method=6)
            if os.path.getsize(out) < 0.7 * os.path.getsize(os.path.join(ROOT, "assets", "media", fn)):
              hs = hs.replace(f'src="/assets/media/{fn}"', f'src="/assets/media/side/{os.path.basename(out)}"', 1).replace(f'width="{w}" height="{h}"', f'width="{nw}" height="{nh}"', 1)
        body = body[:hm.start()] + hs + body[hm.end():]
    vb, extra = video_block(path)
    if vb:
        j = body.rfind("<section")
        body = body[:j] + vb + body[j:] if j > 0 else body + vb
    return body, extra
