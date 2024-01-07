import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
message = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
var = message.split("at ")
car = var[1].split(" with")
time.sleep(5)
#var = message.split("at")[1].strip().split(" ")[0]
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(car[0])
driver.find_element(By.ID, "password").send_keys(car[0])
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)