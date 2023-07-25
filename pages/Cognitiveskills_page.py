import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.Languages_page import Language


class CognitiveSkills(Language):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # locators
    COGNITIVESKILL_EDITPROFILE = "//*[text()='Cognitive Skills']"
    COGNITIVE_SKILL_CHECKBOX = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[{s}]//span[1]"
    COGNITIVE_SKILL_SLIDER = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[{s}]//div[@role='slider']"

    """GETTERS"""
    def get_cognitiveskill_editprofile(self):
        return self.element_to_click(By.XPATH, self.COGNITIVESKILL_EDITPROFILE)

    """SETTERS"""
    def click_cognitiveskill_editprofile(self):
        self.get_cognitiveskill_editprofile().click()

    def select_cognitive_skill(self):
        time.sleep(1)
        for s in range(1, 7):
            self.driver.find_element(By.XPATH, f"//*[@id='root']/div/div[2]/div[2]/div/div/div/div[{s}]//span[1]").click()
            slid = self.element_to_click(By.XPATH, f"//*[@id='root']/div/div[2]/div[2]/div/div/div/div[{s}]//div[@role='slider']")
            ActionChains(self.driver).move_to_element(slid).pause(1).click_and_hold(slid).move_by_offset((35 * (s*2)), 0).release().perform()

    def cognitive(self):
        self.click_cognitiveskill_editprofile()
        self.select_cognitive_skill()
        self.save()
