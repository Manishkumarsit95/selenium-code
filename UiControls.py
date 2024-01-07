from selenium import webdriver
#Chrome driver
from selenium.webdriver.chrome.service import Service
#----Chrome----
from selenium.webdriver.common.by import By

service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_Obj)
# Checkbox----------------------------
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']") #XPath - //input[@type='checkbox']
for checkbox in Checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
"""RadioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']") # XPath - //input[@type='radio']
for RadioButton in RadioButtons:  # not used the for loop because we know that radio button doesnot change 
    if RadioButton.get_attribute("value") == "radio2":
        RadioButton.click()
        assert RadioButton.is_selected()
        break"""
"""RadioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton") # CSS - .radioButton
for RadioButton in RadioButtons:
    if RadioButton.get_attribute("value") == "radio2":
        RadioButton.click()
        assert RadioButton.is_selected()
        break""" # use below program for radio button
RadioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
RadioButtons[2].click()
assert RadioButtons[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "show-textbox").click()