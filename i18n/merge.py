# Merge numbered translation batches (i18n/tr/<lang>_*.tsv, lines "N<TAB>text", "=" keeps English) into i18n/<lang>.json
import json, os, re, sys, glob
ROOT = os.path.dirname(os.path.abspath(__file__))
def hrefs(s): return sorted(re.findall(r'href="([^"]*)"', s))
for lang in ("gu", "hi"):
    out = {}
    jf = os.path.join(ROOT, f"{lang}.json")
    if os.path.exists(jf): out = json.load(open(jf, encoding="utf-8"))
    for src in sorted(glob.glob(os.path.join(ROOT, "src*.json"))):
        keys = json.load(open(src, encoding="utf-8"))
        tag = os.path.basename(src)[3:-5]          # src1.json -> "1"
        for en in keys:                              # file names shown on photo/video placeholders stay as they are
            if re.fullmatch(r"[\w.-]+\.(webp|mp4|jpg|png)", en): out.setdefault(en, en)
        for f in sorted(glob.glob(os.path.join(ROOT, "tr", f"{lang}{tag}_*.tsv"))):
            for ln, line in enumerate(open(f, encoding="utf-8")):
                line = line.rstrip("\n")
                if not line.strip() or line.startswith("#"): continue
                n, t = line.split("\t", 1)
                en = keys[int(n)]
                t = en if t == "=" else t
                if hrefs(en) != hrefs(t): print("LINK MISMATCH", lang, f, n, en[:60]); continue
                out[en] = t
    json.dump(out, open(jf, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(lang, len(out))
