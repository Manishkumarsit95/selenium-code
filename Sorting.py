import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service = service_Obj)
driver.implicitly_wait(5)
BrowserVeggieShorted = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# 1. Click on the Common Header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
#time.sleep(5)
# 2. Collect all veggie name -> BrowserSortedVeggieList
VeggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in VeggieWebElements:
    BrowserVeggieShorted.append(ele.text)
OriginalBrowserSortedList = BrowserVeggieShorted.copy()
# 3. Sort the BrowserSortedVeggieList-> NewShortedList
BrowserVeggieShorted.sort()
assert BrowserVeggieShorted == OriginalBrowserSortedList