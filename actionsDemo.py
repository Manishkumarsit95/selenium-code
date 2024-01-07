import time

from selenium import webdriver
#Chrome driver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
#----Chrome----
from selenium.webdriver.common.by import By

service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service=service_Obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.double_click(driver.find_element) - for double click
#action.click_and_hold(driver.find_element()) - for long hold
#action.context_click(driver.find_element()) - for right click
#action.drag_and_drop()- for drag and drop
#action.move_to_element(driver.find_element(By.ID,"")) for Hover
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(5)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
