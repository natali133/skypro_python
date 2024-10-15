import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from task1.Auth_class import AuthPhorm
from task1.Auth_Chek import authCheck
from task2.Calc_class import Calculator
from task2.Calc_Res import Calcresult
from task3.Shop_main_class import shopMain
from task3.Shop_Bag_class import shopBag
from task3.Shop_price import shopPrice

# форма авторизации
@pytest.mark.test_positive
def test_auth_phorm():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    auth_phorm = AuthPhorm(browser)
    auth_phorm.add_auth_phorm()    
# проверка цвета полей формы    
    auth_check = authCheck(browser)
    color_Zip = auth_check.color_zip()
    assert color_Zip == "rgba(248, 215, 218, 1)"
    color_Adress = auth_check.color_adress()    
    assert color_Adress == "rgba(209, 231, 221, 1)"
    color_Email = auth_check.color_email()    
    assert color_Email == "rgba(209, 231, 221, 1)"
    color_Phone = auth_check.color_phone()
    assert color_Phone == "rgba(209, 231, 221, 1)"
    color_City = auth_check.color_city()
    assert color_City == "rgba(209, 231, 221, 1)"
    color_Country = auth_check.color_country()
    assert color_Country == "rgba(209, 231, 221, 1)"
    color_Jobpos = auth_check.color_jobpos()
    assert color_Jobpos == "rgba(209, 231, 221, 1)"
    color_Company = auth_check.color_company()
    assert color_Company == "rgba(209, 231, 221, 1)"        
    browser.quit()

# тест калькулятора
@pytest.mark.test_positive
def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    Calc = Calculator(browser)
    Calc.Calc_test()
# проверка результата калькулятора    
    Calc_Res = Calcresult(browser)    
    result = Calc_Res.result()    
    assert result == "15"
    browser.quit()

# тест магазина
@pytest.mark.test_positive
def test_shop_main():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    shop_main = shopMain(browser)
    shop_main.shop_auth()
    shop_main.shop_add()
# работа в корзине   
    shop_bag = shopBag(browser)    
    shop_bag.add_pay_phorm()
# проверка стоимости
    shop_price = shopPrice(browser)
    price = shop_price.shop_price()    
    assert price == "58.29"        
    browser.quit()









