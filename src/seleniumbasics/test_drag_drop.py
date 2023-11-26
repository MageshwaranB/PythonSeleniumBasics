import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement


def test_handle_drag_n_drop():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/")
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT, "DragnDrop").click()

    # Like in Java, we have to use actions class for performing the mouse and keyboard operation including the drag and drop
    action = ActionChains(driver)
    src = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    time.sleep(1)
    action.drag_and_drop(src, target).perform()
    time.sleep(2)
    actual = driver.find_element(By.ID, "dropText").text
    assert actual == "Dropped!"
    try:
        driver.refresh()
    except StaleElementReferenceException as exception:
        target = driver.find_element(By.ID, "droppable")
        src = driver.find_element(By.ID, "draggable")
        action.click_and_hold(src).move_to_element(target).perform()

def test_handle_slider_bar():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/")
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT, "DragnDrop").click()

    # Like in Java, we have to use actions class for performing the mouse and keyboard operation including the drag and drop
    action = ActionChains(driver)
    src=driver.find_element(By.XPATH,"//div[@class='slider1']/input")
    action.click_and_hold(src).move_by_offset(30,0).release().perform()
    time.sleep(2)
