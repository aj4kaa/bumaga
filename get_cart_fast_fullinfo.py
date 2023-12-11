import csv
import re
from bs4 import BeautifulSoup
from lxml import etree


def get_cart_fast_fullinfo(src, category_name):
    soup = BeautifulSoup(src, "lxml")
    wrap = soup.find("div", {"id": "productFastPreview"})
    dom = etree.HTML(str(wrap))
    full_info = []
    for inx in range(13):
        full_info.append(' ')
    try:
        href = wrap.find(class_="product-full-link").find("a").get("href").strip()
    except:
        href = "нет информации"
    try:
        name = wrap.find(class_="product-card-information").find("h1").text.strip()
    except:
        name = "нет информации"
    try:
        code = wrap.find(class_="product-main-info-code").find(class_="CopyToClipboard").text.strip()
    except:
        code = "нет информации"
    try:
        article = dom.xpath("//div[contains(text(), 'Артикул:')]/../following-sibling::div/div")
        article = article[0].text.strip()
    except:
        article = "нет информации"
    try:
        trademark = dom.xpath("//div[contains(text(), 'Торговая марка:')]/../following-sibling::div//a")
        trademark = trademark[0].text.strip()
    except:
        trademark = "нет информации"
    try:
        country = dom.xpath("//div[contains(text(), 'Страна:')]/../following-sibling::div/div")
        country = country[0].text.strip()
    except:
        country = "нет информации"
    try:
        package = dom.xpath("//div[contains(text(), 'Упаковка:')]/../following-sibling::div/div")
        package = package[0].text.strip()
    except:
        package = "нет информации"
    try:
        barcode = dom.xpath("//div[contains(text(), 'Штрихкод:')]/../following-sibling::div/div")
        barcode = barcode[0].text.strip()
    except:
        barcode = "нет информации"
    try:
        certificate = dom.xpath("//div[contains(text(), 'Сертификат:')]/../following-sibling::div/div")
        certificate = certificate[0].text.strip()
    except:
        certificate = "нет информации"
    try:
        balance = dom.xpath("//div[contains(text(), 'Остаток:')]/../following-sibling::div/div")
        balance = balance[0].text.strip()
    except:
        balance = "нет информации"
    try:
        if wrap.find(class_="priceRecuction"):
            price = wrap.find(class_="price-regular").text.strip()
            price = ''.join(re.findall(r'[\d.]', price))
        else:
            price = wrap.find(class_="product-price").text.strip()
            price = ''.join(re.findall(r'[\d.]', price))
    except:
        price = "нет информации"
    try:
        info = wrap.find(class_="product-description-wrap").find_all(class_="product-description-item")
        arr = []
        for i in info:
            arr.append(": ".join(i.text.split(":")))
        info = ", ".join(arr)
    except:
        info = "нет информации"
    try:
        image_link = wrap.find(class_="ezoom").find("img").get("src")
    except:
        image_link = "нет информации"

    full_info[0] = href
    full_info[1] = name
    full_info[2] = code
    full_info[3] = article
    full_info[4] = trademark
    full_info[5] = country
    full_info[6] = package
    full_info[7] = barcode
    full_info[8] = certificate
    full_info[9] = balance
    full_info[10] = price
    full_info[11] = info
    full_info[12] = image_link

    with open(f'data_csv/{category_name}.csv', 'a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                full_info
            )
        )
