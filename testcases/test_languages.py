import time
import pytest
from pages.Assessment_page import Assessment
from pages.Carriersummary_page import Carrier
from pages.Cognitiveskills_page import CognitiveSkills
from pages.Languages_page import Language
from pages.SignUp_page import Signup
from pages.Welcome_page import Welcome
from pages.Personal_details_page import Personaldetails
from pages.Jobrole_page import JobRole
from pages.Project_page import Projects
from pages.Education_page import Education

# Variables
language = ["kannada", "english", "hindi"]
proficiency = ["beg", "adv", "inter"]
location = ["bangalore", "delhi", "561203"]
companyname = ["IBM", "Google", "Cognizant"]
jobtype = ["full time", "intern", "part time", "freelanc", "contract"]
experience = ["Advanced Technologies", "IT Services", "Agri-business"]
organization = ["startup", "small", "mnc"]
based = ["product", "service", "both"]
date = "25041999"
month = ["jan", "feb", "march", "may", "june", "july"]
year = ["1900", "1910", "1920", "1930", "1940", "2000", "2001", "2002"]
designation = ["Developer", "Automation", "application"]
managementlevel = ["jun", "sen", "mid"]
functionalarea = ["development", "human", "marketing"]
skill = ["java", "python", "c prog", "automation", "php"]
expertise = ["beg", "skil", "expert"]
startsalary = ["12", "3213", "214"]
endsalary = ["21433", "2136832", "812765"]
degree = ["10th", "12th", "bsc", "mca", "phd"]
university = ["bangalore", "delhi", "odisha"]
cgpa = ["7.89", "9.65", "5.98"]
linkdin = "https://www.linkedin.com/in/amith-kulkarni-1326241b4"
headline = "Automation Developer"
firstname = "Amith"
lastname = "talentPlace"
description = ["Listing projects on your resume allows hiring managers", " It's important to list your most relevant projects on your resume.", "List the skills you want to highlight", "Think of the specific projects you want to include."]


@pytest.mark.usefixtures("setup")
class TestCases:
    # Login happens automatically using fixtures..!!![for all the forms]
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lang = Language(self.driver, self.wait)
        self.cog = CognitiveSkills(self.driver, self.wait)
        self.tass = Assessment(self.driver, self.wait)
        self.cas = Carrier(self.driver, self.wait)
        self.sup = Signup(self.driver, self.wait)
        self.wcl = Welcome(self.driver, self.wait)
        self.per = Personaldetails(self.driver, self.wait)
        self.job = JobRole(self.driver, self.wait)
        self.prj = Projects(self.driver, self.wait)
        self.edu = Education(self.driver, self.wait)

    # def test_signUp(self): BCZ of  Line 25
    #     self.sup.sign_up(firstname, lastname, email, phone_no, dob, gender, location, password, confirm_password)

    def test_welcome_page(self):
        self.wcl.welcomepage()

    def test_personal_details(self):
        for i in range(1):
            self.per.personaldetails(firstname, lastname, date, year[i], location[i], headline, linkdin)

    def test_jobrole(self):
        for i in range(3):
            self.job.addcompany(i, companyname[i], jobtype[i], experience[i], organization[i], based[i], designation[i], managementlevel[i], location[i], functionalarea[i], skill[i], expertise[i], year[i], year[i+1], startsalary[i], endsalary[i])
            self.job.next()

    def test_projects(self):
        self.prj.edit_profile()
        self.prj.click_projectdashboard()
        for j in range(3):
            self.prj.project(firstname, year[j], year[j+1], linkdin, description[j], skill[j], j, description[j])
        self.prj.next()

    @pytest.mark.education
    def test_education(self):
        self.edu.edit_profile()
        self.edu.click_educationdashboard()
        for i in range(3):
            self.edu.education(degree[i], university[i], location[i], cgpa[i], year[i], year[i+1], description[i], description[i+1])
        self.edu.next()

    def test_languages(self):
        for i in range(len(language)):
            self.lang.language(language[i], proficiency[i])
        self.lang.next()

    def test_cognitive_skills(self):
        self.cog.cognitive()

    def test_carrier(self):
        self.cas.carrier()

    def test_assessment(self):
        self.tass.assessment()



