import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys,ActionChains

email = "autotest64@g.co"
password = "New@1234"

class FrameWork():

    def frameworkdemo(self):

        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://test-talentplace.vercel.app/login")
        driver.maximize_window()

        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

        # Going to Dash Board
        dashboard = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Dashboard']")))
        dashboard.click()
        time.sleep(3)

        # Click on edit profile
        edit_profile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
        edit_profile.click()

        # Click on Languages
        language = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Languages']")))
        language.click()

        lang = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class=' css-1yfdfck-control']//input")))
        lang.click()
        time.sleep(2)
        lang.send_keys("k")
        time.sleep(2)

        search_lang = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//*[@id='react-select-2-listbox']")))

        for langua in search_lang:
            print(langua)


ref = FrameWork()
ref.frameworkdemo()