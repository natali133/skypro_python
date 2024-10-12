import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  
        self.driver.maximize_window()

    def delay(self, delay_seconds=45):
        self.driver.find_element(By.ID, "delay").send_keys(delay_seconds)

    def sum_of_the_numbers(self):
        self._driver.find_element(By.XPATH, '//span[contains(text(),"7")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(),"+")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(),"8")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(),"=")]').click()

    def get_result(self):
        result_element = self.driver.find_element(By.ID, "sciOutPut")
        return int(result_element.text)

    def close_driver(self):
        self.driver.quit()

@allure.id("Calculator")
@allure.epic("Калькулятор")
@allure.severity("blocker")
@allure.suite("Тесты на работу с калькулятором")
@allure.story("Выполнение математических операций на калькуляторе")
@allure.title("Сложение чисел на калькуляторе")
@allure.feature("CREATE")
def test_form_calculator():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной, которая хранит экзампляр класса CalculatorPage"):
        calculator_page = CalculatorPage(driver)

    with allure.step("Установка задержки"):
        calculator_page.delay()  

    with allure.step("Сложение чисел"):
        calculator_page.sum_of_the_numbers()

    with allure.step("Получение результата"):
        result = calculator_page.get_result()

    with allure.step("Проверка результата"):
        assert result == 15, "Результат сложения неверный"  

    calculator_page.close_driver()