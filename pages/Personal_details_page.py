import time

from selenium.webdriver import Keys

from base.Basedriver import BaseDriver
from selenium.webdriver.common.by import By
class Personaldetails(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    uploadpicture = "//*[text()='Upload profile']"
    firstname = "first-name"
    lastname = "lastName"
    gender = "//*[@class=' css-19bb58m']/input"
    dob = "//*[@name='dob']"
    currency = "//*[@class='chakra-stack css-11i9qz7']/div[3]/div//input"
    # month = "//*[@id = 'root']/div[2]/div[2]/div/div/div[1]/div[3]/div[2]/div//select"
    month = "//*[@id = 'root']/div[2]/div[2]/div/div/div[1]/div[3]/div[2]/div/div/div/div//select"
    year = "//input[@Placeholder='Year']"
    place = "//*[@id = 'root']/div[2]/div[2]/div/div/div[1]/div[4]/div[1]//input"
    headline = "headline"
    socilamedia = "socialMedia.linkedin"

    """GETTERS"""
    def get_uploadpicture(self):
        return self.element_to_click(By.XPATH, self.uploadpicture)

    def get_firstname(self):
        return self.element_to_click(By.ID, self.firstname)

    def get_lastname(self):
        return self.element_to_click(By.NAME, self.lastname)

    def get_gender(self):
        return self.element_to_click(By.XPATH, self.gender)

    def get_dob(self):
        return self.element_to_click(By.XPATH, self.dob)

    def get_currency(self):
        return self.element_to_click(By.XPATH, self.currency)

    def get_month(self):
        return self.element_to_click(By.XPATH, self.month)

    def get_year(self):
        return self.element_to_click(By.XPATH, self.year)

    def get_place(self):
        return self.element_to_click(By.XPATH, self.place)

    def get_headline(self):
        return self.element_to_click(By.NAME, self.headline)

    def get_socialmedia(self):
        return self.element_to_click(By.NAME, self.socilamedia)

    """SETTERS"""
    def click_uploadpicture(self):
        self.get_uploadpicture().click()
        time.sleep(5)

    def enter_firstname(self, firstname):
        self.get_firstname().click()
        self.get_firstname().send_keys(Keys.CONTROL + "a")
        self.get_firstname().send_keys(firstname)

    def enter_lastname(self, lastname):
        self.get_lastname().click()
        self.get_lastname().send_keys(Keys.CONTROL + "a")
        self.get_lastname().send_keys(lastname)

    def enter_gender(self):
        self.get_gender().click()
        self.get_gender().send_keys(Keys.ARROW_DOWN)
        self.get_gender().send_keys(Keys.ARROW_DOWN)
        self.get_gender().send_keys(Keys.ENTER)
        time.sleep(3)

    def enter_dob(self, dob):
        self.get_dob().click()
        self.get_dob().send_keys(dob)
        self.get_dob().send_keys(Keys.TAB)

    def enter_currency(self):
        self.get_currency().click()
        self.get_currency().send_keys(Keys.ARROW_DOWN)
        self.get_currency().send_keys(Keys.ARROW_DOWN)
        self.get_currency().send_keys(Keys.ENTER)

    def enter_experience(self, year):
        self.get_month().click()
        self.get_month().send_keys(Keys.ARROW_DOWN)
        self.get_month().send_keys(Keys.ENTER)
        self.get_month().send_keys(Keys.TAB)
        self.get_year().send_keys(year)

    def enter_place(self, place):
        self.get_place().click()
        self.get_place().send_keys(Keys.CONTROL + "a")
        self.get_place().send_keys(place)
        self.get_place().send_keys(Keys.BACK_SPACE)
        time.sleep(3)

    def enter_headline(self, headline):
        self.get_headline().click()
        self.get_headline().send_keys(Keys.CONTROL + "a")
        self.get_headline().send_keys(headline)

    def enter_socialmedia(self, socilamedia):
        self.get_socialmedia().click()
        self.get_socialmedia().send_keys(Keys.CONTROL + "a")
        self.get_socialmedia().send_keys(socilamedia)

    def personaldetails(self, firstname, lastname, dob, year, place, headline, socialmedia):
        self.click_uploadpicture()
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_gender()
        self.enter_dob(dob)
        self.enter_currency()
        self.enter_experience(year)
        self.enter_place(place)
        self.enter_headline(headline)
        self.enter_socialmedia(socialmedia)
        self.save()
        time.sleep(3)
        self.back()# back is next here
        # self.dashboard()
