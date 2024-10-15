from selenium.webdriver.common.by import By


class shopPrice:

    def  __init__(self, browser):
        self.driver = browser

        
    def shop_price(self):    
        res = self.driver.find_element(By.CSS_SELECTOR, "[class='summary_total_label']").text
        price = res.strip('Total: $')
        self.driver.close()
        return price
        