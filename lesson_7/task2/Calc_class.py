from time import sleep
from selenium.webdriver.common.by import By


class Calculator:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


    def Calc_test(self):

        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(45)
        self.driver.find_element(By.XPATH, "//span[text() = '7']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '+']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '8']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '=']").click()
        sleep(45)
        

