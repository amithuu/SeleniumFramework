import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver


class HonorAwards(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    HONORAWARDS_DASHBOARD = "//*[text()='Honors & Awards']"
    ADD_HONORAWARDS = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"
    TITLE = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]//input"
    ISSUER = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]//input"
    START_MONTH = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]//select"
    START_YEAR = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]//input"
    ASSOCIATED_WITH = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]//input"
    DESCRIPTION = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]//p"
    SAVE_HONORAWARDS = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/button"

    """GETTERS"""

    def get_honorawarddashboard(self):
        return self.element_to_click(By.XPATH, self.HONORAWARDS_DASHBOARD)

    def get_addhonoraward(self):
        return self.element_to_click(By.XPATH, self.ADD_HONORAWARDS)

    def get_title(self):
        return self.element_to_click(By.XPATH, self.TITLE)

    def get_issuer(self):
        return self.element_to_click(By.XPATH, self.ISSUER)

    def get_startmonth(self):
        return self.element_to_click(By.XPATH, self.START_MONTH)

    def get_startyear(self):
        return self.element_to_click(By.XPATH, self.START_YEAR)

    def get_associatedwith(self):
        return self.element_to_click(By.XPATH, self.ASSOCIATED_WITH)

    def get_description(self):
        return self.element_to_click(By.XPATH, self.DESCRIPTION)

    def get_savehonorawards(self):
        return self.element_to_click(By.XPATH, self.SAVE_HONORAWARDS)

    """SETTERS"""
    def click_honorawarddashboard(self):
        self.get_honorawarddashboard().click()

    def click_addhonoraward(self):
        self.get_addhonoraward().click()

    def enter_title(self, title):
        self.get_title().click()
        self.get_title().send_keys(title)
        self.get_title().send_keys(Keys.TAB)

    def enter_issuer(self, issuer):
        self.get_issuer().click()
        self.get_issuer().send_keys(issuer)
        self.get_issuer().send_keys(Keys.TAB)

    def enter_issuedate(self, year):
        self.get_startmonth().click()
        self.get_startmonth().send_keys(Keys.ARROW_DOWN)
        self.get_startmonth().send_keys(Keys.ARROW_DOWN)
        self.get_startmonth().send_keys(Keys.ENTER)
        self.get_startyear().send_keys(year)

    def enter_associatedwith(self):
        self.get_associatedwith().click()
        self.get_associatedwith().send_keys(Keys.ARROW_DOWN)
        self.get_associatedwith().send_keys(Keys.ARROW_DOWN)
        self.get_associatedwith().send_keys(Keys.ENTER)

    def enter_description(self, description):
        self.get_description().click()
        self.get_description().send_keys(description)

    def click_savehonoraward(self):
        self.get_savehonorawards().click()

    def honorawards(self, i, title, issuer, issueyear, description):
        self.click_addhonoraward()
        self.enter_title(title)
        self.enter_issuer(issuer)
        self.enter_issuedate(issueyear)
        self.enter_associatedwith()
        self.enter_description(description)
        self.click_savehonoraward()
        time.sleep(5)
        if i == 0:
            self.next()
            self.back()
        elif i == 1:
            self.next()
            self.discrad()
            self.back()
        else:
            self.next()
            self.discrad()
