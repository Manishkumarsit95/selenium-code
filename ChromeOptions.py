from selenium import webdriver
chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("--start-maximized") # Maximized the window
chrome_Options.add_argument("headless") # Run Chrome backend
chrome_Options.add_argument("--ignore-certificate-error") # ignore some certificate
chrome_Options.add_argument("--disable-popup-blocking") # Disable popup
driver = webdriver.Chrome(executable_path="C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe",options=chrome_Options)
print(driver.title)