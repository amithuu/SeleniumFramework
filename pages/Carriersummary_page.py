import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.Languages_page import Language


class Carrier(Language):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    generate_suggestion = "//button[text()='Generate Suggestions']"

    """GETTERS"""
    def get_generatesuggestion(self):
        return self.element_to_click(By.XPATH, self.generate_suggestion)

    """SETTERS"""
    def click_generatesuggestion(self):
        self.get_generatesuggestion().click()

    def click_onchoices(self):
        for a in range(1, 4):
            self.element_to_click(By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div{a}//button")
            time.sleep(1)
    def carrier(self):
        self.driver.set_window_size(1200, 1400)
        self.page_down()
        time.sleep(2)
        self.click_generatesuggestion()
        time.sleep(12)
        self.click_onchoices()
        self.save()


