from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("tomsmith")

# input_name.send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# input_pass.send_keys("SuperSecretPassword!")
button = driver.find_element(By.TAG_NAME, "button").click()
sleep(2)

driver.quit()