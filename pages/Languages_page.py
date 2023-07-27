import time
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver


class Language(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    language_editprofile = "//*[text()='Languages']"

    language_dropdown = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[2]/div[1]//input"
    language_dropdown_list = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[2]/div[1]//li/div"

    language_proficiency = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[2]/div[2]//input"
    language_proficiency_list = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[2]/div[2]//li/div"

    add_button = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[2]/div[2]//button"

    """GETTERS"""
    def get_language_editprofile(self):
        return self.element_to_click(By.XPATH, self.language_editprofile)

    def get_language_dropdown(self):
        return self.element_to_click(By.XPATH, self.language_dropdown)

    def get_language_dropdown_list(self):
        return self.presence_of_all_element(By.XPATH, self.language_dropdown_list)

    def get_proficiency(self):
        return self.element_to_click(By.XPATH, self.language_proficiency)

    def get_proficiency_list(self):
        return self.presence_of_all_element(By.XPATH, self.language_proficiency_list)

    def get_add_button(self):
        return self.element_to_click(By.XPATH, self.add_button)

    """SETTERS"""

    def click_language_editprofile(self):
        self.get_language_editprofile().click()

    def select_language_dropdown(self, language):
        self.get_language_dropdown().click()
        self.get_language_dropdown().send_keys(language)
        time.sleep(1)
        languages = self.get_language_dropdown_list()

        for lang in languages:
            if language in lang.text.casefold():
                lang.click()
                break

    def select_language_profiency(self, proficiency):
        self.get_proficiency().click()
        time.sleep(1)
        profcience = self.get_proficiency_list()

        for proficience in profcience:
            if proficiency in proficience.text.casefold():
                proficience.click()
                break

    def click_addbutton(self):
        self.get_add_button().click()

    def language(self, language, proficiency):
        self.click_language_editprofile()
        time.sleep(1)
        self.select_language_dropdown(language)
        self.select_language_profiency(proficiency)
        self.click_addbutton()
        self.save()
        self.backto_menu()
