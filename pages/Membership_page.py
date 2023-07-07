import time
from base.Basedriver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class Membership(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locators
    MEMBERSHIP_DASHBOARD = "//p[text()='Membership']"
    PLAN = "//*[@id='root']/div[2]/div[2]/div/div[2]/div[{i}]//button"
    NAME = "//form/div/div/div[1]//input"
    COUNTRY = "//form/div/div/div[2]//input"
    STATE = "//form/div/div/div[3]//input"
    CITY = "//form/div/div/div[4]//input"
    STREET = "//form/div/div/div[5]//input"
    ZIP_CODE = "//form/div/div/div[6]//input"
    PROCEED_BUTTON = "//button[text()='Proceed']"
    SUCCESS = "//a[text()='Success']"
    SUBSCRIBE_BUTTON = "//*[@type='submit' and @id='submit-button']"
    CLOSE_TAB = "//button[text()='Close this Tab']"
    REFRESH = "//*[text()='Refresh']"
    MORE_SERVICES = "//*[@id='root']/div[2]/div[2]/div/div[3]/div/div/label[{i}]/span[1]"
    BUY_NOW = "//*[@id='root']/div[2]/div[2]/div/div[3]/div[{i}]//button[1]"
    ENQUIRE_NOW = "//*[@id='root']/div[2]/div[2]/div/div[3]/div[{i}]//button[2]"

    """GETTERS"""
    def get_membership_dashboard(self):
        return self.element_to_click(By.XPATH, self.MEMBERSHIP_DASHBOARD)

    def get_plan(self, plan):
        if plan == "Trail":
            return self.element_to_click(By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div[2]/div[1]//button")
        if plan == "Monthly":
            return self.element_to_click(By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div[2]/div[2]//button")
        elif plan == "Quarterly":
            return self.element_to_click(By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div[2]/div[3]//button")
        elif plan == "Year":
            return self.element_to_click(By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div[2]/div[4]//button")

    def get_professionalservice(self, professionalservice, servicetype):
        if professionalservice == "Fresher Resume Writing":
            if servicetype == "Buynow":
                return self.element_to_click(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[3]/div[1]//button[1]")
            else:
                return self.element_to_click(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[3]/div[1]//button[2]")

        if professionalservice == "Experience Resume Writing":
            if servicetype == "Buynow":
                return self.element_to_click(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[3]/div[2]//button[1]")
            else:
                return self.element_to_click(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[3]/div[2]//button[2]")

        if professionalservice == "Linkdin Optimization":
            if servicetype == "Buynow":
                return self.element_to_click(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[3]/div[3]//button[1]")
            else:
                return self.element_to_click(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[3]/div[3]//button[2]")

        if professionalservice == "What Job Fits Me":
            if servicetype == "Buynow":
                return self.element_to_click(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[3]/div[4]//button[1]")

    def get_name(self):
        return self.element_to_click(By.XPATH, self.NAME)

    def get_country(self):
        return self.element_to_click(By.XPATH, self.COUNTRY)

    def get_state(self):
        return self.element_to_click(By.XPATH, self.STATE)

    def get_city(self):
        return self.element_to_click(By.XPATH, self.CITY)

    def get_street(self):
        return self.element_to_click(By.XPATH, self.STREET)

    def get_zipcode(self):
        return self.element_to_click(By.XPATH, self.ZIP_CODE)

    def get_proceedbutton(self):
        return self.element_to_click(By.XPATH, self.PROCEED_BUTTON)

    def get_successlink(self):
        return self.element_to_click(By.XPATH, self.SUCCESS)

    def get_subscribe(self):
        return self.element_to_click(By.XPATH, self.SUBSCRIBE_BUTTON)

    def get_closetab(self):
        return self.element_to_click(By.XPATH, self.CLOSE_TAB)

    def get_refresh(self):
        return self.element_to_click(By.XPATH, self.REFRESH)

    """SETTERS"""
    def click_membershipdashboard(self):
        self.get_membership_dashboard().click()

    def click_plan(self, plan):
        self.get_plan(plan).click()

    def enter_name(self, name):
        self.get_name().click()
        self.get_name().send_keys(name)
        self.get_name().send_keys(Keys.TAB)

    def enter_country(self, country):
        self.get_country().click()
        self.get_country().send_keys(country)
        self.get_country().send_keys(Keys.ARROW_DOWN)
        self.get_country().send_keys(Keys.ENTER)

    def enter_state(self, state):
        self.get_state().click()
        self.get_state().send_keys(state)
        self.get_state().send_keys(Keys.ARROW_DOWN)
        self.get_state().send_keys(Keys.ENTER)

    def enter_city(self, city):
        self.get_city().click()
        self.get_city().send_keys(city)
        self.get_city().send_keys(Keys.TAB)

    def enter_street(self, street):
        self.get_street().click()
        self.get_street().send_keys(street)
        self.get_street().send_keys(Keys.TAB)

    def enter_zipcode(self, zipcode):
        self.get_zipcode().click()
        self.get_zipcode().send_keys(zipcode)
        self.get_zipcode().send_keys(Keys.TAB)

    def click_proceed(self):
        self.get_proceedbutton().click()

    def click_successlink(self):
        self.get_successlink().click()

    def click_subscribe(self):
        self.get_subscribe().click()

    def click_closetab(self):
        self.get_closetab().click()

    def click_refresh(self):
        self.get_refresh().click()

    def click_professionalservice(self, professionalservice, servicetype):
        self.get_professionalservice(professionalservice, servicetype).click()

    def membership(self, plan, user, name, country, state, city, street, zipcode, membership_type, professionalservice, servicetype):
        self.click_membershipdashboard()
        time.sleep(2)
        self.page_end()
        time.sleep(2)
        parent_wind = self.driver.current_window_handle

        if membership_type == "Resume Builder":
            if user == "new":
                self.click_plan(plan)
                time.sleep(2)
                self.enter_name(name)
                self.enter_country(country)
                self.enter_state(state)
                self.enter_city(city)
                self.enter_street(street)
                self.enter_zipcode(zipcode)
                self.click_proceed()
                time.sleep(5)

                all_handles = self.driver.window_handles
                for handle in all_handles:
                    if handle != parent_wind:
                        self.driver.switch_to.window(handle)
                        self.page_end()
                        time.sleep(5)
                        if user == "new":
                            self.click_successlink()
                            time.sleep(2)
                        self.click_subscribe()
                        time.sleep(3)
                        self.click_closetab()
                        break
                self.driver.switch_to.window(parent_wind)

                self.click_refresh()
                for i in range(4):
                    self.driver.refresh()
                    time.sleep(3)

            elif user == "old":
                self.click_plan(plan)
                time.sleep(5)

                all_handles = self.driver.window_handles
                for handle in all_handles:
                    if handle != parent_wind:
                        self.driver.switch_to.window(handle)
                        self.page_end()
                        time.sleep(3)
                        self.click_subscribe()
                        time.sleep(3)
                        self.click_closetab()
                        time.sleep(2)
                        break
                self.driver.switch_to.window(parent_wind)

                self.click_refresh()
                for i in range(4):
                    self.driver.refresh()
                    time.sleep(3)

        elif membership_type == "Professional Service":
            self.click_professionalservice(professionalservice, servicetype)
            time.sleep(2)
            if servicetype == "Buynow":
                self.enter_name(name)
                self.enter_country(country)
                self.enter_state(state)
                self.enter_city(city)
                self.enter_street(street)
                self.enter_zipcode(zipcode)
                self.click_proceed()
                time.sleep(5)

                all_handles = self.driver.window_handles
                for handle in all_handles:
                    if handle != parent_wind:
                        self.driver.switch_to.window(handle)
                        self.page_end()
                        time.sleep(5)
                        if user == "new":
                            self.click_successlink()
                            time.sleep(2)
                        self.click_subscribe()
                        time.sleep(3)
                        self.click_closetab()
                        break
                self.driver.switch_to.window(parent_wind)
