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

    CHANGE_PASSWORD = "//div[@id='root']/div[2]/div[2]/div/ul/li[2]//button"
    OLD_PASSWORD = "//div[@id='root']//form/div/div[1]//input"
    NEW_PASSWORD = "//div[@id='root']//form/div/div[2]//input"
    CONFIRM_PASSWORD = "//div[@id='root']//form/div/div[3]//input"
    EYE_BUTTON = "//div[@id='root']//form/div/div[3]//button"
    CHANGE_PASSWORD_BUTTON = "//button[text()='Change Password']"

    CHANGE_MOBILE = "//div[@id='root']/div[2]/div[2]/div/ul/li[3]//button"
    ENTER_MOBILE_NUMBER = "//*[@id = 'root']/div[2]/div[2]/div/div/div//input"
    UPDATE_MOBILE = "//*[@id = 'root']/div[2]/div[2]/div/div//button"

    CANCEL_SUBSCRIPTION = "//div[@id='root']/div[2]/div[2]/div/ul/li[4]//button"
    X_MARK = "//button[@aria-label='Close']"
    STAY_PREMIUM_POPUP = "//footer//button[1]"
    CANCEL_SUBSCRIPTION_POPUP = "//footer//button[2]"

    """GETTERS"""
    def get_settingdasboard(self):
        return self.element_to_click(By.XPATH, self.SETTING_DASHBOARD)

    def get_changepassword(self):
        return self.element_to_click(By.XPATH, self.CHANGE_PASSWORD)

    def get_oldpassword(self):
        return self.element_to_click(By.XPATH, self.OLD_PASSWORD)

    def get_newpassword(self):
        return self.element_to_click(By.XPATH, self.NEW_PASSWORD)

    def get_confirmpassword(self):
        return self.element_to_click(By.XPATH, self.CONFIRM_PASSWORD)

    def get_eyebutton(self):
        return self.element_to_click(By.XPATH, self.EYE_BUTTON)

    def get_changepasswordbutton(self):
        return self.element_to_click(By.XPATH, self.CHANGE_PASSWORD_BUTTON)

    def get_changemobile(self):
        return self.element_to_click(By.XPATH, self.CHANGE_MOBILE)

    def get_entermobilenumber(self):
        return self.element_to_click(By.XPATH, self.ENTER_MOBILE_NUMBER)

    def get_updatemobile(self):
        return self.element_to_click(By.XPATH, self.UPDATE_MOBILE)

    def get_cancelsubsription(self):
        return self.element_to_click(By.XPATH, self.CANCEL_SUBSCRIPTION)

    def get_closepopup(self):
        return self.element_to_click(By.XPATH, self.X_MARK)

    def get_staypremium(self):
        return self.element_to_click(By.XPATH, self.STAY_PREMIUM_POPUP)

    def get_cancelsubsriptionpopup(self):
        return self.element_to_click(By.XPATH, self.CANCEL_SUBSCRIPTION_POPUP)

    """SETTERS"""

    def click_settingdashboard(self):
        self.get_settingdasboard().click()

    def click_changepassword(self):
        self.get_changepassword().click()

    def enter_oldpassword(self, oldpassword):
        self.get_oldpassword().click()
        self.get_oldpassword().send_keys(oldpassword)

    def enter_newpassword(self, newpassword):
        self.get_newpassword().click()
        self.get_newpassword().send_keys(newpassword)
        self.get_confirmpassword().send_keys(Keys.TAB)

    def enter_confirmpassword(self, confirmpassword):
        self.get_confirmpassword().click()
        self.get_confirmpassword().send_keys(confirmpassword)
        self.get_confirmpassword().send_keys(Keys.TAB)

    def click_eyebutton(self):
        self.get_eyebutton().click()

    def click_changepasswordbutton(self):
        self.get_changepasswordbutton().click()

    def click_changemobile(self):
        self.get_changemobile().click()

    def enter_entermobilenumber(self, number):
        self.get_entermobilenumber().click()
        self.get_entermobilenumber().send_keys(number)
        self.get_entermobilenumber().send_keys(Keys.TAB)

    def click_updatemobilebutton(self):
        self.get_updatemobile().click()

    def click_cancelsubsription(self):
        self.get_cancelsubsription().click()

    def click_closepopup(self):
        return self.get_closepopup().click()

    def click_staypremium(self):
        self.get_staypremium().click()

    def click_cancelsubsriptionpopup(self):
        self.get_cancelsubsriptionpopup().click()

    def setting(self, user, oldpassword, newpassword, confirmpassword, mobilenumber):
        self.click_settingdashboard()
        if user == "editprofile":
            self.editprofiles()

        elif user == "changepassword":
            self.click_changepassword()
            self.enter_oldpassword(oldpassword)
            self.enter_newpassword(newpassword)
            self.enter_confirmpassword(confirmpassword)
            self.click_eyebutton()
            self.click_changepasswordbutton()

        elif user == "changemobile":
            self.click_changemobile()
            self.enter_entermobilenumber(mobilenumber)
            self.click_updatemobilebutton()

        elif user == "cancelsubsription":
            self.click_cancelsubsription()
            self.click_closepopup()
            # self.click_staypremium()
            # self.click_cancelsubsriptionpopup()



