import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.Basedriver import BaseDriver


class Certificate(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    certificate_dashboard = "//*[text()='Certification']"
    add_certificate = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button[1]"
    title = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]//input"
    institution = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]//input"
    save_certificate = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/button"
    startmonth = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]//select"
    startyear = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]//input"
    endmonth = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]//select"
    endyear = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]//input"
    skill = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]//input"
    add_skill = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]//button"
    project_description = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]//p"
    image = "document.getElementsByTagName('u')[0]"
    """GETTERS"""
    def get_certificatedashboard(self):
        return self.element_to_click(By.XPATH, self.certificate_dashboard)

    def get_addcertificate(self):
        return self.element_to_click(By.XPATH, self.add_certificate)

    def get_title(self):
        return self.element_to_click(By.XPATH, self.title)

    def get_institution(self):
        return self.element_to_click(By.XPATH, self.institution)

    def get_startmonth(self):
        return self.element_to_click(By.XPATH, self.startmonth)

    def get_startyear(self):
        return self.element_to_click(By.XPATH, self.startyear)

    def get_endmonth(self):
        return self.element_to_click(By.XPATH, self.endmonth)

    def get_endyear(self):
        return self.element_to_click(By.XPATH, self.endyear)

    def get_skill(self):
        return self.element_to_click(By.XPATH, self.skill)

    def get_addskill(self):
        return self.element_to_click(By.XPATH, self.add_skill)

    def get_projectdescription(self):
        return self.element_to_click(By.XPATH, self.project_description)

    def get_savecertificate(self):
        return self.element_to_click(By.XPATH, self.save_certificate)

    """SETTERS"""
    def click_certificatedashboard(self):
        self.get_certificatedashboard().click()

    def click_addcertificate(self):
        self.get_addcertificate().click()

    def enter_title(self, title):
        self.get_title().click()
        self.get_title().send_keys(title)
        self.get_title().send_keys(Keys.TAB)

    def enter_institution(self, institution):
        self.get_institution().click()
        self.get_institution().send_keys(institution)
        self.get_institution().send_keys(Keys.TAB)

    def enter_durationfrom(self, year):
        self.get_startmonth().click()
        for i in range(2):
            self.get_startmonth().send_keys(Keys.ARROW_DOWN)
        self.get_startmonth().send_keys(Keys.ENTER)
        self.get_startyear().send_keys(year)

    def enter_durationto(self, year):
        self.get_endmonth().click()
        for i in range(3):
            self.get_endmonth().send_keys(Keys.ARROW_DOWN)
        self.get_endmonth().send_keys(Keys.ENTER)
        self.get_endyear().send_keys(year)

    def enter_skill(self, skill):
        self.get_skill().click()
        self.get_skill().send_keys(skill)
        self.get_skill().send_keys(Keys.TAB)

    def click_addskill(self):
        self.get_addskill().click()

    def enter_projectdescription(self, description):
        self.get_projectdescription().click()
        self.get_projectdescription().send_keys(description)

    def click_savecertrificate(self):
        self.get_savecertificate().click()

    def certificate(self, i, title, institution, durationfrom, durationto, skill, description):
        self.click_addcertificate()
        self.enter_title(title)
        self.enter_institution(institution)
        self.enter_durationfrom(durationfrom)
        self.enter_durationto(durationto)
        self.enter_skill(skill)
        self.click_addskill()
        self.enter_projectdescription(description)
        self.javascript_link(self.image)
        self.click_savecertrificate()
        time.sleep(5)
        if i <= 1:
            self.next()
            self.back()
        else:
            self.next()
