num = 100

def call():
    num = 200

    print(num)
call()

stu_De = {1:"naresh", 1:"tttt", 3:"mk",4:"te", 5:"Ra", 6:"mok"}
print(stu_De)
print(stu_De[5])

#stu_De[1] = "rammm"
print(stu_De)
print(stu_De[1])
#output of - tttt
from selenium import webdriver
from selenium.webdriver.chrome.service import service
service_obj = service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#xpath for 1st name - //input[@name='firstname']

# - //spam[@class='_5k_3'][1]




