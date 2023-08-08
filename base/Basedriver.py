import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class BaseDriver:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def page_scroll(self):
        page_length = self.driver.execute_script(
            "window.scrollTo(0, document.body,scrollHeight);var page_Length= document.body.scrollheight")
        match = False
        while match == False:
            lastCount = page_length
            time.sleep(2)
            page_length = self.driver.execute_script(
                "window.scrollTo(0, document.body,scrollHeight);var page_Length= document.body.scrollheight")
            if lastCount == page_length:
                match = True
        time.sleep(2)

    def save_simple(self):
        save = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(2)

    def save_refresh(self):
        save = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)

    def save_next(self):
        save = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save and Next']")))
        save.click()
        time.sleep(3)

    def save_after_refresh(self):
        save_after_refresh = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@data-rbd-droppable-id='droppable']/div[1]/div/div/button[1]")))
        save_after_refresh.click()
        self.page_end()
        self.save_simple()
        time.sleep(1)

    def back(self):
        back_to_company = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
        back_to_company.click()

    def next(self):
        next_ = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
        time.sleep(1)

    def dashboard(self):
        dashboard = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Dashboard']")))
        dashboard.click()
        time.sleep(2)

    def element_to_click(self, locator_id, path):
        element = self.wait.until(ec.element_to_be_clickable((locator_id, path)))
        return element

    def presence_of_all_element(self, locator_id, path):
        list_of_element = self.wait.until(ec.presence_of_all_elements_located((locator_id, path)))
        return list_of_element

    def page_end(self):
        self.driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.END)

    def page_down(self):
        self.driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)

    def page_up(self):
        self.driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)

    def copy_all(self):
        self.driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.CONTROL + "a")

    def page_back(self):
        self.driver.back()

    def edit_profile(self):
        edit_profile = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
        edit_profile.click()

    def experience_dashboard(self):
        experience = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Experience']")))
        experience.click()

    def javascript_link(self, path):
        image = self.driver.execute_script(f" return {path}")
        self.driver.execute_script("arguments[0].click();", image)
        time.sleep(5)

    def discard(self):
        discard = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Discard']")))
        discard.click()

    def select_options(self, path, text):
        author_title = Select(path)
        author_title.select_by_visible_text(text)

    def backto_menu(self):
        back_to_menu = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//a//button")))
        back_to_menu.click()
        time.sleep(1)

    def login(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        self.wait.until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys("autotest30@g.co")
        self.wait.until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys("New@1234")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)
