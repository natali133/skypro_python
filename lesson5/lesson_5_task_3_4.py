from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Запустить сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

#В модальном окне нажмите на кнопку Сlose.
driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

sleep(10)

driver.quit()