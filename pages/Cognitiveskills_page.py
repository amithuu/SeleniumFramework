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
    COGNITIVESKILL_DASHBOARD = "//*[text()='Cognitive Skills']"

    """GETTERS"""
    def get_cognitiveskilldashboard(self):
        return self.element_to_click(By.XPATH, self.COGNITIVESKILL_DASHBOARD)

    """SETTERS"""
    def click_cognitiveskilldashboard(self):
        self.get_cognitiveskilldashboard().click()

    def cognitive(self):
        time.sleep(2)
        """Cognitive skills"""
        for s in range(1, 7):
            self.driver.find_element(By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div/div/div/div[{s}]//span[1]").click()
            slid = self.element_to_click(By.XPATH, f"//*//*[@id='root']/div[2]/div[2]/div/div/div/div/div[{s}]//div[@role='slider']")
            ActionChains(self.driver).move_to_element(slid).pause(1).click_and_hold(slid).move_by_offset((35 * s), 0).release().perform()
            time.sleep(1)
        self.save()
        time.sleep(3)
        self.next()

