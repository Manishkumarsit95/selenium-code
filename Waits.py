import time

from selenium import webdriver
#Chrome driver
from selenium.webdriver.chrome.service import Service
#----Chrome----
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service=service_Obj)
driver.implicitly_wait(5) # maximum 5 sec take any website to upload the but if you put more hrs
# then take every steps 15 sec wait
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
Results = driver.find_elements(By.XPATH, "//div[@class='products']/div") #Exception : list value came so Implicity wait not work
Count = (len(Results))
assert Count > 0
for result in Results:
    result.find_element(By.XPATH,"div/button").click() #Chaining of web element
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(2)
#Sum Validation
Prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in Prices:
    sum = sum + int(price.text)  #(price.text is given the str value so need to convert
    # in to integer so do sum - int(price.text))
print(sum)
TotalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == TotalAmount
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(5)
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
#driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
