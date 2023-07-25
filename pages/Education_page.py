import time
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver

class Education(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    education_editprofiles = "//*[text()='Education']"

    add_another_education = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div//button"

    degree = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[1]/div[1]//input"
    degree_list = "//form/div/div[1]/div[1]/div/div/div[2]//li/div"

    university = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[1]/div[2]//input"
    university_list = "//form/div/div[1]/div[2]/div/div/div[2]//li/div"

    location = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[1]/div[3]//input"
    location_list = "//form/div/div[1]/div[3]/div/div/div//ul/li"

    cgpa = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[1]/div[4]//input"

    start_month = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[2]/div[1]//select"
    start_year = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[2]/div[1]//input"

    end_month = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[2]/div[2]//select"
    end_year = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[2]/div[2]//input"

    project_description = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[3]//p"
    extra_circular = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[4]//p"
    image = "document.getElementsByTagName('u')[0]"
    save = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]//form/div/div[6]//button[2]"

    """GETTERS"""
    def get_educationeditprofile(self):
        return self.element_to_click(By.XPATH, self.education_editprofiles)

    def get_add_another_education(self):
        return self.element_to_click(By.XPATH, self.add_another_education)

    def get_degree(self):
        return self.element_to_click(By.XPATH, self.degree)

    def get_degree_list(self):
        return self.presence_of_all_element(By.XPATH, self.degree_list)

    def get_university(self):
        return self.element_to_click(By.XPATH, self.university)

    def get_university_list(self):
        return self.presence_of_all_element(By.XPATH, self.university_list)

    def get_location(self):
        return self.element_to_click(By.XPATH, self.location)

    def get_location_list(self):
        return self.presence_of_all_element(By.XPATH, self.location_list)

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

    def get_project_description(self):
        return self.element_to_click(By.XPATH, self.project_description)

    def get_extracircular(self):
        return self.element_to_click(By.XPATH, self.extra_circular)

    def get_image(self):
        return self.javascript_link(self.image)

    def get_save(self):
        return self.element_to_click(By.XPATH, self.save)

    """SETTERS"""
    def click_education_editprofiles(self):
        self.get_educationeditprofile().click()

    def click_add_another_education(self):
        self.get_add_another_education().click()

    def enter_degree(self, degree):
        self.get_degree().click()
        self.get_degree().send_keys(degree)

        time.sleep(1)
        qualification = self.get_degree_list()

        for degrees in qualification:
            if degree in degrees.text.casefold():
                degrees.click()
                break

    def enter_university(self, university):
        self.get_university().click()
        self.get_university().send_keys(university)
        time.sleep(1)
        institution = self.get_university_list()

        for universitys in institution:
            if university in universitys.text.casefold():
                universitys.click()
                break

    def enter_location(self, location):
        self.get_location().click()
        self.get_location().send_keys(location)
        time.sleep(2)
        locations = self.get_location_list()

        for location_list in locations:
            if location in location_list.text.casefold():
                location_list.click()
                break

    def enter_cgpa(self, cgpa):
        self.get_cgpa().click()
        self.get_cgpa().send_keys(cgpa)

    def select_durationfrom(self, month, year):
        self.get_startmonth().click()
        self.select_options(self.get_startmonth(), month)
        self.get_startyear().send_keys(year)

    def select_durationto(self, month, year):
        self.get_endmonth().click()
        self.select_options(self.get_endmonth(), month)
        self.get_endyear().send_keys(year)

    def enter_project_description(self, description):
        # self.get_project_description().click()
        self.get_project_description().send_keys(description)

    def enter_extracircular(self, extracircular):
        # self.get_extracircular().click()
        self.get_extracircular().send_keys(extracircular)

    def click_image(self):
        self.get_image()

    def save_button(self):
        self.get_save().click()
        time.sleep(3)
        self.driver.refresh()

    def education(self, user, degree, university, location, cgpa, month, year, month1, year1, project_description, extracircular):
        self.click_education_editprofiles()
        time.sleep(3)

        if user == "new":
            self.enter_degree(degree)
            self.enter_university(university)
            self.enter_location(location)
            self.enter_cgpa(cgpa)
            self.select_durationfrom(month, year)
            self.select_durationto(month1, year1)
            self.enter_project_description(project_description)
            self.enter_extracircular(extracircular)
            self.click_image()
            self.save_button()
            self.click_add_another_education()

        elif user == "old":
            self.click_add_another_education()
            self.enter_degree(degree)
            self.enter_university(university)
            self.enter_location(location)
            self.enter_cgpa(cgpa)
            self.select_durationfrom(month, year)
            self.select_durationto(month1, year1)
            self.enter_project_description(project_description)
            self.enter_extracircular(extracircular)
            self.click_image()
            self.save_button()
