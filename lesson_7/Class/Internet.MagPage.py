import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from Class.InternetMag import InternetMagPage

@allure.id("Internet_mag")
@allure.epic("Интернет магазин")
@allure.severity("blocker")
@allure.story("Покупка товаров")
@allure.feature("CREATE")
@allure.title("Выбор товара, работа с корзиной и оплата")
@allure.suite("Тесты на работу с интернет-магазином")
def test_form_internet_mag():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной, которая хранит экзампляр класса InternetMagPage"):
        internet_mag_page = InternetMagPage(driver)

    internet_mag_page.authorization("standard_user", "secret_sauce")
    
    
    to_be = internet_mag_page.calculate_expected_total() 
    
    internet_mag_page.add_products()  
    internet_mag_page.go_to_cart()
    internet_mag_page.personal_data("Artem", "Vologdin", "301298")
    as_is = internet_mag_page.total_cost()

    with allure.step("Проверить, что ожидаемая и фактическая стоимость равны"):
        assert as_is == to_be

    internet_mag_page.close()