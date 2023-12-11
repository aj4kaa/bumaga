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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from proxy_auth_data import login, password
from get_cart_fast_fullinfo import get_cart_fast_fullinfo
import json
import time
import csv

# url = 'https://bumaga-s.ru/%D1%82%D0%BE%D0%B2%D0%B0%D1%80/%D0%90%D0%BA%D0%B2%D0%B0%D1%80%D0%B5%D0%BB%D1%8C_%D1%85%D1%83%D0%B4%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F_21_%D1%86%D0%B2%D0%B5%D1%82_2_6%D0%BC%D0%BB_%D0%93%D0%B0%D0%BC%D0%BC%D0%B0_%D0%A1%D1%82%D0%B0%D1%80%D1%8B%D0%B9_%D0%BC%D0%B0%D1%81%D1%82%D0%B5%D1%80_%D0%9F%D0%B0%D0%BB%D0%B8%D1%82%D1%80%D0%B0_%D0%90%D0%BD%D0%B0%D1%81%D1%82%D0%B0%D1%81%D0%B8%D0%B8_%D0%9B%D0%BE%D0%B1%D1%83%D0%B7_%D0%BA%D1%8E%D0%B2%D0%B5%D1%82%D1%8B_%D0%BC%D0%B5%D1%82%D0%B0%D0%BB%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%83%D0%BF%D0%B0%D0%BA%D0%BE%D0%B2%D0%BA%D0%B0_200622_3121'
#
#
# useragent = UserAgent()
# options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={useragent.random}")
# proxy_options = {
#     "proxy": {
#         "https": f"http://{login}:{password}@213.166.75.58:9856"
#     }
# }
#
# driver = webdriver.Chrome(options=options, seleniumwire_options=proxy_options, service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
# driver.get(url=url)
# time.sleep(5)
# src = driver.page_source
# with open(f"data/test1.html", 'w', encoding="utf-8") as file:
#     file.write(src)

with open("data/test1.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
price = soup.select("div.product-price")[0].find("span", class_="price-regular").get_text()

print(price)

# driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "a#regionSetWindowBtn"))))
# if driver.find_elements(By.CSS_SELECTOR, 'a#regionSetWindowBtn'):
#     print("Login Successful")
#     modal = driver.find_element(By.CSS_SELECTOR, 'a#regionSetWindowBtn')
#     modal.click()
#     time.sleep(5)
# hidden_btn = driver.find_element(By.ID, "regionSetWindowBtn")
# ActionChains(driver).move_to_element(hidden_btn).click(hidden_btn).perform()
# time.sleep(5)
# driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "div.auth"))))
# time.sleep(5)
# try:
#     driver.find_element(By.CSS_SELECTOR, 'div.auth').click()
#     print('2')
# except:
#     print('3')
# driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "div#is_your_region>a.no_my_region"))))
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, 'input#locality_search').send_keys('краснодар')
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, 'ul.autocomplete-list').click()






