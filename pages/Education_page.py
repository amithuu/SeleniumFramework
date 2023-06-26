import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.Basedriver import BaseDriver
class Education(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    education_dashboard = "//*[text()='Education']"
    add_education = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button[1]"
    degree = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[1]//input"
    university = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[2]//input"
    location = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[1]//input"
    cgpa = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[2]//input"
    start_month = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/div[1]//select"
    start_year = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/div[1]//input"
    end_month = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/div[2]//select"
    end_year = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/div[2]//input"
    description = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[4]//p"
    extra_circular = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[5]//p"
    save_education = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/button"
    image = "document.getElementsByTagName('u')[0]"
    """GETTERS"""
    def get_educationdashboard(self):
        return self.element_to_click(By.XPATH, self.education_dashboard)

    def get_addeducation(self):
        return self.element_to_click(By.XPATH, self.add_education)

    def get_degree(self):
        return self.element_to_click(By.XPATH, self.degree)

    def get_university(self):
        return self.element_to_click(By.XPATH, self.university)

    def get_location(self):
        return self.element_to_click(By.XPATH, self.location)

    def get_cgpa(self):
        return self.element_to_click(By.XPATH, self.cgpa)

    def get_startmonth(self):
        return self.element_to_click(By.XPATH, self.start_month)

    def get_startyear(self):
        return self.element_to_click(By.XPATH, self.start_year)

    def get_endmonth(self):
        return self.element_to_click(By.XPATH, self.end_month)

    def get_endyear(self):
        return self.element_to_click(By.XPATH, self.end_year)

    def get_projectdescription(self):
        return self.element_to_click(By.XPATH, self.description)

    def get_extracircular(self):
        return self.element_to_click(By.XPATH, self.extra_circular)

    def get_image(self):
        return self.javascript_link(self.image)

    def get_saveeducation(self):
        return self.element_to_click(By.XPATH, self.save_education)

    """SETTERS"""
    def click_educationdashboard(self):
        self.get_educationdashboard().click()

    def click_addeducation(self):
        self.get_addeducation().click()

    def enter_degree(self, degree):
        self.get_degree().click()
        self.get_degree().send_keys(degree)
        self.get_degree().send_keys(Keys.TAB)

    def enter_university(self, university):
        self.get_university().click()
        self.get_university().send_keys(university)
        self.get_university().send_keys(Keys.TAB)

    def enter_location(self, location):
        self.get_location().click()
        self.get_location().send_keys(location)
        self.get_location().send_keys(Keys.BACK_SPACE)
        time.sleep(3)

    def enter_cgpa(self, cgpa):
        self.get_cgpa().click()
        self.get_cgpa().send_keys(cgpa)

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

    def enter_projectdescription(self, description):
        self.get_projectdescription().click()
        self.get_projectdescription().send_keys(description)

    def enter_extracircular(self, extracircular):
        self.get_extracircular().click()
        self.get_extracircular().send_keys(extracircular)

    def click_image(self):
        self.get_image().click()

    def click_saveeducation(self):
        self.get_saveeducation().click()

    def education(self, i, degree, university, location, cgpa, fromyear, toyear, description, extracircular):
        self.click_addeducation()
        self.enter_degree(degree)
        self.enter_university(university)
        self.enter_location(location)
        self.enter_cgpa(cgpa)
        self.enter_durationfrom(fromyear)
        self.enter_durationto(toyear)
        self.enter_projectdescription(description)
        self.enter_extracircular(extracircular)
        # self.click_image()
        self.click_saveeducation()
        time.sleep(5)
        if i <= 1:
            self.next()
            self.back()
        else:
            self.next()




