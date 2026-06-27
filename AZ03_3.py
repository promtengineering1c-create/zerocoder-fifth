FILENAME = 'divans.csv'

class Provider:
    __data:  list

    def __init__(self):
        self.__data = []

    @property
    def get_data(self):
        if not self.__data:
            self.scrape()
        return self.__data
    
    def scrape(self):
        import requests
        from bs4 import BeautifulSoup
    
        URL = "https://www.divan.ru/category/pramye-divany"
        response = requests.get(URL)
        page = BeautifulSoup(response.text, 'html.parser')

        products = page.find_all('div', class_='ProductCardMain-module__4dYtKq__infoContainer')

        for product in products:
            try:
                price = product.find('meta', itemprop="price").get('content').strip()
            
                self.__data.append(int(price))
            except AttributeError:
                pass

class Saver_CSV:
    def save(self, list, filename):
        import csv
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file, delimiter=';')  
            csv_writer.writerow(['Цена'])  
            csv_writer.writerows([[item] for item in list])
                         
class Parser:
    def __init__(self, provider, saver):
        self.__provider = provider
        self.__saver = saver

    def parse(self, filename):
        self.__saver.save(self.__provider.get_data, filename)

class Analyzer:
    def analyze(self, filename):
        import pandas as pd
        df = pd.read_csv(filename)
        return df.mean()

class Plotter:
    def plot(self, filename):
        import pandas as pd
        import matplotlib.pyplot as plt
        
        data = pd.read_csv(filename)

        plt.hist(data)
        plt.ylabel('Ось  Y')
        plt.xlabel('Ось  X')
        plt.title('Гистограмма')

        plt.show()

parser = Parser(Provider(), Saver_CSV())
parser.parse(FILENAME)

print('Среднее значение: ')
print(Analyzer().analyze(FILENAME))

Plotter().plot(FILENAME)

