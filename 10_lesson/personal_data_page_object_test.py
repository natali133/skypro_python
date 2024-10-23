import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.PersonalDataPage import PersonalDataPage

@allure.feature ("Персональные данные")
@allure.story("Отправка формы")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Отправка  формы с валидными данными")
@allure.description("Этот тест проверяет, что форма может быть отправлена с  валидными данными")
def test_personal_data_form():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        personal_data_page = PersonalDataPage(driver)

    with allure.step("Заполнение формы персональными данными"):
        personal_data_page.personal_data(
            name="John", last="Doe", address="123 Main St", email="john.doe@example.com",
            phone=1234567890, city="New York", country="USA", job="Engineer", company="Tech Inc"
        )

    with allure.step("Проверка цвета поля ZIP-кода"):
        assert personal_data_page.zip_code_red(), "Поле ZIP-кода должно быть красным"

    with allure.step("Проверка цвета других полей"):
        assert personal_data_page.other_fields_green(), "Другие поля должны быть зелеными"

    with allure.step("Закрытие браузера"):
        personal_data_page.close_driver()