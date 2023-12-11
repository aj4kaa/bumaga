import requests
from bs4 import BeautifulSoup
import json
from transliterate import slugify

url = "https://bumaga-s.ru/%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F/index"
# url = "https://bumaga-s.ru"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "cookie": "_ym_uid=1701268131644558941; _ym_d=1701268131; supportOnlineTalkID=Jox0KL4TenieQxZE4E82qhsgik9I2QHb; viewMode=gallery; PHPSESSID=oc0s5pls5827em17mcn7sngcm1; region=3; cinit=1; region_confirm=1; _ym_isad=1; locality=45"
}

req = requests.get(url, headers=headers)
src = req.text

with open("data/index.html", "w", encoding="utf-8") as file:
    file.write(src)

# with open("data/index.html", encoding="utf-8") as file:
#     src = file.read()

soup = BeautifulSoup(src, "lxml")
all_products_href = soup.select("ul.category-box-list>li>a")

all_products_dict = {}
for item in all_products_href:
    text = item.text
    rep = [",", " ", "-", "'", "/", '+']
    for i in rep:
        if i in text:
            text = text.replace(i, "_")
    rep = ["__", "___", "____"]
    for i in rep:
        if i in text:
            text = text.replace(i, "_")
    for i in rep:
        if i in text:
            text = text.replace(i, "_")
    link = item.get("href")
    print(f"{text}, {link}")
    all_products_dict[text] = link


with open("data/all_products_dict.json", "w", encoding="cp1251") as file:
    json.dump(all_products_dict, file, indent=4, ensure_ascii=False)

print(all_products_dict)

