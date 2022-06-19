from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pandas as pd
import time

class santosh:

    #driver = webdriver.Firefox()
    

    def open_fliplaptops(self):
        #self.driver.get(self.url)
        #time.sleep(3)
        description = []
        processor = []
        ram = []
        harddisk = []
        prices = []

        pages = list(range(1,2))
        for page in pages:
            req = requests.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on&p%5B%5D=facets.hard_disk_capacity%255B%255D%3D1%2BTB&p%5B%5D=facets.system_memory%255B%255D%3D8%2BGB&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi5&p%5B%5D=facets.storage_type%255B%255D%3DHDD&sort=price_asc&page=1".format(page)).text
            soup = BeautifulSoup(req, 'lxml')

            desc = soup.find_all('div' , class_='_4rR01T')
            for i in range(len(desc)):
                description.append(desc[i].text)
            len(description)

            commonclass = soup.find_all('li' , class_='rgWa7D')
            for i in range(0,len(commonclass)):
                p = commonclass[i].text
                if("Core i5" in p):
                    processor.append(p)
                elif("8 GB" in p):
                    ram.append(p)
                elif("1 TB HDD" in p):
                    harddisk.append(p)

            price = soup.find_all('div' , class_='_30jeq3 _1_WHN1')
            for i in range(len(price)):
                prices.append(price[i].text)
                len(prices)
        
        #print(len(description))
        #print(len(prices))
        #print(len(processor))
        #print(len(ram))
        #print(len(harddisk))

        df = {'Description':description[slice(24)], 'processor':processor[slice(24)], 'Ram':ram[slice(24)], 'Harddisk':harddisk[slice(24)], 'Price':prices[slice(24)]}
        dataset = pd.DataFrame(data = df) #Finally merging all the features into a single dataframe 

        print(dataset)

        dataset.to_csv('laptops.csv')

    def open_flipmobiles(self):
        #self.driver.get(self.url)
        #time.sleep(3)
        description1 = []
        ram1 = []
        display1 = []
        prices1 = []

        pages = list(range(1,2))
        for page in pages:
            req = requests.get("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.internal_storage%255B%255D%3D128%2B-%2B255.9%2BGB&p%5B%5D=facets.network_type%255B%255D%3D4G&p%5B%5D=facets.ram%255B%255D%3D6%2BGB&sort=price_asc&page=1".format(page)).text
            soup = BeautifulSoup(req, 'lxml')

            desc = soup.find_all('div' , class_='_4rR01T')
            for i in range(len(desc)):
                description1.append(desc[i].text)
            len(description1)

            commonclass = soup.find_all('li' , class_='rgWa7D')
            for i in range(0,len(commonclass)):
                p = commonclass[i].text
                if("6 GB RAM | 128 GB ROM" in p):
                    ram1.append(p)
                elif("Display" in p):
                    display1.append(p)

            price = soup.find_all('div' , class_='_30jeq3 _1_WHN1')
            for i in range(len(price)):
                prices1.append(price[i].text)
                len(prices1)
        
        #print(len(description1))
        #print(len(prices1))
        #print(len(ram1))
        #print(len(display1))

        df1 = {'Description':description1[slice(24)], 'Ram':ram1[slice(24)], 'Display':display1[slice(24)], 'Price':prices1[slice(24)]}
        dataset1 = pd.DataFrame(data = df1) #Finally merging all the features into a single dataframe 

        print(dataset1)

        dataset1.to_csv('flipmobiles.csv')


s = santosh()
s.open_fliplaptops()
print("*************************************")
s.open_flipmobiles()
