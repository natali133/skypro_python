import pytest
from selenium import webdriver


pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver. maximize_window()    
    yield driver
    driver.quit()