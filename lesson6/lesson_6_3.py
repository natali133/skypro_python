from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
# Перейдите на страницу

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape"))
# дождаться появления 4-й картинки
)

src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src") 
# Получите значение атрибута src у 3-й картинки.

print(src) # вывести в консоль

driver.quit()