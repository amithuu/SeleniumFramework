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
    def get_addbutton(self, i):
        return self.element_to_click(By.XPATH, f"//*[@id = 'root']/div[2]/div[2]//div[2]/div/div[{i}]//button")
    
    """SETTERS"""
    
    def click_addbutton(self, i):
        self.get_addbutton(i).click()

    def editprofiles(self):
        # self.dashboard()
        self.edit_profile()
        for i in range(1, 15):
            self.click_addbutton(i)
        self.save()
