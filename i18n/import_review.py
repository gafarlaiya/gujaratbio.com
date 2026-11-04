# Import corrected review files (gujarati_partNN_of_MM.tsv / hindi_partNN_of_MM.tsv: id, page, english, translation)
# into i18n/tr/<lang>1_review_NN.tsv, which merge.py applies after the original batches.
# Usage: python3 i18n/import_review.py <file> [<file> ...]   then: python3 i18n/merge.py && python3 build.py
import csv, json, os, re, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
keys = json.load(open(os.path.join(ROOT, "src1.json"), encoding="utf-8"))
TAGS = lambda s: sorted(re.findall(r"<[^>]+>", s))
KEEP = ["Immunity", "WhatsApp"]
for f in sys.argv[1:]:
    name = os.path.basename(f).lower()
    lang = "gu" if name.startswith("guj") else "hi" if name.startswith("hin") else None
    if not lang: print("skip (name must start with gujarati or hindi):", f); continue
    part = re.search(r"part(\d+)", name); part = part.group(1) if part else "x"
    d = json.load(open(os.path.join(ROOT, f"{lang}.json"), encoding="utf-8"))
    ok, changed, bad = [], 0, []
    with open(f, encoding="utf-8-sig", newline="") as fh:
        for row in csv.reader(fh, delimiter="\t"):   # handles plain and spreadsheet-quoted fields
            if not row or row[0].strip().lower() == "id": continue
            try: i = int(row[0]); t = row[3].strip()
            except (ValueError, IndexError): bad.append((row[:1], "bad row")); continue
            if i >= len(keys) or not t: bad.append((i, "unknown id or empty")); continue
            en = keys[i]
            if TAGS(en) != TAGS(t): bad.append((i, "HTML tags or links changed")); continue
            if any(w in en and w not in t for w in KEEP): bad.append((i, "brand word removed")); continue
            if en.startswith("<") != t.startswith("<") or en.endswith(">") != t.endswith(">"): bad.append((i, "layout order changed (number or link moved)")); continue
            if d.get(en) != t: changed += 1
            ok.append(f"{i}\t{t}")
    out = os.path.join(ROOT, "tr", f"{lang}1_review_{part}.tsv")
    open(out, "w", encoding="utf-8").write("\n".join(ok) + "\n")
    print(f"{name}: {len(ok)} lines accepted, {changed} changed, {len(bad)} rejected")
    for b in bad[:20]: print("   rejected", b)
