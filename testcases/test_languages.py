import pytest
from
from pages.Languages_page import Language
from pages.Cognitiveskills import CognitiveSkills
from pages.Assessment_page import Assessment
from pages.Carriersummary_page import Carrier

language = ["kannada", "english", "hindi"]
proficiency = ["beg", "adv", "inter"]


@pytest.mark.usefixtures("setup")
class TestCases:
    # Login happens automatically using fixtures..!!![for all the forms]
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lang = Language(self.driver, self.wait)
        self.cog = CognitiveSkills(self.driver, self.wait)
        self.tass = Assessment(self.driver, self.wait)
        self.cas = Carrier(self.driver, self.wait)

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
