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
    projects_editprofiles = "//p[text()='Projects']"

    add_another_projects = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div//button"

    project_name = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[1]//input"

    start_month = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[2]/div[1]//select"
    start_year = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[2]/div[1]//input"
    end_month = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[2]/div[2]//select"
    end_year = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[2]/div[2]//input"

    associated_with = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[3]/div[1]//input"
    associated_with_list = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[3]//li/div"

    project_link = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[3]/div[2]//input"
    description = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[4]//p"

    skill = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[5]/div[2]/div[1]//input"
    skill_list = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[5]//li/div"

    skill_slider = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[5]/div[2]/div[2]//div[@role='slider']"

    skillapplication_descsription = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[6]//p"
    save = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[7]//button[2]"

    """GETTERS"""

    def get_project_editprofiles(self):
        return self.element_to_click(By.XPATH, self.projects_editprofiles)

    def get_add_another_projects(self):
        return self.element_to_click(By.XPATH, self.add_another_projects)

    def get_project_name(self):
        return self.element_to_click(By.XPATH, self.project_name)

    def get_startmonth(self):
        return self.element_to_click(By.XPATH, self.start_month)

    def get_startyear(self):
        return self.element_to_click(By.XPATH, self.start_year)

    def get_endmonth(self):
        return self.element_to_click(By.XPATH, self.end_month)

    def get_endyear(self):
        return self.element_to_click(By.XPATH, self.end_year)

    def get_associated_with(self):
        return self.element_to_click(By.XPATH, self.associated_with)

    def get_associated_with_list(self):
        return self.presence_of_all_element(By.XPATH, self.associated_with_list)

    def get_project_link(self):
        return self.element_to_click(By.XPATH, self.project_link)

    def get_description(self):
        return self.element_to_click(By.XPATH, self.description)

    def get_skill(self):
        return self.element_to_click(By.XPATH, self.skill)

    def get_skill_list(self):
        return self.presence_of_all_element(By.XPATH, self.skill_list)

    def get_skill_slider(self):
        return self.element_to_click(By.XPATH, self.skill_slider)

    def get_skillapplication_description(self):
        return self.element_to_click(By.XPATH, self.skillapplication_descsription)

    def get_save_button(self):
        return self.element_to_click(By.XPATH, self.save)

    """SETTERS"""

    def click_project_editprofiles(self):
        self.get_project_editprofiles().click()
        time.sleep(2)

    def enter_project_name(self, name):
        self.get_project_name().click()
        self.get_project_name().send_keys(name)

    def enter_start_date(self, month, year):
        self.get_startmonth().click()
        self.select_options(self.get_startmonth(), month)
        self.get_startyear().send_keys(year)

    def enter_end_date(self, month, year):
        self.get_endmonth().click()
        self.select_options(self.get_endmonth(), month)
        self.get_endyear().send_keys(year)

    def enter_associated_with(self, associated_with):
        self.get_associated_with().click()
        time.sleep(1)
        associated_withs = self.get_associated_with_list()

        for associates in associated_withs:
            if associated_with in associates.text.casefold():
                associates.click()
                break

    def enter_project_link(self, link):
        self.get_project_link().send_keys(link)

    def enter_description(self, description):
        self.get_description().send_keys(description)

    def enter_skill(self, skill):
        self.get_skill().click()
        self.get_skill().send_keys(skill)
        time.sleep(1)
        skills = self.get_skill_list()

        for skil in skills:
            if skill in skil.text.casefold():
                skil.click()
                break

    def slide_skill_slider(self, j):
        ActionChains(self.driver).move_to_element(self.get_skill_slider()).pause(1).click_and_hold(self.get_skill_slider()).move_by_offset((35 * (j + 1)), 0).release().perform()
        time.sleep(1)

    def enter_skillapplication_description(self, skillapplication_description):
        self.get_skillapplication_description().click()
        self.get_skillapplication_description().send_keys(skillapplication_description)

    def click_save_button(self):
        self.get_save_button().click()
        time.sleep(3)
        self.driver.refresh()

    def click_add_another_project(self):
        self.get_add_another_projects().click()

    def project(self, user, project_name, month, year, month1, year1, associated_with, link, description, skill, j, skillapplication_description):
        self.click_project_editprofiles()

        if user == "new":
            self.enter_project_name(project_name)
            self.enter_start_date(month, year)
            self.enter_end_date(month1, year1)
            self.enter_associated_with(associated_with)
            self.enter_project_link(link)
            self.enter_description(description)
            self.enter_skill(skill)
            self.slide_skill_slider(j)
            self.enter_skillapplication_description(skillapplication_description)
            self.click_save_button()
            self.click_add_another_project()

        elif user == "old":
            self.click_add_another_project()
            self.enter_project_name(project_name)
            self.enter_start_date(month, year)
            self.enter_end_date(month1, year1)
            self.enter_associated_with(associated_with)
            self.enter_project_link(link)
            self.enter_description(description)
            self.enter_skill(skill)
            self.slide_skill_slider(j)
            self.enter_skillapplication_description(skillapplication_description)
            self.click_save_button()


