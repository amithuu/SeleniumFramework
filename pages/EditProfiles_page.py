import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from base.Basedriver import BaseDriver

class EditProfiles(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locators
    ADD_BUTTON = "//*[@id = 'root']/div[2]/div[2]/div/div/div[2]/div[1]//button"

    """GETTERS"""
    def get_addbutton(self):
        return self.element_to_click(By.XPATH, self.ADD_BUTTON)
    
    """SETTERS"""
    
    def click_addbutton(self):
        self.get_addbutton().click()

    def editprofiles(self):
        self.dashboard()
        self.edit_profile()
        for i in range(1, 11):
            self.click_addbutton()
        self.save()
