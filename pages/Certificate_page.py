import time
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver

class Certificate(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    certificate_editprofiles = "//*[text()='Certification']"

    add_another_certificate = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]//button"

    certificate_title = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]//input"

    certificate_institution = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[2]//input"

    save_certificate = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/button"

    startmonth = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]//select"
    startyear = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]//input"

    endmonth = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]//select"
    endyear = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]//input"

    skill = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]//input"
    skill_list = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]//li/div"

    project_description = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[4]//p"

    image = "document.getElementsByTagName('u')[0]"
    save = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[6]//button[2]"

    """GETTERS"""
    def get_certificate_editprofile(self):
        return self.element_to_click(By.XPATH, self.certificate_editprofiles)

    def get_add_another_certificate(self):
        return self.element_to_click(By.XPATH, self.add_another_certificate)

    def get_certificate_title(self):
        return self.element_to_click(By.XPATH, self.certificate_title)

    def get_certificate_institution(self):
        return self.element_to_click(By.XPATH, self.certificate_institution)

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

    def get_skill_list(self):
        return self.presence_of_all_element(By.XPATH, self.skill_list)

    def get_project_description(self):
        return self.element_to_click(By.XPATH, self.project_description)

    def get_save_button(self):
        return self.element_to_click(By.XPATH, self.save)

    def get_image(self):
        return self.javascript_link(self.image)

    """SETTERS"""
    def click_certificate_editprofiles(self):
        self.get_certificate_editprofile().click()
        time.sleep(1)

    def click_add_another_certificate(self):
        self.get_add_another_certificate().click()
        time.sleep(1)

    def enter_certificate_title(self, title):
        self.get_certificate_title().send_keys(title)

    def enter_certificate_institution(self, institution):
        self.get_certificate_institution().send_keys(institution)

    def select_durationfrom(self, month, year):
        self.get_startmonth().click()
        self.select_options(self.get_startmonth(), month)
        self.get_startyear().send_keys(year)

    def select_durationto(self, month, year):
        self.get_endmonth().click()
        self.select_options(self.get_endmonth(), month)
        self.get_endyear().send_keys(year)

    def enter_skill(self, skill):
        self.get_skill().send_keys(skill)
        time.sleep(1)
        skills = self.get_skill_list()

        for skil in skills:
            if skill in skil.text.casefold():
                skil.click()
                break

    def enter_project_description(self, description):
        self.get_project_description().send_keys(description)

    def click_image(self):
        self.get_image()

    def click_save(self):
        self.get_save_button().click()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(1)

    def certificate(self, i, user, title, institution, month, year, month1, year1, skill, description):
        self.click_certificate_editprofiles()

        if user == "new":
            if i == 0:
                self.enter_certificate_title(title)
                self.enter_certificate_institution(institution)
                self.select_durationfrom(month, year)
                self.select_durationto(month1, year1)
                self.enter_skill(skill)
                self.enter_project_description(description)
                self.click_image()
                self.click_save()
            else:
                self.click_add_another_certificate()
                self.enter_certificate_title(title)
                self.enter_certificate_institution(institution)
                self.select_durationfrom(month, year)
                self.select_durationto(month1, year1)
                self.enter_skill(skill)
                self.enter_project_description(description)
                self.click_image()
                self.click_save()

        elif user == "old":
            self.click_add_another_certificate()
            self.enter_certificate_title(title)
            self.enter_certificate_institution(institution)
            self.select_durationfrom(month, year)
            self.select_durationto(month1, year1)
            self.enter_skill(skill)
            self.enter_project_description(description)
            self.click_image()
            self.click_save()
