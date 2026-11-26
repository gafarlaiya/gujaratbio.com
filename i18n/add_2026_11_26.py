# -*- coding: utf-8 -*-
"""Gujarati and Hindi for the 57 English strings added to www pages in Nov 2026 (mango site move,
mango guide cards, 'For business buyers' blocks, contact intro, mango crop calendar).
Without them 11 pages per language stopped rebuilding. Run once: python3 i18n/add_2026_11_26.py"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
MISSING = json.load(open(os.environ.get("MISSING_JSON", os.path.join(HERE, "missing_2026_11_26.json")), encoding="utf-8"))

# plain text and link-text translations: English -> (gu, hi)
T = {
 "Start the free check": ("મફત ચકાસણી શરૂ કરો", "मुफ़्त जाँच शुरू करें"),
 "Get a plan for your own orchard": ("તમારા પોતાના બગીચા માટે પ્લાન મેળવો", "अपने बाग़ के लिए प्लान पाएँ"),
 "More on mango": ("કેરી વિશે વધુ", "आम के बारे में और"),
 "Alternate bearing in mango": ("આંબામાં એકાંતરે ફળ", "आम में एकांतर फलन"),
 "Mango fruit drop": ("કેરી ખરવી", "आम के फल गिरना"),
 "Mango diseases and pests: how to recognise them and what growers can do": ("આંબાના રોગ અને જીવાત: કેવી રીતે ઓળખવા અને ખેડૂત શું કરી શકે", "आम के रोग और कीट: कैसे पहचानें और किसान क्या करें"),
 "Mango diseases and pests": ("આંબાના રોગ અને જીવાત", "आम के रोग और कीट"),
 "Mango farming in India: soil, planting, feeding, flowering and harvest in one guide": ("ભારતમાં આંબાની ખેતી: જમીન, વાવેતર, ખાતર, મોર અને ઉતારો એક જ માર્ગદર્શિકામાં", "भारत में आम की खेती: मिट्टी, रोपाई, खाद, बौर और तुड़ाई एक ही गाइड में"),
 "Mango farming in India: the complete guide": ("ભારતમાં આંબાની ખેતી: સંપૂર્ણ માર્ગદર્શિકા", "भारत में आम की खेती: पूरी गाइड"),
 "Mango flowering care and spray schedule": ("આંબાના મોરની માવજત અને છંટકાવ સમયપત્રક", "आम के बौर की देखभाल और छिड़काव समय-सारणी"),
 "Mango powdery mildew: how to spot it early and when to protect your flowers": ("આંબામાં ભૂકી છારો: વહેલો કેવી રીતે ઓળખવો અને મોરને ક્યારે બચાવવો", "आम में चूर्णिल आसिता (पाउडरी मिल्ड्यू): जल्दी कैसे पहचानें और बौर को कब बचाएँ"),
 "Mango powdery mildew": ("આંબામાં ભૂકી છારો", "आम में पाउडरी मिल्ड्यू"),
 "Biofertiliser manufacturer in India: bulk, private label and export": ("ભારતમાં બાયો ખાતર ઉત્પાદક: જથ્થાબંધ, પ્રાઇવેટ લેબલ અને નિકાસ", "भारत में जैव उर्वरक निर्माता: थोक, प्राइवेट लेबल और निर्यात"),
 "Organic fertilizer manufacturer in India": ("ભારતમાં ઓર્ગેનિક ખાતર ઉત્પાદક", "भारत में जैविक खाद निर्माता"),
 "Types of biofertilizers and what each one does": ("બાયો ખાતરના પ્રકાર અને દરેક શું કરે છે", "जैव उर्वरकों के प्रकार और हर एक क्या करता है"),
 "A plain guide to mango disease and pests: powdery mildew, anthracnose, malformation, sooty mould, dieback and canker, plus hoppers, mealybugs and fruit fly.":
   ("આંબાના રોગ અને જીવાતની સરળ માર્ગદર્શિકા: ભૂકી છારો, કાલવ્રણ (એન્થ્રેક્નોઝ), વિકૃતિ, કાળી ફૂગ, ડાળી સુકારો અને કેન્કર, સાથે મધિયો, ચીકટો અને ફળમાખી.",
    "आम के रोग और कीटों की सरल गाइड: पाउडरी मिल्ड्यू, एन्थ्रेक्नोज़, गुच्छा रोग (मालफ़ॉर्मेशन), काली फफूँद, डाईबैक और कैंकर, साथ में भुनगा (हॉपर), मिलीबग और फल मक्खी."),
 "April to June": ("એપ્રિલ થી જૂન", "अप्रैल से जून"),
 "August to September": ("ઑગસ્ટ થી સપ્ટેમ્બર", "अगस्त से सितंबर"),
 "Contact Gujarat Bio Organics, organic fertilizer manufacturer in Shihor, Bhavnagar, Gujarat. Call or WhatsApp +91 99787 91167 or email sales@gujaratbio.com.":
   ("ગુજરાત બાયો ઓર્ગેનિક્સનો સંપર્ક કરો, શિહોર, ભાવનગર, ગુજરાતના ઓર્ગેનિક ખાતર ઉત્પાદક. ફોન કે WhatsApp +91 99787 91167 અથવા ઈમેલ sales@gujaratbio.com.",
    "गुजरात बायो ऑर्गेनिक्स से संपर्क करें, शिहोर, भावनगर, गुजरात के जैविक खाद निर्माता. फ़ोन या WhatsApp +91 99787 91167 या ईमेल sales@gujaratbio.com."),
 "Contact an Organic Fertilizer Manufacturer in Gujarat | GBO": ("ગુજરાતના ઓર્ગેનિક ખાતર ઉત્પાદકનો સંપર્ક કરો | GBO", "गुजरात के जैविक खाद निर्माता से संपर्क करें | GBO"),
 "December to February": ("ડિસેમ્બર થી ફેબ્રુઆરી", "दिसंबर से फ़रवरी"),
 "February to March": ("ફેબ્રુઆરી થી માર્ચ", "फ़रवरी से मार्च"),
 "For business buyers": ("વેપારી ખરીદદારો માટે", "व्यापारिक ख़रीदारों के लिए"),
 "For manufacturers, importers, dealers and brand owners, our business site has the matching pages:": ("ઉત્પાદકો, આયાતકારો, ડીલરો અને બ્રાન્ડ માલિકો માટે અમારી બિઝનેસ સાઇટ પર સંબંધિત પાનાં છે:", "निर्माताओं, आयातकों, डीलरों और ब्रांड मालिकों के लिए हमारी बिज़नेस साइट पर संबंधित पेज हैं:"),
 "Free mango orchard check": ("આંબાના બગીચાની મફત ચકાસણી", "आम के बाग़ की मुफ़्त जाँच"),
 "Fruit grows and ripens": ("ફળ મોટા થાય અને પાકે", "फल बढ़ते और पकते हैं"),
 "June to July, after harvest": ("જૂન થી જુલાઈ, ઉતારા પછી", "जून से जुलाई, तुड़ाई के बाद"),
 "Mango Farming in India: Care Calendar, Flowering, Diseases": ("ભારતમાં આંબાની ખેતી: માવજત કેલેન્ડર, મોર, રોગ", "भारत में आम की खेती: देखभाल कैलेंडर, बौर, रोग"),
 "Mango care calendar and guides": ("આંબાની માવજતનું કેલેન્ડર અને માર્ગદર્શિકા", "आम की देखभाल का कैलेंडर और गाइड"),
 "Mango cultivation in India from soil and varieties to planting, irrigation, feeding, pruning, flowering care, pests and harvest. A month by month plan for Gujarat growers.":
   ("ભારતમાં આંબાની ખેતી: જમીન અને જાતોથી લઈને વાવેતર, પિયત, ખાતર, છટણી, મોરની માવજત, જીવાત અને ઉતારા સુધી. ગુજરાતના ખેડૂતો માટે મહિના પ્રમાણે પ્લાન.",
    "भारत में आम की खेती: मिट्टी और किस्मों से लेकर रोपाई, सिंचाई, खाद, छँटाई, बौर की देखभाल, कीट और तुड़ाई तक. गुजरात के किसानों के लिए महीने-दर-महीने योजना."),
 "Mango farming guide for growers: month-by-month care, flowering and fruit set, powdery mildew, hoppers, fruit drop and alternate bearing, from Gujarat.":
   ("ખેડૂતો માટે આંબાની ખેતીની માર્ગદર્શિકા: મહિના પ્રમાણે માવજત, મોર અને ફળ બેસવું, ભૂકી છારો, મધિયો, કેરી ખરવી અને એકાંતરે ફળ, ગુજરાતથી.",
    "किसानों के लिए आम की खेती की गाइड: महीने-दर-महीने देखभाल, बौर और फल लगना, पाउडरी मिल्ड्यू, भुनगा, फल गिरना और एकांतर फलन, गुजरात से."),
 "Mango powdery mildew explained: the white powder on panicles, the weather that triggers it, when to protect flowers, and how to avoid common spray mistakes.":
   ("આંબામાં ભૂકી છારો સમજો: મોર પર સફેદ પાવડર, કયું હવામાન તેને વધારે છે, મોરને ક્યારે બચાવવો અને છંટકાવની સામાન્ય ભૂલો કેવી રીતે ટાળવી.",
    "आम में पाउडरी मिल्ड्यू समझें: बौर पर सफ़ेद पाउडर, कौन-सा मौसम इसे बढ़ाता है, बौर को कब बचाएँ और छिड़काव की आम ग़लतियों से कैसे बचें."),
 "Month": ("મહિનો", "महीना"),
 "New flush grows": ("નવી ફૂટ વધે", "नई पत्तियाँ बढ़ती हैं"),
 "New shoots begin": ("નવી ડાળીઓ ફૂટે", "नई टहनियाँ निकलती हैं"),
 "October to November": ("ઓક્ટોબર થી નવેમ્બર", "अक्टूबर से नवंबर"),
 "Panicles and flowers": ("મોર અને ફૂલ", "बौर और फूल"),
 "Protect panicles at emergence; no spray at full bloom": ("મોર નીકળે ત્યારે રક્ષણ કરો; પૂરા ખીલેલા મોર પર છંટકાવ નહીં", "बौर निकलते समय बचाव करें; पूरे खिले बौर पर छिड़काव नहीं"),
 "Prune, clean the orchard, feed with compost or manure": ("છટણી કરો, બગીચો સાફ કરો, કમ્પોસ્ટ કે છાણિયું ખાતર આપો", "छँटाई करें, बाग़ साफ़ करें, कम्पोस्ट या गोबर की खाद दें"),
 "Reduce water, no nitrogen, clear weeds": ("પાણી ઓછું કરો, નાઇટ્રોજન નહીં, નીંદણ સાફ કરો", "पानी कम करें, नाइट्रोजन नहीं, खरपतवार साफ़ करें"),
 "Restart light irrigation; watch for hoppers and fruit drop": ("હળવું પિયત ફરી શરૂ કરો; મધિયો અને કેરી ખરવા પર નજર રાખો", "हल्की सिंचाई फिर शुरू करें; भुनगा और फल गिरने पर नज़र रखें"),
 "Second feeding as advised for your soil; protect the flush": ("તમારી જમીન માટે ભલામણ પ્રમાણે બીજો ખાતર ડોઝ; નવી ફૂટનું રક્ષણ કરો", "अपनी मिट्टी के लिए सिफ़ारिश के अनुसार दूसरी खाद; नई पत्तियों को बचाएँ"),
 "Shoots mature": ("ડાળીઓ પાકટ થાય", "टहनियाँ पकती हैं"),
 "Steady moisture; harvest mature fruit with a short stalk": ("ભેજ સરખો રાખો; પાકટ કેરી ટૂંકા ડીંટા સાથે ઉતારો", "नमी एक-सी रखें; पके फल छोटे डंठल के साथ तोड़ें"),
 "Tell us your tree age and what you see in the orchard. Two minutes, no cost, and you get a plan for this month.":
   ("ઝાડની ઉંમર અને બગીચામાં શું દેખાય છે તે જણાવો. બે મિનિટ, કોઈ ખર્ચ નહીં, અને આ મહિનાનો પ્લાન મળે.", "पेड़ की उम्र और बाग़ में क्या दिख रहा है, बताएँ. दो मिनट, कोई ख़र्च नहीं, और इस महीने का प्लान मिलेगा."),
 "Timing shifts with location and weather. South Gujarat often flowers earlier than Saurashtra and Kutch.":
   ("સમય વિસ્તાર અને હવામાન પ્રમાણે બદલાય છે. દક્ષિણ ગુજરાતમાં ઘણી વાર સૌરાષ્ટ્ર અને કચ્છ કરતાં વહેલો મોર આવે છે.", "समय जगह और मौसम के अनुसार बदलता है. दक्षिण गुजरात में अक्सर सौराष्ट्र और कच्छ से पहले बौर आता है."),
}


def link_text(h, lg):
    """<a ...>Text</a> -> same tag with translated text (and mango-site links in the page's language)."""
    m = re.fullmatch(r'(<a [^>]*>)(.*?)(</a>)', h, re.S)
    if not m or m.group(2) not in T: return None
    tag = m.group(1)
    if "mangofarming.in/check/" in tag: tag = tag.replace("lang=en", "lang=" + lg)
    return tag + T[m.group(2)][0 if lg == "gu" else 1] + m.group(3)


def para(h, lg):
    i = 0 if lg == "gu" else 1
    hrefs = re.findall(r'<a [^>]*>', h)
    if h.startswith("Every orchard is different."):
        chk, prod, kit = hrefs[0].replace("lang=en", "lang=" + lg), hrefs[1], hrefs[2]
        return [f'દરેક બગીચો અલગ હોય છે. {chk}mangofarming.in</a> પરની મફત ચકાસણી ઝાડની ઉંમર, જાત અને તમને શું દેખાય છે તે પૂછે છે, પછી આ મહિનાનો પ્લાન આપે છે. તે ગુજરાતી, હિન્દી અને અંગ્રેજીમાં છે. મોર અને ફળ બેસવાના સમયે ઉત્પાદનની મદદ જોઈએ તો {prod}Immunity Mango Special</a> અથવા {kit}Immunity Mango Kit</a> જુઓ, હંમેશાં લેબલ પ્રમાણે.',
                f'हर बाग़ अलग होता है. {chk}mangofarming.in</a> पर मुफ़्त जाँच पेड़ की उम्र, किस्म और आपको क्या दिख रहा है, यह पूछती है, फिर इस महीने का प्लान देती है. यह हिन्दी, गुजराती और अंग्रेज़ी में है. बौर और फल लगने के समय उत्पाद की मदद चाहिए तो {prod}Immunity Mango Special</a> या {kit}Immunity Mango Kit</a> देखें, हमेशा लेबल के अनुसार.'][i]
    if h.startswith("For the soil fertilizer dose"):
        a = hrefs[0].replace("/en/mango-fertilizer/", "/mango-fertilizer/" if lg == "gu" else "/hi/mango-fertilizer/")
        return [f'ઝાડની ઉંમર પ્રમાણે જમીનમાં આપવાના ખાતરનો ડોઝ NHB, TNAU અને KAU પ્રમાણે, તમારા બગીચા માટે કેલ્ક્યુલેટર સાથે, {a}ઉંમર પ્રમાણે આંબાનું ખાતર</a> પાનામાં જુઓ.',
                f'पेड़ की उम्र के अनुसार मिट्टी में देने वाली खाद की मात्रा NHB, TNAU और KAU के अनुसार, आपके बाग़ के लिए कैलकुलेटर के साथ, {a}उम्र के अनुसार आम की खाद</a> पेज पर देखें.'][i]
    if h.startswith("Read the complete"):
        g, pm, dp = hrefs
        return [f'આંબાની ખેતીની સંપૂર્ણ {g}માર્ગદર્શિકા</a>, અને {pm}ભૂકી છારો</a> તથા {dp}આંબાના રોગ અને જીવાત</a> વિશેની માર્ગદર્શિકા વાંચો.',
                f'आम की खेती की पूरी {g}गाइड</a>, और {pm}पाउडरी मिल्ड्यू</a> तथा {dp}आम के रोग और कीट</a> की गाइड पढ़ें.'][i]
    if h.startswith("We make organic fertilizer"):
        who, fac, q, bio, mf, bulk = hrefs
        return [f'અમે શિહોર, ભાવનગરમાં અમારી પોતાની ફેક્ટરીમાં ઓર્ગેનિક ખાતર, બાયો ખાતર અને બાયોસ્ટિમ્યુલન્ટ બનાવીએ છીએ. {who}અમે કોણ છીએ અને શું બનાવીએ છીએ</a> તે વાંચો, અમારી {fac}ફેક્ટરી અને R&amp;D</a> અને {q}મંજૂરીઓ</a> જુઓ, અથવા {bio}બાયોસ્ટિમ્યુલન્ટ</a> અને {mf}ઉત્પાદન સુવિધા</a>ની વિગત તથા {bulk}જથ્થાબંધ પુરવઠા</a> માટે બિઝનેસ સાઇટ પર જાઓ.',
                f'हम शिहोर, भावनगर में अपनी फ़ैक्टरी में जैविक खाद, जैव उर्वरक और बायोस्टिमुलेंट बनाते हैं. {who}हम कौन हैं और क्या बनाते हैं</a> पढ़ें, हमारी {fac}फ़ैक्टरी और R&amp;D</a> और {q}मंज़ूरियाँ</a> देखें, या {bio}बायोस्टिमुलेंट</a> और {mf}उत्पादन सुविधा</a> की जानकारी तथा {bulk}थोक आपूर्ति</a> के लिए बिज़नेस साइट पर जाएँ.'][i]
    return None


added = {"gu": {}, "hi": {}}
for h in MISSING:
    for lg in ("gu", "hi"):
        v = T[h][0 if lg == "gu" else 1] if h in T else (link_text(h, lg) or para(h, lg))
        if v is None: raise SystemExit("no translation for: " + h[:120])
        assert h.count("<a ") == v.count("<a "), h[:80]
        added[lg][h] = v
for lg, m in added.items():
    f = os.path.join(HERE, lg + ".json"); d = json.load(open(f, encoding="utf-8")); d.update(m)
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(lg, len(m), "added")
