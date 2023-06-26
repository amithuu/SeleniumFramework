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
    VOLUNATRYROLES_DASHBOARD = "//*[text()='Voluntary Roles']"
    ADD_VOLUNTARYROLES = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"
    ROLE = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]//input"
    ORGANIZATION = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]//input"
    START_MONTH = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]//select"
    START_YEAR = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]//input"
    END_MONTH = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]//select"
    END_YEAR = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]//input"
    DESCRIPTION = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]//p"
    SAVE_VOLUNTARYROLES = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/button"

    """GETTERS"""

    def get_voluntaryrolesdashboard(self):
        return self.element_to_click(By.XPATH, self.VOLUNATRYROLES_DASHBOARD)

    def get_addvoluntaryroles(self):
        return self.element_to_click(By.XPATH, self.ADD_VOLUNTARYROLES)

    def get_role(self):
        return self.element_to_click(By.XPATH, self.ROLE)

    def get_organization(self):
        return self.element_to_click(By.XPATH, self.ORGANIZATION)

    def get_startmonth(self):
        return self.element_to_click(By.XPATH, self.START_MONTH)

    def get_startyear(self):
        return self.element_to_click(By.XPATH, self.START_YEAR)

    def get_endmonth(self):
        return self.element_to_click(By.XPATH, self.END_MONTH)

    def get_endyear(self):
        return self.element_to_click(By.XPATH, self.END_YEAR)

    def get_description(self):
        return self.element_to_click(By.XPATH, self.DESCRIPTION)

    def get_savepatent(self):
        return self.element_to_click(By.XPATH, self.SAVE_VOLUNTARYROLES)

    """SETTERS"""
    def click_voluntaryrolesdashboard(self):
        self.get_voluntaryrolesdashboard().click()

    def click_addvoluntarroles(self):
        self.get_addvoluntaryroles().click()

    def enter_role(self, role):
        self.get_role().click()
        self.get_role().send_keys(role)
        self.get_role().send_keys(Keys.TAB)

    def enter_organization(self, organization):
        self.get_organization().click()
        self.get_organization().send_keys(organization)
        self.get_organization().send_keys(Keys.TAB)

    def enter_durationfrom(self, year):
        self.get_startmonth().click()
        self.get_startmonth().send_keys(Keys.ARROW_DOWN)
        self.get_startmonth().send_keys(Keys.ARROW_DOWN)
        self.get_startmonth().send_keys(Keys.ENTER)
        self.get_startyear().send_keys(year)

    def enter_durationto(self, year):
        self.get_endmonth().click()
        self.get_endmonth().send_keys(Keys.ARROW_DOWN)
        self.get_endmonth().send_keys(Keys.ARROW_DOWN)
        self.get_endmonth().send_keys(Keys.ARROW_DOWN)
        self.get_endmonth().send_keys(Keys.ENTER)
        self.get_endyear().send_keys(year)

    def enter_description(self, description):
        self.get_description().click()
        self.get_description().send_keys(description)

    def click_savevoluntaryrole(self):
        self.get_savepatent().click()

    def voluntaryroles(self, role, organization, durationfrom, durationto, description):
        self.click_addvoluntarroles()
        self.enter_role(role)
        self.enter_organization(organization)
        self.enter_durationfrom(durationfrom)
        self.enter_durationto(durationto)
        self.enter_description(description)
        self.click_savevoluntaryrole()
        time.sleep(5)
        self.next()
        self.back()
