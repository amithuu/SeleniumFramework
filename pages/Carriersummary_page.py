import time
from selenium.webdriver.common.by import By
from pages.Languages_page import Language


class Carrier(Language):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    carriersummary_editprofile = "//*[text() = 'Career Summary']"
    generate_suggestion = "//button[text()='Generate Suggestions']"
    add_suggestion = "//div[@id='root']/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div{a}//button"

    """GETTERS"""
    def get_carriersummary_editprofile(self):
        return self.element_to_click(By.XPATH, self.carriersummary_editprofile)

    def get_generatesuggestion(self):
        return self.element_to_click(By.XPATH, self.generate_suggestion)

    def get_add_suggestion(self, a):
        # return self.element_to_click(By.XPATH, f"//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div[{a}]//button")
        return self.element_to_click(By.XPATH, f"//div[@role='group']/div/div[2]/div/div/div[{a}]//button")

    """SETTERS"""
    def click_carriersummary_editprofiles(self):
        self.get_carriersummary_editprofile().click()
        time.sleep(1)

    def click_generatesuggestion(self):
        self.get_generatesuggestion().click()
        time.sleep(12)

    def click_suggestion(self):
        for a in range(1, 5):
            self.get_add_suggestion(a).click()
            time.sleep(1)

    def carrier(self):
        self.click_carriersummary_editprofiles()
        self.click_generatesuggestion()
        self.click_suggestion()
        self.save_simple()
