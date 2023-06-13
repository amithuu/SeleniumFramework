import pytest
from pages.Languages_page import Language
from pages.Cognitiveskills import CognitiveSkills
from pages.Assessment_page import Assessment
from pages.Carriersummary_page import Carrier

language = ["kannada", "english", "hindi"]
proficiency = ["beg", "adv", "inter"]

@pytest.mark.usefixtures("setup")
class TestCases:
    # Login happens automatically using fixtures..!!!

    # Languages from edit profile!!
    def test_languages(self):
        # click on language button from edit profile page
        """Languages"""
        lg = Language(self.driver, self.wait)
        for i in range(len(language)):

            lg.location_button()
            # Language Drop Down
            lg.lang_drop(language[i])
            # Proficiency
            lg.profiency(proficiency[i])
            # Add + Button
            lg.add_button()
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
        # cg.page_scroll()
        cg.save()
        cg.next()
    def test_assessment(self):

        ta = Assessment(self.driver, self.wait)
        ta.dashboard()
        ta.assessment()
        ta.page_scroll()
        ta.checkbox()
        ta.answer()
    def test_carrier(self):

        ca = Carrier(self.driver, self.wait)
        ca.carrier()
        ca.save()
















