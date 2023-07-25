import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver

class VoluntaryRoles(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    VOLUNATRYROLES__EDITPROFILE = "//*[text()='Voluntary Roles']"

    ADD_VOLUNTARYROLES = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]//button"

    VOLUNTARY_ROLE = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]//input"
    VOLUNTARY_ORGANIZATION = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[2]//input"

    START_MONTH = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]//select"
    START_YEAR = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]//input"
    END_MONTH = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]//select"
    END_YEAR = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]//input"

    VOLUNTARY_DESCRIPTION = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]//p"

    SAVE = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[4]//button[2]"

    """GETTERS"""

    def get_voluntaryroles_EDITPROFILE(self):
        return self.element_to_click(By.XPATH, self.VOLUNATRYROLES__EDITPROFILE)

    def get_add_another_voluntaryroles(self):
        return self.element_to_click(By.XPATH, self.ADD_VOLUNTARYROLES)

    def get_voluntary_role(self):
        return self.element_to_click(By.XPATH, self.VOLUNTARY_ROLE)

    def get_voluntary_organization(self):
        return self.element_to_click(By.XPATH, self.VOLUNTARY_ORGANIZATION)

    def get_startmonth(self):
        return self.element_to_click(By.XPATH, self.START_MONTH)

    def get_startyear(self):
        return self.element_to_click(By.XPATH, self.START_YEAR)

    def get_endmonth(self):
        return self.element_to_click(By.XPATH, self.END_MONTH)

    def get_endyear(self):
        return self.element_to_click(By.XPATH, self.END_YEAR)

    def get_voluntary_description(self):
        return self.element_to_click(By.XPATH, self.VOLUNTARY_DESCRIPTION)

    def get_save_button(self):
        return self.element_to_click(By.XPATH, self.SAVE)

    """SETTERS"""
    def click_voluntaryroles_editprofiles(self):
        self.get_voluntaryroles_EDITPROFILE().click()

    def click_add_another_voluntaryroles(self):
        self.get_add_another_voluntaryroles().click()

    def enter_voluntary_role(self, role):
        self.get_voluntary_role().send_keys(role)

    def enter_voluntary_organization(self, organization):
        self.get_voluntary_organization().send_keys(organization)

    def select_durationfrom(self, month, year):
        self.get_startmonth().click()
        self.select_options(self.get_startmonth(), month)
        self.get_startyear().send_keys(year)

    def select_durationto(self, month, year):
        self.get_endmonth().click()
        self.select_options(self.get_endmonth(), month)
        self.get_endyear().send_keys(year)

    def enter_voluntary_description(self, description):
        self.get_voluntary_description().send_keys(description)

    def click_save_button(self):
        self.get_save_button().click()
        time.sleep(3)

    def voluntaryroles(self, user, role, organization, month, year, month1, year1, description):
        self.click_voluntaryroles_editprofiles()

        if user == "new":
            self.enter_voluntary_role(role)
            self.enter_voluntary_organization(organization)
            self.select_durationfrom(month, year)
            self.select_durationto(month1, year1)
            self.enter_voluntary_description(description)
            self.click_save_button()
            self.click_add_another_voluntaryroles()

        elif user == "old":
            self.click_add_another_voluntaryroles()
            self.enter_voluntary_role(role)
            self.enter_voluntary_organization(organization)
            self.select_durationfrom(month, year)
            self.select_durationto(month1, year1)
            self.enter_voluntary_description(description)
            self.click_save_button()
