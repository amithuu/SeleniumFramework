import time
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver


class Welcome(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    carrer_profile = "//div[@id ='root']/div/div[2]/div[2]/div[1]//button"
    assessment = "//div[@id ='root']/div/div[2]/div[2]/div[2]//button"

    """GETTERS"""
    def get_carrerbutton(self):
        return self.element_to_click(By.XPATH, self.carrer_profile)

    def get_assessmentbutton(self):
        return self.element_to_click(By.XPATH, self.assessment)

    """SETTERS"""
    def click_carrerbutton(self):
        self.get_assessmentbutton().click()

    def click_assessmentbutton(self):
        self.get_assessmentbutton().click()

    def welcomepage(self):
        self.click_carrerbutton()
        self.click_assessmentbutton()
