import requests
from bs4 import BeautifulSoup
import csv

data = []

URL = "https://www.divan.ru/category/pramye-divany"
response = requests.get(URL)
page = BeautifulSoup(response.text, 'html.parser')

products = page.find_all('div', class_='ProductCardMain-module__4dYtKq__infoContainer')

for product in products:
    try:
        price = product.find('meta', itemprop="price").get('content').strip()
        print(price)
    
        data.append(int(price))
    except AttributeError:
        pass

print(data)

with open(filename, 'w', newline='', encoding='utf-8') as file:
    csv_writer.writerow(['Цена']) 
    csv_writer = csv.writer(file, delimiter=';')        
    csv_writer.writerows(list)