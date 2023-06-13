import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.Basedriver import BaseDriver


class Assessment(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    def assessment(self):
        button = self.element_to_click(By.XPATH, "//*[text()='Take Assessment']")
        button.click()
        time.sleep(2)

    def checkbox(self):
        # Click on check Box
        check_box = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[2]/div[1]//span")))
        check_box.click()
        # Start Test
        start_test = self.wait.until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[2]/div[1]/div/div[3]//button")))
        start_test.click()

    def answer(self):
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
        time.sleep(2)
