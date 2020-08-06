from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
element_s=[]
while not len(element_s)>0:
    try:
        element_s=driver.find_elements_by_xpath("//div[@class='X7YrQ']//div[@tabindex='-1']//div[@class='_2UaNq']//div[@class='KgevS']//div[@class='_3H4MS']")
    except:
        continue
    
for i in element_s:
    if i.text=="Stuff":
        i.click()
    print(i.text)
element_s1=[]
element_s1=driver.find_elements_by_xpath("//div[@class='FTBzM']//div[@class='_1zGQT _2ugFP message-out tail']//div[@class='-N6Gq']//div[@class='copyable-text']//div[@class='_12pGw EopGb']//span[@dir='ltr']")
for i in element_s1:
    if i.text.__contains__("hackerearth"):
        i.click()
    print(i.text)
    

print(driver.title)
# driver.close()