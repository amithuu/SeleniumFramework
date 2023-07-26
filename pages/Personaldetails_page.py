import time
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from base.Basedriver import BaseDriver
from selenium.webdriver.common.by import By


class Personaldetails(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    personaldetails_editprofiles = "//*[text()='Personal Details']"
    firstname = "first-name"
    lastname = "lastName"
    gender = "//*[@id = 'root']/div/div[2]/div[2]/div/div/div[2]/div[1]//input"
    gender_onboarding = "//*[@id = 'root']/div[2]/div/div/div/div/div[2]/div[1]//input"

    gender_list = "//*[@id ='root']/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[2]//span//li/div"
    gender_list_onboarding = "//*[@id ='root']/div[2]//div/div/div[2]/div[1]/div/div/div[2]//span//li/div"

    dob = "//*[@name='dob']"

    currency = "//*[@id = 'root']/div/div[2]/div[2]/div/div/div[2]/div[3]//input"
    currency_onboarding = "//*[@id = 'root']/div[2]/div/div/div/div/div[2]/div[3]//input"

    currency_list = "//*[@id = 'root']/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[2]//span//li/div"
    currency_list_onboarding = "//*[@id = 'root']/div[2]//div/div/div[2]/div[3]/div/div/div[2]//span//li/div"

    # month = "//*[@id = 'root']/div[2]/div[2]/div/div/div[1]/div[3]/div[2]/div//select"
    month = "//*[@id = 'root']/div/div[2]/div[2]/div/div/div[2]/div[4]//select"
    month_onboarding = "//*[@id = 'root']/div[2]/div/div/div/div/div[2]/div[4]//select"

    year = "//input[@Placeholder='Year']"

    iam_fresher_onboarding = "//*[@id = 'root']/div[2]/div/div/div/div/div[2]/div[4]/div/label/input"
    iam_fresher = "//*[@id = 'root']/div/div[2]/div[2]/div/div/div[2]/div[4]/div/label//span[1]"

    location = "//*[@placeholder ='Search Location']"

    location_list = "//*[@id ='root']/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]//ul/li"
    location_list_onboarding = "//*[@id ='root']/div[2]//div/div/div[1]/div/div/div[2]//ul/li"

    socialmedia = "//*[@id ='root']/div/div[2]/div[2]/div/div/div[3]//button"
    socialmedia_onboarding = "//*[@id ='root']/div[2]//div/div/div[3]//button"

    socilamedia_twitter = "socialMedia.twitter"
    socilamedia_linkdin = "socialMedia.linkedin"
    socilamedia_instagram = "socialMedia.instagram"
    socilamedia_facebook = "socialMedia.facebook"
    socilamedia_github = "socialMedia.github"
    socilamedia_dribble = "socialMedia.dribble"

    """GETTERS"""

    def get_personaldetailsdashboard(self):
        return self.element_to_click(By.XPATH, self.personaldetails_editprofiles)

    def get_firstname(self):
        return self.element_to_click(By.ID, self.firstname)

    def get_lastname(self):
        return self.element_to_click(By.NAME, self.lastname)

    def get_location(self):
        return self.element_to_click(By.XPATH, self.location)

    def get_locationlist(self):
        return self.presence_of_all_element(By.XPATH, self.location_list)

    def get_locationlist_onboarding(self):
        return self.presence_of_all_element(By.XPATH, self.location_list_onboarding)

    def get_gender(self):
        return self.element_to_click(By.XPATH, self.gender)

    def get_gender_onboarding(self):
        return self.element_to_click(By.XPATH, self.gender_onboarding)

    def get_genderlist(self):
        return self.presence_of_all_element(By.XPATH, self.gender_list)

    def get_genderlist_onboarding(self):
        return self.presence_of_all_element(By.XPATH, self.gender_list_onboarding)

    def get_dob(self):
        return self.element_to_click(By.XPATH, self.dob)

    def get_iam_fresher_onboarding(self):
        return self.element_to_click(By.XPATH, self.iam_fresher_onboarding)

    def get_iam_fresher(self):
        return self.element_to_click(By.XPATH, self.iam_fresher)

    def get_currency(self):
        return self.element_to_click(By.XPATH, self.currency)

    def get_currency_onboarding(self):
        return self.element_to_click(By.XPATH, self.currency_onboarding)

    def get_currencylist(self):
        return self.presence_of_all_element(By.XPATH, self.currency_list)

    def get_currencylist_onboarding(self):
        return self.presence_of_all_element(By.XPATH, self.currency_list_onboarding)

    def get_month(self):
        return self.element_to_click(By.XPATH, self.month)

    def get_month_onboarding(self):
        return self.element_to_click(By.XPATH, self.month_onboarding)

    def get_year(self):
        return self.element_to_click(By.XPATH, self.year)

    def get_socialmedia(self):
        return self.element_to_click(By.XPATH, self.socialmedia)

    def get_socialmedia_onboarding(self):
        return self.element_to_click(By.XPATH, self.socialmedia_onboarding)

    def get_socialmedia_linkdin(self):
        return self.element_to_click(By.NAME, self.socilamedia_linkdin)

    def get_socialmedia_twitter(self):
        return self.element_to_click(By.NAME, self.socilamedia_twitter)

    def get_socialmedia_instagram(self):
        return self.element_to_click(By.NAME, self.socilamedia_instagram)

    def get_socialmedia_dribble(self):
        return self.element_to_click(By.NAME, self.socilamedia_dribble)

    def get_socialmedia_facebook(self):
        return self.element_to_click(By.NAME, self.socilamedia_facebook)

    def get_socialmedia_github(self):
        return self.element_to_click(By.NAME, self.socilamedia_github)

    """SETTERS"""

    def click_personaldetailsdashboard(self):
        self.get_personaldetailsdashboard().click()

    def enter_firstname(self, firstname):
        self.get_firstname().click()
        self.get_firstname().send_keys(Keys.CONTROL + "a")
        self.get_firstname().send_keys(firstname)

    def enter_lastname(self, lastname):
        self.get_lastname().click()
        self.get_lastname().send_keys(Keys.CONTROL + "a")
        self.get_lastname().send_keys(lastname)

    def select_location_onboarding(self, location_name):
        self.get_location().click()
        time.sleep(1)
        self.get_location().send_keys(location_name)
        time.sleep(1)

        select_location = self.get_locationlist_onboarding()
        for locations in select_location:
            if location_name in locations.text.casefold():
                locations.click()
                break

    def select_location(self, location_name):
        self.get_location().click()
        time.sleep(1)
        self.get_location().send_keys(Keys.CONTROL + "a")
        self.get_location().send_keys(Keys.BACK_SPACE)
        self.get_location().send_keys(location_name)
        time.sleep(1)

        select_location = self.get_locationlist()
        for locations in select_location:
            if location_name in locations.text.casefold():
                locations.click()
                break

    def enter_gender_onboarding(self, gender):
        self.get_gender_onboarding().click()
        self.get_gender_onboarding().send_keys(gender)
        time.sleep(1)

        select_gender = self.get_genderlist_onboarding()
        for genders in select_gender:
            if gender in genders.text.casefold():
                genders.click()
                break

    def enter_gender(self, gender):
        self.get_gender().click()
        self.get_gender().send_keys(gender)
        time.sleep(1)

        select_gender = self.get_genderlist()
        for genders in select_gender:
            if gender in genders.text.casefold():
                genders.click()
                break

    def enter_dob(self, dob):
        self.get_dob().click()
        self.get_dob().send_keys(dob)
        self.get_dob().send_keys(Keys.TAB)

    def click_iam_fresher_onboarding(self):
        self.get_iam_fresher_onboarding().click()
        time.sleep(1)

    def click_iam_fresher(self):
        self.get_iam_fresher().click()
        time.sleep(1)

    def enter_currency(self, currency):
        self.get_currency().click()
        self.get_currency().send_keys(currency)

        currency_list = self.get_currencylist()

        for currency_lis in currency_list:
            if currency in currency_lis.text.casefold():
                currency_lis.click()
                break

    def enter_currency_onboarding(self, currency):
        self.get_currency_onboarding().click()
        self.get_currency_onboarding().send_keys(currency)

        currency_list = self.get_currencylist_onboarding()

        for currency_lis in currency_list:
            if currency in currency_lis.text.casefold():
                currency_lis.click()
                break

    def enter_experience_onboarding(self, month, year):
        self.get_month_onboarding().click()
        select = Select(self.get_month_onboarding())
        select.select_by_visible_text(month)
        time.sleep(1)

        self.get_year().click()
        self.get_year().send_keys(Keys.CONTROL + "a")
        self.get_year().send_keys(year)

    def enter_experience(self, month, year):
        self.get_month().click()
        select = Select(self.get_month())
        select.select_by_visible_text(month)
        time.sleep(1)

        self.get_year().click()
        self.get_year().send_keys(Keys.CONTROL + "a")
        self.get_year().send_keys(year)

    def enter_socialmedia(self, user, socialmedia, socialmedialink):
        if user == "new":
            self.get_socialmedia_onboarding().click()

            if socialmedia == "twitter":
                # def enter_socilamediatwitter(socialmedialink):
                #     self.get_socialmedia_twitter().click()
                self.get_socialmedia_twitter().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_twitter().send_keys(socialmedialink)

            elif socialmedia == "instagram":
                # def enter_socilamediainstagram(socialmedialink):
                #     self.get_socialmedia_instagram().click()
                self.get_socialmedia_instagram().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_instagram().send_keys(socialmedialink)

            elif socialmedia == "linkdin":
                # def enter_socilamedialinkdin(socialmedialink):
                #     self.get_socialmedia_linkdin().click()
                self.get_socialmedia_linkdin().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_linkdin().send_keys(socialmedialink)

            elif socialmedia == "facebook":
                # def enter_socilamediafacebook(socialmedialink):
                #     self.get_socialmedia_facebook().click()
                self.get_socialmedia_facebook().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_facebook().send_keys(socialmedialink)

            elif socialmedia == "dribble":
                # def enter_socilamediadribble(socialmedialink):
                #     self.get_socialmedia_dribble().click()
                self.get_socialmedia_dribble().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_dribble().send_keys(socialmedialink)

            elif socialmedia == "github":
                # def enter_socilamediagithub(socialmedialink):
                #     self.get_socialmedia_github().click()
                self.get_socialmedia_github().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_github().send_keys(socialmedialink)

        if user == "old":
            self.get_socialmedia().click()

            if socialmedia == "twitter":
                # def enter_socilamediatwitter(socialmedialink):
                #     self.get_socialmedia_twitter().click()
                self.get_socialmedia_twitter().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_twitter().send_keys(socialmedialink)

            elif socialmedia == "instagram":
                # def enter_socilamediainstagram(socialmedialink):
                #     self.get_socialmedia_instagram().click()
                self.get_socialmedia_instagram().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_instagram().send_keys(socialmedialink)

            elif socialmedia == "linkdin":
                # def enter_socilamedialinkdin(socialmedialink):
                #     self.get_socialmedia_linkdin().click()
                self.get_socialmedia_linkdin().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_linkdin().send_keys(socialmedialink)

            elif socialmedia == "facebook":
                # def enter_socilamediafacebook(socialmedialink):
                #     self.get_socialmedia_facebook().click()
                self.get_socialmedia_facebook().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_facebook().send_keys(socialmedialink)

            elif socialmedia == "dribble":
                # def enter_socilamediadribble(socialmedialink):
                #     self.get_socialmedia_dribble().click()
                self.get_socialmedia_dribble().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_dribble().send_keys(socialmedialink)

            elif socialmedia == "github":
                # def enter_socilamediagithub(socialmedialink):
                #     self.get_socialmedia_github().click()
                self.get_socialmedia_github().send_keys(Keys.CONTROL + "a")
                self.get_socialmedia_github().send_keys(socialmedialink)

    def personaldetails(self, user, firstname, lastname, location, gender, dob, currency, month, year, socialmedia, socialmedialink):

        if user == "new":
            self.enter_firstname(firstname)
            self.enter_lastname(lastname)
            self.select_location_onboarding(location)
            self.enter_gender_onboarding(gender)
            self.enter_dob(dob)
            self.enter_currency_onboarding(currency)
            self.enter_experience_onboarding(month, year)
            self.click_iam_fresher_onboarding()
            self.enter_socialmedia(user, socialmedia, socialmedialink)
            self.save_next()

        elif user == "old":
            self.click_personaldetailsdashboard()
            self.enter_firstname(firstname)
            self.enter_lastname(lastname)
            self.select_location(location)
            self.enter_gender(gender)
            self.enter_dob(dob)
            self.enter_currency(currency)
            self.enter_experience(month, year)
            self.click_iam_fresher()
            self.enter_socialmedia(user, socialmedia, socialmedialink)
            self.save()
            self.backto_menu()
