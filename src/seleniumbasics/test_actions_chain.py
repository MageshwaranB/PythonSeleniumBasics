import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import pdb


def test_handle_test_action():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/signup/")
    driver.implicitly_wait(10)
    actions=ActionChains(driver)
    ((actions.send_keys_to_element(driver.find_element(By.ID,"username"),"Tester").
     send_keys_to_element(driver.find_element(By.ID,"email"),"Tester@test.com")).
     click(driver.find_element(By.ID,"submit"))).perform()
    time.sleep(3)
    #pytest.set_trace()
    driver.switch_to.alert.accept()
#there's no particular method to navigate to different url in python, so we can use get method
    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    right_click=driver.find_element(By.XPATH,"//span[contains(text(),'right click')]")
    actions.context_click(right_click).send_keys(Keys.ARROW_DOWN).pause(2).send_keys(Keys.ENTER).perform()
    alert_message=driver.switch_to.alert.text
    print(alert_message)
    assert alert_message.__contains__("edit")
    driver.switch_to.alert.accept()
    time.sleep(2)