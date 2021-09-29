from selenium import webdriver
import webbrowser
from datetime import datetime
import time
import os


#Load login
login = open('login.txt').read().splitlines()

driver = webdriver.Chrome()
driver.set_window_size(1360, 968)

driver.get('https://www.wom.co/customer/consumption/')
time.sleep(1)

#Click
driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()

x = driver.find_element_by_xpath("/html/body/div[3]/main/div[3]/div/div[2]/div[2]/div[1]/form/div[1]/input[2]")

x.clear()
x.send_keys(login[0])
time.sleep(1)
x.clear()
x.send_keys(login[0])

time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/main/div[3]/div/div[2]/div[2]/div[1]/form/div[2]/div/input').send_keys(login[1])
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/main/div[3]/div/div[2]/div[2]/div[1]/form/div[4]/div[1]/div[2]/button').click()

driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[2]/div/div[2]/ul/li[2]/a').click()


use = driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/p/span").text

limitdate = driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div[2]/p[2]").text

# d2 = limitdate
# 
# d1 = datetime.strptime(d1, "%d-%m-%Y")
# d2 = datetime.strptime(d2, "%d-%m-%Y")
# 
# delta = d2 - d1



print(use)
print(limitdate)
# print(delta.days)

