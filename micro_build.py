# Renders the /micronutrients section. exec'd from build.py after the knowledge pages, so it uses the
# site helpers (render, hero, sec, answer, faq_html, faq_ld, article_ld, card, enquiry_box, esc, PBY, CBY ...).

MBASE = "/micronutrients"
EBY = {e["slug"]: e for e in ELEMENTS}
MICRO_DATE = "2026-11-04"
GROUP_ORDER = [("Micronutrient", "Micronutrients"), ("Secondary nutrient", "Secondary nutrients"), ("Beneficial element", "Beneficial elements")]

def _src_note():
    return f'<p class="note">Indian soil figures: {ICAR_SRC} <a href="{ICAR_URL}" rel="noopener">Read the study</a>. The figures include soils with a hidden (latent) shortage.</p>'

def _specials_box(crops):
    """Link the Immunity Special for each listed crop, without claiming what the formula contains."""
    items = []
    for cs in crops:
        c = CBY.get(cs)
        if not c: continue
        p = PBY.get(c["product"])
        if not p: continue
        items.append(f'<li><a href="/crops/{cs}">{esc(c["name"])} guide</a> and <a href="/products/{p["slug"]}">{esc(p["name"])}</a></li>')
    lst = "<ul>" + "".join(dict.fromkeys(items)) + "</ul>" if items else ""
    return sec(f'<div class="prose"><p>Since 2006, lakhs of farmers from Kashmir to Kanyakumari have used Immunity products on almost every crop: from the mango farms around Somnath to the apple orchards of Himachal Pradesh and Kashmir, the tea estates of Assam and Darjeeling, and the banana, coconut and cardamom farms of Tamil Nadu, Karnataka and Kerala. Each Special is one formula made for one crop and its common problems. Tell us your crop, soil test and what you see, and our team will tell you what to check, whether a micronutrient correction is needed, and which Special fits your programme.</p>{lst}'
               f'<div class="btns">{btn_wa("Hello Gujarat Bio Organics, my crop shows a nutrient problem. Crop: ___ What I see: ___", "WhatsApp a photo")}{btn_enq("Send enquiry")}</div><p class="note">{RESULTS}</p></div>',
               "How Gujarat Bio Organics can help", tint=True)

def micro_page(path, crumbs, x, extra="", schema_type="Article"):
    """x: slug,title,h1,desc,answer,sections[(h, items)],faq. crumbs: list of (name, url) ending with (current, None)."""
    start(path)
    body = hero(cap(x["h1"]), x["desc"], crumbs, light=True)
    inner = answer(x["answer"]) + f'<p class="note">By Gafar Laiya and the {SHORT} team. Updated November 2026.</p>'
    toc = [h for h, _ in x["sections"]]
    if len(toc) > 3:
        inner += '<div class="toc"><b>On this page</b><ol>' + "".join(f'<li><a href="#s{i}">{esc(h)}</a></li>' for i, h in enumerate(toc)) + "</ol></div>"
    inner += "".join(f'<h2 id="s{i}">{esc(h)}</h2>' + body_of(items) for i, (h, items) in enumerate(x["sections"]))
    inner += f'<p class="note">Doses depend on the crop, soil and product, so this page gives methods, not amounts. Take the dose from your soil test report, the product label or your local agriculture officer or KVK. {RESULTS}</p>'
    body += sec(f'<div class="prose">{inner}</div>') + extra
    if x.get("faq"): body += sec(faq_html(x["faq"]), "Questions", tint=True)
    sch = [article_ld(path, x["h1"], x["desc"], MICRO_DATE)] + ([faq_ld(x["faq"])] if x.get("faq") else [])
    render(path, x["title"], x["desc"], body, sch, crumbs, "0.7")

def _rel(items, title="Read next"):
    return sec('<div class="grid">' + "".join(card(u, t, d, m) for u, t, d, m in items) + "</div>", title)

# ------------------------------------------------------------ element pages and their two blogs
for e in ELEMENTS:
    ep = f"{MBASE}/{e['slug']}"
    nm = e["name"]; low = nm.split(" (")[0].lower()
    b1, b2 = e["blog1"], e["blog2"]
    b1p, b2p = f"{ep}/{b1['slug']}", f"{ep}/{b2['slug']}"
    pct = (f'<p>In India, an ICAR survey of more than two lakh soil samples found {e["pct"]} of soils short of {low}, counting hidden shortages.</p>' if e["pct"] else "")
    crops_tbl = T(["Crop", "What a shortage looks like"], [[esc(c), esc(s)] for c, s in e["crops"][:5]])
    secs = [(f"What {low} does in the plant", e["roles"]),
            (f"How {low} moves in the plant", [P(esc(e["mobility"]))]),
            (f"Signs of {low} deficiency", e["symptoms"]),
            ("Crop by crop", [crops_tbl, P(f'More crops and look-alikes: <a href="{b1p}">{esc(b1["h1"])}</a>.')]),
            ("Where and why it happens", [("html", pct)] + e["risk"] if pct else e["risk"]),
            ("How it works with other nutrients", e["interactions"] + [f'See <a href="{MBASE}/nutrient-interactions">nutrient interactions</a>.']),
            ("What happens if it is not managed", e["consequences"] + [f'See <a href="{MBASE}/consequences-of-micronutrient-deficiency">the full picture of what unmanaged shortages cost</a>.']),
            ("How to confirm it", e["diagnose"]),
            ("How to correct it", e["correct"]),
            (f"Too much {low}", e["excess"])]
    kind = e["kind"].lower()
    x = dict(title=f"{nm.split(' (')[0]} in Plants: Role, Deficiency Signs and Correction | GBO", h1=f"{nm} ({e['sym']}) in crops: role, deficiency signs and how to correct it",
             desc=f"What {low} does in crops, how a shortage looks in each crop, why it happens, what it costs if ignored, and how growers confirm and correct it.",
             answer=e["answer"], sections=secs, faq=e["faq"])
    if len(x["title"]) > 66: x["title"] = f"{nm.split(' (')[0]}: Role in Plants, Deficiency and Correction | GBO"
    if len(x["title"]) > 66: x["title"] = f"{nm.split(' (')[0]} in Plants: Deficiency and Correction | GBO"
    others = [o for o in ELEMENTS if o["slug"] != e["slug"]]
    extra = _rel([(b1p, b1["h1"], b1["desc"], "Blog"), (b2p, b2["h1"], b2["desc"], "Blog"), (f"{MBASE}/deficiency-symptoms", "Read the leaves: symptom guide", "Which nutrient each pattern points to.", "Guide")], f"More on {low}") \
          + _specials_box(e["crop_links"]) \
          + sec('<div class="chips">' + "".join(f'<a href="{MBASE}/{o["slug"]}">{esc(o["name"].split(" (")[0])}</a>' for o in others) + "</div>", "Other nutrients")
    micro_page(ep, [("Micronutrients", MBASE), (nm.split(" (")[0], None)], x, extra)

    # blog 1: crop by crop symptoms
    rows = T(["Crop", "What you see"], [[esc(c), esc(s)] for c, s in e["crops"]])
    bx = dict(b1); bx["sections"] = [("Crop by crop", [rows])] + b1["sections"] + [("Confirm and correct", ["Confirm with a soil or leaf test before you spend.", f'Read the full <a href="{ep}">{low} guide</a> for causes and correction.', f'Use the <a href="{MBASE}/deficiency-symptoms">symptom guide</a> to compare with other nutrients.'])]
    bx.setdefault("faq", [(f"What does {low} deficiency look like in {c.split(':')[0].lower()}?", s) for c, s in e["crops"][:3]])
    micro_page(b1p, [("Micronutrients", MBASE), (nm.split(" (")[0], ep), (_cr(b1["h1"]), None)], bx,
               _rel([(ep, f"{nm} guide", e["answer"][:140].rsplit(" ", 1)[0] + "...", "Guide"), (b2p, b2["h1"], b2["desc"], "Blog")]) + _specials_box(e["crop_links"]))
    # blog 2: the special topic
    bx = dict(b2); bx["sections"] = b2["sections"] + [("Read more", [f'The full <a href="{ep}">{low} guide</a>.', f'<a href="{b1p}">{esc(b1["h1"])}</a>.'])]
    micro_page(b2p, [("Micronutrients", MBASE), (nm.split(" (")[0], ep), (_cr(b2["h1"]), None)], bx,
               _rel([(ep, f"{nm} guide", e["answer"][:140].rsplit(" ", 1)[0] + "...", "Guide"), (b1p, b1["h1"], b1["desc"], "Blog")]) + _specials_box(e["crop_links"]))

# ------------------------------------------------------------ general pages and blogs
GEN_CARDS = [(f"{MBASE}/{g['slug']}", g["h1"], g["desc"], "Guide") for g in GEN_PAGES]
BLOG_CARDS = [(f"{MBASE}/guides/{g['slug']}", g["h1"], g["desc"], "Blog") for g in GEN_BLOGS]
for g in GEN_PAGES:
    p = f"{MBASE}/{g['slug']}"
    micro_page(p, [("Micronutrients", MBASE), (_cr(g["h1"]), None)], g, _rel([c for c in GEN_CARDS if c[0] != p][:3]) + _specials_box(["mango", "sugarcane", "potato", "cotton"]))
start(f"{MBASE}/guides")
render(f"{MBASE}/guides", "Micronutrient Guides and Blogs for Farmers | GBO", "Practical blogs on micronutrients: why sprays and urea do not fix nutrient problems, fruit quality and brix, soil health and types of micronutrient fertilizers.",
       hero("Micronutrient blogs", "Practical reading on nutrient problems farmers meet in the field.", [("Micronutrients", MBASE), ("Blogs", None)], light=True)
       + sec('<div class="grid">' + "".join(card(u, t, d, m) for u, t, d, m in BLOG_CARDS) + "</div>", "General")
       + sec('<div class="grid">' + "".join(card(f"{MBASE}/{e['slug']}/{b['slug']}", b["h1"], b["desc"], e["name"].split(" (")[0]) for e in ELEMENTS for b in (e["blog1"], e["blog2"])) + "</div>", "By nutrient", tint=True),
       None, [("Micronutrients", MBASE), ("Blogs", None)], "0.6")
for g in GEN_BLOGS:
    p = f"{MBASE}/guides/{g['slug']}"
    micro_page(p, [("Micronutrients", MBASE), ("Blogs", f"{MBASE}/guides"), (_cr(g["h1"]), None)], g, _rel([c for c in BLOG_CARDS if c[0] != p][:3]) + _specials_box(["mango", "sugarcane", "potato", "cotton"]))

# ------------------------------------------------------------ hub
start(MBASE)
groups_tbl = T(["Group", "Nutrients", "Needed in"], [
    ["Major nutrients", "Nitrogen (N), phosphorus (P), potassium (K)", "Large amounts"],
    ["Secondary nutrients", '<a href="/micronutrients/calcium">Calcium (Ca)</a>, <a href="/micronutrients/magnesium">magnesium (Mg)</a>, <a href="/micronutrients/sulphur">sulphur (S)</a>', "Moderate amounts"],
    ["Micronutrients (trace elements)", ", ".join(f'<a href="{MBASE}/{e["slug"]}">{esc(e["name"].split(" (")[0].lower())} ({e["sym"]})</a>' for e in ELEMENTS if e["kind"] == "Micronutrient"), "Very small amounts"],
    ["Beneficial elements", '<a href="/micronutrients/silicon">Silicon (Si)</a>, <a href="/micronutrients/cobalt">cobalt (Co)</a>, sodium (Na), selenium (Se)', "Useful for some crops or for the microbes and animals that depend on them"]])
el_tbl = T(["Nutrient", "Group", "Main job in the plant", "Shows first on", "Indian soils short*"], [
    [f'<a href="{MBASE}/{e["slug"]}">{esc(e["name"])} ({e["sym"]})</a>', esc(e["kind"]), esc(cap(e["short"])),
     {"zinc": "Young leaves", "iron": "Youngest leaves", "manganese": "Young and middle leaves", "copper": "Shoot tips", "boron": "Tips, flowers, fruit", "molybdenum": "Old leaves", "chlorine": "Old leaf tips (excess)",
      "nickel": "Leaf tips", "calcium": "Fruit, tips, roots", "magnesium": "Old leaves", "sulphur": "Young leaves", "silicon": "Whole plant (weak stems)", "cobalt": "Legume nodules"}[e["slug"]], e["pct"] or "Not surveyed"] for e in ELEMENTS])
hub = dict(h1="Micronutrients in agriculture: what they are, how they work and why they matter",
 desc="Micronutrients and trace elements for farmers: the full list, what each does, deficiency signs, fertilizer types, and how to diagnose and correct problems.",
 answer="Micronutrients are the nutrients a crop needs in very small amounts: zinc, iron, manganese, copper, boron, molybdenum, chlorine and nickel. They switch on the enzymes, hormones and processes that let the crop use nitrogen, phosphorus and potassium, form chlorophyll, flower, set fruit and resist stress. A shortage of any one limits the whole crop, however much NPK is applied, and Indian soil tests show such shortages are widespread.",
 sections=[("What are micronutrients?", [P("Plants need 17 essential nutrients. Carbon, hydrogen and oxygen come from air and water. The rest come from the soil and fall into groups by how much the crop needs. Micronutrients, also called trace elements, are needed in grams per acre rather than kilograms, but a crop cannot complete its life without them."), groups_tbl]),
           ("How micronutrients work", ["They switch on enzymes: zinc, manganese, copper, iron, molybdenum and nickel are parts of, or activators for, enzymes that drive growth and energy.",
               "They make chlorophyll possible: iron and manganese are needed to form it and run photosynthesis; magnesium sits at its centre.", "They make hormones: zinc is needed for auxin, the growth hormone.",
               "They build cell walls: boron and calcium hold walls together, and silicon strengthens them.", "They make flowers fertile: boron, zinc and copper are needed for pollen and seed set.",
               "They help use nitrogen: molybdenum, nickel and sulphur turn nitrogen into protein; molybdenum and cobalt help legumes fix it.", "They defend the crop: copper, manganese, boron and silicon strengthen tissue against pests and disease."]),
           ("The nutrients and trace elements, one by one", [el_tbl, ("html", "<p class=\"note\">*Share of soil samples deficient, including hidden shortage, in the ICAR survey. Molybdenum, chlorine, nickel, calcium, magnesium, silicon and cobalt were not part of that survey.</p>")]),
           ("India's soils: shortages are widespread", [P("An ICAR survey of 2,42,827 soil samples from 615 districts found 58.6% of soils short of sulphur, 51.2% of zinc, 44.7% of boron, 19.2% of iron, 17.4% of manganese and 11.4% of copper, counting hidden shortages. Many fields were short of two or three nutrients together, most often sulphur with zinc, zinc with boron and sulphur with boron. Alkaline and calcareous soils, low organic matter and years of urea, DAP and MOP without sulphur or micronutrients are the main reasons."), ("html", _src_note())]),
           ("Common practices that miss the cause", ["Applying more urea when leaves turn yellow, though yellowing from sulphur, iron, zinc or magnesium does not respond to nitrogen.",
               "Using NPK water-soluble fertilizer as a cure-all, though most grades carry little or no micronutrient.", "Spraying a pesticide when the crop looks weak, even when no pest is present.",
               "Treating the nutrient that shows the symptom, when the real limit is another nutrient, the soil pH or the water supply.",
               f'Read <a href="{MBASE}/guides/why-more-urea-does-not-fix-yellow-leaves">why more urea does not fix yellow leaves</a> and <a href="{MBASE}/guides/why-pesticide-spray-wont-fix-a-nutrient-problem">why a pesticide spray will not fix a nutrient problem</a>.']),
           ("Types of micronutrient fertilizers", [MICRO_TYPES, P(f'More detail: <a href="{MBASE}/guides/types-of-micronutrient-fertilizers">types of micronutrient fertilizers compared</a>.')]),
           ("How to identify and solve micronutrient problems", ["Read the leaves: old or young, pattern and colour.", "Rule out pests, disease, water and weather.", "Test the soil before the season and the leaves in orchards.",
               "Fix the cause first: pH, drainage, water supply and fertilizer balance.", "Correct the short nutrient by soil, foliar or seed treatment, at the right stage and the right dose.", "Build soil organic matter so the shortage does not return.",
               f'Follow the <a href="{MBASE}/how-to-diagnose-and-correct">step-by-step guide</a>.']),
           ("Our role", [P("Gujarat Bio Organics began in 2006 with farmers on tired soil that no longer paid back the fertilizer put into it. Today lakhs of farmers from Kashmir to Kanyakumari have used Immunity products on almost every crop: from the mango farms around Somnath to the apple orchards of Himachal Pradesh and Kashmir, the tea estates of Assam and Darjeeling, and the banana, coconut and cardamom farms of Tamil Nadu, Karnataka and Kerala. Our team visits fields, reads crops and soil reports with growers and builds crop programmes around what the soil can supply. This section is part of that work: plain, practical knowledge so every grower can find the real cause of a weak crop, spend less on the wrong inputs and leave healthier soil for the next generation.")])],
 faq=[("What are micronutrients in agriculture?", "Nutrients a crop needs in very small amounts: zinc, iron, manganese, copper, boron, molybdenum, chlorine and nickel. Calcium, magnesium and sulphur are secondary nutrients, and silicon and cobalt are beneficial elements."),
      ("What is the difference between micronutrients and trace elements?", "In farming the two terms are used for the same group: nutrients needed only in trace amounts. Trace elements is sometimes also used for beneficial elements such as cobalt and selenium."),
      ("Which micronutrient is most deficient in Indian soils?", "Among micronutrients, zinc, followed by boron. Sulphur, a secondary nutrient, is even more widely short."),
      ("Can NPK alone give a good crop?", "Only if the soil supplies enough of every other nutrient. Where a micronutrient is short, more NPK does not lift the yield."),
      ("How do I know which micronutrient my crop needs?", "Read the leaf symptoms, rule out pests and disease, and confirm with a soil and leaf test.")])
hub_extra = sec('<div class="grid">' + "".join(card(f"{MBASE}/{e['slug']}", f"{e['name']} ({e['sym']})", cap(e["short"]) + ".", e["kind"], "Read the guide") for e in ELEMENTS) + "</div>", "Nutrient guides", tint=True) \
          + sec('<div class="grid">' + "".join(card(u, t, d, m) for u, t, d, m in GEN_CARDS) + "</div>", "Understand and solve") \
          + sec('<div class="grid">' + "".join(card(u, t, d, m) for u, t, d, m in BLOG_CARDS) + f'</div><div class="btns"><a class="btn btn-line" href="{MBASE}/guides">All micronutrient blogs</a></div>', "Blogs", tint=True) \
          + _specials_box(["mango", "apple", "sugarcane", "potato", "cotton", "citrus"])
_t = "Micronutrients in Agriculture: List, Role, Deficiency | GBO"
micro_page(MBASE, [("Micronutrients", None)], dict(hub, title=_t), hub_extra)
