import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class PersonalDataPage:
    """
    Класс для взаимодействия с веб-страницей персональных данных.

    Атрибуты:
        driver (WebDriver): Веб-драйвер для взаимодействия с браузером.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует PersonalDataPage с веб-драйвером.

        Args:
            driver (WebDriver): Веб-драйвер для взаимодействия с браузером.
        """
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    @allure.step("Заполнение формы с персональными данными")
    def personal_data(self, name: str, last: str, address: str, email: str, phone: int, city: str, country: str, job: str, company: str) -> None:
        """
        Заполняет форму с персональными данными.

        Args:
            name (str): Имя пользователя.
            last (str): Фамилия пользователя.
            address (str): Адрес пользователя.
            email (str): Электронная почта пользователя.
            phone (int): Телефон пользователя.
            city (str): Город пользователя.
            country (str): Страна пользователя.
            job (str): Должность пользователя.
            company (str): Компания пользователя.
        """
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(str(phone))
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').clear()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)

        button = self.driver.find_element(By.CSS_SELECTOR, 'button.btn')
        ActionChains(self.driver).move_to_element(button).perform()
        button.click()

    @allure.step("Проверка, что поле ZIP-кода окрашено в красный цвет, если оно не заполнено")
    def zip_code_red(self) -> bool:
        """
        Проверяет, окрашено ли поле ZIP-кода в красный цвет, если оно не заполнено.

        Returns:
            bool: True, если поле окрашено в красный цвет, иначе False.
        """
        zip_code_color = self.driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        return zip_code_color == 'rgba(248, 215, 218, 1)'

    @allure.step("Проверка, что другие поля окрашены в зеленый цвет, если они заполнены")
    def other_fields_green(self) -> bool:
        """
        Проверяет, окрашены ли другие поля в зеленый цвет, если они заполнены.

        Returns:
            bool: True, если все поля окрашены в зеленый цвет, иначе False.
        """
        other_fields = ["#first-name", "#last-name", "#address", "#e-mail",
                        "#phone", "#city", "#country", "#job-position", "#company"]
        for field in other_fields:
            field_color = self.driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color")
            if field_color != 'rgba(209, 231, 221, 1)':
                return False
        return True

    @allure.step("Закрытие драйвера веб-браузера")
    def close_driver(self) -> None:
        """
        Закрывает драйвер веб-браузера.
        """
        self.driver.quit()