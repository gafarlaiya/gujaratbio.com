# Crop problem pages and farming guides. Plain language, no doses, no promises.
PROBLEMS = [
 dict(slug="apple-root-rot", crop="apple", title="Apple Root Rot: Causes, Signs and What to Do",
      h1="Apple root rot: causes, signs and what to do",
      desc="Why apple trees get root and collar rot, how to recognise it early, and the orchard practices that lower the risk. For growers in Himachal Pradesh and Jammu and Kashmir.",
      answer="Apple root rot is caused by soil fungi that attack roots in wet, poorly drained soil. Trees show weak growth, yellow leaves and small fruit, then die over one or two seasons. Better drainage, healthy soil and early action lower the losses.",
      sections=[("What you see", ["Leaves turn pale or yellow and fall early.", "New shoots are short; the tree looks tired.", "Fruit is small and colours poorly.", "Bark at the collar (soil level) is dark, soft or cracked.", "Roots are brown and soft instead of white and firm."]),
                ("Why it happens", ["Water standing around the trunk after rain or irrigation.", "Heavy soil with little air.", "Old orchard soil with few helpful soil organisms left.", "Wounds on roots and collar from tools or pests.", "Trees already weak from heavy cropping or stress."]),
                ("What growers can do", ["Make sure water drains away from trunks; open drains in low spots.", "Keep the collar clear of soil, mulch and weeds.", "Avoid wounding roots and the collar.", "Build soil organic matter so helpful organisms return.", "Get badly affected trees checked by an expert; follow their advice on treatment.", "Remove dead trees and roots before replanting."])],
      faq=[("Can a tree with root rot recover?", "Trees caught early, with part of the root system still healthy, can recover if drainage and soil are fixed. Trees with most roots gone rarely do."),
           ("Is root rot the same as collar rot?", "They are related. Collar rot attacks the trunk at soil level, root rot attacks the roots. Both are favoured by wet soil."),
           ("Where does Immunity Apple Special fit?", "It supports roots and soil life as part of orchard care. It is not a fungicide; disease control follows an expert's advice.")]),
 dict(slug="mango-fruit-drop", crop="mango", title="Mango Fruit Drop: Why It Happens and How to Reduce It",
      h1="Mango flower and fruit drop: why it happens",
      desc="Why mango trees drop flowers and young fruit, which drop is natural, and the orchard care that reduces heavy losses.",
      answer="Some fruit drop in mango is natural: a tree sets far more fruit than it can carry. Heavy drop follows stress, such as dry soil, hot winds, pests like hoppers, or a tree low on stored food. Steady water and nutrition through fruit set reduce it.",
      sections=[("Natural drop and problem drop", ["A mango panicle carries hundreds of flowers but keeps only a few fruits; most of the drop in the first weeks is normal.", "Problem drop is when most young fruit falls, or fruit keeps falling at marble size and later."]),
                ("Common causes", ["Dry soil during fruit set and growth.", "Hot, dry winds.", "Hoppers, mealybugs and other pests on the panicles.", "Poor pollination in cloudy or rainy weather.", "A tree weak from a heavy crop last year."]),
                ("What growers can do", ["Keep soil moisture steady from fruit set onward; avoid sudden heavy watering after a dry spell.", "Watch panicles for hoppers and act early.", "Feed the tree after harvest so it has reserves for next season.", "Mulch the basin to hold moisture."])],
      faq=[("When should I water mango trees during fruiting?", "Once fruit has set, light and regular watering is better than none or very heavy watering. Your local horticulture office can advise for your soil."),
           ("Does alternate bearing cause fruit drop?", "In the off year the tree has fewer reserves, so it holds less fruit. Good care after harvest helps both problems.")]),
 dict(slug="mango-alternate-bearing", crop="mango", title="Mango Alternate Bearing: Why Trees Fruit Every Other Year",
      h1="Mango alternate bearing: why trees fruit every other year",
      desc="Why mango trees give a heavy crop one year and a poor crop the next, and the orchard care that evens out bearing.",
      answer="A mango tree that carries a heavy crop uses up its stored food and makes little new growth, so it flowers poorly the next year. Feeding after harvest, timely pruning and steady nutrition help the tree make new shoots every year.",
      sections=[("How the cycle works", ["Fruit grows on shoots that matured in the season before.", "A heavy crop takes the food that would have built new shoots.", "Few mature shoots means few flowers next year, and the cycle repeats."]),
                ("What growers can do", ["Harvest on time and prune soon after harvest to start new growth.", "Feed the tree after harvest, when it is building next year's shoots.", "Thin very heavy crops on young trees.", "Keep records of each tree's yield to see the pattern."])],
      faq=[("Are some mango varieties more prone to alternate bearing?", "Yes. Many traditional varieties bear alternately more than some newer ones."),
           ("Can alternate bearing be stopped completely?", "It can be reduced, not always removed. Good care over several seasons evens out the crop.")]),
 dict(slug="sugarcane-poor-germination", crop="sugarcane", title="Sugarcane Poor Germination and Gaps: Causes and Fixes",
      h1="Sugarcane poor germination and gaps",
      desc="Why sugarcane setts fail to germinate, why young plants die, and what growers can do at planting to get an even stand.",
      answer="Poor sugarcane germination usually comes from old or damaged setts, soil that is too dry, too wet or too hard at planting, and sett rot. Tired soil with little organic matter makes every one of these worse.",
      sections=[("Common causes", ["Setts from an old or diseased crop.", "Buds damaged while cutting or transporting.", "Dry soil, or waterlogged soil, at planting.", "Hard soil with little air for new roots.", "Sett rot and termites.", "Planting too deep."]),
                ("What growers can do", ["Use fresh setts from a healthy nursery crop.", "Plant into moist, well-prepared soil.", "Treat setts as advised by your sugar factory or agriculture office.", "Fill gaps early, within the first weeks.", "Build organic matter in the soil over seasons."])],
      faq=[("How long does sugarcane take to germinate?", "Buds usually start within one to three weeks; germination continues for about six weeks depending on soil and weather."),
           ("What is a good germination rate?", "Ask your sugar factory for the local benchmark; poor fields show clear gaps along the row.")]),
 dict(slug="potato-small-tubers", crop="potato", title="Small Potato Tubers and Fewer Tubers: Causes",
      h1="Why potatoes are small, or too few",
      desc="Why potato plants set few tubers or produce small, uneven tubers, and the crop stages when growers can act to prevent it.",
      answer="The number of potato tubers is decided at tuber initiation, around six to eight weeks after planting; their size is decided during bulking. Stress at either stage, from water, heat, weak roots or nutrient shortage, means fewer or smaller potatoes.",
      sections=[("Fewer tubers", ["Stress at tuber initiation.", "Poor or old seed tubers.", "Weak root systems in hard or salty soil."]),
                ("Small tubers", ["Dry spells or heat during bulking.", "Too many tubers on a weak plant.", "Shortage of potash and other nutrients late in the crop.", "Early leaf loss from blight or other disease."]),
                ("What growers can do", ["Use healthy seed of the right size.", "Test soil before planting and correct problems.", "Keep water steady at tuber initiation and bulking.", "Protect leaves; they feed the tubers."])],
      faq=[("Does more urea give bigger potatoes?", "Too much nitrogen gives a big leafy plant and can delay tubers. Balanced nutrition works better than more of one fertilizer.")]),
 dict(slug="citrus-dieback", crop="citrus", title="Citrus Dieback: Causes and Care for Lemon and Orange Trees",
      h1="Citrus dieback: why branches dry from the tip",
      desc="Why lemon, lime and orange branches dry from the tip back, the common causes, and how growers can save declining trees.",
      answer="Citrus dieback, where branches dry from the tip back, has several causes: root rot from poor drainage, nutrient shortages such as zinc, pests and old age. Fixing the root zone and nutrition comes before pruning dry branches.",
      sections=[("Common causes", ["Root rot and gummosis in wet soil.", "Zinc, iron and other micronutrient shortage, especially in alkaline soil.", "Pests such as bark borers.", "Old, neglected trees."]),
                ("What growers can do", ["Improve drainage; keep water off the trunk.", "Test soil and leaves for nutrient shortage.", "Prune dead wood back to healthy tissue.", "Feed the tree and build soil organic matter."])],
      faq=[("Should I cut the dry branches?", "Yes, prune back to healthy wood, but also find the cause, or the dieback will return.")]),
]

GUIDES = [
 dict(slug="gravitropism-and-root-growth", title="Gravitropism and Roots: How Biostimulants Support Root Growth",
      h1="Gravitropism and root growth: how roots find their way, and how biostimulants can help",
      desc="How roots sense gravity, what goes wrong when roots are weak, and how seaweed, amino acid and humic biostimulants can support root growth.",
      answer="Roots grow downward because of gravitropism: cells in the root tip sense gravity and shift the plant hormone auxin, so the root bends toward the soil. Biostimulants do not switch this on. Selected seaweed, amino acid and humic products can support root growth, nutrient uptake and stress tolerance, but only after you find out why the roots are weak.",
      sections=[
       ("Weak roots are usually a soil or stress problem first", [
         "Hard or compacted soil that roots cannot push through.",
         "Waterlogging that leaves roots without oxygen.",
         "Salty soil or salty irrigation water that burns root tips.",
         "Low organic matter, so the soil holds little water and few nutrients.",
         "Transplanting shock, when roots are damaged or dry out at planting.",
         "Nutrient imbalance, such as too much nitrogen and too little phosphorus or potash.",
         "Root diseases and nematodes."]),
       ("How to check the roots in your own field", [
         "Pick three or four plants that look weak and three or four that look healthy. Dig them up with a spade; do not pull them.",
         "Healthy roots are mostly pale or white at the tips, with plenty of fine root hairs. Brown, black, slimy or stunted roots point to waterlogging, disease or salt.",
         "Look for roots that turn sideways or stop at a hard layer. That points to compaction.",
         "Compare the depth: weak plants usually have a shallow, short root system.",
         "Take a soil sample and test for salinity (EC), pH and nutrients before spending money on any product. See <a href=\"/guides/how-to-take-a-soil-sample\">how to take a soil sample</a>."]),
       ("What gravitropism is, in simple words", [
         ("html", "<p>Plants have no eyes or muscles, yet a root knows which way is down. Cells in the root tip contain small starch-filled grains called amyloplasts. They settle to the lower side of the cell, and that tells the plant which way gravity points.</p>"
                  "<p>The signal changes how the growth hormone auxin is spread. In a root, more auxin on the lower side slows growth there, so the root bends downward. In a shoot, more auxin on the lower side speeds growth there, so the shoot bends upward. That is why a seed sown at any angle still sends its root down and its shoot up.</p>"
                  "<p>Side roots grow at an angle, not straight down, so the plant can search a wider volume of soil. Gravity is also not the only cue. Roots respond to water, oxygen and nutrient-rich patches as well, which is why moisture and soil condition shape the root system as much as gravity does.</p>")]),
       ("Gravitropism in the first three crop stages", [
         ("html", "__IMG__")]),
       ("What roots need at each crop stage", [
         ("html", '<div class="tablewrap"><table class="packs"><thead><tr><th>Stage</th><th>What the roots are doing</th><th>What can go wrong</th><th>What growers can check</th></tr></thead><tbody>'
                  '<tr><td>Germination</td><td>The first root (radicle) pushes down for water and anchorage</td><td>Crust, dry soil, poor seed or cold soil</td><td>Seed quality, moisture, depth of sowing</td></tr>'
                  '<tr><td>Seedling</td><td>The main root and side roots begin to branch</td><td>Transplanting shock, salt, compaction</td><td>Handling at transplant, irrigation water quality</td></tr>'
                  '<tr><td>Vegetative growth</td><td>Roots explore deeper layers for water and nutrients</td><td>Shallow roots, waterlogging, nutrient imbalance</td><td>Root depth, drainage, soil test</td></tr>'
                  '<tr><td>Flowering and fruiting</td><td>Roots must keep supplying a high demand for water and nutrients</td><td>Heat and moisture stress, root damage</td><td>Steady irrigation, root health, nutrient supply</td></tr>'
                  '<tr><td>Grain or fruit fill</td><td>Roots stay active to support filling</td><td>Early root decline, stress</td><td>Water supply and plant health late in the crop</td></tr>'
                  '</tbody></table></div>')]),
       ("What biostimulants can and cannot do", [
         ("html", "<p>A biostimulant is not a fertilizer and not a pesticide. It helps the plant use nutrients better and cope with stress. It does not replace gravity sensing, and it does not fix a hard, salty or waterlogged soil by itself. Effects depend on the active ingredient, the formulation, the crop, the soil and the weather.</p>")]),
       ("The main types and what they are used for", [
         "Seaweed extracts: contain a mixture of natural plant-growth substances. They are used to support root and shoot growth and to help crops handle stress.",
         "Amino acids and protein hydrolysates: building blocks that support plant metabolism, and are used to help crops recover from stress and take up nutrients.",
         "Humic and fulvic acid: work through the soil. They are used to support root growth and to help roots reach nutrients. See <a href=\"/guides/compost-and-humic-acid\">compost and humic acid</a>.",
         "Microbial products: beneficial microorganisms that live around the roots and can help release nutrients."]),
       ("Match the problem to the approach", [
         ("html", '<div class="tablewrap"><table class="packs"><thead><tr><th>Problem in the field</th><th>Check first</th><th>Approach that may help</th></tr></thead><tbody>'
                  '<tr><td>Poor root growth</td><td>Compaction, drainage, soil test</td><td>Fix soil first; seaweed or amino acid products to support roots</td></tr>'
                  '<tr><td>Transplanting shock</td><td>Root damage, watering after transplant</td><td>Careful handling plus a stress-support product at transplant</td></tr>'
                  '<tr><td>Salinity</td><td>Soil and water EC</td><td>Better water and drainage first; products evaluated for stress tolerance can support</td></tr>'
                  '<tr><td>Poor use of fertilizer</td><td>Soil test, balance of nutrients</td><td>Balanced nutrition; humic substances and suitable microbial products can support uptake</td></tr>'
                  '<tr><td>Uneven crop establishment</td><td>Seed, sowing depth, moisture</td><td>Good seed and moisture; early-stage applications can support even growth</td></tr>'
                  '<tr><td>Heat or moisture stress</td><td>Irrigation schedule, mulch</td><td>Crop-specific stress management at sensitive stages</td></tr>'
                  '</tbody></table></div><p class="note">No single product solves every problem. Start with the cause, then choose the product.</p>')]),
       ("How to choose and use a biostimulant", [
         "In India, only biostimulants listed in Schedule VI of the Fertiliser Control Order can be sold. Ask your supplier for proof.",
         "Pick the product for the problem and the crop stage, not for the name on the pack.",
         "Keep balanced fertilizer and soil care going. A biostimulant works alongside nutrition, not instead of it.",
         "Test on a small strip first and leave a strip untreated. Compare roots and plants after two to three weeks.",
         "Follow the label for dose and timing, and check that the product mixes with what you spray.",
         "Write down what you applied and when, so you can judge the result honestly."]),
       ("From more inputs to better processes", [
         ("html", "<p>Farming has long asked only how much fertilizer to apply. A better question is whether the roots can use what is already in the soil. Is the root system growing well? Is the plant under salt or water stress? Is the soil alive and rich in organic matter? Biostimulants have a place in this thinking, when they are properly formulated, matched to the problem and tested in the field.</p>")]),
       ("How we work with farmers at Gujarat Bio Organics", [
         "Understand the plant: what the crop needs at each stage.",
         "Understand the soil: what limits the roots and nutrient uptake.",
         "Choose the right solution: a suitable product, tested in the field, with an honest expectation of results.",
         ("html", '<p>Tell us your crop, stage and what you see in the roots, and we will suggest a programme. <a href="/enquiry">Send an enquiry</a> or see <a href="/products">the Immunity range</a>.</p>')])],
      faq=[("What is gravitropism in simple words?", "It is the way plants sense gravity and grow accordingly: roots grow down and shoots grow up."),
           ("Do biostimulants make roots grow downward?", "No. Gravity decides the direction. Biostimulants may support the growth, nutrient uptake and stress tolerance of the roots, depending on the product, crop and soil."),
           ("Which biostimulant is best for root development?", "It depends on the cause. Seaweed extracts, amino acids and humic substances are commonly used to support roots, but check soil, drainage and salinity first."),
           ("How can I tell if my crop has a root problem?", "Dig up a few weak plants and a few healthy ones and compare the roots. Short, brown, slimy or shallow roots, or roots that stop at a hard layer, show a problem."),
           ("Can biostimulants replace fertilizer?", "No. They help the crop use nutrients better, but the crop still needs balanced nutrition."),
           ("How do I know a biostimulant can be sold in India?", "Only products listed in Schedule VI of the Fertiliser Control Order are allowed. Ask the supplier for proof of listing.")]),
 dict(slug="what-are-biostimulants", title="What Are Biostimulants? A Plain Guide for Farmers",
      h1="What are biostimulants? A plain guide for farmers",
      desc="What biostimulants are, how they differ from fertilizers and pesticides, the main types, and how farmers use them.",
      answer="A biostimulant helps a plant use nutrients better and cope with stress such as heat, drought or salty soil. It is not a fertilizer and not a pesticide. Common types are humic acid, seaweed extract, amino acids and botanical extracts.",
      sections=[("How a biostimulant differs", ["A fertilizer supplies nutrients such as nitrogen, phosphorus and potash.", "A pesticide kills or controls pests and diseases.", "A biostimulant helps the plant and the soil work better, so the plant uses nutrients well and handles stress."]),
                ("The main types", ["Humic and fulvic acid: improve soil structure and help roots take up nutrients.", "Seaweed extract: natural growth substances that support roots, flowering and stress tolerance.", "Amino acids and protein hydrolysates: building blocks that help plants recover from stress.", "Botanical extracts: plant-based materials with specific effects."]),
                ("Are biostimulants regulated in India?", ["Yes. Since June 2025 only biostimulants listed in Schedule VI of the Fertiliser Control Order can be sold in India. Ask your supplier for proof that a product is listed."]),
                ("How farmers use them", ["Biostimulants work alongside balanced nutrition, not instead of it.", "They are applied to the soil, through drip, or as a spray, at the stages where stress is likely.", "Results depend on crop, soil, weather and how the crop is managed."])],
      faq=[("Can biostimulants replace fertilizers?", "No. They help the crop use fertilizers better, so many growers can use fertilizers more efficiently, but the crop still needs nutrients."),
           ("Is a biostimulant organic?", "Many are made from natural materials such as seaweed, humus or plant protein, but check the label and certification.")]),
 dict(slug="why-yields-fall-on-old-land", title="Why Yields Fall on Old Farm Land, and How to Rebuild Soil",
      h1="Why yields fall on old land, and how to rebuild the soil",
      desc="Why the same land gives less every year even with more fertilizer, what tired soil looks like, and practical steps to rebuild soil health.",
      answer="When the same land is farmed hard for years with mostly chemical fertilizer, organic matter falls, soil life declines and the soil turns hard. Roots then struggle, and the crop uses fertilizer poorly. Adding organic matter and protecting soil life rebuilds it over seasons.",
      sections=[("Signs of tired soil", ["You need more fertilizer every year for the same yield.", "The soil is hard, cracks when dry and stays wet after rain.", "Few earthworms.", "Roots are short and shallow.", "A soil test shows low organic carbon."]),
                ("Why it happens", ["Crop residues are burned or removed, so little organic matter goes back.", "The same crop is grown year after year.", "Heavy tillage breaks soil structure.", "Salts build up from fertilizer and poor water."]),
                ("How to rebuild it", ["Return organic matter: compost, farmyard manure, crop residues and green manure.", "Rotate crops; include a legume where you can.", "Keep the soil covered with mulch or a crop.", "Use balanced fertilizer based on a soil test, not habit.", "Support soil life with organic inputs and biostimulants such as humic acid."])],
      faq=[("How long does it take to rebuild soil?", "Changes in structure and soil life start within one or two seasons; organic carbon builds slowly over several years."),
           ("What does organic carbon in a soil test mean?", "It measures organic matter in the soil. Low organic carbon usually means tired soil.")]),
 dict(slug="compost-and-humic-acid", title="Compost and Humic Acid: Why They Work Better Together",
      h1="Compost and humic acid: why they work better together",
      desc="How compost and humic acid each improve soil, why using them together helps, and how to make good compost on the farm.",
      answer="Compost feeds the soil with organic matter and living organisms. Humic acid improves soil structure and helps roots hold and take up nutrients. Together they help the soil keep water and nutrients near the roots, so fertilizer is not wasted.",
      sections=[("What compost does", ["Adds organic matter and nutrients slowly.", "Brings helpful microbes into the soil.", "Helps sandy soil hold water and heavy soil drain."]),
                ("What humic acid does", ["Helps soil particles group into crumbs, so air and water move better.", "Holds nutrients so they do not wash away.", "Helps roots take up nutrients."]),
                ("Making good compost", ["Mix green material (fresh leaves, manure) with dry material (straw, dry leaves).", "Keep the heap moist, like a squeezed sponge.", "Turn it every few weeks for air.", "It is ready when it is dark, crumbly and smells of earth."])],
      faq=[("Can I use humic acid without compost?", "Yes, but it works best in soil that also gets organic matter."),
           ("Is raw manure the same as compost?", "No. Raw manure can burn roots and spread weeds and disease; composting makes it safe and stable.")]),
 dict(slug="how-to-take-a-soil-sample", title="How to Take a Soil Sample for Testing: Step by Step",
      h1="How to take a soil sample for testing",
      desc="A step-by-step guide to taking a soil sample that gives an accurate soil test, and what to ask the lab to test.",
      answer="Take soil from 10 to 15 spots across the field at root depth, mix it well, and send about half a kilogram to a soil testing lab. A good sample gives an accurate test, and an accurate test tells you what your soil actually needs.",
      sections=[("Steps", ["Walk the field in a zig-zag and mark 10 to 15 spots. Avoid bunds, manure heaps, trees and wet patches.", "Scrape away surface litter.", "Dig a V-shaped hole to plough depth (about 15 cm; deeper for orchards).", "Take a thin slice from the side of the hole.", "Mix all slices in a clean bucket.", "Spread, remove stones and roots, and keep about half a kilogram.", "Put it in a clean bag with your name, field, crop and date."]),
                ("What to ask the lab to test", ["pH and EC (salts).", "Organic carbon.", "Nitrogen, phosphorus and potash.", "Micronutrients such as zinc, iron and boron."]),
                ("When to sample", ["Before sowing or planting, or after harvest.", "Every two to three years for the same field.", "Separately for parts of the field that look different."])],
      faq=[("Where can I get my soil tested?", "Government soil testing labs, Krishi Vigyan Kendras and private labs test soil. The Soil Health Card scheme also offers testing."),
           ("Should I sample each field separately?", "Yes. Fields with different soil, crop history or yield should be sampled separately.")]),
]
