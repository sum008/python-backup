from selenium import webdriver
import time
#from_username,from_password,from_mail,to_mail,file_name
def automate():
    element=[]
    driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
    driver.get("https://Gmail.com/")
    driver.find_element_by_xpath("//input[@type='email'][@class='whsOnd zHQkBf']").send_keys("sk4641230@gmail.com")
    driver.find_element_by_xpath("//div[@role='button'][@id='identifierNext']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@type='password'][@class='whsOnd zHQkBf']").send_keys("fuckoffichangedmypassword%%%")
    driver.find_element_by_xpath("//div[@role='button'][@id='passwordNext']").click()
    while len(element)<=0:
        try:
            element=driver.find_elements_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3'][@role='button']")
        except:
            continue
    element[0].click()
    
    
automate()
    
    
    
    