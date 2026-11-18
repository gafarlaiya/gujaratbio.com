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
      title="Mango Flowering Spray Schedule and Care: Kesar, Nov to Fruit Set",
      h1="Mango flowering care and spray schedule: more flowers, protected, from November to fruit set",
      desc="A stage-by-stage mango flowering spray schedule for Kesar: what to do from November to fruit set, hopper and mildew timing, and paclobutrazol facts.",
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
       ("Mango flowering spray schedule, stage by stage", [
         ("html", "<p>There is no single magic flowering spray. Each stage has one job, and most orchards need only two or three well-timed rounds. The options below are those listed in the Government of India's integrated pest management package for mango.</p>" + _T([
           ["November to December, before panicles", "Mature the shoots, stop leafy flush", "Usually no spray is needed. Correct zinc or boron only if a leaf or soil test shows a shortage (zinc sulphate, borax)."],
           ["Panicle emergence", "Protect from hoppers and powdery mildew", "Hoppers: imidacloprid, buprofezin, lambda-cyhalothrin or deltamethrin; biological: Beauveria bassiana or Metarhizium anisopliae. Powdery mildew: wettable sulphur, hexaconazole, penconazole or azoxystrobin."],
           ["Cloudy, humid or drizzly spell", "Protect panicles from blossom blight (anthracnose)", "Copper oxychloride or azoxystrobin."],
           ["2 to 3 weeks later, before flowers open", "Second round, only if hoppers or mildew are present", "Use a different chemical group from the first round."],
           ["Full bloom", "Pollination", "No sprays."],
           ["Pea stage", "Hold fruit, prevent black tip", "Borax at pea stage, as in the IPM package; water at regular intervals. Ask your KVK before any fruit-drop growth regulator."]],
           ["Stage", "Job", "Options listed for mango"]) +
          '<p class="note">We do not print doses on this page. The right dose depends on the product\'s strength, its formulation and the size of the tree, and doses copied from the internet are often wrong. Use the dose on the label of the product you buy, registered for mango, or your state agricultural university\'s recommendation.</p>'),
         "Spray in the early morning or evening, never in the midday heat.",
         "Mix at most one insecticide and one fungicide in a tank, and only if the labels say they mix.",
         "Rotate chemical groups between rounds so hoppers and mildew do not become resistant.",
         "Cover the whole panicle and the inner canopy; hoppers hide inside."]),
       ("Does potassium nitrate increase mango flowering?", [
         ("html", "<p>Potassium nitrate sprays are best known from warm tropical mango areas, where winters are not cold enough to trigger flowering. In Gujarat, where cool winter nights already do that job, results are mixed, and it is not part of the national IPM package for mango. It cannot make immature shoots flower. If you want to try it, follow your state university's recommendation, spray a few trees, and keep a few unsprayed to compare.</p>")]),
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
      faq=[("What is the best spray for mango flowering?", "There is no single best spray. At panicle emergence, protect against hoppers and powdery mildew, repeat only if needed before flowers open, and do not spray at full bloom. Use products registered for mango at the label dose."),
           ("Does potassium nitrate spray increase mango flowering?", "It is best known from warm tropical areas. In Gujarat's cooler winters results are mixed. It cannot make immature shoots flower. Test it on a few trees first."),
           ("Can I spray mango trees during flowering?", "Not at full bloom. Spray at panicle emergence and before flowers open. Spraying open flowers harms bees and flies and can burn the flowers."),
           ("Why is my mango tree not flowering?", "Common causes are shoots that came too late to mature, water or nitrogen in winter, a warm winter, a heavy crop last year, or a young, shaded or crowded tree."),
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

SEASON_GUIDES += [
 dict(slug="sugarcane-ratoon-management", date="2026-11-18",
      title="Sugarcane Ratoon Management After Harvest: Step by Step",
      h1="Sugarcane ratoon management after harvest: the first 45 days decide the crop",
      desc="What to do in the weeks after cutting sugarcane so the ratoon sprouts evenly: stubble shaving, trash, gap filling, loosening the soil, water and feeding.",
      answer="A good ratoon is made in the first four to six weeks after harvest. Cut stubble at ground level, spread the trash between rows instead of burning it, loosen the soil beside the rows, irrigate, fill gaps early with pre-sprouted settlings, and feed the ratoon a little more nitrogen than the plant crop got.",
      sections=[
       ("Why ratoons fall behind", [
         "Stubble left high sprouts from upper buds, which give weak, shallow-rooted shoots that lodge later.",
         "Gaps from the plant crop stay gaps, and grow with every ratoon.",
         "The soil between rows is hard and packed after a year of traffic and harvest.",
         "Burnt trash leaves the soil bare, dry and short of organic matter.",
         "Cane cut in the coldest weeks sprouts slowly; buds wait for warmth."]),
       ("Step by step after the last cane is cut", [
         ("html", _T([
           ["Day 0 to 3", "Stubble shaving", "Cut any stubble left above ground with a sharp tool, at or just below soil level, so new shoots come from the lower buds."],
           ["Day 0 to 7", "Trash, not fire", "Spread the dry leaves between the rows as mulch. Pull it off the row itself so shoots are not smothered."],
           ["Week 1", "Loosen the sides (off-barring)", "Loosen the soil on both sides of the row with a plough or cultivator. This cuts old roots and lets new roots and water in."],
           ["Week 1", "First irrigation", "Irrigate soon after shaving and loosening. Dry soil after harvest is a common reason for poor sprouting."],
           ["Week 1 to 2", "Basal feeding", "Apply the basal dose for the ratoon near the row. Ratoons need more nitrogen than the plant crop."],
           ["Week 3 to 5", "Gap filling", "Walk the rows. Fill gaps longer than about 60 cm with pre-sprouted settlings from a nursery or polybags, and water them in."],
           ["Day 45 onward", "Second feeding and weeding", "Second nitrogen dose and weeding; then follow your normal tillering-stage care."]],
           ["When", "Job", "How"]) +
          '<p class="note">Timings are a general guide; follow your state university or sugar factory recommendation for doses.</p>')]),
       ("Why trash is worth more than the fire", [
         ("html", "<p>A hectare of sugarcane leaves several tonnes of dry trash. Burnt, it is gone in an hour. Spread between rows, it keeps moisture in, keeps weeds down, protects soil life, and slowly returns organic matter. Many growers speed it up with a trash decomposer culture and a little water. If you must remove some trash, do not burn the rest on the field.</p>")]),
       ("Feeding the ratoon", [
         "A ratoon grows from an old root system in packed soil, so it needs more nitrogen than the plant crop. Follow the ratoon dose in your state or factory recommendation.",
         "Put fertilizer close to the row after loosening the soil, not on top of the trash.",
         "Acetobacter and other nitrogen-fixing bacteria can support the ratoon's nitrogen supply alongside fertilizer. See <a href=\"/products/immunity-acetobacter\">Immunity Acetobacter</a>.",
         "Organic matter and a living soil help the old stubble root again. See <a href=\"/products/immunity-sugarcane-special\">Immunity Sugarcane Special</a> and the <a href=\"/crops/sugarcane\">sugarcane crop guide</a>."]),
       ("How many ratoons to keep", [
         "Keep a ratoon only when the plant crop was healthy and gaps are few.",
         "If more than about a fifth of the row is gaps, or red rot, wilt or smut was serious, replant instead.",
         "Most growers in Gujarat keep one or two ratoons. Each ratoon is cheaper to grow but usually yields less, unless managed well."]),
       ("Related", [
         ("html", '<p><a href="/guides/how-to-increase-sugarcane-tillers">How to increase sugarcane tillers</a> and <a href="/crop-problems/sugarcane-poor-germination">sugarcane poor germination and gaps</a>.</p>')])],
      faq=[("What should I do after harvesting sugarcane for a ratoon?", "Shave stubble to ground level, spread the trash between rows, loosen the soil beside the rows, irrigate, apply the ratoon basal dose, and fill gaps within about a month."),
           ("Should I burn sugarcane trash?", "No. Spread it between rows as mulch. It keeps moisture, controls weeds and returns organic matter. Burning wastes it and leaves the soil bare."),
           ("When should gaps be filled in a ratoon?", "Within about three to five weeks of harvest, with pre-sprouted settlings, so they keep pace with the ratoon."),
           ("Does a ratoon need more fertilizer?", "It needs more nitrogen than the plant crop, because it grows from an old root system in packed soil. Follow your state or factory recommendation."),
           ("Why is my ratoon sprouting poorly?", "Common reasons are high stubble, dry soil after harvest, hard packed soil, burnt trash, cold weather at harvest, or gaps left from the plant crop.")]),

 dict(slug="how-to-increase-sugarcane-tillers", date="2026-11-18",
      title="How to Increase Sugarcane Tillers, and Keep Them Alive",
      h1="Sugarcane tillers: how to increase them, and why only some become cane",
      desc="When sugarcane tillers form, what makes a clump tiller well, why many tillers die before harvest, and what growers can do to end up with more millable cane.",
      answer="Sugarcane tillers form mostly in the first three to four months after planting or ratooning. Light reaching the base of the plant, steady moisture, enough nitrogen and loose, airy soil make more tillers. Many tillers die later; the aim is not the most tillers but the most strong tillers that survive to harvest.",
      sections=[
       ("How tillering works", [
         ("html", "<p>Each bud that sprouts gives a mother shoot. From its underground nodes come the tillers, then tillers of tillers. Tillering peaks around three to four months after planting. After that the canopy closes, the clump competes for light, and the weakest, latest tillers die. Only the earlier, thicker tillers usually grow into millable cane.</p>")]),
       ("What makes a clump tiller well", [
         "Light at the base. Wide rows and early weed control let light reach the soil, which wakes up tiller buds.",
         "Steady moisture. Long dry gaps in the tillering months cut tiller numbers.",
         "Nitrogen on time. Split nitrogen so enough is there during the tillering months, not all at once.",
         "Loose, airy soil around the clump. Hard or waterlogged soil gives few, weak tillers.",
         "Healthy setts and an even start. Gaps and late shoots never catch up."]),
       ("What to avoid", [
         "Earthing up too early. Full earthing up stops new tillers, so it is done after tillering, not during it.",
         "Weeds in the first three months, which steal light and nitrogen exactly when tillers form.",
         "Heavy late nitrogen after tillering, which pushes late tillers that die anyway.",
         "Very close planting, which shades the base and raises tiller death."]),
       ("Count your tillers", [
         "Around 90 to 100 days, count shoots per clump on a few metres of row in good and weak patches.",
         "A low count in one patch usually points to gaps, dry or hard soil, or weeds there.",
         "Record it in your farm diary, so you can compare this crop with the next. The Hariyo app has a tiller count for each field.",
         "If counts are low across the field, ask us with photos and your planting date."]),
       ("Where biological inputs fit", [
         ("html", '<p>Nitrogen-fixing bacteria such as Acetobacter and a living, organic soil support steady growth in the tillering months, alongside fertilizer. See <a href="/products/immunity-sugarcane-special">Immunity Sugarcane Special</a>, <a href="/guides/sugarcane-ratoon-management">sugarcane ratoon management</a> and the <a href="/crops/sugarcane">sugarcane crop guide</a>.</p>')])],
      faq=[("When does sugarcane tillering happen?", "Mostly in the first three to four months after planting or ratooning, peaking around three to four months."),
           ("How can I increase tillers in sugarcane?", "Control weeds early, keep moisture steady, give nitrogen on time during the tillering months, keep the soil loose and let light reach the base. Do not earth up fully until tillering is over."),
           ("Why do sugarcane tillers die?", "After the canopy closes, late and weak tillers lose the competition for light, water and nutrients. Some tiller death is normal."),
           ("Does earthing up stop tillering?", "Yes. Full earthing up covers the tiller buds, so it is done after the tillering phase.")]),

 dict(slug="salty-borewell-water-for-crops", date="2026-11-18",
      title="Salty Borewell Water: Effect on Crops and What to Do",
      h1="Salty borewell water: how it hurts crops, how to test it, and how to farm with it",
      desc="How salty borewell water affects crops, what EC and TDS numbers mean, which crops tolerate it, and practical ways to keep farming with salty water.",
      answer="Salty borewell water leaves salt in the root zone, so roots struggle to take up water even in wet soil. Leaf edges burn, germination is poor and yields fall. Test the water's EC once. Below about 0.7 dS/m it is generally safe; above about 3 dS/m it needs careful management, salt-tolerant crops and good drainage.",
      sections=[
       ("What salt does to a crop", [
         "Salt in the soil water holds water back from the roots, so the crop shows thirst even after irrigation.",
         "Leaf tips and edges dry and burn, starting on older leaves.",
         "Germination falls and seedlings die, because salt collects near the surface where the seed is.",
         "Some waters also carry a lot of sodium or bicarbonate. Over years this makes the soil hard, sticky and slow to drain."]),
       ("Test the water, once a year", [
         ("html", "<p>Take a clean bottle of water after the pump has run for a few minutes and ask a soil and water testing lab for EC, pH, and RSC (residual sodium carbonate). Many labs also report TDS; as a rough guide, TDS in mg/L is about EC in dS/m multiplied by 640.</p>" + _T([
           ["Below 0.7", "Below about 450", "No restriction for most crops"],
           ["0.7 to 3.0", "About 450 to 2,000", "Slight to moderate restriction: choose crops and manage carefully"],
           ["Above 3.0", "Above about 2,000", "Severe restriction: tolerant crops, good drainage and blending only"]],
           ["EC (dS/m)", "TDS (mg/L)", "What it means"]) +
          '<p class="note">Bands from the FAO guidelines on water quality for agriculture. Soil type, rainfall and drainage change how much a given water hurts; light soils with good rain cope better than heavy, poorly drained soils.</p>')]),
       ("Which crops cope better", [
         ("html", _T([
           ["More tolerant", "Barley, cotton, sugar beet, date palm"],
           ["Moderately tolerant", "Wheat, mustard, sorghum"],
           ["Moderately sensitive", "Sugarcane, groundnut, maize, tomato, chilli, potato"],
           ["Sensitive", "Onion, beans and most pulses, mango, citrus, carrot"]],
           ["Group", "Examples"]) +
          '<p class="note">Varieties differ; ask your KVK for salt-tolerant varieties of your crop. Seedlings are more sensitive than established plants.</p>')]),
       ("How to keep farming with salty water", [
         "Blend or alternate: use canal or rain-harvested water for germination and early growth, and the borewell later.",
         "Irrigate lightly and more often. Letting the soil dry out concentrates salt around the roots.",
         "Use drip where you can. It keeps the root zone moist and pushes salt to the edge of the wetted area.",
         "On ridges and beds, sow on the side of the ridge, not the top, where salt collects.",
         "Let the monsoon flush salt down: keep fields level and bunded so rain soaks in, and keep drains open.",
         "Add organic matter: compost and crop residues improve structure so salt can be washed below the roots.",
         "Gypsum helps where the problem is sodium or high RSC, not plain salt. Use it on a lab's advice.",
         "Mulch the soil surface to cut evaporation, which pulls salt up."]),
       ("Where biostimulants fit", [
         ("html", '<p>Some seaweed, amino acid and humic products are used to help crops cope with salt stress. They do not remove salt, and they work only alongside the water and soil steps above. See <a href="/guides/biostimulants-for-salinity-and-drought-stress">biostimulants for salinity and drought stress</a> and <a href="/guides/why-yields-fall-on-old-land">why yields fall on old land</a>.</p>')])],
      faq=[("How do I know if my borewell water is salty?", "Test it for EC in a soil and water testing lab. Burnt leaf edges, white crust on the soil and poor germination are signs, but only a test tells you how salty."),
           ("What EC of water is good for irrigation?", "Below about 0.7 dS/m is safe for most crops. From 0.7 to 3 dS/m needs care; above 3 dS/m is severe."),
           ("What is a safe TDS for irrigation water?", "Below about 450 mg/L is generally safe. Above about 2,000 mg/L severely limits most crops."),
           ("Can salty water be used for drip irrigation?", "Yes, often more safely than flood irrigation, because drip keeps the root zone moist. Flush the lines and let the monsoon wash salt down."),
           ("Does gypsum remove salt from water?", "No. Gypsum helps where the water or soil has too much sodium or bicarbonate. It does not remove ordinary salt."),
           ("Which crops grow well with salty water?", "Barley, cotton and sugar beet are among the more tolerant; wheat and mustard moderately. Onion, pulses, mango and citrus are sensitive.")]),
]

# Farmer questions batch (19 Nov 2026): top farmer questions in soil health, crop problems and organic farming
SEASON_GUIDES += [
 dict(slug="yellow-leaves-despite-fertilizer", date="2026-11-19",
      title="Leaves Turning Yellow Even After Fertilizer: Causes and Fixes",
      h1="Why leaves turn yellow even after you apply fertilizer, and how to find the real cause",
      desc="Leaves still yellow after urea or NPK? Read which leaves turn yellow first, and check roots, water, pH and micronutrients before buying another bag.",
      answer="If leaves stay yellow after fertilizer, the crop is usually not short of that fertilizer. Either the roots cannot take it up (waterlogging, dry soil, root disease, salt, high pH), or the shortage is a different nutrient such as magnesium, sulphur, iron or zinc. Which leaves turn yellow first tells you where to look.",
      sections=[
       ("Step 1: which leaves are yellow?", [
         ("html", _T([
           ["Old, lower leaves, whole leaf pale", "Nitrogen", "Common after heavy rain or waterlogging, which washes away or locks nitrogen"],
           ["Old leaves, yellow between green veins", "Magnesium", "Often on sandy soils, or where much potash is used"],
           ["Old leaves, yellow or burnt edges", "Potash", "Edges dry first, then the whole leaf"],
           ["Young, top leaves, whole leaf pale", "Sulphur", "Looks like nitrogen shortage but on new leaves"],
           ["Young leaves, yellow between green veins", "Iron or manganese", "Very common on high pH, calcareous soils of Gujarat"],
           ["Young leaves small, crowded, mottled", "Zinc", "Short internodes, small narrow leaves"],
           ["Patches in the field, plants wilt at midday", "Roots", "Root rot, nematodes, termites or waterlogging; dig a plant"]],
           ["What you see", "Likely shortage", "Notes"]) +
          '<p class="note">These patterns are a guide. Several shortages can show together, and a leaf or soil test confirms them. See <a href="/micronutrients/deficiency-symptoms">deficiency symptoms with photos</a>.</p>')]),
       ("Step 2: check the roots before the bag", [
         "Pull out one yellow plant and one green plant. Compare the roots: white and many is healthy; brown, few, rotten or knotted is a root problem.",
         "Waterlogged soil for even two or three days suffocates roots. Fertilizer cannot help until the soil drains.",
         "Very dry soil also stops uptake. Fertilizer on dry soil sits unused.",
         "Salty water or soil makes leaves yellow and burnt at the edges; see <a href=\"/guides/salty-borewell-water-for-crops\">salty borewell water</a>.",
         "Cold nights in winter can make leaves pale for a while; they recover as days warm."]),
       ("Step 3: is the soil locking nutrients?", [
         "On soils with pH above about 8, iron, zinc and manganese are present but locked. Adding more to the soil often fails; foliar sprays or chelated forms work better.",
         "Too much phosphorus can lock zinc. Too much potash can lock magnesium.",
         "Low organic matter means nutrients wash away or get locked quickly. See <a href=\"/guides/compost-and-humic-acid\">compost and humic acid</a>."]),
       ("What to do", [
         "Fix drainage or irrigation first, if roots are the problem.",
         "Get a soil test, and a leaf test if you can, before adding more NPK.",
         "Correct the specific shortage the pattern and test show, at the label dose.",
         "Keep roots strong with organic matter; a healthy root system takes up more of what is already there.",
         "Ask us with a photo of the whole plant, a close-up of the leaf, and the roots."])],
      faq=[("Why are leaves yellow even after applying urea?", "The crop may not be short of nitrogen. Waterlogging, dry soil, root damage, salt, high pH or a shortage of magnesium, sulphur, iron or zinc can all cause yellowing that urea does not fix."),
           ("Which deficiency causes yellow leaves between green veins?", "On old leaves, usually magnesium. On young leaves, usually iron or manganese, common on high pH soils."),
           ("Can too much water make leaves yellow?", "Yes. Waterlogged roots cannot breathe or take up nutrients, so leaves turn yellow even with plenty of fertilizer."),
           ("Should I spray or add more fertilizer to the soil?", "Find the cause first. Locked micronutrients on high pH soil respond better to foliar sprays; root and water problems need fixing before any fertilizer works.")]),

 dict(slug="flower-drop-before-fruit-set", date="2026-11-19",
      title="Why Flowers Drop Before Fruit Set, and What Helps",
      h1="Why flowers drop before fruit set in vegetables, cotton and fruit crops, and what helps",
      desc="Why tomato, chilli, brinjal, cotton, pomegranate and mango shed flowers before fruit set: heat, water, nitrogen, pests, pollination and boron, and what helps.",
      answer="Every crop sheds some flowers; that is normal. Heavy flower drop is usually caused by heat or cold, a dry or waterlogged root zone, too much nitrogen, sucking pests such as thrips and mites, poor pollination, or a shortage of boron. Find which one applies before you spray anything.",
      sections=[
       ("Normal drop and problem drop", [
         ("html", "<p>A plant makes more flowers than it can carry. Cotton sheds many of its squares and young bolls, and a mango panicle keeps only a few fruits out of hundreds of flowers. It becomes a problem when the drop is sudden, most flowers fall, or the plant keeps flowering and setting nothing.</p>")]),
       ("The common causes", [
         ("html", _T([
           ["Heat", "Very hot days and hot winds dry pollen; tomato and chilli drop flowers in heat waves", "Irrigate in the evening, mulch, use shade nets in nurseries"],
           ["Cold and fog", "Pollen does not work well on cold nights; mango and vegetables set poorly in long foggy spells", "Wait for warmer days; protect flowers from mildew"],
           ["Water stress", "Dry spells, or a sudden flood after a dry spell", "Light, regular irrigation; drip where possible"],
           ["Too much nitrogen", "The plant grows leaves instead of holding flowers", "Cut nitrogen at flowering; balance with potash"],
           ["Thrips, mites, hoppers", "They feed on flower parts and buds", "Check the inside of flowers with a white paper; act early"],
           ["Poor pollination", "Few bees and insects, often after sprays at bloom", "Do not spray open flowers; spray morning or evening"],
           ["Boron shortage", "Pollen tubes do not grow; flowers fall or fruit is misshapen", "Correct only if a soil or leaf test, or clear symptoms, show it"]],
           ["Cause", "What happens", "What helps"]))]),
       ("Crop notes", [
         "<strong>Tomato, chilli, brinjal:</strong> heat, thrips and mites, and too much nitrogen are the usual causes. See <a href=\"/crops/chilli\">chilli</a> and <a href=\"/crops/vegetables\">vegetables</a>.",
         "<strong>Cotton:</strong> squares and young bolls fall with water stress, cloudy wet spells, excess nitrogen and sucking pests. See <a href=\"/crops/cotton\">cotton</a>.",
         "<strong>Pomegranate:</strong> male flowers always fall; that is normal. Watch for heat and irregular water. See <a href=\"/crops/pomegranate\">pomegranate</a>.",
         "<strong>Mango:</strong> see <a href=\"/crop-problems/mango-fruit-drop\">mango flower and fruit drop</a> and <a href=\"/guides/mango-flowering-care\">mango flowering care</a>."]),
       ("Before you spray", [
         "Look at the dropped flowers: a clean break with no damage points to stress; brown, chewed or scarred flowers point to pests or disease.",
         "Check soil moisture with your hand at root depth.",
         "Think back over the last week: heat wave, cold spell, heavy rain, a big urea dose or a spray at bloom?",
         "Growth regulators are sold for flower drop. Use them only on your state university's or KVK's advice, at the label dose."]),
       ("Where biostimulants fit", [
         ("html", '<p>Seaweed and amino acid based products are used before and during flowering to help plants cope with heat and cold stress. They support a crop that is watered and fed well; they do not fix a pest or water problem. See <a href="/guides/what-are-biostimulants">what biostimulants are</a> and <a href="/micronutrients/boron">boron</a>.</p>')])],
      faq=[("Why are my flowers dropping before fruit set?", "Usually heat or cold, water stress, too much nitrogen, sucking pests like thrips and mites, poor pollination or boron shortage. Some flower drop is normal in every crop."),
           ("Why do tomato and chilli flowers fall?", "Most often heat waves and hot winds, thrips and mites, irregular water or too much nitrogen."),
           ("Does boron stop flower drop?", "Only where boron is short. Boron helps pollen grow and fruit set. Adding it where it is not short does not help, and too much is harmful."),
           ("Should I spray a hormone to stop flower drop?", "Only on your state university's or KVK's advice, at the label dose, after you have ruled out water, heat and pests.")]),

 dict(slug="hard-compact-soil", date="2026-11-19",
      title="Hard, Compact Soil: Why It Happens and How to Fix It",
      h1="Why soil becomes hard, compact and less productive, and how to bring it back",
      desc="Why farm soil turns hard and compact, how to check for a plough pan or sodic soil, and practical steps to loosen it and keep it loose.",
      answer="Soil turns hard when organic matter falls, when it is ploughed or driven on while wet, when the same depth is tilled every year (a plough pan), or when sodium builds up from irrigation water. Roots then stay shallow, water runs off or stands, and yields fall. Organic matter, the right tillage at the right moisture, and gypsum where sodium is the cause bring it back.",
      sections=[
       ("Why soil becomes hard", [
         "Organic matter has fallen. Organic matter is the glue that keeps soil crumbly.",
         "Ploughing or running a tractor on wet soil smears and packs it.",
         "Tilling to the same depth every year forms a hard layer, a plough pan, just below.",
         "Bare soil under heavy rain or flood irrigation forms a crust on top.",
         "Sodium from irrigation water makes clay soils sticky when wet and hard as stone when dry."]),
       ("Check your soil in 10 minutes", [
         "Push a steel rod into moist soil. If it stops suddenly at 15 to 25 cm, there is a plough pan.",
         "Dig a pit 45 cm deep. Roots turning sideways at one level show the hard layer.",
         "Drop a dry clod in a glass of water. A healthy clod holds together; a clod that melts into mud has poor structure; cloudy water that does not settle can point to sodium.",
         "Watch after irrigation: water standing for a day, or running off, shows poor infiltration.",
         ("html", '<p>A soil test with pH, EC and, where needed, exchangeable sodium confirms a sodic soil. See <a href="/guides/how-to-take-a-soil-sample">how to take a soil sample</a>.</p>')]),
       ("How to loosen it", [
         "Break a plough pan once with a chisel plough or subsoiler, when the soil is dry enough to crack, not wet.",
         "Then keep it open: grow deep-rooted crops, green manure such as dhaincha or sunhemp, and return crop residues.",
         "Add compost or farmyard manure every season. See <a href=\"/guides/compost-and-humic-acid\">compost and humic acid</a>.",
         "Do not plough or drive on wet soil.",
         "Mulch or keep the soil covered, so rain does not crust it.",
         "Use gypsum only where a soil or water test shows sodium is the problem, on a lab's advice."]),
       ("Related", [
         ("html", '<p><a href="/guides/why-yields-fall-on-old-land">Why yields fall on old land</a>, <a href="/guides/soil-microbial-activity">soil microbial activity</a> and <a href="/knowledge/soil-health">soil health</a>.</p>')])],
      faq=[("Why is my soil becoming hard?", "Usually falling organic matter, ploughing or driving on wet soil, a plough pan from tilling the same depth every year, crusting from heavy rain, or sodium from irrigation water."),
           ("How do I know if I have a plough pan?", "Push a steel rod into moist soil. If it stops suddenly at about 15 to 25 cm, or roots turn sideways at one level in a pit, there is a hard layer."),
           ("Does gypsum soften hard soil?", "Only where sodium causes the hardness. On ordinary compact soil, organic matter and correct tillage help; gypsum does not."),
           ("How long does it take to improve compact soil?", "Breaking a plough pan works at once, but the soil packs again unless organic matter and good practice keep it open. Real improvement takes a few seasons.")]),

 dict(slug="soil-microbial-activity", date="2026-11-19",
      title="How to Improve Soil Microbial Activity and Beneficial Bacteria",
      h1="How to improve soil microbial activity: feeding the life that feeds your crop",
      desc="What soil microbes do for crops, what feeds and what harms them, simple field signs of a living soil, and where biofertilizers fit.",
      answer="Soil microbes need food (organic matter and living roots), water, air and cover. Feed them with compost, crop residues, green manure and living roots in the soil for as much of the year as possible. Avoid burning, bare soil, waterlogging and heavy tillage. Biofertilizers add useful microbes, but they survive only in a soil that feeds them.",
      sections=[
       ("What microbes do for your crop", [
         "Break down crop residues and manure into nutrients plants can use.",
         "Free phosphorus, potash and zinc locked in the soil.",
         "Fix nitrogen from the air, in legume roots and around other crops.",
         "Make the glue that holds soil in crumbs, so water and roots move freely.",
         "Compete with, and keep down, some disease-causing fungi."]),
       ("What feeds them", [
         "Organic matter: compost, farmyard manure, crop residues. See <a href=\"/guides/how-to-start-composting\">how to start composting</a>.",
         "Living roots: roots release sugars that feed microbes. Avoid long bare fallows.",
         "Variety: rotations and intercrops feed a wider range of microbes than one crop every year.",
         "Moisture and air together: moist, crumbly soil, not dry dust and not waterlogged mud."]),
       ("What harms them", [
         "Burning residues, which removes their food and heats the surface.",
         "Bare soil in summer sun.",
         "Waterlogging, which drives out air.",
         "Frequent deep tillage, which breaks fungal networks and burns organic matter.",
         "Seed or soil treated with chemicals at the same time as live biofertilizers; apply them separately, as the label says."]),
       ("Signs of a living soil", [
         "Earthworms and their casts after rain.",
         "A sweet, earthy smell when you dig.",
         "Crumbly soil that holds together in a ball but breaks easily.",
         "Crop residues that disappear within a season instead of lying for a year.",
         "Water that soaks in quickly after irrigation."]),
       ("Where biofertilizers fit", [
         ("html", '<p>Biofertilizers add specific useful microbes, such as nitrogen fixers or phosphate solubilisers. They work best in soil with organic matter and moisture. See <a href="/guides/which-biofertilizers-to-use">which biofertilizers to use</a> and <a href="/products/immunity-consortia">Immunity Consortia</a>.</p>')])],
      faq=[("How can I increase beneficial bacteria in my soil?", "Add compost and crop residues, keep living roots in the soil, rotate crops, avoid burning and waterlogging, and use biofertilizers in soil that has organic matter."),
           ("Do chemical fertilizers kill soil microbes?", "Balanced fertilizer at normal doses does not kill soil life. Long-term use with no organic matter starves it. Some chemical seed treatments and fungicides can harm live biofertilizers applied at the same time."),
           ("How do I know my soil is biologically active?", "Earthworms, an earthy smell, crumbly structure, residues that break down within a season, and water that soaks in quickly.")]),

 dict(slug="which-biofertilizers-to-use", date="2026-11-19",
      title="Which Biofertilizers to Use: A Crop-by-Crop Guide",
      h1="Which biofertilizers to use for your crop, and how to make them work",
      desc="Rhizobium, Azotobacter, Azospirillum, Acetobacter, PSB, KMB, ZSB and mycorrhiza explained: what each does, which crops it suits and how to apply it well.",
      answer="Choose biofertilizers by the job: Rhizobium for pulses and groundnut, Azotobacter or Azospirillum for cereals, vegetables and cotton, Acetobacter for sugarcane, PSB for phosphorus, KMB for potash, ZSB for zinc, and mycorrhiza for roots. They are living products, so freshness, storage and soil organic matter decide whether they work.",
      sections=[
       ("What each one does", [
         ("html", _T([
           ['<a href="/products/immunity-rhizobium">Rhizobium</a>', "Fixes nitrogen in root nodules", "Gram, tur, moong, urad, soybean, groundnut"],
           ['<a href="/products/immunity-azotobacter">Azotobacter</a>', "Fixes nitrogen around roots", "Wheat, cotton, vegetables, many non-legumes"],
           ['<a href="/products/immunity-azospirillum">Azospirillum</a>', "Fixes nitrogen, supports root growth", "Maize, sorghum, millets, paddy"],
           ['<a href="/products/immunity-acetobacter">Acetobacter</a>', "Fixes nitrogen inside the plant", "Sugarcane"],
           ['<a href="/products/immunity-psb">PSB</a> and <a href="/products/immunity-psf">PSF</a>', "Free locked phosphorus", "All crops"],
           ['<a href="/products/immunity-kmb">KMB</a>', "Free potash from soil minerals", "All crops"],
           ['<a href="/products/immunity-zsb">ZSB</a>', "Free locked zinc", "All crops, especially on high pH soils"],
           ['<a href="/products/immunity-mycorrhiza">Mycorrhiza</a>', "Extends roots to reach water and phosphorus", "Fruit trees, vegetables, many field crops"],
           ['<a href="/products/immunity-consortia">Consortia</a>', "Several of the above together", "Where one product is easier than many"]],
           ["Biofertilizer", "What it does", "Suits"]))]),
       ("How to apply them", [
         "Seed treatment: coat seed just before sowing and sow within a few hours.",
         "Seedling dip: dip roots of transplants before planting.",
         "Soil: mix with well-rotted compost or farmyard manure and apply in the root zone.",
         "Drip: some liquid products can go through drip; follow the label.",
         "Always at the dose and method on the label."]),
       ("Why biofertilizers sometimes fail", [
         "Old or badly stored product. Keep packs in a cool, shaded place, never in the sun or a hot vehicle, and use before expiry.",
         "Mixed with chemical seed treatment or fungicide at the same time. Apply them separately.",
         "Dry soil. Microbes need moisture to settle in.",
         "Soil with almost no organic matter, where they have nothing to live on.",
         "Wrong match: Rhizobium on a non-legume does nothing."]),
       ("What to expect", [
         ("html", '<p>Biofertilizers support nutrient supply and root health over a season, and can let many growers reduce chemical fertilizer. They do not replace all fertilizer at once, and results build over seasons with organic matter. Use products approved under the Fertiliser Control Order. See <a href="/guides/soil-microbial-activity">soil microbial activity</a> and <a href="/guides/reduce-chemical-fertilizer-without-yield-loss">reduce chemical fertilizer without losing yield</a>.</p>')])],
      faq=[("Which biofertilizer is best?", "There is no single best. Choose by crop and job: Rhizobium for pulses, Azotobacter or Azospirillum for cereals and vegetables, Acetobacter for sugarcane, PSB for phosphorus, KMB for potash, ZSB for zinc."),
           ("Can biofertilizers replace chemical fertilizers?", "Not fully at once. They help the crop get more from soil and fertilizer, so many growers can reduce chemical use step by step."),
           ("Can I mix biofertilizer with fungicide seed treatment?", "Not at the same time. Apply them separately, as the label says, because fungicides can kill the microbes."),
           ("How should biofertilizers be stored?", "In a cool, shaded place, away from sun and heat, and used before the expiry date.")]),

 dict(slug="reduce-chemical-fertilizer-without-yield-loss", date="2026-11-19",
      title="How to Reduce Chemical Fertilizer Without Reducing Yield",
      h1="How to reduce chemical fertilizer without losing yield: a step-by-step path",
      desc="A practical, step-by-step way to cut chemical fertilizer use without a yield drop: soil testing, better placement, organic matter and biofertilizers.",
      answer="Cut waste first, not the crop's food. Test the soil to stop applying what is already there, place and split fertilizer so more reaches the roots, build organic matter, and add biofertilizers. Reduce in steps over seasons, comparing a strip of the field each time, rather than stopping all fertilizer at once.",
      sections=[
       ("Why cutting all at once fails", [
         ("html", "<p>A field used to high chemical doses, with low organic matter, cannot feed a crop on its own in one season. Growers who stop suddenly often lose yield and go back. Growers who reduce step by step, while building the soil, usually keep their yield and lower their cost.</p>")]),
       ("The path, step by step", [
         ("html", _T([
           ["Season 1", "Soil test; stop applying nutrients the test shows are high; place fertilizer near roots; split nitrogen"],
           ["Season 1 onward", "Add compost or farmyard manure; return crop residues; add biofertilizers suited to the crop"],
           ["Season 2", "Reduce chemical NPK by a modest share on one test strip; compare yield with the rest of the field"],
           ["Season 3 onward", "If the test strip held its yield, extend the reduction; test the soil again"]],
           ["When", "What to do"]))]),
       ("Where most fertilizer is wasted", [
         "Applying phosphorus every year on soils already high in it.",
         "Broadcasting on the surface instead of placing near roots.",
         "Giving all the nitrogen at once, much of it lost before the crop can use it.",
         "Fertilizer on dry soil, or just before heavy rain.",
         "Ignoring zinc, sulphur or boron, so the NPK cannot do its job."]),
       ("Tools that help", [
         "Soil and leaf tests. See <a href=\"/guides/how-to-take-a-soil-sample\">how to take a soil sample</a>.",
         "Compost and humic substances. See <a href=\"/guides/compost-and-humic-acid\">compost and humic acid</a>.",
         "Biofertilizers. See <a href=\"/guides/which-biofertilizers-to-use\">which biofertilizers to use</a>.",
         "Legumes and green manure in the rotation.",
         "Drip fertigation, which puts small amounts where the roots are.",
         "When DAP is short: <a href=\"/guides/dap-shortage-what-to-use-instead\">what to use instead of DAP</a>."])],
      faq=[("How can I reduce chemical fertilizer without losing yield?", "Test the soil, stop applying what is already high, place and split fertilizer, build organic matter, add biofertilizers, and reduce in steps on a test strip before the whole field."),
           ("Can I stop chemical fertilizer completely?", "Stopping suddenly usually lowers yield. Reducing step by step over seasons, while building organic matter, is safer."),
           ("How much fertilizer can I save?", "It depends on your soil and how much was being wasted. A soil test and a test strip in your own field are the honest way to find out.")]),

 dict(slug="organic-vs-natural-farming", date="2026-11-19",
      title="Organic Farming vs Natural Farming: What Is the Difference?",
      h1="Organic farming vs natural farming: the difference, the rules and which suits you",
      desc="The difference between organic and natural farming in India: inputs allowed, certification, the conversion period, markets, and how to choose.",
      answer="Both avoid synthetic chemicals. Organic farming allows bought organic inputs such as compost, manures, biofertilizers and approved products, and can be certified (NPOP for export, PGS-India for the domestic market) after a conversion period. Natural farming relies mainly on on-farm inputs such as cow dung and urine preparations, mulching and mixed cropping, with minimal bought inputs, and is promoted by the government's National Mission on Natural Farming.",
      sections=[
       ("Side by side", [
         ("html", _T([
           ["Synthetic fertilizers and pesticides", "Not allowed", "Not allowed"],
           ["Bought inputs", "Allowed if approved for organic use: compost, manures, biofertilizers, bio-pesticides", "Kept to a minimum; mostly made on the farm"],
           ["Typical inputs", "Compost, vermicompost, FYM, biofertilizers, green manure", "Jeevamrut, beejamrut, mulch, mixed crops, desi cow based preparations"],
           ["Certification", "NPOP (third party, for export) or PGS-India (group based, domestic)", "Not required; some states support group recognition"],
           ["Conversion period", "Usually 2 years for seasonal crops and 3 years for perennial crops before certified sale", "No formal period"],
           ["Market", "Certified organic price premium where buyers exist", "Mostly local and direct sales"]],
           ["", "Organic farming", "Natural farming"]))]),
       ("What both share", [
         "Building soil organic matter and soil life.",
         "Mulching and keeping soil covered.",
         "Crop rotation, intercropping and legumes.",
         "Biological pest management.",
         "Patience: yields often dip in the first seasons and recover as the soil improves."]),
       ("How to choose", [
         "If you want to sell certified produce, especially for export, choose organic and plan certification from the start.",
         "If you want to cut input cost and sell locally, natural farming practices can fit.",
         "Many growers start with one plot, not the whole farm, and expand what works.",
         "Either way, keep records of what you apply and what you harvest."]),
       ("Related", [
         ("html", '<p><a href="/guides/reduce-chemical-fertilizer-without-yield-loss">Reduce chemical fertilizer without losing yield</a>, <a href="/guides/which-biofertilizers-to-use">which biofertilizers to use</a> and <a href="/guides/biological-pest-and-disease-control">biological pest and disease control</a>.</p>')])],
      faq=[("What is the difference between organic and natural farming?", "Organic farming allows bought organic inputs and can be certified. Natural farming relies mainly on on-farm preparations and mulching with minimal bought inputs, and usually is not certified."),
           ("Is natural farming the same as zero budget natural farming?", "Natural farming in India grew out of what was called zero budget natural farming. The government now promotes it under the National Mission on Natural Farming."),
           ("How long does organic certification take?", "Usually a 2 year conversion period for seasonal crops and 3 years for perennial crops before produce can be sold as certified organic."),
           ("Can I use biofertilizers in natural farming?", "Natural farming keeps bought inputs to a minimum, but many growers use biofertilizers during the change. In certified organic farming, approved biofertilizers are allowed.")]),

 dict(slug="biological-pest-and-disease-control", date="2026-11-19",
      title="Biological Pest and Disease Control: A Farmer's Guide",
      h1="Biological pest and disease control: what works, and how to use it well",
      desc="Trichoderma, Pseudomonas, Beauveria, Metarhizium, NPV, Trichogramma, traps and neem: what each controls, how to use them, and why timing matters.",
      answer="Biological control uses living organisms and natural products to keep pests and diseases below damaging levels: beneficial fungi and bacteria such as Trichoderma, Pseudomonas, Beauveria and Metarhizium, viruses such as NPV, parasitoids such as Trichogramma, and traps and neem. They work best early and preventively, as part of integrated pest management, not as a last rescue.",
      sections=[
       ("The main tools", [
         ("html", _T([
           ["Trichoderma", "Soil fungus", "Root rot, wilt, damping off; seed and soil treatment"],
           ["Pseudomonas fluorescens", "Bacterium", "Several leaf and root diseases; seed, soil and spray"],
           ["Beauveria bassiana", "Insect-killing fungus", "Hoppers, whitefly, borers, beetles"],
           ["Metarhizium anisopliae", "Insect-killing fungus", "White grub, termites, hoppers"],
           ["NPV (nuclear polyhedrosis virus)", "Virus specific to one pest", "Helicoverpa and Spodoptera caterpillars"],
           ["Trichogramma cards", "Tiny wasp that kills pest eggs", "Borers in sugarcane, cotton bollworms"],
           ["Pheromone traps", "Lure male moths", "Monitoring and mass trapping of bollworms, fruit fly, borers"],
           ["Yellow and blue sticky traps", "Catch flying insects", "Whitefly, aphids, thrips"],
           ["Neem products", "Plant extract", "Feeding deterrent and growth disruptor for many sucking and chewing pests"]],
           ["Tool", "What it is", "Used against"]))]),
       ("Rules that make them work", [
         "Start early. Biologicals prevent and slow pests; they rarely rescue a crop that is already badly hit.",
         "Fungal products need humidity; spray in the evening.",
         "Do not mix live fungal or bacterial products with chemical fungicides in the same tank.",
         "Use fresh product from a registered source, stored cool, before expiry. Bio-pesticides must be registered with the Central Insecticides Board.",
         "Count pests with traps and field checks, so you act at the right time.",
         "Protect natural enemies: ladybirds, spiders and lacewings are free pest control. Avoid broad-spectrum sprays where you can."]),
       ("Prevention first", [
         "Healthy seed and seed treatment.",
         "Crop rotation, and removing infected plants and residues.",
         "Balanced nutrition: too much nitrogen invites sucking pests.",
         "Good drainage and spacing so leaves dry quickly.",
         "Strong roots and healthy soil; see <a href=\"/guides/soil-microbial-activity\">soil microbial activity</a>."]),
       ("When to use chemicals", [
         ("html", '<p>When pests cross the level that causes economic loss and biological options cannot hold them, a registered chemical at the label dose may be needed. Choose the most specific product, and leave a gap before returning to biologicals. See <a href="/guides/mango-flowering-care">mango flowering care</a> and <a href="/guides/potato-early-blight-vs-late-blight">potato blight</a> for crop examples.</p>')])],
      faq=[("What is biological pest control?", "Using living organisms and natural products, such as beneficial fungi, bacteria, viruses, parasitic wasps, traps and neem, to keep pests and diseases below damaging levels."),
           ("Does Trichoderma control root rot?", "Trichoderma is widely used as a seed and soil treatment to protect roots against root rot, wilt and damping off. It works best as prevention."),
           ("Can I mix bio-pesticides with chemical fungicides?", "Do not mix live fungal or bacterial products with chemical fungicides in the same tank; the fungicide can kill them."),
           ("Do biological controls work as fast as chemicals?", "Usually slower. They work best early and as prevention, combined with traps, monitoring and good crop care.")]),
]
