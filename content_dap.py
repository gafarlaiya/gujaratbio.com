# DAP shortage cluster (November 2026): five long-form guides for the rabi 2026 DAP, urea and potash crunch.
# Farmer results are the farmers' own words from our YouTube videos (transcripts checked 22 Nov 2026), never promises.
# No product doses here: doses come from the team on WhatsApp for each crop and acreage.
_TD = lambda rows, head: ('<div class="tablewrap"><table class="packs"><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
                          + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")
_WA = '<a href="https://wa.me/919978791167">WhatsApp +91 99787 91167</a>'

DAP_GUIDES = [
 dict(slug="dap-token-booking-online", date="2026-11-22",
      title="DAP Token and Booking App 2026: Book DAP and Urea Online",
      h1="DAP token and fertilizer booking app: how to book DAP and urea online in 2026",
      desc="How the new fertilizer token systems work: the FFS app, MP e-Token, Rajasthan's 48-hour token and Haryana's portal rule. Documents, steps, price rules, and what to do if your token comes too late.",
      answer="Many states now sell subsidised DAP, urea and other fertilizers only against a token linked to your Farmer ID or Aadhaar and your land record. You book on the state's app or portal, or at a CSC or e-Mitra centre, choose a sale centre and date, and collect the bags within the token's time limit after OTP or thumb verification. The printed price still applies: ₹1,350 for a 50 kg bag of DAP.",
      sections=[
       ("Why DAP now comes with a token", [
         ("html", "<p>India imports much of its DAP and the raw material to make it. In 2026 China, once a large supplier, has nearly stopped exporting DAP: its exports from January to July were down about 95% on the year before, and it shipped none at all in July. World prices have stayed high, so every bag is harder to bring in.</p>"
                  "<p>When stock is short, the queue decides who sows on time. In November 2026 farmers in Hamirpur, Uttar Pradesh waited up to 10 hours at cooperative societies and received only two bags each; in Banda, Chandauli and Prayagraj the queues and protests made the news. To stop hoarding, black marketing and fights at the counter, states are moving to tokens: the fertilizer is reserved for you against your land and crop, and you collect it on a fixed day.</p>")]),
       ("Which state uses which system", [
         ("html", _TD([
           ["Many states (rolling out)", "Framework for Fertilizer Sale (FFS), built on the Farmer Registry under AgriStack", "FFS mobile app, or the nearest CSC", "Log in with Farmer ID or Aadhaar and OTP. Your quota depends on your land and crop."],
           ["Madhya Pradesh", "e-Token for fertilizer", "The state's e-Token portal, or a CSC", "Reported: Farmer ID must be linked. Carry the token, Aadhaar and Farmer ID."],
           ["Rajasthan", "FFS pilot from 25 June 2026 in Sirohi and Rajsamand", "Mobile phone or e-Mitra centre", "The token is valid for 48 hours. Miss it and you must book again."],
           ["Haryana", "Registration on the Meri Fasal Mera Byora portal", "Meri Fasal Mera Byora portal", "Reported in rabi 2025: registration needed before buying DAP."],
           ["Bihar", "FFS app with an option for sharecroppers", "FFS app or the state DBT Agriculture portal", "Tenants and sharecroppers can apply with the owner's land details and a declaration."]],
           ["State", "System", "Where to book", "What to know"]) +
          '<p class="note">These systems change quickly and differ by district. Before you travel, confirm with your village agriculture worker, cooperative society or district agriculture office. Use only the official app or portal.</p>')]),
       ("How to book a fertilizer token, step by step", [
         ("html", "<ol><li>Get your Farmer ID made under the Farmer Registry if you do not have one. A CSC or your agriculture office can do it.</li>"
                  "<li>Install the official app named in your state, or visit a CSC or e-Mitra centre.</li>"
                  "<li>Log in with your Farmer ID or Aadhaar. An OTP comes to your Aadhaar-linked mobile.</li>"
                  "<li>Check that your land shows correctly: survey, khasra or khata number and area.</li>"
                  "<li>Choose this season's crop and the area you will sow. The app shows how many bags you can book.</li>"
                  "<li>Pick the sale centre and the date, and submit. Save the booking ID or token as a screenshot.</li>"
                  "<li>Go on that date, within the token's time limit, with Aadhaar. Verify by OTP or thumb.</li>"
                  "<li>Pay the printed price and take a bill.</li></ol>")]),
       ("Documents to keep ready", [
         "Aadhaar card, and the mobile number linked to it.",
         "Farmer ID, where your state has started the Farmer Registry.",
         "Land record: 7/12, khatauni or the state's record, with survey or khasra number and area.",
         "Tenants and sharecroppers: the lease paper or the self-declaration your state asks for.",
         "Money for the printed price, in cash or UPI as the centre accepts."]),
       ("Common problems and what to do", [
         "<strong>Token booked but no stock at the centre:</strong> ask the society when the next rake is due and book again for that date.",
         "<strong>Token expired:</strong> in Rajasthan a token lasts 48 hours. Book again.",
         "<strong>Land not showing:</strong> your land record or Farmer ID needs updating. Go to the CSC or the patwari or talati.",
         "<strong>OTP not coming:</strong> your mobile is not linked to Aadhaar, or the number has changed. Update it at an Aadhaar centre.",
         "<strong>Dealer asks more than ₹1,350 for DAP, or forces you to buy another product with it:</strong> refuse, ask for a bill, and complain to your district agriculture office."]),
       ("Beware of fake apps and fake DAP", [
         "Download only the official app, published by the government department. Do not install apps sent as links on WhatsApp.",
         "No real token system asks you to pay an advance to a person or a UPI ID.",
         "Check every bag: printed price, company name, batch number and date. Buy only with a bill.",
         "Very cheap DAP sold door to door is a warning sign."]),
       ("If your token comes too late for sowing", [
         ("html", "<p>Sowing dates do not wait for rakes. If your field is ready and the token is days away, you have three choices, and you can combine them:</p>"
                  "<ul><li><strong>Another phosphate bag:</strong> SSP or an NPK grade can give the same phosphorus. See <a href=\"/guides/dap-shortage-what-to-use-instead\">what to use instead of DAP</a>.</li>"
                  "<li><strong>Use the phosphorus already in your soil:</strong> years of DAP leave most of it locked in the field. See <a href=\"/guides/free-locked-phosphorus-in-soil\">how to free locked phosphorus</a>.</li>"
                  "<li><strong>Feed the soil and roots:</strong> farmers in Gujarat have grown cumin, sugarcane and castor without DAP using Immunity Granules, their crop's Immunity Special and Immunity Gold. See <a href=\"/guides/farming-without-dap\">farming without DAP</a> and <a href=\"/guides/organic-alternative-to-dap\">the organic alternative to DAP</a>.</li></ul>"
                  f"<p>Tell us your crop, area and sowing date on {_WA} and our team will suggest a plan for your field.</p>")])],
      faq=[("How do I book DAP online?", "Use your state's official fertilizer app or portal, or a CSC or e-Mitra centre. Log in with Farmer ID or Aadhaar and OTP, confirm your land and crop, choose a sale centre and date, and collect the bags with your token."),
           ("What is the FFS app?", "Framework for Fertilizer Sale, a system built on the Farmer Registry under AgriStack. It lets farmers book subsidised fertilizer against their land and crop and collect it with a digital token."),
           ("Is a Farmer ID needed to buy DAP?", "In states that have moved to the Farmer Registry, yes or soon. Madhya Pradesh reportedly needs it for e-Tokens. Ask your agriculture office about your state."),
           ("How long is a DAP token valid?", "It depends on the state. In Rajasthan's system a token is valid for 48 hours."),
           ("What is the price of DAP in 2026?", "The printed maximum retail price is ₹1,350 for a 50 kg bag. Do not pay more, and always take a bill."),
           ("Can a sharecropper book a DAP token?", "In Bihar's FFS app, yes, with the owner's land details and a declaration. Other states have their own rules; ask your agriculture office."),
           ("What if DAP is not available at all?", "Use SSP or an NPK grade for phosphorus, and help the crop use the phosphorus already in your soil. Many farmers grow without DAP using Immunity Granules, their crop's Special and Immunity Gold.")]),

 dict(slug="farming-without-dap", date="2026-11-22",
      title="Farming Without DAP: Farmers Who Stopped Using DAP",
      h1="Farming without DAP: what happened when these farmers stopped using it",
      desc="Farmers in Gujarat who grew cumin, sugarcane and castor without DAP, or with half their chemical fertilizer: what they used instead, what they saw in the field, and what it means for your rabi crop.",
      answer="Farmers in Gujarat have grown cumin with no DAP at all and sugarcane on half their usual chemical fertilizer, using Immunity Granules in the soil, the Immunity Special for their crop and Immunity Gold. These are their own field experiences, not a promise. The approach works best on old farms, where years of DAP have left phosphorus locked in the soil.",
      sections=[
       ("Why many farms can do without DAP for a season", [
         ("html", "<p>Only about 15 to 25% of the phosphorus in fertilizer becomes available to the crop. The rest stays in the soil, locked with calcium in alkaline soils or with iron and aluminium in acid soils. After 20 or 30 years of DAP, most old farms hold a large bank of this phosphorus.</p>"
                  "<p>So the real question is not only where to buy the next bag. It is how to get the crop's roots to the phosphorus you have already paid for. That needs a loose, living soil and a big, healthy root system. This is what the Immunity program is made for. The science is explained in <a href=\"/guides/free-locked-phosphorus-in-soil\">how to free locked phosphorus</a>.</p>")]),
       ("Bharatbhai, cumin, Lariya village, Padadhari (Rajkot): no DAP at all", [
         ("html", "<p>Bharatbhai has grown cumin for 30 to 35 years. This season he used Immunity Granules at sowing, Immunity Cumin Special through the irrigation water, and sprays of Immunity Gold with Cumin Special.</p>"
                  "<p>In front of our team and his neighbours he said he had put no DAP in the field. He gave urea only once, a small amount, and mainly to carry a fungicide. At 60 days his cumin was even and green, with more than 95% of the plants standing, and in full flower.</p>"
                  "<p>He said that in 30 to 35 years he had seen cumin like this only once: this season. He expected about 13 to 14 man per bigha (20 kg to a man). A farmer from the next village, looking at the field, estimated his own cumin at about 4 to 5 man. Bharatbhai also said his cost was lower than with full chemical fertilizer. These were his estimates at 60 days, in his own words.</p>")]),
       ("Budhabhai Patel, sugarcane: half the bags of chemical fertilizer", [
         ("html", "<p>Budhabhai planted variety 86032 on 3 September with Immunity Granules, Immunity Sugarcane Special and Immunity Gold. The plot next to his, planted two or three days apart, got 10 to 12 bags of chemical fertilizer. His got 6.</p>"
                  "<p>He counted 8 to 12 tillers per clump, and said he expected nearly all of them to reach the mill rather than die in the shade.</p>")]),
       ("Falguniben Patel, sugarcane, Nani Chovisi (Navsari): less urea, green leaves at harvest", [
         ("html", "<p>Falguniben planted 86002 in October 2025 and the mill's first cutting began on 24 October 2026. She used Immunity Granules, Immunity Sugarcane Special and Immunity Gold with our schedule, and kept urea at about 2 to 2.5 bags where farmers might otherwise use 3 or 4.</p>"
                  "<p>At cutting the leaves were still green and the canes long, and she said her cost was a little lower than in earlier years, when rising chemical prices pushed it up. She said she would recommend the products to other farmers.</p>")]),
       ("Jitendrabhai Patel, castor, Vadnagar (Mehsana): roots deep in hard soil", [
         ("html", "<p>Jitendrabhai applied Immunity Granules in pits in his 6 vigha of castor (variety Avni 11). His soil is hard, and he said the roots went deep, the plants stayed dark green, and fungus was lower than in his other castor field. He has since used the granules in tobacco and plans to use them in wheat.</p>")]),
       ("What these farms have in common", [
         "They fed the soil first, with Immunity Granules at sowing or planting.",
         "They used the Immunity Special made for their crop, through irrigation water or drip and as a spray.",
         "They sprayed Immunity Gold for vigour and stress.",
         "They kept managing water, weeds, pests and disease as good farmers do.",
         "They compared their plot with a neighbour's, so the difference was there for everyone to see."]),
       ("Will it work on your farm?", [
         "Old farms with years of DAP behind them usually hold a phosphorus bank. These are the fields where skipping or cutting DAP works best.",
         "A soil test tells you how much phosphorus is there. If it is very low, use the program with a reduced dose of SSP or NPK, not with nothing. See <a href=\"/guides/dap-shortage-what-to-use-instead\">what to use instead of DAP</a>.",
         "Start with part of a field and compare it with the rest, as Budhabhai did.",
         "Results differ with soil, water, weather, variety and care. What these farmers saw is their own experience."]),
       ("Start this rabi", [
         ("html", f"<p>Send us your crop, area, sowing date and village on {_WA}. Our team will tell you which Immunity products suit your crop, how much to use for your acreage, and when. See <a href=\"/products/immunity-granules\">Immunity Granules</a>, <a href=\"/products/immunity-gold\">Immunity Gold</a> and the <a href=\"/products\">crop Specials</a>.</p>")])],
      faq=[("Can a crop grow without DAP?", "Yes, on many farms. The crop needs phosphorus, not DAP. Old farms usually hold phosphorus locked from past DAP, and a loose, living soil with strong roots helps the crop reach it. On soils that test very low, add some phosphorus from SSP or NPK."),
           ("What did these farmers use instead of DAP?", "Immunity Granules in the soil at sowing, the Immunity Special for their crop through water or drip and as a spray, and Immunity Gold as a spray."),
           ("Did they use any chemical fertilizer?", "Bharatbhai used no DAP and a little urea once. Budhabhai used 6 bags of chemical fertilizer where the next plot used 10 to 12. Falguniben used about 2 to 2.5 bags of urea in sugarcane."),
           ("Is the result guaranteed?", "No. These are the farmers' own experiences. Results depend on soil, water, weather, variety and care. Try it on part of a field first."),
           ("How do I start?", "Send your crop, area, sowing date and village on WhatsApp to +91 99787 91167. Our team will suggest products and doses for your crop and acreage.")]),

 dict(slug="organic-alternative-to-dap", date="2026-11-22",
      title="Organic Alternative to DAP: Granules, Crop Specials, Gold",
      h1="Organic alternative to DAP: how to feed your crop when DAP is not available",
      desc="What can really stand in for DAP, how Immunity Granules, your crop's Immunity Special and Immunity Gold work together, crop-by-crop plans for this rabi, and when you still need some phosphorus.",
      answer="No organic product carries 23 kg of phosphorus in a bag the way DAP does. What an organic program can do is help the crop use the phosphorus already in your soil: loosen the soil, feed soil life, grow a bigger root system and free locked phosphorus. Many farmers do this with Immunity Granules at sowing, the Immunity Special for their crop through water or drip, and Immunity Gold as a spray, and have cut or stopped DAP.",
      sections=[
       ("DAP feeds the crop. The Immunity program feeds the soil that feeds the crop", [
         ("html", "<p>A bag of DAP puts about 9 kg of nitrogen and 23 kg of phosphorus into the soil. But most of that phosphorus is locked up within weeks, and the crop uses only about 15 to 25% of it. Year after year the locked part builds up, while the soil gets harder and its life gets weaker.</p>"
                  "<p>The Immunity program works the other way round. It starts with the soil and the roots, so the crop can reach the phosphorus, potash and micronutrients already in the field. That is why farmers using it have been able to skip DAP or cut chemical fertilizer, and why it keeps paying back season after season.</p>")]),
       ("The three parts of the program", [
         ("html", _TD([
           ["<a href=\"/products/immunity-granules\">Immunity Granules</a>", "In the soil at sowing or planting: in the furrow, in pits, or in the tree basin", "Made for hard, compact soil, weak soil life, poor roots and fields that need more fertilizer every year", "All crops"],
           ["Your crop's Immunity Special", "With irrigation water as a drench, through drip, and as a spray", "Made for the needs of that crop at each stage", "Sugarcane, potato, cumin, cotton, onion, chilli, mango, banana, citrus, apple and more"],
           ["<a href=\"/products/immunity-gold\">Immunity Gold</a>", "As a spray", "Our general formula for vigour and stress", "All crops, and crops without their own Special"]],
           ["Product", "Where it goes", "Its job", "For"]) +
          "<p>Biofertilizers add to the program: <a href=\"/products/immunity-psb\">PSB</a> and <a href=\"/products/immunity-psf\">PSF</a> free phosphorus, <a href=\"/products/immunity-kmb\">KMB</a> frees potash, <a href=\"/products/immunity-azotobacter\">Azotobacter</a> and <a href=\"/products/immunity-azospirillum\">Azospirillum</a> add nitrogen, and <a href=\"/products/immunity-rhizobium\">Rhizobium</a> feeds pulses.</p>")]),
       ("Crop by crop this rabi", [
         ("html", _TD([
           ["Wheat", "Immunity Granules at sowing, Immunity Gold sprays", "Add PSB and Azotobacter. Give the first irrigation at crown root stage on time."],
           ["Potato", "Immunity Granules, <a href=\"/products/immunity-potato-special\">Potato Special</a>, Immunity Gold", "Potato needs a lot of phosphorus and potash at planting. On low-testing soils, keep a reduced dose of SSP or NPK."],
           ["Cumin", "Immunity Granules, <a href=\"/products/immunity-cumin-special\">Cumin Special</a>, Immunity Gold", "Bharatbhai of Lariya grew cumin with no DAP this way."],
           ["Sugarcane", "Immunity Granules, <a href=\"/products/immunity-sugarcane-special\">Sugarcane Special</a>, Immunity Gold", "Budhabhai and Falguniben cut chemical fertilizer this way."],
           ["Gram and other pulses", "<a href=\"/products/immunity-pulses-special\">Pulses Special</a>, with Rhizobium on the seed", "Pulses make their own nitrogen when Rhizobium is active."],
           ["Mustard", "Immunity Granules, Immunity Gold", "Add PSB. Mustard also needs sulphur; SSP gives it."],
           ["Onion and vegetables", "<a href=\"/products/immunity-onion-special\">Onion Special</a> or <a href=\"/products/immunity-vegetable-special\">Vegetable Special</a>", "Start with Immunity Granules at transplanting."],
           ["Castor", "Immunity Granules, Immunity Gold", "Jitendrabhai of Vadnagar used the granules in pits in hard soil."],
           ["Mango and fruit trees", "Immunity Granules in the basin, the Special for the tree", "See <a href=\"/products/immunity-mango-special\">Mango Special</a> and the other fruit Specials."]],
           ["Crop", "Immunity products", "Notes"]) +
          f"<p class=\"note\">Doses depend on the crop, its stage and your acreage. Ask on {_WA} and our team will send the schedule for your field.</p>")]),
       ("When you still need some phosphorus", [
         "Your soil test shows phosphorus is low.",
         "Very sandy soil, or the first crop on newly broken land.",
         "Potato on low-testing soil, which needs phosphorus fast at planting.",
         "In these fields, use the Immunity program with a reduced dose of SSP or NPK. See <a href=\"/guides/dap-shortage-what-to-use-instead\">how many bags equal one DAP bag</a>."]),
       ("Drench and drip: put the product where the roots are", [
         "Phosphorus barely moves in soil. Anything spread on top later reaches few roots.",
         "Immunity Granules go into the furrow, pits or basin, close to where roots will grow.",
         "The crop's Special goes in with irrigation water at the base of the plants, or through drip, so it soaks into the root zone.",
         "Sprays of the Special and of Immunity Gold feed the leaves and help the plant through stress.",
         "Apply biofertilizers and chemical fungicides at different times; fungicide can kill the microbes."]),
       ("How to start", [
         ("html", f"<ol><li>Send your crop, area, sowing date, village and, if you have it, your soil test on {_WA}.</li>"
                  "<li>Get the schedule for your crop and acreage from our team.</li>"
                  "<li>Buy direct from us, or ask us for the nearest dealer.</li>"
                  "<li>Start on a block of your field, compare it with the rest, and decide for next season with your own eyes.</li></ol>")])],
      faq=[("What is the best organic alternative to DAP?", "There is no organic bag that carries as much phosphorus as DAP. The working alternative is a program that frees the phosphorus already in your soil and grows stronger roots: Immunity Granules at sowing, your crop's Immunity Special and Immunity Gold, with PSB."),
           ("Can Immunity Granules replace DAP?", "Many farmers have skipped DAP using Immunity Granules with their crop's Special and Immunity Gold, especially on old farms with phosphorus locked in the soil. On soils that test very low in phosphorus, use the program with a reduced dose of SSP or NPK."),
           ("Can I use the Immunity program with SSP or NPK?", "Yes. Immunity products can be used with chemical fertilizers. Do a small jar test before mixing anything in one tank."),
           ("Does it work for wheat?", "Yes. Use Immunity Granules at sowing with PSB and Azotobacter, and Immunity Gold sprays. Ask our team for doses for your acreage."),
           ("Where can I buy Immunity products?", "Directly from Gujarat Bio Organics, Bhavnagar, or through a dealer near you. Call or WhatsApp +91 99787 91167.")]),

 dict(slug="free-locked-phosphorus-in-soil", date="2026-11-22",
      title="Locked Phosphorus in Soil: How to Free the DAP in Your Field",
      h1="Locked phosphorus: how to free the DAP you have already paid for",
      desc="Why only 15-25% of the phosphorus in fertilizer feeds the crop, how calcium in alkaline soils locks the rest, and how humic acid, phosphate-solubilising microbes, drench and drip, and a softer soil bring it back to the roots.",
      answer="Only about 15-25% of the phosphorus you apply as fertilizer becomes available to the crop. The rest is locked by calcium in alkaline soils, or by iron and aluminium in acid soils, and builds up over the years. Humic substances, phosphate-solubilising microbes, organic matter, a looser soil with deeper roots, and products placed in the root zone by drench or drip help the crop reach it.",
      sections=[
       ("Where your DAP goes", [
         ("html", "<p>India's National Academy of Agricultural Sciences reports that only 15 to 25% of fertilizer phosphorus becomes available to plants, and only 1 to 3% of all the phosphorus in a soil is available at any time. In alkaline soils, above pH 7, phosphorus reacts with calcium and magnesium. In acid soils, below pH 6, it reacts with iron and aluminium. Either way it turns into forms that roots cannot easily take up.</p>"
                  "<p>Much of Gujarat has alkaline, calcium-rich black and coastal soils. Here a large share of each DAP bag ends up as calcium phosphate. It is not lost; it is locked. And after decades of DAP, many fields hold a large bank of it.</p>")]),
       ("Signs your soil is holding phosphorus back", [
         "The soil test shows medium or high phosphorus, but the crop still shows phosphorus hunger: slow early growth, weak roots, a purple tinge on young wheat or maize leaves.",
         "Yields have stopped rising though you use more DAP every year.",
         "The soil is hard and crusts after irrigation, and water stands on the surface.",
         "Fields fed DAP for years run short of zinc. See <a href=\"/micronutrients/zinc/zinc-and-phosphorus-dap\">zinc and phosphorus</a>."]),
       ("Five ways to bring locked phosphorus back", [
         ("html", "<ul><li><strong>Humic substances.</strong> In a study on alkaline soil (Wang and others, Soil Use and Management, 1995), adding humic acids with phosphorus fertilizer increased water-soluble phosphate, slowed the formation of locked forms, and raised phosphorus uptake and wheat yield by 25%. See <a href=\"/guides/humic-acid-and-root-zone-development\">humic acid and the root zone</a>.</li>"
                  "<li><strong>Microbes that dissolve phosphate.</strong> Phosphate-solubilising bacteria and fungi release organic acids that dissolve calcium phosphate near the roots. The national academy recommends such consortia, with mycorrhiza, to raise phosphorus use. See <a href=\"/products/immunity-psb\">Immunity PSB</a>, <a href=\"/products/immunity-psf\">PSF</a> and <a href=\"/products/immunity-mycorrhiza\">Mycorrhiza</a>.</li>"
                  "<li><strong>Organic matter.</strong> Compost and well-rotted farmyard manure release phosphorus slowly and keep it in forms roots can use. See <a href=\"/guides/compost-and-humic-acid\">compost and humic acid</a>.</li>"
                  "<li><strong>Bigger roots.</strong> Phosphorus barely moves, so the roots must come to it. A larger, deeper root system, extended by mycorrhiza, reaches far more of the soil.</li>"
                  "<li><strong>Placement.</strong> Phosphorus and products placed near the seed or in the root zone work better than the same amount spread on top.</li></ul>")]),
       ("A softer soil, deeper roots", [
         ("html", "<p>Hard, compact soil keeps roots short and shallow, so they touch only a thin layer of the phosphorus bank. When soil life and organic matter return, the soil crumbles, holds air and water, and roots travel deeper.</p>"
                  "<p>A living soil also holds nutrients better. Soil scientists call this the cation exchange capacity: the soil's power to hold calcium, magnesium, potash and other nutrients like a sponge and release them to the roots. Organic matter raises it. And around every active root, the acids made by roots and microbes lower the pH in a thin zone, where locked calcium phosphate dissolves even when the rest of the soil stays alkaline.</p>"
                  "<p><a href=\"/products/immunity-granules\">Immunity Granules</a> are made for exactly this: hard, compact soil, weak soil life and poor roots. The crop's Immunity Special, given with irrigation water or through drip, goes straight into that root zone. Jitendrabhai of Vadnagar saw his castor roots go deep into hard soil after using the granules.</p>")]),
       ("A season plan to unlock phosphorus", [
         ("html", "<ol><li>Test your soil. Know how much phosphorus is already there. See <a href=\"/guides/how-to-take-a-soil-sample\">how to take a soil sample</a>.</li>"
                  "<li>Before sowing, add compost or farmyard manure, and put Immunity Granules in the furrow, pits or basin.</li>"
                  "<li>Treat seed or soil with PSB, and Rhizobium for pulses. Keep chemical fungicide seed treatment separate in time.</li>"
                  "<li>After the sowing irrigations, give the crop's Immunity Special as a drench or through drip.</li>"
                  "<li>Spray Immunity Gold at fast growth and after stress.</li>"
                  "<li>Use phosphorus fertilizer only as your soil test says, placed near the seed.</li>"
                  f"<li>Leave a strip on your old practice, compare at harvest, and ask us on {_WA} for doses for your crop.</li></ol>")])],
      faq=[("Why does my crop show phosphorus deficiency even after DAP?", "Most of the DAP phosphorus gets locked in the soil, by calcium in alkaline soils or iron and aluminium in acid soils. Hard soil and weak roots make it worse. The crop needs a living soil and strong roots to reach it."),
           ("Can I free phosphorus without adding more DAP?", "Yes, partly. Humic substances, phosphate-solubilising microbes, organic matter, deeper roots and placing products in the root zone all help the crop use phosphorus already in the soil."),
           ("Does humic acid release phosphorus?", "Studies on alkaline soils show humic acids keep more phosphate soluble and slow its locking, so the crop takes up more."),
           ("Is high pH soil bad for phosphorus?", "Above pH 7, phosphorus reacts with calcium and gets locked. Roots and microbes can dissolve it again in the zone right around the root."),
           ("How long do PSB take to work?", "They start working once the soil is moist and warm, and work best with organic matter. The benefit builds over the season and over seasons.")]),

 dict(slug="urea-and-potash-alternatives", date="2026-11-22",
      title="Urea and Potash Shortage: Cut Urea, Potash and NPK Naturally",
      h1="Urea and potash shortage: how humic acid, seaweed and amino acids help you need fewer bags",
      desc="Why only 30-45% of urea reaches the crop, how to stop the losses, how potash-mobilising bacteria, humic acid, seaweed extract and amino acids help the crop do more with less, and how farmers cut urea.",
      answer="Indian crops use only about 30-45% of the nitrogen in urea; the rest is lost to the air and to leaching. You can need fewer bags by splitting urea, placing it well and using biostimulants and microbes: humic acid keeps nutrients in the root zone, seaweed extract and amino acids help the plant use what it takes up and cope with stress, and bacteria add nitrogen and free potash. Many farmers have cut urea this way; it does not mean starving the crop.",
      sections=[
       ("Where your urea goes", [
         ("html", "<p>In India, heavy urea use has pulled nitrogen use efficiency down to about 30 to 45%. Most of the rest escapes as gas from urea left on the soil surface, or washes below the roots with irrigation water. Too much urea also makes crops soft and lush, so pests and diseases come faster and the crop can fall over.</p>"
                  "<p>So every bag saved from loss is a bag you do not need to buy. When urea, DAP or potash is short, that matters twice.</p>")]),
       ("Use fewer bags of urea", [
         "Split urea into two or three doses at the stages the crop needs it, instead of one heavy dose.",
         "Give it just before irrigation, or mix it into the soil. Urea left on dry, hot soil turns to gas.",
         "Do not overdo early doses. Watch the leaf colour, and add more only if the crop turns pale.",
         "Use nitrogen-fixing bacteria: <a href=\"/products/immunity-azotobacter\">Azotobacter</a> for wheat and vegetables, <a href=\"/products/immunity-azospirillum\">Azospirillum</a> for cereals, <a href=\"/products/immunity-acetobacter\">Acetobacter</a> for sugarcane and <a href=\"/products/immunity-rhizobium\">Rhizobium</a> for pulses.",
         "Return crop residues and add compost. Organic matter releases nitrogen slowly through the season."]),
       ("Potash: the bag many farmers skip, and how to stretch it", [
         "Potash fills grain, tubers, fruit and sugar, and helps the crop stand heat, cold and disease.",
         "Many Indian soils hold potash locked in their minerals. Potash-mobilising bacteria such as <a href=\"/products/immunity-kmb\">Immunity KMB</a> help release it.",
         "Crop residues are rich in potash. Burning them or carrying them away takes that potash off the farm.",
         "Do not skip potash for potato, banana or sugarcane on soils that test low."]),
       ("How humic acid, seaweed and amino acids help", [
         ("html", _TD([
           ["Humic acid", "Holds nutrients in the root zone, improves soil structure, and helps roots grow", "Hard or sandy soils, at sowing and with fertilizer", "<a href=\"/guides/humic-acid-and-root-zone-development\">Humic acid and the root zone</a>"],
           ["Seaweed extract", "Carries natural growth signals that support roots, flowering and fruit set, and helps plants cope with stress", "Heat, cold or drought, flowering, fruit set", "<a href=\"/guides/seaweed-extracts-and-plant-physiology\">Seaweed extracts and plant physiology</a>"],
           ["Amino acids and protein hydrolysates", "Give the plant ready building blocks, so it recovers faster and uses nutrients better", "After stress, during fast growth", "<a href=\"/guides/protein-hydrolysates-and-nutrient-use-efficiency\">Protein hydrolysates and nutrient use</a>"]],
           ["Biostimulant", "What it does", "Where it helps most", "Read more"]) +
          "<p>Quality matters. A mildly processed seaweed extract keeps much more of what the plant uses than a cheap one made with harsh chemicals and high heat. Biostimulants sold in India must meet the Fertiliser Control Order; see <a href=\"/guides/what-are-biostimulants\">what biostimulants are</a>.</p>")]),
       ("What farmers saw", [
         "<strong>Falguniben Patel, Navsari:</strong> sugarcane with about 2 to 2.5 bags of urea where farmers might otherwise use 3 or 4, using Immunity Granules, Sugarcane Special and Gold. Leaves were still green at harvest.",
         "<strong>Budhabhai Patel:</strong> sugarcane on 6 bags of chemical fertilizer, while the plot next door got 10 to 12.",
         "<strong>Bharatbhai, Lariya:</strong> cumin with no DAP, and urea only once in a small amount.",
         "These are their own experiences. Read their stories in <a href=\"/guides/farming-without-dap\">farming without DAP</a>."]),
       ("A simple plan to cut urea and NPK this season", [
         ("html", "<ol><li>Test your soil, so you cut what the crop does not need, not what it does.</li>"
                  "<li>At sowing: compost, <a href=\"/products/immunity-granules\">Immunity Granules</a> and the right biofertilizers.</li>"
                  "<li>During the crop: your crop's Immunity Special through irrigation water or drip, and <a href=\"/products/immunity-gold\">Immunity Gold</a> sprays at fast growth and after stress.</li>"
                  "<li>Cut one urea dose, or reduce each split, and watch the leaf colour.</li>"
                  "<li>Leave a strip on your old practice and compare at harvest.</li>"
                  f"<li>Next season, cut a step more where the crop stayed strong. Ask on {_WA} for a schedule for your crop.</li></ol>")])],
      faq=[("What is the organic alternative to urea?", "No organic product carries 46% nitrogen. What works is cutting losses and adding biological nitrogen: split urea, nitrogen-fixing bacteria such as Azotobacter, Azospirillum, Acetobacter and Rhizobium, compost, and biostimulants that help the crop use nitrogen better."),
           ("Can I stop urea completely?", "Pulses can need little or none when Rhizobium is active. For most other crops, reduce urea step by step and watch the crop, rather than stopping at once."),
           ("What can replace potash?", "Potash-mobilising bacteria release potash locked in soil minerals, and returning crop residues brings potash back. On soils that test low, potato, banana and sugarcane still need potash fertilizer."),
           ("Do seaweed and humic acid reduce fertilizer need?", "They help the crop take up and use nutrients better and cope with stress, so many farmers can use fewer bags. They work alongside good nutrition, not in place of all of it."),
           ("How do I know I have cut too much nitrogen?", "Older leaves turn pale yellow first and growth slows. Give a split dose of urea and adjust next time.")]),
]
SEASON_GUIDES = DAP_GUIDES + SEASON_GUIDES

DEEP.update({
"/guides/dap-token-booking-online": dict(
  hook="The bag costs ₹1,350 on paper. In a shortage, the real price is a 10-hour queue and a sowing date that slips. A token cannot make more DAP, but it can stop someone else from taking yours.",
  stats=[("₹1,350", "printed price of a 50 kg DAP bag"), ("48 hours", "how long a Rajasthan fertilizer token is valid"), ("95%", "fall in China's DAP exports, Jan-Jul 2026")],
  sources=[("AgToday: DAP international prices firm, China's export policy restrictive (August 2026)", "https://agtoday.info/2026/08/27/dap-international-prices-remain-firm-amid-tight-supply-while-chinas-export-policy-stays-restrictive/"),
           ("Amar Ujala: DAP shortage puts sowing at risk, Hamirpur (19 November 2026)", "https://www.amarujala.com/uttar-pradesh/hamirpur/shortage-of-dap-farmers-distressed-sowing-at-risk-hamirpur-news-c-223-1-sknp1030-147877-2026-11-19"),
           ("CMV360: Rajasthan launches online fertilizer booking (June 2026)", "https://www.cmv360.com/news/farmers-can-now-book-urea-and-dap-online-from-home-rajasthan-launches-new-digital-fertilizer-booking-system"),
           ("eGovtSchemes: MP e-Token for fertilizer (unofficial summary, June 2026)", "https://www.egovtschemes.com/e-token-mp-krishi/"),
           ("Online Gramin Help: FFS app token booking (unofficial summary, September 2026)", "https://onlinegramin.com/framework-for-fertilizer-sale-app-download/"),
           ("National Herald: DAP shortage spreads across India (October 2025)", "https://www.nationalheraldindia.com/national/sowing-season-turns-into-struggle-as-dap-fertiliser-shortage-spreads-across-india")]),
"/guides/farming-without-dap": dict(
  hook="A cumin farmer near Rajkot put no DAP in his field. At 60 days, his neighbours said they had never seen cumin like it. He had not found a secret bag. He had stopped feeding only the crop and started feeding the soil.",
  stats=[("0", "bags of DAP in Bharatbhai's cumin"), ("6 vs 10-12", "bags of chemical fertilizer: Budhabhai's sugarcane vs the plot next door"), ("15-25%", "of fertilizer phosphorus that ever reaches the crop")],
  sources=[("Gujarat Bio Organics on YouTube: Bharatbhai's cumin without DAP", "https://www.youtube.com/watch?v=O8MwXfORioU"),
           ("Gujarat Bio Organics on YouTube: Budhabhai Patel's sugarcane", "https://www.youtube.com/watch?v=bepJSpkepfg"),
           ("Gujarat Bio Organics on YouTube: Falguniben Patel's sugarcane", "https://www.youtube.com/watch?v=6lyzRwnubrQ"),
           ("Gujarat Bio Organics on YouTube: Jitendrabhai Patel's castor", "https://www.youtube.com/watch?v=8OFyCo49cAI"),
           ("NAAS Policy Paper 68: Efficient Utilization of Phosphorus (2014)", "https://naas.org.in/Policy%20Papers/policy%2068.pdf")]),
"/guides/organic-alternative-to-dap": dict(
  hook="Searching for a bag that replaces DAP is the wrong search. Your field already holds years of phosphorus it never gave to the crop. The alternative to DAP is getting that phosphorus back.",
  stats=[("23 kg", "phosphorus (P2O5) in one 50 kg DAP bag"), ("15-25%", "of it the crop actually uses"), ("3", "parts of the program: Granules, crop Special, Gold")],
  sources=[("NAAS Policy Paper 68: Efficient Utilization of Phosphorus (2014)", "https://naas.org.in/Policy%20Papers/policy%2068.pdf"),
           ("The Tribune: PAU urges growers to use DAP alternatives", "https://tribuneindia.com/news/pau-urges-growers-to-use-dap-alternatives")]),
"/guides/free-locked-phosphorus-in-soil": dict(
  hook="Every bag of DAP you ever bought is partly still in your field. It did not wash away. It turned into calcium phosphate, a rock the roots cannot eat, waiting for something to dissolve it.",
  stats=[("15-25%", "of fertilizer phosphorus becomes available to plants"), ("1-3%", "of all soil phosphorus is available at any time"), ("25%", "higher wheat yield with humic acids in one alkaline-soil study")],
  sources=[("NAAS Policy Paper 68: Efficient Utilization of Phosphorus (2014)", "https://naas.org.in/Policy%20Papers/policy%2068.pdf"),
           ("Wang, Wang and Li (1995): The effect of humic acids on the availability of phosphorus fertilizers in alkaline soils", "https://agris.fao.org/search/en/records/65dfbf654c5aef494fe4f324")]),
"/guides/urea-and-potash-alternatives": dict(
  hook="Of every three bags of urea, more than one may never reach the crop. When urea and potash are short, the cheapest bag is the one you stop losing.",
  stats=[("30-45%", "nitrogen use efficiency of urea in India"), ("46%", "nitrogen in urea: no organic bag matches it, so cut the losses")],
  sources=[("Down To Earth: Why India must reduce its dependence on conventional urea (July 2026)", "https://www.downtoearth.org.in/agriculture/why-india-must-reduce-its-dependence-on-conventional-urea"),
           ("Gujarat Bio Organics on YouTube: Falguniben Patel's sugarcane", "https://www.youtube.com/watch?v=6lyzRwnubrQ")]),
})
DEEP["/guides/dap-shortage-what-to-use-instead"].setdefault("add", []).append(("More on the DAP shortage", [
  "<a href=\"/guides/dap-token-booking-online\">DAP token and booking app: how to book DAP and urea online</a>",
  "<a href=\"/guides/farming-without-dap\">Farming without DAP: what happened when these farmers stopped using it</a>",
  "<a href=\"/guides/organic-alternative-to-dap\">Organic alternative to DAP: Immunity Granules, crop Specials and Gold</a>",
  "<a href=\"/guides/free-locked-phosphorus-in-soil\">Locked phosphorus: how to free the DAP you have already paid for</a>",
  "<a href=\"/guides/urea-and-potash-alternatives\">Urea and potash shortage: how to need fewer bags</a>"]))
