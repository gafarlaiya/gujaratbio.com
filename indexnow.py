#!/usr/bin/env python3
"""Tell IndexNow engines (Bing, Yandex, Seznam, Naver) about pages added or changed recently.
Usage:  python3 indexnow.py [days]      default 1 day; reads sitemap.xml lastmod dates.
Google does not use IndexNow. Use Search Console for Google."""
import re, sys, json, datetime, urllib.request
KEY = "fef7e73a0979c91804157ca615fdea01"
HOST = "www.gujaratbio.com"
days = int(sys.argv[1]) if len(sys.argv) > 1 else 1
since = (datetime.date.today() - datetime.timedelta(days=days)).isoformat()
xml = open("sitemap.xml", encoding="utf-8").read()
urls = [u for u, d in re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", xml) if d >= since]
print(f"{len(urls)} URLs changed since {since}")
if not urls: sys.exit(0)
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls[:9000]}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", body, {"Content-Type": "application/json; charset=utf-8"})
try:
    print("IndexNow answered", urllib.request.urlopen(req, timeout=30).status)
except Exception as e:
    print("IndexNow error:", e); sys.exit(1)
