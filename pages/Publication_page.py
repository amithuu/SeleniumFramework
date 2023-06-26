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
    publication_title = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[1]//input"
    add_publication = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"
    publisher_id = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[2]//input"
    publication_date = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[1]//input"
    publication_url = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[2]//input"
    add_author = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]//button"
    author_title = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[1]/div[1]//select"
    author_name = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[1]/div[2]//input"
    link = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[2]//input"
    description = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[4]//p"
    save_publication = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/button"

    """GETTERS"""
    def get_publicationdashboard(self):
        return self.element_to_click(By.XPATH, self.publication_dashboard)

    def get_addpublication(self):
        return self.element_to_click(By.XPATH, self.add_publication)

    def get_publicationtitle(self):
        return self.element_to_click(By.XPATH, self.publication_title)

    def get_publisherid(self):
        return self.element_to_click(By.XPATH, self.publisher_id)

    def get_publicationdate(self):
        return self.element_to_click(By.XPATH, self.publication_date)

    def get_publicationurl(self):
        return self.element_to_click(By.XPATH, self.publication_url)

    def get_addauthor(self):
        return self.element_to_click(By.XPATH, self.add_author)

    def get_authortitle(self):
        return self.element_to_click(By.XPATH, self.author_title)

    def get_author_name(self):
        return self.element_to_click(By.XPATH, self.author_name)

    def get_link(self):
        return self.element_to_click(By.XPATH, self.link)

    def get_description(self):
        return self.element_to_click(By.XPATH, self.description)

    def get_savepublication(self):
        return self.element_to_click(By.XPATH, self.save_publication)

    """SETTERS"""
    def click_publicationdashboard(self):
        self.get_publicationdashboard().click()

    def enter_publicationtitle(self, title):
        self.get_publicationtitle().click()
        self.get_publicationtitle().send_keys(title)
        self.get_publicationtitle().send_keys(Keys.TAB)

    def click_addpublication(self):
        self.get_addpublication().click()

    def enter_publisherid(self, id):
        self.get_publisherid().click()
        self.get_publisherid().send_keys(id)
        self.get_publisherid().send_keys(Keys.TAB)

    def enter_publicationdate(self, date):
        self.get_publicationdate().click()
        self.get_publicationdate().send_keys(date)
        self.get_publicationdate().send_keys(Keys.TAB)

    def enter_publicationurl(self, url):
        self.get_publicationurl().click()
        self.get_publicationurl().send_keys(url)
        self.get_publicationurl().send_keys(Keys.TAB)

    def click_addauthor(self):
        self.get_addauthor().click()

    def enter_authortitle(self):
        self.get_authortitle().click()
        self.get_authortitle().send_keys(Keys.ARROW_DOWN)
        self.get_authortitle().send_keys(Keys.ENTER)
        self.get_authortitle().send_keys(Keys.TAB)

    def enter_authorname(self, name):
        self.get_author_name().click()
        self.get_author_name().send_keys(name)
        self.get_author_name().send_keys(Keys.TAB)

    def enter_link(self, link):
        self.get_link().click()
        self.get_link().send_keys(link)

    def enter_description(self, description):
        self.get_description().click()
        self.get_description().send_keys(description)

    def click_savepublication(self):
        self.get_savepublication().click()

    def publication(self, i, title, id, date, url, name, link, description):
        self.click_addpublication()
        self.enter_publicationtitle(title)
        self.enter_publisherid(id)
        self.enter_publicationdate(date)
        self.enter_publicationurl(url)
        self.click_addauthor()
        self.page_down()
        self.enter_authortitle()
        self.enter_authorname(name)
        self.enter_link(link)
        self.enter_description(description)
        self.click_savepublication()
        time.sleep(5)
        if i <= 1:
            self.next()
            self.back()
        else:
            self.next()




