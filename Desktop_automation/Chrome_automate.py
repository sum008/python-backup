from selenium import webdriver
from pywinauto import application
import pyautogui

pyautogui.click(30, 750)

app = application.Application()
app.start("C:/Users/Sumit/Downloads/Win.exe",wait_for_idle=False)

# 'app': 'C:\\Users\\Sumit\\AppData\\Roaming\\uTorrent\\uTorrent.exe',

driver = webdriver.Remote(command_executor='http://localhost:9999',
         desired_capabilities={
         'args': '-port 345'})

a = driver.find_elements_by_name("Microsoft Store").click()
print(len(a))