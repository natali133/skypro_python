from time import sleep
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# Запустить сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(1)

#В модальном окне нажмите на кнопку Сlose.
driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

sleep(1)

driver.quit()