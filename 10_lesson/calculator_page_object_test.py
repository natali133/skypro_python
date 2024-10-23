import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage

@allure.feature("Калькулятор")
@allure.story("Операция сложения")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест операция сложения в калькуляторе")
@allure.description("Этот тест проверяет, правильно ли калькулятор выполняет сложение.")
def test_addition_operation():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        calculator_page = CalculatorPage(driver)

    with allure.step("Установка задержки"):
        calculator_page.delay()

    with allure.step("Выполнение операции сложения"):
        calculator_page.perform_addition()

    with allure.step("Проверка результата"):
        assert calculator_page.get_result(), "Ожидаемый результат сложения: 15"

    with allure.step("Закрытие браузера"):
        calculator_page.close_driver()