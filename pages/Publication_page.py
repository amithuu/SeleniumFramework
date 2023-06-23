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
    publication_dashboard = "//*[text()='Publication']"
    add_publication = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"
    publisher_id = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[2]//input"
    publication_url = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[2]//input"

    """GETTERS"""
    def get_publicationdashboard(self):
        return self.element_to_click(By.XPATH, self.publication_dashboard)

    def get_addpublication(self):
        return self.element_to_click(By.XPATH, self.add_publication)

    def get_publisherid(self):
        return self.element_to_click(By.XPATH, self.publisher_id)

    def get_publicationurl(self):
        return self.element_to_click(By.XPATH, self.publication_url)

    """SETTERS"""
    def click_publicationdashboard(self):
        self.get_publicationdashboard().click()

    def click_addpublication(self):
        self.get_addpublication().click()

    def enter_publisherid(self, id):
        self.get_publisherid().click()
        self.get_publisherid().send_keys(id)
        self.get_publisherid().send_keys(Keys.TAB)

    def enter_publicationurl(self, url):
        self.get_publicationurl().click()
        self.get_publicationurl().send_keys(url)
        self.get_publicationurl().send_keys(Keys.TAB)

    def publication(self, id, url):
        self.click_publicationdashboard()
        self.click_addpublication()
        self.enter_publisherid(id)
        self.enter_publicationurl(url)

