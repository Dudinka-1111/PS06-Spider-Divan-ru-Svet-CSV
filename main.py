import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/perm/category/lyustry"
driver.get(url)
time.sleep(20)

lyustries = driver.find_elements(By.CLASS_NAME, 'LlPhw')

parsed_data = []

for lyustry in lyustries:
    try:
        name = lyustry.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        price = lyustry.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
        url = lyustry.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')

    except:
        print("произошла ошибка при парсинге")
        continue

    parsed_data.append([name, price, url])

driver.quit()

with open("divan.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название люстры', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)