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

# ---------------- Batch 2: crop pages and hubs
DEEP.update({
"/crops/chilli": dict(
  hook="India grows more chilli than any other country, yet one tiny insect can wipe out a field: thrips and whiteflies carry leaf curl, and once a plant is curled it rarely bears well again. In chilli, the battle is won in the nursery, weeks before the first flower.",
  add=[("Where chilli growers lose money", [
         "<strong>Leaf curl:</strong> spread by thrips, whitefly and mites. Infected plants stay stunted and drop flowers. Prevention is the only cure.",
         "<strong>Flower drop in heat:</strong> above about 35°C, or when watering is irregular, chilli drops flowers in large numbers.",
         "<strong>Plants that stop early:</strong> chilli is picked for months. A plant not fed after each picking runs out of strength and the late pickings, often the best paid, are lost.",
         "<strong>Fruit rot and die-back:</strong> follow rain and humid weather; dead twig tips and spotted fruit are the warning."]),
       ("A simple weekly routine in the field", [
         "Turn over a few leaves each week and look underneath for thrips and whitefly; act early, before numbers explode.",
         "Remove and destroy the first curled plants you see; they spread the virus.",
         "Keep yellow and blue sticky traps around the field to see what is flying in.",
         "Water lightly and regularly; avoid long dry gaps followed by flooding.",
         "Feed after every picking so the next flush of flowers has food."])],
  faq=[("Can a chilli plant with leaf curl recover?", "Mild curl from mites can recover after control, but virus leaf curl does not. Remove infected plants early and control the insects that spread it."),
       ("Why do chilli plants stop fruiting after a few pickings?", "Usually the plant runs short of food and roots after heavy cropping, often with heat or water stress. Feeding after each picking and steady water keep it bearing longer.")],
  sources=[("Spices Board India, chilli", "https://www.indianspices.com/")]),

"/crops/maize": dict(
  hook="In 2018 a new pest arrived in Karnataka and spread across India in about a year: the fall armyworm. It feeds deep inside the maize whorl, where sprays struggle to reach. Fields that are not checked in the first 30 days can lose the crop before the farmer notices.",
  stats=[("2018", "fall armyworm first reported in India"), ("first 30 days", "when whorl damage is easiest to catch"), ("1 week", "the silking window that decides grain set")],
  add=[("The two weeks that decide your cob", [
         ("html", "<p>Maize tassels shed pollen and the silks catch it over only a few days. Each silk leads to one grain. If the plant is short of water, heat-stressed or the silks come late, many grains never form, and you see cobs with gaps and bare tips. Missing silking water costs more than missing water at almost any other stage.</p>")]),
       ("How to scout for fall armyworm", [
         "Walk the field in a W pattern twice a week for the first month.",
         "Look into the whorl for ragged holes in leaves and wet, sawdust-like droppings.",
         "Young larvae have a pale inverted Y on the head; older ones hide deep in the whorl.",
         "Act on the advice of your agriculture office when you find damage on a fair share of plants; early action is cheaper.",
         "Sow neighbouring fields at about the same time so the pest does not move from older to younger crops."])],
  faq=[("Why does my maize cob have an empty tip?", "Usually stress at silking or poor pollination: water shortage, heat, or silks emerging after pollen shed. Steady water around tasselling and silking helps most."),
       ("Is fall armyworm only a maize pest?", "It prefers maize but also attacks sorghum, other cereals and some vegetables.")],
  sources=[("ICAR-National Bureau of Agricultural Insect Resources (fall armyworm in India)", "https://www.nbair.res.in/")]),

"/crops/pulses": dict(
  hook="India is the world's biggest grower of pulses and still imports them every year. A pulse plant can make its own nitrogen fertilizer for free, through root nodules, but in tired or salty soil those nodules often never form, and the farmer pays for urea the plant could have made itself.",
  add=[("Read your roots: the nodule test", [
         "At 4 to 5 weeks, dig (do not pull) three plants with a spade and wash the roots gently.",
         "Count the nodules: a healthy plant has many, mostly on the main root.",
         "Cut a few open. Pink or red inside means they are fixing nitrogen. White, green or brown inside means they are not working.",
         "Few or dead nodules point to no Rhizobium on the seed, waterlogging, salty or very acidic soil, or heavy nitrogen fertilizer at sowing."]),
       ("Why flowers drop in pulses", [
         "Pulses make far more flowers than they can carry; some drop is normal.",
         "Heavy drop follows dry soil, hot winds, cloudy wet weather or pod borer attack.",
         "Too much nitrogen makes leafy plants that set fewer pods.",
         "Light irrigation at flowering, where water is available, and early borer control help most."])],
  faq=[("Do pulses need urea?", "Only a small starter amount, if any. A crop with healthy nodules makes most of its own nitrogen; heavy urea can actually reduce nodulation."),
       ("Why are my nodules white inside?", "They are not fixing nitrogen. Common reasons are wrong or no Rhizobium, waterlogging, drought or salty soil.")],
  sources=[("ICAR-Indian Institute of Pulses Research", "https://iipr.icar.gov.in/")]),

"/crops/cereals": dict(
  hook="A global study found that every 1°C rise in temperature cuts world wheat yield by about 6%. In much of India, a hot spell in March during grain filling, called terminal heat, quietly shrinks the grain just weeks before harvest.",
  stats=[("~6%", "wheat yield lost per 1°C of warming (global estimate)"), ("CRI", "crown root irrigation, about 3 weeks after sowing"), ("March", "the month terminal heat usually hits")],
  add=[("Three moments you cannot miss in wheat", [
         "<strong>Crown root initiation (about 20 to 25 days):</strong> the first irrigation now builds the root system and tillers. Missing it costs the most.",
         "<strong>Flowering:</strong> stress now means fewer grains per ear.",
         "<strong>Grain filling:</strong> hot, dry winds shrivel the grain. Timely sowing is the best protection, because late-sown wheat fills in the hottest weeks."]),
       ("Hidden hunger in cereal fields", [
         "Zinc shortage is common in Indian soils, especially alkaline and sandy ones; it shows as stunted plants with pale stripes or brown spots.",
         "Sulphur shortage looks like nitrogen shortage but starts on young leaves.",
         "Fields that grew wheat after rice or bajra for many years often need a soil test for micronutrients, not just more urea."])],
  faq=[("Why is my wheat grain shrivelled?", "Usually heat or water stress during grain filling, late sowing, rust disease or lodging. Sowing on time is the strongest protection."),
       ("When should wheat get its first irrigation?", "At crown root initiation, about three weeks after sowing, unless your local agriculture office advises otherwise for your area and variety.")],
  sources=[("Asseng et al., Rising temperatures reduce global wheat production, Nature Climate Change (2015)", "https://www.nature.com/articles/nclimate2470"),
           ("ICAR-Indian Institute of Wheat and Barley Research", "https://iiwbr.icar.gov.in/")]),

"/crops/cumin": dict(
  hook="Gujarat and Rajasthan grow almost all of India's cumin, and India grows most of the world's. It is also one of the riskiest crops a farmer can sow: two or three cloudy, humid days at flowering can bring blight that turns a green field brown within a week.",
  add=[("The two diseases that decide your cumin crop", [
         "<strong>Wilt:</strong> plants yellow, droop and dry, often in patches, usually in fields where cumin was grown recently. The fungus lives in the soil for years, so rotation matters.",
         "<strong>Blight:</strong> brown spots on leaves and stems after cloudy or foggy weather, spreading fast. Watch the forecast at flowering and act on your agriculture office's advice before it spreads."]),
       ("Low-cost habits that protect cumin", [
         "Rotate: avoid cumin in the same field more often than once in three years.",
         "Sow on time; late-sown cumin flowers in riskier weather.",
         "Irrigate lightly; cumin hates wet soil and standing water.",
         "Do not sow too thick; crowded plants stay humid and blight spreads faster.",
         "Use clean, treated seed from a healthy crop."])],
  faq=[("Why does my cumin field dry in patches?", "Patchy drying is usually wilt from soil-borne fungus, made worse by heavy irrigation and repeated cumin in the same field."),
       ("How often should cumin be irrigated?", "Lightly and only as needed; heavy or frequent irrigation raises the risk of wilt and blight. Follow your local agriculture office for your soil.")],
  sources=[("Spices Board India, cumin", "https://www.indianspices.com/")]),

"/crops/paddy": dict(
  hook="In parts of India, transplanted paddy turns rusty brown and stops growing a few weeks after transplanting. Farmers call it khaira. It is not a disease at all: it is zinc hunger, and the standing water of a paddy field is part of the cause.",
  add=[("Why paddy soils run short of zinc", [
         ("html", "<p>When a field is flooded, the soil loses oxygen and its chemistry changes. Zinc becomes harder for roots to take up, especially in alkaline, calcareous or high-phosphorus soils. The result is khaira: rusty spots on older leaves, stunted hills and poor tillering two to four weeks after transplanting.</p>")]),
       ("Checks that save a paddy crop", [
         "Count tillers per hill at mid-tillering; few tillers early means fewer panicles later.",
         "Look for rusty brown spots on older leaves after transplanting; get a zinc check if they appear.",
         "Do not keep fields flooded deeper than the stage needs; brief drying in the tillering stage, where advised, helps roots.",
         "Watch for stem borer dead hearts and leaf folder in the vegetative stage.",
         "At flowering, keep water steady; stress now gives chaffy, empty grain."])],
  faq=[("What is khaira disease in paddy?", "It is zinc deficiency, not an infection. It shows as rusty brown leaves and stunted plants a few weeks after transplanting, mostly on alkaline or calcareous soils."),
       ("Why is my paddy grain chaffy?", "Chaffy grain usually follows stress at flowering: heat, cold, drought, pests or disease at that stage.")],
  sources=[("ICAR-National Rice Research Institute", "https://icar-nrri.in/")]),

"/crops/pomegranate": dict(
  hook="In the 2000s, bacterial blight, which farmers call telya, swept through pomegranate orchards in Maharashtra and Karnataka and forced many growers to uproot. The lesson for every grower: in pomegranate, clean orchard habits matter as much as fertilizer.",
  add=[("Why fruit cracks", [
         ("html", "<p>The skin of a growing pomegranate hardens as it matures. If the soil stays dry for a while and then gets heavy water, or heavy rain, the inside swells faster than the skin can stretch, and it cracks. Steady, light watering through fruit growth, mulching, and enough calcium and boron in the plant all lower the risk.</p>")]),
       ("Orchard hygiene against telya", [
         "Collect and destroy fallen infected leaves, fruit and pruned twigs; do not leave them in the orchard.",
         "Disinfect pruning tools between plants.",
         "Avoid taking a bahar in the rainy season in blight-prone areas; choose the bahar your local research station advises.",
         "Plant only healthy, disease-free nursery plants.",
         "Watch for oily, water-soaked spots on leaves and fruit, and act early on expert advice."])],
  faq=[("What is telya in pomegranate?", "Telya is bacterial blight. It shows as oily, dark spots on leaves, stems and fruit, and spreads fast in warm, humid weather."),
       ("Which bahar is best for pomegranate?", "It depends on your area's rainfall and disease pressure. Many growers in blight-prone areas avoid the monsoon bahar; ask your local research station.")],
  sources=[("ICAR-National Research Centre on Pomegranate, Solapur", "https://nrcpomegranate.icar.gov.in/")]),

"/crops/coconut": dict(
  hook="The coconut you harvest today was decided more than three years ago. A coconut flower bunch starts forming inside the palm long before it opens, and the nut then takes about a year to mature. That is why feeding a palm only when yield falls never seems to work.",
  stats=[("~1 a month", "new leaf and flower bunch on a healthy palm"), ("~12 months", "from flower opening to mature nut"), ("3+ years", "from bunch formation to harvest")],
  add=[("Feeding for the long cycle", [
         "Feed every year, split over the monsoon and post-monsoon, not just once.",
         "Apply in a circular basin around the palm, where feeder roots are, not against the trunk.",
         "Potash matters a lot in coconut: low potash shows as yellowing older fronds and small nuts.",
         "Mulch the basin with husks or fronds to hold moisture in summer.",
         "Coconut is long-term: expect improvements in yield over seasons, not weeks."]),
       ("Pests to check every few months", [
         "Rhinoceros beetle: V-shaped cuts in fronds and holes at the crown.",
         "Red palm weevil: oozing brown liquid and holes on the trunk, a wilting crown. Act fast; it kills palms.",
         "Eriophyid mite: brown, cracked, scarred nuts.",
         "Keep the crown clean and remove dead palms and rotting material where beetles breed."])],
  faq=[("How long until coconut yield improves after better care?", "Because a nut takes more than three years from bunch formation to harvest, steady care usually shows over two to three years, though nut drop can reduce sooner."),
       ("Where should fertilizer go for a coconut palm?", "In a basin about 1.5 to 2 metres from the trunk, where feeder roots are, mixed into the soil and followed by water.")],
  sources=[("ICAR-Central Plantation Crops Research Institute, Kasaragod", "https://cpcri.icar.gov.in/")]),

"/crops/groundnut": dict(
  hook="Gujarat grows more groundnut than any other state. Yet many Saurashtra farmers break open pods at harvest and find them empty. The reason is surprising: groundnut pods take calcium straight from the soil around them, not through the roots, so a plant can look healthy above ground while its pods starve.",
  add=[("Why pods stay empty", [
         ("html", "<p>After flowering, the groundnut plant pushes a peg into the soil, and the pod forms at its tip. The developing pod absorbs calcium directly from the soil water around it. If the top few inches of soil are low in calcium, dry, or hard, pods form but do not fill: you get pops (empty pods) and shrivelled kernels. That is why gypsum is applied to the pegging zone in many areas, and why moisture at pod filling matters so much.</p>")]),
       ("Season checklist", [
         "Sow Rhizobium-treated seed for better nodules.",
         "Keep the soil loose at flowering so pegs can enter easily; avoid deep hoeing that damages pegs after pegging starts.",
         "Apply gypsum in the pegging zone where your agriculture office advises.",
         "Avoid water stress at pegging and pod filling.",
         "Pale yellow young leaves on alkaline soil often mean iron shortage; get it checked.",
         "Harvest when most pods show dark veins inside the shell."])],
  faq=[("Why are groundnut pods empty at harvest?", "Usually calcium shortage in the pod zone, water stress at pod filling, or hard soil at pegging. Gypsum and steady moisture help in many fields."),
       ("Why are young groundnut leaves pale yellow?", "On alkaline, calcareous soils this is often iron deficiency. Older leaves turning yellow points more to nitrogen or weak nodules.")],
  sources=[("ICAR-Directorate of Groundnut Research, Junagadh", "https://dgr.icar.gov.in/")]),

"/crops": dict(
  hook="Most crop losses are not caused by one big disaster. They come from small problems noticed late: a dry week at flowering, a hungry tree after harvest, a hidden zinc shortage. Each guide below is built to help you notice early.",
  add=[("How to use these crop guides", [
         "Start with your crop's stage-by-stage section and find where your crop is today.",
         "Check the 'What to check first' list before buying any product.",
         "Read the linked crop-problem pages if you see a specific symptom.",
         "Get a soil and water test once every two to three years; most of our advice depends on it.",
         "Send us a photo on WhatsApp if you are unsure; our team will tell you what to check."])]),

"/crops/fruits": dict(
  hook="An orchard is a ten to forty year investment, and almost every fruit tree decides next year's crop in the months after this year's harvest. Growers who stop caring for the tree once the fruit is sold usually see it in the next season.",
  add=[("Four habits shared by productive orchards", [
         "Feed and prune after harvest, when the tree builds the shoots that will flower next.",
         "Keep basins and drainage right: wet roots and collar rot kill more fruit trees than any pest.",
         "Water lightly and steadily at fruit set and growth; sudden swings cause drop and cracking.",
         "Keep records per tree or per block, so you can see alternate bearing and weak patches."])]),

"/crops/vegetables": dict(
  hook="Vegetables are the fastest money on a farm, and the fastest way to lose it. A short crop leaves no time to recover: one missed week of pest control or water in a 90-day crop can decide the season.",
  add=[("What separates good vegetable growers", [
         "Healthy nursery seedlings raised under insect-proof net.",
         "Weekly field walks, turning leaves to look for pests early.",
         "Small, regular feeding instead of one big dose.",
         "Steady drip or light irrigation, especially at flowering and fruiting.",
         "Rotation between vegetable families so soil diseases do not build up."])]),

"/crop-problems": dict(
  hook="When a crop looks sick, the first instinct is to spray. But many problems farmers bring us, such as fruit drop, small tubers, dieback and poor germination, start in the soil, the roots or the weather, where no spray reaches. Finding the real cause first saves money.",
  add=[("Before you spray, check these five things", [
         "Is the soil too dry, too wet or hard? Dig a hand-deep hole and look.",
         "Are the roots white and firm, or brown and soft?",
         "Are insects present? Turn leaves and shake flowers over a white cloth.",
         "What was the weather in the last week: heat, cold, fog, heavy rain?",
         "Is it the whole field or patches? Patches point to soil, drainage or disease spots."])]),
})

# ---------------- Batch 3: trust and buying pages
VAJ = ("Vajiram & Ravi, Biostimulants under central scrutiny for plant growth claims (July 2025)", "https://vajiramias.com/article/biostimulants-under-central-scrutiny-for-plant-growth-claims/68806dda4f1b743ecd684797")
DEEP.update({
"/quality": dict(
  hook="For years, nearly 30,000 biostimulant products were sold in India without proper checks. After the rules were tightened, only about 650 were still on the market by July 2025. If a product cannot tell you its Schedule VI grade, it may be one of the ones that should not be sold.",
  stats=[("~30,000", "biostimulant products once sold without checks"), ("~650", "still in the market by July 2025"), ("2021", "the year biostimulants came under the Fertiliser Control Order")],
  add=[("Five checks before you buy any biostimulant", [
         "Ask for the Schedule VI grade name, exactly as it is written in the Fertiliser Control Order.",
         "Check the label for the manufacturer's name and address, batch number, and manufacturing and expiry dates.",
         "Ask for proof of the approval or certificate behind the product.",
         "Be careful with labels that promise a fixed yield increase or say the product 'cures' disease.",
         "Buy from a seller who will still answer your call after the sale."]),
       ("What happens to every batch at our factory", [
         "Raw materials are checked when they arrive, before they go into production.",
         "Each batch is made to the grade's specification and given its own batch number.",
         "Samples from every batch are checked in-house before filling.",
         "Bulk buyers can ask for third-party testing of their lot."])],
  faq=[("How do I know a biostimulant is legal in India?", "It must match a grade listed in Schedule VI of the Fertiliser Control Order, and the label must show the grade, manufacturer, batch number and dates. Ask the seller for the approval behind it."),
       ("Can I get a test report for my batch?", "Bulk buyers can ask for third-party testing of their lot. Farmers can ask us about the batch number printed on their pack.")],
  sources=[VAJ]),

"/factory-and-rd": dict(
  hook="When you buy a biostimulant, ask one simple question: who actually made it? Many products are made by one company and sold under another name. Every Immunity product is made in our own factory in Shihor, Bhavnagar, by the same team that visits farms.",
  stats=[("100 KL", "liquid production capacity per month"), ("2,500 t", "solid and granule capacity per month"), ("since 2006", "working with farmers")],
  add=[("From field problem to finished product", [
         "<strong>The field:</strong> a problem farmers keep bringing us, such as sugarcane gaps, apple tree losses or small potatoes.",
         "<strong>The formula:</strong> our team works out which approved grades and nutrients address it.",
         "<strong>Field trials:</strong> the formula is tried on growers' farms across seasons before it is sold.",
         "<strong>Production:</strong> made in batches at our Shihor plant, with gentle extraction that avoids harsh chemicals, very high pH and heat.",
         "<strong>Checks and dispatch:</strong> every batch is checked, packed with its batch number and dispatched across India and abroad."]),
       ("Why gentle extraction matters", [
         ("html", "<p>Seaweed, humic and amino acid extracts carry natural compounds that can break down under very strong alkali, acid or high heat. Harsh processing is faster and cheaper, but it can leave a dark liquid with less of what the plant actually responds to. We extract without harsh chemicals, very high pH or heat, which takes longer but keeps more of the raw material's value.</p>")])],
  faq=[("Where is your factory?", "Plot No. 321, GIDC 2, Ghanghali Road, Shihor, Bhavnagar, Gujarat 364240."),
       ("Can bulk buyers visit the factory?", "Bulk, OEM and dealer partners can ask to visit; contact us to arrange a time.")]),

"/our-story": dict(
  hook="Most fertilizer companies start with a product and look for farmers to sell it to. We started the other way round, in 2006, in farmers' fields around Bhavnagar, with problems no product on the shelf was solving.",
  add=[("What nearly 20 years on farms taught us", [
         "<strong>The soil is usually the real problem.</strong> Most yield falls we see trace back to tired soil, salty water or weak roots, not a missing spray.",
         "<strong>Farmers trust what they see.</strong> That is why we work through field visits, demonstrations and other farmers' own words.",
         "<strong>Honesty sells longer than promises.</strong> We never promise a yield; we share what growers report and what to check first.",
         "<strong>One crop, one formula.</strong> A mango tree and a sugarcane field do not need the same thing, so the Immunity range is built crop by crop.",
         "<strong>Answer the phone after the sale.</strong> Our team stays on WhatsApp and phone through the season."]),
       ("Where we are going", [
         ("html", "<p>Today the Immunity range covers 20 crops, with 36 biostimulant grades and 11 biofertilizer types under Gujarat NOCs, made at our own factory in Shihor. The next step is the same as the first: more time in farmers' fields, more crop guides in Hindi and Gujarati, and more growers telling their own stories.</p>")])]),

"/where-to-buy": dict(
  hook="Fake and unapproved farm inputs are a real problem in rural India, and the farmer pays twice: once for the bottle, and again in the lost crop. Buying Immunity from a known dealer or directly from us is the simplest protection.",
  add=[("How ordering works", [
         "<strong>Step 1:</strong> send your village, district, crop and the problem on WhatsApp, or call.",
         "<strong>Step 2:</strong> our team suggests the right product and pack size for your crop and area.",
         "<strong>Step 3:</strong> we connect you to the nearest dealer, or supply direct by courier or transport where there is no dealer.",
         "<strong>Step 4:</strong> after delivery, our team stays available on WhatsApp to answer questions through the season."]),
       ("How to check that your pack is genuine", [
         "Look for Gujarat Bio Organics Pvt. Ltd. and our Shihor, Bhavnagar factory address on the label.",
         "Check the batch number and the manufacturing and expiry dates.",
         "Check that the seal is intact.",
         "If anything looks wrong, send us a photo of the label on WhatsApp before using it."])],
  faq=[("Do you deliver to villages?", "Yes. Where there is no dealer near you, we deliver across India by courier or transport."),
       ("Can I become the dealer for my area?", "Yes. See the dealer page or send us an enquiry with your shop and district.")],
  sources=[("Krishi Jagran, strict action on uncertified biostimulants and spurious inputs (2025)", "https://krishijagran.com/news/strict-action-initiated-on-uncertified-bio-stimulants-spurious-fertilizers-seeds-and-pesticides-shivraj-singh-chouhan")]),

"/bulk-buyers": dict(
  hook="For an FPO, plantation or sugar factory, the real cost of a farm input is not the price per litre. It is the cost of a product that does not work across hundreds of acres, or arrives late in the season. Buying direct from the maker removes most of that risk.",
  add=[("How a bulk programme works", [
         "<strong>Share your crop, acreage and problem:</strong> what you grow, where, and what is holding yields back.",
         "<strong>We propose a programme:</strong> which products, at which crop stages, and in which pack sizes.",
         "<strong>Trial first if you wish:</strong> many buyers start with a block or a group of growers before scaling up.",
         "<strong>Supply and support:</strong> factory dispatch, crop leaflets for your growers, and field visits where needed."]),
       ("What to prepare for a quick quote", [
         "Crop and approximate acreage or number of growers.",
         "District and state for dispatch.",
         "Preferred pack sizes.",
         "When in the season you need the material.",
         "Any testing or documentation your organisation needs."])],
  faq=[("Do you supply FPOs and sugar factories?", "Yes. We supply farmer producer organisations, cooperatives, sugar factories for their growers, plantations and institutional buyers."),
       ("Can we get our own crop programme?", "Yes. Tell us your crop, area and the problem; we suggest products, stages and pack sizes, and support your field team.")]),

"/oem-private-label": dict(
  hook="Building a biostimulant brand in India is now harder than it looks: since the rules were tightened, products must match an approved Schedule VI grade, and most of the products once on the market have gone. A manufacturer with approved grades is the fastest legal route to your own label.",
  add=[("From enquiry to your branded product", [
         "<strong>1. Choose grades:</strong> pick from our 36 Schedule VI biostimulant grades and 11 biofertilizer types, in liquid, powder or granule.",
         "<strong>2. Specification and samples:</strong> we share specifications and samples for your evaluation.",
         "<strong>3. Packaging and label:</strong> your brand, our manufacturing details as required by the rules, packs from 250 mL bottles to 1000 L IBC tanks.",
         "<strong>4. Production and checks:</strong> batch production with in-house checks and batch numbers.",
         "<strong>5. Dispatch:</strong> across India, or export by sea from Indian ports."]),
       ("Questions to ask any OEM manufacturer", [
         "Which Schedule VI grades are you approved for, and can I see the certificates?",
         "Do you make the product yourselves, or buy it in?",
         "How do you keep batches consistent?",
         "What happens if a batch has a problem?",
         "Can you support my sales team with crop information?"])],
  faq=[("Can you make products under our brand?", "Yes. We formulate, manufacture, fill and label under your brand, from approved grades."),
       ("Do you export private-label products?", "Yes. We export by sea from Indian ports; full terms are on our business site.")],
  sources=[VAJ]),

"/dealers": dict(
  hook="A dealer's reputation in the village is only as good as the last product he sold. A product that does not work, or a supplier who disappears after the sale, costs a dealer customers for years. That is why we support dealers in the field, not just at billing.",
  add=[("How to become an Immunity dealer", [
         "<strong>1.</strong> Send an enquiry with your shop name, district and the crops grown around you.",
         "<strong>2.</strong> Our team calls you to discuss the range, pack sizes, prices and margins.",
         "<strong>3.</strong> Start with the products for your area's main crops.",
         "<strong>4.</strong> We support you with posters, leaflets, farmer meetings and demonstration plots."])],
  faq=[("Do I need a licence to sell biostimulants?", "Fertilizer and biostimulant sellers usually need the dealer authorisation required by their state. Check with your district agriculture office; we can guide you on documents."),
       ("Is there a minimum order for dealers?", "Terms are shared when you enquire, based on your area and the products you choose.")]),

"/farmer-stories": dict(
  hook="Farmers trust other farmers more than any advertisement, and they are right to. That is why every story here is told in the grower's own words, with their name and place, and why we never turn their results into a promise.",
  add=[("How to read these stories", [
         "Each story is one grower's experience on their own farm, in their own season.",
         "Soil, water, weather, variety and care all change results; your result can be different.",
         "Look at what the grower changed, not just the result: often it is the timing, the water or the soil care that made the difference.",
         "If a story sounds like your problem, send us your crop photos and we will tell you what to check first."]),
       ("Share your own story", [
         "Send a short video or photos on WhatsApp: your crop before, during and after the season.",
         "Tell us your crop, village and what you changed.",
         "With your permission, we share it here and on our other pages, with your name and place."])])
})
