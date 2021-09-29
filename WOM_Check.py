from selenium import webdriver
from datetime import datetime
import time
import easygui

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r'E:\OneDrive\Piton\chromedriver.exe', options=options)

#Load login
login = open('login.txt').read().splitlines()

#Get webpage
driver.get('https://www.wom.co/customer/consumption/')

#Click options

driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()

x = driver.find_element_by_xpath("/html/body/div[3]/main/div[3]/div/div[2]/div[2]/div[1]/form/div[1]/input[2]")
x.clear()
x.send_keys(login[0])

driver.find_element_by_xpath('/html/body/div[3]/main/div[3]/div/div[2]/div[2]/div[1]/form').click()

driver.find_element_by_xpath('/html/body/div[3]/main/div[3]/div/div[2]/div[2]/div[1]/form/div[2]/div/input').send_keys(login[1])

driver.find_element_by_css_selector('#send2').click()

driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[2]/div/div[2]/ul/li[2]/a').click()

#Usage calculations

use = driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/p/span").text
limitdate = driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div[2]/p[2]").text

today = datetime.today().strftime('%d-%m-%Y')
start = datetime.strptime(today, "%d-%m-%Y")
end = datetime.strptime(limitdate, "%d/%m/%Y")

diff = end.date() - start.date()
use1 = use.replace(" GIGAS","")

left = float(120 - float(use1))
gbxday = float(left/(float(diff.days)))
answer = str(round(gbxday, 2))

print("Quedan: " + str(left) + " GB")
print("Para usar en " + str(diff.days) + " días.")
print("GB por día: " + answer)

#MesaggeBox
easygui.msgbox("Uso: " + str(use1) + " GB" + "\n" + "Quedan: " + str(left) + " GB" + "\n" + "Para usar en " + str(diff.days) + " días." +  "\n" + "GB por día: " + answer, title="WOM Checker")

#Driver close
driver.close()
