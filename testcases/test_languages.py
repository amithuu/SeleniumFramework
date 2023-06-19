import pytest
from pages.Assessment_page import Assessment
from pages.Carriersummary_page import Carrier
from pages.Cognitiveskills_page import CognitiveSkills
from pages.Languages_page import Language
from pages.SignUp_page import Signup
from pages.Welcome_page import Welcome
from pages.Personal_details_page import Personaldetails
from pages.Experience_page import Experience

# Variables
language = ["kannada", "english", "hindi"]
proficiency = ["beg", "adv", "inter"]
location = ["bangalore", "delhi", "561203"]
companyname = ["IBM", "Google", "Cognizant"]
jobtype = ["full time", "intern", "part time", "freelanc", "contract"]
experience = ["Advanced Technologies", "IT Services", "Agri-business"]
organization = ["startup", "small", "mnc"]
based = ["product", "service", "both"]
linkdin = "https://www.linkedin.com/in/amith-kulkarni-1326241b4"
month = ["jan", "feb", "march"]
year = ["1999", "2020", "2010"]
dob = "25031999"
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
        self.exp = Experience(self.driver, self.wait)

    # def test_signUp(self): BCZ of  Line 25
    #     self.sup.sign_up(firstname, lastname, email, phone_no, dob, gender, location, password, confirm_password)

    def test_welcome_page(self):
        self.wcl.welcomepage()

    def test_personal_details(self):
        for i in range(1):
            self.per.personaldetails(firstname, lastname, dob, month[i], year[i], location[i], headline, linkdin)

    def test_experience(self):
        for i in range(3):
            self.exp.addcompany(companyname[i], jobtype[i], experience[i], organization[i], based[i])

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



