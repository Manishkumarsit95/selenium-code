from selenium import webdriver
#Chrome driver
from selenium.webdriver.chrome.service import Service
#----Chrome----
from selenium.webdriver.common.by import By
name = "Manish Loves H"
service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_Obj)
# Checkbox----------------------------
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert # Switch the mode from driver to alert
alertText = alert.text # What ever test message on alert will store
print(alertText)
assert name in alertText # validation
alert.accept() # To Positive response accepted
#alert.dismiss() to negative response reject