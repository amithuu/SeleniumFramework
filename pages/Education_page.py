import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.Basedriver import BaseDriver
class Education(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    add_education = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button[1]"
    degree = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[1]//input"
    university = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[2]//input"
    location = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[1]//input"
    """GETTERS"""
    def get_addeducation(self):
        return self.element_to_click(By.XPATH, self.add_education)

    def get_degree(self):
        return self.element_to_click(By.XPATH, self.degree)

    def get_university(self):
        return self.element_to_click(By.XPATH, self.university)

    def get_location(self):
        return self.element_to_click(By.XPATH, self.location)

    """SETTERS"""
    def click_addeducation(self):
        self.get_addeducation().click()

    def enter_degree(self, degree):
        self.get_degree().click()
        self.get_degree().send_keys(degree)
        self.get_degree().send_keys(Keys.TAB)

    def enter_university(self, university):
        self.get_university().click()
        self.get_university().send_keys(university)
        self.get_university().send_keys(Keys.TAB)

    def enter_location(self, location):
        self.get_location().click()
        self.get_location().send_keys(location)
        self.get_location().send_keys(Keys.TAB)

    def education(self, degree, university, location):
        self.click_addeducation()
        self.enter_degree(degree)
        self.enter_university(university)
        self.enter_location(location)
