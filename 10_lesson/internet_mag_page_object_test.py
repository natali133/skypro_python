import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.InternetMagPage import InternetMagPage

@allure.id("Internet_mag")
@allure.epic("Интернет магазин")
@allure.severity(allure.severity_level.BLOCKER)
@allure.story("Покупка товаров")
@allure.feature("CREATE")
@allure.title("Выбор товара и оплата товара")

def test_form_internet_mag():
    with allure.step("Открытие страницы"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной с  классом InternetMagPage"):
        internet_mag_page = InternetMagPage(driver)

    with allure.step("Авторизация пользователя"):
        internet_mag_page.authorization("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        to_be = internet_mag_page.add_products()

    with allure.step("Переход в корзину"):
        internet_mag_page.go_to_cart()

    with allure.step("Ввод личных данных"):
        internet_mag_page.personal_data("Aleksandr", "Kalashnikov", "346880")

    with allure.step("Получение  стоимости товара" ):
        as_is = internet_mag_page.total_cost()

    with allure.step("Проверка, что ожидаемая и фактическая стоимость равны"):
        assert as_is == to_be

    with allure.step("Закрытие браузера"):
        internet_mag_page.close()