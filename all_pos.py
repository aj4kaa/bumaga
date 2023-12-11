import json
import csv

with open("data/all_products_dict.json") as file:
    all_category = json.load(file)



with open(f'data_csv/key.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            'kek'
        )
    )
for category_name, category_href in all_category.items():
    key = []
    key.append(category_name)
    with open(f'data_csv/key.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                key
            )
        )



print(key)
