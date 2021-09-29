from selenium import webdriver
import webbrowser
import time
import os


#Load login
login = open('login.txt').read().splitlines()

driver = webdriver.Chrome()
driver.set_window_size(1360, 968)

driver.get('https://www.wom.co/customer/consumption/')
time.sleep(1)

#Click Cookies
#driver.find_element_by_xpath('//*[@id="politics_cookieCO"]/div/div[2]/a[2]').click()

print(login[0])
print(login[1])