import time

from selenium import webdriver
#Chrome driver
from selenium.webdriver.chrome.service import Service
#----Chrome----
from selenium.webdriver.common.by import By

service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_Obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
Countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a") # Css path for common dropdown value
# CSS - li[class='ui-menu-item'] a
# Note:- Countries Variable defeined so it will store the drop downvalues
print(len(Countries)) # Countries variable output is List
for Country in Countries:
    if Country.text == "India":
        Country.click()
        break
#print(driver.find_element(By.ID, "autosuggest").text) # not working for variable drop down value because after referesh
# it will not visible so use ".get_attribute("value")
#print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) # Print the value
assert (driver.find_element(By.ID, "autosuggest").get_attribute("value")) == "India"


