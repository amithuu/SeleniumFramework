import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver

class Profile_picture(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locators
    picturestatus_editprofiles = "//*[text()='Picture/Status']"
    uploadpicture = "//button[text()='Upload Picture']"
    headline = "headline"
    Iam_opento_work = "//*[@id = 'root']/div[2]/div[2]/div/div/div[2]/label//span"

    # GETTERS
    def get_picturestatus(self):
        return self.element_to_click(By.XPATH, self.picturestatus_editprofiles)

    def get_uploadpicture(self):
        return self.element_to_click(By.XPATH, self.uploadpicture)

    def get_headline(self):
        return self.element_to_click(By.NAME, self.headline)

    def get_iamopentowork_checkbox(self):
        return self.element_to_click(By.XPATH, self.Iam_opento_work)

    # SETTERS
    def click_picturestatus(self):
        self.get_picturestatus().click()

    def click_uploadpicture(self):
        self.get_uploadpicture().click()
        time.sleep(5)

    def enter_headline(self, headline):
        self.get_headline().click()
        self.get_headline().send_keys(Keys.CONTROL + "a")
        self.get_headline().send_keys(headline)

    def click_iamopentowork(self):
        self.get_iamopentowork_checkbox().click()

    def picturestatus(self, headline):
        self.click_picturestatus()
        self.click_uploadpicture()
        self.enter_headline(headline)
        self.click_iamopentowork()
        self.save()
        time.sleep(3)
