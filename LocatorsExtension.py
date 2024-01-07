from selenium import webdriver
#Chrome driver
from selenium.webdriver.chrome.service import Service
#----Chrome----
from selenium.webdriver.common.by import By

service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service=service_Obj)

driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT, "Forgot password?").click() # Link text - Forget password?
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com") # xpath for email- //form/div[1]/input"
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Mk@1234")# Css - form div:nth-child(2) input
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Mk@1234") # Css - through #ID
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
# 2nd way Exact same text
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
