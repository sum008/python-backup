'''
Created on Jul 11, 2020

@author: Sumit
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
import pyautogui as p

import time

def automate():
    
    rom="crdroid"
    link="https://forum.xda-developers.com/redmi-note-7/development"
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--window-size=1920x1080") 
#     driver = webdriver.Chrome(options=chrome_options,executable_path="D:\chromedriver.exe")
    driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
    driver.get(link)
    
    u=driver.current_url
    source=requests.get(u).text
    soup=BeautifulSoup(source,"html5lib")
    lis=soup.select("div[class='thread-row']")
    l=""
    for i in lis: #span[class='responsive-text-show']
        a=i.select("div[class='info-cell']")
        if "Today" and rom in str(a) :
            l="https://forum.xda-developers.com"+str(a[0].find("a"))[9:len(str(a[0].find("a")))-11]
            print(l)
            time.sleep(1)
            
            break
    return l
          
    
l=automate() 
driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
driver.get(l)
# driver.fullscreen_window()
# driver.find_element_by_xpath("//input[@type='tel']").send_keys("7210570625")
# time.sleep(1)
# driver.find_element_by_xpath("//div[@id='next-step']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//textarea[@id='sms-message']").send_keys("Update is here ,link :"+l)
# time.sleep(1)
# p.leftClick(947, 521)
# driver.find_element_by_xpath("//div[@id='next-step']").click()
    