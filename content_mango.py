# Mango cluster (23 Nov 2026): pillar guide, diseases and pests, powdery mildew.
# Facts follow the Government of India IPM package for mango (NIPHM) and ICAR/state university advice.
# No product doses anywhere: the label dose, or the state agricultural university's recommendation, applies.
# No yield or income promises. Farmer results appear only elsewhere, as the farmers' own words.
_TM = lambda rows, head: ('<div class="tablewrap"><table class="packs"><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
                          + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")
_MG = '<a href="https://wa.me/919978791167">WhatsApp +91 99787 91167</a>'

MANGO_GUIDES = [
 dict(slug="mango-farming-in-india", date="2026-11-23",
      title="Mango Farming in India: Complete Guide to Cultivation and Care",
      h1="Mango farming in India: soil, planting, feeding, flowering and harvest in one guide",
      desc="Mango cultivation in India from soil and varieties to planting, irrigation, feeding, pruning, flowering care, pests and harvest. A month by month plan for Gujarat growers.",
      answer="Mango grows best in deep, well-drained soil with a pH of about 5.5 to 7.5, in a warm climate with a dry, cool spell before flowering. Plant grafted trees of a variety suited to your region at the start of the monsoon, water young trees regularly, prune after harvest, and from November hold back water and nitrogen so the tree flowers. Protect panicles before the flowers open, restart light irrigation at fruit set, and harvest mature fruit with a short stalk.",
      sections=[
       ("Soil, climate and varieties", [
         "Mango does best in deep, well-drained loam. Waterlogged, very shallow, rocky or strongly saline land gives weak trees. Test the soil before planting.",
         "The tree needs a warm climate and a cool, dry spell in winter to flower. Fog, mist or rain at flowering invite disease, and frost harms young trees and panicles.",
         ("html", "<p>Choose a variety that sells in your market and suits your region:</p>" + _TM([
           ["Kesar", "Gujarat, especially Saurashtra and south Gujarat", "Popular for fresh sale and export; see our guides on high density planting and flowering care."],
           ["Alphonso (Hapus)", "Konkan and coastal Maharashtra", "Premium variety; sensitive to weather at flowering."],
           ["Dasheri, Langra, Chausa", "Uttar Pradesh and the north", "Traditional North Indian varieties."],
           ["Totapuri, Banganapalli, Neelam", "Southern states", "Widely grown for pulp and for fresh sale."],
           ["Amrapali, Mallika", "Several regions", "Hybrids often used where closer planting is planned."]],
           ["Variety", "Main region", "Note"]) + '<p class="note">Variety performance depends on your soil, water and market. Ask your KVK or state horticulture department which varieties are recommended in your district.</p>')]),
       ("Planting a new orchard", [
         "Buy grafted plants from a nursery you trust, with a healthy graft union and a straight stem.",
         "Dig pits well before planting and fill them with topsoil mixed with well-rotted compost or farmyard manure.",
         "Traditional orchards use wide spacing. Newer orchards use closer spacing and prune every year to keep trees small; read our guide to <a href=\"/guides/high-density-kesar-mango\">high density Kesar mango</a> before choosing.",
         "In most of India the best planting time is the start of the monsoon, July to August, so young plants establish without heat stress.",
         "Stake and shade young trees, and protect them from strong wind and, in cold areas, frost."]),
       ("Caring for young trees", [
         "Water young trees regularly in the first two to three years, in small amounts and often, never leaving the root zone flooded.",
         "Keep the trunk base clean of weeds and mulch the soil to hold moisture.",
         "Train the tree to a strong frame. Many growers remove early flowers in the first years so the tree builds branches and roots before it carries fruit.",
         "Grafted trees usually begin to bear in about three to five years. Full cropping takes longer, and depends on variety, spacing and care."]),
       ("Feeding a mango tree through the year", [
         ("html", "<p>Feed on the evidence from a soil test, and split feeding across the year. A common pattern in Gujarat:</p>" + _TM([
           ["After harvest (June to July)", "Compost or farmyard manure around the canopy edge. Feed the tree so the new shoots can grow strong and mature in time for flowering."],
           ["August to September", "Second feeding as advised for your soil. Support the new flush."],
           ["October to November", "Stop nitrogen. Correct zinc or boron only if a soil or leaf test shows a shortage."],
           ["Fruit set to fruit growth", "Steady moisture, and potash-rich feeding if your adviser recommends it for the fruit growth period."]],
           ["When", "What growers do"]) + '<p class="note">We do not print fertilizer or product doses here. The right amount depends on tree age, canopy size, variety and soil. Use your state agricultural university\'s recommendation, or ask us on ' + _MG + ' with your tree age, spacing and a recent soil test.</p>')]),
       ("Irrigation: the part most growers get wrong", [
         "Young trees: regular, light watering.",
         "Bearing trees: reduce and then stop irrigation from about November until panicles have emerged. Water and nitrogen in winter make the tree push leaves instead of flowers.",
         "Restart light, regular irrigation at fruit set, and keep moisture steady while fruit grows. Big swings between dry and wet increase fruit drop.",
         ("html", '<p>Full month-by-month detail is in <a href="/guides/mango-flowering-care">mango flowering care and spray schedule</a>.</p>')]),
       ("Pruning and canopy care", [
         "Prune right after harvest, not in winter. Remove dead, diseased and crossing branches and open the canopy to light and air.",
         "An open canopy reduces hoppers and powdery mildew, and helps sprays reach the inside of the tree.",
         "Winter pruning should be light, so you do not remove flowering wood."]),
       ("Pests and diseases to watch", [
         "The big three at flowering are hoppers, powdery mildew and, in humid or drizzly weather, anthracnose (blossom blight).",
         ("html", '<p>Learn to recognise each of them in <a href="/guides/mango-diseases-and-pests">mango diseases and pests</a> and <a href="/guides/mango-powdery-mildew">mango powdery mildew</a>.</p>'),
         "Use only products registered for mango, at the dose on the label, and rotate chemical groups between rounds."]),
       ("Flowering, fruit set and fruit drop", [
         "A tree sets far more fruit than it can carry, so some early drop is normal. Heavy drop follows stress: dry soil then sudden watering, heat, nutrient shortage or hopper damage.",
         ("html", '<p>See <a href="/crop-problems/mango-fruit-drop">mango fruit drop</a> and <a href="/crop-problems/mango-alternate-bearing">alternate bearing in mango</a> for causes and what growers can do.</p>')]),
       ("Harvest", [
         "Harvest mature fruit: the shoulders fill out and the skin colour lightens. Fruit picked too early ripens poorly and has weaker taste.",
         "Cut the fruit with a short piece of stalk, and keep the sap off the skin. Handle gently and keep fruit in shade.",
         "Start planning next year's crop at harvest: pruning and feeding right after picking decide how many mature shoots the tree has for flowering."]),
       ("Common mistakes", [
         "Irrigating and feeding nitrogen in November and December.",
         "Spraying at full bloom, which harms bees and flies that pollinate the flowers.",
         "Heavy pruning in winter.",
         "Copying spray doses from the internet instead of using the product label.",
         "Planting too close without a plan to prune every year."]),
       ("Where biostimulants fit", [
         ("html", '<p>Seaweed, humic and amino acid based products are used to help trees cope with stress and to support roots and fruit set. They work alongside good water, nutrition and protection, not instead of them. See <a href="/crops/mango">our mango page</a> for the Immunity Mango Special, or ask us on ' + _MG + '. Farmers\' results with any product are their own experiences, not promises.</p>')])],
      faq=[("When is the best time to plant mango in India?", "The start of the monsoon, July to August in most regions, so young plants establish without heat stress."),
           ("Which soil is best for mango farming?", "Deep, well-drained loam with a pH of about 5.5 to 7.5. Avoid waterlogged, very shallow or strongly saline land."),
           ("How long does a mango tree take to bear fruit?", "Grafted trees usually begin to bear in about three to five years. Full cropping takes longer and depends on variety, spacing and care."),
           ("How often should I water mango trees?", "Young trees need regular light watering. Bearing trees need water cut back from about November until panicles appear, then light, regular irrigation from fruit set."),
           ("When should I prune mango trees?", "Right after harvest. Keep winter pruning light so you do not remove flowering wood."),
           ("Why is my mango tree not flowering?", "Common reasons are late shoots that did not mature, water or nitrogen in winter, a warm winter, a heavy crop last year, or a young, shaded tree."),
           ("Which mango variety is best for Gujarat?", "Kesar is the most widely grown in Gujarat. Ask your KVK or state horticulture department which varieties suit your district."),
           ("How do I stop mango fruit drop?", "Keep soil moisture steady from fruit set, protect against hoppers, and make sure the tree is fed. Some early drop is natural.")]),

 dict(slug="mango-diseases-and-pests", date="2026-11-23",
      title="Mango Diseases and Pests: Symptoms, Causes and Control",
      h1="Mango diseases and pests: how to recognise them and what growers can do",
      desc="A plain guide to mango disease and pests: powdery mildew, anthracnose, malformation, sooty mould, dieback and canker, plus hoppers, mealybugs and fruit fly.",
      answer="The most common mango diseases are powdery mildew and anthracnose at flowering, malformation of shoots and panicles, sooty mould after hoppers, branch dieback, and bacterial canker on fruit. The main pests are hoppers, mealybugs, stem borers and fruit fly. Start with orchard hygiene, an open canopy and timely protection at panicle emergence, using products registered for mango at the label dose.",
      sections=[
       ("Diseases at a glance", [
         ("html", _TM([
           ["Powdery mildew", "White powdery coating on panicles, flowers and young fruit; flowers dry and drop", "Cool nights with mist or fog at flowering", "Protect at panicle emergence"],
           ["Anthracnose (blossom blight)", "Black spots on flowers, leaves and fruit; flowers turn dark and fall", "Humid, drizzly or cloudy weather", "Clean orchard, protect in wet spells"],
           ["Malformation", "Dense, bunched, deformed shoots or panicles that give no fruit", "Fungal; spreads on infected plant parts", "Remove and destroy malformed parts"],
           ["Sooty mould", "Black coating on leaves and panicles", "Honeydew left by hoppers and mealybugs", "Control the insects first"],
           ["Dieback", "Branches dry from the tip downward", "Fungal infection through wounds, stress", "Prune below the dead part and clean up"],
           ["Bacterial canker", "Black, raised spots with a yellow halo on leaves and fruit; cracks on fruit", "Bacterial; spreads in wet, windy weather", "Hygiene, resistant planting material"]],
           ["Disease", "What you see", "Favoured by", "First step"]))]),
       ("Powdery mildew and anthracnose at flowering", [
         "These two can destroy the crop before it sets. Powdery mildew likes cool, misty nights. Anthracnose follows humid, drizzly or cloudy weather.",
         ("html", '<p>Protection works best before symptoms are widespread. See the full timing on <a href="/guides/mango-powdery-mildew">mango powdery mildew</a> and <a href="/guides/mango-flowering-care">mango flowering care</a>.</p>')]),
       ("Malformation", [
         "Affected shoots and panicles become thick, bunched and deformed, and do not set fruit.",
         "Cut off malformed parts and burn or bury them away from the orchard. Do not leave them under the tree.",
         "Plant healthy, certified grafts, and do not take planting material from affected orchards."]),
       ("Dieback and canker", [
         "For dieback, prune a hand's length below the dead part, remove the cut branches from the orchard and keep the tree out of water and nutrient stress.",
         "For canker, avoid wounding fruit and trees during wet weather, and keep the orchard clean. Ask your KVK for the current recommendation in your district."]),
       ("The pests that cause the most loss", [
         ("html", _TM([
           ["Mango hoppers", "Small, wedge-shaped insects that jump when you tap a branch; sticky honeydew and sooty mould", "Open the canopy, protect panicles at emergence and again before flowers open if needed"],
           ["Mealybugs", "White cottony insects climbing the trunk to the panicles", "Clean up and stop them climbing the trunk early in the season"],
           ["Stem borers", "Holes in the trunk with sawdust-like frass, drying branches", "Remove and destroy badly affected branches; ask your KVK about control"],
           ["Fruit fly", "Maggots in ripening fruit, fruit falling with soft spots", "Collect and destroy fallen fruit; traps are used in many orchards"]],
           ["Pest", "How to recognise it", "What growers do"]))]),
       ("How to protect your orchard without wasting money", [
         "Walk the orchard every week from November and look at panicles, not only at leaves.",
         "Keep the canopy open and the floor clean. This alone reduces hoppers and mildew.",
         "Spray only at the stages that matter, not on a fixed calendar. Never spray at full bloom.",
         "Use products registered for mango, at the dose on the label. Mixing many chemicals in one tank does not work better.",
         "Rotate chemical groups between rounds so pests and fungus do not become resistant.",
         "Biological options such as Beauveria bassiana and Metarhizium anisopliae are listed in the government IPM package for mango.",
         ("html", '<p>Not sure what you are looking at? Send photos on ' + _MG + ' and our team will help you identify the problem. We do not print doses, because they depend on the product and the tree.</p>')]),
       ("Healthy trees resist better", [
         "A tree that is fed on the evidence from a soil test, watered steadily and pruned every year copes better with disease and pests. Seaweed and humic acid products can help trees cope with stress; they do not replace protection sprays. See the <a href=\"/guides/mango-farming-in-india\">complete mango farming guide</a>."])],
      faq=[("What are the common diseases of mango?", "Powdery mildew, anthracnose, malformation, sooty mould, dieback and bacterial canker. Powdery mildew and anthracnose are the most damaging at flowering."),
           ("Why are there black spots on mango fruit?", "Black spots are often anthracnose, which thrives in humid and rainy weather, or bacterial canker. Clean orchard hygiene and timely protection reduce both."),
           ("What is the white powder on mango flowers?", "Powdery mildew, a fungus that spreads in cool, misty nights. Protect panicles at emergence, before the powder appears."),
           ("What causes black coating on mango leaves?", "Sooty mould, which grows on honeydew left by hoppers and mealybugs. Control the insects and the mould fades."),
           ("How do I control mango malformation?", "Cut off the malformed shoots and panicles, remove them from the orchard and plant healthy, certified grafts."),
           ("Which pest harms mango flowers the most?", "Hoppers. They suck sap from panicles, so flowers dry and drop. Protect at panicle emergence and again before flowers open if needed.")]),

 dict(slug="mango-powdery-mildew", date="2026-11-23",
      title="Mango Powdery Mildew: Symptoms, Timing and Control",
      h1="Mango powdery mildew: how to spot it early and when to protect your flowers",
      desc="Mango powdery mildew explained: the white powder on panicles, the weather that triggers it, when to protect flowers, and how to avoid common spray mistakes.",
      answer="Powdery mildew shows as a white, powdery coating on mango panicles, flowers and young fruit. It spreads in cool nights with mist or fog during flowering. The fungus is easiest to stop before the powder appears, so protect panicles at emergence, repeat once before flowers open only if needed, never spray at full bloom, and use a product registered for mango at the label dose.",
      sections=[
       ("What powdery mildew looks like", [
         "A fine white or grey powder on the panicle stalk, flowers and tiny fruits. It rubs off on your finger.",
         "Affected flowers shrivel and fall, and young fruits turn dull, then drop. A heavily infected panicle may end with no fruit.",
         "Leaves, especially young ones, can show white patches too."]),
       ("Do not confuse it with other problems", [
         ("html", _TM([
           ["White powder on panicles and flowers", "Powdery mildew", "Protect early; remove badly infected panicles"],
           ["Sticky shine, then black coating", "Sooty mould from hopper honeydew", "Control hoppers first"],
           ["Tiny jumping insects on a shaken panicle", "Hoppers", "Shake panicles over a white cloth to confirm"],
           ["Black spots on flowers in a drizzly spell", "Anthracnose (blossom blight)", "Different protection; see mango diseases"]],
           ["What you see", "Likely cause", "What to do"]))]),
       ("The weather that brings it", [
         "Cool nights with mist or fog, and warm, dry days, during flowering. This is exactly the weather of many Gujarat winters from December to February.",
         "Dense, shaded canopies hold humidity and make it worse. An open canopy lets air and sunlight dry the panicles."]),
       ("When to protect", [
         ("html", _TM([
           ["Before panicles", "Open the canopy after harvest; keep the orchard clean", "No spray needed"],
           ["Panicle emergence", "First protection, before the white coating appears", "Sulphur-based or other fungicide recommended for mango powdery mildew"],
           ["2 to 3 weeks later, before flowers open", "Second round, only if mildew is present or the weather stays favourable for it", "Use a different chemical group from the first round"],
           ["Full bloom", "No spray", "Let bees and flies pollinate"],
           ["Fruit set", "Check again; protect only if mildew is active", "Follow the label"]],
           ["Stage", "What growers do", "Note"]) + '<p class="note">The government IPM package for mango lists wettable sulphur, hexaconazole, penconazole and azoxystrobin among the options for powdery mildew. We do not print doses: use the dose on the label of a product registered for mango, or your state agricultural university\'s recommendation. Sulphur can scorch leaves and flowers in high heat, so spray in the early morning or evening.</p>')]),
       ("Remove and clean up", [
         "Cut off and destroy badly infected panicles; the fungus survives in dormant buds and old infected tissue.",
         "Cover the whole panicle and the inner canopy when spraying, because the fungus hides inside.",
         "Avoid heavy nitrogen in winter. Soft, fast growth is more prone to infection."]),
       ("Mistakes that make mildew worse", [
         "Waiting until the powder is everywhere before acting.",
         "Spraying at full bloom, which drives away pollinators and can burn flowers.",
         "Repeating the same chemical group every time.",
         "Mixing many chemicals in one tank.",
         "Leaving a dense, shaded canopy."]),
       ("More help", [
         ("html", '<p>Full month-by-month care is in <a href="/guides/mango-flowering-care">mango flowering care and spray schedule</a>, and an overview of other problems is in <a href="/guides/mango-diseases-and-pests">mango diseases and pests</a>. Send photos of your panicles on ' + _MG + ' if you are unsure.</p>')])],
      faq=[("What is the white powder on my mango flowers?", "Most likely powdery mildew, a fungus that spreads in cool nights with mist or fog. It rubs off on your finger."),
           ("When should I spray for powdery mildew in mango?", "At panicle emergence, before the white coating appears, and again 2 to 3 weeks later before flowers open only if it is needed. Never at full bloom."),
           ("Which fungicide is best for mango powdery mildew?", "The government IPM package lists wettable sulphur, hexaconazole, penconazole and azoxystrobin among the options. Use a product registered for mango, at the label dose, and rotate groups between rounds."),
           ("Can I spray sulphur in hot weather?", "Sulphur can scorch in high heat, so spray in the early morning or evening and follow the label."),
           ("Can mango recover from powdery mildew?", "Healthy flowers can still set fruit if infection is stopped early. Flowers and fruitlets that are heavily coated usually drop."),
           ("Does a dense canopy cause powdery mildew?", "It makes it worse by holding humidity. An open canopy, pruned after harvest, helps panicles dry.")]),
]
# add a short 'more on mango' link block to the existing flowering guide so equity flows to the new pillar
for _g in SEASON_GUIDES:
    if _g["slug"] == "mango-flowering-care":
        _g["sections"].append(("More on mango", [("html", '<p>Read the complete <a href="/guides/mango-farming-in-india">mango farming guide</a>, and the guides on <a href="/guides/mango-powdery-mildew">powdery mildew</a> and <a href="/guides/mango-diseases-and-pests">mango diseases and pests</a>.</p>')]))
SEASON_GUIDES = MANGO_GUIDES + SEASON_GUIDES

DEEP.update({
"/guides/mango-farming-in-india": dict(
  hook="A mango tree decides next year's crop the moment this year's harvest ends. What you do in June and July, and what you leave alone in November, matters more than any spray in February.",
  stats=[("5.5 to 7.5", "soil pH range mango grows best in"), ("Nov-Feb", "the window that decides the flowering")],
  sources=[("NIPHM: IPM package for mango", "https://niphm.gov.in/IPMPackages/Mango.pdf"),
           ("ICAR-Central Institute for Subtropical Horticulture", "https://cish.res.in/")]),
"/guides/mango-diseases-and-pests": dict(
  hook="Most mango disease is decided by weather you cannot change and habits you can: an open canopy, a clean floor, and protection at the right week.",
  stats=[("Dec-Feb", "the flowering window when mildew and blight strike"), ("0", "sprays at full bloom")],
  sources=[("NIPHM: IPM package for mango", "https://niphm.gov.in/IPMPackages/Mango.pdf")]),
"/guides/mango-powdery-mildew": dict(
  hook="By the time the white powder is visible, the flowers are already losing. The week that matters is the week the panicle comes out.",
  stats=[("Panicle emergence", "the moment to protect, before the powder appears"), ("0", "sprays at full bloom")],
  sources=[("NIPHM: IPM package for mango", "https://niphm.gov.in/IPMPackages/Mango.pdf")]),
})
