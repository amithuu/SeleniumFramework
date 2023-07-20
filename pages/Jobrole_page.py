import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

from base.Basedriver import BaseDriver


class JobRole(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    experience_editprofiles = "//*[text()='Experience']"

    addcompany_button = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"

    company_name = "//div[@id='root']/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]//input"
    companyname_list = "//div[@id='root']/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]//li/div"

    nature_work = "//div[@id='root']/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]//input"
    naturework_list = "//div[@id='root']/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[2]//div/div/li/div"

    industry = "//div[@id='root']/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]//input"
    industry_list = "//div[@id='root']/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]//div/div/li/div"

    organization_type = "//div[@id='root']/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]//input"
    organization_list = "//div[@id='root']/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/div/div/div[2]//div/div/li/div"

    based = "//div[@id='root']/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]//input"
    based_list = "//div[@id='root']/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[2]//div/div/li/div"

    save_next = "//button[text()='Save and Next']"

    addrole_button = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div/div[{s+1}]//ul//button"
    designation = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[1]/div[1]/div[1]//input"
    management_level = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[1]/div[2]/div[1]//input"
    location = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[2]/div[1]/div[1]//input"
    functional_area = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[2]/div[2]/div[1]//input"
    skill = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[3]/div[2]/div[1]//input"
    expertise = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[3]/div[2]/div[2]//input"
    addskill_button = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[3]/div[2]/div[2]//button"
    start_date = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[4]/div[1]//select"
    start_year = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[4]/div[1]//input"
    end_date = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[4]/div[2]//select"
    end_year = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[4]/div[2]//input"
    start_salary = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[5]/div[1]//input"
    end_salary = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[5]/div[2]//input"
    generate_suggestion = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[6]/div/div[2]//button"
    save_role = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/button"
    back_to_company = "//*[@class='css-hboir5']//button"

    """GETTERS"""
    def get_experience_dashbaord(self):
        return self.element_to_click(By.XPATH, self.experience_editprofiles)

    def get_addcompanybutton(self):
        return self.element_to_click(By.XPATH, self.addcompany_button)

    def get_companyname(self):
        return self.element_to_click(By.XPATH, self.company_name)

    def get_company_list(self):
        return self.presence_of_all_element(By.XPATH, self.companyname_list)

    def get_nature_of_work(self):
        return self.element_to_click(By.XPATH, self.nature_work)

    def get_naturework_list(self):
        return self.presence_of_all_element(By.XPATH, self.naturework_list)

    def get_experience(self):
        return self.element_to_click(By.XPATH, self.industry)

    def get_organization(self):
        return self.element_to_click(By.XPATH, self.organization_type)

    def get_based(self):
        return self.element_to_click(By.XPATH, self.based)

    def get_addrolebutton(self):
        return self.element_to_click(By.XPATH, self.addrole_button)

    def get_designation(self):
        return self.element_to_click(By.XPATH, self.designation)

    def get_managementlevel(self):
        return self.element_to_click(By.XPATH, self.management_level)

    def get_location(self):
        return self.element_to_click(By.XPATH, self.location)

    def get_functionalarea(self):
        return self.element_to_click(By.XPATH, self.functional_area)

    def get_skill(self):
        return self.element_to_click(By.XPATH, self.skill)

    def get_expertise(self):
        return self.element_to_click(By.XPATH, self.expertise)

    def get_addskillbutton(self):
        return self.element_to_click(By.XPATH, self.addskill_button)

    def get_startdate(self):
        return self.element_to_click(By.XPATH, self.start_date)

    def get_startyear(self):
        return self.element_to_click(By.XPATH, self.start_year)

    def get_enddate(self):
        return self.element_to_click(By.XPATH, self.end_date)

    def get_endyear(self):
        return self.element_to_click(By.XPATH, self.end_year)

    def get_startsalary(self):
        return self.element_to_click(By.XPATH, self.start_salary)

    def get_endsalary(self):
        return self.element_to_click(By.XPATH, self.end_salary)

    def get_generatesuggestion(self):
        return self.element_to_click(By.XPATH, self.generate_suggestion)

    def get_backtocompany(self):
        return self.element_to_click(By.XPATH, self.back_to_company)

    def get_save_next(self):
        return self.element_to_click(By.XPATH, self.save_next)

    def get_saverole(self):
        return self.element_to_click(By.XPATH, self.save_role)

    """SETTERS"""
    def click_experience_editprofile(self):
        self.get_experience_dashbaord().click()

    def click_addcompanybutton(self):
        self.get_addcompanybutton().click()

    def enter_companyname(self, companyname):
        self.get_companyname().click()
        self.get_companyname().send_keys(companyname)
        time.sleep(2)
        company_name = self.get_company_list()

        for companies in company_name:
            if companyname in companies.text.casefold():
                companies.click()
                break

    def enter_nature_of_work(self, jobtype):
        self.get_nature_of_work().click()
        self.get_nature_of_work().send_keys(jobtype)
        time.sleep(2)
        job_type = self.get_naturework_list()

        for naturework in job_type:
            if jobtype in naturework.text.casefold():
                naturework.click()
                break

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

    def click_savenext(self):
        self.get_save_next().click()

    def enter_designation(self, designation):
        self.get_designation().click()
        self.get_designation().send_keys(designation)
        self.get_designation().send_keys(Keys.TAB)

    def enter_managementlevel(self, managementlevel):
        self.get_managementlevel().click()
        self.get_managementlevel().send_keys(managementlevel)
        self.get_managementlevel().send_keys(Keys.TAB)

    def enter_location(self, location):
        self.get_location().click()
        self.get_location().send_keys(Keys.CONTROL + "a")
        self.get_location().send_keys(location)
        self.get_location().send_keys(Keys.BACK_SPACE)
        time.sleep(3)

    def enter_functionalarea(self, functionalarea):
        self.get_functionalarea().click()
        self.get_functionalarea().send_keys(functionalarea)
        self.get_functionalarea().send_keys(Keys.TAB)

    def enter_skill(self, skill):
        self.get_skill().click()
        self.get_skill().send_keys(skill)
        self.get_skill().send_keys(Keys.TAB)

    def enter_expertise(self, expertise):
        self.get_expertise().click()
        self.get_expertise().send_keys(expertise)
        self.get_expertise().send_keys(Keys.TAB)

    def click_addskillbutton(self):
        self.get_addskillbutton().click()

    def enter_startdate(self, startyear):
        self.get_startdate().click()
        self.get_startdate().send_keys(Keys.ARROW_DOWN)
        self.get_startdate().send_keys(Keys.ENTER)
        self.get_startyear().send_keys(startyear)

    def enter_enddate(self, endyear):
        self.get_enddate().click()
        self.get_enddate().send_keys(Keys.ARROW_DOWN)
        self.get_enddate().send_keys(Keys.ENTER)
        self.get_endyear().send_keys(endyear)

    def enter_startsalary(self, startsalary):
        self.get_startsalary().click()
        self.get_startsalary().send_keys(startsalary)
        self.get_startsalary().send_keys(Keys.TAB)
        self.get_startsalary().send_keys(startsalary)

    def enter_endsalary(self, endsalary):
        self.get_endsalary().click()
        self.get_endsalary().send_keys(endsalary)
        self.get_endsalary().send_keys(Keys.TAB)
        self.get_endsalary().send_keys(endsalary)

    def click_generatesuggestion(self):
        self.get_generatesuggestion().click()
        for j in range(1, 4):
            self.element_to_click(By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[6]/div/div[2]/div/div/div[{j}]//button").click()
            time.sleep(1)

    def click_saverole(self):
        return self.get_saverole().click()

    def click_backtocompany(self):
        self.get_backtocompany().click()

    # " jobtype, experience, organization, based, designation, managemnetlevel, location, functionalarea, skill, expertise, startyear, endyear, startsalary, endsalary"
    def addcompany(self, s, companyname, jobtype):
        # self.click_addcompanybutton()
        self.enter_companyname(companyname)
        self.enter_nature_of_work(jobtype)
        self.click_savenext()
        time.sleep(2)
        # self.enter_experience(experience)
        # self.enter_organization(organization)
        # self.enter_based(based)
        # # add job role
        # for a in range(1, 3):
        #     self.element_to_click(By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div/div[{s+1}]//ul//button").click()
        #     self.enter_designation(designation)
        #     self.enter_managementlevel(managemnetlevel)
        #     self.enter_location(location)
        #     self.enter_functionalarea(functionalarea)
        #     self.enter_skill(skill)
        #     self.enter_expertise(expertise)
        #     self.enter_startdate(startyear)
        #     self.enter_enddate(endyear)
        #     self.enter_startsalary(startsalary)
        #     self.enter_endsalary(endsalary)
        #     # self.click_generatesuggestion()
        #     self.click_saverole()
        #     time.sleep(3)
        #     self.click_backtocompany()



