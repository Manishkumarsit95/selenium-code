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
#driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
WindowChild = driver.window_handles
driver.switch_to.window(WindowChild[1])
time.sleep(5)
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(WindowChild[0])
assert "Opening a new window" == (driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
