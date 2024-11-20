from time import sleep
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# Запустить сайт
driver.get("http://the-internet.herokuapp.com/inputs")

# Ввод значения "1000" в поле ввода
search_field = "input[type='number']"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
sleep(1)
search_input.send_keys("1000")
sleep(1)
search_input.clear()
sleep(1)
search_input.send_keys("999")


sleep(1)

# Закрыть браузер
driver.quit()