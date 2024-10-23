from selenium.webdriver.common.by import By




class shopMain:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/")

    

    def shop_auth(self):
        
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    
    
    def shop_add(self):
    
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        