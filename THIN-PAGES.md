# Thin pages: deepening queue (gujaratbio.com)

Goal: every content page worth visiting. Each deepened page gets: a true "Reality check" hook (sourced if it has a number),
2-3 sourced key figures (stats) where real data exists, practical field checks, common mistakes, 2 more FAQs, and sources.
Target: about 700-1,000 words of main content per page.

Rules (always): no doses; no promises; results only as attributed farmer experience; no competitor names; never mention Plantonics;
contact details unchanged (phone only 9978791167); scary headlines only when true and fixed in the first lines; no invented prices,
ratings or reviews; plain farmer language.

How (engine already built, commit 4cf7bb7):
- Add content to `content_deepen.py` (DEEP dict keyed by page path): hook, stats, add, faq, sources.
- `article_page()` in build.py renders it for /crop-problems/* and /guides/*. Crop pages (/crops/<slug>, rendered in the
  `for c in CROPS:` loop) and product pages need the same 4 lines wired in before their batch (hook + stats after the intro,
  add sections after existing sections, faq appended to the page FAQ and FAQ schema, sources list).
- If the page has Hindi/Gujarati versions (listed in i18n/pages.json): `python3 build.py && python3 i18n/missing_auto.py <tag>`,
  translate every line into i18n/tr/hi<tag>_01.tsv and i18n/tr/gu<tag>_01.tsv ("N<TAB>text", keep tags and hrefs),
  `python3 i18n/merge.py && python3 build.py` must print `incomplete: {}` (otherwise hi/gu pages drop out). Then commit and push.
- Re-measure with a word count of <main> text; tick the page below.

## Done
- [x] /crop-problems/mango-fruit-drop, mango-alternate-bearing, citrus-dieback, potato-small-tubers, sugarcane-poor-germination (en+hi+gu)
- [x] /guides/compost-and-humic-acid, how-to-take-a-soil-sample, why-yields-fall-on-old-land, what-are-biostimulants (en)

## Batch 2: crop pages (words now)
- [ ] /crops/chilli (312), /crops/maize (325), /crops/pulses (332), /crops/cereals (344)
- [ ] /crops/cumin (347), /crops/paddy (351), /crops/pomegranate (355), /crops/coconut (362), /crops/groundnut (363)
- [ ] hubs: /crops (253), /crops/fruits (281), /crops/vegetables (293), /crop-problems (307)

## Batch 3: trust pages (facts only from the company: since 2006, plant at GIDC Shihor, 100 KL liquid and 2,500 t solid per month, 36 FCO Schedule VI biostimulant grades + 11 biofertilisers under Gujarat NOCs)
- [ ] /factory-and-rd (100), /quality (139), /our-story (238), /where-to-buy (100), /bulk-buyers (175), /oem-private-label (102), /dealers (378), /farmer-stories (257)

## Batch 4: biofertiliser product pages (educational: what the organism does, how to store, mix and apply safely, mistakes)
- [ ] immunity-consortia, -acetobacter, -npk-consortia, -mycorrhiza, -rhizobium, -azospirillum, -azotobacter, -kmb, -psb, -psf, -zsb

## Batch 5: Immunity crop product pages (~300-440 words): add crop-stage problems the product supports, mistakes, FAQs
- [ ] finisher, eleven, pulses, spices-mix, paddy, vegetable, cotton, maize, onion, banana, pomegranate, coconut, cumin, fruit, potato, mungfali, apple, chilli, dhanya, citrus, mango, granules, gold, sugarcane, tea

## Not padded on purpose
/contact, /enquiry, /privacy-policy, /terms, /shipping-and-returns, /our-websites, /sugarcane-meeting, /tools/fertilizer-dose-calculator (utility pages; short is right).
