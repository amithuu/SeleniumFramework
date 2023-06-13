import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver

class Language(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait
    # Locators
    location_button_in_edit_profile = "//*[text()='Languages']"

    def getLocationpath(self):
        return self.element_to_click(By.XPATH, self.location_button_in_edit_profile)

    def location_button(self):
        self.getLocationpath().click()


    def lang_drop(self, user_language):
        lan = self.element_to_click(By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div/div[1]//input")
        lan.send_keys(user_language)
        lan.send_keys(Keys.TAB)

    def profiency(self, user_proficiency):
        prof = self.element_to_click(By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div/div[2]//input")
        prof.send_keys(user_proficiency)
        prof.send_keys(Keys.TAB)

    def add_button(self):
        add = self.element_to_click(By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[2]/div[2]//button")
        add.click()
        time.sleep(2)



