import time

from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver

class EditProfiles(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locators
    # ADD_BUTTON = "//*[@id = 'root']/div[2]/div[2]/div/div/div[2]/div[1]//button"
    ADD_BUTTON = "//*[@id = 'root']/div/div[2]/div[2]/div/div[2]/div/div[3]//button"
    ADD_BUTTON_ONBOARDING = "//*[@id='root']/div[2]//div[{i}]//button"

    """GETTERS"""
    def get_addbutton(self, i):
        return self.element_to_click(By.XPATH, f"//*[@id = 'root']/div/div[2]/div[2]/div/div[2]/div/div[{i}]//button")

    def get_addbutton_onbaodring(self, i):
        return self.element_to_click(By.XPATH, f"//*[@id='root']/div[2]//div[{i}]//button")
    
    """SETTERS"""

    def click_addbutton_onboarding(self):
        for i in range(1, 17):
            self.get_addbutton_onbaodring(i).click()
            time.sleep(1)

    def click_addbutton(self):
        for i in range(1, 17):
            self.get_addbutton(i).click()
            time.sleep(1)

    def editprofiles(self, user):
        if user == "new":
            self.click_addbutton_onboarding()
            self.save_next()
            self.dashboard()
        else:
            self.edit_profile()
            self.click_addbutton()
            self.save()

