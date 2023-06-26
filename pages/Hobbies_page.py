import time
from base.Basedriver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class Hobbies(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # LOCATORS
    HOBBIES_DASHBOARD = "//*[text()='Hobbies']"
    CATEGORY = "//*[@id='root']/div[2]/div/div/div/div/div[1]/div[1]//input"
    HOBBIES = "//*[@id='root']/div[2]/div/div/div/div/div[1]/div[2]//input"
    ADD_HOBBIES = "//*[@id='root']/div[2]/div/div/div/div/div[1]/div[2]//button"

    """GETTERS"""
    def get_hobbiesdashboard(self):
        return self.element_to_click(By.XPATH, self.HOBBIES_DASHBOARD)

    def get_category(self):
        return self.element_to_click(By.XPATH, self.CATEGORY)

    def get_hobbies(self):
        return self.element_to_click(By.XPATH, self.HOBBIES)

    def get_addhobbies(self):
        return self.element_to_click(By.XPATH, self.ADD_HOBBIES)

    """SETTERS"""
    def click_hobbiesdashboard(self):
        self.get_hobbiesdashboard().click()

    def choose_category(self, i):
        self.get_category().click()
        for i in range(i):
            self.get_category().send_keys(Keys.ARROW_DOWN)
        self.get_category().send_keys(Keys.ENTER)

    def enter_hobbies(self, hobbies):
        self.get_hobbies().click()
        self.get_hobbies().send_keys(hobbies)

    def click_addhobbies(self):
        self.get_addhobbies().click()

    def hobbies(self, i, hobbies):
        time.sleep(2)
        self.choose_category(i)
        self.enter_hobbies(hobbies)
        self.click_addhobbies()
        self.save()
        if i <= 1:
            self.next()
            self.back()
        else:
            self.next()

