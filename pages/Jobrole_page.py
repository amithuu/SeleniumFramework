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

    save_next = "//*[@id ='root']/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[4]//button[2]"

    add_another_job_role = "//button[text() = 'Add another job role']"

    add_another_company = "//*[@id ='root']/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]//button"

    addrole_button = "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div/div[{s+1}]//ul//button"

    back_to_company = "//*[@id = 'root']/div[2]/div[2]/div/div[2]/div/div[2]//button"

    designation = "//form/div/div[1]/div[1]//input"
    designation_list = "//form/div/div[1]/div[1]/div/div/div[2]//div/div/li/div"

    management_level = "//form/div/div[1]/div[2]//input"
    managementlevel_list = "//form/div/div[1]/div[2]/div/div/div[2]//div/div/li/div"

    location = "//*[@placeholder ='Search Location']"
    location_list = "//form/div/div[1]/div[3]/div/div/div//ul/li"

    functional_area = "//form/div/div[1]/div[4]//input"
    functionalarea_list = "//form/div/div[1]/div[4]/div/div/div[2]//div/div/li/div"

    skill = "//form/div/div[2]/div[2]/div[1]//input"
    skill_list = "//form/div/div[2]/div[2]/div[1]/div/div/div/div[2]//div/div/li/div"

    expertise = "//form/div/div[2]/div[2]/div[2]//input"
    expertise_list = "//form/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]//div/div/li/div"

    start_month = "//form/div/div[3]/div[1]//select"
    start_year = "//form/div/div[3]/div[1]//input"

    end_month = "//form/div/div[3]/div[2]//select"
    end_year = "//form/div/div[3]/div[2]//input"

    start_salary = "//form/div/div[4]/div[1]//input"
    end_salary = "//form/div/div[4]/div[2]//input"

    generate_suggestion = "//form/div/div[5]/div/div[2]//button"

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

    def get_industry(self):
        return self.element_to_click(By.XPATH, self.industry)

    def get_industry_list(self):
        return self.presence_of_all_element(By.XPATH, self.industry_list)

    def get_organization(self):
        return self.element_to_click(By.XPATH, self.organization_type)

    def get_organization_list(self):
        return self.presence_of_all_element(By.XPATH, self.organization_list)

    def get_based(self):
        return self.element_to_click(By.XPATH, self.based)

    def get_based_list(self):
        return self.presence_of_all_element(By.XPATH, self.based_list)

    def get_addrolebutton(self):
        return self.element_to_click(By.XPATH, self.addrole_button)

    def get_designation(self):
        return self.element_to_click(By.XPATH, self.designation)

    def get_designation_list(self):
        return self.presence_of_all_element(By.XPATH, self.designation_list)

    def get_managementlevel(self):
        return self.element_to_click(By.XPATH, self.management_level)

    def get_managementlevel_list(self):
        return self.presence_of_all_element(By.XPATH, self.managementlevel_list)

    def get_location(self):
        return self.element_to_click(By.XPATH, self.location)

    def get_location_list(self):
        return self.presence_of_all_element(By.XPATH, self.location_list)

    def get_functionalarea(self):
        return self.element_to_click(By.XPATH, self.functional_area)

    def get_functionalarea_list(self):
        return self.presence_of_all_element(By.XPATH, self.functionalarea_list)

    def get_skill(self):
        return self.element_to_click(By.XPATH, self.skill)

    def get_skill_list(self):
        return self.presence_of_all_element(By.XPATH, self.skill_list)

    def get_expertise(self):
        return self.element_to_click(By.XPATH, self.expertise)

    def get_expertise_list(self):
        return self.presence_of_all_element(By.XPATH, self.expertise_list)

    def get_startmonth(self):
        return self.element_to_click(By.XPATH, self.start_month)

    def get_startyear(self):
        return self.element_to_click(By.XPATH, self.start_year)

    def get_endmonth(self):
        return self.element_to_click(By.XPATH, self.end_month)

    def get_endyear(self):
        return self.element_to_click(By.XPATH, self.end_year)

    def get_startsalary(self):
        return self.element_to_click(By.XPATH, self.start_salary)

    def get_endsalary(self):
        return self.element_to_click(By.XPATH, self.end_salary)

    def get_generatesuggestion(self):
        return self.element_to_click(By.XPATH, self.generate_suggestion)

    def get_save_next(self):
        return self.element_to_click(By.XPATH, self.save_next)

    def get_add_another_job_role(self):
        return self.element_to_click(By.XPATH, self.add_another_job_role)

    def get_add_another_company(self):
        return self.element_to_click(By.XPATH, self.add_another_company)

    def get_back_to_company(self):
        return self.element_to_click(By.XPATH, self.back_to_company)

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

    def enter_industry(self, industry):
        self.get_industry().click()
        self.get_industry().send_keys(industry)
        time.sleep(2)
        industries = self.get_industry_list()

        for industry_list in industries:
            if industry in industry_list.text.casefold():
                industry_list.click()
                break

    def enter_organization(self, organition):
        self.get_organization().click()
        self.get_organization().send_keys(organition)
        time.sleep(2)
        organizations = self.get_organization_list()

        for organization in organizations:
            if organition in organization.text.casefold():
                organization.click()
                break

    def enter_based(self, based):
        self.get_based().click()
        self.get_based().send_keys(based)
        time.sleep(2)
        service_based = self.get_based_list()

        for based_list in service_based:
            if based in based_list.text.casefold():
                based_list.click()
                break

    def click_savenext(self):
        self.get_save_next().click()

    def enter_designation(self, designation):
        self.get_designation().click()
        self.get_designation().send_keys(designation)
        time.sleep(1)
        designations = self.get_designation_list()

        for designation_list in designations:
            if designation in designation_list.text.casefold():
                designation_list.click()
                break

    def enter_managementlevel(self, managementlevel):
        self.get_managementlevel().click()
        self.get_managementlevel().send_keys(managementlevel)
        time.sleep(1)
        manage_list = self.get_managementlevel_list()

        for management_list in manage_list:
            if managementlevel in management_list.text.casefold():
                management_list.click()
                break

    def enter_location(self, location_name):
        self.get_location().click()
        self.get_location().send_keys(location_name)
        time.sleep(2)
        select_location = self.get_location_list()

        for locations in select_location:
            if location_name in locations.text:
                locations.click()
                break

    def enter_functionalarea(self, functionalarea):
        self.get_functionalarea().click()
        self.get_functionalarea().send_keys(functionalarea)
        time.sleep(1)
        functional_area = self.get_functionalarea_list()

        for functionalarea_list in functional_area:
            if functionalarea in functionalarea_list.text.casefold():
                functionalarea_list.click()
                break

    def enter_skill(self, skill):
        self.get_skill().click()
        self.get_skill().send_keys(skill)
        time.sleep(1)
        skills = self.get_skill_list()

        for skill_list in skills:
            if skill in skill_list.text.casefold():
                skill_list.click()
                break

    def enter_expertise(self, expertise):
        self.get_expertise().click()
        self.get_expertise().send_keys(expertise)
        expertises = self.get_expertise_list()

        for expertise_list in expertises:
            if expertise in expertise_list.text.casefold():
                expertise_list.click()
                break

    def select_startmonth(self, startmonth, year):
        self.get_startmonth().click()
        self.select_options(self.get_startmonth(), startmonth)
        time.sleep(1)

        self.get_startyear().send_keys(year)

    def select_endmonth(self, endmonth, year):
        self.get_endmonth().click()
        self.select_options(self.get_endmonth(), endmonth)
        time.sleep(1)

        self.get_endyear().send_keys(year)

    def enter_salary(self, startsalary, endsalary):
        self.get_startsalary().click()
        self.get_startsalary().send_keys(startsalary)
        time.sleep(1)
        self.get_endsalary().click()
        self.get_endsalary().send_keys(endsalary)

    def click_generatesuggestion(self):
        self.get_generatesuggestion().click()
        for j in range(1, 4):
            self.element_to_click(By.XPATH, f"//form/div/div[6]/div/div[2]/div/div/div[{j}]//button").click()
            time.sleep(1)

    def click_add_another_job_role(self):
        self.get_add_another_job_role().click()

    def click_add_another_company(self):
        self.get_add_another_company().click()

    def click_back_to_company(self):
        self.get_back_to_company().click()

    def addcompany(self, user,  companyname, jobtype, industry, organization, based, designation, managementlevel, location, functionalarea, skill, expertise, month, year, month1, year1, startsalary, endsalary):

        if user == "new":
            self.enter_companyname(companyname)
            self.enter_nature_of_work(jobtype)
            self.enter_industry(industry)
            self.enter_organization(organization)
            self.enter_based(based)
            self.click_savenext()
            time.sleep(2)
            self.enter_designation(designation)
            self.enter_managementlevel(managementlevel)
            self.enter_location(location)
            self.enter_functionalarea(functionalarea)
            self.enter_skill(skill)
            self.enter_expertise(expertise)
            self.select_startmonth(month, year)
            self.select_endmonth(month1, year1)
            self.enter_salary(startsalary, endsalary)
            # self.click_generatesuggestion()
            self.save()
            time.sleep(3)
            self.driver.refresh()
            time.sleep(3)
            self.click_back_to_company()
            time.sleep(1)
            self.click_add_another_company()
        else:
            self.click_add_another_company()
            self.enter_companyname(companyname)
            self.enter_nature_of_work(jobtype)
            self.enter_industry(industry)
            self.enter_organization(organization)
            self.enter_based(based)
            self.click_savenext()
            time.sleep(2)
            self.enter_designation(designation)
            self.enter_managementlevel(managementlevel)
            self.enter_location(location)
            self.enter_functionalarea(functionalarea)
            self.enter_skill(skill)
            self.enter_expertise(expertise)
            self.select_startmonth(month, year)
            self.select_endmonth(month1, year1)
            self.enter_salary(startsalary, endsalary)
            # self.click_generatesuggestion()
            self.save()
            time.sleep(3)
            self.driver.refresh()
            time.sleep(5)
            self.click_back_to_company()



