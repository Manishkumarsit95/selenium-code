from selenium import webdriver
#Chrome driver
from selenium.webdriver.chrome.service import Service
#----Chrome----
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_Obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service=service_Obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Locator are find by 6 ways
# 1. ID, 2. Xpath, 3.CSSSelector, 4. classname, 5. Name, 6. LinkText
driver.find_element(By.NAME, "email").send_keys("mk@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath:-  //tagname[@attribute = 'value'] - xpath of submit button:- //input[@type = 'submit']
# Css :-   tagname[attribute = 'value'] - Css selector :- input[name = 'name']
# N0te - #ID value and .Classname is Css selector
# if Xpath is found multiple matching Element then you need to use index value.
# X path :- (//tagname[@attribute = 'value'])[indexvalue]
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Harshita Janu") # Css- input[name = 'name']
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click() # Css by #ID - #inlineRadio1
# Static Drop Down (need import- from selenium.webdriver.support.select import Select)
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()
driver.find_element(By.XPATH, "//input[@type = 'submit']").click() # Xpath- //input[@type = 'submit']
Message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(Message)
assert "Success" in Message
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("Harshu Again love you")
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()
#driver.close()

