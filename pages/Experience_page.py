import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from base.Basedriver import BaseDriver


class Experience(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    addcompany_button = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"
    company_name = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div[1]//input"
    job_type = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div[1]//input"
    experience = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]//input"
    organization = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[3]/div[1]//input"
    based = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[3]/div[2]//input"

    """GETTERS"""
    def get_addcompanybutton(self):
        return self.element_to_click(By.XPATH, self.addcompany_button)

    def get_companyname(self):
        return self.element_to_click(By.XPATH, self.company_name)

    def get_jobtype(self):
        return self.element_to_click(By.XPATH, self.job_type)

    def get_experience(self):
        return self.element_to_click(By.XPATH, self.experience)

    def get_organization(self):
        return self.element_to_click(By.XPATH, self.organization)

    def get_based(self):
        return self.element_to_click(By.XPATH, self.based)

    """SETTERS"""
    def click_addcompanybutton(self):
        self.get_addcompanybutton().click()

    def enter_companyname(self, companyname):
        self.get_companyname().click()
        self.get_companyname().send_keys(companyname)
        self.get_companyname().send_keys(Keys.TAB)

    def enter_jobtype(self, jobtype):
        self.get_jobtype().click()
        self.get_jobtype().send_keys(jobtype)
        self.get_jobtype().send_keys(Keys.TAB)

    def enter_experience(self, experience):
        self.get_experience().click()
        self.get_experience().send_keys(experience)
        self.get_experience().send_keys(Keys.TAB)

    def enter_organization(self, organition):
        self.get_organization().click()
        self.get_organization().send_keys(organition)
        self.get_organization().send_keys(Keys.TAB)

    def enter_based(self, based):
        self.get_based().click()
        self.get_based().send_keys(based)
        self.get_based().send_keys(Keys.TAB)

    def addcompany(self, companyname, jobtype, experience, organization, based):
        for i in range(3):
            self.click_addcompanybutton()
            self.enter_companyname(companyname)
            self.enter_jobtype(jobtype)
            self.enter_experience(experience)
            self.enter_organization(organization)
            self.enter_based(based)
            self.save()
            time.sleep(3)
            self.next()
