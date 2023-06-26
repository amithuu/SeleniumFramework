import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver

class Causes(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # LOCATORS
    CAUSES_DASHBOARD = "//*[text()='Causes']"
    ICON = "//div[@id='root']/div[2]/div[2]/div/div/div/div/div[{i}]//span[1]"
    SAVE_CAUSES = "//div[@id='root']/div[2]/div[2]/div/div/div/button"
    """GETTERS"""
    def get_causesdashboard(self):
        return self.element_to_click(By.XPATH, self.CAUSES_DASHBOARD)

    """SETTERS"""
    def click_causesdashboard(self):
        self.get_causesdashboard().click()

    def causes(self):
        time.sleep(2)
        for i in range(1, 7):
            self.element_to_click(By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div/div/div[{i}]//span[1]").click()
            time.sleep(1)
        self.save()
        time.sleep(3)
        self.next()
