import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement


def test_handle_dropdown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/")
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT, "SignUp Form").click()
    # Like in java, create an object of Select class to work with dropdowns created with select tag
    gender_dropdown = Select(driver.find_element(By.NAME, "sgender"))
    # selecting with dropdown by value
    gender_dropdown.select_by_value("male")
    assert gender_dropdown.first_selected_option.text == "Male"
    print("Selected Male")
    time.sleep(3)
    gender_dropdown.select_by_index(3)
    print("Selected the index 3")
    time.sleep(3)
    gender_dropdown.select_by_visible_text("Female")
    assert gender_dropdown.first_selected_option.text == "Female"
    print("Selected the visible text ", "Female")
    gender_list = (driver.find_elements(By.XPATH, "//select[@name='sgender']/option"))
    available_options = gender_dropdown.options
    filter_gender_search(available_options, "Male").click()
    time.sleep(2)


def filter_gender_search(list_web_element:list, gender: str) -> WebElement:
    """
    in the method declaration, we're explicitly specifying that list_web_element must be a list and gender must be string using the :
    -> represents what we want to return and we're mentioning we want to return WebElement class
    :param list_web_element:
    :param gender:
    :return:
    """
    for index in range(len(list_web_element)):
        current_element = list_web_element.__getitem__(index)
        current_gender = current_element.text
        if current_gender == gender:
            print("Selected the ", current_gender, " gender")
            time.sleep(2)
            return current_element
