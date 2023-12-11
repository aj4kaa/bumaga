import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from proxy_auth_data import login, password
from auth_data import login_bumaga, password_bumaga
from get_cart_fast_fullinfo import get_cart_fast_fullinfo
import json
import time
import csv

url = "https://bumaga-s.ru/"

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@213.166.75.58:9856"
    }
}

driver = webdriver.Chrome(options=options, seleniumwire_options=proxy_options,
                          service=Service(ChromeDriverManager().install()))
driver.maximize_window()


def auth(login_bumaga, password_bumaga):
    driver.get(url=url)
    time.sleep(5)
    wrap = driver.find_element(By.CSS_SELECTOR, "div.otherRegionText")
    hidden_btn = wrap.find_element(By.CSS_SELECTOR, "a")
    ActionChains(driver).move_to_element(wrap).click(hidden_btn).perform()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "div.auth").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'input#login').send_keys(login_bumaga)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys(password_bumaga)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'div.buttons-item-left').click()
    time.sleep(10)
    # src = driver.page_source
    # with open(f"data/123213213.html", 'w', encoding="utf-8") as file:
    #     file.write(src)
    print(login_bumaga, password_bumaga)


def get_card_html(category_name, category_href):
    print(category_name)
    try:
        driver.get(url=category_href)
        time.sleep(3)
        products_count = int(driver.find_element(By.CSS_SELECTOR, 'span.productsCount').text)
        while True:
            items = driver.find_elements(By.CSS_SELECTOR, 'div.products-item')
            driver.execute_script("arguments[0].scrollIntoView();", items[-1])
            time.sleep(2)
            try:
                driver.find_element(By.CSS_SELECTOR, 'div.show-more').click()
            except:
                print(len(items))
            if len(items) == products_count:
                # src = driver.page_source
                # with open(f"data/{category_name}.html", 'w', encoding="utf-8") as file:
                #     file.write(src)
                with open(f'data_csv/{category_name}.csv', 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow(
                        (
                            "Cсылка на карточку",
                            "Наименование",
                            "Код товара",
                            "Артикул",
                            "Торговая марка",
                            "Страна",
                            "Упаковка",
                            "Штрихкод",
                            "Сертификат",
                            "Остаток",
                            "Цена",
                            "Характеристики",
                            "Ссылка на изображение",

                        )
                    )
                    writer.writerow(
                        (
                            {category_name}
                        )
                    )
                all_card = driver.find_elements(By.CSS_SELECTOR, 'div.products-item')
                for item in all_card:
                    driver.execute_script("arguments[0].scrollIntoView();", item)
                    wrap = item.find_element(By.CSS_SELECTOR, "div.product-top")
                    hidden_btn = item.find_element(By.CSS_SELECTOR, "i.fast-preview")
                    ActionChains(driver).move_to_element(wrap).click(hidden_btn).perform()
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ezoom")))
                    # src = driver.page_source
                    get_cart_fast_fullinfo(driver.page_source, category_name)
                    # with open(f"data/src.html", 'w', encoding="utf-8") as file:
                    #     file.write(src)
                    driver.find_element(By.CSS_SELECTOR, 'a.close').click()
                break
    except Exception as ex:
        print(ex)


def main():
    with open("data/all_products_dict.json") as file:
        all_categories = json.load(file)
    auth(login_bumaga, password_bumaga)
    for category_name, category_href in all_categories.items():
        get_card_html(category_name, category_href)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    main()
