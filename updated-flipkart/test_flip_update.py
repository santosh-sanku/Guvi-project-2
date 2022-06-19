from turtle import title
import pytest
import flip_update 
from selenium import webdriver
import time
import csv
import os
import pandas as pd

obj_o = flip_update.santosh()

@pytest.mark.first
def test_firefox_url():
    web_driver = webdriver.Firefox()
    web_driver.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.hard_disk_capacity%255B%255D%3D1%2BTB&p%5B%5D=facets.system_memory%255B%255D%3D8%2BGB&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi5&p%5B%5D=facets.storage_type%255B%255D%3DHDD&sort=price_asc")
    
    web_driver.maximize_window()    
    
    title = "Laptop- Buy Products Online at Best Price in India - All Categories | Flipkart.com"
    assert title ==  web_driver.title
    time.sleep(2)
    web_driver.close()

#def test_csv_search():
    #with open("laptops.csv",'w') as csvfile:
        #csvwritter = csv.writer(csvfile)
        #csvwritter.writerow(santosh().open_fliplaptops())

@pytest.mark.second
def test_annualized():
    fname = os.path.join(os.path.dirname(__file__), 'fliplaptops.csv')
    pd.read_csv(fname)

@pytest.mark.third
def test_annualized_1():
    fname = os.path.join(os.path.dirname(__file__), 'flip_mobiles.csv')
    pd.read_csv(fname)

@pytest.mark.fourth
def test_firefox_url_1():
    web_driver = webdriver.Firefox()
    web_driver.get("https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.internal_storage%255B%255D%3D128%2B-%2B255.9%2BGB&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.ram%255B%255D%3D6%2BGB&p%5B%5D=facets.network_type%255B%255D%3D4G&sort=price_asc")
    
    web_driver.maximize_window()    
    
    title = "Phone- Buy Products Online at Best Price in India - All Categories | Flipkart.com"
    assert title ==  web_driver.title
    time.sleep(2)
    web_driver.close()

@pytest.mark.fifth
def test_close_browser():
    flip_update.santosh.close_browser(obj_o) 


