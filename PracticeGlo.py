import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("--ignore-certificate-errors")
chrome_Options.add_argument("--disable-popup-blocking") # Disable popup
service_obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_Options)
driver.implicitly_wait(5)

driver.get("https://glo.globallogic.com/users/profile/manish.kumar20")
driver.find_element(By.ID, "login").send_keys("manish.kumar20")
driver.find_element(By.ID, "password").send_keys("Globallogic2023!")
driver.find_element(By.XPATH, "//input[@value='LOGIN']").click()

alert = driver.switch_to.alert
time.sleep(5)
driver.find_element(By.XPATH, "//div//button[@class='close']").click()