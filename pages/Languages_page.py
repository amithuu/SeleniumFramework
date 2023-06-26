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
    language_drop_down = "//*[@id='root']/div[2]/div/div/div/div/div/div[1]//input"
    language_proficiency = "//*[@id='root']/div[2]/div/div/div/div/div/div[2]//input"
    language_add_button = "//*[@id='root']/div[2]/div/div/div/div/div[2]/div[2]//button"

    """GETTERS"""
    def get_Locationbutton(self):
        return self.element_to_click(By.XPATH, self.location_button_in_edit_profile)
    def get_locationdropdown(self):
        return self.element_to_click(By.XPATH, self.language_drop_down)
    def get_proficiency(self):
        return self.element_to_click(By.XPATH, self.language_proficiency)
    def get_addbutton(self):
        return self.element_to_click(By.XPATH, self.language_add_button)

    """SETTERS"""

    def click_locationbutton(self):
        self.get_Locationbutton().click()

    def enter_langdrop(self, user_language):
        self.get_locationdropdown().click()
        self.get_locationdropdown().send_keys(user_language)
        self.get_locationdropdown().send_keys(Keys.TAB)

    def enter_profiency(self, user_proficiency):
        self.get_proficiency().click()
        self.get_proficiency().send_keys(user_proficiency)
        self.get_proficiency().send_keys(Keys.TAB)

    def click_addbutton(self):
        self.get_addbutton().click()
        time.sleep(2)

    def language(self, i, user_language, user_proficiency):
        self.click_locationbutton()
        # time.sleep(5)
        self.enter_langdrop(user_language)
        self.enter_profiency(user_proficiency)
        self.click_addbutton()
        self.save()
        if i <= 1:
            self.next()
            self.back()
        else:
            self.next()


