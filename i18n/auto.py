# Pattern rules for repeated sentences (product pages, crop page photo slots). Writes i18n/tr/<lang>1_auto.tsv
# for strings that match a rule and are not yet translated. A rule's template may use {1}, {2}... for groups and
# {t1}, {t2}... for the translation of a group (looked up in the dictionary; the rule is skipped if missing).
import json, re, sys, os
ROOT = os.path.dirname(os.path.abspath(__file__))
lang = sys.argv[1]
keys = json.load(open(os.path.join(ROOT, "src1.json"), encoding="utf-8"))
d = json.load(open(os.path.join(ROOT, f"{lang}.json"), encoding="utf-8"))
P = r"(Immunity [^?]+?)"
RULES = {
 "gu": [
  (rf"^Video coming soon: Farmer who used {P} talking in his field about his crop$", "વિડિયો જલ્દી આવશે: {1} વાપરનાર ખેડૂત પોતાના ખેતરમાં પાક વિશે વાત કરે છે"),
  (rf"^Farmer who used {P} talking in his field about his crop$", "{1} વાપરનાર ખેડૂત પોતાના ખેતરમાં પાક વિશે વાત કરે છે"),
  (rf"^Video coming soon: Short video showing how {P} is mixed and applied in the field$", "વિડિયો જલ્દી આવશે: ખેતરમાં {1} કેવી રીતે ભેળવીને આપવું તેનો ટૂંકો વિડિયો"),
  (rf"^Short video showing how {P} is mixed and applied in the field$", "ખેતરમાં {1} કેવી રીતે ભેળવીને આપવું તેનો ટૂંકો વિડિયો"),
  (rf"^Photo coming soon: Clear photo of the back label of {P} showing composition and directions$", "ફોટો જલ્દી આવશે: {1}ના પાછળના લેબલનો સ્પષ્ટ ફોટો, ઘટકો અને ઉપયોગની રીત સાથે"),
  (rf"^Clear photo of the back label of {P} showing composition and directions$", "{1}ના પાછળના લેબલનો સ્પષ્ટ ફોટો, ઘટકો અને ઉપયોગની રીત સાથે"),
  (rf"^Send your crop, its stage and your location, and our team will tell you how {P} fits your programme\.$", "તમારો પાક, તેનો તબક્કો અને તમારું સ્થળ મોકલો, અને અમારી ટીમ જણાવશે કે {1} તમારા કાર્યક્રમમાં કેવી રીતે બેસે છે."),
  (rf"^What is {P}\?$", "{1} શું છે?"),
  (rf"^What pack sizes does {P} come in\?$", "{1} કયા પેકિંગમાં આવે છે?"),
  (rf"^What is the price of {P}\?$", "{1}નો ભાવ શું છે?"),
  (r"^(.+?) It is made by Gujarat Bio Organics Pvt\. Ltd\. in Bhavnagar, Gujarat\.$", "{t1} તે ભાવનગર, ગુજરાતમાં ગુજરાત બાયો ઓર્ગેનિક્સ પ્રા. લિ. બનાવે છે."),
  (r"^(.+?) Pack sizes, who it is for, how farmers use it, and how to send an(?: enquiry on WhatsApp\.| enquiry on\.\.\.|\.\.\.)$", "{t1} પેકિંગ, કોના માટે છે, ખેડૂતો કેવી રીતે વાપરે છે અને WhatsApp પર પૂછપરછ કેવી રીતે કરવી."),
  (rf"^{P} Organic Fertilizer \| (?:Gujarat Bio Organics|GBO)$", "{1} ઓર્ગેનિક ખાતર | GBO"),
  (rf"^{P} Biofertilizer \| (?:Gujarat Bio Organics|GBO)$", "{1} બાયો ખાતર | GBO"),
  (rf"^{P} \| GBO$", "{1} | GBO"),
  (r'^<a href="/">Home</a> / <a href="/products">Products</a> / (.+)$', '<a href="/">હોમ</a> / <a href="/products">ઉત્પાદનો</a> / {1}'),
  (r"^([\d., ]+(?:mL|L|kg)[\w ,.]*)\.$", "{1}."),
 ],
 "hi": [
  (rf"^Video coming soon: Farmer who used {P} talking in his field about his crop$", "वीडियो जल्द आएगा: {1} इस्तेमाल करने वाले किसान अपने खेत में फसल के बारे में बात करते हुए"),
  (rf"^Farmer who used {P} talking in his field about his crop$", "{1} इस्तेमाल करने वाले किसान अपने खेत में फसल के बारे में बात करते हुए"),
  (rf"^Video coming soon: Short video showing how {P} is mixed and applied in the field$", "वीडियो जल्द आएगा: खेत में {1} कैसे मिलाकर डालें, इसका छोटा वीडियो"),
  (rf"^Short video showing how {P} is mixed and applied in the field$", "खेत में {1} कैसे मिलाकर डालें, इसका छोटा वीडियो"),
  (rf"^Photo coming soon: Clear photo of the back label of {P} showing composition and directions$", "फोटो जल्द आएगी: {1} के पिछले लेबल की साफ फोटो, सामग्री और इस्तेमाल के तरीके के साथ"),
  (rf"^Clear photo of the back label of {P} showing composition and directions$", "{1} के पिछले लेबल की साफ फोटो, सामग्री और इस्तेमाल के तरीके के साथ"),
  (rf"^Send your crop, its stage and your location, and our team will tell you how {P} fits your programme\.$", "अपनी फसल, उसकी अवस्था और अपनी जगह भेजें, हमारी टीम बताएगी कि {1} आपके कार्यक्रम में कैसे काम आएगा।"),
  (rf"^What is {P}\?$", "{1} क्या है?"),
  (rf"^What pack sizes does {P} come in\?$", "{1} किन पैकिंग में आता है?"),
  (rf"^What is the price of {P}\?$", "{1} की कीमत क्या है?"),
  (r"^(.+?) It is made by Gujarat Bio Organics Pvt\. Ltd\. in Bhavnagar, Gujarat\.$", "{t1} इसे भावनगर, गुजरात में गुजरात बायो ऑर्गेनिक्स प्रा. लि. बनाती है।"),
  (r"^(.+?) Pack sizes, who it is for, how farmers use it, and how to send an(?: enquiry on WhatsApp\.| enquiry on\.\.\.|\.\.\.)$", "{t1} पैकिंग, किसके लिए है, किसान कैसे इस्तेमाल करते हैं और WhatsApp पर पूछताछ कैसे करें।"),
  (rf"^{P} Organic Fertilizer \| (?:Gujarat Bio Organics|GBO)$", "{1} जैविक खाद | GBO"),
  (rf"^{P} Biofertilizer \| (?:Gujarat Bio Organics|GBO)$", "{1} जैव उर्वरक | GBO"),
  (rf"^{P} \| GBO$", "{1} | GBO"),
  (r'^<a href="/">Home</a> / <a href="/products">Products</a> / (.+)$', '<a href="/">होम</a> / <a href="/products">उत्पाद</a> / {1}'),
  (r"^([\d., ]+(?:mL|L|kg)[\w ,.]*)\.$", "{1}."),
 ]}

CROP_HI = {"apple": "सेब", "banana": "केला", "chilli (mirchi)": "मिर्च", "citrus": "नींबू-संतरा (सिट्रस)", "coconut": "नारियल", "cotton": "कपास",
 "cumin (jeera)": "जीरा", "fruit orchards": "फल बाग", "groundnut (mungfali)": "मूंगफली", "maize": "मक्का", "mango": "आम", "onion": "प्याज",
 "paddy": "धान", "pomegranate": "अनार", "potato": "आलू", "pulses": "दलहन", "sugarcane": "गन्ना", "tea": "चाय", "vegetables": "सब्ज़ियाँ", "wheat and cereals": "गेहूं और अनाज"}
PLACE_HI = {"Himachal Pradesh and Jammu and Kashmir": "हिमाचल प्रदेश और जम्मू-कश्मीर", "Gujarat": "गुजरात", "Punjab": "पंजाब", "Andhra Pradesh": "आंध्र प्रदेश",
 "Maharashtra": "महाराष्ट्र", "Kerala": "केरल", "Gujarat and Rajasthan": "गुजरात और राजस्थान", "Across India": "पूरे भारत", "Karnataka": "कर्नाटक",
 "West Bengal": "पश्चिम बंगाल", "Madhya Pradesh": "मध्य प्रदेश", "Assam": "असम"}
CR = "(" + "|".join(re.escape(k) for k in sorted(CROP_HI, key=len, reverse=True)) + ")"
def ch(m, i): return CROP_HI[m.group(i).lower()]
CROP_RULES_HI = [
 (rf"^(Photo coming soon: )?Wide photo of a healthy {CR} crop in the field, ideally with the farmer, in (.+)$", lambda m: (("फोटो जल्द आएगी: " if m.group(1) else "") + f"खेत में स्वस्थ {ch(m,2)} फसल की बड़ी फोटो, हो सके तो किसान के साथ, {PLACE_HI[m.group(3)]} में") if m.group(3) in PLACE_HI else None),
 (rf"^(Photo coming soon: )?Close-up photo of a healthy {CR} plant, roots or produce for comparison$", lambda m: ("फोटो जल्द आएगी: " if m.group(1) else "") + f"तुलना के लिए स्वस्थ {ch(m,2)} के पौधे, जड़ों या उपज की नज़दीकी फोटो"),
 (rf"^(Video coming soon: )?{CR} farmer talking in his field about his crop and what changed$", lambda m: ("वीडियो जल्द आएगा: " if m.group(1) else "") + f"{ch(m,2)} किसान अपने खेत में फसल के बारे में और क्या बदला, इस पर बात करते हुए"),
 (rf"^(Video coming soon: )?Second {CR} farmer story, filmed in the field$", lambda m: ("वीडियो जल्द आएगा: " if m.group(1) else "") + f"दूसरे {ch(m,2)} किसान की कहानी, खेत में रिकॉर्ड की गई"),
 (rf"^(Video coming soon: )?Our team on a field visit to a {CR} farm, checking roots and crop$", lambda m: ("वीडियो जल्द आएगा: " if m.group(1) else "") + f"हमारी टीम {ch(m,2)} के खेत के दौरे पर, जड़ें और फसल जाँचते हुए"),
 (rf"^{CR} stage by stage$", lambda m: f"{ch(m,1)}: अवस्था के अनुसार"),
 (rf"^{CR} guide$", lambda m: f"{ch(m,1)} गाइड"),
 (rf"^Common {CR} problems$", lambda m: f"{ch(m,1)} की आम समस्याएँ"),
 (rf"^{CR} farmers in their own words$", lambda m: f"{ch(m,1)} किसान अपने शब्दों में"),
 (rf"^{CR} questions$", lambda m: f"{ch(m,1)} से जुड़े सवाल"),
 (rf"^The Immunity formula for {CR}$", lambda m: f"{ch(m,1)} के लिए Immunity फॉर्मूला"),
 (rf"^Micronutrients to watch in {CR}$", lambda m: f"{ch(m,1)} में ध्यान रखने वाले सूक्ष्म पोषक तत्व"),
 (rf"^Many weak-crop problems in {CR} trace back to a hidden nutrient shortage\. These are the ones to check first:$", lambda m: f"{ch(m,1)} में कमज़ोर फसल की कई समस्याओं के पीछे पोषक तत्वों की छिपी कमी होती है। पहले इन्हें जाँचें:"),
 (rf"^Which Immunity product is for {CR}\?$", lambda m: f"{ch(m,1)} के लिए कौन-सा Immunity उत्पाद है?"),
 (rf"^Articles on {CR}$", lambda m: f"{ch(m,1)} पर लेख"),
 (r"^See (Immunity .+)$", lambda m: f"{m.group(1)} देखें"),
 (rf"^{CR} Farming Guide: Stages, Problems & Care \| GBO$", lambda m: f"{ch(m,1)} की खेती: अवस्थाएँ, समस्याएँ और देखभाल | GBO"),
 (rf"^{CR} guide for growers: stage-by-stage care, common problems, what to check, and how farmers use (Immunity .+?) through the season\.$", lambda m: f"{ch(m,1)} उत्पादकों के लिए गाइड: अवस्था के अनुसार देखभाल, आम समस्याएँ, क्या जाँचें, और पूरे मौसम में किसान {m.group(2)} कैसे इस्तेमाल करते हैं।"),
 (rf'^<a href="/">Home</a> / <a href="/crops">Crops</a> / {CR}$', lambda m: f'<a href="/">होम</a> / <a href="/crops">फसलें</a> / {ch(m,1)}'),
]
out = []
for i, k in enumerate(keys):
    if k in d: continue
    if lang == "hi":
        done = False
        for rx, fn in CROP_RULES_HI:
            m = re.match(rx, k, re.I)
            if m:
                try: v = fn(m)
                except KeyError: v = None
                if v: out.append(f"{i}\t{v}"); done = True
                break
        if done: continue
    for rx, tpl in RULES[lang]:
        m = re.match(rx, k)
        if not m: continue
        ok = True; s = tpl
        for gi, g in enumerate(m.groups(), 1):
            s = s.replace("{%d}" % gi, g)
            if "{t%d}" % gi in s:
                if g in d: s = s.replace("{t%d}" % gi, d[g])
                else: ok = False
        if ok: out.append(f"{i}\t{s}"); break
open(os.path.join(ROOT, "tr", f"{lang}1_auto.tsv"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(lang, "auto", len(out))
