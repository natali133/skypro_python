from time import sleep
from selenium.webdriver.common.by import By

class authCheck:

    def  __init__(self, browser):
        self.driver = browser

    
    def color_zip(self):
        
        color_Zip = self.driver.find_element(By.CSS_SELECTOR, "#zip-code"
                                             ).value_of_css_property('background-color')
        return color_Zip                                           
        
    def color_adress(self):    
        
        color_Adress = self.driver.find_element(By.CSS_SELECTOR, "#address"
                                                ).value_of_css_property('background-color')
        return color_Adress

    def color_email(self):
        color_Email = self.driver.find_element(By.CSS_SELECTOR, "#e-mail"
                                               ).value_of_css_property('background-color')
        return color_Email
    
    def color_phone(self):
        color_Phone = self.driver.find_element(By.CSS_SELECTOR, "#phone"
                                               ).value_of_css_property('background-color')
        return color_Phone
    
    def color_city(self):
        color_City = self.driver.find_element(By.CSS_SELECTOR, "#city"
                                              ).value_of_css_property('background-color')
        return color_City
    
    def color_country(self):
        color_Country = self.driver.find_element(By.CSS_SELECTOR, "#country"
                                                 ).value_of_css_property('background-color')
        return color_Country
    
    def color_jobpos(self):
        color_Jobpos = self.driver.find_element(By.CSS_SELECTOR, "#job-position"
                                                ).value_of_css_property('background-color')
        return color_Jobpos
    
    def color_company(self):
        color_Company = self.driver.find_element(By.CSS_SELECTOR, "#company"
                                                 ).value_of_css_property('background-color')
        return color_Company
    

        
    
    
    
    
        
        