import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

@pytest.fixture(scope="class")
def setup(request):

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # driver.get("https://test-talentplace.vercel.app/login")
    driver.get("https://www.talentplace.ai/login")
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    """ Login Page"""
    wait.until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys("prod2@g.co")
    wait.until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys("New@1234")
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
    time.sleep(3)

    # Going to Dash Board
    dashboard = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Dashboard']")))
    dashboard.click()
    time.sleep(3)

    # Click on edit profile
    edit_profile = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
    edit_profile.click()

    request.cls.driver = driver
    request.cls.wait = wait

    yield
    driver.close()
