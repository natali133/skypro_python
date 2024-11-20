from time import sleep
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


# Запустить сайт
driver.get("http://uitestingplayground.com/classattr/")


# Повторить действия три раза
for _ in range(3):
    button = driver.find_element(By.XPATH,
                                 "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    button.click()
    sleep(1)
    driver.switch_to.alert.accept()

driver.quit()