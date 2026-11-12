# Deeper content for pages that were too thin. Keyed by page path.
# hook: opening reality check (true, sourced where it carries a number). stats: [(figure, label)].
# add: extra sections [(heading, items)] in the same format as content_knowledge.py. faq: extra questions. sources: [(name, url)].
# Rules: no doses, no promises, results only as attributed farmer experience, no competitor names.
CSE = ("Centre for Science and Environment, Indian soils severely deficient in essential nutrients (Soil Health Card data, 2023-25)", "https://www.cseindia.org/indian-soils-severely-deficient-in-essential-nutrients-12908")
NITI = ("NITI Aayog / EPW, Fertiliser use and imbalance in India", "https://www.niti.gov.in/sites/default/files/2021-08/4_EPW_Article_Fertiliser_Use_and_Imbalance_in_India.pdf")

DEEP = {
"/crop-problems/mango-fruit-drop": dict(
  hook="In one study of Indian mango varieties, about half of the young fruit fell in the first 15 days after set, and Alphonso lost close to 90% of its set fruit before harvest. Most growers think they have a disease problem. Usually they have a stress and reserves problem.",
  stats=[("~50%", "of young fruit can drop in the first 15 days"), ("~90%", "of set fruit lost in Alphonso in one study"), ("45 days", "the main drop period after fruit set")],
  add=[("The three waves of drop, and what each one tells you", [
         "<strong>Wave 1, flowers and pinhead fruit (first 1 to 2 weeks):</strong> mostly unfertilised flowers. This is normal and you cannot stop it. Poor pollination in cloudy, wet or very cold weather makes it heavier.",
         "<strong>Wave 2, pea to marble size (2 to 6 weeks):</strong> the tree drops fruit it cannot feed. This is where water stress, hot winds, hoppers and a hungry tree show up. This is the drop you can reduce.",
         "<strong>Wave 3, near-mature fruit (April to May):</strong> heat waves, sudden heavy irrigation after a dry spell, fruit fly and stem-end problems. Losses here hurt most, because the fruit is almost ready."]),
       ("A 10-minute field check before you spray anything", [
         "Shake a few panicles over a white cloth. Many small jumping insects means hoppers, not a nutrient problem.",
         "Look at the dropped fruit: a black, shrivelled stalk end points to disease; a clean break at the stalk points to stress.",
         "Dig a hand-deep hole in the basin. Dry, cracked soil during fruit set is the most common cause we see in Saurashtra and Kutch orchards.",
         "Compare trees: if only the trees that carried a heavy crop last year are dropping, the cause is low reserves, not weather.",
         "Note the date and weather. Drop that follows two or three days of hot, dry wind is weather stress."]),
       ("Mistakes that make drop worse", [
         "Flooding the basin after a long dry gap. The sudden swing shocks the tree and fruit falls within days.",
         "Spraying mixtures of several chemicals during full bloom, which can harm flowers and pollinating insects.",
         "Feeding the tree only when fruit is already falling. Reserves are built after harvest, months earlier.",
         "Ignoring the basin: bare, hot soil loses water fast. A mulch of dry leaves or straw keeps roots cooler."]),
       ("What some growers tell us", [
         ("html", "<p>Mango growers who switched from irregular to light, regular watering at fruit set, and who fed their trees soon after harvest, have told us they saw less drop the following season. That is their experience, in their orchards; soil, variety, weather and care decide the result in yours.</p>")])],
  faq=[("Is 90% fruit drop normal in mango?", "Losing most of the flowers and pinhead fruit is normal. Losing most fruit at marble size or later is not, and usually points to water stress, heat, pests or a weak tree."),
       ("Do hormone sprays stop mango fruit drop?", "Some plant growth regulators are used under expert advice, but they cannot make up for a dry, hungry or pest-hit tree. Fix water, pests and nutrition first, and follow your local horticulture office on any spray.")],
  sources=[("Studies on fruit drop in mango varieties, Journal of Tropical Agriculture (Kerala Agricultural University)", "https://jtropag.kau.in/index.php/ojs2/article/view/93")]),

"/crop-problems/mango-alternate-bearing": dict(
  hook="A mango tree that gives you a bumper crop this year is quietly spending next year's crop. That is why so many orchards swing between a rich year and a poor one. The cycle can be softened, but only by acting in the months after harvest, when most growers have stopped looking at the tree.",
  add=[("Why the 'on' year steals from the 'off' year", [
         ("html", "<p>Mango flowers form on shoots that grew and matured in the previous season. Those shoots need food: sugars and starch made by the leaves and stored in the branches and roots. In an 'on' year, the fruit pulls almost all of that food. The tree makes few new shoots, those shoots do not mature in time, and next season there is little to flower on.</p>"
                  "<p>Varieties differ. Many traditional varieties, including Alphonso, Kesar, Langra and Dashehari, are known for strong alternate bearing. Some newer hybrids, such as Amrapali, were bred partly to bear more regularly.</p>")]),
       ("The after-harvest calendar that decides next year", [
         "<strong>Within a month of harvest:</strong> remove dead, crossing and inward-growing branches so light reaches the canopy, and clear the basin.",
         "<strong>Early monsoon:</strong> this is when the tree builds new shoots. Balanced feeding and healthy soil now matter more than any spray at flowering.",
         "<strong>Through the monsoon:</strong> keep drainage open. Waterlogged roots cannot feed the new flush.",
         "<strong>Before flowering:</strong> the new shoots must mature, turning from soft and bronze to hard and dark green. Avoid heavy nitrogen late in the season, which pushes fresh soft growth instead.",
         "<strong>At flowering and fruit set:</strong> protect the panicles from hoppers and keep soil moisture steady."]),
       ("Signs your tree is heading into an 'off' year", [
         "Very few new shoots after harvest, or shoots that stay short.",
         "Leaves that are pale, small or fall early.",
         "A crop last season that bent the branches.",
         "Trees on the same farm flowering well while one block stays green."]),
       ("What about chemical flower inducers?", [
         ("html", "<p>Growth-retarding chemicals are used in some regions to force flowering. They are not a substitute for a well-fed tree, and wrong use can harm trees and leave residues. Use them only on the advice of your state horticulture department or a mango research station, and never on weak or young trees.</p>")])],
  faq=[("Can alternate bearing be stopped completely?", "Rarely in strongly alternate varieties, but good after-harvest care and thinning of very heavy crops can make the swings much smaller."),
       ("Which mango variety bears every year?", "Some hybrids, such as Amrapali, bear more regularly than many traditional varieties. Ask your local mango research station which suits your area.")],
  sources=[]),

"/crop-problems/citrus-dieback": dict(
  hook="In the 2000s the orange belt around Nagpur lost half its orange area in under ten years, and trees that once lived 65 to 70 years started dying at 30. Root rot, pests, heat and tired soil did it together. Dieback at the branch tip is the first warning that the roots are in trouble.",
  stats=[("50%", "of Nagpur division's orange area lost, 1995 to 2004"), ("30-35 yrs", "orchard life, down from 65-70 years"), ("46°C+", "the 2010 heat that killed lakhs of trees")],
  add=[("Read the tree from the bottom up", [
         "<strong>Collar and trunk:</strong> gum oozing from cracked bark near soil level means gummosis (Phytophthora). Scrape the bark gently: brown, wet tissue below is a bad sign.",
         "<strong>Feeder roots:</strong> scratch the soil under the canopy edge. Healthy feeder roots are white or cream and firm. Brown roots that slip their skin are rotting.",
         "<strong>Leaves:</strong> yellow patches between veins on new leaves point to zinc or iron shortage; blotchy, uneven yellowing on one side of the tree needs an expert check for greening disease.",
         "<strong>Twigs:</strong> small holes and sawdust on branches mean bark borer. Dieback from the tip with no other signs often follows a root problem."]),
       ("Why alkaline and salty soils make it worse", [
         ("html", "<p>Much of western and central India has alkaline, calcareous soil. In such soil, zinc and iron are present but locked in forms the roots cannot take up. A citrus tree on weak roots in alkaline soil runs short of exactly the nutrients it needs to make new leaves, so branches thin out and die back. Salty irrigation water adds to the damage by burning the fine roots.</p>")]),
       ("A practical rescue plan", [
         "Stop water touching the trunk: use a double-ring basin so the area around the trunk stays dry.",
         "Open drainage before the monsoon; standing water for even a few days damages roots.",
         "Get an expert to confirm gummosis or greening before you spend on sprays. Greening has no cure, and infected trees spread it.",
         "Test soil and irrigation water. Fix pH and salinity issues you can fix, and feed micronutrients the tree is short of.",
         "Prune dead wood back to healthy tissue after the cause is known, and seal large cuts.",
         "Rebuild organic matter in the basin every season."])],
  faq=[("Is citrus dieback contagious?", "Dieback itself is a symptom. Some causes, such as Phytophthora and greening disease, do spread, so find the cause early."),
       ("Can an old declining lemon tree be saved?", "If the collar and a good part of the roots are healthy, yes, often. If the trunk is girdled by rot or the tree has greening, replanting with healthy nursery stock is usually wiser.")],
  sources=[("Down To Earth, Orange tumbles (2012)", "https://www.downtoearth.org.in/environment/orange-tumbles-37976"),
           ("ICAR-Central Citrus Research Institute, Nagpur", "https://ccri.icar.gov.in/")]),

"/crop-problems/potato-small-tubers": dict(
  hook="India harvests roughly half as many tonnes of potato per hectare as the Netherlands or the USA, on average. A big part of that gap is decided in two short windows of the crop that many growers miss: tuber initiation and bulking.",
  stats=[("28-30 t/ha", "average Indian potato yield"), ("about 2x", "yield in the Netherlands and the USA"), ("25-30%", "share of Indian growers using quality seed")],
  add=[("Two windows that decide your harvest", [
         "<strong>Tuber initiation (about 5 to 8 weeks after planting, depending on variety):</strong> stolons swell and the plant decides how many tubers to carry. Dry soil, heat, or a big push of nitrogen at this time means fewer tubers.",
         "<strong>Bulking (the next 6 to 8 weeks):</strong> the leaves send sugars down and tubers grow fast. Every day of water stress or leaf loss now means smaller potatoes. Healthy leaves are your factory."]),
       ("Seed is half the story", [
         ("html", "<p>Only about a quarter to a third of Indian potato growers use quality-assured seed; the rest plant tubers saved from the last crop. Saved seed carries viruses that build up year after year, giving weak plants that set few, small tubers. Buying certified or well-tested seed every two or three seasons is one of the cheapest yield fixes available.</p>")]),
       ("A quick dig test", [
         "Around 45 days after planting, carefully dig two plants from a good patch and two from a weak patch.",
         "Count the swelling stolon tips. Few tips on the weak plants points to stress at initiation.",
         "Check the roots: brown, short roots point to hard or salty soil, or waterlogging.",
         "Look at the lower leaves: early yellowing or blight spots mean the leaf factory is closing early."]),
       ("Common mistakes", [
         "Heavy urea late in the crop. The plant grows leaves, not potatoes.",
         "Long gaps between irrigations during bulking, then heavy watering. This can cause cracks and hollow heart.",
         "Ignoring potash. Potato needs plenty of it for tuber filling and quality.",
         "Waiting for blight before protecting leaves in cold, foggy weather."])],
  faq=[("At what stage do potatoes grow fastest?", "During bulking, after tuber initiation. Steady water and healthy leaves at this stage decide tuber size."),
       ("Why are my potatoes many but small?", "A plant that sets many tubers but cannot feed them gives small potatoes. Weak leaves, water stress or low potash during bulking are the usual causes.")],
  sources=[("FreshPlaza, India's potato yield gap linked to seed system weaknesses (Aug 2026)", "https://www.freshplaza.com/asia/article/9863197/india-s-potato-yield-gap-linked-to-seed-system-weaknesses/"),
           ("ICAR-Central Potato Research Institute", "https://cpri.icar.gov.in/")]),

"/crop-problems/sugarcane-poor-germination": dict(
  hook="Every gap in a sugarcane row is a clump that never pays you back, for the plant crop and every ratoon after it. Gaps are cheapest to prevent on planting day and most expensive to ignore.",
  add=[("Why a gap costs more than it looks", [
         ("html", "<p>Sugarcane is a long crop, and a ratoon grows back from the same stubble. A gap in the plant crop stays a gap in the first and second ratoon unless it is filled early. Neighbouring clumps do send out more tillers into the space, but rarely enough to make up the loss, and late tillers often die before harvest.</p>")]),
       ("Planting-day checklist", [
         "Take setts from a healthy nursery crop that is about 8 to 10 months old. Old, mature cane germinates more slowly.",
         "Plant within a day of cutting; setts that dry in the sun lose buds.",
         "Check buds before planting: plump, firm buds with no damage. Discard setts with dried, split or red-rotted tissue.",
         "Plant into soil that is moist but not muddy; irrigate lightly soon after if the soil is dry.",
         "Do not plant too deep; a light soil cover is enough.",
         "Treat setts as recommended by your sugar factory or agriculture office against sett rot and termites."]),
       ("Newer planting methods worth asking about", [
         ("html", "<p>Single-bud setts and nursery-raised seedlings (settlings) are used more widely now. They need less seed cane, and transplanting healthy seedlings gives a more even stand. Ask your sugar factory's cane department whether they supply seedlings in your area.</p>")]),
       ("Gap filling: the 30-day rule", [
         "Walk the field three to four weeks after planting and mark gaps longer than about a foot.",
         "Fill gaps with pre-sprouted setts or seedlings raised at the same time as the main planting.",
         "Gaps filled after about 45 days rarely catch up with the crop around them."])],
  faq=[("Why do sugarcane setts rot instead of sprouting?", "Usually waterlogged or very wet soil, damaged setts, or setts taken from a diseased crop. Sett treatment and good drainage lower the risk."),
       ("Does soaking setts help germination?", "Soaking setts in water for some hours before planting is a common practice, especially when the cane is a little old or dry. Follow your sugar factory's advice on any treatment added to the water.")],
  sources=[("ICAR-Sugarcane Breeding Institute, Coimbatore", "https://sugarcane.icar.gov.in/")]),

"/crop-problems/apple-root-rot": None,
}

GUIDE_DEEP = {
"/guides/compost-and-humic-acid": dict(
  hook="Soil Health Card tests of about 1.3 crore samples in 2023-25 found almost half of India's farm soils low in organic carbon. Soil without organic matter holds less water, holds fewer nutrients and lets more of your fertilizer wash away.",
  stats=[("48.5%", "of tested soils low in organic carbon"), ("64%", "low in nitrogen"), ("1.3 crore", "soil samples tested, 2023-25")],
  add=[("Compost and humic acid are not the same thing", [
         "<strong>Compost</strong> is decomposed farm waste. It adds organic matter, food for soil life and small amounts of many nutrients. You need tonnes of it per acre to change soil, and it works over seasons.",
         "<strong>Humic acid</strong> is a concentrated part of organic matter, extracted from sources such as leonardite or lignite. It is used in much smaller amounts and mainly helps the soil hold and release nutrients and supports root growth.",
         "Neither replaces the other. Compost builds the soil body; humic substances help the root zone work better while that body is being built."]),
       ("How to make compost that is actually ready", [
         "Mix green material (fresh crop waste, dung) with brown material (dry leaves, straw).",
         "Keep the heap moist like a squeezed sponge, not wet.",
         "Turn it every two to three weeks so air reaches the middle.",
         "Ready compost is dark, crumbly, smells like soil and is no longer hot. Half-made compost can rob nitrogen from your crop."]),
       ("When humic acid makes sense", [
         "Sandy soils that hold little water and lose nutrients fast.",
         "Old, heavily cropped land where organic matter is very low.",
         "Crops at transplanting or root-building stages.",
         "Alongside fertilizers, to help more of what you apply stay in the root zone. Check the product's FCO grade and label before buying."])],
  faq=[("Can humic acid replace compost?", "No. Humic acid is used in small amounts and supports the root zone; compost adds bulk organic matter and soil life. They work best together."),
       ("How do I know if my soil is low in organic carbon?", "A soil test reports organic carbon. Many Indian soil labs class values below about 0.5% as low.")],
  sources=[CSE]),

"/guides/how-to-take-a-soil-sample": dict(
  hook="A soil test is only as good as the sample. A spoonful taken from one corner, near the dung heap or under a tree can give a report that is wrong for the whole field, and you spend a season fertilizing the wrong way.",
  add=[("Step by step, the right way", [
         "Divide the farm into blocks that look and behave alike: same soil colour, same crop history, same slope.",
         "In each block, take soil from 8 to 10 spots in a zig-zag walk.",
         "At each spot, scrape away grass and leaves, dig a V-shaped pit about 15 cm (6 inches) deep for field crops, and slice a thin layer from one side.",
         "For orchards, sample deeper, as advised by your lab, and from the area under the canopy edge where feeder roots are.",
         "Mix all the slices in a clean bucket, remove stones and roots, and keep about half a kilo.",
         "Dry it in shade, put it in a clean cloth or plastic bag, and label it with your name, field, crop and date."]),
       ("Where not to sample", [
         "Near bunds, channels, trees, compost or dung heaps, or where fertilizer was just applied.",
         "Wet, waterlogged patches, unless you want to test that patch separately.",
         "Using a rusty tool or a fertilizer bag, which can change the result."]),
       ("When to sample", [
         "After harvest and before the next sowing, when the field is empty.",
         "At least two months after the last fertilizer or manure application.",
         "Every two to three years, and the same time of year, so you can compare reports."]),
       ("Reading the report", [
         ("html", "<p>The main numbers are pH, EC (salt), organic carbon, nitrogen, phosphorus, potash and micronutrients such as zinc, iron and boron. The Soil Health Card scheme gives free tests through government labs. Ask the lab or your agriculture officer to explain the recommendation for your crop, and keep the old reports.</p>")])],
  faq=[("How deep should I take a soil sample?", "For most field crops, about 15 cm (6 inches). For orchards and deep-rooted crops, ask your lab; deeper samples are common."),
       ("Can I mix samples from two different fields?", "Only if they have the same soil, crop history and management. Otherwise send separate samples.")],
  sources=[("Soil Health Card scheme, Government of India", "https://soilhealth.dac.gov.in/")]),

"/guides/why-yields-fall-on-old-land": dict(
  hook="Many farmers now put more fertilizer on the same field than their fathers did and harvest no more. The soil is not lazy. It is short of what the fertilizer bag does not contain.",
  stats=[("8.2:3.2:1", "India's N:P:K use in 2012-13"), ("4:2:1", "the long-used reference ratio"), ("48.5%", "of tested soils low in organic carbon")],
  add=[("Five reasons old land gives less", [
         "<strong>Imbalanced feeding:</strong> India uses far more nitrogen than potash. Urea makes plants green, but without enough potash, phosphorus, sulphur and micronutrients the extra nitrogen is wasted.",
         "<strong>Hidden hunger:</strong> zinc, boron, sulphur and iron are taken out with every harvest and rarely put back. Shortage shows as weak yields long before it shows on the leaves.",
         "<strong>Falling organic matter:</strong> crop residue burnt or removed, little compost added. The soil holds less water and fewer nutrients.",
         "<strong>Hard soil:</strong> repeated tillage at the same depth makes a hard layer that roots cannot cross.",
         "<strong>Salt build-up:</strong> salty borewell water and poor drainage slowly push salt into the root zone."]),
       ("How to tell which problem is yours", [
         "Get a soil test that includes organic carbon, EC and micronutrients, not just NPK.",
         "Test your irrigation water once; salty water explains many 'unexplained' yield falls.",
         "Dig a pit and look for a hard layer and where roots stop.",
         "Compare your best and worst patches; the difference is usually soil, not seed."]),
       ("Bringing old land back", [
         "Feed by soil test, with potash, sulphur and micronutrients where needed.",
         "Return crop residue to the soil and add compost or farmyard manure every season.",
         "Rotate with a pulse or green manure crop.",
         "Break hard layers with deeper tillage once every few years.",
         "Manage salty water with drainage and, where advised, gypsum."])],
  faq=[("Why does more urea not increase my yield?", "Because the crop is limited by something else, often potash, sulphur, zinc or poor roots. Adding more of what is not short does not help."),
       ("How long does it take to revive tired soil?", "Some changes, such as correcting a micronutrient shortage, show in one crop. Building organic matter takes several seasons of steady effort.")],
  sources=[NITI, CSE]),

"/guides/what-are-biostimulants": dict(
  hook="Until 2021, there was no legal category for biostimulants in India, and almost anything could be sold under that name. Today a biostimulant has to be listed in Schedule VI of the Fertiliser (Control) Order to be sold legally. Many farmers still do not know to check.",
  add=[("The main types of biostimulants", [
         "<strong>Seaweed extracts:</strong> from species such as Ascophyllum, Kappaphycus and Sargassum. Used for stress tolerance, flowering and fruit set.",
         "<strong>Humic and fulvic substances:</strong> support the root zone and nutrient holding in soil.",
         "<strong>Protein hydrolysates and amino acids:</strong> building blocks that the plant can use during stress and fast growth.",
         "<strong>Botanical extracts:</strong> plant-derived extracts listed under the Schedule.",
         "Biofertilisers (living bacteria and fungi) are a separate category under the same order, with their own standards."]),
       ("What a biostimulant is not", [
         "Not a fertilizer: it does not replace NPK and micronutrients the soil lacks.",
         "Not a pesticide or fungicide: it does not kill pests or cure disease.",
         "Not magic: results depend on soil, water, weather and timing, and on fixing the main problem first."]),
       ("How to check a product before you buy", [
         "Look for the FCO Schedule VI grade name on the label, and the manufacturer's registration details.",
         "Read the composition: the active content should be stated as a percentage.",
         "Prefer products with clear use instructions for your crop and stage.",
         "Be careful of labels that promise a fixed yield increase. Honest suppliers talk about farmer experiences and conditions."]),
       ("When biostimulants are worth using", [
         ("html", "<p>They earn their place at stress points: transplanting, flowering and fruit set, heat or cold spells, salty water, and recovery after a disease or pest attack. Growers who use them at these stages, on a crop that is already fed properly, are the ones who most often tell us they saw a difference. That is their experience; your soil and season decide yours.</p>")])],
  faq=[("Are biostimulants legal in India?", "Yes, when the product matches a grade listed in Schedule VI of the Fertiliser (Control) Order and the seller meets registration rules."),
       ("Can I use a biostimulant instead of fertilizer?", "No. Biostimulants help the plant use nutrients and handle stress; they do not supply the bulk nutrients a crop needs.")],
  sources=[("Department of Agriculture and Farmers Welfare, Fertiliser (Control) Order", "https://agriwelfare.gov.in/")]),
}

DEEP = {k: v for k, v in DEEP.items() if v}
DEEP.update(GUIDE_DEEP)
