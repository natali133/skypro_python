from time import sleep
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Запустить сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
# Пять раз кликнуть на кнопку Add Element
for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()

# Собрать со страницы список кнопок Delete
add_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')

print(len(add_buttons))

# Закрыть браузер
driver.quit()

    
    

        