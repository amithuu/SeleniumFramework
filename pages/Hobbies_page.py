import time
from base.Basedriver import BaseDriver
from selenium.webdriver.common.by import By

class Hobbies(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # LOCATORS
    HOBBIES_EDITPROFILE = "//*[text()='Hobbies']"
    HOBBIES_CATEGORY = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[1]/div[1]//input"
    HOBBIES_CATEGORY_LIST = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div//li/div"

    HOBBIES = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[1]/div[2]//input"
    ADD_BUTTON = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[1]/div[2]//button"

    """GETTERS"""
    def get_hobbies_editprofiles(self):
        return self.element_to_click(By.XPATH, self.HOBBIES_EDITPROFILE)

    def get_category(self):
        return self.element_to_click(By.XPATH, self.HOBBIES_CATEGORY)

    def get_category_list(self):
        return self.presence_of_all_element(By.XPATH, self.HOBBIES_CATEGORY_LIST)

    def get_hobbies(self):
        return self.element_to_click(By.XPATH, self.HOBBIES)

    def get_add_hobbies(self):
        return self.element_to_click(By.XPATH, self.ADD_BUTTON)

    """SETTERS"""
    def click_hobbies_editprofiles(self):
        self.get_hobbies_editprofiles().click()

    def select_category(self, category, hobbies):
        self.get_category().click()
        time.sleep(1)
        catergories = self.get_category_list()

        for catergry in catergories:
            if category in catergry.text.casefold():
                catergry.click()
                break

        self.get_hobbies().send_keys(hobbies)

    def click_add_hobbies(self):
        self.get_add_hobbies().click()

    def hobbies(self, category, hobbies):
        self.click_hobbies_editprofiles()
        self.select_category(category, hobbies)
        self.click_add_hobbies()
        self.save()
        self.backto_menu()
