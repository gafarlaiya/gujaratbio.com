# Season guides (November 2026): DAP shortage, potato blight, mango flowering, high density Kesar.
# Kept separate so the seasonal set is easy to review. Doses here are fertilizer nutrient arithmetic
# (published by Punjab Agricultural University), never product doses.
_T = lambda rows, head: ('<div class="tablewrap"><table class="packs"><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
                         + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")

SEASON_GUIDES = [
 dict(slug="dap-shortage-what-to-use-instead", date="2026-11-18",
      title="DAP Shortage: What to Use Instead of DAP for Wheat and Potato",
      h1="DAP shortage: what to use instead of DAP for wheat, potato and other rabi crops",
      desc="No DAP at the shop? How many bags of SSP, 12:32:16 or 10:26:26 equal one DAP bag, how to adjust urea and potash, and how to need less DAP every year.",
      answer="If DAP is not available, the crop needs the same phosphorus from another bag. About 3 bags of SSP, 1.5 bags of NPK 12:32:16 or 1.8 bags of NPK 10:26:26 give the phosphorus of one 50 kg DAP bag. With SSP or TSP, add about 20 kg of urea for the nitrogen DAP would have given. Put the phosphorus in at sowing, near the seed.",
      sections=[
       ("What one bag of DAP actually gives your crop", [
         ("html", "<p>DAP is 18% nitrogen and 46% phosphorus (as P<sub>2</sub>O<sub>5</sub>). So one 50 kg bag gives about 9 kg of nitrogen and 23 kg of phosphorus. The crop does not need DAP; it needs those 23 kg of phosphorus at sowing and the nitrogen over the season. Any bag that supplies them does the same job.</p>")]),
       ("How many bags equal one DAP bag", [
         ("html", _T([
           ["SSP (single super phosphate, 16% P)", "About 3 bags (around 145 kg)", "Add about 20 kg urea for the missing nitrogen. SSP also gives sulphur and calcium, which oilseeds, pulses and potato use well."],
           ["NPK 12:32:16", "About 1.5 bags (around 72 kg)", "Nitrogen is almost the same as DAP. It also gives about 11 kg potash, so reduce MOP by about 20 kg."],
           ["NPK 10:26:26", "About 1.8 bags (around 88 kg)", "Nitrogen is almost the same. It also gives about 23 kg potash, so reduce MOP by about 38 kg."],
           ["TSP (triple super phosphate, 46% P)", "1 bag", "No nitrogen. Add about 20 kg urea. Often hard to find."],
           ["20:20:0:13 (ammonium phosphate sulphate)", "About 2.3 bags (around 115 kg)", "Gives much more nitrogen than DAP (about 23 kg). Cut your later urea by about 30 kg. Also gives sulphur."]],
           ["Instead of 1 bag DAP", "How much", "What to change"]) +
          '<p class="note">Phosphorus figures and bag counts as published by Punjab Agricultural University; urea and potash adjustments are simple arithmetic from the grade on the bag (urea 46% N, MOP 60% K<sub>2</sub>O). Your crop\'s total need still comes from a soil test or your crop recommendation.</p>')]),
       ("Rules that matter more than the bag", [
         "Apply phosphorus at sowing or planting, in the furrow or near the seed. Phosphorus barely moves in soil; spread on top later, most of it never reaches the roots.",
         "Do not cut phosphorus to zero on soil that tested low. Wheat roots and young potato plants need it in the first weeks.",
         "If you switch to NPK grades, count the potash and nitrogen in them so you do not pay twice for the same nutrient.",
         "SSP is bulky. Three bags per DAP bag means more carrying cost, but SSP is often available when DAP is not.",
         "Mixing SSP with urea just before application is fine; do not store the mixture for days, it becomes sticky."]),
       ("How to need less DAP every year", [
         "Get a soil test. Many fields in Gujarat already have medium to high phosphorus from years of DAP; such fields often need far less. See <a href=\"/guides/how-to-take-a-soil-sample\">how to take a soil sample</a>.",
         "Place, do not broadcast. Phosphorus placed near the seed is used better than the same amount spread over the field.",
         "Feed the soil. Compost and well-rotted farmyard manure release phosphorus slowly and keep it in a form roots can use. See <a href=\"/guides/compost-and-humic-acid\">compost and humic acid</a>.",
         "Use phosphate solubilising bacteria (PSB). They free phosphorus that is already locked in your soil. They work alongside fertilizer, not as a full replacement. See <a href=\"/products/immunity-psb\">Immunity PSB</a>.",
         "Keep the roots strong. A crop with a large, healthy root system reaches more of the phosphorus in the soil. See <a href=\"/guides/humic-acid-and-root-zone-development\">humic acid and the root zone</a>."]),
       ("Crop notes for this rabi", [
         "<strong>Wheat:</strong> SSP or 12:32:16 at sowing works well; keep the first urea dose at crown root stage as usual. See the <a href=\"/crops/cereals\">wheat and cereals guide</a>.",
         "<strong>Potato:</strong> potato needs a lot of phosphorus and potash at planting, so 12:32:16 or 10:26:26 often suits it better than SSP alone. See the <a href=\"/knowledge/potato-fertilizer-schedule\">potato fertilizer schedule</a>.",
         "<strong>Gram, mustard and other oilseeds and pulses:</strong> SSP is a good choice because of its sulphur. Rhizobium on gram seed adds nitrogen from the air. See <a href=\"/crops/pulses\">pulses</a>.",
         "<strong>Cumin:</strong> keep the basal dose moderate and balanced; heavy nitrogen makes cumin soft and wilt-prone. See <a href=\"/crops/cumin\">cumin</a>."]),
       ("Do not pay more than the printed price", [
         "The maximum retail price is printed on every subsidised bag. For DAP it is ₹1,350 per 50 kg bag.",
         "Always take a bill. Without a bill you cannot complain, and you cannot be sure the bag is genuine.",
         "If a dealer refuses to sell without a bill, asks above the printed price, or forces you to buy another product with DAP, report it to your taluka or district agriculture officer.",
         "Buy only what you need for this season. Panic buying is what empties the shops for your neighbours."])],
      faq=[("What can I use instead of DAP for wheat?", "About 3 bags of SSP plus about 20 kg of urea, or about 1.5 bags of NPK 12:32:16, give the phosphorus and nitrogen of one bag of DAP. Apply it at sowing."),
           ("How many bags of SSP equal one bag of DAP?", "About 3 bags of SSP give the phosphorus of one bag of DAP. SSP has no nitrogen, so add about 20 kg of urea."),
           ("Is SSP better than DAP?", "For phosphorus alone, DAP is more concentrated. SSP also gives sulphur and calcium, which helps oilseeds, pulses and potato. For the crop, the right amount of phosphorus matters more than which bag it came from."),
           ("Can I use NPK 12:32:16 instead of DAP?", "Yes. About 1.5 bags of 12:32:16 give the phosphorus of one DAP bag and nearly the same nitrogen. It also gives potash, so reduce your MOP."),
           ("Can I skip phosphorus this year?", "Only if a soil test shows your field is high in phosphorus. On low or medium soils, skipping it usually costs yield."),
           ("Can PSB replace DAP completely?", "No. PSB frees phosphorus that is already in the soil and helps the crop use fertilizer better, so many growers can use less. It does not add new phosphorus."),
           ("What is the price of DAP in 2026?", "The printed maximum retail price for a 50 kg bag of DAP is ₹1,350. Do not pay more, and always take a bill.")]),

 dict(slug="potato-early-blight-vs-late-blight", date="2026-11-18",
      title="Potato Early Blight vs Late Blight: How to Tell Them Apart",
      h1="Potato early blight vs late blight: how to tell them apart and what to do",
      desc="How to tell early blight from late blight on potato leaves, the weather that brings each one, and why late blight needs action before you see it.",
      answer="Early blight makes dry brown spots with rings like a target, first on old lower leaves, and spreads slowly in warm weather. Late blight makes dark, wet-looking patches with white mould underneath, can start anywhere on the plant, and can kill a field within a week in cool, foggy, humid weather. Late blight must be prevented before it appears.",
      sections=[
       ("The difference at a glance", [
         ("html", _T([
           ["Cause", "A fungus (Alternaria solani)", "A water mould (Phytophthora infestans)"],
           ["Where it starts", "Old, lower leaves first", "Any leaf, often the top and middle"],
           ["What the spot looks like", "Dry, brown to black, with rings like a target, often with a yellow edge", "Pale green to dark brown, wet-looking, spreads without a clear border"],
           ["Under the leaf", "No white growth", "White, cottony mould at the edge of the spot on humid mornings"],
           ["Weather", "Warm days, dew, and plants under stress", "Cool, cloudy, foggy, humid weather, light rain"],
           ["Speed", "Slow, over weeks", "Fast: a field can collapse in 7 to 10 days"],
           ["Stems and tubers", "Stems rarely; tubers get small dark sunken spots", "Dark stem lesions; tubers get reddish-brown rot under the skin"],
           ["Smell", "None", "A rotten smell in a badly hit field"]],
           ["", "Early blight", "Late blight"]))]),
       ("Why late blight is the one to fear in Gujarat", [
         ("html", "<p>In north Gujarat and other potato belts, late blight comes with the cold, foggy spells of December and January, when nights are cool and leaves stay wet for long hours. It is the disease behind the Irish famine of the 1840s, and it is still the most damaging potato disease in the world. Once you see the spots on many plants, the field has already been infected for days.</p>")]),
       ("What to do about late blight", [
         "Plant healthy, certified seed. Infected seed tubers carry the disease into the field.",
         "Watch the weather. When cool, foggy or drizzly days are forecast, protect the crop before the spell, not after. Ask your agriculture department or KVK for blight forecasts in your district.",
         "Protective sprays must cover the leaves before infection. Use only products recommended for potato late blight by your state university, at the label dose, and rotate groups as advised.",
         "Avoid evening irrigation in foggy weather, so leaves do not stay wet all night.",
         "Earth up well so tubers stay covered and spores washing down do not reach them.",
         "Remove and bury the first infected plants you find; do not leave them in the field or on the bund.",
         "If the haulm is badly hit late in the season, cut it and wait about two weeks before digging, so tubers are not infected at harvest."]),
       ("What to do about early blight", [
         "Early blight attacks weak plants. Balanced nutrition, enough potash and steady irrigation keep it in check.",
         "Remove the lowest infected leaves where practical, and keep the field free of potato and tomato volunteers.",
         "Spray only when spots climb from the lower leaves to the middle of the plant, with a product recommended for potato by your state university, at the label dose.",
         "Rotate potato with wheat or other non-host crops; do not follow potato with tomato or brinjal."]),
       ("Healthy leaves mean bigger potatoes", [
         ("html", '<p>Leaves are the factory that fills the tubers. Every leaf lost to blight during bulking means smaller potatoes. See <a href="/crop-problems/potato-small-tubers">why potatoes are small, or too few</a> and the <a href="/crops/potato">potato crop guide</a>.</p>')])],
      faq=[("How can I tell early blight from late blight?", "Early blight makes dry brown spots with target-like rings on older leaves. Late blight makes dark, wet-looking patches with white mould under the leaf in humid weather, and spreads very fast."),
           ("Which is more dangerous, early or late blight?", "Late blight. In cool, foggy weather it can destroy a field in about a week. Early blight spreads slowly and mostly hits stressed plants."),
           ("When does late blight attack potato in Gujarat?", "Mostly during cold, foggy, humid spells in December and January, when leaves stay wet for long hours."),
           ("Can late blight be cured after it appears?", "Infected leaves cannot be cured. Sprays protect the healthy leaves, which is why they must go on before or at the very start of an outbreak."),
           ("Does blight affect the tubers?", "Late blight causes a reddish-brown rot in tubers, and infected tubers rot in storage. Early blight causes small dark sunken spots.")]),

 dict(slug="mango-flowering-care", date="2026-11-18",
      title="Mango Flowering Care: Kesar Pre-Flowering to Fruit Set",
      h1="Mango flowering care: how to get more flowers and protect them, from November to fruit set",
      desc="How Kesar mango trees decide to flower, what to do and avoid from November to fruit set, hopper and powdery mildew timing, and an honest look at paclobutrazol.",
      answer="A mango tree flowers on shoots that matured after the last harvest, after a dry, cool spell. From November, hold back irrigation and nitrogen, keep the canopy open, and watch for hoppers. When panicles appear, protect them from hoppers and powdery mildew before the flowers open. Do not spray at full bloom, so that bees and flies can pollinate.",
      sections=[
       ("How a mango tree decides to flower", [
         ("html", "<p>Flowers come at the tips of shoots that grew after harvest and have had time to mature, usually several months. In winter, cool nights and dry soil stop new leafy growth and tell those mature tips to make flowers instead. If the tree gets water and nitrogen now, it often pushes new leaves instead of flowers, and the season is lost. This is why the work for flowering really starts at harvest, with pruning and feeding in June and July, and why a heavy crop one year often means few flowers the next. See <a href=\"/crop-problems/mango-alternate-bearing\">alternate bearing in mango</a>.</p>")]),
       ("Month by month, November to fruit set", [
         ("html", _T([
           ["November", "Mature shoots, no new flush", "Stop or reduce irrigation. No nitrogen. Clear weeds. Check bark and leaves for hoppers."],
           ["December", "Buds swell; in south Gujarat panicles may begin", "Prune dense, crossing branches lightly to open the canopy. Keep the soil dry. Watch for hoppers on new panicles."],
           ["Panicle emergence (Dec to Feb)", "Panicles push out and lengthen", "First protection against hoppers and powdery mildew, before flowers open."],
           ["About 2 to 3 weeks later", "Panicles fully grown, flowers about to open", "Second protection, if hoppers or mildew are present."],
           ["Full bloom", "Flowers open", "No sprays. Let bees and flies work."],
           ["Fruit set (pea size)", "Small fruits hold", "Restart light, regular irrigation. Watch for hoppers again. See fruit drop."]],
           ["When", "What the tree is doing", "What growers do"]) +
          '<p class="note">Timing shifts with location and weather: south Gujarat often flowers earlier than Saurashtra and Kutch, and a warm winter delays flowering.</p>')]),
       ("Mango hoppers: the biggest threat at flowering", [
         "Hoppers are small, wedge-shaped insects that jump with a clicking sound when you tap a branch. They suck sap from panicles, so flowers dry and drop.",
         "Their sticky honeydew grows black sooty mould on leaves and panicles.",
         "Before panicles appear, they hide in bark cracks and the dense canopy. An open canopy and clean orchard floor reduce them.",
         "Protect at panicle emergence and again before the flowers open, with a product recommended for mango by your state university, at the label dose. Mixing many chemicals in one tank does not work better.",
         "Biological options include Beauveria bassiana or Metarhizium anisopliae, as listed in the government IPM package for mango.",
         ("html", '<p>To check panicles quickly, see the shake test in <a href="/crop-problems/mango-fruit-drop">mango fruit drop</a>.</p>')]),
       ("Powdery mildew on mango flowers", [
         "A white, powdery coating on panicles, flowers and young fruit. Affected flowers dry and fall.",
         "It spreads in cool nights with mist, fog or light rain during flowering, exactly the weather of many Gujarat winters.",
         "Protect at panicle emergence, before the coating appears, with a sulphur-based or other product recommended for mango powdery mildew, at the label dose.",
         "Remove malformed and badly infected panicles; the fungus survives in dormant buds and old infected tissue."]),
       ("Paclobutrazol: an honest look", [
         ("html", "<p>Paclobutrazol is a growth regulator applied to the soil to slow leafy growth and bring flowering in a year the tree would otherwise rest. Many orchards use it, and it can work. But it is not a tonic, and it does not replace a healthy tree.</p>"),
         "It stays in the soil for a long time. Repeated, heavy yearly use can build up residues.",
         "Growers and studies report over-compact panicles, very short shoots and small leaves where it is overused, and trees that weaken over years.",
         "It only redirects the tree's reserves. A tree that is underfed or carrying a disease load will flower, then struggle to hold fruit.",
         "If you use it, follow your state university's recommendation for dose and timing, base the dose on canopy size, and do not use it every year on young or weak trees."]),
       ("Mistakes that cost flowers", [
         "Irrigating in November and December. The tree flushes leaves instead of flowers.",
         "Urea or other nitrogen before flowering. Same result.",
         "Spraying at full bloom. It drives away pollinators and can burn flowers.",
         "Waiting for hoppers to be everywhere before acting.",
         "Heavy pruning in winter. Heavy pruning belongs right after harvest; winter pruning should be light.",
         "Expecting a young, shaded or crowded tree to flower like a mature, open one."]),
       ("Where biostimulants fit", [
         ("html", '<p>Seaweed and amino acid based products are used at panicle emergence and fruit set to help trees cope with cold, fog and heat stress. They work alongside good water, nutrition and protection, not instead of them. <a href="/products/immunity-mango-special">Immunity Mango Special</a> is made for mango; ask us which stage suits your orchard. See also the full <a href="/crops/mango">mango crop guide</a>.</p>')])],
      faq=[("Why is my mango tree not flowering?", "Common causes are shoots that came too late to mature, water or nitrogen in winter, a warm winter, a heavy crop last year, or a young, shaded or crowded tree."),
           ("How can I increase flowering in Kesar mango?", "Prune and feed the tree right after harvest so new shoots mature, then keep it dry and without nitrogen from November until panicles appear. A healthy, unstressed tree with mature shoots flowers best."),
           ("Should I irrigate mango trees before flowering?", "No. Hold back irrigation from about November until panicles have emerged. Water now pushes new leaves instead of flowers. Restart light irrigation from fruit set."),
           ("When should I spray mango before flowering?", "At panicle emergence, against hoppers and powdery mildew, and if needed again about 2 to 3 weeks later before the flowers open. Never at full bloom."),
           ("How do I control mango hoppers during flowering?", "Keep the canopy open and the orchard clean, protect panicles at emergence and before flowers open with a recommended product, and do not spray at full bloom."),
           ("What causes white powder on mango flowers?", "Powdery mildew, a fungus that spreads in cool nights with fog or mist. Protect panicles at emergence, before the powder appears."),
           ("Is paclobutrazol harmful to mango trees?", "Used at the recommended dose it can help an off-year tree flower. Heavy, repeated yearly use can leave soil residues and weaken trees. It does not replace good feeding and care."),
           ("Why is my mango tree giving new leaves instead of flowers?", "Usually water, nitrogen or warm weather during winter. It can also mean the shoots were too young to flower.")]),

 dict(slug="high-density-kesar-mango", date="2026-11-18",
      title="High Density Kesar Mango: Spacing, Pruning and Planning",
      h1="High density Kesar mango: spacing, pruning and what to plan before you plant",
      desc="Common spacings for high density Kesar mango in Gujarat, why close planting fails without yearly pruning, and the July pruning window.",
      answer="Most new Kesar orchards in Gujarat are planted at 5 x 5 m, and some at 5 x 2.5 m. Closer spacing gives more fruit per acre in the early years, but only if you prune every year to keep each tree small. Without that commitment, close-planted Kesar becomes crowded and yields fall.",
      sections=[
       ("Common spacings", [
         ("html", _T([
           ["10 x 10 m (traditional)", "About 40", "Large trees, slow to full yield, little pruning"],
           ["5 x 5 m (high density)", "About 160", "The common choice for new Kesar orchards"],
           ["5 x 2.5 m (closer)", "About 320", "Needs yearly pruning without fail"],
           ["3 x 2 m (ultra high density)", "About 670", "Under research for Kesar; no university recommendation yet"]],
           ["Spacing", "Trees per acre", "What it means"]) +
          '<p class="note">Trees per acre are rounded arithmetic (1 acre = about 4,047 m<sup>2</sup>). Navsari Agricultural University began a trial of very close spacing with Kesar in 2025; results are not yet out.</p>')]),
       ("Why close planting fails for many growers", [
         "Kesar is a vigorous tree. Left alone, neighbouring canopies touch within a few years.",
         "Crowded trees shade each other, flower less inside the canopy, and hold hoppers and mildew.",
         "Heavy pruning to recover a crowded orchard then cuts yield for a season or more.",
         "Researchers at Navsari Agricultural University note that earlier attempts at closer Kesar planting failed from overcrowding and excess pruning; growers who succeed commit to pruning every year."]),
       ("The yearly pruning window", [
         ("html", "<p>Prune right after harvest, so new shoots have time to mature before winter. A Navsari Agricultural University study on high density Kesar found that pruning in the first fortnight of July, cutting back about 25 cm of the shoots, gave better fruit set and yield than later pruning or no pruning. Pruning in winter, close to flowering, removes the shoots that would have flowered.</p>")]),
       ("What to plan before planting", [
         "Water: drip irrigation is close to essential for high density, to control water before flowering and feed through the season.",
         "Labour: yearly pruning of every tree, plus closer spraying and harvesting work.",
         "Soil: deep, well-drained land. Kesar does poorly where water stands after rain.",
         "Plants: grafts from a known, healthy mother orchard.",
         "Training: shape each young tree with a short trunk and open centre from the first year.",
         "Patience: high density brings fruit per acre earlier, but no spacing makes an unfed tree productive."]),
       ("Related guides", [
         ("html", '<p><a href="/guides/mango-flowering-care">Mango flowering care</a>, <a href="/crop-problems/mango-alternate-bearing">alternate bearing</a>, <a href="/crop-problems/mango-fruit-drop">fruit drop</a> and the <a href="/crops/mango">mango crop guide</a>.</p>')])],
      faq=[("What is the best spacing for high density Kesar mango?", "5 x 5 m is the most common for new Kesar orchards in Gujarat. 5 x 2.5 m is used by growers who prune every year. Closer spacings are still being researched."),
           ("How many Kesar mango plants per acre in high density?", "About 160 at 5 x 5 m and about 320 at 5 x 2.5 m."),
           ("When should I prune high density mango?", "Right after harvest. A Navsari Agricultural University study found the first fortnight of July best for high density Kesar."),
           ("Is high density mango profitable?", "It can bring fruit per acre earlier, but only with drip irrigation and yearly pruning. Without them, crowded trees yield less.")]),
]
