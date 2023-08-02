import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from pages.EditProfiles_page import EditProfiles


class Setting(EditProfiles):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locators
    SETTING_DASHBOARD = "//p[text()='Settings']"

    # CHANGE_PASSWORD = "//ul/li[2]//button"
    CHANGE_PASSWORD = "//button[text() ='Change Password']"
    OLD_PASSWORD = "//input[@name = 'oldPassword']"
    NEW_PASSWORD = "//input[@name = 'newPassword']"
    CONFIRM_PASSWORD = "//input[@name = 'confirmPassword']"
    EYE_BUTTON = "//button[@aria-label = 'Show or Hide password']"
    CHANGE_PASSWORD_BUTTON = "//button[text()='Change Password']"

    # CHANGE_MOBILE = "//div[@id='root']/div[2]/div[2]/div/ul/li[3]//button"
    # ENTER_MOBILE_NUMBER = "//*[@id = 'root']/div[2]/div[2]/div/div/div//input"
    # UPDATE_MOBILE = "//*[@id = 'root']/div[2]/div[2]/div/div//button"
    CHANGE_MOBILE = "//button[text() =' Change Mobile']"
    COUNTRY_FLAG = "//*[@class='selected-flag']"
    SELECTCOUNTRY_LIST = "//div[@class = 'flag-container']/ul/li//span"
    ENTER_MOBILE_NUMBER = "//input[@type ='tel']"
    SEND_OTP = "//button[text()='Send OTP']"
    UPDATE_MOBILE = "//button[text() = 'Update Mobile Number']"

    CANCEL_SUBSCRIPTION = "//div[@id='root']/div[2]/div[2]/div/ul/li[4]//button"
    X_MARK = "//button[@aria-label='Close']"
    STAY_PREMIUM_POPUP = "//footer//button[1]"
    CANCEL_SUBSCRIPTION_POPUP = "//footer//button[2]"

    """GETTERS"""
    def get_setting_editprofile(self):
        return self.element_to_click(By.XPATH, self.SETTING_DASHBOARD)

    def get_change_password(self):
        return self.element_to_click(By.XPATH, self.CHANGE_PASSWORD)

    def get_old_password(self):
        return self.element_to_click(By.XPATH, self.OLD_PASSWORD)

    def get_new_password(self):
        return self.element_to_click(By.XPATH, self.NEW_PASSWORD)

    def get_confirmpassword(self):
        return self.element_to_click(By.XPATH, self.CONFIRM_PASSWORD)

    def get_eye_button(self):
        return self.element_to_click(By.XPATH, self.EYE_BUTTON)

    def get_changepassword_button(self):
        return self.element_to_click(By.XPATH, self.CHANGE_PASSWORD_BUTTON)

    def get_changemobile(self):
        return self.element_to_click(By.XPATH, self.CHANGE_MOBILE)

    def get_enter_mobilenumber(self):
        return self.element_to_click(By.XPATH, self.ENTER_MOBILE_NUMBER)

    def get_countaryflag(self):
        return self.element_to_click(By.XPATH, self.COUNTRY_FLAG)

    def get_countrydropdown(self):
        return self.presence_of_all_element(By.XPATH, self.SELECTCOUNTRY_LIST)

    def get_update_mobilenumber(self):
        return self.element_to_click(By.XPATH, self.UPDATE_MOBILE)

    def get_send_otp(self):
        return self.element_to_click(By.XPATH, self.SEND_OTP)

    def get_cancelsubsription(self):
        return self.element_to_click(By.XPATH, self.CANCEL_SUBSCRIPTION)

    def get_close_popup(self):
        return self.element_to_click(By.XPATH, self.X_MARK)

    def get_stay_premium(self):
        return self.element_to_click(By.XPATH, self.STAY_PREMIUM_POPUP)

    def get_cancel_subsriptionpopup(self):
        return self.element_to_click(By.XPATH, self.CANCEL_SUBSCRIPTION_POPUP)

    """SETTERS"""

    def click_setting_sidepanel(self):
        self.get_setting_editprofile().click()

    def click_changepassword(self):
        self.get_change_password().click()

    def enter_old_password(self, old_password):
        self.get_old_password().click()
        self.get_old_password().send_keys(old_password)

    def enter_new_password(self, new_password):
        self.get_new_password().click()
        self.get_new_password().send_keys(new_password)
        self.get_confirmpassword().send_keys(Keys.TAB)

    def enter_confirmpassword(self, confirmpassword):
        self.get_confirmpassword().click()
        self.get_confirmpassword().send_keys(confirmpassword)
        self.get_confirmpassword().send_keys(Keys.TAB)

    def click_eye_button(self):
        self.get_eye_button().click()
        time.sleep(2)

    def click_changepassword_button(self):
        self.get_changepassword_button().click()
        time.sleep(2)

    def click_changemobile(self):
        self.get_changemobile().click()

    def select_countarydropdown(self, countryname):
        # I am storing the all the list of country flags in this list and taking which ever I need by sending its country name.
        self.get_countaryflag().click()
        time.sleep(2)

        country_list = self.get_countrydropdown()
        for country in country_list:
            if countryname in country.text:
                country.click()
                break

    def enter_mobilenumber(self, number):
        self.get_enter_mobilenumber().click()
        self.get_enter_mobilenumber().send_keys(number)
        self.get_enter_mobilenumber().send_keys(Keys.TAB)

    def click_update_mobilebutton(self):
        self.get_update_mobilenumber().click()
        time.sleep(2)

    def click_send_otp(self):
        self.get_send_otp().click()
        time.sleep(2)

    def click_cancelsubsription(self):
        self.get_cancelsubsription().click()

    def click_close_popup(self):
        return self.get_close_popup().click()

    def click_stay_premium(self):
        self.get_stay_premium().click()

    def click_cancel_subsriptionpopup(self):
        self.get_cancel_subsriptionpopup().click()

    def setting(self, user, old_password, new_password, confirmpassword, countryname, mobile_number):
        self.click_setting_sidepanel()

        if user == "editprofile":
            self.editprofiles(user)

        elif user == "changepassword":
            self.click_changepassword()
            self.enter_old_password(old_password)
            self.enter_new_password(new_password)
            self.enter_confirmpassword(confirmpassword)
            self.click_eye_button()
            self.click_changepassword_button()

        elif user == "changemobile":
            self.click_changemobile()
            self.select_countarydropdown(countryname)
            self.enter_mobilenumber(mobile_number)
            if countryname.casefold() == "india":
                self.click_send_otp()
            else:
                self.click_update_mobilebutton()

        elif user == "cancelsubsription":
            self.click_cancelsubsription()
            self.click_close_popup()
            # self.click_stay_premium()
            # self.click_cancel_subsriptionpopup()
