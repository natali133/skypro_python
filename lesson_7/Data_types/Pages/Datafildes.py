from selenium.webdriver.common.by import By

class DataFild:
    def __init_ (self.browser):
        self.browser = browser

    # Находим необходимые поля для заполнения
    def find_fields(self):
        self.class_first_name = (By.ID, "first-name")
        self.class_last_name = (By.ID, "last-name")
        self.class_address = (By.ID, "address")
        self.class_email = (By.ID, "e-mail")
        self.class_phone = (By.ID, "phone")
        self.class_zip_code = (By.ID, "zip-code")
        self.class_city = (By.ID, "city")
        self.class_country = (By.ID, "country")
        self.class_qob_position = (By.ID, "qob-position")
        self.class_company = (By.ID, "company")

    # Получить значение классов полей
    def get_class_first_name(self):
        return self.browser.find_element(*self.class_first_name).get_attribute("class")
    def get_class_last_name(self):
        return self.browser.find_element(*self.class_last_name).get_attribute("class")
    def get_class_address(self):
        return self.browser.find_element(*self.class_address).get_attribute("class")
    def get_class_email(self):
        return self.browser.find_element(*self.class_email).get_attribute("class")
    def get_class_phone(self):
        return self.browser.find_element(*self.class_phone).get_attribute("class")
    def get_class_zip_code(self):
        return self.browser.find_element(*self.class_zip_code).get_attribute("class")
    def get_class_city(self):
        return self.browser.find_element(*self.class_city).get_attribute("class")
    def get_class_country(self):
        return self.browser.find_element(*self.class_country).get_attribute("class")
    def get_class_qob_position(self):
        return self.browser.find_element(*self.class_qob_position).get_attribute("class")
    def get_class_company(self):
        return self.browser.find_element(*self.class_company).get_attribute("class")
    
    
    
    
    
        