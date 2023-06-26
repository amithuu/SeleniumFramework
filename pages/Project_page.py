import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from base.Basedriver import BaseDriver


class Projects(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    projects_dashboard = "//p[text()='Projects']"
    add_projects = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button[1]"
    project_name = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/input"
    start_month = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/form/div/div[2]/div[1]//select"
    start_year = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/form/div/div[2]/div[1]//input"
    end_month = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/form/div/div[2]/div[2]//select"
    end_year = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/form/div/div[2]/div[2]//input"
    associated_with = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/form/div/div[3]/div[1]//input"
    project_link = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/form/div/div[3]/div[2]//input"
    description = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[4]//p"
    skill = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[5]/div[2]/div[1]//input"
    skill_slider = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[5]/div[2]/div[2]//div[@role='slider']"
    add_button = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[5]/div[2]/div[2]//button"
    description_skillapplication = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[6]//p"
    save_project = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/form/div/button"

    """GETTERS"""

    def get_projectdasboard(self):
        return self.element_to_click(By.XPATH, self.projects_dashboard)

    def get_addprojects(self):
        return self.element_to_click(By.XPATH, self.add_projects)

    def get_name(self):
        return self.element_to_click(By.XPATH, self.project_name)

    def get_startmonth(self):
        return self.element_to_click(By.XPATH, self.start_month)

    def get_startyear(self):
        return self.element_to_click(By.XPATH, self.start_year)

    def get_endmonth(self):
        return self.element_to_click(By.XPATH, self.end_month)

    def get_endyear(self):
        return self.element_to_click(By.XPATH, self.end_year)

    def get_associatedwith(self):
        return self.element_to_click(By.XPATH, self.associated_with)

    def get_projectlink(self):
        return self.element_to_click(By.XPATH, self.project_link)

    def get_description(self):
        return self.element_to_click(By.XPATH, self.description)

    def get_skill(self):
        return self.element_to_click(By.XPATH, self.skill)

    def get_skillslider(self):
        return self.element_to_click(By.XPATH, self.skill_slider)

    def get_addbutton(self):
        return self.element_to_click(By.XPATH, self.add_button)

    def get_descriptionskillapplication(self):
        return self.element_to_click(By.XPATH, self.description_skillapplication)

    def get_saveproject(self):
        return self.element_to_click(By.XPATH, self.save_project)

    def click_addprojects(self):
        self.get_addprojects().click()

    """SETTERS"""

    def click_projectdashboard(self):
        self.get_projectdasboard().click()

    def enter_name(self, name):
        self.get_name().click()
        self.get_name().send_keys(name)
        self.get_name().send_keys(Keys.TAB)

    def enter_startdate(self, year):
        self.get_startmonth().click()
        self.get_startmonth().send_keys(Keys.ARROW_DOWN)
        self.get_startmonth().send_keys(Keys.ARROW_DOWN)
        self.get_startmonth().send_keys(Keys.ENTER)
        self.get_startyear().send_keys(year)

    def enter_enddate(self, year):
        self.get_endmonth().click()
        self.get_endmonth().send_keys(Keys.ARROW_DOWN)
        self.get_endmonth().send_keys(Keys.ARROW_DOWN)
        self.get_endmonth().send_keys(Keys.ARROW_DOWN)
        self.get_endmonth().send_keys(Keys.ENTER)
        self.get_endyear().send_keys(year)

    def enter_associatedwith(self):
        self.get_associatedwith().click()
        self.get_associatedwith().send_keys(Keys.ARROW_DOWN)
        self.get_associatedwith().send_keys(Keys.ENTER)

    def enter_projectlink(self, link):
        self.get_projectlink().click()
        self.get_projectlink().send_keys(link)

    def enter_description(self, description):
        self.get_description().click()
        self.get_description().send_keys(description)

    def enter_skill(self, skill):
        self.get_skill().click()
        self.get_skill().send_keys(skill)
        self.get_skill().send_keys(Keys.TAB)

    def slide_skillslider(self, j):
        ActionChains(self.driver).move_to_element(self.get_skillslider()).pause(1).click_and_hold(self.get_skillslider()).move_by_offset((35 * (j + 1)), 0).release().perform()
        time.sleep(1)

    def click_addbutton(self):
        self.get_addbutton().click()

    def enter_descriptionskillapplication(self, descriptionskillapplication):
        self.get_descriptionskillapplication().click()
        self.get_descriptionskillapplication().send_keys(descriptionskillapplication)

    def click_saveproject(self):
        self.get_saveproject().click()

    def project(self, name, startyear, endyear, link, description, skill, j, descriptionskillapplication):
        self.click_addprojects()
        self.enter_name(name)
        self.enter_startdate(startyear)
        self.enter_enddate(endyear)
        self.enter_associatedwith()
        self.enter_projectlink(link)
        self.enter_description(description)
        self.enter_skill(skill)
        self.slide_skillslider(j)
        self.click_addbutton()
        self.enter_descriptionskillapplication(descriptionskillapplication)
        self.click_saveproject()
        time.sleep(5)
        if j == 0:
            self.next()
            self.back()
        elif j == 1:
            self.next()
            self.discrad()
            self.back()
        else:
            self.next()


