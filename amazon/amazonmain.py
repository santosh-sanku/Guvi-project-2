from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

class santosh:

    url = "https://www.amazon.in/"
    driver = webdriver.Firefox()

    def open_laptop(self):
        self.driver.get(self.url)
        time.sleep(3) # search bar
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').send_keys("laptops")
        time.sleep(2) #search button
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()
        time.sleep(2) #8GB ram
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[5]/ul[1]/li[3]/span/a/span').click()
        time.sleep(2) #1TB HDD
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[6]/li[5]/span/a/span').click()
        time.sleep(2) #i5 processor
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[2]/li[6]/span/a/span').click()
        time.sleep(2) 
        #clicking the top 5 brands
        #lenovo
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[3]/ul/li[2]/span/a/span').click()
        time.sleep(2) #hp
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[3]/ul/li[3]/span/a/span').click()
        time.sleep(2) #Dell
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[3]/ul/li[4]/span/a/span').click()
        time.sleep(2) # acer
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[3]/ul/li[5]/span/a/span').click()
        time.sleep(2) #asus
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[3]/ul/li[6]/span/a/span').click()
        time.sleep(2) #price feature
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/span/div/h1/div/div[2]/div/div/form/span/span/span').click() 
        time.sleep(3) #price low to high clicking
        self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div/div/ul/li[2]').click()
        time.sleep(3)
        return self.driver.current_url

    def lap_scrap(self):
        url_new = self.open_laptop()

        description = []
        prices = []

        pages = list(range(1,2))
        for page in pages:
            data = requests.get(url_new).text
            soup = BeautifulSoup(data,'lxml')

            desc = soup.find_all('span',class_='a-size-medium a-color-base a-text-normal')
            for i in range(len(desc)):
                description.append(desc[i].text)
                len(description)

            price = soup.find_all('span',class_='a-price-whole')
            for i in range(len(price)):
                prices.append(price[i].text)
                len(prices)

        print(len(description))
        print(len(prices))

        df1 = {'Description':description[slice(24)], 'Price':prices[slice(24)]}
        dataset1 = pd.DataFrame(data = df1) #Finally merging all the features into a single dataframe 

        print(dataset1)

        dataset1.to_csv('amazonlaptop.csv')

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

    def open_phones(self):
        self.driver.get(self.url)
        time.sleep(3) # search bar
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').send_keys("phones")
        time.sleep(2) #search button
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()
        time.sleep(2) #6GB ram
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[2]/span/a/span').click()
        time.sleep(5) #128GB
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[3]/li[5]/span/a/span').click()
        time.sleep(3) #4G MOBILE
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[23]/li[2]/span/a/span').click()
        time.sleep(5)        
        #price feature
        self.driver.find_element(by=By.XPATH,value='//*[@id="a-autoid-2"]').click() 
        time.sleep(3) #price low to high clicking
        self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div/div/ul/li[2]').click()
        time.sleep(3) 
        #clicking the top 5 brands of our choice
        #oppo
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[3]/ul/li[2]/span/a/span').click()
        time.sleep(3) #samsung
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[3]/ul/li[3]/span/a/span').click()
        time.sleep(3) #realme
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[3]/ul/li[4]/span/a/span').click()
        time.sleep(3) #redmi
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[3]/ul/li[5]/span/a/span').click()
        time.sleep(3) #vivo
        self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[3]/ul/li[6]/span/a/span').click()
        time.sleep(3)
        return self.driver.current_url

    def phone_scrap(self):
        url_new = self.open_laptop()

        description = []
        prices = []

        pages = list(range(1,2))
        for page in pages:
            data = requests.get(url_new).text
            soup = BeautifulSoup(data,'lxml')
            #print(soup.prettify())

            desc = soup.find_all('span' , class_='a-size-medium a-color-base a-text-normal')
            for i in range(len(desc)):
                description.append(desc[i].text)
                len(description)

            price = soup.find_all('span' , class_='a-price-whole')
            for i in range(len(price)):
                prices.append(price[i].text)
                len(prices)

        print(len(description))
        print(len(prices))

        
        df = {'Description':description[slice(23)], 'PhonePrice':prices[slice(23)]}
        dataset = pd.DataFrame(data = df) #Finally merging all the features into a single dataframe 

        print(dataset)

        dataset.to_csv('amazonmobiles.csv')

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


    def close_browser(self):
        self.driver.close()


s = santosh()
#s.open_laptop()
s.lap_scrap()
time.sleep(5)
#s.open_phones()
s.phone_scrap()