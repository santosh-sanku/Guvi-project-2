from multiprocessing.connection import wait
from tkinter import PAGES
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
import csv

class santosh:

    url = "https://www.flipkart.com/"
    driver = webdriver.Firefox()

    def open_web(self):
        self.driver.get(self.url)
        time.sleep(3) 
        #not now
        self.driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/button').click()
        time.sleep(2) 
        #search tab
        self.driver.find_element(by=By.CLASS_NAME,value='_3704LK').send_keys("laptop")
        time.sleep(2) 
        #search button
        self.driver.find_element(by=By.CLASS_NAME,value='L0Z3Pu').click()
        time.sleep(3) 
        #core i5
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[4]/div[2]/div[1]/div[2]/div/label/div[2]').click()
        time.sleep(3)
        #1TB drop down
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[10]/div/div').click() 
        #1TB
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[10]/div[2]/div/div[1]/div/label').click()
        time.sleep(3) 
        #RAM CAPACITY DROP DOWN
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[18]/div/div').click()
        #8GB RAM
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[18]/div[2]/div/div[1]/div/label/div[2]').click()
        time.sleep(3)
        #STORAGE TYPE DROP DOWM
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[24]/div/div').click() 
        #HDD
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[24]/div[2]/div/div[2]/div/label/div[2]').click()
        time.sleep(3) 
        #price low to high
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[3]').click()
        time.sleep(3)
        return self.driver.current_url

    def lap_scrap(self):
        url_new = self.open_web()

        description = []
        processor = []
        ram = []
        harddisk = []
        prices = []

        pages = list(range(1,2))
        for page in pages:
            data = requests.get(url_new).text
            soup = BeautifulSoup(data,'lxml')
            #print(soup.prettify())

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

        df = {'Title':description[slice(24)], 'processor':processor[slice(24)], 'Ram':ram[slice(24)], 'Harddisk':harddisk[slice(24)], 'Price':prices[slice(30)]}
        dataset = pd.DataFrame(data = df) #Finally merging all the features into a single dataframe 

        print(dataset)

        dataset.to_csv('fliplaptops1.csv')

        a = []
        for i in description:
            a.append(i.split()[0])

        #print(a)
        print("The top 3 brands based on low price")
        unique_list = []
        for x in a:
            if x not in unique_list:
                unique_list.append(x)
        
        print(unique_list[0:3])

        self.close_browser()

    def web_mobiles(self):
        self.driver.get(self.url)
        time.sleep(3)
        #not now
        self.driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/button').click()
        time.sleep(2) 
        #search tab
        self.driver.find_element(by=By.CLASS_NAME,value='_3704LK').send_keys("phone")
        time.sleep(2) 
        #search button
        self.driver.find_element(by=By.CLASS_NAME,value='L0Z3Pu').click()
        time.sleep(3)
        #5 brands checkbox clicking
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[5]/div/label/div[2]').click() #samsung
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[4]/div/label/div[2]').click() #realme
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[5]/div/label/div[2]').click() #poco
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[7]/div/label/div[2]').click() #MI
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[2]/input').send_keys("vivo") #more
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[3]/div/label/div[2]').click() #vivo
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[7]/div[2]/div/div[5]/div/label/div[2]').click() #6GB RAM
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[8]/div/div').click() #internal storage drop down
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[8]/div[2]/div/div[1]/div/label/div[2]').click() #128GB        
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[17]/div/div').click() #network type
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[17]/div[2]/div/div[3]/div/label/div[2]').click() #4G        
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[3]').click() #price low to high
        time.sleep(2)
        return self.driver.current_url

    def phone_scrap(self):
        new_url = self.web_mobiles()

        description1 = []
        ram1 = []
        display1 = []
        prices1 = []

        pages = list(range(1,2))
        for page in pages:
            data = requests.get(new_url).text
            soup = BeautifulSoup(data,'lxml')
            #print(soup.prettify())

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

        dataset1.to_csv('flip_mobiles1.csv')
        #sample = len(description1)
        a = []
        for i in description1:
            a.append(i.split()[0])

        #print(a)
        print("The top 3 brands based on low price")
        unique_list = []
        for x in a:
            if x not in unique_list:
                unique_list.append(x)
        
        print(unique_list[0:3])

        self.close_browser()

    def close_browser(self):
        self.driver.close()

s = santosh()
s.lap_scrap()
#s.web_mobiles()
time.sleep(5)
s.phone_scrap()
#s.open_web()