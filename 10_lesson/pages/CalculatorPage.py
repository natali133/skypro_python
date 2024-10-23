import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    """
    Класс для взаимодействия с веб-страницей калькулятора.

    Атрибуты:
        _driver (webdriver): Веб-драйвер для взаимодействия с браузером.
    """

    def __init__(self, driver: webdriver) -> None:
        """
        Инициализирует CalculatorPage с веб-драйвером.

        Args:
            driver (webdriver): Веб-драйвер для взаимодействия с браузером.
        """
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.step("Установка задержки перед выполнением следующего шага")
    def delay(self) -> None:
        """
        Устанавливает задержку перед выполнением следующего шага.
        """
        input_delay = self._driver.find_element(By.CSS_SELECTOR, 'input[id="delay"]')
        input_delay.clear()
        input_delay.send_keys('3')

    @allure.step("Ввод числа в калькулятор")
    def click_element(self, num: str) -> None:
        """
        Вводит число в калькулятор.

        Args:
            num (str): Число, которое нужно ввести в калькулятор.
        """
        self._driver.find_element(By.XPATH, f'//span[contains(text(),"{num}")]').click()

    @allure.step("Выполнение операции сложения")
    def perform_addition(self) -> None:
        """
        Выполняет операцию сложения чисел 7 и 8.
        """
        self.click_element("7")
        self.click_element("+")
        self.click_element("8")
        self.click_element("=")

    @allure.step("Получение результата сложения")
    def get_result(self) -> bool:
        """
        Получает результат сложения.

        Returns:
            bool: True, если результат сложения равен 15, иначе False.
        """
        WebDriverWait(self._driver, 48).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
        return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text == "15"

    @allure.step("Закрытие драйвера веб-браузера")
    def close_driver(self) -> None:
        """
        Закрывает драйвер веб-браузера.
        """
        self._driver.quit()