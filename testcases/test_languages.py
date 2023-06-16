import pytest
from pages.Assessment_page import Assessment
from pages.Carriersummary_page import Carrier
from pages.Cognitiveskills_page import CognitiveSkills
from pages.Languages_page import Language
from pages.SignUp_page import Signup

# Variables
k = 3
language = ["kannada", "english", "hindi"]
proficiency = ["beg", "adv", "inter"]
firstname = "test"
lastname = "talentPlace"
email = f"prod{k}@g.co"
phone_no = f"+1 {k}45848445"
location = "Bangalore"
dob = "25031999"
gender = "male"
password = "New@1234"
confirm_password = "New@1234"


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

    # def test_signUp(self): BCZ of  Line 25
    #     self.sup.sign_up(firstname, lastname, email, phone_no, dob, gender, location, password, confirm_password)

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


