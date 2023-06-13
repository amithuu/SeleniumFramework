import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.Languages_page import Language

class Carrier(Language):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    def carrier(self):
        """Add Carrier Summary"""
        self.driver.set_window_size(1200, 1400)
        self.driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        generate_suggestion = self.element_to_click(By.XPATH, "//button[text()='Generate Suggestions']")
        generate_suggestion.click()
        time.sleep(12)
        for a in range(1, 4):
            self.element_to_click(By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div{a}//button")
            time.sleep(1)



