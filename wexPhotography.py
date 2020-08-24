from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#This option stops the browser from popping up
opts = webdriver.ChromeOptions()
opts.headless =True

driver = webdriver.Chrome("./chromedriver")

def wex_photography_cameras():
    print('Wex Photography')
    print('-' * 10)

    driver.get(f'https://www.wexphotovideo.com/used-cameras/#esp_category_cf=Manufacturer&esp_category_filter_Manufacturer=Fuji')
    brand_cameras = driver.find_elements_by_class_name('listing-product')
    
    print(len(brand_cameras))
