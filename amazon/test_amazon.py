import csv
import pytest
from amaze_dup import santosh
from selenium import webdriver
import time
import os
import pandas as pd

@pytest.mark.first
def test_firefox_url():
    web_driver = webdriver.Firefox()
    web_driver.get("https://www.amazon.in/s?k=laptops&i=computers&rh=n%3A1375424031%2Cp_n_feature_twenty-six_browse-bin%3A27399070031%2Cp_n_pattern_browse-bin%3A8609969031%2Cp_n_feature_thirteen_browse-bin%3A12598162031&s=price-asc-rank&dc&crid=30RVQGLAKFPWI&qid=1655371505&rnid=12598141031&sprefix=laptops%2Caps%2C667&ref=sr_st_price-asc-rank&ds=v1%3Akyg%2BpWcAQ7RKpQONJJF6LL1nPEZ8KIqFPkZ0JWxowb0")
    #web_driver.get(santosh.amaze_phones.cur_url)
    
    web_driver.maximize_window()    
    
    title = "Amazon.in : laptops"
    assert title ==  web_driver.title
    time.sleep(2)
    web_driver.close()

@pytest.mark.second
def test_firefox_url_1():
    web_driver = webdriver.Firefox()
    web_driver.get("https://www.amazon.in/s?k=phones&i=electronics&rh=n%3A1805560031%2Cp_n_feature_seven_browse-bin%3A16757454031%2Cp_n_feature_eight_browse-bin%3A8561112031%2Cp_n_feature_five_browse-bin%3A8561106031&dc&crid=11M5LJ0A1JIJ7&qid=1655372384&rnid=1484936031&sprefix=phones%2Caps%2C273&ref=sr_nr_p_n_feature_five_browse-bin_2&ds=v1%3AHgjHuruLCJ0QC7wcwkIikzLjSpbPoAieThxMUQ5QkfQ")
    #web_driver.get(santosh.amaze_phones.cur_url)
    
    web_driver.maximize_window()    
    
    title = "Amazon.in : phones"
    assert title ==  web_driver.title
    time.sleep(2)
    web_driver.close()

@pytest.mark.third
def test_annualized():
    fname = os.path.join(os.path.dirname(__file__), 'amazonlaptop.csv')
    pd.read_csv(fname)

@pytest.mark.fourth
def test_annualized_1():
    fname = os.path.join(os.path.dirname(__file__), 'amazonmobiles.csv')
    pd.read_csv(fname)

#def test_closebrowser():
    #amazon_dup.santosh.close_browser()
