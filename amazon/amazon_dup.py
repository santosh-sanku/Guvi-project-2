from subprocess import list2cmdline
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time 
from bs4 import BeautifulSoup
import pandas as pd
import csv

class santosh:
    url = "https://www.amazon.in/"
    driver = webdriver.Firefox() 

    def amaze_phones(self):
        self.driver.get(self.url)
        time.sleep(3)
        s_bar = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
        s_bar.send_keys("phones")
        time.sleep(2)
        s_button = self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
        s_button.click()
        time.sleep(2) #6GB ram
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[2]/span/a/span').click()
        time.sleep(5) #128GB
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[3]/li[5]/span/a/span').click()
        time.sleep(3) #4G MOBILE
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[23]/li[2]/span/a/span').click()
        time.sleep(5) #price feature
        self.driver.find_element(by=By.XPATH,value='//*[@id="a-autoid-2"]').click() 
        time.sleep(4) #price low to high clicking
        self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div/div/ul/li[2]').click()
        time.sleep(4)
        cur_url = self.driver.current_url
        print(cur_url)
        phonenames = self.driver.find_elements(by=By.XPATH,value="//span[contains(@class,'a-color-base a-text-normal')]")
        prices = self.driver.find_elements(by=By.XPATH,value="//span[contains(@class,'price-whole')]")

        phone_names = []
        phone_price = []

        for phone in phonenames:
            #print(phone.text)
            phone_names.append(phone.text)

        print("*"*50)

        for price in prices:
            #print(price.text)
            phone_price.append(price.text)

        print(len(phone_names))
        print(len(phone_price))

        
        df = {'Description':phone_names[slice(23)], 'PhonePrice':phone_price[slice(23)]}
        dataset = pd.DataFrame(data = df) #Finally merging all the features into a single dataframe 

        print(dataset)

        dataset.to_csv('amazonmobiles.csv')

        self.close_browser()



    def amaze_laptop(self):
        self.driver.get(self.url)
        time.sleep(3)
        s_bar = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
        s_bar.send_keys("laptops")
        time.sleep(2)
        s_button = self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
        s_button.click()
        time.sleep(2) #8GB ram
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[18]/li[3]/span/a/span').click()
        time.sleep(5) #1TB HDD
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[7]/li[5]/span/a/span').click()
        time.sleep(3) #i5 processor
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[7]/span/a/span').click()
        time.sleep(5) #price feature
        self.driver.find_element(by=By.XPATH,value='//*[@id="a-autoid-2"]').click() 
        time.sleep(4) #price low to high clicking
        self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div/div/ul/li[2]').click()
        time.sleep(4)
        cur_url = self.driver.current_url
        print("*"*50)
        print(cur_url)
        print("*"*50)
        time.sleep(4)

        descriptions = []
        prices = []

        laptopnames = self.driver.find_elements(by=By.XPATH,value="//span[contains(@class,'a-color-base a-text-normal')]")
        lprices = self.driver.find_elements(by=By.XPATH,value="//span[contains(@class,'price-whole')]")

        for laptop in laptopnames:
            #print(laptop.text)
            descriptions.append(laptop.text)

        #print("*"*50)

        for price in lprices:
            #print(price.text)
            prices.append(price.text)
        
        #pages = list(range(1,3))
        #for page in pages:
            #req = requests.get("https://www.amazon.in/s?k=laptops&i=computers&rh=n%3A1375424031%2Cp_n_feature_twenty-six_browse-bin%3A27399070031%2Cp_n_pattern_browse-bin%3A8609969031%2Cp_n_feature_thirteen_browse-bin%3A12598162031&s=price-asc-rank&dc&page={}&crid=L02JH4Q5877Z&qid=1655357277&rnid=12598141031&sprefix=laptops%2Caps%2C287&ref=sr_pg_2".format(page)).text
            #soup = BeautifulSoup(req, 'lxml')

            #des = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
            #for i in range(len(des)):
                #descriptions.append(des[i].text)
            #len(descriptions)

        #price = soup.find_all('span', class_='a-offscreen')
        #for i in range(len(price)):
            #prices.append(price[i].text)
        #len(prices)

        #print(len(descriptions))
        #print(len(prices))

        
        df1 = {'Description':descriptions[slice(24)], 'Price':prices[slice(24)]}
        dataset1 = pd.DataFrame(data = df1) #Finally merging all the features into a single dataframe 

        print(dataset1)

        dataset1.to_csv('amazonlaptop.csv')

        self.close_browser()

    
    def close_browser(self):
        self.driver.close()


s = santosh()
s.amaze_phones()
time.sleep(5)
s.amaze_laptop()
