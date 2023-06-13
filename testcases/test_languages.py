import pytest
from pages.Languages_page import Language
from pages.Cognitiveskills import CognitiveSkills
from pages.Assessment_page import Assessment
from pages.Carriersummary_page import Carrier

language = ["kannada", "english", "hindi"]
proficiency = ["beg", "adv", "inter"]


@pytest.mark.usefixtures("setup")
class TestCases:
    # Login happens automatically using fixtures..!!![for all the forms]

    def test_languages(self):
        # click on language button from edit profile page
        """Languages"""
        lg = Language(self.driver, self.wait)
        for i in range(len(language)):
            lg.language(language[i], proficiency[i])
            # Save
            lg.save()
            # Back
            lg.back()
            # Next
            lg.next()
        # Next
        lg.next()

    def test_cognitive_skills(self):
        cg = CognitiveSkills(self.driver, self.wait)
        cg.cognitive()
        cg.save()
        # cg.next()

    @pytest.mark.tryagain
    def test_assessment(self):
        ta = Assessment(self.driver, self.wait)
        ta.dashboard()
        ta.assessment()

    def test_carrier(self):
        ca = Carrier(self.driver, self.wait)
        ca.carrier()
        ca.save()


