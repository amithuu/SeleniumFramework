import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver
from selenium.webdriver.support import expected_conditions as ec
# firstname = "test"
# lastname = "talentPlace"
# email = f"prod{k}@g.co"
# phone_no = f"1{k}234567890"
# location = "Bangalore"
# dob = "25031999"
# gender = "male"
# password = "New@1234"
# confirm_password = "New@1234"

class Signup(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    SIGN_UP = "//button[text()='Sign Up']"
    FIRST_NAME = "//*[@name='firstName']"
    LAST_NAME = "//*[@name='lastName']"
    EMAIL = "//*[@name='email']"
    PHONE_NO = "//input[@type='tel']"
    COUNTRY_FLAG = "//*[@class='selected-flag']"
    COUNTRY_DROPDOWN = "//*[@class = 'country-list']/li/span"
    DOB = "//*[@name='dob']"
    GENDER = "//*[@name='gender']"
    PASSWORD = "//*[@name='password']"
    CONFIRM_PASSWORD = "//*[@name='confirmPassword']"
    LOCATION = "[@class='chakra-stack css-14uartk']/div[5]//input"

    """GETTERS"""
    def get_signupbutton(self):
        return self.element_to_click(By.XPATH, self.SIGN_UP)

    def get_firstname(self):
        return self.element_to_click(By.XPATH, self.FIRST_NAME)

    def get_lastname(self):
        return self.element_to_click(By.XPATH, self.LAST_NAME)

    def get_email(self):
        return self.element_to_click(By.XPATH, self.EMAIL)

    def get_phoneno(self):
        return self.element_to_click(By.XPATH, self.PHONE_NO)

    def get_countaryflag(self):
        return self.element_to_click(By.XPATH, self.COUNTRY_FLAG)

    def get_countrydropdown(self):
        return self.presence_of_all_element(By.XPATH, self.COUNTRY_DROPDOWN)

    def get_dob(self):
        return self.element_to_click(By.XPATH, self.DOB)

    def get_gender(self):
        return self.element_to_click(By.XPATH, self.GENDER)

    def get_location(self):
        return self.element_to_click(By.XPATH, self.LOCATION)

    def get_password(self):
        return self.element_to_click(By.XPATH, self.PASSWORD)

    def get_confirmpassword(self):
        return self.element_to_click(By.XPATH, self.CONFIRM_PASSWORD)

    """SETTERS"""
    def click_signupbutton(self):
        self.get_signupbutton().click()

    def enter_firstname(self, firstname):
        self.get_firstname().click()
        self.get_firstname().send_keys(firstname)
        self.get_firstname().send_keys(Keys.TAB)

    def enter_lastname(self, lastname):
        self.get_lastname().click()
        self.get_lastname().send_keys(lastname)
        self.get_lastname().send_keys(Keys.TAB)

    def enter_email(self, email):
        self.get_email().click()
        self.get_email().send_keys(email)
        self.get_email().send_keys(Keys.TAB)

    def click_countryflag(self):
        self.get_countaryflag().click()

    def select_countarydropdown(self, countryname):
        # I am storing the all the list of country flags in this list and taking which ever I need by sending its country name.
        country_list = self.get_countrydropdown()
        for country in country_list:
            if countryname in country.text:
                country.click()
                break

    def enter_phonenumber(self, phoneno):
        self.get_phoneno().click()
        self.get_phoneno().send_keys(Keys.CONTROL + "a")
        self.get_phoneno().send_keys(phoneno)

    def enter_dob(self, date_of_birth):
        self.get_dob().click()
        self.get_dob().send_keys(date_of_birth)
        # self.get_dob().send_keys("03")
        # self.get_dob().send_keys("1999")

    def enter_gender(self, gender):
        self.get_gender().click()
        self.get_gender().send_keys(gender)
        self.get_gender().send_keys(Keys.TAB)

    def enter_location(self):
        self.get_location().click()
        self.get_location().send_keys(Keys.CONTROL + "a")
        self.get_location().send_keys("Bangalore, Karnataka, India")
        time.sleep(5)

    def enter_password(self, password):
        self.get_password().send_keys(password)

    def enter_confirmpassword(self, confirm_password):
        self.get_confirmpassword().send_keys(confirm_password)

    def sign_up(self, firstname, lastname, email, countaryname, phone_no, password, confirm_password):
        self.click_signupbutton()
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_email(email)
        self.click_countryflag()
        self.select_countarydropdown(countaryname)
        time.sleep(5)
        self.enter_phonenumber(phone_no)
        self.enter_password(password)
        self.enter_confirmpassword(confirm_password)
        self.click_signupbutton()
        time.sleep(5)
