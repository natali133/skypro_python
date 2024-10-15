from selenium.webdriver.common.by import By



class shopBag:

    def  __init__(self, browser):
        self.driver = browser
        
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.driver.find_element(By.ID, "checkout").click()

    
    
    def add_pay_phorm(self):
    
        self.driver.find_element(By.ID, "first-name").send_keys("Maxim")
        self.driver.find_element(By.ID, "last-name").send_keys("Boev")
        self.driver.find_element(By.ID, "postal-code").send_keys("173023")
        self.driver.find_element(By.ID, "continue").click()

        



