import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.Basedriver import BaseDriver


class Assessment(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    assessment_button = "//*[text()='Take Assessment']"
    check_box = "//*[@id='root']/div/div[2]/div[1]/div[2]/div[1]//span[1]"
    start_test = "//*[@id='root']/div/div[2]/div[1]/div[2]/div[1]/div/div[3]//button"

    """GETTERS"""

    def get_assessment(self):
        return self.element_to_click(By.XPATH, self.assessment_button)

    def get_checkbox(self):
        return self.element_to_click(By.XPATH, self.check_box)

    def get_starttest(self):  # Start Test
        return self.element_to_click(By.XPATH, self.start_test)

    """ SETTERS"""

    def click_takeassessment(self):
        self.get_assessment().click()

    def click_checkbox(self):
        self.get_checkbox().click()

    def click_starttest(self):
        self.get_starttest().click()

    def click_answer(self):
        # Answers
        for i in range(1, 10):
            for j in range(1, 6):
                answer = self.element_to_click(By.XPATH, f"//*[@id='root']/div/div[2]/div[1]/div[2]/div[2]//p[{j}]")
                answer.click()
        # Click on submit
        submit = self.element_to_click(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[3]//button[2]")
        submit.click()
        time.sleep(15)
        # Click on view Report
        view_report = self.element_to_click(By.XPATH, "//*[@id='root']/div/div[2]//button")
        view_report.click()
        time.sleep(3)

    def assessment(self):
        self.click_takeassessment()
        self.page_down()
        self.click_checkbox()
        self.click_starttest()
        self.click_answer()
