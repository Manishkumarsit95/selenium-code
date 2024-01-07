import time

from selenium import webdriver
#Chrome driver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#----Chrome----
#from selenium.webdriver.common.by import By
service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_Obj)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://glbrandstore.foxboxrewards.com/")
driver.find_element(By.CSS_SELECTOR, ".header-search").click()
driver.find_element(By.XPATH, "//div[@class='row header-row header-row-top']").send_keys("BO")
#driver.find_element(By.CSS_SELECTOR, ".header-search").click()





