from time import sleep
from selenium import webdriver


#from selenium import webdriver
#options = webdriver.ChromeOptions()

#options.add_argument('--ignore-ssl-errors=yes')

#options.add_argument('--ignore-certificate-errors')


driver = webdriver.Chrome()

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#accept_insecure_certs = True

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#chrome_options = webdriver.ChromeOptions()


# Запустить сайт
driver.get (" http://uitestingplayground.com/dynamicid/")
sleep(1)
# Кликнуть на синюю кнопку(нажать) и в поле, любое место(отжать)
button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
sleep(1)
field = driver.find_element(By.CSS_SELECTOR, "div[class='container']").click()
sleep(1)
# Повторение нажатия три раза
for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
    sleep(1)
    field = driver.find_element(By.CSS_SELECTOR, "div[class='container']").click()
    
sleep(1)
# Закрыть браузер
driver.quit()