import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver


class Publication(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locator
    publication_editprofiles = "//*[text()='Publication']"

    publication_title = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[1]/div[1]//input"

    add_another_publication = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div//button"

    publisher_id = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[1]/div[2]//input"
    publication_date = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[1]/div[3]//input"
    publication_url = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[1]/div[4]//input"

    add_author = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[2]//button"
    author_title = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[2]//form/div/div[1]/div/div/select"
    author_name = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[2]//form/div/div[1]//input"
    link = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[2]//form/div/div[2]//input"
    delete_author = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[2]//form/div/div[2]//button"

    description = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[3]//p"

    save = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[4]//button[2]"

    """GETTERS"""
    def get_publication_editprofiles(self):
        return self.element_to_click(By.XPATH, self.publication_editprofiles)

    def get_add_another_publication(self):
        return self.element_to_click(By.XPATH, self.add_another_publication)

    def get_publication_title(self):
        return self.element_to_click(By.XPATH, self.publication_title)

    def get_publisher_id(self):
        return self.element_to_click(By.XPATH, self.publisher_id)

    def get_publication_date(self):
        return self.element_to_click(By.XPATH, self.publication_date)

    def get_publication_url(self):
        return self.element_to_click(By.XPATH, self.publication_url)

    def get_add_author(self):
        return self.element_to_click(By.XPATH, self.add_author)

    def get_author_title(self):
        return self.element_to_click(By.XPATH, self.author_title)

    def get_author_name(self):
        return self.element_to_click(By.XPATH, self.author_name)

    def get_link(self):
        return self.element_to_click(By.XPATH, self.link)

    def get_description(self):
        return self.element_to_click(By.XPATH, self.description)

    def get_save_button(self):
        return self.element_to_click(By.XPATH, self.save)

    """SETTERS"""
    def click_publication_editprofiles(self):
        self.get_publication_editprofiles().click()
        time.sleep(2)

    def enter_publication_title(self, title):
        self.get_publication_title().click()
        self.get_publication_title().send_keys(title)
        self.get_publication_title().send_keys(Keys.TAB)

    def click_add_another_publication(self):
        self.get_add_another_publication().click()

    def enter_publisher_id(self, id):
        self.get_publisher_id().click()
        self.get_publisher_id().send_keys(id)
        self.get_publisher_id().send_keys(Keys.TAB)

    def enter_publication_date(self, date):
        self.get_publication_date().click()
        self.get_publication_date().send_keys(date)

    def enter_publication_url(self, url):
        self.get_publication_url().send_keys(url)

    def click_add_author(self):
        self.get_add_author().click()
        time.sleep(3)

    def enter_author_title(self, title):
        self.get_author_title().click()
        self.select_options(self.get_author_title(), title)

    def enter_author_name(self, name):
        self.get_author_name().send_keys(name)

    def enter_link(self, link):
        self.get_link().send_keys(link)

    def enter_description(self, description):
        self.get_description().send_keys(description)

    def click_save_button(self):
        self.get_save_button().click()
        time.sleep(3)

    def publication(self, user, title, id, date, url, author_title, author_name, linkdin_link, publication_description):
        self.click_publication_editprofiles()

        if user == "new":
            self.enter_publication_title(title)
            self.enter_publisher_id(id)
            self.enter_publication_date(date)
            self.enter_publication_url(url)
            self.click_add_author()
            self.enter_author_title(author_title)
            self.enter_author_name(author_name)
            self.enter_link(linkdin_link)
            self.enter_description(publication_description)
            self.click_save_button()
            self.click_add_another_publication()

        elif user == "old":
            self.click_add_another_publication()
            self.enter_publication_title(title)
            self.enter_publication_title(title)
            self.enter_publisher_id(id)
            self.enter_publication_date(date)
            self.enter_publication_url(url)
            self.click_add_author()
            self.enter_author_title(author_title)
            self.enter_author_name(author_name)
            self.enter_link(linkdin_link)
            self.enter_description(publication_description)
            self.click_save_button()
