import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://qavbox.github.io/demo/")
assert "QAVBOX" in driver.title
driver.find_element(By.LINK_TEXT,"SignUp Form")
driver.save_screenshot(r"C:\Users\mages\PycharmProjects\PythonSeleniumBasics\src\Screenshots\screen.png")
time.sleep(3)
driver.quit()