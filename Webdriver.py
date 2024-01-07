from selenium import webdriver
#Chrome driver
from selenium.webdriver.chrome.service import Service
#----Chrome----
#service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe");
#driver = webdriver.Chrome(service=service_Obj)
#----Firefox-----
#service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\geckodriver-v0.32.0-win-aarch64\\geckodriver.exe");
#driver = webdriver.Firefox(service=service_Obj)
#-----Edge---
service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\edgedriver_win64\\msedgedriver.exe");
driver = webdriver.Edge(service=service_Obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://www.rahulshettyacademy.com/mentorship")
driver.back()
driver.refresh()
driver.forward()
driver.close()
