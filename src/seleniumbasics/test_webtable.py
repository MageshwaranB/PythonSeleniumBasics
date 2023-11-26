import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_handle_web_tables():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/")
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT,"WebTable").click()
    table=driver.find_element(By.ID,"table01")
    headers=table.find_elements(By.TAG_NAME,"tbody")
    cells=table.find_elements(By.TAG_NAME,"td")
    rows=table.find_elements(By.TAG_NAME,"tr")

    print("Values in the header")
    for header in headers:
        print(header.text)

    count=0
    print("Values in the table: ")
    for cell in cells:
        print(cell.text)
    for i in range(len(rows)):
        columns=rows[i].find_elements(By.TAG_NAME,"td")
        for j in range(len(columns)):
            if columns[j].text=="TFS":
                columns[0].click()
                text=columns[0].text
                print("Successfully has clicked "+text)
                time.sleep(3)
                count=-1

    assert count==-1