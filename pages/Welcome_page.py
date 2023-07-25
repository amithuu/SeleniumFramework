from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver


class Welcome(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    carrier_profile = "//div[@id ='root']/div/div[2]/div[2]/div[1]//button"
    assessment = "//div[@id ='root']/div/div[2]/div[2]/div[2]//button"

    """GETTERS"""
    def get_carrier_button(self):
        return self.element_to_click(By.XPATH, self.carrier_profile)

    def get_assessment_button(self):
        return self.element_to_click(By.XPATH, self.assessment)

    """SETTERS"""
    def click_carrier_button(self):
        self.get_carrier_button().click()

    def click_assessment_button(self):
        self.get_assessment_button().click()

    def welcomepage(self, choose):

        if choose == "carrier":
            self.click_carrier_button()
        elif choose == "assessment":
            self.click_assessment_button()
