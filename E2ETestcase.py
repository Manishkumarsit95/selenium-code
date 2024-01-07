import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
# Xpath - //a[text()='Shop'] , 2nd xpath - //a[contains(@href,'shop')] CSS- Selector- a[href='/angularpractice/shop']
# Css - a[href*='shop']
driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']").click()
# Xpath for all the product list - //div[@class='card h-100']
Products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in Products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait(driver,20) #Explicit Wait
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
SuccessText = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(SuccessText)
assert "Success! Thank you!" in SuccessText
driver.close()






