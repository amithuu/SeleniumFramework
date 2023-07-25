import time
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver

class Causes(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # LOCATORS
    CAUSES_EDITPROFILE = "//*[text()='Causes']"
    CAUSES_ICON = "//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[{i}]//span[1]"

    """GETTERS"""
    def get_causes_editprofile(self):
        return self.element_to_click(By.XPATH, self.CAUSES_EDITPROFILE)

    """SETTERS"""
    def click_causes_editprofiles(self):
        self.get_causes_editprofile().click()

    def select_causes(self):
        for i in range(1, 9):
            self.element_to_click(By.XPATH, f"//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[{i}]//span[1]").click()
            time.sleep(1)

    def causes(self):
        self.click_causes_editprofiles()
        self.select_causes()
        self.save()
