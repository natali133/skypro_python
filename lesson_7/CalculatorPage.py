import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Class.Calculator import CalculatorPage  

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
        calculator_page.delay(45)  

    with allure.step("Сложение чисел"):
        calculator_page.sum_of_the_numbers()

    with allure.step("Получение результата"):
        result = calculator_page.get_result()  

    
    calculator_page.close_driver()