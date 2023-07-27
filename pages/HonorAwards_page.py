import time
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver


class HonorAwards(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    HONORAWARDS_EDITPROFILE = "//*[text()='Honors & Awards']"
    
    ADD_ANOTHER_HONORAWARDS = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div//div[2]//button"
    
    HONOR_AWARD_TITLE = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]//input"
    HONOR_AWARD_ISSUER = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[2]//input"

    START_MONTH = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[3]//select"
    START_YEAR = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[3]//input"

    ASSOCIATED_WITH = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[4]//input"
    ASSOCIATED_WITH_LIST = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]//div[4]/div/div/div[2]//li"

    HONOR_AWARD_DESCRIPTION = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]//p"

    SAVE = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]//button[2]"

    """GETTERS"""

    def get_honoraward_editprofiles(self):
        return self.element_to_click(By.XPATH, self.HONORAWARDS_EDITPROFILE)

    def get_add_another_honoraward(self):
        return self.element_to_click(By.XPATH, self.ADD_ANOTHER_HONORAWARDS)

    def get_honoraward_title(self):
        return self.element_to_click(By.XPATH, self.HONOR_AWARD_TITLE)

    def get_honoraward_issuer(self):
        return self.element_to_click(By.XPATH, self.HONOR_AWARD_ISSUER)

    def get_startmonth(self):
        return self.element_to_click(By.XPATH, self.START_MONTH)

    def get_startyear(self):
        return self.element_to_click(By.XPATH, self.START_YEAR)

    def get_associatedwith(self):
        return self.element_to_click(By.XPATH, self.ASSOCIATED_WITH)

    def get_associated_with_list(self):
        return self.presence_of_all_element(By.XPATH, self.ASSOCIATED_WITH_LIST)

    def get_honoraward_description(self):
        return self.element_to_click(By.XPATH, self.HONOR_AWARD_DESCRIPTION)

    def get_save_button(self):
        return self.element_to_click(By.XPATH, self.SAVE)

    """SETTERS"""
    def click_honoraward_editprofiles(self):
        self.get_honoraward_editprofiles().click()

    def click_add_another_honoraward(self):
        self.get_add_another_honoraward().click()

    def enter_honoraward_title(self, title):
        self.get_honoraward_title().send_keys(title)

    def enter_honoraward_issuer(self, issuer):
        self.get_honoraward_issuer().send_keys(issuer)

    def select_honoraward_issuedate(self, month, year):
        self.get_startmonth().click()
        self.select_options(self.get_startmonth(), month)
        self.get_startyear().send_keys(year)

    def enter_associatedwith(self, associated_with):
        time.sleep(2)
        self.get_associatedwith().click()
        time.sleep(3)
        associated_withs = self.get_associated_with_list()

        for associates in associated_withs:
            if associated_with in associates.text.casefold():
                associates.click()
                break

    def enter_honoraward_description(self, description):
        self.get_honoraward_description().send_keys(description)

    def click_save_button(self):
        self.get_save_button().click()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(1)

    def honorawards(self, i, user, honoraward_title, honoraward_issuer, month, year, associated_with, honoraward_description):
        self.click_honoraward_editprofiles()

        if user == "new":
            if i == 0:
                self.enter_honoraward_title(honoraward_title)
                self.enter_honoraward_issuer(honoraward_issuer)
                self.select_honoraward_issuedate(month, year)
                self.enter_associatedwith(associated_with)
                self.enter_honoraward_description(honoraward_description)
                self.click_save_button()
            else:
                self.click_add_another_honoraward()
                self.enter_honoraward_title(honoraward_title)
                self.enter_honoraward_issuer(honoraward_issuer)
                self.select_honoraward_issuedate(month, year)
                self.enter_associatedwith(associated_with)
                self.enter_honoraward_description(honoraward_description)
                self.click_save_button()

        elif user == "old":
            self.click_add_another_honoraward()
            self.enter_honoraward_title(honoraward_title)
            self.enter_honoraward_issuer(honoraward_issuer)
            self.select_honoraward_issuedate(month, year)
            self.enter_associatedwith(associated_with)
            self.enter_honoraward_description(honoraward_description)
            self.click_save_button()
