import json
import csv
from bs4 import BeautifulSoup

with open("data/all_products_dict.json") as file:
    all_categories = json.load(file)

for category_name, category_href in all_categories.items():
    with open(f"data/{category_name}.html", encoding='utf-8') as file:
        src = file.read()
    print(category_name)
    with open(f'data_csv/{category_name}.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(
            (
                "Код товара",
                "Наименование",
                "Упаковка",
                "Остаток",
                "Характеристики",
                "Цена",
                "Ссылка на изображение"
            )
        )
        writer.writerow(
            (
                {category_name}
            )
        )
    soup = BeautifulSoup(src, "lxml")
    cards = soup.find_all(class_="products-item")
    full_info = []
    for inx in range(7):
        full_info.append(' ')
    for card in cards:
        code = card.find(class_="product-code").find("span").text.strip()
        name = card.find(class_="product-name").find("span").text.strip()
        try:
            package = card.find(class_="product-unit").contents[-1].strip()
        except:
            package = " "
        balance = card.find(class_="product-free-balance").contents[-1].strip()
        try:
            info = card.find(class_="product-short-description").find_all("li")
            arr = []
            for i in info:
                arr.append(": ".join(i.text.split(":")))
            info = ", ".join(arr)
        except:
            info = "новинка"
        price = card.find(class_="product-price").find("span", class_="price-regular").text.strip()
        image_link = card.find(class_="product-image").find("img").get("src")
        # print(f"Код- {code}\nНаименование- {name}\nУпаковка- {package}\nОстаток- {balance}\nИнформация- {info}\nЦена- {price}\nСсылка- {image_link}")

        full_info[0] = code
        full_info[1] = name
        full_info[2] = package
        full_info[3] = balance
        full_info[4] = info
        full_info[5] = price
        full_info[6] = image_link

        with open(f'data_csv/{category_name}.csv', 'a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    full_info
                )
            )
