import pytest
from pages.Assessment_page import Assessment
from pages.Carriersummary_page import Carrier
from pages.Cognitiveskills_page import CognitiveSkills
from pages.Languages_page import Language
from pages.SignUp_page import Signup
from pages.Welcome_page import Welcome
from pages.Personal_details_page import Personaldetails
from pages.Jobrole_page import JobRole

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
month = ["jan", "feb", "march"]
year = ["1999", "2020", "2010"]
endyear = ["2000", "2021", "2022"]
endmonth = ["april", "may", "june"]
designation = ["Developer", "Automation", "application"]
managementlevel = ["jun", "sen", "mid"]
functionalarea = ["development", "human", "marketing"]
skill = ["java", "python", "c prog"]
expertise = ["beg", "skil", "expert"]
startsalary = ["12", "3213", "214"]
endsalary = ["2143312", "2136832", "812765"]
linkdin = "https://www.linkedin.com/in/amith-kulkarni-1326241b4"
headline = "Automation Developer"
firstname = "Amith"
lastname = "talentPlace"


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

    # def test_signUp(self): BCZ of  Line 25
    #     self.sup.sign_up(firstname, lastname, email, phone_no, dob, gender, location, password, confirm_password)

    def test_welcome_page(self):
        self.wcl.welcomepage()

    def test_personal_details(self):
        for i in range(1):
            self.per.personaldetails(firstname, lastname, date, year[i], location[i], headline, linkdin)

    def test_jobrole(self):
        self.job.edit_profile()
        self.job.experience()
        for i in range(3):
            self.job.addcompany(i, companyname[i], jobtype[i], experience[i], organization[i], based[i], designation[i], managementlevel[i], location[i], functionalarea[i], skill[i], expertise[i], month[i], year[i], endyear[i], endmonth[i], startsalary[i], endsalary[i])

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



