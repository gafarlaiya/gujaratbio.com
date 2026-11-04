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
out = []
for i, k in enumerate(keys):
    if k in d: continue
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
