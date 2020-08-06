from selenium import webdriver
# from pywinauto import application
# 
# app = application.Application()
# app.start("C:/Users/Sumit/Downloads/Win.exe",wait_for_idle=False)

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        "debugConnectToRunningApp": 'false',
        "app": r"C:/windows/system32/calc.exe"
    })

driver.find_element_by_name("Menu").click()
driver.find_element_by_name('Standard Calculator').click()

driver.find_element_by_name("Display is 0").send_keys("45")
driver.find_element_by_name("Plus").click()
driver.find_element_by_name("Display is 45").send_keys("15")
driver.find_element_by_name("Equals").click()

# view_menu_item.click()
# view_menu_item.find_element_by_name('Scientific').click()
# 
# view_menu_item.click()
# view_menu_item.find_element_by_name('History').click()
# 
# window.find_element_by_id('132').click()
# window.find_element_by_id('93').click()
# window.find_element_by_id('134').click()
# window.find_element_by_id('97').click()
# window.find_element_by_id('138').click()
# window.find_element_by_id('121').click()

driver.close()