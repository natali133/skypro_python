from selenium.webdriver.common.by import By

class Calcresult:

    def __init__(self, browser):
        self.driver = browser
        
    def result(self):       
        result = self.driver.find_element(By.CSS_SELECTOR, "[class='screen']").text

        return result    